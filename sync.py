#!/usr/bin/env python3
"""
Weekly data sync for crawfordsmetaldetectorsreviews.co.uk
=========================================================
Refreshes five things, then build.py regenerates the site:

  1. Product stock       — from each crawfordsmd.com product page
  2. Product prices      — monitored for CHANGES only. Prices are deliberately
                           NOT published on the review site (they move weekly and
                           the site links to live product pages instead), but a
                           change is flagged in the report so the team knows to
                           re-check the copy — e.g. a "best value" claim.
  3. Review platforms    — Trustpilot + Google shop rating and review counts
  4. Crawfords blog      — new posts on crawfordsmd.com/blog, surfaced on our
                           Blog page as "Latest from the Crawfords blog"
  5. Review corpus       — full review bodies from Trustpilot (3-star minimum),
                           de-duplicated, newest first, with product mentions
                           auto-linked to our own verdict pages

FAILS SAFE. If a source can't be reached (crawfordsmd.com's firewall blocks
datacenter IPs, Trustpilot bot-checks, etc.) the existing data is kept, the
source is listed as UNREACHED in the report, and the site still deploys.
Nothing on the site ever goes blank or stale-but-silent.

Usage:  python3 sync.py          then  python3 build.py
"""
import json, os, re, sys, urllib.request, urllib.error
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(ROOT, "data", "products.json")
BLOG_PATH = os.path.join(ROOT, "data", "shop_blog.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 CMD-ReviewsSiteSync/2.0")

TRUSTPILOT_URL = "https://uk.trustpilot.com/review/www.crawfordsmd.com"
GOOGLE_STORE_URL = "https://www.google.com/storepages?q=crawfordsmd.com&c=GB&v=19"
BLOG_URL = "https://crawfordsmd.com/blog"

report = {"changed": [], "unreached": [], "ok": []}


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Language": "en-GB,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def text_of(html_str):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", html_str, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


# ── 1 + 2. product stock and price ───────────────────────────────────
def stock_from(t):
    if re.search(r"out\s+of\s+stock", t, re.I):
        return "Out Of Stock"
    if re.search(r"pre-?order", t, re.I):
        return "Pre-Order"
    if re.search(r"in\s+stock", t, re.I):
        return "In Stock"
    return None


def price_from(t):
    m = re.search(r"£\s?([0-9][0-9,]*(?:\.[0-9]{2})?)", t)
    return ("£" + m.group(1)) if m else None


def sync_products(data):
    base = data["shop_base"]
    for p in data["products"]:
        url = base + p["shop_path"]
        try:
            t = text_of(fetch(url))
        except Exception as e:
            report["unreached"].append(f"product {p['slug']} ({str(e)[:60]})")
            continue

        stock = stock_from(t)
        if stock and stock != p.get("stock"):
            report["changed"].append(
                f"STOCK  {p['full_name']}: {p.get('stock')} -> {stock}"
                + ("   << decide: keep on site or move to 'retired'" if stock == "Out Of Stock" else ""))
            p["stock"] = stock

        price = price_from(t)
        if price:
            old = p.get("price_seen")
            if old and price != old:
                report["changed"].append(
                    f"PRICE  {p['full_name']}: {old} -> {price}"
                    "   << re-check any value/price claims in the review copy")
            p["price_seen"] = price   # monitored only — never rendered on the site
        report["ok"].append(p["slug"])


# ── 3. review platforms ──────────────────────────────────────────────
def sync_trustpilot(data):
    try:
        t = text_of(fetch(TRUSTPILOT_URL))
    except Exception as e:
        report["unreached"].append(f"Trustpilot ({str(e)[:60]})")
        return
    m = re.search(r"Reviews\s*([0-9][0-9,]*)\s*[•·]\s*([0-9](?:\.[0-9])?)", t)
    if not m:
        report["unreached"].append("Trustpilot (rating/count not found — page layout may have changed)")
        return
    count, rating = m.group(1), m.group(2)
    tp = data["platforms"]["trustpilot"]
    if (rating, count) != (tp.get("rating"), tp.get("count")):
        report["changed"].append(f"TRUSTPILOT: {tp.get('rating')}/{tp.get('count')} -> {rating}/{count}")
        tp["rating"], tp["count"] = rating, count
    report["ok"].append("trustpilot")


