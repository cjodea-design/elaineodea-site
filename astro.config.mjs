// @ts-check
import { defineConfig } from 'astro/config';

// Old flat-file URLs from the first static build, kept working so nothing
// that was bookmarked or indexed breaks after the move to Astro.
const legacySlugs = [
  'ambit-2025', 'thresholds-2025', 'ncad-works-2023', 'continuum-2022',
  'subjective-objects-2022', 'if-walls-could-talk-2021', 'fragility-2020',
  'ncad-works-2019', 'sculpture-in-context-2019', 'colour-is-dangerous-2018',
  'gentle-persuasion-2018',
];
const redirects = Object.fromEntries([
  ['/index.html', '/'],
  ['/bio.html', '/bio/'],
  ...legacySlugs.map((s) => [`/${s}.html`, `/${s}/`]),
]);

export default defineConfig({
  site: 'https://elaineodea.com',
  output: 'static',
  trailingSlash: 'ignore',
  redirects,
});
