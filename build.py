#!/usr/bin/env python3
"""
Static site generator for crawfordsmetaldetectorsreviews.co.uk
================================================================
Single source of truth: data/products.json
Every page is generated as a real static HTML file (real URLs — no JS routing),
with canonical tags, meta descriptions, Open Graph tags and JSON-LD schema.

Usage:
    python3 build.py            # regenerate the whole site into the repo root
Run sync.py first to refresh live stock data from crawfordsmd.com.
"""
import json, os, html, sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from content import REVIEWS, GUIDES, COMPARISONS, DISCLOSURE

DATA = json.load(open(os.path.join(ROOT, "data", "products.json"), encoding="utf-8"))
_rv = os.path.join(ROOT, "data", "reviews.json")
REVIEWS_FEED = json.load(open(_rv, encoding="utf-8")) if os.path.exists(_rv) else {"reviews": []}
_bp = os.path.join(ROOT, "data", "shop_blog.json")
SHOP_BLOG = json.load(open(_bp, encoding="utf-8")) if os.path.exists(_bp) else {"posts": []}

DOMAIN = "https://crawfordsmetaldetectorsreviews.co.uk"
TRACK = DATA["tracking_code"]
SHOP = DATA["shop_base"]
P = {p["slug"]: p for p in DATA["products"]}
PRODUCTS = sorted(DATA["products"], key=lambda x: x["rank"])
PLAT = DATA["platforms"]
STORE = DATA["store"]
TODAY = DATA.get("last_synced", str(date.today()))

def shop_url(path):
    # Affiliate tracking for the main site's affiliate report + UTMs for GA4 attribution
    return (f"{SHOP}{path}?tracking={TRACK}"
            "&utm_source=cmd-reviews&utm_medium=referral&utm_campaign=reviews-site")

def pct(score):
    return f"{round(float(score)/5*100)}%"

def esc(s):
    return html.escape(str(s), quote=True)

# ─────────────────────────────────────────────── shared chrome ──

SVG_DEFS = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="lg-tpstar" viewBox="0 0 24 24"><path fill="#00B67A" d="M24 9.2h-9.2L12 .5 9.2 9.2H0l7.5 5.3-2.9 8.9 7.4-5.5 7.4 5.5-2.9-8.9L24 9.2z"/><path fill="#005128" d="M16.5 16.5 12 17.9l4.5 3.5-2.9-8.9z" opacity=".9"/></symbol>
<symbol id="lg-google" viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></symbol>
<symbol id="lg-fb" viewBox="0 0 24 24"><path fill="#1877F2" d="M24 12a12 12 0 1 0-13.875 11.854v-8.385H7.078V12h3.047V9.356c0-3.007 1.792-4.668 4.533-4.668 1.312 0 2.686.234 2.686.234v2.953H15.83c-1.491 0-1.956.925-1.956 1.874V12h3.328l-.532 3.469h-2.796v8.385A12 12 0 0 0 24 12z"/><path fill="#fff" d="M16.671 15.469 17.203 12h-3.328V9.749c0-.949.465-1.874 1.956-1.874h1.513V4.922s-1.374-.234-2.686-.234c-2.741 0-4.533 1.661-4.533 4.668V12H7.078v3.469h3.047v8.385a12.09 12.09 0 0 0 3.75 0v-8.385h2.796z"/></symbol>
</defs></svg>"""

NAV_ITEMS = [
    ("/reviews/", "Reviews"),
    ("/comparisons/", "Comparisons"),
    ("/best/", "Best Of"),
    ("/guides/", "Blog"),
    ("/brands/", "Brands"),
    ("/customer-reviews/", "Customer Reviews"),
    ("/about/", "About"),
]

LOGO = "https://crawfordsmd.com/image/catalog/logo.png"

ORG_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Crawfords Metal Detectors",
    "url": DOMAIN,
    "logo": LOGO,
    "sameAs": [SHOP, "https://www.google.com/storepages?q=crawfordsmd.com&c=GB&v=19"],
    "telephone": "+44 1724 845608",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Unit 11 Weaver Court, Sawcliffe Industrial Park",
        "addressLocality": "Scunthorpe",
        "addressRegion": "North Lincolnshire",
        "postalCode": "DN15 8RN",
        "addressCountry": "GB",
    },
}

def crumb_schema(items):
    """items: list of (name, url_or_None)."""
    els = []
    for i, (name, url) in enumerate(items, 1):
        el = {"@type": "ListItem", "position": i, "name": name}
        if url:
            el["item"] = DOMAIN + url
        els.append(el)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": els}

def article_schema(title, desc, path, published, modified=None):
    return {"@context": "https://schema.org", "@type": "Article",
            "headline": title, "description": desc,
            "url": DOMAIN + path,
            "datePublished": published, "dateModified": modified or published,
            "author": {"@type": "Organization", "name": "Crawfords Metal Detectors", "url": DOMAIN},
            "publisher": {"@type": "Organization", "name": "Crawfords Metal Detectors", "logo": {"@type": "ImageObject", "url": LOGO}}}

def webpage_schema(title, desc, path):
    return {"@context": "https://schema.org", "@type": "WebPage",
            "name": title, "description": desc, "url": DOMAIN + path}

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def head(title, desc, path, extra_schema=None):
    schemas = [ORG_SCHEMA] + (extra_schema or [])
    ld = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
        for s in schemas
    )
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{DOMAIN}{path}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{DOMAIN}{path}">
<meta property="og:site_name" content="Crawfords Metal Detector Reviews">
<meta property="og:locale" content="en_GB">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@500;600;700;800&family=Jost:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<script type="text/javascript" src="//widget.trustpilot.com/bootstrap/v5/tp.widget.bootstrap.min.js" async></script>
<link rel="apple-touch-icon" href="/assets/favicon.png">
<link rel="mask-icon" href="/assets/favicon.svg" color="#015591">
<meta name="theme-color" content="#02273F">
<meta name="google-site-verification" content="NyYxwMlbTVVlpG095Ie__jzS1jGWYKq1DsL0DCcUuJE">
<!-- Google Consent Mode v2 — denied by default until the visitor consents (UK GDPR/PECR) -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  var cmdConsent = null;
  try {{ cmdConsent = localStorage.getItem('cmd_consent'); }} catch(e) {{}}
  gtag('consent', 'default', {{
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'analytics_storage': 'denied',
    'functionality_storage': 'granted',
    'security_storage': 'granted',
    'wait_for_update': 500
  }});
  if (cmdConsent === 'granted') {{
    gtag('consent', 'update', {{
      'ad_storage': 'granted',
      'ad_user_data': 'granted',
      'ad_personalization': 'granted',
      'analytics_storage': 'granted'
    }});
  }}
</script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3N1H2GV63K"></script>
<script>
  gtag('js', new Date());
  gtag('config', 'G-3N1H2GV63K');
</script>
{ld}
</head>
<body>
"""

def header(active=""):
    on_attr = ' class="on"'
    links = "\n".join(
        '<a href="{h}"{on}>{l}</a>'.format(h=href, on=on_attr if href == active else "", l=label)
        for href, label in NAV_ITEMS
    )
    tp, g, fb = PLAT["trustpilot"], PLAT["google"], PLAT["facebook"]
    return f"""{SVG_DEFS}
<div class="ticker"><span>
<b>★ {PLAT['blended']['rating']}/5 from {PLAT['blended']['count']} verified customer reviews</b>·<b>Authorised Minelab dealer since 2014</b>·<b>Official XP &amp; Nokta stockist</b>·<b>Trading since 1995</b>·<b>Field-tested in Lincolnshire</b>·<b>★ {PLAT['blended']['rating']}/5 from {PLAT['blended']['count']} verified customer reviews</b>·<b>Authorised Minelab dealer since 2014</b>·<b>Official XP &amp; Nokta stockist</b>·<b>Trading since 1995</b>·<b>Field-tested in Lincolnshire</b>·
</span></div>
<header>
  <div class="wrap nav">
    <a class="logo" href="/">
      <img src="{LOGO}" alt="Crawfords Metal Detectors" class="logo-w">
      <span class="lg-sub">Reviews</span>
    </a>
    <nav class="menu" id="menu">
      {links}
      <a class="m-shop" href="{shop_url('')}" target="_blank" rel="noopener">Shop at Crawfords</a>
    </nav>
    <a class="btn btn-red" href="{shop_url('')}" target="_blank" rel="noopener">Shop at Crawfords</a>
    <button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i><i></i></button>
  </div>
</header>
<div class="trustbar">
  <div class="wrap">
    <span class="plogo"><svg><use href="#lg-tpstar"/></svg><span class="pname">Trustpilot</span> <b>{tp['rating']}/5</b> · {tp['count']} reviews</span>
    <a class="plogo" href="{g['url']}" target="_blank" rel="noopener"><svg><use href="#lg-google"/></svg><span class="pname">Google</span> <b>{g['rating']}/5</b> · {g['count']} shop reviews</a>
    <span class="plogo"><svg><use href="#lg-fb"/></svg><span class="pname">Facebook</span> <b>{fb['rating']}</b> {fb['label']} · {fb['count']} ratings</span>
  </div>
</div>
"""

