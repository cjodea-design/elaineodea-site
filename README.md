# elaineodea.com

Elaine O'Dea's portfolio site. Built with [Astro](https://astro.build) from
plain content files, edited through [Pages CMS](https://pagescms.org), and
served by Cloudflare straight from this repository.

## Editing the site (no code needed)

Go to **https://app.pagescms.org**, sign in with GitHub, and open this
repository. You'll see:

- **Exhibitions** — one entry per show. Add a new one, fill in the title,
  year, venue, pick a layout, add each work with its photos, Save.
- **Bio** — the biography text and the Education / Awards / Press /
  Group Exhibitions lists.
- **Home page** — the photo on the front page.
- **Site settings** — the name in the sidebar, footer text, Instagram link.

Saving writes a commit to this repository; Cloudflare rebuilds the site and
the change is live within a minute or two. Every save is a commit, so any
change can be undone from the repository's history.

### Layouts

| Layout | What it does |
|---|---|
| Stacked | Caption above each work's photos (most pages) |
| Stacked, captions below | Photos first, caption beneath (Ambit 2025) |
| Grid | Works with several photos become a thumbnail grid |
| Feature | First work large with its caption alongside, a series as a grid, the rest in two columns (Thresholds 2025) |

### Photos

Upload photos straight from the camera; the build makes web-sized versions
automatically. A first work entry with photos but no title displays as an
installation view.

## Working locally

```
npm install      # once
npm run dev      # http://localhost:4321, live-reloads as you edit
npm run build    # writes the finished site to dist/
```

Content lives in `src/content/exhibitions/*.md`, `src/content/pages/*.md`
and `src/data/site.json`; photos in `src/images/<folder>/`. Those files are
exactly what the CMS edits, so they can equally be changed by hand.

## How it's put together

```
src/content.config.ts      the shape of an exhibition / the bio page
src/content/               the content itself (one file per page)
src/images/                photos, organised by exhibition
src/layouts/Base.astro     sidebar, navigation, footer, fonts
src/components/Works.astro the four layout presets
src/components/Photo.astro responsive, optimised images + lightbox link
src/styles/global.css      all styling
.pages.yml                 the CMS form definitions
```

## Deploying

Cloudflare Workers builds the site from the `master` branch on every push.
In the dashboard the build command is `npm run build` and the deploy command
is `npx wrangler deploy`; the output folder (`dist/`) is declared in
`wrangler.jsonc`, not in the dashboard. Old `*.html` URLs from the first
version of the site are redirected in `public/_redirects`.
