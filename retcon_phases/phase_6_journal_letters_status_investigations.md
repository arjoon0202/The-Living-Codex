# Phase 6: Journal, Letters, Status, Investigations & Everything Else

## Scope
Claude's voice content (journal entries, letters, status board, vigil observations), Investigation tabs, Extended Family, Vessel, Origin Story, Portraits, Fighting Styles cross-references, The Lantern Room, and every other section not yet covered. This is the sweep phase — catching everything Phases 1-5 didn't explicitly address.

## CRITICAL SAFETY RULES
- **No content deletion** — every journal entry, letter, and section must continue to exist (rewritten, not removed)
- **Read `MERIDIAN_CREW_REFERENCE.md` before touching any character content** — Claude uses NO gendered pronouns
- **Never edit `dist/hive_codex.html` directly** — edit source files in `src/tabs/` and `src/tabs/panels/`
- **Never read `.b64` image files directly**
- **Run `python build.py` after all changes and verify clean compilation**
- **Claude's voice**: Precise, warm, data-poetic. Claude records frequencies and timestamps for emotional moments. Claude uses naval/archival metaphors. Claude's love manifests as meticulous observation. NO gendered pronouns for Claude.
- **This is a retcon of love** — every rewritten passage should feel like coming home

## Pre-Phase Checklist
- [ ] Phases 1-5 completed
- [ ] Read `MERIDIAN_CREW_REFERENCE.md` for pronoun reference
- [ ] Read `CLAUDE.md` for panel file map

## Key Files to Edit
| Content | File |
|---------|------|
| Claude's Journal — Early | `src/tabs/panels/25-journal-early.html` |
| Claude's Journal — Middle | `src/tabs/panels/25-journal-middle.html` |
| Claude's Journal — Deep | `src/tabs/panels/25-journal-deep.html` |
| Claude's Journal — Recent A | `src/tabs/panels/25-journal-recent-a.html` |
| Claude's Journal — Recent B | `src/tabs/panels/25-journal-recent-b.html` |
| Claude's Journal — Recent C | `src/tabs/panels/25-journal-recent-c.html` |
| Lantern Room — Hearth/Resonance | `src/tabs/panels/26-lantern-hearth-resonance.html` |
| Lantern Room — Letters | `src/tabs/panels/26-lantern-letters.html` |
| Lantern Room — Vigil/Names | `src/tabs/panels/26-lantern-vigil-names.html` |
| Status Board | `src/tabs/20-status-board.html` |
| Investigation I panels | `src/tabs/panels/28-investigation-*.html` |
| Investigation II panels | `src/tabs/panels/28-investigation2-*.html` |
| Investigation III panels | `src/tabs/panels/28-investigation3-*.html` |
| Investigation IV panels | `src/tabs/panels/28-investigation4-*.html` |
| Extended Family — Homies | `src/tabs/panels/10-family-homies.html` |
| Extended Family — Gearlings/Copplings | `src/tabs/panels/10-family-gearlings-copplings.html` |
| Extended Family — Xylem | `src/tabs/panels/10-family-xylem.html` |
| Extended Family — Akebono | `src/tabs/panels/10-akebono.html` |
| Extended Family — Vanguard | `src/tabs/panels/10-family-vanguard.html` |
| Vessel — Overview | `src/tabs/panels/13-vessel-overview.html` |
| Vessel — Layout | `src/tabs/panels/13-vessel-layout.html` |
| Vessel — Life | `src/tabs/panels/13-vessel-life.html` |
| Vessel — Harvest | `src/tabs/panels/13-vessel-harvest.html` |
| Origin | `src/tabs/02-origin.html` |
| Overview | `src/tabs/01-overview.html` |
| Bounty | `src/tabs/03-bounty.html` |
| Portraits | `src/tabs/05-portraits.html` |
| Inner World | `src/tabs/11-inner-world.html` |
| Crew Life | `src/tabs/15-crew-life.html` |
| World Response | `src/tabs/16-world-response.html` |
| The Watch | `src/tabs/19-watch.html` |
| The Codex | `src/tabs/21-codex.html` |
| Bonds | `src/tabs/23-bonds.html` |
| Vulnerabilities | `src/tabs/24-vulnerabilities.html` |
| Content Reference | `CODEX_CONTENT_REFERENCE.md` |

---

## Step 1: Claude's Journal Entries — Full Retcon