def sync_google(data):
    try:
        t = text_of(fetch(GOOGLE_STORE_URL))
    except Exception as e:
        report["unreached"].append(f"Google shop rating ({str(e)[:60]})")
        return
    m = re.search(r"([0-9]\.[0-9])\s*shop rating\s*\(([0-9][0-9,]*)\s*reviews\)", t, re.I)
    if not m:
        m2 = re.search(r"([0-9]\.[0-9]).{0,40}?([0-9][0-9,]{2,})\s*reviews", t, re.I)
        m = m2
    if not m:
        report["unreached"].append("Google shop rating (not found — page layout may have changed)")
        return
    rating, count = m.group(1), m.group(2)
    g = data["platforms"]["google"]
    if (rating, count) != (g.get("rating"), g.get("count")):
        report["changed"].append(f"GOOGLE: {g.get('rating')}/{g.get('count')} -> {rating}/{count}")
        g["rating"], g["count"] = rating, count
    report["ok"].append("google")


def recompute_blended(data):
    """Blended = Trustpilot + Google Business + Facebook counts.
    The Google *shop* rating aggregates Trustpilot, so it is not added again."""
    def n(x):
        try:
            return int(str(x).replace(",", ""))
        except Exception:
            return 0
    p = data["platforms"]
    total = n(p["trustpilot"]["count"]) + 153 + n(p["facebook"]["count"])
    formatted = f"{total:,}"
    if formatted != p["blended"].get("count"):
        report["changed"].append(f"BLENDED count: {p['blended'].get('count')} -> {formatted}")
        p["blended"]["count"] = formatted


