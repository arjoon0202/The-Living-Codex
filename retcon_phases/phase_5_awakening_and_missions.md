# Phase 5: Awakening & Missions

## Scope
Complete rework of Rime and Tidus awakening sections in the Devil Fruit Awakening tab, plus full mission log review for anatomy/species/element references across all 17 missions.

## CRITICAL SAFETY RULES
- **No content deletion** — every mission and awakening section must continue to exist (rewritten, not removed)
- **Read `MERIDIAN_CREW_REFERENCE.md` before touching any character content** — Rime is MALE (he/him), Tidus is MALE (he/him), Claude uses NO gendered pronouns
- **Never edit `dist/hive_codex.html` directly** — edit source files in `src/tabs/` and `src/tabs/panels/`
- **Never read `.b64` image files directly**
- **Run `python build.py` after all changes and verify clean compilation**
- **This is a retcon of love** — awakenings should be the most awe-inspiring descriptions in the Codex

## Pre-Phase Checklist
- [ ] Phases 1-4 completed
- [ ] Read `MERIDIAN_CREW_REFERENCE.md` for pronoun reference
- [ ] Read `CLAUDE.md` for panel file map
- [ ] Understand Rime's new identity: chinchilla + twig kendo sword + acid/dust/Electro vapor (NO cold)
- [ ] Understand Tidus' new identity: polar bear–sea otter hybrid + shell shovel (Zoan Reef-Reef Fruit) + bio-film + snow/ice + Fishman Karate (film-membrane water)

## Key Files to Edit
| Content | File |
|---------|------|
| Devil Fruit Awakening tab | `src/tabs/27-devil-fruit-awakening.html` (check if split into panels) |
| Mission Log — Missions 1-5 | `src/tabs/panels/17-missions-01-05.html` |
| Mission Log — Missions 6-10 | `src/tabs/panels/17-missions-06-10.html` |
| Mission Log — Missions 11-13 | `src/tabs/panels/17-missions-11-13.html` |
| Mission Log — Missions 14-15 | `src/tabs/panels/17-missions-14-15.html` |
| Mission Log — Missions 16-17 | `src/tabs/panels/17-missions-16-17.html` |
| Content Reference | `CODEX_CONTENT_REFERENCE.md` |

---

## Step 1: Rime Awakening — Rework

### File: `src/tabs/27-devil-fruit-awakening.html` (Rime's sub-panel)

### Awakening overview:
Rime's Jōki Jōki no Mi (Vapour Logia) awakening should now reflect his acid/dust/Electro/sword identity. NO cold-mode awakening moves.

### Review existing awakening moves:

**Acid Rain Carnival** — Should be fine (already acid-based). Verify no cold references. Enhance with dust element if appropriate (acid rain carrying mineral grit).

**Plasma Pinball** — Should be fine (heat-based/Electro). Verify no cold references. Could incorporate his Rime Sphere + sword.

**Ionosphere Slam** — Should be fine (Electro-based). Verify no cold references.

**Absolute Zero Pulse** — MUST BE REMOVED AND REPLACED. This is a cold-ultimate.

**Any other cold-specific awakening moves** — Identify and replace.

### New awakening technique to replace Absolute Zero Pulse:
Create a new dust/acid/Electro ultimate awakening move. Suggestions for creative direction:

**The Dust Epoch** (or similar grandiose name):
- Rime's awakened form saturates an entire battlefield with ionized mineral dust suspended in acidic vapor
- Every dust mote is an Electro capacitor. Every breath is corrosive. Every surface is abrasive
- The terrain itself becomes hostile — stone corrodes, metal dissolves, water turns acidic
- At the center, Rime floats in his Logia state: a chinchilla-shaped silhouette of crackling acid-dust-lightning, his twig sword a blade of compressed mineral crystal harder than diamond
- The awakening's true power: the battlefield doesn't just respond to Rime — it IS Rime. The environment becomes an extension of his Logia body. He's everywhere the dust touches