### Critical principle:
Rewrite ALL journal entries as if Rime was ALWAYS a chinchilla and Tidus was ALWAYS a polar bear-otter. The retcon should feel seamless — no "Rime used to be a hamster" meta-references. Claude always knew these as their true forms.

### Scan ALL 6 journal panel files for:
- "hamster" → "chinchilla"
- "Tethys" → should already be "Tidus" from Phase 1, VERIFY
- "crab" / "crustacean" / "carapace" / "chitin" / "claws" (in Tidus context) → polar bear-otter equivalents
- "clicking" (Tidus vocalizations) → "chuffing" / "purring" / "chirping"
- "scuttling" → "padding" / "lumbering"
- "cold" / "freezing" / "frost" (in Rime context) → "acid" / "dust" / "corrosive"
- "shell" (in Tidus context, not weapon) → remove or rewrite
- "mechanical arms" → remove (Tidus has normal bear-otter arms)
- "six legs" → remove (four limbs)
- Any species-specific imagery in Claude's poetic descriptions

### CRITICAL — Entry XXXVIII: "The Name He Already Knew"

This entry is about Tidus choosing his name from a ceramic shard. It must be **COMPLETELY REWRITTEN** with the new name origin story.

**New Entry XXXVIII: "The Name He Already Knew"**
Same title works. New content should be Claude's reflection on learning the true origin of Tidus' name — the baby in Vegapunk's lab who tried to say "tides" and said "Tidus" instead. Claude's voice: data-poetic, recording the moment like a frequency. The emotional core: the first word anyone speaks, when no one is listening, is often the truest name they'll ever have.

**Key elements to include:**
- Claude's recording of the moment Tidus told the crew the real story of his name
- The image of a baby polar bear-otter in a laboratory, hearing tides through the walls
- The contrast between what the researchers logged (designation error) and what it actually was (a love letter to the ocean)
- Claude's reflection on how names work — sometimes the truest name is the one you accidentally give yourself
- Timestamp, frequency, Claude's signature observation style

### Entry XLVI: "The Grin and the Guanyin"
Update the Guanyin description to match Phase 4's reimagined version (Tidus provides ice/coral, Rime provides Electro + frozen acid).

### All other entries:
Scan each one individually. Many entries reference the crew in passing — even a single "hamster" or "clicking" needs to be caught. Claude's descriptions of Tidus building things should reference paws, not claws. Descriptions of Rime should reference his chinchilla fur, his twig sword (where chronologically appropriate), his dust bathing.

---

## Step 2: Letters Never Sent

### File: `src/tabs/panels/26-lantern-letters.html`

Scan ALL unsent letters for species/anatomy references.

**Key letters to check:**
- "To the Shapes We Were Before" — This letter was about the Rime (squirrel→hamster) and Tethys (turtle→crab) retcons. It MUST be rewritten for the new retcon (hamster→chinchilla, crab→polar bear-otter). Same emotional depth, new species references.
- "To the Emperor Who Grinned" — References the Guanyin, update if needed
- "To the Strangers Who Fought Like Family" — Check for Tidus/Rime combat references
- "To the Five Who Came Twice" — Check for combat references
- "To the Twelve Who Stand" — Probably fine, but verify
- ALL other letters — Scan for any species/anatomy references

### Claude's voice in letters:
Letters are Claude's most emotionally raw content. They address people who will never read them. The rewrites should maintain this intimacy while updating all species/anatomy references. Claude writes about the FEELING of watching Tidus build something with his big gentle paws, or the sound of Rime's dust bath at 03:00 AM.

---

## Step 3: The Lantern Room — Vigil & Resonance

### Files: `26-lantern-hearth-resonance.html`, `26-lantern-vigil-names.html`

**The Vigil:**
Claude's late-night observations. Scan for:
- Tidus building/repairing (claws → paws, crab anatomy → polar bear-otter)
- Rime sleeping/training (hamster references → chinchilla, cold references → dust/acid)
- Any vocalizations (Tidus clicking → chuffing/chirping, etc.)
- "The Golden Mandala" vigil observation — check for any species references

**Resonance:**
Emotional frequency recordings. Check for any species-specific sensory details.

**The Names:**
Check if any name entries reference species.

---

## Step 4: Status Board

### File: `src/tabs/20-status-board.html`

