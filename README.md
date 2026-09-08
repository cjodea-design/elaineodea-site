# elaineodea.com

A plain static rebuild of Elaine O'Dea's portfolio site (bio + one page per
exhibition), replacing the Wix version. No build tools or frameworks required
to run it — it's just HTML, CSS and images.

## Structure

```
index.html                  Home
bio.html                    Bio, education, awards, exhibitions
thresholds-2025.html        One HTML file per exhibition page
...
css/style.css                Shared stylesheet
images/<page-slug>/NN.jpg    Web-sized photos for each page (~1800px, optimized)
originals/                   Full-resolution camera originals (gitignored — kept
                              locally only, not needed to serve the site)
build.py                     Optional generator script — see "Editing content" below
robots.txt
```

## Previewing locally

Since every link is a relative path, you can just open `index.html` directly
in a browser (double-click it, or `open index.html` on macOS) — no server
needed. If you'd rather run one:

```
python3 -m http.server 8000
```

then visit http://localhost:8000

## Editing content

Two ways to make changes, pick whichever's easier:

1. **Hand-edit the HTML.** Every page is a normal, readable HTML file — open
   e.g. `thresholds-2025.html` and edit the text or `<img>` tags directly.
2. **Edit `build.py` and regenerate.** All page text/captions live in one
   Python dict near the bottom of `build.py`. Change it, then run
   `python3 build.py` to regenerate every `.html` file from scratch. Handy if
   you're adding a whole new exhibition page, since it keeps the header/nav/
   footer consistent across all pages automatically.

### Adding a new exhibition page

1. Drop the photos in `images/<new-slug>/01.jpg`, `02.jpg`, etc. (resize/
   compress first — see below).
2. Add an entry to `PAGES` and `galleries` in `build.py` following the
   existing examples.
3. Run `python3 build.py`.

### Resizing/compressing new photos

Camera originals are typically several MB each — too large for a fast site.
Before adding a new photo to `images/`, shrink it, e.g. with ImageMagick:

```
convert original.jpg -auto-orient -resize '1800x1800>' -strip -quality 82 images/my-page/01.jpg
```

## Deploying

This repo is git-ready but not yet pushed anywhere. Pick one:

### Option A — GitHub Pages (simplest, everything on GitHub)

1. Create a new empty repo on github.com (don't initialize it with a README).
2. From this folder:
   ```
   git remote add origin <your-repo-url>
   git branch -M main
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Source → Deploy from a branch → `main` / `/ (root)`**.
4. GitHub gives you a `https://<you>.github.io/<repo>` URL. To use
   elaineodea.com instead, add a `CNAME` file to the repo containing just
   `elaineodea.com`, and point the domain's DNS at GitHub Pages (an `A`
   record to GitHub's IPs, or a `CNAME` record if using a `www` subdomain —
   GitHub's custom domain docs list the current values).

### Option B — Cloudflare Pages (free, and pairs with an at-cost domain if you
move the domain there too — see the earlier hosting comparison)

1. Push this repo to GitHub as in steps 1–2 above.
2. In the Cloudflare dashboard: **Workers & Pages → Create → Pages → Connect
   to Git**, pick this repo.
3. Build settings: no build command, output directory `/` (it's already
   plain HTML — nothing to build).
4. Once deployed, add elaineodea.com as a custom domain for the Pages project
   (Cloudflare handles the DNS automatically if the domain is also on
   Cloudflare; otherwise it'll give you records to add wherever the domain
   is managed).

Either way: keep the current Wix site live until the new one is confirmed
working end-to-end at elaineodea.com, then cancel/let the Wix plan lapse.
