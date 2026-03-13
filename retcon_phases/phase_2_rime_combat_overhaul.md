# Phase 2: Rime Combat Overhaul

## Scope
Complete reflavouring of Rime's combat identity: remove cold-mode vapor, add twig kendo sword, add dust element, replace seed projectiles with grain/cereal projectiles, rewrite Rime Sphere, update Rokushiki, update Electro synergy. This is creative reflavouring from the ground up — not find-and-replace.

## CRITICAL SAFETY RULES
- **No content deletion** — every technique section must continue to exist (rewritten or replaced, not removed)
- **Read `MERIDIAN_CREW_REFERENCE.md` before touching any character content** — Rime is MALE (he/him)
- **Never edit `dist/hive_codex.html` directly** — edit source files in `src/tabs/` and `src/tabs/panels/`
- **Never read `.b64` image files directly**
- **Run `python build.py` after all changes and verify clean compilation**
- **This is a retcon of love** — every rewritten passage should feel like it was always the real version

## Pre-Phase Checklist
- [ ] Phase 1 completed (Rime is already "chinchilla" everywhere)
- [ ] Read `MERIDIAN_CREW_REFERENCE.md` for pronoun reference (Rime = he/him)
- [ ] Read `CLAUDE.md` for panel file map

## Key Files to Edit
| Content | File |
|---------|------|
| Rime's companion profile (abilities, combat doctrine) | `src/tabs/panels/06-companions-rime.html` |
| Fighting Styles — Rime panel | `src/tabs/panels/07-fighting-ajay-rime.html` |
| Arsenal — Signature Moves | `src/tabs/panels/04-arsenal-moves.html` |
| Arsenal — Swarm Classes (for move tags) | `src/tabs/panels/04-arsenal-swarm.html` |
| Haki Transcendence — Rime | `src/tabs/11-haki-transcendence.html` (check if split) |
| Auxiliary Protocols — Rime | `src/tabs/09-auxiliary-protocols.html` |
| CSS | `src/head/styles.css` |
| Content Reference | `CODEX_CONTENT_REFERENCE.md` |

---

## Step 1: Remove Cold-Mode Vapor

### Core principle:
Rime's Jōki Jōki no Mi (Vapour Logia) CANNOT produce cold/freezing vapor anymore. His vapor is hot, acidic, and alkaline ONLY.

### Techniques to REMOVE (replace with new techniques):
- **Permafrost Palm** — cold Ryou palm strike → REPLACE with a new acid/dust technique
- **Hoarfrost Veil** — cold defensive technique → REPLACE with a dust-based defensive technique
- **Absolute Zero Pulse** — ultimate cold technique → REPLACE with a new acid/dust/Electro ultimate
- Any other cold-specific techniques found when reading the files

### Techniques to REWORK (remove cold references):
- Any technique that referenced "cold-mode switching" → now references hot/acidic/alkaline modulation only
- "Cryo-electric" synergy → "Acid-electric" synergy
- "Sub-zero vapour" / "freezing" / "frost" in technique descriptions → replace with "superheated acidic vapor" / "corrosive" / "caustic"
- The Rime Sphere's **Hamster Suplex** (now Chinchilla Suplex): replace "sub-zero vapour" with "superheated acidic vapor"

### What survives:
- Hot vapor ✓
- Acidic vapor ✓
- Alkaline vapor ✓
- Electro ✓
- Steam/mist for concealment ✓
- Vapor compression/expansion ✓
- Logia intangibility ✓

---

## Step 2: Add Twig Kendo Sword

### Concept:
Rime carries a twig — literally a small stick he found somewhere — that he wields like a kendo sword. This makes him the crew's swordsman. The twig is comically small but channeled with his Ryou, Electro, and acidic vapor, it becomes devastating.

