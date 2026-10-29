// @ts-check
import { defineConfig } from 'astro/config';

// Redirects for the old *.html URLs live in public/_redirects (served by
// Cloudflare as proper 301s) — not here: Astro's static `redirects` option
// writes each one as a folder, which collides with the real index.html.
export default defineConfig({
  site: 'https://elaineodea.com',
  output: 'static',
  trailingSlash: 'ignore',
});