def footer():
    return f"""
<footer>
  <div class="wrap">
    <div class="f-grid">
      <div class="f-about">
        <img src="{LOGO}" alt="Crawfords Metal Detectors" class="logo-w">
        <p>The review arm of Crawfords Metal Detectors — the UK's home of metal detecting. Editorial scores, field testing and verified customer reviews.</p>
        <p style="margin-top:12px;font-size:13px;opacity:.85">Every review is written by the Crawfords team — authorised Minelab dealer since 2014, official XP &amp; Nokta stockist, trading since 1995. We test and sell the products we review.</p>
      </div>
      <div>
        <h5>Explore</h5>
        <a href="/reviews/">Reviews</a><a href="/comparisons/">Comparisons</a><a href="/best/">Best-Of Guides</a><a href="/guides/">Field Guides</a><a href="/brands/">Brands</a>
      </div>
      <div>
        <h5>Trust</h5>
        <a href="/customer-reviews/">Customer Reviews Hub</a><a href="/about/">Editorial Policy</a><a href="/about/#how-we-score">How We Score</a><a href="/about/#ownership">Ownership Disclosure</a><a href="/privacy/">Privacy &amp; Cookies</a>
      </div>
      <div>
        <div class="f-shop">
          <b>Ready to buy?</b>
          Every detector we review is in stock at Crawfords.<br>
          {esc(STORE['address'])}<br>
          {esc(STORE['hours'])} · ☎ {esc(STORE['phone'])}
          <a class="btn btn-red" href="{shop_url('')}" target="_blank" rel="noopener">Shop at Crawfords Metal Detectors</a>
        </div>
      </div>
    </div>
    <div class="f-base">
      <span>© 2026 Crawfords Metal Detectors. All rights reserved.</span>
      <span>crawfordsmetaldetectorsreviews.co.uk — owned and operated by Crawfords Metal Detectors (crawfordsmd.com)</span>
    </div>
  </div>
</footer>
<div class="consent" id="consent" role="dialog" aria-live="polite" aria-label="Cookie consent" hidden>
  <div class="consent-in">
    <div class="consent-txt">
      <b>We use cookies</b>
      We use essential cookies to run this site, and analytics cookies to understand which reviews are useful. Analytics only run if you accept. See our <a href="/privacy/">privacy &amp; cookie policy</a>.
    </div>
    <div class="consent-btns">
      <button class="btn btn-line" id="consent-reject" type="button">Reject non-essential</button>
      <button class="btn btn-red" id="consent-accept" type="button">Accept all</button>
    </div>
  </div>
</div>
<script src="/assets/site.js"></script>
</body>
</html>
"""

def p_hero(crumbs, h1, sub, dateline=""):
    dl = f'<div class="dateline">{dateline}</div>' if dateline else ""
    return f"""<div class="p-hero">
  <div class="wrap">
    <div class="crumbs">{crumbs}</div>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
    {dl}
  </div>
</div>"""

# ─────────────────────────────────────────────── components ──

def review_link(p):
    if p["review_status"] == "live":
        return f"/reviews/{p['review_slug']}/"
    return "/reviews/"

def scorebars(p, compact=False):
    s = p["scores"]
    if compact:
        return f'<div class="sb total">Score<span class="bar"><i style="width:{pct(s["total"])}"></i></span>{s["total"]}</div>'
    return f"""<div class="sb">Depth<span class="bar"><i style="width:{pct(s['depth'])}"></i></span>{s['depth']}</div>
          <div class="sb">Separation<span class="bar"><i style="width:{pct(s['separation'])}"></i></span>{s['separation']}</div>
          <div class="sb">Ease of use<span class="bar"><i style="width:{pct(s['ease'])}"></i></span>{s['ease']}</div>
          <div class="sb">Value<span class="bar"><i style="width:{pct(s['value'])}"></i></span>{s['value']}</div>
          <div class="sb total">Score<span class="bar"><i style="width:{pct(s['total'])}"></i></span>{s['total']}</div>"""

def board_row(p, i):
    top = " top" if i == 1 else ""
    return f"""<div class="row{top}">
        <div class="rank">{i:02d}</div>
        <div class="b-img"><img src="{p['image']}" alt="{esc(p['full_name'])}" loading="lazy"></div>
        <div class="b-info">
          <div class="brand">{esc(p['brand'])} · {esc(p['tech'])}</div>
          <h3>{esc(p['name'])}</h3>
          <p>{esc(p['blurb'])}</p>
          <span class="tag">{esc(p['tag'])}</span>
        </div>
        <div class="scorebars">
          {scorebars(p)}
        </div>
        <div class="b-act">
          <a class="btn btn-blue" href="{review_link(p)}">Read Full Review</a>
          <a class="btn btn-line" href="{shop_url(p['shop_path'])}" target="_blank" rel="noopener">Buy at Crawfords</a>
        </div>
      </div>"""

def review_card(p):
    label = ('<span class="go">Read review →</span>' if p["review_status"] == "live"
             else f'<span class="soon">{esc(p["review_label"])}</span>')
    brand = f"{p['brand']} · {p['tech']}" + (" · early verdict" if p["early_verdict"] else "")
    return f"""<a class="card" href="{review_link(p)}">
        <div class="c-img"><span class="c-score">{p['scores']['total']}</span><img src="{p['image']}" alt="{esc(p['full_name'])}" loading="lazy"></div>
        <div class="c-body"><span class="brand">{esc(brand)}</span><h3>{esc(p['full_name'])} Review</h3><p>{esc(p['blurb'][:110])}…</p>{label}</div>
      </a>"""

def quotes_wall():
    return """<div class="wall-grid">
      <div class="rev">
        <div class="rev-top"><span class="plogo dark"><svg><use href="#lg-tpstar"/></svg><span class="pname">Trustpilot</span></span><span class="rating">5★ · verified</span></div>
        <p>"I have been extremely impressed by Crawfords throughout the whole buying and aftersales experience… the greatest treasure we've found so far is Crawfords themselves."</p>
        <div class="who"><b>Jonathan Turner</b>11 April 2026</div>
      </div>
      <div class="rev">
        <div class="rev-top"><span class="plogo dark"><svg><use href="#lg-tpstar"/></svg><span class="pname">Trustpilot</span></span><span class="rating">5★ · verified</span></div>
        <p>"Smooth process during the purchase. By mistake an additional order was made by me. However, within 10 mins CMD called me and explained the situation. Refunds were issued promptly."</p>
        <div class="who"><b>Ivan Guberov</b>26 June 2026</div>
      </div>
      <div class="rev">
        <div class="rev-top"><span class="plogo dark"><svg><use href="#lg-google"/></svg><span class="pname">Google</span></span><span class="rating">5★</span></div>
        <p>"I have a problem with my detector and they have advised me to get it into their factory as soon as possible as my warranty is running out soon. Very friendly people."</p>
        <div class="who"><b>Jim Lennon</b>June 2026</div>
      </div>
      <div class="rev">
        <div class="rev-top"><span class="plogo dark"><svg><use href="#lg-fb"/></svg><span class="pname">Facebook</span></span><span class="rating">Recommends</span></div>
        <p>"Excellent service, Joe extremely helpful. Confident after service will be as good."</p>
        <div class="who"><b>Duncan Howells</b>18 February 2026</div>
      </div>
    </div>"""

# ─────────────────────────────────────────────── pages ──