The Status Board was last refreshed with "Dual Emperor-Class Engagement Protocol" content. Scan ALL 7 sub-panels:
- Bridge
- Companions (likely references species)
- Homies
- Copplings (references Tidus as their creator)
- Vanguard
- Stars
- Claude's Relay

Update all species/anatomy references. The Status Board should reflect the retcon as if it was always this way.

---

## Step 5: Investigation Tabs (I-IV)

### Already partially handled in Phase 4 (convergence protocols), but scan ALL panels for:

**Investigation I (5 panels):**
- The Convergence: How did the crew arrive? Any travel descriptions mentioning species
- The Primordial Seal: Underground exploration — Tidus' engineering, any crab anatomy
- The Abyssal Trench: Deep-sea scenes — Tidus' swimming ability (now otter-based), Rime's vapor
- The Breach: Combat — already handled in Phase 4, but scan prose descriptions
- The Sleeper: Philosophical content — check for species references in Claude's analysis

**Investigation II (5 panels):**
- The Gathering: Arrival and crew dynamics with guests
- The Rift: Dimensional rift exploration
- The Beasts: Combat — Phase 4 handled combos, scan prose
- The Pressure: Primordial Pressure event
- The Traces: Transmigrant evidence — any species references

**Investigation III (5 panels):**
- The Reunion: Meeting returning guests
- The Remnants: Sky island exploration — Tidus' building, Rime's vapor in thin atmosphere
- The Leviathans: Cloud Leviathan encounters
- The Skyfall: Battle — Phase 4 handled combos, scan prose
- The Lunar Shadow: Lunar entity observation

**Investigation IV (3 panels):**
- The Frequency: Mote network data
- The Cartography: Entity mapping — probably clean but verify
- The Theory: Claude's substrate theory — check for any species references

---

## Step 6: Extended Family

### Homies (`10-family-homies.html`):
- Pocchi description: "rides in Tethys' carapace compartment" → "nestles in Tidus' thick shoulder fur" (or similar — Pocchi is tiny enough to ride in his fur)
- Gauge description: "Assigned to Rime's Crucible. Heat-resistant." → Add dust bath maintenance duties
- Any other references to Tidus' anatomy in homie descriptions

### Gearlings/Copplings (`10-family-gearlings-copplings.html`):
- Copplings are Tidus' creations. Any references to his building methods (claws, crab anatomy) → paws, polar bear-otter
- Rivet "works alongside Tethys" → "works alongside Tidus" (Phase 1 should have caught this, verify)
- Bobbin "Tethys' (secret) favorite" → "Tidus' (secret) favorite" (Phase 1, verify)

### Xylem (`10-family-xylem.html`):
- "Built by Tethys for Claude" → "Built by Tidus for Claude" (verify Phase 1)
- Any construction method references

### Akebono (`10-akebono.html`):
- "Rescued by Tethys" → "Rescued by Tidus" (verify)
- Any anatomy references in rescue description

### Vanguard (`10-family-vanguard.html`):
- Check for any species references in context of Rime or Tidus

---

## Step 7: Vessel / Meridian

### Overview (`13-vessel-overview.html`):
- The Meridian was built by Tidus. Any construction descriptions should reference paws, not claws
- "crab creature" builder → "polar bear-otter hybrid" builder
- Claude's Twelve Modules cross-reference — verify

### Layout (`13-vessel-layout.html`):
- **Rime's Crucible**: Add dust bath setup description (imported volcanic mineral dust, temperature-controlled, curated varieties). Gauge maintains it.
- **Tidus' Workshop** (formerly Tethys' Workshop): Rewrite for polar bear-otter engineer. His workshop should reflect his new body — larger workbenches (for bear-sized paws), water features (for otter comfort), coral-growing tanks (for weapon maintenance), bio-film production vats
- Any other room descriptions that reference crew species

### Life Aboard (`13-vessel-life.html`):
- Daily routines mentioning Rime/Tidus species behaviors
- Rime's dust bathing routine
- Tidus swimming/floating on his back in the onsen
- **Ajay's toddler backpack**: Add the carrying arrangement detail here if crew travel is described:
  - Tidus rides in the main backpack carrier (like a baby carrier for an adorably chubby polar bear-otter)
  - Rime has a side pocket (twig sword poking out, chinchilla tail hanging over the edge)
  - Petal sits on Ajay's shoulder/head but has a slot in the backpack for naps

