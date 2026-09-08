import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    ("index", "Home"),
    ("bio", "Bio"),
    ("thresholds-2025", "Thresholds 2025"),
    ("ncad-works-2023", "NCAD Works 2023"),
    ("continuum-2022", "Continuum 2022"),
    ("subjective-objects-2022", "Subjective Objects 2022"),
    ("if-walls-could-talk-2021", "If Walls Could Talk 2021"),
    ("fragility-2020", "Fragility 2020"),
    ("ncad-works-2019", "NCAD Works 2019"),
    ("sculpture-in-context-2019", "Sculpture In Context 2019"),
    ("colour-is-dangerous-2018", "Colour Is Dangerous 2018"),
    ("gentle-persuasion-2018", "Gentle Persuasion 2018"),
]

SITE_TITLE = "Elaine O'Dea"
SITE_DESC = "Sculpture and visual art by Elaine O'Dea, Dublin, Ireland."

def nav_html(active):
    links = []
    for slug, label in PAGES:
        href = "index.html" if slug == "index" else f"{slug}.html"
        cls = ' class="active"' if slug == active else ""
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n      ".join(links)

def page_shell(active, title, description, body):
    page_title = SITE_TITLE if active == "index" else f"{title} — {SITE_TITLE}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<header class="site-header">
  <div class="site-header-inner">
    <a class="wordmark" href="index.html">Elaine O'Dea</a>
    <input type="checkbox" id="nav-toggle" class="nav-toggle">
    <label for="nav-toggle" class="nav-toggle-label">Menu</label>
    <nav class="site-nav">
      {nav_html(active)}
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="site-footer-inner">
    <span>&copy; 2026 Elaine O'Dea</span>
    <a href="https://instagram.com/elaineodeaart/" target="_blank" rel="noopener">Instagram</a>
  </div>
