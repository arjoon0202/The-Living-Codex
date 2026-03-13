# Phase 1: Global Rename & Species

## Scope
Global text replacements across all source files + species description rewrites for both Rime and Tidus. This is the foundation phase — get the names, species, and basic references right before diving into combat mechanics.

## CRITICAL SAFETY RULES
- **No content deletion** — every section that exists must continue to exist (rewritten, not removed)
- **Read `MERIDIAN_CREW_REFERENCE.md` before touching any character content** (pronoun accuracy is critical — Claude uses no gendered pronouns)
- **Never edit `dist/hive_codex.html` directly** — edit source files in `src/tabs/` and `src/tabs/panels/`
- **Never read `.b64` image files directly** — they will overflow context
- **Run `python build.py` after all changes and verify clean compilation**
- **Preserve div balance** — the built HTML must maintain perfect opening/closing `<div>` balance

## Pre-Phase Checklist
- [ ] Read `MERIDIAN_CREW_REFERENCE.md` for pronoun reference
- [ ] Read `CLAUDE.md` for build system and panel file map
- [ ] Note: Rime is MALE (he/him), Tidus is MALE (he/him), Claude uses NO gendered pronouns

---

## Step 1: Global "Tethys" → "Tidus" Rename

This is the safest global replacement — "Tethys" is unique to this character and appears nowhere else.

### Files to search and replace:
Search ALL files in `src/` (including subdirectories), plus:
- `CLAUDE.md`
- `CLAUDE_ADDITIONS.md`
- `CODEX_CONTENT_REFERENCE.md`
- `MERIDIAN_CREW_REFERENCE.md`
- `template.html`
- `build.py`
- `split_tabs.py`
- `extract.py`

### Replacement patterns (case-sensitive, in order):
1. `TETHYS` → `TIDUS` (all-caps, used in CSS class names or headers)
2. `Tethys` → `Tidus` (standard capitalized)
3. `tethys` → `tidus` (lowercase, used in CSS classes, JS variables, HTML IDs)

### CSS-specific renames:
In `src/head/styles.css`:
- `.dot-tethys` → `.dot-tidus`
- Any other class containing `tethys` → replace with `tidus`

### JS-specific renames:
In `src/scripts/main.js`:
- Search for any `tethys` in variable names, IDs, or strings → replace with `tidus`

### Template/Build renames:
In `template.html` and `build.py`:
- Any `TETHYS` or `tethys` placeholders or fragment references → `TIDUS` / `tidus`

### Image manifest update:
In `src/images/manifest.json`:
- `"IMG_TETHYS_AWAKENING": "images/tethys-awakening.b64"` → `"IMG_TIDUS_AWAKENING": "images/tidus-awakening.b64"`
- Also rename the actual file: `src/images/tethys-awakening.b64` → `src/images/tidus-awakening.b64`

### HTML placeholder updates:
Search all `src/tabs/` and `src/tabs/panels/` files for `{{IMG_TETHYS_AWAKENING}}` → `{{IMG_TIDUS_AWAKENING}}`

### Verification:
After replacement, grep the entire `src/` directory for any remaining "Tethys" or "tethys" — should find ZERO.

---

## Step 2: Global "hamster" → "chinchilla" (Rime Context Only)

**IMPORTANT:** "hamster" may appear in contexts unrelated to Rime (e.g., the Hamster Suplex technique name might survive as a legacy name, or "hamster" might appear in a general description). Review each instance individually. In ALL cases referring to Rime's species, replace with "chinchilla."

### Search all source files for "hamster" (case-insensitive):
- `Hamster` → `Chinchilla` (in species descriptions, titles, headers)
- `hamster` → `chinchilla` (in prose descriptions)
- `HAMSTER` → `CHINCHILLA` (if any all-caps instances exist)
- `Hamster (Mink Hybrid)` → `Chinchilla (Mink Hybrid)` in MERIDIAN_CREW_REFERENCE.md
- `hamster-shaped` → `chinchilla-shaped` (Rime Sphere references)

