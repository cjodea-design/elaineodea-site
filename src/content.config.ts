import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders';

// Image paths in content are stored as "/src/images/<folder>/<file>.jpg" —
// that is what the CMS writes, and what src/lib/images.ts resolves to an
// optimised asset at build time.
const imagePath = z.string().regex(/^\/src\/images\/.+\.(jpe?g|png|webp|avif)$/i, {
  message: 'Image paths must look like /src/images/<folder>/<file>.jpg',
});

const work = z.object({
  title: z.string().optional(),
  materials: z.string().optional(),
  dimensions: z.string().optional(),
  images: z.array(imagePath).default([]),
});

const exhibitions = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/exhibitions' }),
  schema: z.object({
    title: z.string(),
    year: z.number().int(),
    date: z.coerce.date(),
    heading: z.string().optional(),
    subtitle: z.string().optional(),
    venue: z.string().optional(),
    layout: z.enum(['stacked', 'captions-below', 'grid', 'feature']).default('stacked'),
    works: z.array(work).default([]),
  }),
});

const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pages' }),
  schema: z.object({
    title: z.string(),
    heroImage: imagePath.optional(),
    heroAlt: z.string().optional(),
    education: z
      .array(z.object({ qualification: z.string(), institution: z.string(), years: z.string(), note: z.string().optional() }))
      .optional(),
    awards: z.array(z.object({ title: z.string(), year: z.string() })).optional(),
    press: z.array(z.object({ title: z.string(), year: z.string() })).optional(),
    exhibitions: z.array(z.object({ year: z.string(), title: z.string(), venue: z.string() })).optional(),
  }),
});

export const collections = { exhibitions, pages };