</footer>
</body>
</html>
"""

def gallery_captioned(slug, count, captions):
    figs = []
    for i in range(1, count + 1):
        cap = captions[i - 1] if i - 1 < len(captions) else ""
        figs.append(f"""      <figure>
        <img src="images/{slug}/{i:02d}.jpg" alt="{cap}" loading="lazy">
        <figcaption>{cap}</figcaption>
      </figure>""")
    return '    <div class="gallery">\n' + "\n".join(figs) + "\n    </div>"

def gallery_grouped(slug, count):
    figs = []
    for i in range(1, count + 1):
        figs.append(f"""      <figure>
        <img src="images/{slug}/{i:02d}.jpg" alt="{slug} artwork {i}" loading="lazy">
      </figure>""")
    return '    <div class="gallery">\n' + "\n".join(figs) + "\n    </div>"

def works_list(items):
    lis = "\n".join(f'      <li><span class="work-title">{t}</span> — {m}</li>' for t, m in items)
    return f"""    <div class="works">
      <h2>Works shown</h2>
      <ul>
{lis}
      </ul>
    </div>"""

def page_head(eyebrow, heading, venue):
    venue_html = f'<p class="venue">{venue}</p>' if venue else ""
    return f"""    <div class="page-head">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{heading}</h1>
      {venue_html}
    </div>"""

# ---------- HOME ----------
home_body = f"""{page_head("Sculpture & material", "Elaine O'Dea", "Dublin, Ireland")}
    <div class="hero">
      <figure>
        <img src="images/home/01.jpg" alt="Elaine O'Dea, sculpture work" loading="eager">
      </figure>
      <p class="hero-caption">Elaine O'Dea explores the boundaries between body and surroundings through cast and constructed sculpture.</p>
    </div>"""
open(os.path.join(ROOT, "index.html"), "w").write(
    page_shell("index", "Home", SITE_DESC, home_body)
)

# ---------- BIO ----------
bio_body = """    <div class="page-head">
      <p class="eyebrow">Bio</p>
      <h1>Elaine O'Dea</h1>
    </div>
    <div class="bio">
      <p>Elaine O'Dea is a visual artist living and working in Dublin, Ireland.</p>
      <p>Boundaries create limits, interiors and exteriors, insides and outsides. Boundaries have borders, edges, thresholds — liminal spaces.</p>
      <p>O'Dea explores the relationship of the body and its surroundings, interrogating boundaries and spaces of conflict with a subtle gesture towards societal structures and the ways in which we move against and within those frameworks.</p>
      <p>O'Dea aims to highlight the influence of power dynamics and structures within patriarchal society from a female perspective.</p>
      <p>Her work challenges both the tangible and the intangible, the physical and the cognitive barriers that confine us and the divisions that are created and continuously perpetuated between one and other, subject and object, human and non human, leading to the fragmented nature of our world experience.</p>
      <p>Drawn to the construction and materiality of the world around her, O'Dea's believes materials have associations&hellip; with emotions, histories and memories.</p>
      <p>Her sculptural practice involves the manipulation of natural and man-made materials used in the building of homes and their interiors such as plaster, wood, steel, aluminium, copper, concrete, plastic and fabric.</p>
      <p>Andr&eacute; Breton said &lsquo;Nothing that surrounds us is object, all is subject&rsquo; and through mould making, casting, sculpting and material manipulation, O'Dea produces and reproduces her subjects &mdash; soft and hard, dark and light, inside and outside, human and non human.</p>

      <h2>Education</h2>
      <ul>
        <li><span class="cv-year">2021&ndash;2023</span> &mdash; Master of Fine Arts, National College of Art and Design, Dublin</li>
        <li><span class="cv-year">2016&ndash;2019</span> &mdash; Bachelor of Fine Arts with Critical Cultures, National College of Art and Design, Dublin. Sculpture and Expanded Practice &mdash; First Class Honours</li>
        <li><span class="cv-year">1999&ndash;2000</span> &mdash; Diploma (RHODEC) Interior Design, Portobello Institute, Dublin</li>
        <li><span class="cv-year">1993&ndash;1994</span> &mdash; Higher Diploma in Education, University College Dublin</li>
        <li><span class="cv-year">1988&ndash;1991</span> &mdash; Bachelor of Arts &mdash; Economics and Geography, University College Dublin</li>
      </ul>

      <h2>Awards</h2>
      <ul>
        <li><span class="cv-year">2020</span> &mdash; Fire Station Artist's Studio Sculpture Bursary Award</li>
      </ul>

      <h2>Group Exhibitions</h2>
      <ul>
        <li><span class="cv-year">2025</span> &mdash; AMBIT, Signal Arts Centre, Bray, Co. Wicklow</li>
        <li><span class="cv-year">2025</span> &mdash; Thresholds, Seamus Ennis Arts Centre, Naul, Co. Dublin</li>
        <li><span class="cv-year">2023</span> &mdash; NCAD Works, Graduate Exhibition, NCAD Annex, Dublin 8</li>
        <li><span class="cv-year">2022</span> &mdash; Continuum, Irish Georgian Society, Dublin 2</li>
        <li><span class="cv-year">2022</span> &mdash; Subjective Objects, BKB Visual Art Studios, Dublin 9</li>
        <li><span class="cv-year">2021</span> &mdash; AFFECT, BKB Visual Art Studios, Dublin 9</li>
        <li><span class="cv-year">2020</span> &mdash; Fragility &mdash; Delicate Aspect and Precarious Presentation, BKB Visual Art Studios, Dublin 9</li>
        <li><span class="cv-year">2019</span> &mdash; Sculpture in Context, National Botanic Gardens, Dublin 9</li>
        <li><span class="cv-year">2019</span> &mdash; NCAD Works, Graduate Exhibition, NCAD, Dublin 8</li>
        <li><span class="cv-year">2018</span> &mdash; Sculpture in Context, National Botanic Gardens, Dublin 9</li>
        <li><span class="cv-year">2018</span> &mdash; Disjunction, Eblana House, Dublin 8</li>
      </ul>
    </div>"""
open(os.path.join(ROOT, "bio.html"), "w").write(
    page_shell("bio", "Bio", "Biography, education and exhibition history for artist Elaine O'Dea.", bio_body)
)

# ---------- GALLERY PAGES ----------
galleries = {
    "thresholds-2025": dict(
        eyebrow="2025", heading="Thresholds", venue="The Seamus Ennis Art Centre",
        mode="grouped", count=11,
        works=[
            ("Castings", "Jesmonite, iron filings, wire mesh, copper"),
            ("Cast #1&ndash;#7", "Jesmonite, iron filings, wire mesh, copper"),
            ("Cast Form #1", "Jesmonite"),
            ("EndoCast", "Jesmonite"),
            ("Cast Form #2", "Jesmonite"),
        ],
    ),
    "ncad-works-2023": dict(
        eyebrow="2023", heading="NCAD Works", venue="National College of Art and Design, Dublin 8",
        mode="captioned", count=3,
        captions=[
            "Run &amp; Fell &mdash; fabric, steel, copper, wood, plasterboard, wallpaper, clay, jesmonite (installation view)",
            "Run &amp; Fell (detail) &mdash; fabric, steel, copper",
            "Run &amp; Fell &mdash; fabric, steel, concrete, copper, clay, jesmonite",
        ],
    ),
    "continuum-2022": dict(
        eyebrow="2022", heading="Continuum", venue="Irish Georgian Society, Dublin 2",
        mode="captioned", count=3,
        captions=["Inside/Out &mdash; steel, latex, jesmonite"] * 3,
    ),
    "subjective-objects-2022": dict(
        eyebrow="2022", heading="Subjective Objects", venue="BKB Visual Art Studios",
        mode="captioned", count=2,
        captions=["Nexus I &amp; II &mdash; copper, aluminium, 40 &times; 40 &times; 40cm"] * 2,
    ),
    "if-walls-could-talk-2021": dict(
        eyebrow="2021", heading="If Walls Could Talk", venue="National College of Art and Design, Dublin 8",
        mode="captioned", count=3,
        captions=["If Walls Could Talk &mdash; copper, aluminium, perspex, 200 &times; 220 &times; 300cm (audio work)"] * 3,
    ),
    "fragility-2020": dict(
        eyebrow="2020", heading="Fragility: Delicate Aspect and Precarious Presentation", venue="BKB Visual Art Studios",
        mode="grouped", count=3,
        works=[
            ("The Bough", "Steel, plaster, resin, iron filings, 150 &times; 40 &times; 30cm"),
            ("Sticks and Stones", "Copper pipe, plaster, rubber"),
        ],
    ),
    "ncad-works-2019": dict(
        eyebrow="2019", heading="NCAD Grad Show", venue="National College of Art and Design, Dublin 8",
        mode="captioned", count=3,
        captions=[
            "Upstand / Overcome / Underpin &mdash; mild steel, plaster (installation view)",
            "Overcome &mdash; mild steel, plaster, 200 &times; 90 &times; 20cm",
            "Upstand &mdash; mild steel, plaster, 165 &times; 50 &times; 50cm",
        ],
    ),
    "sculpture-in-context-2019": dict(
        eyebrow="2019", heading="Sculpture in Context", venue="National Botanic Gardens, Dublin",
        mode="captioned", count=1,
        captions=["Overcome II &mdash; steel, chrome, plaster, resin, chain, 90 &times; 60 &times; 30cm"],
    ),
    "colour-is-dangerous-2018": dict(
        eyebrow="2018", heading="Colour is Dangerous", venue="National College of Art and Design, Dublin 8",
        mode="captioned", count=2,
        captions=["Colour is Dangerous &mdash; resin, aluminium cages (30 &times; 30cm), spotlights, chain"] * 2,
    ),
    "gentle-persuasion-2018": dict(
        eyebrow="2018", heading="Disjunction", venue="Eblana House, Dublin 8",
        mode="captioned", count=2,
        captions=["Gentle Persuasion &mdash; plaster board, wooden frame, ratchet strap, paint"] * 2,
    ),
}

for slug, nav_label in PAGES:
    if slug not in galleries:
        continue
    g = galleries[slug]
    body_parts = [page_head(g["eyebrow"], g["heading"], g["venue"])]
    if g["mode"] == "captioned":
        body_parts.append(gallery_captioned(slug, g["count"], g["captions"]))
    else:
        body_parts.append(gallery_grouped(slug, g["count"]))
        body_parts.append(works_list(g["works"]))
    body = "\n".join(body_parts)
    desc = f"{g['heading']}, {g['venue']} &mdash; sculpture by Elaine O'Dea."
    open(os.path.join(ROOT, f"{slug}.html"), "w").write(
        page_shell(slug, nav_label, desc, body)
    )

print("Built", len(PAGES), "pages")
