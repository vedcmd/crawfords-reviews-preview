# -*- coding: utf-8 -*-
"""
Editorial content for the Crawfords Reviews site.
Separated from build.py so content edits never touch template code.
Facts sourced from crawfordsmd.com brand/category page content (Jul 2026)
and the CMD comparison blog assets. Dealer status: Crawfords is an
authorised Minelab dealer/distributor ONLY; XP and Nokta are stocked
and supported but NOT authorised-dealer relationships.
"""

DISCLOSURE = ("Crawfords Metal Detectors is an authorised Minelab dealer and an "
              "official stockist of XP and Nokta. We test and sell the products we review.")

# ── Per-product review pages ─────────────────────────────────────────
REVIEWS = {
  "minelab-manticore": {
    "h1": "Minelab Manticore Review: Is It Worth the Upgrade?",
    "sub": "The most information-rich detector we’ve ever sold — tested on Lincolnshire pasture, iron-heavy Roman scatter and North Sea wet sand.",
    "verdict_head": "The premium benchmark — and worth it for the right detectorist",
    "bestfor": "experienced detectorists on mineralised pasture and iron-heavy sites who want the most target information money can buy.",
    "chips": [("Multi-IQ+", "Simultaneous multi-frequency"), ("5m", "Waterproof rating"), ("M11 coil", "28cm standard"), ("3-year", "Minelab warranty")],
    "pros": ["2D target trace ID is a genuine step-change on iffy, deep targets",
             "Multi-IQ+ noticeably stronger than Equinox on mineralised ground",
             "Superb ferrous separation on Roman and medieval scatter sites",
             "All-terrain: submersible to 5m with beach-specific modes"],
    "cons": ["Menu depth takes a good few outings to master — ease of use scores 3.9 for a reason",
             "Premium price — the Equinox 900 covers 90% of hunts for less",
             "Standard coil options narrower than the Deus II ecosystem"],
    "capsule": "Yes — if you hunt difficult ground. The Manticore’s Multi-IQ+ engine and 2D target trace deliver clearer information on deep, masked and iron-adjacent targets than anything else we stock. Casual detectorists will be equally happy with the Equinox 900 for less.",
    "testing": [
      ("Depth &amp; ground handling", "On our mineralised Lincolnshire test paddock the Manticore held stable IDs at depths where single-frequency machines were guessing. Ground balance is quick and holds well across ploughed and pasture transitions."),
      ("Discrimination &amp; separation", "This is where the money goes. The 2D target trace plots ferrous and conductive properties on two axes, so a hammered coin sitting beside a nail reads as two distinct events rather than one mushy tone. Recovery speed on the standard M11 coil kept pace through dense iron."),
      ("Build &amp; ergonomics", "Balance is good, the display is readable in low winter sun, and the whole unit is submersible to 5m — wet sand and shallow surf are on the menu. The menu system is deep; give yourself three or four outings before judging it."),
    ],
    "specs": [("Technology", "Multi-IQ+ simultaneous multi-frequency"),
              ("Target ID", "2D target trace + numeric ID"),
              ("Standard coil", "M11 — 28cm (11\") Double-D"),
              ("Waterproof", "Submersible to 5m"),
              ("Audio", "Built-in speaker, Bluetooth low-latency wireless"),
              ("Warranty", "3-year Minelab manufacturer warranty via Crawfords (authorised dealer)")],
    "compare_note": "Deciding between the flagships? Read the <a href='/comparisons/xp-icon-x-vs-minelab-manticore/'>XP ICON X vs Manticore comparison</a> or the <a href='/comparisons/xp-deus-2-vs-minelab-manticore/'>Deus 2 head-to-head</a>.",
    "faqs": [
      ("Is the Manticore better than the Equinox 900?",
       "On difficult, mineralised or iron-heavy ground, yes — the Multi-IQ+ implementation is stronger and the 2D target trace gives you more to work with. On easier ground the gap narrows considerably, which is why the Equinox 900 remains our best all-terrain pick."),
      ("Is Multi-IQ+ the same as Multi-IQ?",
       "No. Multi-IQ+ is the higher-powered engine found only in the Manticore and Equinox 900. Multi-IQ (without the plus) is the technology in the X-Terra Elite and Vanquish series. Both are simultaneous multi-frequency, but they are not the same platform."),
      ("Can I use the Manticore on the beach?",
       "Yes — it has dedicated beach modes for dry sand, wet sand and surf, and the whole unit is submersible to 5m. On mineralised black-sand patches, Multi-IQ+ keeps IDs usable where single-frequency machines fall apart."),
      ("Does Crawfords offer a warranty on the Manticore?",
       "Yes — as an authorised Minelab dealer since 2014, every Manticore we sell carries the full 3-year manufacturer warranty, with service support through our Scunthorpe store (01724 845608)."),
    ],
    "final": "The Manticore is the best detector we’ve ever scored — <b>4.8/5</b> — and the premium is justified for detectorists who hunt hard ground and want every scrap of target information available. If that’s not you yet, the Equinox 900 is the smarter spend. Either way, you get three decades of Crawfords backup behind it.",
  },

  "minelab-equinox-900": {
    "h1": "Minelab Equinox 900 Review: Multi-IQ+ Tested on UK Ground",
    "sub": "The all-terrain benchmark — flagship-grade Multi-IQ+ without the flagship price, tested inland and on North Sea beaches.",
    "verdict_head": "The one machine most serious detectorists should actually buy",
    "bestfor": "detectorists who want a single machine that handles pasture, ploughed fields and wet sand without compromise.",
    "chips": [("Multi-IQ+", "Simultaneous multi-frequency"), ("5m", "Waterproof rating"), ("11\" coil", "EQX Double-D standard"), ("3-year", "Minelab warranty")],
    "pros": ["Genuine Multi-IQ+ — the same engine family as the Manticore",
             "The best wet-sand stability in its class; beach modes genuinely work",
             "Simpler, faster to learn than the Manticore",
             "Strong value against every flagship it undercuts"],
    "cons": ["Numeric target ID only — no 2D target trace",
             "Wired coil where the XP platform is fully wireless",
             "If you already own an Equinox 800, the upgrade case is narrower"],
    "capsule": "The Equinox 900 is the best all-round detector we sell: Multi-IQ+ performance across every UK terrain, 5m submersion and beach modes that actually hold up on wet salt sand. Only detectorists chasing maximum target information need to spend more on the Manticore.",
    "testing": [
      ("All-terrain performance", "Multi-frequency is what separates this machine from single-frequency rivals: on our test ground it held stable, repeatable IDs through mineralisation that forced single-frequency machines to be desensitised into blindness."),
      ("On the beach", "Saltwater is conductive and wet sand behaves like a large diffuse target to lesser machines. The 900’s dedicated beach modes kept falsing under control on wet sand where it matters — this is the machine we most often recommend to coastal customers."),
      ("Handling &amp; learning curve", "Menus are logical and shallow enough to learn in an afternoon. It is noticeably easier to get productive with than the Manticore, which is exactly why it scores 4.4 for ease of use against the flagship’s 3.9."),
    ],
    "specs": [("Technology", "Multi-IQ+ simultaneous multi-frequency"),
              ("Target ID", "Expanded numeric ID"),
              ("Standard coil", "11\" EQX Double-D"),
              ("Waterproof", "Submersible to 5m"),
              ("Audio", "Built-in speaker, Bluetooth wireless"),
              ("Warranty", "3-year Minelab manufacturer warranty via Crawfords (authorised dealer)")],
    "compare_note": "See how it fares against the value challenger in <a href='/comparisons/nokta-legend-2-vs-minelab-equinox-900/'>Legend 2 vs Equinox 900</a>.",
    "faqs": [
      ("Is the Equinox 900 good for beaches?",
       "Yes — this is its strongest suit relative to price. Simultaneous multi-frequency plus dedicated wet-sand and surf modes keep it stable on conductive salt sand, and the whole unit submerges to 5m."),
      ("Equinox 900 or Manticore?",
       "The Manticore adds the 2D target trace and a stronger Multi-IQ+ implementation for difficult ground — at a meaningful premium. If you hunt averagely difficult permissions, the 900 does the job; our full Manticore review covers when the upgrade is worth it."),
      ("What is the difference between Multi-IQ+ and Multi-IQ?",
       "Multi-IQ+ (Equinox 900, Manticore) is the newer, higher-powered engine. Multi-IQ (X-Terra Elite, Vanquish) is still simultaneous multi-frequency but on the previous platform."),
    ],
    "final": "<b>4.6/5.</b> The Equinox 900 is the machine we recommend more than any other above entry level: nearly all of the flagship performance, most of the ease, and a price that leaves money for a pinpointer and a spade.",
  },

  "xp-deus2": {
    "h1": "XP Deus II Review: The Featherweight Flagship",
    "sub": "Fully wireless, absurdly light and rated to 20 metres — the French flagship tested through Lincolnshire iron and open water.",
    "verdict_head": "The lightest serious detector ever made — and a diver’s only real choice",
    "bestfor": "experienced detectorists who swing long sessions, hunt dense iron, or need genuine deep-water capability.",
    "chips": [("FMF", "Fast multi-frequency"), ("20m", "Waterproof rating"), ("Wireless", "Coil-to-remote radio link"), ("5-year", "XP manufacturer warranty")],
    "pros": ["Fully wireless platform — no cables, less weight, less to fail",
             "Fastest recovery speed in dense iron we have tested",
             "Submersible to 20m — in a different class for divers",
             "5-year XP manufacturer warranty, the longest of any major brand"],
    "cons": ["Ease of use 3.8: the settings depth rewards experience and punishes impatience",
             "Numeric ID gives less target information than the Manticore’s 2D trace",
             "Flagship pricing against the Equinox 900’s all-round value"],
    "capsule": "The Deus II is the recovery-speed king: XP’s FMF multi-frequency in a fully wireless package that weighs less than anything comparable and submerges to 20 metres. It rewards experienced hands; newcomers get productive faster on the Minelab platform.",
    "testing": [
      ("Weight &amp; ergonomics", "XP pioneered wireless detecting in 2009 with the original Deus, and the benefit is still obvious: after a six-hour session the difference against a standard-class machine is felt in the shoulder, not read on a spec sheet."),
      ("Iron-infested ground", "On medieval scatter thick with nails, recovery speed is what finds the coin beside the iron — and this is the fastest machine we test. Separation scored 4.8, the highest on our leaderboard."),
      ("In the water", "Rated to 20 metres, the Deus II is the only mainstream flagship genuinely built for diving. For wading and surf work the rating is academic overkill — which is exactly what you want."),
    ],
    "specs": [("Technology", "FMF — Fast Multi-Frequency"),
              ("Platform", "Fully wireless: coil, remote and headphones on a digital radio link"),
              ("Waterproof", "Submersible to 20m"),
              ("Made in", "France — designed and manufactured by XP"),
              ("Warranty", "5-year XP manufacturer warranty")],
    "compare_note": "Choosing a flagship? Read the full <a href='/comparisons/xp-deus-2-vs-minelab-manticore/'>Deus 2 vs Manticore head-to-head</a>.",
    "faqs": [
      ("Is the XP Deus II good for UK beaches?",
       "Yes — FMF multi-frequency handles wet salt sand well, and the 20m rating means surf and rock pools hold no fear. For pure beach work the Equinox 900 gets you most of the way for less."),
      ("Deus II or Manticore?",
       "Manticore for maximum target information on difficult inland ground; Deus II for weight, wireless freedom and anything underwater. Our head-to-head comparison covers it in full."),
      ("What warranty does the Deus II carry?",
       "XP backs it with a 5-year manufacturer warranty — the longest standard warranty of any major detector brand. Crawfords stocks and supports the full XP range."),
    ],
    "final": "<b>4.6/5.</b> If your sessions are long, your permissions ironed-up, or your hunting takes you underwater, the Deus II justifies every penny. If none of those apply, the Equinox 900 remains the smarter first flagship.",
  },

  "minelab-x-terra-elite": {
    "h1": "Minelab X-Terra Elite Review: Mid-Range Multi-IQ",
    "sub": "Simultaneous multi-frequency and 5m submersion at a mid-range price — currently bundled with ML-85 wireless headphones.",
    "verdict_head": "The most detector per pound in the Minelab range",
    "bestfor": "improving detectorists who want genuine multi-frequency and full submersion without flagship spending.",
    "chips": [("Multi-IQ", "Simultaneous multi-frequency"), ("5m", "Waterproof rating"), ("ML-85", "Wireless headphones bundled"), ("3-year", "Minelab warranty")],
    "pros": ["Genuine Multi-IQ simultaneous multi-frequency at a mid-range price",
             "Fully submersible to 5m — beach-capable out of the box",
             "Current bundle includes ML-85 wireless headphones",
             "Value score 4.7 — it embarrasses machines a tier up"],
    "cons": ["Depth and separation sit clearly below the Multi-IQ+ machines",
             "Numeric ID is basic next to the flagships",
             "Coil options are limited against the Equinox ecosystem"],
    "capsule": "The X-Terra Elite brings Minelab’s Multi-IQ multi-frequency and 5m submersion down to a mid-range price. It will not out-dig an Equinox 900, but nothing else this side of one gets this close — which makes it our best-value Minelab and top beginner step-up pick.",
    "testing": [
      ("Where it wins", "The tech that matters — simultaneous multi-frequency — is real Multi-IQ, not marketing. On damp pasture and dry sand it behaves like a machine costing considerably more."),
      ("Where it gives ground", "Depth (4.1) and separation (4.0) are honest mid-range numbers: on heavily ironed sites the flagships pull identifiable signals this machine reads as mixed. That is the trade, and at this price it is a fair one."),
      ("The bundle", "The current ML-85 wireless headphone bundle is genuine added value — low-latency audio that would cost real money separately."),
    ],
    "specs": [("Technology", "Multi-IQ simultaneous multi-frequency"),
              ("Waterproof", "Submersible to 5m"),
              ("Audio", "ML-85 wireless headphones (current bundle), built-in speaker"),
              ("Warranty", "3-year Minelab manufacturer warranty via Crawfords (authorised dealer)")],
    "compare_note": "Weighing it against the rugged single-frequency option? See the <a href='/reviews/minelab-x-terra-pro-review/'>X-Terra Pro review</a>.",
    "faqs": [
      ("X-Terra Elite or X-Terra Pro?",
       "They share a family name but not a technology. The Elite runs Multi-IQ simultaneous multi-frequency; the Pro is Pro-Switch switchable single frequency. If beaches or mineralised ground feature in your plans, the Elite is worth the difference."),
      ("Is the X-Terra Elite waterproof?",
       "Yes — the whole unit is submersible to 5m, so wet sand, streams and shallow surf are all in play."),
      ("Is it a good first detector?",
       "It is our top beginner buy for anyone who can stretch to it — the one machine in our beginners guide you will not outgrow in a season."),
    ],
    "final": "<b>4.3/5.</b> The smartest money in the Minelab range. Buy it over the budget machines if you can; skip it only if the Equinox 900 is within reach.",
  },

  "nokta-legend-2": {
    "h1": "Nokta Legend 2 Review: Most Features Per Pound?",
    "sub": "Simultaneous multi-frequency, IP68 waterproofing and a spec sheet that undercuts the establishment — with a learning curve to match.",
    "verdict_head": "A serious spec sheet at a disruptive price — if you will tolerate the menus",
    "bestfor": "confident detectorists who want maximum features per pound and don’t mind tuning audio and menus to get them.",
    "chips": [("SMF", "Simultaneous multi-frequency"), ("IP68", "Fully waterproof"), ("Wireless", "Audio + rechargeable"), ("Value 4.8", "Highest on our board")],
    "pros": ["Genuine simultaneous multi-frequency at a price the big brands don’t match",
             "IP68 waterproofing — wet sand, rivers and UK weather all covered",
             "Wireless audio and rechargeable battery as standard",
             "Deep customisation for tinkerers"],
    "cons": ["Menus are fiddlier than the Minelabs — ease of use scores 3.8",
             "Audio needs tuning before it sings; out-of-the-box tones are divisive",
             "Depth and separation are good, not flagship"],
    "capsule": "The Legend 2 is Nokta’s value statement: real simultaneous multi-frequency, full waterproofing and wireless audio at a price that undercuts every comparable Minelab and XP. The trade is a fiddlier interface — which is why it scores 4.8 for value and 3.8 for ease.",
    "testing": [
      ("The value equation", "Nokta has built its reputation on shipping features competitors reserve for higher price brackets — SMF, waterproofing, wireless audio and rechargeable batteries across the range rather than only at the top. The Legend 2 is the clearest expression of that."),
      ("In the field", "Performance on ordinary pasture is genuinely close to machines costing more. Push into dense iron or hot ground and the flagships pull ahead on separation — 4.1 here against the Deus II’s 4.8 tells that story."),
      ("Living with it", "Expect to spend your first sessions in the settings. Owners who persist tend to love it; buyers expecting Minelab-style turn-on-and-go simplicity are the ones who return it."),
    ],
    "specs": [("Technology", "SMF — simultaneous multi-frequency"),
              ("Waterproof", "IP68 — fully submersible"),
              ("Audio", "Wireless audio support, built-in speaker"),
              ("Battery", "Internal rechargeable"),
              ("Warranty", "Manufacturer warranty, supported via Crawfords")],
    "compare_note": "The obvious cross-shop is covered in full: <a href='/comparisons/nokta-legend-2-vs-minelab-equinox-900/'>Legend 2 vs Equinox 900</a>.",
    "faqs": [
      ("Is the Legend 2 better than the Equinox 900?",
       "On price, comfortably. On performance and refinement, the Equinox 900 keeps the edge — our full comparison breaks down where each machine wins."),
      ("Is the Nokta Legend 2 waterproof?",
       "Yes — IP68 rated and fully submersible, so beaches, streams and British weather are all covered."),
      ("Is it beginner-friendly?",
       "Capable beginners manage, but the menu depth is real. If simplicity matters most, look at the Simplex Ultra or the Minelab machines first."),
    ],
    "final": "<b>4.2/5.</b> The best pure value on our leaderboard. Buy it for the spec sheet, keep it for the performance — just go in knowing the menus are part of the deal.",
  },

  "xp-icon-x": {
    "h1": "XP ICON X Review: First Field Test of XP’s New Release",
    "sub": "Deus II technology in a simpler, more affordable package — an early verdict after our first weeks field-side.",
    "verdict_head": "Early verdict: Deus DNA at a friendlier price — promising, not yet proven",
    "bestfor": "detectorists drawn to XP’s wireless, lightweight platform who don’t need the Deus II’s full modularity or dive rating.",
    "chips": [("FMF", "Fast multi-frequency"), ("Wireless", "XP platform"), ("Early verdict", "New release"), ("5-year", "XP manufacturer warranty")],
    "pros": ["XP’s FMF multi-frequency and wireless architecture below Deus II money",
             "Light, fast-handling and quick to start with",
             "Shares the XP ecosystem including MI-6 pinpointer compatibility",
             "5-year XP manufacturer warranty"],
    "cons": ["New release — long-term reliability and resale are unproven, hence the early-verdict tag",
             "Value scores 4.0 while launch pricing settles",
             "Accessory and coil ecosystem still smaller than the established platforms"],
    "capsule": "The ICON X packages XP’s Fast Multi-Frequency and wireless design into a simpler, more affordable machine than the Deus II. Early field results are promising; we hold the score at 4.2 until it has done a full season in UK soil.",
    "testing": [
      ("What it is — and isn’t", "This is not XP’s flagship: the Deus II remains the top of the range. The ICON X is the accessible route into the same FMF and wireless engineering, aimed at detectorists who found the Deus II’s price or complexity a step too far."),
      ("First weeks in the field", "Handling is classic XP — light, balanced, quick to recover. IDs on our test ground were stable and the learning curve is noticeably gentler than its big brother’s."),
      ("Why the early-verdict tag", "Scores on new releases firm up after a season of customer feedback, firmware updates and hard weather. We would rather hold at 4.2 and be right than headline-score a honeymoon."),
    ],
    "specs": [("Technology", "FMF — Fast Multi-Frequency"),
              ("Platform", "XP wireless architecture"),
              ("Made in", "France — designed and manufactured by XP"),
              ("Warranty", "5-year XP manufacturer warranty")],
    "compare_note": "How does it stack against our top score? Read <a href='/comparisons/xp-icon-x-vs-minelab-manticore/'>ICON X vs Manticore</a>.",
    "faqs": [
      ("Is the XP ICON X a flagship?",
       "No — the Deus II is XP’s flagship. The ICON X is the more affordable route into XP’s FMF multi-frequency and wireless platform."),
      ("ICON X or Deus II?",
       "Deus II for maximum capability, 20m waterproofing and the full modular ecosystem; ICON X for most of the character at a friendlier price."),
      ("Why is the score an early verdict?",
       "It is a new release. We re-score after a full season of UK use, customer feedback and firmware maturity — the 4.2 may move either way."),
    ],
    "final": "<b>4.2/5 (early verdict).</b> A genuinely promising new release that brings XP’s best ideas down the price ladder. We will re-score once it has a season behind it.",
  },

  "simplex-ultra": {
    "h1": "Nokta Simplex Ultra Review: Budget Waterproof All-Rounder",
    "sub": "The starter machine we recommend most often across the counter — simple, rugged, waterproof, and honest about its limits.",
    "verdict_head": "The best answer to “what should my first detector be?” on a real budget",
    "bestfor": "first-season detectorists and anyone who wants a rugged, waterproof machine with zero fuss.",
    "chips": [("Single freq", "Simple and stable inland"), ("Waterproof", "Fully submersible"), ("Ease 4.8", "Highest on our board"), ("Budget", "Entry price")],
    "pros": ["Ease of use 4.8 — switch on, ground balance, detect",
             "Fully waterproof — rivers, rain and dry beach work all fine",
             "Rugged build that shrugs off beginner treatment",
             "The machine our counter staff recommend most to first-timers"],
    "cons": ["Single frequency struggles on wet salt sand and hot mineralised ground",
             "Depth (3.5) and separation (3.4) are honest budget numbers",
             "You may outgrow it in a season or two of serious use"],
    "capsule": "The Simplex Ultra is the budget benchmark: waterproof, rugged and genuinely simple, it finds things from day one — the single most important quality in a first detector. Its single-frequency engine is the only real limit, and it only bites on wet sand and hot ground.",
    "testing": [
      ("Why beginners succeed with it", "A machine that beeps randomly and finds nothing discourages a beginner faster than anything else. The Simplex Ultra’s stability inland is exactly why it has become our default first recommendation."),
      ("Its honest limits", "Wet salt sand is conductive and defeats single-frequency machines — that is physics, not a flaw unique to Nokta. Dry sand is fine; serious beach ambitions need multi-frequency."),
      ("Build", "IP-rated, submersible and solid. Of everything at this price, it is the machine we least often see back for repair."),
    ],
    "specs": [("Technology", "Single frequency"),
              ("Waterproof", "Fully submersible"),
              ("Audio", "Built-in speaker, wireless-capable"),
              ("Warranty", "Manufacturer warranty, supported via Crawfords")],
    "compare_note": "Ready to see the step-up options? Start with our <a href='/best/'>beginners buying guide</a>.",
    "faqs": [
      ("Is the Simplex Ultra good for beginners?",
       "It is the machine we hand to first-timers more than any other. Simple controls, rugged build, and it finds things immediately — which is what keeps new detectorists in the hobby."),
      ("Can I use the Simplex Ultra on the beach?",
       "Dry sand, yes. Wet salt sand is hard on any single-frequency machine — if the tide line is your plan, budget for multi-frequency instead."),
      ("What would I upgrade to?",
       "The X-Terra Elite or Legend 2 for multi-frequency on a budget, or the Equinox 900 when you are ready for the all-terrain benchmark."),
    ],
    "final": "<b>3.9/5.</b> Judged as a first machine, it is close to faultless; judged against the multi-frequency board above it, the score is honest. Know which purchase you are making and you will not regret it.",
  },

  "minelab-x-terra-pro": {
    "h1": "Minelab X-Terra Pro Review: The Rugged Workhorse",
    "sub": "Pro-Switch switchable single frequency, waterproof to 5m, and nothing to go wrong — the no-nonsense field machine.",
    "verdict_head": "The simplest Minelab route into the hobby — dependable within its limits",
    "bestfor": "detectorists who want Minelab build and backup in a simple, rugged package for inland work.",
    "chips": [("Pro-Switch", "5/8/10/15 kHz switchable"), ("5m", "Waterproof rating"), ("Ease 4.7", "Turn on and go"), ("3-year", "Minelab warranty")],
    "pros": ["Rugged, waterproof to 5m, and genuinely simple to run",
             "Pro-Switch lets you match frequency to target type — a real feature, used properly",
             "Minelab dealer support and 3-year warranty behind it",
             "Ease of use 4.7 — nothing here intimidates a newcomer"],
    "cons": ["Switchable single frequency is not multi-frequency — wet sand and hot ground expose it",
             "Separation (3.2) is the lowest on our leaderboard",
             "The X-Terra Elite exists, and the upgrade case is strong"],
    "capsule": "The X-Terra Pro is a rugged, waterproof, switchable single-frequency machine — 5, 8, 10 or 15 kHz, one at a time. That is a genuine tool for inland work, and a genuine limit on wet sand. Simple, dependable, honest: a workhorse, not a thoroughbred.",
    "testing": [
      ("Pro-Switch in practice", "Switchable frequency is often confused with multi-frequency — it is not. You select one frequency at a time: lower for larger, deeper conductors, higher for small targets. Used deliberately, it works; it never processes several frequencies at once the way Multi-IQ does."),
      ("Where it earns its keep", "Dry pasture, stubble and parkland are its home. IDs are stable, the build shrugs off knocks and weather, and the 5m rating means rivers and rain never stop play."),
      ("Where it struggles", "Wet salt sand and heavily mineralised ground are single-frequency territory’s hard boundary — the falsing that results is physics. That is what the separation score reflects."),
    ],
    "specs": [("Technology", "Pro-Switch switchable single frequency — 5/8/10/15 kHz"),
              ("Waterproof", "Submersible to 5m"),
              ("Audio", "Built-in speaker, wireless-capable"),
              ("Warranty", "3-year Minelab manufacturer warranty via Crawfords (authorised dealer)")],
    "compare_note": "Torn between the X-Terras? The <a href='/reviews/minelab-x-terra-elite-review/'>Elite review</a> covers the multi-frequency case.",
    "faqs": [
      ("Is the X-Terra Pro multi-frequency?",
       "No — this is the most common misunderstanding about it. Pro-Switch is switchable single frequency: you choose one of 5, 8, 10 or 15 kHz at a time. Simultaneous multi-frequency is the X-Terra Elite and up."),
      ("Is the X-Terra Pro waterproof?",
       "Yes — the whole unit is submersible to 5m."),
      ("X-Terra Pro or Simplex Ultra?",
       "Very close call at the budget end: the Nokta is simpler still and cheaper; the Minelab buys you Pro-Switch flexibility and Minelab’s dealer network. Neither handles wet salt sand well."),
    ],
    "final": "<b>3.6/5.</b> The lowest score on our board — and still a machine we happily sell every week. It does exactly what it claims, lasts for years, and costs little. Just be sure single frequency suits the ground you actually hunt.",
  },
}