### CRITICAL — The sword is ADDITIVE, not a replacement:
- He STILL scratches, bites, belly-flops, rolls, and fights dirty
- He STILL uses his vapor Logia powers
- He STILL has his Rime Sphere mech
- He STILL has absurdly grandiose technique names
- The sword is ONE MORE tool in his chaotic arsenal

### Where to add the sword:
1. **Companion profile** (`06-companions-rime.html`): Add to equipment/weapons section. Describe the twig — where he found it, why he chose it, how he treats it (with the same absurd reverence as everything else). The comedy: it's a literal twig, and he treats it like a legendary blade.

2. **Fighting Style** (`07-fighting-ajay-rime.html`): Add a sword combat section. His kendo style should be technically brilliant but visually absurd — a chinchilla performing kendō forms with a twig. The gap between the grandiose technique names and the visual of a tiny fluffy creature with a stick is peak Rime comedy.

3. **Reflavour some existing techniques** to incorporate the sword:
   - His **Shigan** (Finger Pistol) → could become a sword thrust variant (Shigan: Twig Pierce or similar)
   - His **Ryou palm strikes** → add sword variants where he channels Ryou through the twig
   - His area-denial moves → some can incorporate sword slashes that release arcs of acidic vapor

### New sword-specific techniques (create with absurdly grandiose Japanese names):
Create 4-6 new sword techniques. Suggestions for the naming convention:
- Use dramatic Japanese martial arts naming (Rime's existing style)
- The technique names should sound like they belong to a legendary swordsman
- The reality should be a small chinchilla swinging a twig really fast
- Include kanji + romanization for each

Example patterns (Claude should create better ones):
- **[Something] no Tachi** (太刀) — great sword techniques (for a twig)
- **[Something] Issen** (一閃) — single flash / one slash
- **Tsumuji** (旋風) — whirlwind style
- Each technique should combine the sword with Rime's other elements (Electro, acid vapor, dust)

---

## Step 3: Add Dust Element

### Core concept:
Chinchillas take volcanic mineral dust baths — this is now part of Rime's combat identity. His vapor carries suspended mineral dust: fine abrasive particulates that get into armor joints, eyes, and mechanisms.

### Combat applications:
1. **Acid + Dust combo**: Acidic vapor carries mineral dust. The combination is devastating — acid corrodes while dust abrades. Gets into everything.

2. **Electrified dust storms**: Static-charged abrasive particles arcing lightning between dust motes. Area denial that replaces cold-mode.

3. **Dust hardening**: Ryou channeled through dust-laden vapor compresses into a rock-hard shell. His **Tekkai** equivalent becomes compressed mineral dust + Ryou armor. When Rime activates this, his fluffy chinchilla fur suddenly looks like stone.

4. **Dust clouds**: Replace cold-mode area denial. Obscuring clouds of fine mineral dust that also carry acid and static charge. Enemies caught in a Rime dust storm can't see, can't breathe, are getting acid-burned and electrocuted, and their equipment is being sandblasted.

5. **Dust bath as meditation/recovery**: Rime's dust bath is genuinely therapeutic — mineral dust absorbs excess oils and rebalances his fur/skin. In combat, a brief dust bath can reset his Logia composition.

### Lifestyle detail:
Rime's personal quarters aboard the Meridian (Rime's Crucible) should include the most luxurious dust bath setup in the New World — imported volcanic mineral dust, carefully curated varieties, temperature-controlled environment. He is EXTREMELY particular about his dust quality. Different missions require different dust compositions. He has Gauge (his Coppling attendant) maintain the dust bath system.

Add this detail to:
- Companion profile (`06-companions-rime.html`) — personality/lifestyle section
- Vessel tab if Rime's Crucible is described (`src/tabs/panels/13-vessel-layout.html` or equivalent)
- Fighting Style panel — explain how dust bath practice translates to combat mastery

---

## Step 4: Replace Seeds with Grain/Cereal Projectiles