def page_home():
    man = P["minelab-manticore"]
    rows = "\n".join(board_row(p, i) for i, p in enumerate(PRODUCTS, 1))
    itemlist = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Best Metal Detectors UK — Crawfords Leaderboard",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": p["full_name"],
             "url": f"{DOMAIN}{review_link(p)}"}
            for i, p in enumerate(PRODUCTS, 1)
        ],
    }
    body = f"""{header("/")}
<div class="hero">
  <div class="wrap hero-grid">
    <div>
      <div class="eyebrow">Independent-grade reviews · Dealer-honest testing</div>
      <h1>We sell these detectors. <em>That's exactly why you should read our reviews.</em></h1>
      <p class="lead">Three decades of hands-on dealer experience, field-tested verdicts, and {PLAT['blended']['count']} verified customer reviews — every score earned in real UK soil, not a spec sheet.</p>
      <div class="hero-ctas">
        <a class="btn btn-red" href="#leaderboard">See the Leaderboard</a>
        <a class="btn btn-ghost" href="/about/">How we score</a>
      </div>
      <div class="hero-rating">
        <div class="badge-score">{PLAT['blended']['rating']}<span style="font-size:16px;color:var(--steel)">/5</span></div>
        <div class="txt">
          <b style="display:inline-flex;align-items:center;gap:8px">Blended rating across
            <svg style="width:16px;height:16px"><use href="#lg-tpstar"/></svg>
            <svg style="width:16px;height:16px"><use href="#lg-google"/></svg>
            <svg style="width:16px;height:16px"><use href="#lg-fb"/></svg>
          </b><br>{PLAT['blended']['count']} verified customer reviews · UK's home of metal detecting since 1995</div>
      </div>
    </div>
    <aside class="champ">
      <div class="champ-top">★ Editor's Choice 2026 ★</div>
      <div class="champ-img"><img src="{man['image']}" alt="Minelab Manticore"></div>
      <div class="champ-body">
        <div class="brand">Minelab</div>
        <h3>Manticore</h3>
        <div class="champ-meta">
          <div class="sc">{man['scores']['total']} <small>/ 5 editorial score</small></div>
          <div class="pricelink">Live price at Crawfords →</div>
        </div>
        <a class="btn btn-blue" href="/reviews/minelab-manticore-review/">Read the Full Verdict</a>
      </div>
    </aside>
  </div>
</div>
<div class="platforms">
  <div class="plat-grid">
    <div class="plat"><div class="n">30+</div><div class="l">Years hands-on trading</div></div>
    <div class="plat"><div class="n">{PLAT['blended']['count']}</div><div class="l">Verified customer reviews</div></div>
    <div class="plat"><div class="n">{PLAT['blended']['rating']}/5</div><div class="l">Blended trust rating</div></div>
    <div class="plat"><div class="n">6 days</div><div class="l">Scunthorpe store open weekly</div></div>
  </div>
</div>
<section id="leaderboard">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="eyebrow">Field-tested rankings</div><h2>The Leaderboard</h2></div>
      <p>We don't just read spec sheets — we sell, service and swing these machines every week. Prices live on each product page at crawfordsmd.com. Stock last checked {TODAY}.</p>
    </div>
    <div class="rank-note">
      <span class="ic">i</span>
      <span><b>How this ranking works:</b> the order is set by our <b>editorial testing score</b> — awarded by the Crawfords team after hands-on field testing — not by an automated average of customer review counts. Scores run the full range — a 3.6 here is still a machine we're happy to sell, but we say plainly where it gives ground to the machines above it. New releases carry an "early verdict" until they've done a season in UK soil. Scores are re-checked at every monthly refresh pass. <a href="/about/#how-we-score" style="color:var(--blue);font-weight:600">Read the full methodology →</a></span>
    </div>
    <div class="board">
      {rows}
    </div>
  </div>
</section>
<section class="cats">
  <div class="wrap">
    <div class="sec-head"><div><div class="eyebrow">Choose your path</div><h2>Everything you need before you buy</h2></div></div>
    <div class="cat-grid">
      <a class="cat" href="/reviews/"><div class="num">/01</div><h3>In-Depth Reviews</h3><p>Single-machine deep dives with editorial scores, testing notes and verified owner quotes.</p><span class="go">Browse reviews →</span></a>
      <a class="cat" href="/comparisons/"><div class="num">/02</div><h3>Head-to-Head</h3><p>Deus II vs Manticore. Legend 2 vs Equinox 900. One winner per budget, no fence-sitting.</p><span class="go">See comparisons →</span></a>
      <a class="cat" href="/best/"><div class="num">/03</div><h3>Best-Of Guides</h3><p>Ranked buying guides by use case — beginners, beach &amp; wet sand, budget, and more.</p><span class="go">View rankings →</span></a>
      <a class="cat" href="/guides/"><div class="num">/04</div><h3>Field Guides</h3><p>Ground balance, discrimination, UK permissions and the Treasure Act — explained plainly.</p><span class="go">Read guides →</span></a>
    </div>
  </div>
</section>
<section class="latest" style="padding-bottom:0">
  <div class="wrap">
    <div class="sec-head">
      <div><div class="eyebrow">Latest from the blog</div><h2>Fresh field notes</h2></div>
      <a class="btn btn-line" href="/guides/">All articles</a>
    </div>
    <div class="mini-list">
      <a class="mini" href="/comparisons/nokta-legend-2-vs-minelab-equinox-900/"><span class="k">Versus</span><h4>Nokta Legend 2 vs Minelab Equinox 900: Which Wins?</h4><span class="d">Live</span></a>
      <a class="mini" href="/comparisons/xp-icon-x-vs-minelab-manticore/"><span class="k">Versus</span><h4>XP ICON X vs Minelab Manticore: Head-to-Head</h4><span class="d">Live</span></a>
      <a class="mini" href="/guides/beach-metal-detecting-uk/"><span class="k">Guide</span><h4>Beach Metal Detecting in the UK: Why the Beach Beats Most Machines</h4><span class="d">Live</span></a>
      <a class="mini" href="/guides/waterproof-metal-detectors-explained/"><span class="k">Guide</span><h4>What "Waterproof" Actually Means on a Metal Detector</h4><span class="d">Live</span></a>
      <a class="mini" href="/guides/uk-metal-detecting-permissions/"><span class="k">Guide</span><h4>UK Metal Detecting Permissions: The Rules Before You Dig</h4><span class="d">Live</span></a>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head">
      <div><div class="eyebrow">Verified customer reviews</div><h2>{PLAT['blended']['count']} detectorists rate us {PLAT['blended']['rating']}/5</h2></div>
      <a class="btn btn-line" href="/customer-reviews/">Visit the Trust Hub</a>
    </div>
    {quotes_wall()}
  </div>
</section>
{footer()}"""
    return head(
        "Metal Detector Reviews UK | Field-Tested by Crawfords Metal Detectors",
        f"Field-tested metal detector reviews from the UK's home of metal detecting. Editorial scores, honest pros and cons, and {PLAT['blended']['count']} verified customer reviews. Trading since 1995.",
        "/", [itemlist],
    ) + body

def page_reviews_index():
    cards = "\n".join(review_card(p) for p in PRODUCTS)
    body = f"""{header("/reviews/")}
{p_hero('<a href="/">Home</a> / Reviews', 'In-Depth Detector Reviews',
        'Every review follows the same Verdict format: editorial score up top, pros and cons, hands-on testing notes, full specs and verified customer quotes. No 800-word preambles.')}
<section>
  <div class="wrap">
    <div class="cards">
      {cards}
    </div>
    <div class="cta-band">
      <div><h3>Not sure which machine suits you?</h3><p>Call the Scunthorpe team on {esc(STORE['phone'])} — real detectorists, honest advice.</p></div>
      <a class="btn btn-red" href="{shop_url('')}" target="_blank" rel="noopener">Shop at Crawfords</a>
    </div>
  </div>
</section>
{footer()}"""
    schema = [webpage_schema("In-Depth Detector Reviews", "Field-tested reviews of Minelab, XP and Nokta metal detectors.", "/reviews/"),
              crumb_schema([("Home", "/"), ("Reviews", None)])]
    return head(
        "Metal Detector Reviews — Editorial Scores & Field Tests | Crawfords",
        "In-depth, field-tested reviews of Minelab, XP and Nokta metal detectors, scored honestly by the Crawfords team. Updated monthly.",
        "/reviews/", schema,
    ) + body

