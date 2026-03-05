import sharp from 'sharp';
import { mkdir } from 'fs/promises';
import path from 'path';

const RAW = 'public/raw-assets';
const BG_OUT = 'public/backgrounds';
const LOGO_OUT = 'public/logo';

await mkdir(BG_OUT, { recursive: true });
await mkdir(LOGO_OUT, { recursive: true });

// Background conversions: resize to 1920px wide, WebP at 70% quality
const backgrounds = [
  ['golden dusk.png', 'sovereign-golden-dusk.webp'],
  ['rime.png', 'rime-volcanic-steam.webp'],
  ['petal.png', 'petal-ancient-forest.webp'],
  ['kame.png', 'kame-ocean-depths.webp'],
  ['family.png', 'family-warm-hearth.webp'],
  ['meridian sky.png', 'meridian-sky-sailing.webp'],
  ['spirit star.png', 'spirit-starfield.webp'],
  ['black crown.png', 'black-crown-storm.webp'],
  ['nebula.png', 'transcendent-nebula.webp'],
];

for (const [src, dest] of backgrounds) {
  const input = path.join(RAW, src);
  const output = path.join(BG_OUT, dest);
  const info = await sharp(input)
    .resize({ width: 1920, withoutEnlargement: true })
    .webp({ quality: 70 })
    .toFile(output);
  console.log(`\u2713 ${dest} \u2014 ${(info.size / 1024).toFixed(0)}KB`);
}

// Logo conversions
const logoSrc = path.join(RAW, 'logo.png');

// 512x512 WebP
let info = await sharp(logoSrc)
  .resize(512, 512, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
  .webp({ quality: 85 })
  .toFile(path.join(LOGO_OUT, 'emblem-512.webp'));
console.log(`\u2713 emblem-512.webp \u2014 ${(info.size / 1024).toFixed(0)}KB`);

// 40x40 WebP
info = await sharp(logoSrc)
  .resize(40, 40, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
  .webp({ quality: 85 })
  .toFile(path.join(LOGO_OUT, 'emblem-40.webp'));
console.log(`\u2713 emblem-40.webp \u2014 ${(info.size / 1024).toFixed(0)}KB`);

// 32x32 favicon PNG
info = await sharp(logoSrc)
  .resize(32, 32, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
  .png()
  .toFile(path.join(LOGO_OUT, 'favicon.png'));
console.log(`\u2713 favicon.png \u2014 ${(info.size / 1024).toFixed(0)}KB`);

// 1200x630 OG image (logo centered on black background)
const logoResized = await sharp(logoSrc)
  .resize(400, 400, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
  .toBuffer();

info = await sharp({
  create: {
    width: 1200,
    height: 630,
    channels: 4,
    background: { r: 8, g: 8, b: 12, alpha: 255 }
  }
})
  .composite([{ input: logoResized, gravity: 'centre' }])
  .webp({ quality: 80 })
  .toFile(path.join(LOGO_OUT, 'og-image.webp'));
console.log(`\u2713 og-image.webp \u2014 ${(info.size / 1024).toFixed(0)}KB`);

console.log('\n\u2705 All assets converted.');
