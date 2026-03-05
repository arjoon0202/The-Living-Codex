import { defineCollection, z } from 'astro:content';

const loreCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    volume: z.number(),
    section: z.string().optional(),
    order: z.number().optional(),
    character: z.string().optional(),
    subtitle: z.string().optional(),
    color: z.string().optional(),
    ambientColor: z.string().optional(),
  }),
});

export const collections = {
  'volume-1': loreCollection,
  'volume-2': loreCollection,
  'volume-3': loreCollection,
  'volume-4': loreCollection,
  'volume-5': loreCollection,
};
