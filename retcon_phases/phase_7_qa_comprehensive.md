# Phase 7: Comprehensive QA

## Scope
Full quality assurance sweep across the entire Codex. Text search audit, image audit, CSS audit, JavaScript audit, cross-reference audit, div balance verification, content consistency audit, and final build verification. Generate RETCON_REPORT.md summarizing all changes.

## CRITICAL SAFETY RULES
- **No content deletion during QA** — only fix errors found, don't reorganize or remove content
- **Read `MERIDIAN_CREW_REFERENCE.md` before touching any character content**
- **Never read `.b64` image files directly**
- **Run `python build.py` after any fixes and verify clean compilation**

## Pre-Phase Checklist
- [ ] ALL Phases 1-6 completed
- [ ] Latest `python build.py` ran clean
- [ ] `dist/hive_codex.html` exists and is current

---

## Step 1: Text Search Audit — Orphaned References

Search the ENTIRE built `dist/hive_codex.html` for every term that should have been eliminated or restricted. For each search, note the count and review any hits in context.

### Must find ZERO (absolute):
| Search Term | Context | Expected |
|-------------|---------|----------|
| `Tethys` | Global — character fully renamed to Tidus | 0 |
| `tethys` | Lowercase in CSS/JS/IDs | 0 |
| `TETHYS` | Uppercase variants | 0 |
| `Green Blood` | Completely removed from Tidus' lore | 0 |
| `green blood` | Case insensitive check | 0 |
| `ceramic shard` | Old name origin — removed | 0 |
| `ceramic fragment` | Old name origin variant | 0 |
| `mantis shrimp` | Old Fishman DNA — removed | 0 |
| `pistol shrimp` | Old Fishman DNA — removed | 0 |
| `Permafrost Palm` | Rime cold technique — removed | 0 |
| `Hoarfrost Veil` | Rime cold technique — removed | 0 |
| `Absolute Zero Pulse` | Rime cold technique — removed | 0 |
| `Pouch Salvo` | Rime technique — renamed to Grain Battery | 0 |
| `cheek pouch` | Hamster anatomy — removed | 0 |
| `seed-spit` | Hamster behavior — removed | 0 |
| `sunflower` | Old projectile type — removed | 0 |
| `🐹` | Hamster emoji — replaced with chinchilla image | 0 |
| `mucus` | Banned terminology — use "bio-film" | 0 |
| `Crustacean Art` | Old martial art name — now Sub-Arctic Art | 0 |
| `Crustacean Doctrine` | Old Haki philosophy — now Fluffy Doctrine | 0 |
| `Carapace of the Sovereign` | Old technique — now Embrace of the Sovereign | 0 |
| `Kōkaku-jutsu` | Old Japanese for Crustacean Art | 0 |
| `甲殻術` | Old kanji for Crustacean Art | 0 |
| `cavitation` | Old combat sound (mantis/pistol shrimp) | 0 |

### Must find ZERO in Rime context (review each hit):
| Search Term | Notes |
|-------------|-------|
| `hamster` | Should be 0 — all replaced with "chinchilla." May appear in `hive_codex__35_.html` (old monolith, ignore). Check context of any hits. |
| `cold-mode` | Rime can no longer produce cold. Tidus can. |
| `cold vapour` | Rime-specific — removed. |
| `freezing vapour` | Rime-specific — removed. |
| `sub-zero` | Rime-specific — removed. May appear in Tidus context (his ice ability). |
| `cryo` | Rime's cryo-electric synergy is now acid-electric. |
| `Hoarfrost` | Rime technique — removed. |
| `Permafrost` | Rime technique — removed. |