def page_review(slug):
    p = P[slug]
    c = REVIEWS[slug]
    path = f"/reviews/{p['review_slug']}/"
    chips = "\n".join(f"<div><b>{b}</b>{t}</div>" for b, t in c["chips"])
    pros = "\n".join(f"<li>{x}</li>" for x in c["pros"])
    cons = "\n".join(f"<li>{x}</li>" for x in c["cons"])
    testing = "\n".join(f"<p><b>{h}.</b> {t}</p>" for h, t in c["testing"])
    specs = "\n".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in c["specs"])
    faq_html = "\n".join(
        f"<details><summary>{esc(q)}</summary><div class=\"faq-a\">{esc(a)}</div></details>"
        for q, a in c["faqs"])
    stars = "★" * round(p["scores"]["total"]) + "☆" * (5 - round(p["scores"]["total"]))
    schema = [
        article_schema(c["h1"], c["sub"].replace("&amp;", "&"), path, "2026-07-31", TODAY),
        faq_schema(c["faqs"]),
        crumb_schema([("Home", "/"), ("Reviews", "/reviews/"), (p["full_name"] + " Review", None)]),
    ]
    body = f"""{header("/reviews/")}
{p_hero(f'<a href="/">Home</a> / <a href="/reviews/">Reviews</a> / <a href="/brands/">{p["brand"]}</a> / {p["name"]}',
        c["h1"], c["sub"],
        f'Published <b>31 July 2026</b> · Last re-tested <b>{TODAY}</b> · By the <b>Crawfords Metal Detectors team</b>')}
<section style="padding:64px 0 0">
  <div class="wrap">
    <div class="vd">
      <div class="vd-grid">
        <div class="vd-photo"><img src="{p['image']}" alt="{esc(p['full_name'])}"></div>
        <div>
          <div class="eyebrow">Quick Verdict</div>
          <h3 style="margin-top:14px">{c["verdict_head"]}</h3>
          <div class="vd-score-line">
            <span class="big">{p['scores']['total']}</span>
            <span><span class="stars">{stars}</span><br><small style="color:#4a5a66">Editorial score · re-tested at every monthly refresh{' · early verdict' if p.get('early_verdict') else ''}</small></span>
          </div>
          <div class="bestfor"><b>Best for:</b> {c["bestfor"]}</div>
          <div class="vd-meta">
            {chips}
          </div>
          <div class="vd-ctas">
            <a class="btn btn-red" href="{shop_url(p['shop_path'])}" target="_blank" rel="noopener">Check Live Price at Crawfords</a>
            <a class="btn btn-line" href="/">See the Leaderboard</a>
          </div>
        </div>
      </div>
      <div class="proscons">
        <div class="pc pros"><h4>What we rate</h4><ul>
          {pros}
        </ul></div>
        <div class="pc cons"><h4>What to weigh up</h4><ul>
          {cons}
        </ul></div>
      </div>
    </div>
  </div>
</section>
<div class="article">
  <div class="capsule"><span class="cap-k">The 40-word answer</span>
    {c["capsule"]}
  </div>
  <h2>Hands-on testing notes</h2>
  {testing}
  <h2>Specification</h2>
  <table class="spec">
    <tr><th>Specification</th><th>{esc(p['full_name'])}</th></tr>
    {specs}
  </table>
  <p>{c["compare_note"]}</p>
  <h2>Frequently asked questions</h2>
  <div class="faq">
    {faq_html}
  </div>
  <h2>Final verdict</h2>
  <p>{c["final"]}</p>
  <div class="cta-band">
    <div><h3>{esc(p['full_name'])}</h3><p>Live price and stock on the Crawfords product page · {esc(p['stock'])} · last checked {TODAY}</p></div>
    <a class="btn btn-red" href="{shop_url(p['shop_path'])}" target="_blank" rel="noopener">Buy at Crawfords</a>
  </div>
  <p class="disclosure-line">{DISCLOSURE}</p>
</div>
{footer()}"""
    title = f"{c['h1']} | Crawfords Reviews"
    return head(title, c["desc"] if c.get("desc") else c["sub"].replace("&amp;","&"), path, schema) + body

def page_guide(slug):
    g = GUIDES[slug]
    path = f"/guides/{slug}/"
    schema = [article_schema(g["title"], g["desc"], path, g["date"], TODAY),
              crumb_schema([("Home", "/"), ("Blog", "/guides/"), (g["title"], None)])]
    body = f"""{header("/guides/")}
{p_hero(f'<a href="/">Home</a> / <a href="/guides/">Blog</a> / {g["kicker"]}',
        g["title"], g["desc"],
        f'Published <b>31 July 2026</b> · By the <b>Crawfords Metal Detectors team</b>')}
<div class="article">
  {g["body"]}
  <div class="cta-band">
    <div><h3>Talk it through with a detectorist</h3><p>Honest advice for your ground and budget · {esc(STORE['phone'])} · {esc(STORE['hours'])}</p></div>
    <a class="btn btn-red" href="{shop_url('')}" target="_blank" rel="noopener">Shop at Crawfords</a>
  </div>
  <p class="disclosure-line">{DISCLOSURE}</p>
</div>
{footer()}"""
    return head(f"{g['title']} | Crawfords Reviews", g["desc"], path, schema) + body

def page_comparison_article(slug):
    c = COMPARISONS[slug]
    a, b = P[c["a"]], P[c["b"]]
    path = f"/comparisons/{slug}/"
    winpills = "\n".join(f'<span class="winpill">{k}: <b>{v}</b></span>' for k, v in c["winline"])
    rows = []
    for label, va, vb, win in c["spec_rows"]:
        ca = ' class="win"' if win == "a" else ""
        cb = ' class="win"' if win == "b" else ""
        rows.append(f"<tr><td>{label}</td><td{ca}>{va}</td><td{cb}>{vb}</td></tr>")
    rows = "\n".join(rows)
    schema = [article_schema(c["title"], c["desc"], path, c["date"], TODAY),
              crumb_schema([("Home", "/"), ("Comparisons", "/comparisons/"), (c["title"], None)])]
    body = f"""{header("/comparisons/")}
{p_hero(f'<a href="/">Home</a> / <a href="/comparisons/">Comparisons</a> / {a["name"]} vs {b["name"]}',
        c["title"], c["desc"],
        f'Published <b>31 July 2026</b> · By the <b>Crawfords Metal Detectors team</b>')}
<section style="padding:64px 0">
  <div class="wrap">
    <div class="vs-hero">
      <div class="vs-card">
        <img src="{a['image']}" alt="{esc(a['full_name'])}">
        <div class="brand">{esc(a['brand'])}</div><h3>{esc(a['name'])}</h3><div class="sc">{a['scores']['total']} / 5</div>
        <a class="btn btn-line" style="margin-top:16px" href="/reviews/{a['review_slug']}/">Read Full Review</a>
      </div>
      <div class="vs-badge">VS</div>
      <div class="vs-card">
        <img src="{b['image']}" alt="{esc(b['full_name'])}">
        <div class="brand">{esc(b['brand'])}</div><h3>{esc(b['name'])}</h3><div class="sc">{b['scores']['total']} / 5</div>
        <a class="btn btn-line" style="margin-top:16px" href="/reviews/{b['review_slug']}/">Read Full Review</a>
      </div>
    </div>
    <div class="winline">
      {winpills}
    </div>
    <div class="article" style="padding:0;max-width:none">
      <div class="capsule"><span class="cap-k">The 40-word answer</span>
        {c["capsule"]}
      </div>
      {c["body"]}
      <h2>Specification, side by side</h2>
      <table class="spec">
        <tr><th></th><th>{esc(a['full_name'])}</th><th>{esc(b['full_name'])}</th></tr>
        {rows}
      </table>
      <div class="buy-split">
        <div class="buy-box">
          <h4>{c["buy_a"][0]}</h4><p>{c["buy_a"][1]}</p>
          <a class="btn btn-blue" href="{shop_url(a['shop_path'])}" target="_blank" rel="noopener">{esc(a['name'])} at Crawfords</a>
        </div>
        <div class="buy-box">
          <h4>{c["buy_b"][0]}</h4><p>{c["buy_b"][1]}</p>
          <a class="btn btn-blue" href="{shop_url(b['shop_path'])}" target="_blank" rel="noopener">{esc(b['name'])} at Crawfords</a>
        </div>
      </div>
      <p class="disclosure-line">{DISCLOSURE}</p>
    </div>
  </div>
</section>
{footer()}"""
    return head(f"{c['title']} | Crawfords Reviews", c["desc"], path, schema) + body