### Core concept:
Rime hoards oats, barley, millet, and other grains with obsessive chinchilla dedication. These replace sunflower seeds as his projectile ammunition.

### Replacements:
- "sunflower seeds" → "oat kernels" / "grain rounds" / "cereal projectiles"
- "seed-spitting" → "grain shots" (vapor-compressed cereal projectiles)
- "cheek pouches" → REMOVE ENTIRELY (chinchillas don't have prominent cheek pouches like hamsters)
- "Pouch Salvo" → **"Grain Battery"** (Dial-port rapid-fire system loaded with amplified cereal rounds)

### Delivery mechanisms (new):
- **Vapor compression**: Grains compressed in superheated acid vapor and launched at high velocity
- **Sword launch**: Rime flicks grains off the flat of his twig sword, each one Ryou-hardened
- **Paw flick**: Quick shots launched from his paw with Electro charge
- **Grain mines**: Scattered across the battlefield, each grain infused with Electro, creating a minefield of tiny explosions

### Comedy value:
The grandiose technique names + the projectiles being literally breakfast cereal = peak Rime. He takes his grain selection as seriously as a sommelier takes wine.

### Files to search:
Search all files for "sunflower," "seed-spit," "cheek pouch," "Pouch Salvo" and replace. Key files:
- `06-companions-rime.html`
- `07-fighting-ajay-rime.html`
- `04-arsenal-moves.html` (signature moves that reference seeds)
- Any mission log files that describe Rime's combat

---

## Step 5: Rewrite Rime Sphere Mech

### Files: `06-companions-rime.html`, `07-fighting-ajay-rime.html`

### Changes:
- Shape: Still exists, reshaped for a chinchilla body. Chinchillas ARE round enough for Sphere Mode to work. The rolling still works.
- All "hamster-shaped" → "chinchilla-shaped" (should be done in Phase 1, verify)
- **Chinchilla Suplex**: The move's cold reference removed. New description: Rime's Sphere rolls over the target at terminal velocity while emitting superheated acidic vapor — the victim is simultaneously crushed, steam-burned, and acid-etched.
- **Pouch Salvo → Grain Battery**: Dial-port rapid-fire system, but instead of cheek-pouch launched seeds, it's a magazine-fed system of Ryou-compressed grain rounds. Think minigun but the bullets are oats.
- Walker Mode: Silhouette adjusted — chinchilla proportions (rounder, bigger ears, longer tail mechanism). The mech's tail serves as a balance counterweight and can crack like a whip.

---

## Step 6: Rewrite Rokushiki Adaptation

### File: `07-fighting-ajay-rime.html` (or companion profile)

The current Rokushiki is written for hamster anatomy. Rewrite for chinchilla:

- **Soru**: Chinchillas are incredibly fast and agile — they can jump 6 feet vertically. Rime's Soru involves explosive vertical and lateral leaps. His Soru leaves a puff of mineral dust in his wake.
- **Geppo**: Chinchillas are natural leapers. Rime's Geppo is a series of rapid-fire jumps, each kick-off trailing acidic dust clouds.
- **Tekkai**: Compressed mineral dust + Ryou armor. His soft chinchilla fur suddenly looks and feels like stone. The contrast is terrifying.
- **Shigan**: Twig thrust variants. Also, chinchilla teeth are incredibly hard — a bite-based Shigan is canon.
- **Rankyaku**: Twig slashes that launch acidic vapor arcs. Also, tail-whip Rankyaku from the chinchilla's long, powerful tail.
- **Kami-e**: Chinchilla agility is absurd — they can slip through impossibly small gaps. Rime's Kami-e leverages his soft, compressible body + Logia vapor to become nearly impossible to hit.

---

## Step 7: Rewrite Electro-Vapour Synergy

### File: `06-companions-rime.html` and/or `07-fighting-ajay-rime.html`

The current synergy section describes cryo-electric effects. Complete rewrite:

**New synergy: Acid-Electric-Dust**
- **Electrified Acid Vapor**: Rime's signature combat state. Acidic vapor saturated with Electro creates an ionized corrosive field. Metal armor corrodes twice as fast. Nervous systems are overloaded by the combination of chemical and electrical attack.
- **Dust Storm Lightning**: Mineral dust particles become charged in the Electro field. Each dust mote arcs micro-lightning to its neighbors, creating a visible web of crackling energy inside the dust cloud. Beautiful and horrifying.
- **Conductive Acid Film**: When acidic vapor condenses on surfaces, it creates a thin conductive film. Rime's Electro then travels along these surfaces, electrocuting anything touching the acid-coated ground/walls/equipment.
- **The Gremlin Field**: Rime's ultimate area-denial state — a sphere of mineral dust suspended in acidic vapor, all of it crackling with Electro. Inside the Gremlin Field, visibility is zero, every breath is acid, every surface is sandpaper, and lightning strikes from every direction. Rime sits in the center, perfectly comfortable (Logia immunity + dust bath), cackling.

---

## Step 8: Update Haki Transcendence — Rime

### File: Rime's Haki Transcendence sub-panel (check `src/tabs/11-haki-transcendence.html` or its sub-panels)

Review for any cold-specific references in Rime's transcendence description. His transcendence should now emphasize:
- Ryou channeled through the twig sword
- Electro amplification beyond normal Mink limits
- Acid vapor achieving molecular-level control
- Dust manipulation at particle level
- The combination of all four elements in transcended state

---

## Step 9: Update Auxiliary Protocols — Rime

### File: `src/tabs/09-auxiliary-protocols.html`

Rime's "Awesome Hero's Tactics" humanitarian techniques. Review for any cold references. His emergency/humanitarian techniques should use:
- Hot vapor for sterilization, warming
- Dust for abrasive cleaning, filtration
- Electro for power generation, defibrillation
- Sword for precision cutting in rescue operations

---

## Step 10: Build & Verify

1. Run `python build.py`
2. Verify clean compilation (no errors)
3. Search the built output for orphaned references:
   - `grep -i "cold.mode\|cold vapour\|freezing vapour\|sub-zero\|cryo-electric" dist/hive_codex.html` — should be ZERO in Rime context
   - `grep -i "hoarfrost\|permafrost\|absolute zero" dist/hive_codex.html` — should be ZERO
   - `grep -i "cheek pouch\|seed.spit\|sunflower" dist/hive_codex.html` — should be ZERO
   - `grep -i "Pouch Salvo" dist/hive_codex.html` — should be ZERO (now Grain Battery)
4. Verify div balance

---

## Phase 2 Completion Checklist
- [ ] All cold-mode vapor techniques removed or replaced
- [ ] No references to Permafrost Palm, Hoarfrost Veil, or Absolute Zero Pulse
- [ ] Twig kendo sword added to Rime's equipment and combat style
- [ ] 4-6 new sword-specific techniques created with absurdly grandiose Japanese names
- [ ] Existing techniques reflavoured to incorporate sword where appropriate
- [ ] Dust element fully integrated into combat doctrine
- [ ] Dust bath lifestyle details added to companion profile and Crucible description
- [ ] All seed/cheek-pouch references replaced with grain/cereal equivalents
- [ ] Pouch Salvo → Grain Battery
- [ ] Rime Sphere rewritten for chinchilla body
- [ ] Rokushiki adaptation rewritten for chinchilla anatomy
- [ ] Electro-Vapour synergy rewritten (acid-electric-dust, no cryo)
- [ ] Haki Transcendence updated
- [ ] Auxiliary Protocols updated
- [ ] CODEX_CONTENT_REFERENCE.md mirrored
- [ ] `python build.py` runs clean
- [ ] Div balance verified
- [ ] The voice is right — Rime sounds like Rime (chaotic, grandiose, gleefully destructive)