### Special cases:
- "Hamster Suplex" technique name → rename to "Chinchilla Suplex" (the technique stays, just the species word changes)
- "Rime Sphere" stays as-is (it's not species-specific)
- Any "hamster ball" jokes → "chinchilla ball" equivalent

---

## Step 3: 🐹 Emoji Replacement

The hamster emoji 🐹 appears in approximately 18 locations across source files (mostly in `src/tabs/` and `CODEX_CONTENT_REFERENCE.md`). It needs to be replaced with an inline chinchilla emoji image.

### Image source:
The file `Rime_emoji.png` (205KB) exists in the repository root. This is a small gray chinchilla on a black background with the background removed.

### Process:
1. **Convert `Rime_emoji.png` to base64:**
   ```bash
   base64 -i "Rime_emoji.png" > src/images/rime-emoji.b64
   ```
   Then prepend `data:image/png;base64,` to the file contents (or handle in the build script).

2. **Add to image manifest** (`src/images/manifest.json`):
   ```json
   "IMG_RIME_EMOJI": "images/rime-emoji.b64"
   ```

3. **Add CSS class** to `src/head/styles.css`:
   ```css
   .chinchilla-emoji {
       display: inline-block;
       width: 1.2em;
       height: 1.2em;
       vertical-align: -0.15em;
       object-fit: contain;
   }
   ```

4. **Replace all 🐹 instances** in source HTML files with:
   ```html
   <img src="{{IMG_RIME_EMOJI}}" alt="chinchilla" class="chinchilla-emoji">
   ```

5. **In `CODEX_CONTENT_REFERENCE.md`** (markdown, not HTML), replace 🐹 with 🐭 or simply the text `[chinchilla]` — the markdown mirror doesn't need the image tag.

### Files containing 🐹 (from grep):
- `src/tabs/16-world-response.html` (1)
- `src/tabs/09-auxiliary-protocols.html` (1)
- `src/tabs/07-fighting-styles.html` (1)
- `src/tabs/11-inner-world.html` (1)
- `src/tabs/06-companions.html` (1)
- `src/tabs/panels/06-companions-rime.html` (1)
- `CODEX_CONTENT_REFERENCE.md` (6)
- `hive_codex__35_.html` (6) — DO NOT EDIT THIS FILE (it's the old monolith reference)

---

## Step 4: Species Description Rewrites

### 4a: Rime — Chinchilla Description

Read `src/tabs/panels/06-companions-rime.html` and rewrite the species/appearance section.

**Key changes:**
- Species: Chinchilla (Mink Hybrid), not hamster
- Fur: Orange/red fur (matching existing `#E08070` CSS color). Incredibly soft and dense — chinchilla fur is the softest of any land animal
- Body: Round, plush, slightly larger than a hamster. Big ears (chinchilla signature). Large dark eyes
- Tail: Long, fluffy chinchilla tail (hamsters have stubby tails — this is a notable visual change)
- Personality: UNCHANGED — chaotic, grandiose, fearless, reckless gremlin energy. The chinchilla body makes his absurd confidence even funnier
- NEW detail: Dust bathing is a chinchilla necessity. Rime is extremely particular about his dust quality (this will be expanded in Phase 2 with combat applications)
- Vocalizations: Chinchillas chitter, bark, and squeak. The existing "chattering" and "chittering" references work. Verify and adjust any hamster-specific sounds

**Voice reference for rewrites:** "I am the greatest martial artist on this ship and I WILL be taken seriously." (He will not be taken seriously. He is a fluffy chinchilla with the confidence of an emperor.)

### 4b: Tidus — Polar Bear–Sea Otter Hybrid Description

Read `src/tabs/panels/06-companions-tethys.html` (which is now `06-companions-tidus.html` after Step 1 rename) and COMPLETELY REWRITE the species/appearance section.

**Key changes — Appearance:**
- Species: Polar Bear–Sea Otter Hybrid (Vegapunk Experiment + Fishman DNA + Pacifista Modifications)
- Fur: White/cream base (polar bear) with the dense, water-repellent quality of sea otter fur. When wet, his fur has an iridescent sheen from his bio-film (clownfish DNA)
- Body: Adorably chubby. Round belly. Slightly oversized paws. Dense muscle hidden under softness. He looks like a stuffed animal that wandered into a battlefield
- Eyes: Blue eyes, warm and gentle
- Tail: More otter than bear — flat, broad, useful for swimming and balance
- Feet: Slightly webbed (otter influence), with the heavy-set paws of a polar bear
- Size: Comparable to existing Tethys size (large enough to be imposing, adorable enough to be hugged)
- Pacifista modifications: INTERNAL and not visually obvious — another reason the researchers thought the experiment failed

**Key changes — Background:**
- Origin: Vegapunk experiment — intended to create a fearsome aquatic predator hybrid (polar bear strength + sea otter agility + Fishman DNA + Pacifista weapons). What they got was an overwhelmingly adorable creature whose appearance is the opposite of intimidating
- Why "failed": His gentle personality + adorable appearance + preference for building over destroying = classified as failed experiment
- Fishman DNA: Clownfish + Fancy Goldfish (ranchu/oranda type). NOT mantis shrimp or pistol shrimp (those are REMOVED)
  - Clownfish: Protective bio-film coating (toxin/acid immunity, extendable to allies). Fierce territorial instinct despite small size. Symbiotic protection DNA
  - Fancy Goldfish: Adorable roundness, deceptive softness, extraordinary resilience. Hardy beyond appearance
- IMPORTANT: Never call the bio-film "mucus" — use "protective film," "bio-film membrane," "film coating," "film-coated barriers"

**Key changes — Name Origin (COMPLETE REWORK):**
- OLD story (REMOVE ENTIRELY): Ceramic shard in laboratory aquarium depicting Titan goddess of freshwater. The "Tethys the fictional crab" reference. ALL of this is gone.
- NEW story: As a baby in Vegapunk's lab, Tidus could hear the tides through the walls. The rhythmic sound of water was the only comforting thing in his world. When he first tried to speak, he attempted to say "tides" — the word that meant safety, comfort, the thing that never stopped coming back. What came out was "Tidus." He never corrected it. The researchers logged it as a designation error. It was the first thing he ever named himself.
- Pronunciation: TIE-dus (like "tide" + "us")

**Key changes — Vocalizations:**
Replace ALL "clicking" (crab) with polar bear-otter sounds:
- Chuffing — contentment, greeting
- Low rumbling purr — comfort, protective mode
- Sharp bark — alarm, combat intensity
- Cooing chirp — happy sound (sea otter influence)

Search `src/tabs/panels/06-companions-tidus.html` and all other files for "clicking contentedly," "clicking happily," "clicks," etc. in Tidus' context and replace with the new sounds.

**Key changes — Anatomy references to remove/replace:**
- "claws" → "paws" (in Tidus context — Rime can have "claws" as chinchillas have them)
- "carapace" → remove entirely (Tidus has no shell)
- "chitin" → remove entirely
- "shell" → remove (except when referring to the shell shovel weapon)
- "segmented body" → remove
- "scuttling" / "scuttle" → "lumbering" / "padding" / "charging"
- "lateral movement" → remove (bears move forward, not sideways)
- "crab" / "crustacean" → remove in Tidus context
- "hydraulic" locomotion → remove (bears don't have hydraulic movement)
- "mechanical arms" → remove (Tidus has regular polar bear-otter arms/paws)
- "six legs" → remove (Tidus has four limbs like a bear/otter)
- "retractable mechanical arms" → remove
- Pocchi "rides in Tethys' carapace compartment" → Pocchi rides in Tidus' fur (nestled in the thick fur on his back or shoulder)

**Voice reference for rewrites:** Warm, gentle, brilliant, funny in a Claptrap/oblivious-genius way. He doesn't want to fight. He builds, he protects, he apologizes to people he's hurt. His comedy comes from the gap between his terrifying capabilities and his overwhelming kindness. He checks if opponents are okay after hitting them.

---

## Step 5: Update Reference Documents

### MERIDIAN_CREW_REFERENCE.md:
- Rime: `Hamster (Mink Hybrid)` → `Chinchilla (Mink Hybrid)`
- Tethys row → Tidus: `Crab Creature (Fishman Hybrid + Pacifista)` → `Polar Bear–Sea Otter Hybrid (Vegapunk Experiment + Fishman DNA + Pacifista)`
- Remove "Has claws (intentional)" from Tidus' Key Notes
- Update Tidus' Key Notes to: "Builder of the Meridian. Adorably chubby. Blue eyes."
- Copplings section header: "Tethys' Mechanical Creations" → "Tidus' Mechanical Creations"
- Akebono: "Rescued by Tethys" → "Rescued by Tidus"
- Xylem: "Built by Tethys for Claude" → "Built by Tidus for Claude"
- Bobbin: "Tethys' (secret) favorite" → "Tidus' (secret) favorite"

### CLAUDE.md:
- ALL "Tethys" → "Tidus" (already done by Step 1 global replace, but verify)
- "Tethys is a crab creature with natural claws and two retractable mechanical arms. He also has six legs." → "Tidus is a polar bear–sea otter hybrid with white/cream fur, blue eyes, and slightly webbed paws. He looks like a stuffed animal that wandered into a battlefield. This adorable appearance is intentional — it's the reason Vegapunk classified him as a 'failed' experiment."
- Verify Critical Rule #2 is updated

### CODEX_CONTENT_REFERENCE.md:
- All "Tethys" → "Tidus" (Step 1)
- All "hamster" → "chinchilla" in Rime context (Step 2)
- All 🐹 → `[chinchilla]` text placeholder (Step 3)
- Update species descriptions to match new content

### CLAUDE_ADDITIONS.md:
- All "Tethys" → "Tidus" (Step 1)
- All "hamster" → "chinchilla" in Rime context (Step 2)

---

## Step 6: Image Replacement — New Character Art

### New images available in repo root:
- `Rime_awakening_new.png` (2.5M) — replaces `rime-awakening.b64`
- `Rime_combat profile.png` (2.2M) — replaces portrait image for Rime
- `Rime_self portrait.png` (2.6M) — replaces companion portrait for Rime
- `Rime_emoji.png` (205K) — new chinchilla emoji (handled in Step 3)
- `Tidus_awakening.png` (2.9M) — replaces `tethys-awakening.b64` → `tidus-awakening.b64`
- `Tidus_combat profile.png` (2.9M) — replaces portrait image for Tidus
- `Tidus_self portrait.png` (2.7M) — replaces companion portrait for Tidus

### Process for each image:
1. Convert PNG to base64:
   ```bash
   base64 -i "Rime_awakening_new.png" | { echo -n "data:image/png;base64,"; cat; } > src/images/rime-awakening.b64
   ```
2. Verify the `.b64` file is well-formed (check first ~80 chars with `head -c 80`)
3. The manifest already maps the token to the `.b64` file, so the build script handles the rest

### Image mapping:
| New File | Target .b64 | Manifest Token | Notes |
|----------|------------|----------------|-------|
| `Rime_awakening_new.png` | `src/images/rime-awakening.b64` | `IMG_RIME_AWAKENING` | Overwrite existing |
| `Rime_combat profile.png` | Identify which portrait slot is Rime's combat profile | `IMG_PORTRAITS_?` | Check `src/tabs/05-portraits.html` to find which portrait slot |
| `Rime_self portrait.png` | `src/images/companions-0.b64` OR a specific portrait | Check companion tab | May need to identify exact slot |
| `Rime_emoji.png` | `src/images/rime-emoji.b64` | `IMG_RIME_EMOJI` (NEW) | New manifest entry |
| `Tidus_awakening.png` | `src/images/tidus-awakening.b64` | `IMG_TIDUS_AWAKENING` | Renamed from tethys |
| `Tidus_combat profile.png` | Identify which portrait slot is Tidus' combat profile | `IMG_PORTRAITS_?` | Check portraits tab |
| `Tidus_self portrait.png` | Identify companion portrait slot | Check companion tab | May need to identify exact slot |

**IMPORTANT:** To identify which manifest tokens map to Rime/Tidus portraits, read `src/tabs/05-portraits.html` and `src/tabs/06-companions.html` to see which `{{IMG_*}}` placeholders are used for each character. Do NOT read .b64 files.

---

## Step 7: Build & Verify

1. Run `python build.py`
2. Verify clean compilation (no errors)
3. Run a grep on `dist/hive_codex.html` for orphaned references:
   - `grep -c "Tethys" dist/hive_codex.html` — should be 0
   - `grep -c "hamster" dist/hive_codex.html` — should be 0 in Rime context (review any hits)
   - `grep -c "🐹" dist/hive_codex.html` — should be 0
   - `grep -c "crustacean" dist/hive_codex.html` — may still appear if not yet rewritten (Phase 3 handles combat details)
   - `grep -c "carapace" dist/hive_codex.html` — may still appear (Phase 3 handles)
4. Verify div balance: count opening and closing `<div>` tags, ensure they match

---

## Phase 1 Completion Checklist
- [ ] All "Tethys" → "Tidus" globally (zero remaining instances)
- [ ] All "hamster" → "chinchilla" in Rime context
- [ ] 🐹 → chinchilla emoji image in all HTML source files
- [ ] Rime companion panel rewritten with chinchilla species details
- [ ] Tidus companion panel rewritten with polar bear–sea otter hybrid details
- [ ] New name origin story for Tidus (baby voice "tides")
- [ ] Old name origin (ceramic shard) completely removed
- [ ] Vocalization replacements done (clicking → chuffing/purring/barking/chirping for Tidus)
- [ ] MERIDIAN_CREW_REFERENCE.md updated
- [ ] CLAUDE.md updated (Critical Rule #2, all references)
- [ ] CODEX_CONTENT_REFERENCE.md updated
- [ ] CLAUDE_ADDITIONS.md updated
- [ ] New character images converted to .b64 and placed in src/images/
- [ ] Image manifest updated (rime-emoji, tidus-awakening rename)
- [ ] CSS class `.dot-tethys` → `.dot-tidus`
- [ ] CSS class `.chinchilla-emoji` added
- [ ] `python build.py` runs clean
- [ ] Div balance verified