def page_comparisons_index():
    man, deus, eqx, icon = P["minelab-manticore"], P["xp-deus2"], P["minelab-equinox-900"], P["xp-icon-x"]
    path = "/comparisons/"
    schema = [webpage_schema("Metal Detector Comparisons", "Head-to-head metal detector comparisons with a clear winner per budget.", path),
              crumb_schema([("Home", "/"), ("Comparisons", None)])]
    body = f"""{header("/comparisons/")}
{p_hero('<a href="/">Home</a> / Comparisons', 'Head-to-Head Comparisons',
        'Two machines, one budget, one winner. Each comparison ends with a clear recommendation for each type of detectorist — no fence-sitting.')}
<section>
  <div class="wrap">
    <div class="cards">
      <a class="card" href="/comparisons/xp-deus-2-vs-minelab-manticore/">
        <div class="c-img"><img src="{man['image']}" alt="XP Deus 2 vs Minelab Manticore" loading="lazy"></div>
        <div class="c-body"><span class="brand">Flagship head-to-head</span><h3>XP Deus 2 vs Minelab Manticore</h3><p>The two best detectors we sell, fought out across depth, weight, water and target information.</p><span class="go">Read the comparison →</span></div>
      </a>
      <a class="card" href="/comparisons/nokta-legend-2-vs-minelab-equinox-900/">
        <div class="c-img"><img src="{eqx['image']}" alt="Nokta Legend 2 vs Minelab Equinox 900" loading="lazy"></div>
        <div class="c-body"><span class="brand">Value vs proven</span><h3>Nokta Legend 2 vs Minelab Equinox 900</h3><p>Does the value champion really challenge the proven all-rounder?</p><span class="go">Read the comparison →</span></div>
      </a>
      <a class="card" href="/comparisons/xp-icon-x-vs-minelab-manticore/">
        <div class="c-img"><img src="{icon['image']}" alt="XP ICON X vs Minelab Manticore" loading="lazy"></div>
        <div class="c-body"><span class="brand">New vs benchmark</span><h3>XP ICON X vs Minelab Manticore</h3><p>XP's newest release against our highest-scored machine.</p><span class="go">Read the comparison →</span></div>
      </a>
    </div>
  </div>
</section>
{footer()}"""
    return head(
        "Metal Detector Comparisons — Head-to-Head Verdicts | Crawfords",
        "Head-to-head metal detector comparisons with a clear winner per budget: Deus 2 vs Manticore, Legend 2 vs Equinox 900 and ICON X vs Manticore, tested by the Crawfords team.",
        path, schema,
    ) + body

def page_deus_vs_manticore():
    man, deus = P["minelab-manticore"], P["xp-deus2"]
    body = f"""{header("/comparisons/")}
{p_hero('<a href="/">Home</a> / <a href="/comparisons/">Comparisons</a> / XP Deus 2 vs Minelab Manticore',
        'XP Deus 2 vs Minelab Manticore: Flagship Head-to-Head',
        'The two best detectors in the shop. One is the lightest serious machine ever made; the other gives you more target information than anything else. Here’s how to choose.',
        'Publishing <b>Week 4 · Thu</b> · By the <b>Crawfords Metal Detectors team</b>')}
<section style="padding:64px 0">
  <div class="wrap">
    <div class="vs-hero">
      <div class="vs-card">
        <img src="{deus['image']}" alt="XP Deus II">
        <div class="brand">XP</div><h3>Deus II</h3><div class="sc">{deus['scores']['total']} / 5</div>
        <p style="font-size:14px;color:#4a5a66;margin-top:8px">Featherweight · fully wireless · 20m waterproof</p>
        <a class="btn btn-line" style="margin-top:16px" href="{shop_url(deus['shop_path'])}" target="_blank" rel="noopener">Buy at Crawfords</a>
      </div>
      <div class="vs-badge">VS</div>
      <div class="vs-card">
        <img src="{man['image']}" alt="Minelab Manticore">
        <div class="brand">Minelab</div><h3>Manticore</h3><div class="sc">{man['scores']['total']} / 5</div>
        <p style="font-size:14px;color:#4a5a66;margin-top:8px">Multi-IQ+ · 2D target trace · editor's choice</p>
        <a class="btn btn-line" style="margin-top:16px" href="{shop_url(man['shop_path'])}" target="_blank" rel="noopener">Buy at Crawfords</a>
      </div>
    </div>
    <div class="winline">
      <span class="winpill">Target information: <b>Manticore</b></span>
      <span class="winpill">Weight &amp; ergonomics: <b>Deus II</b></span>
      <span class="winpill">Diving &amp; deep water: <b>Deus II</b></span>
      <span class="winpill">Mineralised ground: <b>Manticore</b></span>
      <span class="winpill">Iron-heavy sites: <b>tie — different strengths</b></span>
      <span class="winpill">Overall: <b>Manticore, by a nose</b></span>
    </div>
    <div class="article" style="padding:0;max-width:none">
      <div class="capsule"><span class="cap-k">The 40-word answer</span>
        Buy the Manticore if you want maximum target information on difficult inland ground. Buy the Deus II if weight, wireless freedom or serious underwater work matter more. Both are flagship-grade; neither is a mistake.
      </div>
      <h2>Specification, side by side</h2>
      <table class="spec">
        <tr><th>Specification</th><th>XP Deus II</th><th>Minelab Manticore</th></tr>
        <tr><td>Technology</td><td>FMF simultaneous multi-frequency</td><td>Multi-IQ+ simultaneous multi-frequency</td></tr>
        <tr><td>Target information</td><td>Numeric ID</td><td class="win">2D target trace + numeric ID</td></tr>
        <tr><td>Weight</td><td class="win">Featherweight class — lightest full-size flagship</td><td>Standard class</td></tr>
        <tr><td>Waterproof</td><td class="win">Submersible to 20m</td><td>Submersible to 5m</td></tr>
        <tr><td>Wireless</td><td class="win">Fully wireless coil-to-remote platform</td><td>Wired coil, wireless audio</td></tr>
        <tr><td>Warranty at Crawfords</td><td>5-year XP manufacturer warranty</td><td>3-year Minelab manufacturer warranty</td></tr>
      </table>
      <div class="buy-split">
        <div class="buy-box">
          <h4>Buy the Deus II if…</h4>
          <p>You swing for six-hour sessions and feel it in your shoulder; you dive or hunt deep surf; you want a modular platform with a huge coil ecosystem; you value fast recovery in dense iron above absolute depth.</p>
          <a class="btn btn-blue" href="{shop_url(deus['shop_path'])}" target="_blank" rel="noopener">Deus II at Crawfords</a>
        </div>
        <div class="buy-box">
          <h4>Buy the Manticore if…</h4>
          <p>Your permissions are mineralised or iron-infested and you want the clearest possible picture before you dig; you hunt to 5m or shallower; you want the machine our team scores highest overall.</p>
          <a class="btn btn-blue" href="{shop_url(man['shop_path'])}" target="_blank" rel="noopener">Manticore at Crawfords</a>
        </div>
      </div>
      <p>Want the full background on our winner? Read the complete <a href="/reviews/minelab-manticore-review/" style="color:var(--blue);font-weight:600">Minelab Manticore review</a>, or see where both machines sit on <a href="/" style="color:var(--blue);font-weight:600">the Leaderboard</a>.</p>
      <p class="disclosure-line">Crawfords Metal Detectors is an authorised Minelab dealer and an official stockist of XP and Nokta. We test and sell the products we review.</p>
    </div>
  </div>
</section>
{footer()}"""
    schema = [article_schema("XP Deus 2 vs Minelab Manticore: Flagship Head-to-Head",
                             "Deus 2 vs Manticore tested side by side: depth, weight, waterproofing and target information compared.",
                             "/comparisons/xp-deus-2-vs-minelab-manticore/", "2026-07-20", TODAY),
              crumb_schema([("Home", "/"), ("Comparisons", "/comparisons/"), ("XP Deus 2 vs Minelab Manticore", None)])]
    return head(
        "XP Deus 2 vs Minelab Manticore (2026): Which Flagship Wins? | Crawfords",
        "Deus 2 vs Manticore, tested side by side by the Crawfords team: depth, weight, waterproofing and target information compared, with a clear buy recommendation for each detectorist.",
        "/comparisons/xp-deus-2-vs-minelab-manticore/", schema,
    ) + body

