import { defineConfig } from 'astro/config';
import rehypeGlassCards from './src/plugins/rehype-glass-cards.mjs';

export default defineConfig({
  site: 'https://arjoon0202.github.io',
  base: '/The-Living-Codex',
  prefetch: true,
  markdown: {
    rehypePlugins: [rehypeGlassCards],
  },
});