# ── Blog / guide articles ────────────────────────────────────────────
# Sourced/condensed from crawfordsmd.com category page content (Jul 2026).
GUIDES = {
  "multi-frequency-vs-single-frequency": {
    "title": "Multi-Frequency vs Single Frequency: Which Do You Actually Need?",
    "desc": "Multi-IQ, Multi-IQ+, FMF, SMF and Pro-Switch explained in plain English — what the badges mean and when multi-frequency is worth paying for.",
    "kicker": "Technology",
    "date": "2026-07-31",
    "body": """
<p>Every detector brand has its own badge for frequency technology, and the naming does more to confuse buyers than any other spec. Here is the plain-English version.</p>
<h2>Single frequency</h2>
<p>The detector transmits one signal into the ground. Simple, stable and cheap — and entirely adequate for dry inland ground. The limits appear on conductive wet salt sand and heavily mineralised soil, where a single frequency either falses constantly or has to be desensitised until it finds little. The <a href="/reviews/nokta-simplex-ultra-review/">Simplex Ultra</a> is our benchmark single-frequency machine.</p>
<h2>Switchable single frequency — Pro-Switch</h2>
<p>A common misunderstanding: Minelab’s Pro-Switch (<a href="/reviews/minelab-x-terra-pro-review/">X-Terra Pro</a>) lets you choose 5, 8, 10 or 15 kHz — <b>one at a time</b>. Lower frequencies favour larger, deeper conductors; higher frequencies favour small targets. It is a genuine tool, but it is not multi-frequency, and it shares single frequency’s wet-sand limits.</p>
<h2>Simultaneous multi-frequency</h2>
<p>The machine transmits and processes several frequencies at once, which is what keeps IDs stable on mineralised and salt-wet ground. The badges: Minelab’s <b>Multi-IQ</b> (X-Terra Elite, Vanquish) and higher-powered <b>Multi-IQ+</b> (Equinox 900, Manticore — those two only); XP’s <b>FMF</b> (Deus II, ICON X); Nokta’s <b>SMF</b> (Legend 2). All are simultaneous multi-frequency; they are not the same platform, and the implementations differ in refinement.</p>
<h2>So which do you need?</h2>
<p>Inland-only on ordinary soil: single frequency is fine, and the savings are real. If wet-sand beaches or mineralised ground feature anywhere in your plans, multi-frequency is worth the stretch — it is the single most consequential spec on the sheet. Our <a href="/best/">beginners guide</a> and <a href="/">leaderboard</a> mark the technology on every machine.</p>
""",
  },
  "beach-metal-detecting-uk": {
    "title": "Beach Metal Detecting in the UK: Why the Beach Beats Most Machines",
    "desc": "Saltwater conductivity, black sand and the three technologies that cope — what actually matters when choosing a beach metal detector for UK coasts.",
    "kicker": "Beach detecting",
    "date": "2026-07-31",
    "body": """
<p>Beach detecting demands more from a machine than any other UK environment — and it defeats detectors that perform perfectly well inland.</p>
<h2>Why beaches are hard</h2>
<p>Saltwater conducts electricity. A detector works by generating an electromagnetic field and reading the response; wet salt sand responds as though it were itself a large, diffuse metal target. A single-frequency machine reads constant signal where there is nothing, and either becomes unusable or must be desensitised to the point of finding little. Black sand — heavily mineralised with iron oxides — compounds the problem.</p>
<h2>What copes</h2>
<p>Three technologies handle it: <b>simultaneous multi-frequency</b>, which processes several frequencies at once and separates ground response from target response; <b>dedicated beach modes</b>, which bias the processing for salt; and <b>pulse induction</b>, the specialist route. On our leaderboard, the <a href="/reviews/minelab-equinox-900-review/">Equinox 900</a> is the beach pick at its price, the <a href="/reviews/minelab-manticore-review/">Manticore</a> adds flagship headroom, and the <a href="/reviews/xp-deus-2-review/">Deus II</a> brings a 20m rating for surf and rock pools.</p>
<h2>Practical beach rules</h2>
<p>Work the tide: falling tide exposes fresh ground, and the low-water scallops where heavy objects settle. Check waterproof ratings honestly — a submersible coil under a rain-resistant control box is not a submersible detector. And know your beach’s rules: some UK foreshores need a permit (most of the Crown Estate foreshore allows detecting; always check locally).</p>
<p>Coming from inland detecting? Read <a href="/guides/multi-frequency-vs-single-frequency/">multi-frequency vs single frequency</a> first — it is the spec that decides beach capability.</p>
""",
  },
  "waterproof-metal-detectors-explained": {
    "title": "What “Waterproof” Actually Means on a Metal Detector",
    "desc": "Waterproof coil, weatherproof box or fully submersible? The three levels of detector waterproofing explained — and the depth ratings that matter.",
    "kicker": "Buying advice",
    "date": "2026-07-31",
    "body": """
<p>“Waterproof” is the most misleading word in the detector industry, and it costs people money every year. There are three distinct levels, and manufacturers are not always careful to distinguish them.</p>
<h2>The three levels</h2>
<p><b>1. Waterproof search coil only.</b> The coil can be submerged; the control box cannot. Fine for wet grass, puddles and shallow wading where the box stays dry. Many entry-level machines are this — and describe themselves simply as “waterproof”.</p>
<p><b>2. Weather-resistant control box.</b> Survives British rain, not submersion. Drop it in a stream and the claim expires with the warranty’s goodwill.</p>
<p><b>3. Fully submersible, with a published depth rating.</b> The whole machine goes underwater to a stated depth. This is the only level that means what buyers assume “waterproof” means.</p>
<h2>The ratings that matter</h2>
<p>Most fully-submersible machines are rated to <b>5 metres</b> — the <a href="/reviews/minelab-manticore-review/">Manticore</a>, <a href="/reviews/minelab-equinox-900-review/">Equinox 900</a>, <a href="/reviews/minelab-x-terra-elite-review/">X-Terra Elite</a> and <a href="/reviews/minelab-x-terra-pro-review/">X-Terra Pro</a> all sit here, as does the IP68-rated <a href="/reviews/nokta-legend-2-review/">Legend 2</a>. The <a href="/reviews/xp-deus-2-review/">XP Deus II</a> stands apart at <b>20 metres</b> — the only mainstream flagship genuinely built for diving.</p>
<p>Match the rating to what you actually do: wading and surf need 5m and honesty about which parts submerge; diving needs the Deus II class. When in doubt, ask us exactly what a rating covers — 01724 845608.</p>
""",
  },
  "gold-detecting-uk": {
    "title": "Gold Prospecting Detectors: Why Gold Needs a Specialist Machine",
    "desc": "Why standard coin and relic detectors walk over gold, and what makes a dedicated gold prospecting machine different — high frequency, pulse induction and beyond.",
    "kicker": "Gold prospecting",
    "date": "2026-07-31",
    "body": """
<p>Gold prospecting demands specialist equipment, and the reason is physics rather than marketing: a capable coin-and-treasure machine can walk straight over nuggets that a dedicated gold detector finds easily.</p>
<h2>Three properties that make gold hard</h2>
<p><b>Gold is low-conductivity</b> — small nuggets respond weakly to the frequencies coin machines use. <b>Gold is usually small</b> — sub-gram pieces are the norm, not the exception. And <b>gold lives in mineralised ground</b> — the ironstone and hot rocks of gold country generate exactly the ground noise that defeats standard VLF detectors.</p>
<h2>What specialist machines do differently</h2>
<p>Dedicated gold detectors take one of two routes: <b>very high frequencies</b>, which trade depth for sensitivity to tiny, low-conductivity targets; or <b>pulse induction</b>, which fires powerful pulses and reads the decay — largely ignoring ground mineralisation, at the cost of discrimination.</p>
<h2>The UK angle</h2>
<p>Natural gold in the UK is real but modest — Scottish and Welsh streams have produced it for centuries. Most UK detectorists encounter gold as jewellery and hammered coinage, which standard multi-frequency machines handle well. Dedicated prospecting machines — Minelab’s GPX and GPZ ranges, stocked by Crawfords as authorised Minelab distributor — earn their keep for serious prospecting, at home or abroad.</p>
<p>Not sure which side of that line you are on? Start with the <a href="/">leaderboard</a> — if “gold” means rings and hammereds, our standard picks already cover you.</p>
""",
  },
  "uk-metal-detecting-permissions": {
    "title": "UK Metal Detecting Permissions: The Rules Before You Dig",
    "desc": "Landowner permission, the Treasure Act 1996, NCMD membership and protected sites — the legal basics every UK detectorist must know before swinging a coil.",
    "kicker": "Law & permissions",
    "date": "2026-07-31",
    "body": """
<p>Metal detecting in the UK is legal, popular and welcoming — provided you follow rules that are genuinely not optional. The essentials:</p>
<h2>Permission is everything</h2>
<p>All land in the UK belongs to someone, and you need the landowner’s permission to detect on it — including beaches, commons and footpaths. A polite knock, an honest explanation and an offer to share finds and fill holes properly is still how most permissions are won. Get agreements in writing for anything you value.</p>
<h2>The Treasure Act 1996</h2>
<p>In England, Wales and Northern Ireland, finds that qualify as treasure — broadly, gold and silver objects over 300 years old, and groups of coins — must be reported to the local coroner within 14 days. Failure to report is a criminal offence. Scotland’s rules are stricter still: virtually all archaeological finds must be reported. Report non-treasure finds voluntarily through the Portable Antiquities Scheme; it protects the hobby’s reputation and the historical record.</p>
<h2>Where you must not detect</h2>
<p>Scheduled Monuments and Sites of Special Scientific Interest are off-limits without specific consent, regardless of landowner permission. Check the National Heritage List before pursuing a promising permission.</p>
<h2>Insurance and clubs</h2>
<p>NCMD membership provides public liability insurance most landowners expect, and club digs are the fastest route to good land and better habits. Detect responsibly: fill your holes, take your rubbish, report your finds — the hobby’s access depends on it.</p>
""",
  },
}