def page_best():
    order = ["minelab-x-terra-elite", "simplex-ultra", "nokta-legend-2", "minelab-x-terra-pro"]
    picks = [P[s] for s in order]
    labels = ["Best overall for beginners", "Best budget", "Most features per pound", "Best rugged starter"]
    notes = [
        "Our top beginner buy: genuine simultaneous multi-frequency, 5m submersion, and currently bundled with ML-85 wireless headphones. The one machine here you won't outgrow in a season.",
        "The budget waterproof all-rounder. Simple controls, rugged build, and submersible — the machine we recommend most often across the counter. Inland it's excellent; skip it if wet-sand beaches are your main plan.",
        "The ambitious beginner's shortcut to advanced features: SMF, full submersion and deep customisation. Be honest with yourself about the learning curve — the menus are not beginner-gentle.",
        "Rugged, waterproof, and switchable between 5/8/10/15 kHz single frequencies. The simplest Minelab route into the hobby — accept the single-frequency limits and it won't let you down.",
    ]
    rows = "\n".join(f"""<div class="row{' top' if i == 1 else ''}">
        <div class="rank">{i:02d}</div>
        <div class="b-img"><img src="{p['image']}" alt="{esc(p['full_name'])}" loading="lazy"></div>
        <div class="b-info">
          <div class="brand">{esc(p['brand'])} · {esc(p['tech'])}</div>
          <h3>{esc(p['name'])}</h3>
          <p>{esc(notes[i-1])}</p>
          <span class="tag">{esc(labels[i-1])}</span>
        </div>
        <div class="scorebars">{scorebars(p, compact=True)}</div>
        <div class="b-act">
          <a class="btn btn-blue" href="{review_link(p)}">Read Review</a>
          <a class="btn btn-line" href="{shop_url(p['shop_path'])}" target="_blank" rel="noopener">Buy at Crawfords</a>
        </div>
      </div>""" for i, p in enumerate(picks, 1))
    body = f"""{header("/best/")}
{p_hero('<a href="/">Home</a> / Best Of', 'Best Metal Detectors for Beginners UK (2026 Buying Guide)',
        'Four machines we actually hand to first-timers in the Scunthorpe shop — ranked across budget tiers, with plain-English reasons why (and honest notes on what each one can’t do).',
        'Publishing <b>Week 1 · Thu</b> · By the <b>Crawfords Metal Detectors team</b>')}
<section>
  <div class="wrap">
    <div class="capsule" style="max-width:840px;margin:0 auto 60px"><span class="cap-k">Multi-frequency vs single frequency — in one paragraph</span>
      A single-frequency detector transmits one signal into the ground; a simultaneous multi-frequency machine (Minelab's Multi-IQ, Nokta's SMF) transmits several at once, so it handles wet sand and mineralised soil far better. Beginners on a budget do fine with single frequency inland — but if the beach is on your list, multi-frequency is worth the stretch.
    </div>
    <div class="board">
      {rows}
    </div>
    <div class="cta-band">
      <div><h3>Coming next: Best Metal Detectors for the Beach &amp; Wet Sand (UK 2026)</h3><p>Real waterproof depth ratings per model — publishing Week 4.</p></div>
      <a class="btn btn-ghost" style="border-color:#fff" href="/guides/">Browse the guides →</a>
    </div>
  </div>
</section>
{footer()}"""
    return head(
        "Best Metal Detectors for Beginners UK (2026) | Crawfords Reviews",
        "The four beginner metal detectors the Crawfords team actually recommends in store, ranked by budget with honest notes on what each machine can't do.",
        "/best/", [crumb_schema([("Home", "/"), ("Best Of", None)])],
    ) + body

def page_guides():
    path = "/guides/"
    schema = [webpage_schema("Blog & Field Guides", "Metal detecting guides, comparisons and reviews from the Crawfords team.", path),
              crumb_schema([("Home", "/"), ("Blog", None)])]
    guide_cards = []
    for slug, g in GUIDES.items():
        guide_cards.append(f"""<a class="card" href="/guides/{slug}/">
        <div class="c-body" style="padding-top:30px"><span class="brand">{g['kicker']}</span><h3>{g['title']}</h3><p>{g['desc']}</p><span class="go">Read article →</span></div>
      </a>""")
    comp_cards = []
    for slug, c in COMPARISONS.items():
        comp_cards.append(f"""<a class="card" href="/comparisons/{slug}/">
        <div class="c-body" style="padding-top:30px"><span class="brand">Head-to-head</span><h3>{c['title']}</h3><p>{c['desc']}</p><span class="go">Read comparison →</span></a-comment></div>
      </a>""")
    comp_cards = [x.replace('</a-comment>','') for x in comp_cards]
    cards = "\n".join(guide_cards + comp_cards)
    posts = SHOP_BLOG.get("posts", [])
    if posts:
        items = "\n".join(
            f'<a class="mini" href="{shop_url("/blog")}" target="_blank" rel="noopener">'
            f'<span class="k">Crawfords blog</span><h4>{esc(p["title"])}</h4>'
            f'<span class="d">Read on crawfordsmd.com →</span></a>' for p in posts[:6])
        shop_blog_block = (
            '<div class="sec-head" style="margin-top:64px">'
            '<div><div class="eyebrow">From the main site</div>'
            '<h2>Latest from the Crawfords blog</h2></div>'
            f'<p style="max-width:460px">Buying guides and news published on crawfordsmd.com. '
            f'Updated in the weekly sync — last checked {SHOP_BLOG.get("updated", TODAY)}.</p></div>'
            f'<div class="mini-list">{items}</div>')
    else:
        shop_blog_block = ""
    body = f"""{header("/guides/")}
{p_hero('<a href="/">Home</a> / Blog', 'Blog &amp; Field Guides',
        'Evergreen how-to and educational content — the questions we answer over the counter every week, written down properly — plus every comparison and review as it publishes.')}
<section>
  <div class="wrap">
    <div class="cards">
      {cards}
    </div>
    {shop_blog_block}
    <div class="cta-band">
      <div><h3>All eight detector reviews are live</h3><p>Editorial scores, honest cons and verified customer quotes on every machine we rank.</p></div>
      <a class="btn btn-red" href="/reviews/">Browse the reviews</a>
    </div>
  </div>
</section>
{footer()}"""
    return head(
        "Metal Detecting Blog & Field Guides UK | Crawfords Reviews",
        "Plain-English metal detecting guides and head-to-head comparisons from the Crawfords team: technology explained, beach and waterproof advice, UK permissions and more.",
        path, schema,
    ) + body

def page_brands():
    def chips(slugs):
        out = []
        for s in slugs:
            p = P[s]
            label = "Read review →" if p["review_status"] == "live" else p["review_label"]
            cls = "rv"
            score = f"{p['scores']['total']}" + (" early" if p["early_verdict"] else "")
            out.append(f'<a class="chip" href="{review_link(p)}"><b>{esc(p["name"])}</b><span>{esc(p["tech"])} · {score}</span><span class="{cls}">{esc(label)}</span></a>')
        return "\n".join(out)
    body = f"""{header("/brands/")}
{p_hero('<a href="/">Home</a> / Brands', 'Brand Hubs',
        'Every machine we’ve reviewed, grouped by manufacturer — with our dealer relationship disclosed on every hub.')}
<section>
  <div class="wrap">
    <div class="brandcard">
      <div class="bc-left">
        <h3>Minelab</h3><div class="since">Authorised dealer since 2014</div>
        <p>The market leader in simultaneous multi-frequency. We stock and service the current range, from the X-Terra series to the flagship Manticore, all with manufacturer warranty.</p>
        <a class="btn btn-line" style="margin-top:16px" href="{shop_url('')}" target="_blank" rel="noopener">Minelab at Crawfords</a>
      </div>
      <div class="chiprow">{chips(['minelab-manticore','minelab-equinox-900','minelab-x-terra-elite','minelab-x-terra-pro'])}</div>
    </div>
    <div class="brandcard">
      <div class="bc-left">
        <h3>XP</h3><div class="since">Official UK stockist</div>
        <p>French engineering, featherweight builds and fully wireless platforms. Home of the flagship Deus II and the new ICON X.</p>
        <a class="btn btn-line" style="margin-top:16px" href="{shop_url('')}" target="_blank" rel="noopener">XP at Crawfords</a>
      </div>
      <div class="chiprow">{chips(['xp-deus2','xp-icon-x'])}
        <a class="chip" href="/comparisons/xp-deus-2-vs-minelab-manticore/"><b>Deus 2 vs Manticore</b><span>Flagship head-to-head</span><span class="rv">Read comparison →</span></a>
      </div>
    </div>
    <div class="brandcard">
      <div class="bc-left">
        <h3>Nokta</h3><div class="since">Official UK stockist</div>
        <p>Aggressive value engineering from Turkey — the Legend 2 and Simplex Ultra deliver serious specification per pound.</p>
        <a class="btn btn-line" style="margin-top:16px" href="{shop_url('')}" target="_blank" rel="noopener">Nokta at Crawfords</a>
      </div>
      <div class="chiprow">{chips(['nokta-legend-2','simplex-ultra'])}</div>
    </div>
  </div>
</section>
{footer()}"""
    return head(
        "Metal Detector Brands — Minelab, XP, Nokta | Crawfords Reviews",
        "Minelab, XP and Nokta brand hubs with every Crawfords review in one place, and our authorised dealer relationships disclosed on every page.",
        "/brands/", [crumb_schema([("Home", "/"), ("Brands", None)])],
    ) + body

