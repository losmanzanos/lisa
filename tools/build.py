#!/usr/bin/env python3
"""Builds the static pages for brilliantlysane. Run from the repo root:
       python3 tools/build.py
   Emits folder/index.html everywhere so URLs stay clean. Links are written
   relative, so the same build works at a domain root and at a project
   subpath like losmanzanos.github.io/lisa.
"""
import os, re, html, json, datetime

SITE = "https://losmanzanos.github.io/lisa"   # swap to https://www.brilliantlysane.org at launch
NAME = "Brilliantly Sane"
WHO  = "Lisa Wallace, LPC"
TEL  = "970-368-9185"
MAIL = "lisa@brilliantlysane.org"
TODAY = datetime.date.today().isoformat()

NAV = [("about/", "About"), ("approach/", "Approach"), ("work-with/", "Work With"),
       ("rates/", "Rates"), ("faq/", "FAQ"), ("journal/", "Journal")]

FOOT_LINKS = [("about/", "About Lisa"), ("approach/", "Therapeutic approach"),
              ("work-with/", "Who I work with"), ("young-adult-therapy/", "Young adults"),
              ("lgbtqia-therapy/", "Queer and gender affirming"),
              ("religious-trauma-therapy/", "Religious trauma"),
              ("rates/", "Rates and payment"), ("faq/", "Questions"),
              ("journal/", "Journal"), ("contact/", "Reach out")]


def rel(depth, target):
    """Relative href from a page at `depth` folders deep to a root-relative target."""
    up = "../" * depth
    if target in ("", "/"):
        return up if up else "./"
    return up + target.lstrip("/")


def head(p):
    d, slug = p["depth"], p["slug"]
    url = SITE + "/" + (slug + "/" if slug else "")
    img = SITE + "/assets/img/og-brilliantly-sane.jpg"
    a = rel(d, "assets/")
    schema = [{
        "@context": "https://schema.org", "@type": "LocalBusiness",
        "@id": SITE + "/#practice", "name": NAME,
        "alternateName": "Brilliantly Sane Counseling",
        "description": "Contemplative psychotherapy with Lisa Wallace, LPC. Telehealth across Colorado, based in Boulder.",
        "url": SITE + "/", "telephone": TEL, "email": MAIL, "image": img,
        "priceRange": "$175",
        "address": {"@type": "PostalAddress", "addressLocality": "Boulder",
                    "addressRegion": "CO", "addressCountry": "US"},
        "areaServed": {"@type": "State", "name": "Colorado"},
        "founder": {"@type": "Person", "name": "Lisa Wallace",
                    "honorificSuffix": "LPC", "jobTitle": "Licensed Professional Counselor",
                    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Naropa University"}},
    }]
    schema += p.get("schema", [])
    crumbs = p.get("crumbs")
    if crumbs:
        schema.append({"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n,
                                 "item": SITE + "/" + (s + "/" if s else "")}
                                for i, (s, n) in enumerate(crumbs)]})
    tags = "\n".join('<script type="application/ld+json">%s</script>'
                     % json.dumps(x, separators=(",", ":")) for x in schema)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(p['title'])}</title>
<meta name="description" content="{html.escape(p['desc'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{p.get('ogtype','website')}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{html.escape(p['title'])}">
<meta property="og:description" content="{html.escape(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta property="og:image:alt" content="The Brilliantly Sane monogram, a copper ring enclosing the letters B and S.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(p['title'])}">
<meta name="twitter:description" content="{html.escape(p['desc'])}">
<meta name="twitter:image" content="{img}">
<meta name="theme-color" content="#F8F4F1">
<link rel="icon" href="{a}img/favicon.png" sizes="64x64">
<link rel="icon" href="{a}img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="{a}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Karla:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{a}site.css">{p.get('extracss','')}
{tags}
</head>"""


def header(p):
    d, slug = p["depth"], p["slug"]
    a = rel(d, "assets/")
    links = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if slug == href.strip("/") or slug.startswith(href.strip("/") + "/") else ""
        links += f'      <a href="{rel(d, href)}"{cur}>{label}</a>\n'
    brandhref = rel(d, "")
    bid = ' id="brand"' if slug == "" else ""
    return f"""<body class="{p.get('bodyclass','interior')}">
<a class="skip" href="#main">Skip to content</a>
<div class="aura"></div>
<div class="grain"></div>

<header class="site-head">
  <a class="brand"{bid} href="{brandhref}" aria-label="{NAME}, home">
    <picture>
      <source srcset="{a}img/logo.webp" type="image/webp">
      <img class="mark" src="{a}img/logo.png" width="46" height="46" alt="The Brilliantly Sane monogram, a copper ring enclosing the letters B and S.">
    </picture>
    <span><span class="brand-name">{NAME}</span><span class="brand-sub">Contemplative Psychotherapy</span></span>
  </a>
  <button class="menu-btn" aria-expanded="false" aria-controls="sitenav">Menu</button>
  <nav class="site-nav" id="sitenav" aria-label="Main">
{links}      <a class="cta" href="{rel(d, 'contact/')}">Reach out</a>
  </nav>