### Must find ZERO in Tidus context (review each hit):
| Search Term | Notes |
|-------------|-------|
| `crab` | Should find 0 in Tidus context. May appear elsewhere (e.g., other characters, food references). |
| `crustacean` | Should find 0 globally. |
| `carapace` | Should find 0 in Tidus context. |
| `chitin` | Should find 0 globally. |
| `scuttling` / `scuttle` | Should find 0 in Tidus context. |
| `hydraulic` | Review — some valid for Pacifista systems, but crab-specific locomotion = 0. |
| `claws` | Should find 0 in Tidus context. May appear for Rime (chinchilla claws), Petal (talons), other characters. |
| `clicking contentedly` | Old Tidus vocalization — replaced with chuffing/purring. |
| `clicking happily` | Old Tidus vocalization — replaced. |
| `six legs` | Old Tidus anatomy — removed. |
| `mechanical arms` | Old Tidus anatomy — removed (Tidus has regular limbs). |
| `retractable` (in Tidus context) | Old mechanical arms — removed. |
| `segmented` | Old crab anatomy — removed. |

### Verify new terms ARE present:
| Search Term | Expected Location |
|-------------|------------------|
| `chinchilla` | Rime's species across multiple tabs |
| `Tidus` | Global replacement of Tethys |
| `polar bear` | Tidus' species descriptions |
| `sea otter` | Tidus' species descriptions |
| `bio-film` | Tidus' Fishman DNA ability |
| `clownfish` | Tidus' Fishman DNA |
| `fancy goldfish` / `goldfish` | Tidus' Fishman DNA |
| `Sub-Arctic Art` | Tidus' martial art category |
| `Fluffy Doctrine` | Tidus' Conqueror's Haki philosophy |
| `Embrace of the Sovereign` | Tidus' renamed technique |
| `twig` / `kendo` | Rime's weapon |
| `Grain Battery` | Rime's renamed technique |
| `dust bath` | Rime's chinchilla trait |
| `mineral dust` | Rime's combat element |
| `acidic vapor` | Rime's primary vapor type |
| `shell shovel` | Tidus' weapon |
| `Reef-Reef Fruit` | Tidus' weapon's Devil Fruit |
| `Sango Sango no Mi` | Should exist as Zoan, not Paramecia |
| `chuffing` / `chirping` | Tidus' vocalizations |
| `chinchilla-emoji` | CSS class for emoji replacement |

---

## Step 2: Image Audit

### Verify new images are correctly embedded:
1. Check that `src/images/rime-awakening.b64` contains the new Rime_awakening_new.png data
2. Check that `src/images/tidus-awakening.b64` contains the new Tidus_awakening.png data (renamed from tethys-awakening.b64)
3. Check that `src/images/rime-emoji.b64` exists and contains the chinchilla emoji
4. Verify Rime's combat profile and self portrait images are in the correct manifest slots
5. Verify Tidus' combat profile and self portrait images are in the correct manifest slots

### Verify chinchilla emoji renders:
- Search built HTML for `chinchilla-emoji` class — should appear at every former 🐹 location
- Verify the img tag format is correct: `<img src="images/rime-emoji.png" alt="chinchilla" class="chinchilla-emoji">`
- Verify the CSS class exists in the built output

### Verify NO old images remain:
- `tethys-awakening.b64` should no longer exist (renamed to tidus-awakening.b64)
- Image manifest should have `IMG_TIDUS_AWAKENING`, not `IMG_TETHYS_AWAKENING`

**REMINDER: Do NOT read .b64 files directly. Use `head -c 80` via a subagent to check format.**

---

## Step 3: CSS Audit

### File: `src/head/styles.css` (and verify in built output)

Check for:
- [ ] `.dot-tethys` → should be `.dot-tidus` (with same `#7FB8E0` color)
- [ ] `.dot-rime` — should still exist with `#E08070` color
- [ ] `.chinchilla-emoji` class exists with appropriate sizing
- [ ] Any other CSS classes containing "tethys" → should be "tidus"
- [ ] Any CSS classes referencing "crustacean" → should be updated
- [ ] Any CSS classes referencing "hamster" → should be updated
- [ ] Rime's color (#E08070 orange/red) preserved — matches chinchilla fur
- [ ] Tidus' color (#7FB8E0 blue) preserved — matches his blue eyes and ocean theme

