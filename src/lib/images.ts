import type { ImageMetadata } from 'astro';

// Every image under src/images is made available to Astro's image pipeline
// here. Content files refer to images by path ("/src/images/<folder>/<file>")
// — the form the CMS writes — and this turns that path into an optimised asset.
const modules = import.meta.glob<{ default: ImageMetadata }>(
  '/src/images/**/*.{jpg,jpeg,png,webp,avif,JPG,JPEG,PNG}'
);

export async function resolveImage(path: string): Promise<ImageMetadata> {
  const load = modules[path];
  if (!load) {
    const known = Object.keys(modules).slice(0, 5).join(', ');
    throw new Error(
      `Image not found: "${path}". Check the path in the content file — it should look like /src/images/<folder>/<file>.jpg (e.g. ${known}).`
    );
  }
  return (await load()).default;
}