</header>
"""


def footer(p):
    d = p["depth"]
    items = "".join(f'<li><a href="{rel(d, h)}">{l}</a></li>' for h, l in FOOT_LINKS)
    return f"""
<footer class="site-foot">
  <div class="inner">
    <div>
      <h4>Brilliantly Sane</h4>
      <p>Contemplative psychotherapy with {WHO}. Telehealth across Colorado, based in Boulder.</p>
      <p><a href="{rel(d, 'contact/')}">Book a free twenty minute consult</a></p>
    </div>
    <div>
      <h4>Pages</h4>
      <ul class="foot-links">{items}</ul>
    </div>
    <div>
      <h4>Get in touch</h4>
      <p><a href="tel:+19703689185">{TEL}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p>
      <p class="crisis">If you are in crisis, call or text 988 for the Suicide and Crisis Lifeline, or call 911. Email is not monitored for emergencies.</p>
    </div>
  </div>
  <div class="legal">
    <span>&copy; {datetime.date.today().year} Brilliantly Sane. {WHO}, Colorado.</span>
    <span>Site by Chad Moravec</span>
  </div>
</footer>
<script src="{rel(d, 'assets/site.js')}" defer></script>{p.get('extrajs','')}
</body>
</html>
"""


def page_head_block(p):
    motif = MOTIF % rel(p["depth"], "assets/")
    sf = f'<p class="standfirst">{p["standfirst"]}</p>' if p.get("standfirst") else ""
    return f"""<main id="main">
<div class="page-head">
  <div class="motif-layer">{motif}</div>
  <div>
    <p class="eyebrow">{p['eyebrow']}</p>
    <h1>{p['h1']}</h1>
  </div>
  {sf}
</div>
<div class="rule-full"><span></span></div>
"""


def sheets(p):
    out = ""
    for s in p.get("sheets", []):
        note = f'<p>{s["note"]}</p>' if s.get("note") else ""
        h2 = f'<h2>{s["h2"]}</h2>' if s.get("h2") else ""
        out += f"""<section class="sheet {s.get('cls','')}">
  <div class="aside">{h2}{note}</div>
  <div class="prose">{s['body']}</div>
</section>
"""
    return out


MOTIF = '<img class="motif" src="%simg/rings-motif.svg" alt="" aria-hidden="true" width="400" height="400">'


def shot(d, alt):
    """Responsive photographic layer for a band."""
    a = rel(d, "assets/")
    return (f'<picture>'
            f'<source type="image/webp" srcset="{a}img/lake-1000.webp 1000w, {a}img/lake-1600.webp 1600w, {a}img/lake-2400.webp 2400w" sizes="100vw">'
            f'<img class="shot" src="{a}img/lake-1600.jpg" '
            f'srcset="{a}img/lake-1000.jpg 1000w, {a}img/lake-1600.jpg 1600w, {a}img/lake-2400.jpg 2400w" sizes="100vw" '
            f'width="2400" height="1279" loading="lazy" decoding="async" alt="{alt}">'
            f'</picture>')


def band(p):
    b = p.get("band")
    if not b:
        return ""
    d = p["depth"]
    img = shot(d, b["img"]) if b.get("img") else ""
    cls = "band has-img" if b.get("img") else "band"
    return f"""<section class="{cls}">
  {img}
  <div class="motif-layer">{MOTIF % rel(d, 'assets/')}</div>
  <div class="inner">
    <div><blockquote>{b['quote']}</blockquote><p class="by">{b.get('by','Brilliantly Sane')}</p></div>
    <div class="side">{b['side']}</div>
  </div>