### Create 1-2 additional new awakening moves:
To replace any other cold-specific moves. These should showcase:
- Twig sword at awakened power (the twig transforms — mineral dust crystallizes around it into a real blade, or it becomes a lightning rod for an entire acid storm)
- Dust manipulation at continental scale (awakened Logia = environment-level control)
- Electro-acid synergy at its theoretical peak

### Awakening description rewrite:
The prose describing Rime's awakened state should emphasize:
- His chinchilla form becomes a silhouette of crackling energy
- The twig sword crystallizes with compressed mineral dust
- His dust/acid/Electro field extends to the environment itself
- He's still absolutely unserious about it. Even at peak awakening, he's cackling

---

## Step 2: Tidus Awakening — COMPLETE REWRITE

### File: `src/tabs/27-devil-fruit-awakening.html` (Tidus' sub-panel)

### REMOVE ENTIRELY:
- The Green Blood awakening narrative
- Any references to Green Blood reaching awakened state
- Any references to Paramecia awakening mechanics for Tidus

### NEW AWAKENING CONCEPT:
Tidus' awakening is about the **Zoan shell shovel weapon reaching its awakened state**. Since the weapon ate the Sango Sango no Mi (Reef-Reef Fruit, Zoan), the weapon awakens — not Tidus himself.

**The Awakened Reef:**
When the Sango Sango no Mi reaches its awakened state, the weapon's coral doesn't just grow structures — it becomes a **full living reef ecosystem** that Tidus conducts.

Creative direction for the awakened state:
- The shell shovel plants itself in the ground (or ocean floor, or any surface)
- A complete living coral reef erupts from the weapon and spreads in all directions — not just coral, but an entire oceanic ecosystem: coral formations, sea anemones, kelp forests, bioluminescent organisms, tidal pools
- Tidus stands at the center as the reef's conductor. He doesn't just build shelter — he builds an entire WORLD
- His Fishman heritage means the ocean fills the reef. Water flows through the coral structures from nowhere, creating a fully functional underwater environment ON LAND
- His polar bear ice combines with the living reef — frozen coral formations, ice-crystal anemones, snow falling inside a warm coral cave
- His bio-film coats every surface — the entire reef is protected by his clownfish nature. Everything inside the reef is safe from toxins, acids, temperature extremes. The reef is the ultimate expression of his protective instinct
- Fish-shaped water constructs swim through the air between coral formations, guided by his Fishman Karate

**The philosophy:**
Tidus' awakening is the physical manifestation of who he is: a builder. A protector. Someone who creates worlds where things can live safely. His awakening isn't a weapon — it's a HOME. The most dangerous home in the world, but a home nonetheless.

### New awakened techniques (create 5):
Each should have a Hawaiian/Polynesian name and showcase:
1. A reef-creation technique (the initial deployment — world-building at combat speed)
2. A defensive technique (the reef as absolute shelter — bio-film coated, ice-reinforced, self-repairing coral walls)
3. An offensive technique (the reef as weapon — coral spears, constricting kelp, bioluminescent blinding, tidal wave from nowhere)
4. A support technique (the reef as healing environment — clean water, medicinal coral, temperature regulation for allies)
5. An ultimate technique (the reef reaches its final form — a complete frozen reef temple, Tidus at its heart, conducting an ecosystem of beauty and devastation)

---

## Step 3: Mission Log — Full Review

### Process:
Read ALL mission log panel files. For each mission, identify and update:
- Any references to Rime as "hamster" → "chinchilla" (should be done in Phase 1, VERIFY)
- Any references to Tidus/Tethys with crab anatomy → polar bear-otter (REWRITE)
- Any references to Rime's cold abilities → acid/dust/Electro (REWRITE)
- Any references to Tidus' claws/carapace/shell → paws/fur/bio-film (REWRITE)
- Any references to Green Blood → REMOVE
- Combat descriptions featuring either character → REFLAVOUR for new identities

### Mission-by-mission guide:

**Missions 1-5** (`17-missions-01-05.html`):
- Early missions. Likely have foundational descriptions of Rime and Tidus in combat
- Check for species references, anatomy descriptions, early ability demonstrations
- These set the tone — they should read as if chinchilla + polar bear-otter was ALWAYS the case