# ── Comparison articles (from CMD blog assets) ───────────────────────
COMPARISONS = {
  "nokta-legend-2-vs-minelab-equinox-900": {
    "title": "Nokta Legend 2 vs Minelab Equinox 900: Which Multi-Frequency Machine Deserves Your Investment?",
    "desc": "Legend 2 vs Equinox 900 compared on UK ground: SMF vs Multi-IQ+, target ID, recovery speed, audio and value — with a clear recommendation for each buyer.",
    "a": "nokta-legend-2", "b": "minelab-equinox-900",
    "date": "2026-07-31",
    "winline": [("Value for money", "Legend 2"), ("Refinement &amp; stability", "Equinox 900"),
                ("Wet-sand performance", "Equinox 900"), ("Feature count per pound", "Legend 2"),
                ("Ease of use", "Equinox 900"), ("Overall", "Equinox 900")],
    "capsule": "Buy the Equinox 900 if you want the more refined, more stable machine with the stronger beach manners — it is the better detector. Buy the Legend 2 if the price difference funds your pinpointer and spade — it is the better deal.",
    "spec_rows": [
      ("Technology", "SMF simultaneous multi-frequency", "Multi-IQ+ simultaneous multi-frequency", "b"),
      ("Waterproofing", "IP68 fully submersible", "Submersible to 5m", ""),
      ("Ease of use", "Deep menus, needs tuning (3.8)", "Logical, learn in an afternoon (4.4)", "b"),
      ("Wet salt sand", "Capable with careful setup", "Class-leading beach modes", "b"),
      ("Value", "4.8 — highest on our board", "4.6", "a"),
      ("Editorial score", "4.2", "4.6", "b"),
    ],
    "body": """
<p>The simultaneous multi-frequency arms race has produced two of the most capable machines ever offered to UK detectorists at sensible money. Nokta’s Legend 2 attacks on price and feature count; Minelab’s Equinox 900 defends with the battle-hardened Multi-IQ+ engine and a decade of platform refinement.</p>
<p>On ordinary pasture the honest finding is that both find the same targets. The differences appear at the margins: on wet salt sand the Equinox 900’s beach modes hold stable where the Legend 2 needs careful setup; in dense iron the 900’s ID stability gives more confident dig-or-walk decisions. The Legend 2 answers with a spec sheet — wireless audio, waterproofing, customisation — at a price Minelab does not match.</p>
<p>Full reviews: <a href="/reviews/nokta-legend-2-review/">Nokta Legend 2</a> · <a href="/reviews/minelab-equinox-900-review/">Minelab Equinox 900</a>.</p>
""",
    "buy_a": ("Buy the Legend 2 if…", "Maximum features per pound is the brief, you enjoy tuning a machine to your ground, and the saving matters. It is the best pure value on our leaderboard."),
    "buy_b": ("Buy the Equinox 900 if…", "You want the machine that is simply better more often — especially on beaches — and will hold its edge as your skills grow. It is our all-terrain benchmark for a reason."),
  },
  "xp-icon-x-vs-minelab-manticore": {
    "title": "XP ICON X vs Minelab Manticore: Budget-Smart Performance or Flagship Power?",
    "desc": "XP ICON X vs Minelab Manticore compared: Multi-IQ+ vs FMF, target information, coils, waterproofing and price — which UK detector deserves your investment?",
    "a": "xp-icon-x", "b": "minelab-manticore",
    "date": "2026-07-31",
    "winline": [("Price &amp; accessibility", "ICON X"), ("Target information", "Manticore"),
                ("Weight &amp; wireless", "ICON X"), ("Difficult ground", "Manticore"),
                ("Proven track record", "Manticore"), ("Overall", "Manticore")],
    "capsule": "The Manticore is the better detector: more target information, stronger performance on difficult ground, and a proven platform. The ICON X is the smarter buy for detectorists who want XP’s wireless, lightweight character without flagship spending — accepting an early-verdict machine.",
    "spec_rows": [
      ("Technology", "FMF fast multi-frequency", "Multi-IQ+ simultaneous multi-frequency", ""),
      ("Target information", "Numeric ID", "2D target trace + numeric ID", "b"),
      ("Platform", "Fully wireless, featherweight", "Wired coil, standard weight", "a"),
      ("Waterproof", "XP platform rating", "Submersible to 5m", ""),
      ("Warranty", "5-year XP manufacturer warranty", "3-year Minelab manufacturer warranty", "a"),
      ("Editorial score", "4.2 (early verdict)", "4.8", "b"),
    ],
    "body": """
<p>An unusual head-to-head: XP’s newest release against the highest score we have ever awarded. It is not a fair fight on performance — the Manticore’s 2D target trace and Multi-IQ+ engine give it more to say about every target, and on mineralised or iron-heavy ground that information wins hunts. It is, however, a very fair fight on money.</p>
<p>The ICON X brings XP’s defining virtues — wireless architecture, featherweight handling, fast recovery — down the price ladder, backed by XP’s 5-year manufacturer warranty. For a large group of buyers the honest question is not “which is better?” but “do I need what the extra spend buys?” If your ground is ordinary and your sessions long, the XP’s weight advantage is worth more than the Minelab’s trace display.</p>
<p>Full reviews: <a href="/reviews/xp-icon-x-review/">XP ICON X (early verdict)</a> · <a href="/reviews/minelab-manticore-review/">Minelab Manticore</a>.</p>
""",
    "buy_a": ("Buy the ICON X if…", "You want XP’s wireless, lightweight character and FMF multi-frequency at a friendlier price, and you are comfortable with a new release whose long-term record is still being written."),
    "buy_b": ("Buy the Manticore if…", "You hunt difficult ground and want the most target information available. It is the best machine we have ever scored, and the premium buys real capability, not a badge."),
  },
}