</section>
"""


# ---------------------------------------------------------------- ring wayfinder
import math

RING_OUTER = [("contact/", "Sessions", "#63554D"), ("rates/", "Rates", "#5A4C44"),
              ("approach/", "Approach", "#51443C"), ("faq/", "Questions", "#483C35")]
RING_MID = [("young-adult-therapy/", "Young adults", "#CFCDE9"), ("work-with/", "Introspective", "#C6C4E4"),
            ("lgbtqia-therapy/", "LGBTQIA+", "#BDBBDD"), ("religious-trauma-therapy/", "Religious trauma", "#B4B2D6")]
RING_CORE = ("about/", "Lisa", "#CABFB6")
_CX = _CY = 200


def _pol(r, deg):
    a = math.radians(deg)
    return _CX + r * math.cos(a), _CY + r * math.sin(a)


def _annulus(a0, a1, ri, ro):
    la = 1 if (a1 - a0) > 180 else 0
    x1, y1 = _pol(ro, a0); x2, y2 = _pol(ro, a1)
    x3, y3 = _pol(ri, a1); x4, y4 = _pol(ri, a0)
    return (f"M{x1:.2f} {y1:.2f}A{ro} {ro} 0 {la} 1 {x2:.2f} {y2:.2f}"
            f"L{x3:.2f} {y3:.2f}A{ri} {ri} 0 {la} 0 {x4:.2f} {y4:.2f}Z")


def ringnav(p):
    """The mandala repeated as wayfinding, with the segment you arrived through lit.
       Rendered server side as linked SVG so it works with JavaScript off."""
    if p.get("noring"):
        return ""
    d = p["depth"]
    active = p.get("ring")
    a = rel(d, "assets/")
    seg_html, items = [], []

    def band_of(defs, rIn, rOut, gap, cls):
        n = len(defs)
        step = 360 / n
        for i, (href, label, fill) in enumerate(defs):
            key = href.strip("/")
            a0 = -90 + i * step + gap
            a1 = -90 + (i + 1) * step - gap
            on = (key == active)
            mid = (a0 + a1) / 2
            dx, dy = _pol((rIn + rOut) / 2, mid)
            dot = f'<circle class="pip" cx="{dx:.1f}" cy="{dy:.1f}" r="3.4"/>' if on else ""
            seg_html.append(
                f'<a href="{rel(d, href)}" class="nseg {cls}{" on" if on else ""}" data-k="{key}" '
                f'aria-label="{label}"><title>{label}</title>'
                f'<path d="{_annulus(a0, a1, rIn, rOut)}" fill="{fill}"/>{dot}</a>')
            items.append((cls, key, href, label, on))

    band_of(RING_OUTER, 132, 192, 2.2, "o")
    band_of(RING_MID, 82, 126, 2.6, "m")

    chref, clabel, _ = RING_CORE
    con = (chref.strip("/") == active)
    core = (f'<a href="{rel(d, chref)}" class="nseg c{" on" if con else ""}" data-k="about" '
            f'aria-label="{clabel}"><title>{clabel}</title>'
            f'<circle cx="200" cy="200" r="74" fill="#EDE7E1"/>'
            f'<image href="{a}img/lisa.jpg" x="126" y="126" width="148" height="148" '
            f'clip-path="circle(74px at 74px 74px)" preserveAspectRatio="xMidYMid slice"/>'
            f'<circle cx="200" cy="200" r="74" fill="none" stroke="rgba(65,30,6,.18)"/></a>')
    items.append(("c", "about", chref, clabel, con))

    def group(cls, title):
        rows = "".join(
            f'<li><a href="{rel(d, h)}" data-k="{k}"{" aria-current=\"page\"" if on else ""}>{lb}</a></li>'
            for c, k, h, lb, on in items if c == cls)
        return f'<div class="wgroup"><h3>{title}</h3><ul>{rows}</ul></div>'

    return f"""<section class="wayfind" aria-labelledby="wayfind-h">
  <div class="wrap">
    <h2 id="wayfind-h">Where this sits</h2>
    <div class="wayfind-in">
      <svg class="ringnav" viewBox="0 0 400 400" role="group" aria-label="Site map as concentric rings">
        {''.join(seg_html)}
        {core}
      </svg>
      <div class="wlist">
        {group('o', 'Ring 01 &middot; The Practical')}
        {group('m', 'Ring 02 &middot; Who This Is For')}
        {group('c', 'The Center')}
      </div>
    </div>
  </div>
</section>
"""


def facts(rows):
    """Compact at a glance strip. Replaces the repeated prose block on specialty pages."""
    cells = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows)
    return f'<section class="facts"><div class="wrap"><dl>{cells}</dl></div></section>\n'


def build(p):
    p.setdefault("depth", len([x for x in p["slug"].split("/") if x]))
    if p.get("layout") == "post":
        body = (page_head_block(p) + '<div class="post-wrap"><p class="byline">'
                + p.get("byline", "Lisa Wallace, LPC") + '</p><div class="prose">'
                + p["post"] + '</div></div>' + band(p) + ringnav(p) + "</main>")
        doc = head(p) + header(p) + body + footer(p)
        path = os.path.join(p["slug"], "index.html")
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        open(path, "w").write(doc)
        return path
    body = p.get("custom") or (page_head_block(p) + sheets(p)
                               + (facts(p["facts"]) if p.get("facts") else "")
                               + band(p) + ringnav(p) + "</main>")
    doc = head(p) + header(p) + body + footer(p)
    path = os.path.join(p["slug"], "index.html") if p["slug"] else (p.get("file") or "index.html")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w").write(doc)
    return path