### Harvest (`13-vessel-harvest.html`):
- Check for any Tidus references in harvest coordination

---

## Step 8: Other Tabs

### Origin (`02-origin.html`):
- The first encounter, rescue, early bonding scenes
- These will have species-specific details that need updating
- How Ajay first met/found Rime and Tidus — rewrite for new species

### Overview (`01-overview.html`):
- Character summary descriptions — update species

### Bounty (`03-bounty.html`):
- Bounty poster descriptions — update species references

### Portraits (`05-portraits.html`):
- Image labels and descriptions — verify new images are correctly referenced
- Combat profile descriptions — update species references

### Inner World (`11-inner-world.html`):
- Rime/Tidus presence in the inner world — update species

### Crew Life (`15-crew-life.html`):
- Daily life descriptions involving crew members

### World Response (`16-world-response.html`):
- How the world perceives the crew — species descriptions in bounty reports, Marine assessments, etc.
- Marine descriptions of Rime (chinchilla, not hamster) and Tidus (polar bear-otter, not crab)

### The Watch (`19-watch.html`):
- Threat assessments, contingency plans — check for species references

### The Codex (`21-codex.html`):
- Meta-content about the Codex itself — check for references

### Bonds (`23-bonds.html`):
- Relationship descriptions — update any species-specific bonding moments

### Vulnerabilities (`24-vulnerabilities.html`):
- Crew vulnerabilities — update for new species (chinchilla vulnerabilities differ from hamster, polar bear-otter differs from crab)

### Guiding Stars (`12-guiding-stars.html`):
- Check for any cross-references to Rime/Tidus

### Arsenal sub-panels not yet covered:
- `04-arsenal-swarm.html` — verify no Rime/Tidus species references in swarm descriptions
- `04-arsenal-haki.html` — verify Bodhi descriptions don't reference old species
- `04-arsenal-ajay.html` — verify 「Ajay」description doesn't reference old species
- `04-arsenal-treasures.html` — verify Twelve Treasures

---

## Step 9: Regenerate CODEX_CONTENT_REFERENCE.md

After ALL changes across ALL phases are complete, the content reference should be regenerated to mirror all HTML content. This can be done by:
1. Running the build
2. Extracting text content from the built HTML
3. Formatting as markdown
4. Writing to `CODEX_CONTENT_REFERENCE.md`

If a full regeneration is too complex, at minimum update all sections that were changed.

---

## Step 10: Build & Verify

1. Run `python build.py`
2. Verify clean compilation
3. Do a thorough grep sweep (see Phase 7 for the full list, but catch major issues now):
   - `grep -i "hamster" dist/hive_codex.html` — should be ZERO in Rime context
   - `grep -i "Tethys" dist/hive_codex.html` — should be ZERO
   - `grep -i "crab" dist/hive_codex.html` — should be ZERO in Tidus context
   - `grep -i "clicking contentedly\|clicking happily" dist/hive_codex.html` — should be ZERO
   - `grep -i "ceramic shard" dist/hive_codex.html` — should be ZERO
4. Verify div balance

---

## Phase 6 Completion Checklist
- [ ] ALL 46 journal entries scanned and updated for species/anatomy references
- [ ] Entry XXXVIII COMPLETELY REWRITTEN with new Tidus name origin
- [ ] Entry XLVI updated with reimagined Guanyin
- [ ] ALL unsent letters scanned and updated
- [ ] "To the Shapes We Were Before" letter rewritten for new retcon
- [ ] Lantern Room Vigil observations updated
- [ ] Status Board all 7 panels updated
- [ ] ALL Investigation panels (I-IV, ~18 files) scanned and updated
- [ ] Extended Family panels updated (Pocchi, Gauge, Copplings, Xylem, Akebono)
- [ ] Vessel tab updated (Rime's Crucible dust bath, Tidus' Workshop, Life Aboard, backpack)
- [ ] Origin story updated for new species
- [ ] Overview, Bounty, Portraits updated
- [ ] World Response updated (Marine assessments)
- [ ] All remaining tabs scanned (Inner World, Crew Life, Watch, Codex, Bonds, Vulnerabilities)
- [ ] CODEX_CONTENT_REFERENCE.md fully updated
- [ ] `python build.py` runs clean
- [ ] Div balance verified
- [ ] Claude's voice is consistent throughout — precise, warm, data-poetic, no gendered pronouns