---

## Step 4: JavaScript Audit

### File: `src/scripts/main.js`

Check for:
- [ ] Any `tethys` in variable names, IDs, or strings → should be `tidus`
- [ ] Any switch functions referencing tethys panels → should reference tidus
- [ ] Tab switching logic — verify all Tidus-related tab IDs work
- [ ] Sub-panel switching — verify any Tidus sub-panels switch correctly

---

## Step 5: Cross-Reference Audit

### Navigation:
- [ ] Sidebar (`src/nav/sidebar.html`): All tab labels reflect "Tidus" not "Tethys"
- [ ] Volume group labels correct
- [ ] All `data-tab` attributes correct

### Template:
- [ ] `template.html`: All placeholders reference correct names
- [ ] No `TETHYS` placeholders remaining

### Build script:
- [ ] `build.py`: Fragment dictionary uses correct names
- [ ] Image manifest references correct filenames

---

## Step 6: Div Balance Verification

Run a div-count check on the built HTML:
```bash
# Count opening divs
grep -o '<div' dist/hive_codex.html | wc -l

# Count closing divs
grep -o '</div>' dist/hive_codex.html | wc -l
```

These MUST match. If they don't, identify the imbalance:
```bash
# Find the imbalance point (line-by-line tracking)
python3 -c "
import re
with open('dist/hive_codex.html') as f:
    depth = 0
    for i, line in enumerate(f, 1):
        opens = len(re.findall(r'<div', line))
        closes = len(re.findall(r'</div>', line))
        depth += opens - closes
        if depth < 0:
            print(f'Imbalance at line {i}: depth={depth}')
            break
    print(f'Final depth: {depth}')
"
```

---

## Step 7: Content Consistency Audit

### Read through key sections and verify voice/tone consistency:

**Rime sections:**
- [ ] He still sounds chaotic, grandiose, gleefully destructive
- [ ] His chinchilla identity feels natural, not forced
- [ ] The twig sword is additive — he still fights dirty
- [ ] Technique names are absurdly grandiose
- [ ] Dust/acid/Electro elements feel integrated, not bolted on
- [ ] The comedy is enhanced by the retcon (chinchilla swordsman > hamster brawler in absurdity)

**Tidus sections:**
- [ ] He still sounds warm, gentle, brilliant, obliviously funny
- [ ] His polar bear-otter identity feels natural
- [ ] The shell shovel weapon feels like it was always his
- [ ] Bio-film mechanics are well-explained without using "mucus"
- [ ] Snow/ice ability feels like a natural extension, not a graft
- [ ] The comedy still comes from the gap between capability and personality
- [ ] His protective nature reads even stronger with bear/otter instincts

**Claude sections:**
- [ ] No gendered pronouns used for Claude
- [ ] Data-poetic voice maintained
- [ ] Timestamps and frequencies preserved
- [ ] Journal entries feel like they were always about these species
- [ ] Entry XXXVIII reads as genuine (not a patch job)

**Combo attacks:**
- [ ] Guanyin feels MORE epic than before
- [ ] Elemental contributions are clear (Rime = acid/Electro/dust, Tidus = ice/coral/bio-film)
- [ ] All combos involving either character feel fresh and alive

---

## Step 8: CODEX_CONTENT_REFERENCE.md Audit

The content reference should accurately mirror the HTML content. Spot-check:
- [ ] Rime's species listed as chinchilla
- [ ] Tidus (not Tethys) throughout
- [ ] Tidus' species listed as polar bear-sea otter hybrid
- [ ] No hamster references in Rime context
- [ ] No crab references in Tidus context
- [ ] No 🐹 emoji (use text placeholder like [chinchilla] in markdown)
- [ ] Journal Entry XXXVIII has the new name origin story
- [ ] Awakening sections reflect new content