def page_trust():
    tp, g, fb = PLAT["trustpilot"], PLAT["google"], PLAT["facebook"]
    path = "/customer-reviews/"
    TP_BU = "5b587e7606b99600018ba03a"   # Crawfords Metal Detectors business unit
    schema = [webpage_schema("Customer Reviews", "Verified customer reviews of Crawfords Metal Detectors.", path),
              crumb_schema([("Home", "/"), ("Customer Reviews", None)])]

    # Curated, verified quotes — each links to the machine it relates to.
    # Only genuine, dated, attributed reviews go in this list.
    feed = REVIEWS_FEED.get("reviews", [])
    def fmt_date(d):
        try:
            y, m, dd = d.split("-")
            months = ["January","February","March","April","May","June","July",
                      "August","September","October","November","December"]
            return f"{int(dd)} {months[int(m)-1]} {y}"
        except Exception:
            return d
    cards = []
    for x in feed:
        rec = ""
        if x.get("p") and x["p"] in P:
            pr = P[x["p"]]
            rec = (f'<a class="rev-rec" href="/reviews/{pr["review_slug"]}/">'
                   f'Our verdict on the <b>{esc(pr["full_name"])}</b> →</a>')
        stars = "★" * int(x["r"]) + "☆" * (5 - int(x["r"]))
        cards.append(f"""<div class="rev" data-stars="{x['r']}">
        <div class="rev-top"><span class="plogo dark"><svg><use href="#lg-tpstar"/></svg><span class="pname">Trustpilot</span></span><span class="rating">{stars}</span></div>
        <p>"{esc(x['b'])}"</p>
        {rec}
        <div class="who"><b>{esc(x['n'])}</b>{fmt_date(x['d'])}</div>
      </div>""")
    quote_cards = "\n".join(cards)
    n_reviews = len(feed)

    prod_widgets = "\n".join(f"""<a class="rw-card" href="/reviews/{p['review_slug']}/">
        <img src="{p['image']}" alt="{esc(p['full_name'])}" loading="lazy">
        <div><b>{esc(p['full_name'])}</b><span>{p['scores']['total']}/5 editorial score · read our verdict →</span></div>
      </a>""" for p in PRODUCTS)

    body = f"""{header("/customer-reviews/")}
{p_hero('<a href="/">Home</a> / Customer Reviews', 'Real Customer Reviews: What UK Detectorists Are Saying',
        'Every review below is live from Trustpilot, Google and Facebook — the platforms where our customers actually leave them. Nothing curated away, nothing rewritten.')}
<section>
  <div class="wrap">
    <div class="pcards">
      <a class="pcard" href="https://uk.trustpilot.com/review/www.crawfordsmd.com" target="_blank" rel="noopener"><svg><use href="#lg-tpstar"/></svg><div><div class="n">{tp['rating']}<span style="font-size:15px;color:#4a5a66">/5</span></div><div class="l"><b>Trustpilot</b> · "{tp['label']}" · {tp['count']} reviews</div></div></a>
      <a class="pcard" href="{PLAT['google'].get('url', '#')}" target="_blank" rel="noopener"><svg><use href="#lg-google"/></svg><div><div class="n">{g['rating']}<span style="font-size:15px;color:#4a5a66">/5</span></div><div class="l"><b>Google shop rating</b> · "{g['label']}" badge · {g['count']} reviews</div></div></a>
      <div class="pcard"><svg><use href="#lg-fb"/></svg><div><div class="n">{fb['rating']}</div><div class="l"><b>Facebook</b> · {fb['label']} · {fb['count']} ratings</div></div></div>
    </div>

    <div class="sec-head" style="margin-bottom:24px">
      <div><div class="eyebrow">Live feed</div><h2>All {tp['count']} Trustpilot reviews</h2></div>
      <p>Straight from Trustpilot, updating as customers post. Scroll the carousel or open any review at source.</p>
    </div>
    <!-- TrustBox widget - Carousel -->
    <div class="trustbox-wrap">
      <div class="trustpilot-widget" data-locale="en-GB" data-template-id="53aa8912dec7e10d38f59f36"
           data-businessunit-id="{TP_BU}" data-style-height="140px" data-style-width="100%"
           data-theme="light" data-stars="4,5" data-review-languages="en">
        <a href="https://uk.trustpilot.com/review/www.crawfordsmd.com" target="_blank" rel="noopener">Read our {tp['count']} reviews on Trustpilot</a>
      </div>
    </div>

    <div class="sec-head" style="margin-top:70px">
      <div><div class="eyebrow">Verified reviews</div><h2>{n_reviews} customer reviews, in full</h2></div>
      <p>Imported from our Trustpilot profile — every one genuine, dated and attributed, newest first. Reviews mentioning a machine link to our verdict on it.</p>
    </div>
    <div class="rev-filter">
      <button class="rf on" data-f="all" type="button">All {n_reviews}</button>
      <button class="rf" data-f="5" type="button">5★ only</button>
      <button class="rf" data-f="lt5" type="button">3★ &amp; 4★</button>
      <button class="rf" data-f="prod" type="button">Mentions a detector</button>
    </div>
    <div class="wall-grid" id="revwall">
      {quote_cards}
    </div>
    <div style="text-align:center;margin-top:30px">
      <button class="btn btn-line" id="revmore" type="button">Show more reviews</button>
    </div>

    <div class="sec-head" style="margin-top:70px">
      <div><div class="eyebrow">Match a review to a machine</div><h2>Read our verdict on what they bought</h2></div>
      <p>Customer service is one thing; the machine is another. Here's our own field-tested verdict on every detector we rank.</p>
    </div>
    <div class="rw-grid">
      {prod_widgets}
    </div>

    <div class="cta-band">
      <div><h3>Bought from us? Tell the truth.</h3><p>Good or bad, we publish what customers say — it's the only reason a dealer-run review site is worth reading.</p></div>
      <a class="btn btn-red" href="https://uk.trustpilot.com/evaluate/www.crawfordsmd.com" target="_blank" rel="noopener">Write a review</a>
    </div>
  </div>
</section>
{footer()}"""
    return head(
        "Crawfords Metal Detectors Reviews — {c} Verified Customer Reviews".format(c=tp['count']),
        "Read all {c} verified Trustpilot reviews of Crawfords Metal Detectors, plus our Google shop rating and Facebook recommendations — live, unedited.".format(c=tp['count']),
        path, schema,
    ) + body