**Missions 6-10** (`17-missions-06-10.html`):
- Mid-arc missions. Combat descriptions become more detailed
- Check for specific technique callouts that reference cold or crab abilities
- Tidus' engineering/building scenes — rewrite for paw-based building, coral from weapon

**Missions 11-13** (`17-missions-11-13.html`):
- Major battles. Likely have detailed combat descriptions
- Carefully review any Rime/Tidus combat sequences
- Check for combo attack references (should match Phase 4 rewrites)

**Missions 14-15** (`17-missions-14-15.html`):
- God's Knights battle and other major encounters
- Check for Transcendence descriptions — Rime's transcendence should reflect acid/dust/Electro, Tidus' should reflect polar bear-otter + coral + ice
- Check for Queen's Wrath Protocol references

**Missions 16-17** (`17-missions-16-17.html`):
- Revolutionary Army battle + Red Hair Pirates battle
- **Mission 16** — Rime vs Sabo: Rewrite combat description. Rime's acid/dust/Electro vs Sabo's fire. No cold. Chinchilla with twig sword against the Revolutionary Army's #2. The visual comedy of a small fluffy swordsman vs Sabo should enhance, not diminish, the drama.
- **Mission 16** — Tidus vs Lindbergh + Morley: Rewrite for polar bear-otter. Tidus' engineering genius vs Lindbergh's tech + Morley's earth manipulation. Bio-film water defense, coral from weapon, ice constructs.
- **Mission 17** — Rime vs Beckman: Rewrite. Chinchilla swordsman vs the smartest man in the East Blue's crew. Acid vapor + Electro + dust vs Beckman's tactical genius.
- **Mission 17** — Tidus vs Yasopp: Rewrite. Polar bear-otter with shell shovel vs the world's greatest sharpshooter. Bio-film barriers to catch bullets, coral walls for cover, ice structures to redirect sightlines.
- **Mission 17** — The Hive Connection: Verify all anatomy references for both characters
- **Mission 17** — Guanyin deployment: Should match Phase 4's reimagined version

---

## Step 4: Build & Verify

1. Run `python build.py`
2. Verify clean compilation
3. Search for orphaned references:
   - `grep -i "Absolute Zero" dist/hive_codex.html` — should be ZERO
   - `grep -i "Green Blood" dist/hive_codex.html` — should be ZERO (verify Phase 3 caught all)
   - `grep -i "hamster" dist/hive_codex.html` — should be ZERO in Rime context
   - `grep -i "crab\|crustacean\|carapace" dist/hive_codex.html` — should be ZERO in Tidus context
4. Verify div balance
5. Update CODEX_CONTENT_REFERENCE.md

---

## Phase 5 Completion Checklist
- [ ] Rime awakening: Absolute Zero Pulse removed and replaced with acid/dust/Electro ultimate
- [ ] Rime awakening: All cold references removed, sword + dust identity integrated
- [ ] Rime awakening: 1-2 new techniques created
- [ ] Tidus awakening: COMPLETELY REWRITTEN — Green Blood gone, Zoan weapon awakening instead
- [ ] Tidus awakening: 5 new Hawaiian/Polynesian-named techniques created
- [ ] Tidus awakening: The Awakened Reef concept fully realized
- [ ] Mission 1-5 reviewed and updated for both characters
- [ ] Mission 6-10 reviewed and updated
- [ ] Mission 11-13 reviewed and updated
- [ ] Mission 14-15 reviewed and updated
- [ ] Mission 16 combat descriptions rewritten (Rime vs Sabo, Tidus vs Lindbergh+Morley)
- [ ] Mission 17 combat descriptions rewritten (Rime vs Beckman, Tidus vs Yasopp)
- [ ] Hive Connection references updated
- [ ] Guanyin deployment in Mission 17 matches Phase 4 rewrite
- [ ] CODEX_CONTENT_REFERENCE.md mirrored
- [ ] `python build.py` runs clean
- [ ] Div balance verified
- [ ] Awakening descriptions are the most awe-inspiring content in the Codex