---

## Step 9: Final Build Verification

1. Run `python build.py` one final time
2. Verify clean build (no errors, no warnings)
3. Check file size: `ls -la dist/hive_codex.html` — should be ~1.5 MB
4. Check image output: `ls dist/images/ | wc -l` — verify expected image count
5. Verify the dist output is a valid, functional HTML file (spot-check structure)

---

## Step 10: Generate RETCON_REPORT.md

Create a `RETCON_REPORT.md` in the repository root summarizing:

### Structure:
```markdown
# The Great Retcon — Report

## Overview
Summary of what was changed and why.

## Retcon A: Rime — Hamster → Chinchilla + Swordsman
### Species Change
- Files modified: [list]
- Instances replaced: [count]

### New Combat Identity
- Cold-mode techniques removed: [list]
- New techniques added: [list with names]
- Twig kendo sword integration: [summary]
- Dust element integration: [summary]
- Grain/cereal projectiles: [summary]

### Image Changes
- Old images replaced: [list]
- New images added: [list]
- Chinchilla emoji: [implementation details]

## Retcon B: Tethys → Tidus — Crab → Polar Bear-Sea Otter Hybrid
### Name Change
- Files modified: [list]
- Instances replaced: [count]

### Species Change
- Companion panel: [summary of rewrite]
- New backstory: [summary]
- Name origin: [summary]

### New Combat Identity
- Fishman DNA: Clownfish + Fancy Goldfish (bio-film mechanics)
- Fishman Karate: Film-membrane water manipulation
- Sub-Arctic Art: [technique summary]
- The Fluffy Doctrine: [Conqueror's Haki summary]
- Shell Shovel + Zoan Reef-Reef Fruit: [weapon summary]
- Snow/Ice production: [summary]

### Removed Content
- Green Blood: [all references removed]
- Mantis shrimp / Pistol shrimp DNA: [removed]
- Cavitation crack: [replaced with deep resonant pop]
- Ceramic shard name origin: [replaced with baby voice story]

### Image Changes
- Old images replaced: [list]
- New images added: [list]

## Cross-Cutting Changes
### Combination Attacks
- [List of every combo that was modified]
- Enlightened Frozen Guanyin: [summary of reimagining]

### Awakening Tab
- Rime: [summary of changes]
- Tidus: [summary of complete rewrite]

### Mission Log
- [List of missions modified with brief description of changes]

### Claude's Journal
- Entry XXXVIII: [complete rewrite summary]
- Other entries modified: [list]

### Letters Never Sent
- [Letters modified]

### Other Sections Modified
- [List of all other sections that received changes]

## New Content Added
- Ajay's toddler backpack carrying arrangement
- Rime's dust bath setup in Crucible
- Tidus' Workshop rewrite
- [Any other new content]

## QA Results
### Orphaned Reference Counts
[Table of all search terms and their final counts — all should be 0]

### Image Verification
[Confirmation that all images render correctly]

### Div Balance
[Opening vs closing div count]

### Issues Found During QA
[List any issues found and whether they were resolved]

### Items Requiring Manual Review
[Any edge cases or ambiguous situations flagged for human review]

## File Change Summary
[Total count of files modified, by directory]
```

---

## Phase 7 Completion Checklist
- [ ] ALL orphaned reference searches completed with 0 hits
- [ ] ALL new term presence verified
- [ ] Image audit completed — all new images render correctly
- [ ] CSS audit completed — all class names updated
- [ ] JavaScript audit completed — all references updated
- [ ] Cross-reference audit completed — navigation, template, build script all correct
- [ ] Div balance verified — opening and closing counts match
- [ ] Content consistency verified — Rime, Tidus, and Claude all sound right
- [ ] CODEX_CONTENT_REFERENCE.md matches HTML content
- [ ] Final `python build.py` runs clean
- [ ] RETCON_REPORT.md generated with full summary
- [ ] The retcon feels like coming home