# ── Gist articles derived from crawfordsmd.com blog posts ────────────
# Each is an original rewrite (not a copy), SEO-optimised, linking back
# to the full post on the main site and across to our own reviews.
GUIDES.update({
  "best-metal-detector-for-gold-prospecting-uk": {
    "title": "Best Metal Detector for Gold Prospecting UK (2026 Guide)",
    "desc": "Which metal detector finds gold in the UK? High-frequency VLF vs pulse induction explained, plus the Minelab GPX and GPZ machines that professionals actually use.",
    "kicker": "Gold prospecting",
    "date": "2026-08-06",
    "body": """
<p>Searching for a <b>gold prospecting metal detector</b> is a different problem from choosing a coin and relic machine. Gold is low-conductivity, usually small, and almost always sits in heavily mineralised ground — the exact combination that defeats a standard VLF detector.</p>
<h2>Why standard detectors miss gold</h2>
<p>A £1,500 coin-and-treasure machine can walk straight over a sub-gram nugget. Three properties explain it: gold responds weakly at the frequencies coin machines favour, most natural gold is tiny, and gold country is full of ironstone and hot rocks that generate constant ground noise.</p>
<h2>High-frequency VLF vs pulse induction</h2>
<p>Dedicated <b>gold detectors</b> take one of two routes. <b>High-frequency VLF</b> machines trade depth for sensitivity to small, low-conductivity targets — ideal for shallow nugget patches. <b>Pulse induction (PI)</b> fires powerful pulses and reads the decay, largely ignoring mineralisation to reach serious depth, at the cost of discrimination. Minelab's GPX and flagship <b>GPZ 8000</b> with GeoZVT sit at the professional end of that spectrum.</p>
<h2>Gold detecting in the UK</h2>
<p>Natural UK gold is real but modest — Scottish and Welsh streams have produced it for centuries. Most British detectorists meet gold as jewellery and hammered coinage, which simultaneous multi-frequency machines handle perfectly well. Before buying a specialist machine, be honest about which you are chasing.</p>
<p>If "gold" means rings and hammereds rather than nuggets, our <a href="/reviews/minelab-manticore-review/">Manticore review</a> and <a href="/reviews/minelab-equinox-900-review/">Equinox 900 review</a> cover the machines that do that job best. For the full prospecting rundown including current GPX and GPZ stock, read the complete guide on the main site.</p>
""",
  },
  "cleaning-metal-detecting-finds": {
    "title": "How to Clean Metal Detecting Finds Without Destroying Them",
    "desc": "Cleaning and preserving metal detecting finds: what to clean, what to leave alone, and how to avoid wiping value off a hammered coin or Roman bronze.",
    "kicker": "Finds care",
    "date": "2026-08-06",
    "body": """
<p>More historical value is destroyed by over-enthusiastic cleaning than by any detector setting. Knowing <b>how to clean metal detecting finds</b> starts with knowing when not to.</p>
<h2>The golden rule: stop before you start</h2>
<p>If a find might be significant — a hammered coin, a Roman bronze, anything gold or silver over 300 years old — clean nothing. Under the Treasure Act 1996 it may need reporting to the coroner within 14 days, and conservators want it untouched. Rinse off loose soil in plain water and stop there.</p>
<h2>Safe cleaning by metal</h2>
<p><b>Gold</b> needs almost nothing — warm water and a soft brush. It does not corrode, so what you dig is what it looked like when lost. <b>Silver</b> is fragile once corroded; avoid abrasives entirely. <b>Copper and bronze</b> develop a protective patina that should be preserved, not scrubbed away — the green surface is the object's skin. <b>Iron</b> is the hardest of all and is best left to a conservator.</p>
<h2>What to avoid</h2>
<p>Never use household metal polish, wire brushes, vinegar baths or electrolysis on anything you care about. They strip patina, leave permanent scratches, and can turn a reportable find into a worthless disc.</p>
<h2>Storage matters as much as cleaning</h2>
<p>Dry finds thoroughly, keep them in acid-free containers away from damp, and label them with findspot details — that context is often worth more than the object. The full guide, including specific conservation products we stock, is on the main site.</p>
""",
  },
  "xp-icon-x-vs-minelab-vanquish-560": {
    "title": "XP ICON X vs Minelab Vanquish 560: Which Should a Beginner Buy?",
    "desc": "XP ICON X vs Minelab Vanquish 560 compared for UK detectorists — FMF vs Multi-IQ, weight, wireless audio and value at the entry-to-mid tier.",
    "kicker": "Head-to-head",
    "date": "2026-08-06",
    "body": """
<p>The <b>XP ICON X vs Minelab Vanquish 560</b> question comes up constantly at the counter, because they sit either side of the same decision: how much machine do you actually need to start finding things?</p>
<h2>The technology gap</h2>
<p>The <b>Vanquish 560</b> runs Minelab's <b>Multi-IQ</b> simultaneous multi-frequency — the same family of technology as machines costing far more, in a package aimed squarely at newcomers. The <b>XP ICON X</b> uses XP's <b>FMF</b> fast multi-frequency in the brand's characteristically light, fully wireless architecture. Both are genuine simultaneous multi-frequency; neither is a switchable single-frequency machine.</p>
<h2>Weight and handling</h2>
<p>XP's defining advantage is weight. If your sessions run long, the ICON X is noticeably kinder on the shoulder, and the wireless design removes the cable that is the most common failure point on any detector. The Vanquish answers with simplicity — fewer settings between you and a signal.</p>
<h2>Which one, honestly</h2>
<p>Choose the <b>Vanquish 560</b> if you want the shortest route from box to first find, with Minelab's dealer network behind it. Choose the <b>ICON X</b> if lightness and the XP ecosystem matter, and you are comfortable with a newer platform — see our <a href="/reviews/xp-icon-x-review/">ICON X early verdict</a> for why we hold that score at 4.2 for now.</p>
<p>Also worth reading: our <a href="/best/">beginners buying guide</a>, which ranks the machines we hand to first-timers in the shop.</p>
""",
  },
  "minelab-gold-monster-1000-vs-2000": {
    "title": "Minelab Gold Monster 1000 vs 2000: What Actually Changed?",
    "desc": "Gold Monster 1000 vs 2000 compared — sensitivity, automatic ground balance, coils and who should upgrade. A UK dealer's take.",
    "kicker": "Head-to-head",
    "date": "2026-08-06",
    "body": """
<p>The <b>Minelab Gold Monster</b> series exists to do one job supremely well: find small gold in mineralised ground without demanding that the operator become a ground-balancing expert.</p>
<h2>The Gold Monster proposition</h2>
<p>Both machines pair a very high operating frequency with fully automatic ground balance and sensitivity — the design decision that made the original <b>Gold Monster 1000</b> such a common first prospecting machine. You switch on and detect; the machine handles the hot rocks.</p>
<h2>1000 vs 2000: who should upgrade</h2>
<p>The step up from <b>1000 to 2000</b> is about refinement rather than reinvention — improved sensitivity to the smallest targets and updated handling. If you already own a 1000 and hunt occasionally, the case for upgrading is modest. If you are buying your first dedicated gold machine, buy the newer platform.</p>
<h2>Where it sits against the GPX and GPZ</h2>
<p>Gold Monster is a high-frequency VLF machine, not pulse induction. That makes it excellent on shallow, small gold and considerably less capable at depth in the most severely mineralised ground, where Minelab's <b>GPX</b> and <b>GPZ</b> series take over. Our <a href="/guides/best-metal-detector-for-gold-prospecting-uk/">gold prospecting guide</a> explains the difference in plain terms.</p>
<p>As an authorised Minelab dealer we stock and support the full prospecting range — full comparison on the main site.</p>
""",
  },
  "minelab-gpz-7000-vs-gpz-8000": {
    "title": "Minelab GPZ 7000 vs GPZ 8000: Is the Flagship Upgrade Worth It?",
    "desc": "GPZ 7000 vs GPZ 8000 compared: GeoZVT technology, weight, ergonomics and depth. Which Minelab gold flagship deserves the investment?",
    "kicker": "Head-to-head",
    "date": "2026-08-06",
    "body": """
<p>At the very top of gold prospecting sits Minelab's <b>GPZ</b> series — machines built for detectorists who measure success in grams recovered rather than hours enjoyed.</p>
<h2>What GeoZVT does</h2>
<p>The GPZ platform uses <b>Zero Voltage Transmission</b> technology, a different transmission approach from conventional pulse induction that delivers exceptional depth on deep gold in severely mineralised ground. It is the reason the <b>GPZ 7000</b> held its position at the top of the market for so long.</p>
<h2>7000 to 8000: the real differences</h2>
<p>The <b>GPZ 8000</b> is the generational successor, and the meaningful improvements are in ergonomics and usability as much as raw performance — significant when the machine in question is one you carry across difficult terrain all day. Weight distribution and handling improvements matter more at this level than a headline depth figure.</p>
<h2>Who this is for</h2>
<p>Be clear-eyed: this is professional prospecting equipment. For UK detectorists chasing hammered coins and jewellery, a <a href="/reviews/minelab-manticore-review/">Manticore</a> or <a href="/reviews/minelab-equinox-900-review/">Equinox 900</a> is the right machine and a fraction of the outlay. The GPZ earns its keep on serious goldfields.</p>
<p>Crawfords is an authorised Minelab dealer with the widest UK prospecting range — current stock and full specifications on the main site.</p>
""",
  },
  "metal-detecting-rally-season-tips": {
    "title": "Metal Detecting Rally Tips: How to Get More From a Dig",
    "desc": "Expert metal detecting rally tips for UK detectorists — machine setup, ground coverage, kit checklist and etiquette that finds more on crowded permissions.",
    "kicker": "Technique",
    "date": "2026-08-06",
    "body": """
<p>A <b>metal detecting rally</b> puts hundreds of coils over the same field in a weekend. The detectorists who go home happy are rarely the ones with the most expensive machine — they are the ones who prepared.</p>
<h2>Set your machine up before you arrive</h2>
<p>Rally fields are noisy in every sense. Ground balance properly on arrival, and resist the urge to run sensitivity at maximum — with dozens of machines nearby, electromagnetic interference will punish you. A stable machine at moderate sensitivity out-finds an unstable one at full tilt every time.</p>
<h2>Cover ground others have written off</h2>
<p>The obvious lines get hammered in the first hour. Field edges, hedgerows, gateways, awkward slopes and the ground under thick stubble stay under-detected all weekend. Slow your swing and overlap properly — most missed finds are missed by speed, not depth.</p>
<h2>Kit checklist</h2>
<p>Spare batteries or a power bank, a proper digging spade, a pinpointer, knee pads, a finds pouch, waterproofs and more water than you think you need. A pinpointer alone will save you an hour of digging across a weekend.</p>
<h2>Etiquette that keeps rallies happening</h2>
<p>Fill every hole, take all rubbish including yours and other people's, record findspots for the Portable Antiquities Scheme, and report anything that may qualify under the Treasure Act 1996. Rallies continue because landowners let them — see our <a href="/guides/uk-metal-detecting-permissions/">UK permissions guide</a> for the full legal picture.</p>
"""
  },
})