# ── 4. Crawfords blog ────────────────────────────────────────────────
def sync_blog():
    try:
        html_str = fetch(BLOG_URL)
    except Exception as e:
        report["unreached"].append(f"Crawfords blog ({str(e)[:60]})")
        return
    posts, seen = [], set()
    for href, label in re.findall(r'<a[^>]+href="([^"]*/blog/[^"#?]+)"[^>]*>(.*?)</a>', html_str, re.S | re.I):
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", label)).strip()
        if not title or len(title) < 12:
            continue
        url = href if href.startswith("http") else "https://crawfordsmd.com" + href
        if url in seen:
            continue
        seen.add(url)
        posts.append({"title": title, "url": url})
        if len(posts) >= 12:
            break
    if not posts:
        report["unreached"].append("Crawfords blog (no posts parsed — layout may have changed)")
        return

    old = []
    if os.path.exists(BLOG_PATH):
        try:
            old = json.load(open(BLOG_PATH, encoding="utf-8")).get("posts", [])
        except Exception:
            old = []
    old_urls = {p["url"] for p in old}
    new = [p for p in posts if p["url"] not in old_urls]
    for p in new:
        report["changed"].append(f"NEW BLOG POST: {p['title'][:70]}")
    json.dump({"updated": str(date.today()), "posts": posts},
              open(BLOG_PATH, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    report["ok"].append("blog")




# ── 5. Trustpilot review corpus (bodies, not just the rating) ────────
TP_PAGES = 11          # ~24 reviews per page
MIN_RATING = 3         # editorial rule: never publish 1-2 star reviews
REVIEWS_PATH = os.path.join(ROOT, "data", "reviews.json")

PRODUCT_KEYWORDS = {
    "minelab-manticore":    ["manticore"],
    "minelab-equinox-900":  ["equinox 900", "equinox 700", "equinox 800", "nox 800", "nox800", "equinox"],
    "minelab-x-terra-elite":["x-terra elite", "xterra elite", "x terra elite"],
    "minelab-x-terra-pro":  ["x-terra pro", "xterra pro"],
    "nokta-legend-2":       ["legend"],
    "simplex-ultra":        ["simplex"],
    "xp-deus2":             ["deus 2", "deus2", "deus ii"],
    "xp-icon-x":            ["icon x"],
}


def _match_product(text):
    low = text.lower()
    for slug, kws in PRODUCT_KEYWORDS.items():
        if any(k in low for k in kws):
            return slug
    return None


def sync_review_corpus():
    """Harvest review bodies from Trustpilot's embedded __NEXT_DATA__ JSON.

    Only 3-star-and-above reviews are kept. That is an editorial decision,
    not a technical one: the site publishes genuine reviews but does not
    lead with one-star outliers. Never synthesise reviews to pad this file
    — fabricated reviews are illegal under the UK DMCC Act 2024 and would
    destroy the credibility the whole site is built on.
    """
    collected = []
    for page in range(1, TP_PAGES + 1):
        url = (f"{TRUSTPILOT_URL}?stars=3&stars=4&stars=5&page={page}")
        try:
            html_str = fetch(url)
        except Exception as e:
            report["unreached"].append(f"Trustpilot reviews p{page} ({str(e)[:50]})")
            break
        m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
                      html_str, re.S)
        if not m:
            report["unreached"].append(f"Trustpilot reviews p{page} (no __NEXT_DATA__ — layout changed)")
            break
        try:
            revs = json.loads(m.group(1))["props"]["pageProps"]["reviews"]
        except Exception:
            report["unreached"].append(f"Trustpilot reviews p{page} (unexpected JSON shape)")
            break
        for x in revs:
            body = (x.get("text") or "").strip()
            rating = x.get("rating") or 0
            if not body or rating < MIN_RATING:
                continue
            collected.append({
                "n": (x.get("consumer") or {}).get("displayName", "Customer"),
                "r": int(rating),
                "d": (x.get("dates") or {}).get("publishedDate", "")[:10],
                "b": re.sub(r"\s+", " ", body)[:400],
            })

    if not collected:
        report["unreached"].append("Trustpilot review corpus (kept existing reviews.json)")
        return

    # de-duplicate, newest first, tag product mentions
    seen, out = set(), []
    for x in sorted(collected, key=lambda z: z["d"], reverse=True):
        key = (x["n"], x["d"], x["b"][:40])
        if key in seen:
            continue
        seen.add(key)
        x["p"] = _match_product(x["b"])
        out.append(x)

    old_n = 0
    if os.path.exists(REVIEWS_PATH):
        try:
            old = json.load(open(REVIEWS_PATH, encoding="utf-8"))
            old_keys = {(r["n"], r["d"], r["b"][:40]) for r in old.get("reviews", [])}
            old_n = len(old.get("reviews", []))
            fresh = [x for x in out if (x["n"], x["d"], x["b"][:40]) not in old_keys]
            for f in fresh[:5]:
                report["changed"].append(f"NEW REVIEW: {f['r']}\u2605 {f['n']} \u2014 {f['b'][:60]}")
            if len(fresh) > 5:
                report["changed"].append(f"...and {len(fresh)-5} more new reviews")
        except Exception:
            pass

    if len(out) != old_n:
        report["changed"].append(f"REVIEW CORPUS: {old_n} -> {len(out)} reviews")
    json.dump({"source": "Trustpilot", "profile": TRUSTPILOT_URL,
               "fetched": str(date.today()), "min_rating": MIN_RATING,
               "count": len(out), "reviews": out},
              open(REVIEWS_PATH, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    report["ok"].append(f"review corpus ({len(out)})")


# ── main ─────────────────────────────────────────────────────────────
def main():
    data = json.load(open(DATA_PATH, encoding="utf-8"))
    sync_products(data)
    sync_trustpilot(data)
    sync_google(data)
    recompute_blended(data)
    sync_blog()
    sync_review_corpus()

    if report["ok"]:
        data["last_synced"] = str(date.today())
    json.dump(data, open(DATA_PATH, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    lines = [f"# Weekly sync — {date.today()}", ""]
    lines.append(f"**Sources reached:** {len(report['ok'])}  ·  "
                 f"**Changes:** {len(report['changed'])}  ·  "
                 f"**Unreached:** {len(report['unreached'])}")
    lines.append("")
    if report["changed"]:
        lines.append("## Changes applied")
        lines += [f"- {c}" for c in report["changed"]]
        lines.append("")
    else:
        lines.append("_No changes this week._\n")
    if report["unreached"]:
        lines.append("## Could not reach (existing data kept)")
        lines += [f"- {u}" for u in report["unreached"]]
        lines.append("")
        lines.append("> If these persist, the source is blocking the GitHub runner. "
                     "Run `python3 sync.py && python3 build.py` from an office machine and push.")
    out = "\n".join(lines)
    print(out)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(out + "\n")

    sys.exit(0)   # never break the deploy


if __name__ == "__main__":
    main()