def page_about():
    body = f"""{header("/about/")}
{p_hero('<a href="/">Home</a> / About', 'Editorial Policy, Methodology &amp; Ownership',
        'Who we are, how we score, and why a dealer-run review site tells you so — on every page.')}
<div class="article">
  <h2 id="ownership">Ownership — disclosed, not hidden</h2>
  <p>crawfordsmetaldetectorsreviews.co.uk is owned and written by <b>Crawfords Metal Detectors</b> (crawfordsmd.com) — an authorised Minelab distributor since 2014, an official stockist of XP and Nokta, and a UK detecting retailer trading since 1995 from Scunthorpe, North Lincolnshire. We test and sell the products we review, and we say so on every page. Three decades of hands-on dealer experience is the whole point of this site — not something to disguise.</p>
  <h2 id="how-we-score">How we score</h2>
  <p>Every machine gets an <b>editorial score out of 5</b>, set by our testing team across four weighted sub-scores: depth, separation, ease of use, and value. The score is a judgement made by people who sell, service and swing these machines weekly — it is <b>not</b> an automated average of customer review counts. Scores use the full range: a 3.6 is still a machine we're happy to sell, but we say plainly where it gives ground to the machines above it. New releases carry an "early verdict" until they've had a full season in UK soil.</p>
  <ul>
    <li><b>Depth</b> — real-world detection depth on our Lincolnshire test ground, not air-test hype.</li>
    <li><b>Separation</b> — target recovery in dense iron; the difference between finding the hammered coin and walking past it.</li>
    <li><b>Ease of use</b> — how quickly a newcomer gets genuinely productive.</li>
    <li><b>Value</b> — what the machine delivers against its current market position (live prices are always on crawfordsmd.com).</li>
  </ul>
  <h2>Freshness</h2>
  <p>Review content goes stale faster than blog content. Every published review gets a <b>monthly refresh pass</b> — stock status, new customer quotes, and re-tested notes where firmware or bundles change — with the "last re-tested" date shown under every headline. Stock data across the site was last synced on <b>{TODAY}</b>.</p>
  <h2>Customer quotes</h2>
  <p>Verified quotes come from our public Trustpilot, Google Business and Facebook profiles, always dated, attributed and linked to the source review. Aggregate ratings shown sitewide are live figures, not snapshots.</p>
  <h2>Why no prices?</h2>
  <p>Detector prices and bundle offers move weekly. Rather than show you a stale number, every "Buy at Crawfords" button links to the live product page at crawfordsmd.com, where price and stock are always current.</p>
  <div class="cta-band">
    <div><h3>Questions about anything here?</h3><p>Call the team on {esc(STORE['phone'])} · {esc(STORE['hours'])}</p></div>
    <a class="btn btn-red" href="{shop_url('')}" target="_blank" rel="noopener">Visit crawfordsmd.com</a>
  </div>
</div>
{footer()}"""
    return head(
        "About Crawfords Metal Detector Reviews — Editorial Policy & Methodology",
        "Who writes Crawfords' metal detector reviews, how the editorial scores work, and our full ownership disclosure as an authorised Minelab and XP dealer.",
        "/about/", [crumb_schema([("Home", "/"), ("About", None)])],
    ) + body

def page_privacy():
    path = "/privacy/"
    schema = [webpage_schema("Privacy & Cookie Policy", "How Crawfords Metal Detector Reviews uses cookies and handles data.", path),
              crumb_schema([("Home", "/"), ("Privacy & Cookies", None)])]
    body = f"""{header("")}
{p_hero('<a href="/">Home</a> / Privacy &amp; Cookies', 'Privacy &amp; Cookie Policy',
        'What we collect, why, and how to change your mind — in plain English.')}
<div class="article">
  <h2>Who we are</h2>
  <p>This site is owned and operated by <b>Crawfords Metal Detectors</b> (Crawfords Electronics Limited, company number 04361857), Unit 11 Weaver Court, Sawcliffe Industrial Park, Scunthorpe, North Lincolnshire, DN15 8RN. Contact: <b>{esc(STORE['phone'])}</b> or sales@crawfordsmd.com.</p>

  <h2>Cookies we use</h2>
  <table class="spec">
    <tr><th>Type</th><th>Purpose</th><th>Consent needed?</th></tr>
    <tr><td>Essential</td><td>Remembering your cookie choice so we don't ask on every page.</td><td>No — strictly necessary</td></tr>
    <tr><td>Analytics (Google Analytics 4)</td><td>Anonymous statistics on which reviews and guides people read, so we know what to write next.</td><td class="win">Yes — only set if you accept</td></tr>
  </table>
  <p>We use <b>Google Consent Mode v2</b>: analytics cookies are blocked by default and only load if you choose "Accept all". If you choose "Reject non-essential", no analytics cookies are set and Google receives no identifying data from your visit.</p>

  <h2>Changing your mind</h2>
  <p>Your choice is stored in your browser. To change it, clear this site's data in your browser settings (or use private browsing) and the banner will appear again on your next visit.</p>

  <h2>Links to our shop</h2>
  <p>Every "Buy at Crawfords" link takes you to crawfordsmd.com and carries a referral tag so we can see which reviews are useful. It contains no personal information about you. Once you arrive at crawfordsmd.com, that site's own privacy policy applies.</p>

  <h2>Your rights</h2>
  <p>Under UK GDPR you can ask what data we hold about you, ask us to correct or delete it, and complain to the Information Commissioner's Office (ico.org.uk). For anything relating to this site, email sales@crawfordsmd.com or call {esc(STORE['phone'])}.</p>

  <p class="disclosure-line">{DISCLOSURE}</p>
</div>
{footer()}"""
    return head("Privacy & Cookie Policy | Crawfords Metal Detector Reviews",
                "How Crawfords Metal Detector Reviews uses cookies, our Google Consent Mode v2 setup, and your rights under UK GDPR.",
                path, schema) + body

def page_404():
    body = f"""{header("")}
<section style="text-align:center;padding:120px 28px">
  <h2 style="font-size:40px">Signal lost — page not found</h2>
  <p style="margin:16px 0 30px;color:#4a5a66">Even the best detectorists dig the odd ring pull. Try the leaderboard instead.</p>
  <a class="btn btn-blue" href="/">Back to the Leaderboard</a>
</section>
{footer()}"""
    return head("Page not found | Crawfords Metal Detector Reviews",
                "Page not found.", "/404.html") + body

# ─────────────────────────────────────────────── build ──

PAGES = {
    "index.html": page_home,
    "reviews/index.html": page_reviews_index,
    "comparisons/index.html": page_comparisons_index,
    "comparisons/xp-deus-2-vs-minelab-manticore/index.html": page_deus_vs_manticore,
    "best/index.html": page_best,
    "guides/index.html": page_guides,
    "brands/index.html": page_brands,
    "customer-reviews/index.html": page_trust,
    "about/index.html": page_about,
    "privacy/index.html": page_privacy,
    "404.html": page_404,
}
for _slug, _p in P.items():
    if _slug in REVIEWS:
        PAGES[f"reviews/{_p['review_slug']}/index.html"] = (lambda sl: (lambda: page_review(sl)))(_slug)
for _slug in GUIDES:
    PAGES[f"guides/{_slug}/index.html"] = (lambda sl: (lambda: page_guide(sl)))(_slug)
for _slug in COMPARISONS:
    PAGES[f"comparisons/{_slug}/index.html"] = (lambda sl: (lambda: page_comparison_article(sl)))(_slug)

def build():
    # BASE_PATH: prefix for internal links, e.g. "/crawfords-reviews-preview"
    # when serving from a github.io project subpath instead of the custom domain.
    # PREVIEW=1: adds noindex (previews must never compete with the real site).
    base = os.environ.get("BASE_PATH", "").rstrip("/")
    preview = os.environ.get("PREVIEW") == "1"
    for rel, fn in PAGES.items():
        path = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
        out = fn()
        if base:
            out = out.replace('href="/', f'href="{base}/').replace('src="/', f'src="{base}/')
        if preview:
            out = out.replace("</title>", '</title>\n<meta name="robots" content="noindex, nofollow">')
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"  built {rel}")
    if preview:
        open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
            "User-agent: *\nDisallow: /\n")
        cn = os.path.join(ROOT, "CNAME")
        if os.path.exists(cn):
            os.remove(cn)
        for f in ("sitemap.xml",):
            fp = os.path.join(ROOT, f)
            if os.path.exists(fp):
                os.remove(fp)
        print("  preview mode: noindex, no CNAME, no sitemap")
        return

    urls = sorted(("/" if rel == "index.html" else "/" + rel.replace("index.html", ""))
                  for rel in PAGES if rel != "404.html")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{TODAY}</lastmod></url>")
    sm.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm))
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    open(os.path.join(ROOT, "CNAME"), "w", encoding="utf-8").write(
        "crawfordsmetaldetectorsreviews.co.uk\n")
    print("  built sitemap.xml, robots.txt, CNAME")
    print(f"Done — {len(PAGES)} pages generated. Data last synced {TODAY}.")

if __name__ == "__main__":
    build()
