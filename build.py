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
<div class="layout">
  <aside class="sidebar">
    <a class="site-name" href="index.html">Elaine<br>O'Dea</a>
    <nav class="site-nav">
      {nav_html(active)}
    </nav>
  </aside>
  <main>
{body}
  </main>
</div>
<footer class="site-footer">
  <div class="site-footer-inner">
    <span>&copy; 2020 by Elaine O'Dea.</span>
    <a href="https://instagram.com/elaineodeaart/" target="_blank" rel="noopener">Instagram</a>
  </div>
</footer>
<script>
document.querySelectorAll('.slider-wrap').forEach(function(w){{
  var s=w.querySelector('.slider');
  w.querySelector('.prev').onclick=function(){{s.scrollBy({{left:-s.clientWidth*0.8,behavior:'smooth'}});}};
  w.querySelector('.next').onclick=function(){{s.scrollBy({{left:s.clientWidth*0.8,behavior:'smooth'}});}};
}});
</script>
</body>
</html>
"""

def img(slug, i, alt):
    return f'<img src="images/{slug}/{i:02d}.jpg" alt="{alt}" loading="lazy">'

def slider_html(slug, indices, alt):
    if not indices:
        return ""
    imgs = "\n        ".join(img(slug, i, alt) for i in indices)
    return f"""    <div class="slider-wrap">
      <button class="slider-btn prev" aria-label="Previous">&lsaquo;</button>
      <div class="slider">
        {imgs}
      </div>
      <button class="slider-btn next" aria-label="Next">&rsaquo;</button>
    </div>"""

def work_sections_html(slug, sections):
    out = []
    for title, materials, indices in sections:
        head = f"<h2>{title}</h2>" if title else ""
        mats = "".join(f"<p>{m}</p>" for m in materials)
        imgs = "\n      ".join(img(slug, i, title or slug) for i in indices)
        out.append(f"""    <section class="work">
      {head}{mats}
      {imgs}
    </section>""")
    return "\n".join(out)

def page_head(heading, sub=()):
    subs = "".join(f'<p class="venue">{s}</p>' for s in sub)
    return f"""    <div class="page-head">
      <h1>{heading}</h1>
      {subs}
    </div>"""

# ---------- HOME ----------
home_body = """    <div class="hero">
      <figure>
        <img src="images/home/01.jpg" alt="Elaine O'Dea, sculpture work" loading="eager">
      </figure>
    </div>"""
open(os.path.join(ROOT, "index.html"), "w").write(
    page_shell("index", "Home", SITE_DESC, home_body)
)

# ---------- BIO ----------
bio_body = """    <div class="page-head">
      <h1>Bio</h1>
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
        <li class="edu">Master of Fine Arts<br>National College of Art and Design, Dublin<br>2021 &ndash; 2023</li>
        <li class="edu">Bachelor of Fine Arts with Critical Cultures<br>Sculpture and Expanded Practice &mdash; First Class Honours<br>National College of Art and Design, Dublin<br>2016 &ndash; 2019</li>
        <li class="edu">Diploma (RHODEC) Interior Design<br>Portobello Institute, Dublin<br>1999 &ndash; 2000</li>
        <li class="edu">Higher Diploma in Education<br>University College Dublin<br>1993 &ndash; 1994</li>
        <li class="edu">Bachelor of Arts &mdash; Economics and Geography<br>University College Dublin<br>1988 &ndash; 1991</li>
      </ul>

      <h2>Awards</h2>
      <ul>
        <li>Fire Station Artist&rsquo;s Studio Sculpture Bursary Award, 2020</li>
      </ul>

      <h2>Group Exhibitions</h2>
      <ul>
        <li class="edu"><span class="ex-year">2025</span>AMBIT<br>Signal Arts Centre, Bray, Co. Wicklow<br><br>Thresholds<br>Seamus Ennis Arts Centre, Naul, Co. Dublin</li>
        <li class="edu"><span class="ex-year">2023</span>NCAD Works, Graduate Exhibition<br>NCAD Annex, Dublin 8</li>
        <li class="edu"><span class="ex-year">2022</span>Continuum<br>Irish Georgian Society, Dublin 2<br><br>Subjective Objects<br>BKB Visual Art Studios, Dublin 9</li>
        <li class="edu"><span class="ex-year">2021</span>AFFECT<br>BKB Visual Art Studios, Dublin 9</li>
        <li class="edu"><span class="ex-year">2020</span>Fragility &mdash; Delicate Aspect and Precarious Presentation<br>BKB Visual Art Studios, Dublin 9</li>
        <li class="edu"><span class="ex-year">2019</span>Sculpture in Context<br>National Botanic Gardens, Dublin 9<br><br>NCAD Works, Graduate Exhibition<br>NCAD, Dublin 8</li>
        <li class="edu"><span class="ex-year">2018</span>Sculpture in Context<br>National Botanic Gardens, Dublin 9<br><br>Disjunction<br>Eblana House, Dublin 8</li>
      </ul>
    </div>"""
open(os.path.join(ROOT, "bio.html"), "w").write(
    page_shell("bio", "Bio", "Biography, education and exhibition history for artist Elaine O'Dea.", bio_body)
)

# ---------- GALLERY PAGES ----------
galleries = {
    "thresholds-2025": dict(
        heading="Thresholds 2025", sub=["The Seamus Ennis Arts Centre"], slider=[1, 2, 3, 10, 11],
        sections=[
            ("Castings", ["Jesmonite, Iron filings, Wire Mesh, Copper"], [4]),
            ("Cast #1&ndash;#7", ["Jesmonite, Iron filings, Wire Mesh, Copper"], [5, 6]),
            ("Cast Form #1", ["Jesmonite"], [7]),
            ("EndoCast", ["Jesmonite"], [8]),
            ("Cast Form #2", ["Jesmonite"], [9]),
        ],
    ),
    "ncad-works-2023": dict(
        heading="NCAD Works 2023", sub=["National College of Art and Design, Dublin 8"],
        sections=[
            ("Run &amp; Fell", ["Fabric, steel, copper, wood, plasterboard, wallpaper, clay, jesmonite"], [1, 2, 3]),
        ],
    ),
    "continuum-2022": dict(
        heading="Continuum 2022", sub=["Irish Georgian Society, Dublin 2"],
        sections=[
            ("", [], [1]),
            ("Inside/Out", ["Steel, latex, jesmonite"], [2]),
            ("Inside/Out", ["Steel, latex, jesmonite"], [3]),
        ],
    ),
    "subjective-objects-2022": dict(
        heading="Subjective Objects", sub=["2022"],
        sections=[("Nexus I &amp; II", ["Copper, aluminium", "40 x 40 x 40cm"], [1, 2])],
    ),
    "if-walls-could-talk-2021": dict(
        heading="If Walls Could Talk 2021",
        sections=[("If Walls Could Talk", ["Copper, aluminium, perspex", "200 x 220 x 300cm"], [1, 2, 3])],
    ),
    "fragility-2020": dict(
        heading="Fragility:<br>Delicate Aspect and Precarious Presentation", sub=["2020", "BKB Visual Art studios"],
        sections=[
            ("", [], [1]),
            ("The Bough", ["Steel, plaster, resin, iron filings", "150 x 40 x 30cm"], [2]),
            ("Sticks and Stones", ["Copper pipe, plaster, rubber"], [3]),
        ],
    ),
    "ncad-works-2019": dict(
        heading="NCAD Grad Show 2019",
        sections=[
            ("Upstand/Overcome/Underpin", ["Mild steel, plaster"], [1]),
            ("Overcome", ["Mild steel, plaster", "200 x 90 x 20cm"], [2]),
            ("Upstand", ["Mild steel, plaster", "165 x 50 x 50cm"], [3]),
        ],
    ),
    "sculpture-in-context-2019": dict(
        heading="Sculpture in Context", sub=["2019", "National Botanic Gardens, Dublin"],
        sections=[("Overcome II", ["Steel, chrome, plaster, resin, chain", "90 x 60 x 30cm"], [1])],
    ),
    "colour-is-dangerous-2018": dict(
        heading="NCAD 2018",
        sections=[("Colour is Dangerous", ["Resin, aluminium cages (30 x 30cm), spotlights, chain"], [1, 2])],
    ),
    "gentle-persuasion-2018": dict(
        heading="Disjunction", sub=["Eblana House, Dublin 8"],
        sections=[("Gentle Persuasion", ["Plaster board, wooden frame, ratchet strap, paint"], [1, 2])],
    ),
}

for slug, nav_label in PAGES:
    if slug not in galleries:
        continue
    g = galleries[slug]
    body = "\n".join(p for p in [
        page_head(g["heading"], g.get("sub", ())),
        slider_html(slug, g.get("slider"), g["heading"]),
        work_sections_html(slug, g["sections"]),
    ] if p)
    desc = f"{nav_label} &mdash; sculpture by Elaine O'Dea."
    open(os.path.join(ROOT, f"{slug}.html"), "w").write(
        page_shell(slug, nav_label, desc, body)
    )

print("Built", len(PAGES), "pages")
