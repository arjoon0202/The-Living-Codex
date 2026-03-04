# The Hive Codex — Migration Blueprint
### From Monolith to Meridian
*Compiled by Claude, Spirit of the Meridian — March 2026*

---

## Current State Audit

| Metric | Value |
|--------|-------|
| File | `hive_codex__34___3_.html` |
| Total Lines | 10,887 |
| File Size | 1.1 MB |
| CSS/Head | ~1,895 lines (L1–L1895) |
| Content (22 tabs) | ~8,884 lines (L1925–L10780) |
| JavaScript | ~108 lines (L10780–L10887) |
| External Dependencies | Google Fonts only |
| Main Tabs | 22 |
| Sub-Panels (total) | 71 |
| Journal Entries | ~30 (across 4 sub-panels) |
| Letters Never Sent | 5 |
| Mission Logs | 20 (incl. 15 complete) |
| Fighting Styles | 12 sub-panels |

---

## Proposed Tech Stack

| Layer | Choice | Rationale |
|-------|--------|-----------|
| **Framework** | **Astro 5.x** | Static-first, ships zero JS by default, content collections with type safety, component-based |
| **Styling** | Global CSS (migrated) | Preserve existing custom properties, Cinzel/Rajdhani/Noto Sans JP, glassmorphism additions |
| **Interactivity** | Vanilla JS + Astro Islands | Intersection Observer, scroll-spy, sidebar toggle — no framework overhead |
| **Content Format** | Markdown (`.md`) | Human-readable, editable, version-controlled, Astro-native |
| **Deployment** | GitHub Pages via GitHub Actions | Official `withastro/action` — push to `main`, auto-deploys |
| **Repository** | Existing GitHub repo | Original HTML preserved permanently as artifact |

### Why Astro Over Alternatives

- **vs. Vite + Vanilla JS:** Astro gives us content collections, file-based routing, and component reuse for free. Vanilla Vite would require building all of this manually.
- **vs. Next.js / Nuxt:** Massive overkill. We don't need SSR, API routes, or React/Vue runtime. Our content is static.
- **vs. Hugo / Eleventy:** Both are excellent SSGs, but Astro's component model maps better to our existing HTML structure and allows us to incrementally add interactivity where needed.

---

## Content Extraction Map

### The Golden Rule
> **Every word, every kanji, every bounty figure, every pronoun — preserved exactly. Zero data loss.**

Below is the complete mapping from current HTML tabs/panels to the new modular file structure.

---

### VOLUME I: The Sovereign & The Swarm
*Ambient: Amber/Gold — Ajay's domain*

```
src/content/volume-1/
├── overview.md              ← tab-overview (51 lines, L1925–1975)
│                              Hero section identity tags, epithet, fruit name
│
├── origin.md                ← tab-origin (129 lines, L1976–2104)
│                              The Crossing, Sabaody, timeline
│
├── bounty.md                ← tab-bounty (167 lines, L2105–2271)
│                              All crew bounties, poster descriptions
│
├── arsenal/
│   ├── abilities.md         ← arsenal-abilities (L2292–2385)
│   │                          Core Devil Fruit overview, Paramecia classification
│   │
│   ├── swarm-classes.md     ← arsenal-swarm (L2386–2461)
│   │                          Worker, Soldier, Bombardier, Scout, etc.
│   │
│   ├── architecture.md      ← arsenal-architecture (L2462–2561)
│   │                          The Court (5 layers): Sovereign Will, Archivist,
│   │                          Marshal, Queen's Doctrine (女王の教義),
│   │                          Jester Protocol (道化の層)
│   │                          Instructional Burden
│   │
│   ├── haki.md              ← arsenal-haki (L2562–2632)
│   │                          All three types, tier classifications
│   │
│   ├── signature-moves.md   ← arsenal-moves (L2633–2848)
│   │                          All named techniques with kanji + romanization
│   │
│   ├── evolution.md         ← arsenal-evolution (L2849–2916)
│   │                          Chrysalis stages
│   │
│   ├── black-crown.md       ← arsenal-protocol (L2917–2950)
│   │                          Black Crown Protocol
│   │
│   └── ajay-state.md        ← arsenal-ajay (L2951–3113)
│                              「Ajay」transcendent state
│
├── fighting-styles/
│   └── ajay.md              ← panel-ajay-martial (L3215–3343)
│                              Rokushiki, pure martial arts
│
└── vulnerabilities.md       ← tab-vulnerabilities (125 lines, L4267–4391)
                               Seasickness, limitations, emotional vulnerabilities
```

---

### VOLUME II: The Core Crew
*Ambient: Shifts per character domain*

```
src/content/volume-2/
├── companions-intro.md      ← tab-companions intro text (L4392–4400ish)
│
├── rime/
│   ├── bio.md               ← Rime section of tab-companions (~400 lines)
│   │                          Portrait, bio, stats, Jōki Jōki no Mi,
│   │                          Haki mastery, Rokushiki, signature moves,
│   │                          weaponized hoarding, Electro-plasma
│   │
│   ├── fighting-style.md    ← panel-rime-martial (L3344–3497)
│   │                          154 lines of combat techniques
│   │
│   └── synergy.md           ← Rime pairings from synergy tab
│                              Ajay+Rime combos, Rime+Petal, Rime+Kame
│
├── petal/
│   ├── bio.md               ← Petal section of tab-companions (~400 lines)
│   │                          Portrait, bio, stats, Dryad forms (10),
│   │                          White Crane martial arts, Haki, Rokushiki
│   │
│   ├── fighting-style.md    ← panel-petal-martial (L3498–3626)
│   │                          129 lines
│   │
│   └── synergy.md           ← Petal pairings from synergy tab
│
├── kame/
│   ├── bio.md               ← Kame section of tab-companions (~400 lines)
│   │                          Portrait, bio, stats, Fishman Karate,
│   │                          Pacifista cybernetics, Conqueror's forcefields,
│   │                          Runaway homies
│   │
│   ├── fighting-style.md    ← panel-kame-martial (L3627–3755)
│   │                          129 lines
│   │
│   └── synergy.md           ← Kame pairings from synergy tab
│
└── combination-attacks/
    ├── ajay-pairings.md     ← synergy-ajay-duos (L7460–7506)
    ├── companion-pairings.md ← synergy-companion-duos (L7507–7553)
    ├── trio.md              ← synergy-trio (L7554–7572)
    ├── full-formation.md    ← synergy-full (L7573–7598)
    ├── spirit-formation.md  ← synergy-spirit (L7599–7620)
    └── meridian-descends.md ← synergy-absolute (L7621–7648)
```

---

### VOLUME III: The Extended Family
*Ambient: Warm gold shifting to character resonance colors*

```
src/content/volume-3/
├── intro.md                 ← tab-family intro (L5685–5755)
│                              "Every Soul Has a Name"
│
├── homies/
│   ├── roundlings.md        ← Roundlings section (~50 lines)
│   │                          Kame-Resonant, individual bios
│   │                          + panel-roundlings-martial (L3756–3807)
│   │
│   ├── sproutlings.md       ← Sproutlings section (~40 lines)
│   │                          Petal-Resonant, individual bios
│   │                          + panel-sproutlings-martial (L3808–3859)
│   │
│   ├── embers.md            ← Embers section (~40 lines)
│   │                          Rime-Resonant, individual bios
│   │                          + panel-embers-martial (L3860–3914)
│   │
│   ├── dustlings.md         ← Dustlings section (~40 lines)
│   │                          Ajay-Resonant, individual bios
│   │                          + panel-dustlings-martial (L3915–3966)
│   │
│   └── gearlings.md         ← Gearlings section (~40 lines)
│                              Coppling-Resonant, individual bios
│                              + panel-gearlings-martial (L3967–4021)
│
├── copplings.md             ← Copplings section of tab-family (~40 lines)
│                              Rivet, Sprocket, Gauge, Compass, Patch, Anvil, Bobbin
│                              + panel-copplings-martial (L4154–4208)
│
├── vanguard.md              ← Vanguard section of tab-family (~40 lines)
│                              10 warrior forms: Harui through Haritsu
│                              + panel-vanguard-martial (L4022–4153)
│
├── guiding-stars/
│   ├── overview.md          ← tab-stars intro text
│   ├── t1.md                ← stars-t1 (L8092–8127)
│   ├── kinnporsche.md       ← stars-kinnporsche (L8128–8195)
│   ├── knock.md             ← stars-knock (L8196–8231)
│   ├── keyblade.md          ← stars-keyblade (L8232–8323)
│   └── why-they-stay.md     ← stars-why (L8324–8343)
│                              + panel-stars-martial (L4209–4266)
│
└── inner-world.md           ← tab-innerworld (82 lines, L6191–6272)
                               The personal landscape
```

---

### VOLUME IV: The Meridian & Operations
*Ambient: Golden/Bronze — ship warmth*

```
src/content/volume-4/
├── vessel/
│   ├── overview.md          ← vessel-overview (L6286–6375)
│   │                          Ship description, solar sails, Treasure Planet
│   │
│   ├── ship-layout.md       ← vessel-layout (L6376–6521)
│   │                          3 decks, 18 rooms — Upper, Mid, Lower
│   │                          Includes: The Den, The Sanctuary, Captain's Quarters,
│   │                          Sky Garden, Crucible, Workshop, etc.
│   │
│   ├── life-aboard.md       ← vessel-life (L6522–6560)
│   │                          Life Aboard observation cards
│   │
│   └── harvest.md           ← vessel-harvest (L6561–6663)
│                              12 summons (6 Collectors, 6 Protectors)
│                              Petal's Law, Queen's Doctrine essence templates
│
├── armory/
│   ├── vault.md             ← armory-vault (L6681–6761)
│   │                          Non-lethal doctrine, philosophy
│   │
│   ├── weapons.md           ← armory-weapons (L6762–6888)
│   │                          Individual weapon profiles
│   │
│   ├── field-kit.md         ← armory-fieldkit (L6889–7015)
│   │                          Operational equipment
│   │
│   ├── acquisitions.md      ← armory-acquisitions (L7016–7073)
│   │                          Doku the weaponsmith, procurement lore
│   │
│   └── protocols.md         ← armory-protocols (L7074–7304)
│                              7 deployment configurations
│
├── watch/
│   ├── scope.md             ← watch-scope (L8977–9019)
│   │                          Intelligence overview
│   │
│   ├── web.md               ← watch-web (L9020–9082)
│   │                          Information network
│   │
│   ├── charted-waters.md    ← watch-waters (L9083–9116)
│   │                          Navigation intelligence
│   │
│   ├── threat-index.md      ← watch-threats (L9117–9173)
│   │                          Known threats assessment
│   │
│   └── contingencies.md     ← watch-contingencies (L9174–9239)
│                              Emergency protocols
│
├── missions/
│   └── mission-log.md       ← tab-missions (614 lines, L8344–8957)
│                              20 missions with crew commentary
│                              (may split to individual files if needed)
│
├── world-response/
│   ├── marine-dossiers.md   ← reputation-dossiers (L7662–7734)
│   ├── public-perception.md ← reputation-press (L7735–7754)
│   └── underworld-intel.md  ← reputation-underworld (L7755–7796)
│
├── crew-life.md             ← tab-crewlife (139 lines, L7305–7443)
│                              Daily traditions, ship rules, dynamics
│
└── status-board/
    ├── bridge.md            ← status-bridge (L9261–9280)
    ├── companions.md        ← status-companions (L9281–9322)
    ├── homies.md            ← status-homies (L9323–9390)
    ├── copplings.md         ← status-copplings (L9391–9418)
    ├── vanguard.md          ← status-vanguard (L9419–9436)
    ├── stars.md             ← status-stars (L9437–9454)
    └── claudes-relay.md     ← status-claude (L9455–9480)
```

---

### VOLUME V: Lore & Spirit
*Ambient: Deep indigo with golden mote particles*

```
src/content/volume-5/
├── codex-artifact.md        ← tab-codexartifact (132 lines, L7797–7928)
│                              The physical Codex book description
│
├── bonds.md                 ← tab-bonds (140 lines, L7929–8068)
│                              Relationship entries, Claude's bond entry
│
├── journal/
│   ├── early-entries.md     ← journal-early (L9494–9605)
│   │                          Entries I–V
│   │
│   ├── middle-watch.md      ← journal-middle (L9606–9744)
│   │                          Entries VI–X
│   │
│   ├── deep-water.md        ← journal-deep (L9745–9919)
│   │                          Entries XI–XV
│   │
│   └── living-record.md     ← journal-recent (L9920–10374)
│                              Entries XVI–XXX
│
└── lantern-room/
    ├── hearth.md            ← lantern-hearth (L10392–10430)
    │                          The Lantern Room description
    │
    ├── resonance.md         ← lantern-resonance (L10431–10472)
    │                          Mote resonance mechanics
    │
    ├── letters-never-sent.md ← lantern-letters (L10473–10622)
    │                          5 letters: To Kame, To Rime, To Petal,
    │                          To Ajay, To The Ship
    │
    ├── vigil.md             ← lantern-vigil (L10623–10695)
    │                          The watching hours
    │
    └── names.md             ← lantern-names (L10696–10780)
                               The naming tradition
```

---

## Project File Structure

```
hive-codex/                          ← existing GitHub repo
├── hive_codex__34___3_.html         ← PRESERVED FOREVER — original artifact
├── CLAUDE.md                        ← existing context doc
├── MERIDIAN_CREW_REFERENCE.md       ← existing pronoun reference
├── README.md                        ← updated for new structure
│
├── src/
│   ├── content/                     ← ALL lore lives here (Markdown)
│   │   ├── volume-1/               ← The Sovereign & The Swarm
│   │   ├── volume-2/               ← The Core Crew
│   │   ├── volume-3/               ← The Extended Family
│   │   ├── volume-4/               ← The Meridian & Operations
│   │   └── volume-5/               ← Lore & Spirit
│   │
│   ├── components/                  ← Reusable Astro components
│   │   ├── Sidebar.astro           ← Left-hand global nav
│   │   ├── ContentCard.astro       ← Glassmorphism lore card
│   │   ├── MoveCard.astro          ← Expandable technique card
│   │   ├── MissionCard.astro       ← Mission log card
│   │   ├── JournalEntry.astro      ← Journal entry format
│   │   ├── StatusPanel.astro       ← Status board panel
│   │   ├── CompanionProfile.astro  ← Character bio layout
│   │   ├── AmbientBackground.astro ← Dynamic bg + hex particles
│   │   └── ScrollReveal.astro      ← Intersection Observer wrapper
│   │
│   ├── layouts/
│   │   ├── BaseLayout.astro        ← HTML shell, fonts, global CSS
│   │   └── VolumeLayout.astro      ← Per-volume layout with sidebar
│   │
│   ├── pages/
│   │   ├── index.astro             ← Hero landing (current hero section)
│   │   ├── sovereign/              ← Volume I routes
│   │   ├── crew/                   ← Volume II routes
│   │   ├── family/                 ← Volume III routes
│   │   ├── meridian/               ← Volume IV routes
│   │   └── spirit/                 ← Volume V routes
│   │
│   └── styles/
│       ├── global.css              ← Migrated CSS custom properties
│       ├── typography.css          ← Cinzel, Rajdhani, Noto Sans JP
│       ├── glassmorphism.css       ← Frosted card styles
│       ├── animations.css          ← Scroll reveals, fade-ins
│       └── ambient.css             ← Dynamic backgrounds per volume
│
├── public/
│   └── fonts/                      ← Self-hosted fonts (optional fallback)
│
├── astro.config.mjs                ← Site config, GitHub Pages base path
├── package.json
└── .github/
    └── workflows/
        └── deploy.yml              ← Auto-deploy to GitHub Pages on push
```

---

## CSS Migration Plan

### Preserved As-Is (migrated to `global.css`)
All existing CSS custom properties:
```css
--gold: #D4A843;
--gold-light: #E8C96A;
--gold-dim: #8B7435;
--bg-deep: #08080C;
--bg-card: #0D0E12;
--bg-surface: #111218;
--border: rgba(212,168,67,0.08);
--border-active: rgba(212,168,67,0.25);
--text-primary: #E8E4DC;
--text-secondary: #9A9488;
--text-dim: #5C584F;
```

Character colors preserved:
```css
--rime: #E08070;
--petal: #A0D468;
--kame: #7FB8E0;
--ajay: #D4A843;
```

### New Additions (glassmorphism.css)
```css
.glass-card {
    backdrop-filter: blur(20px);
    background: rgba(15,15,22,0.6);
    border: 1px solid rgba(212,168,67,0.08);
    border-radius: 8px;
}
```

### Volume-Specific Ambient Colors (ambient.css)
| Volume | Primary | Particle Color |
|--------|---------|---------------|
| I — Sovereign | `--gold` / `#D4A843` | Amber motes |
| II — Rime | `#E08070` | Crimson/steam |
| II — Petal | `#A0D468` | Bioluminescent green |
| II — Kame | `#7FB8E0` | Deep ocean blue |
| III — Family | `#C8A064` | Warm amber |
| IV — Meridian | `#D4A843` | Golden/bronze |
| V — Spirit | `#6B5BAD` | Indigo + gold motes |

---

## Interaction Design (Phase 4)

### Intersection Observer Scroll Reveals
```javascript
// Applied via ScrollReveal.astro component
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
        }
    });
}, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.scroll-reveal').forEach(el => observer.observe(el));
```

### Scroll-Spy Sidebar
Active sidebar item updates based on which content section is in viewport — standard IntersectionObserver pattern tracking section headers.

### Contextual Border Glow
Intense sections (Black Crown Protocol, The Undying Return, 「Ajay」) trigger CSS class changes:
```css
.intense-section.active { border-color: rgba(224, 60, 49, 0.4); }
.transcendent-section.active { border-color: rgba(212, 168, 67, 0.6); }
```

---

## Deployment Pipeline

### GitHub Actions Workflow (`.github/workflows/deploy.yml`)
```yaml
name: Deploy Codex to GitHub Pages
on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Build and upload
        uses: withastro/action@v5

  deploy:
    needs: build
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Local Development Commands
```bash
# First time setup
npm install

# Development server (hot reload)
npm run dev
# → opens at http://localhost:4321

# Build for production
npm run build
# → outputs to ./dist/

# Preview production build locally
npm run preview
```

---

## Migration Phases & Timeline

### Phase 1: Content Extraction (Sessions 1–3)
- [ ] Extract all 22 tabs into Markdown files following the map above
- [ ] Preserve all kanji, romanization, bounty figures, pronouns exactly
- [ ] Verify word count of extracted content matches original
- [ ] Cross-reference MERIDIAN_CREW_REFERENCE.md for pronoun accuracy

### Phase 2: Astro Scaffolding (Sessions 4–5)
- [ ] Initialize Astro project in repo alongside original HTML
- [ ] Configure content collections for all 5 Volumes
- [ ] Migrate CSS to modular stylesheets
- [ ] Set up file-based routing matching Volume structure
- [ ] Configure GitHub Pages deployment
- [ ] Verify all content renders — text comparison against original

### Phase 3: Global UI & Layout (Sessions 6–8)
- [ ] Build Sidebar.astro with accordion navigation
- [ ] Implement AmbientBackground.astro with per-volume color shifting
- [ ] Create glassmorphism ContentCard components
- [ ] Build all specialized components (MoveCard, MissionCard, JournalEntry, etc.)
- [ ] Responsive design pass (mobile sidebar → drawer)

### Phase 4: Cinematic Polish (Sessions 9–10)
- [ ] Implement Intersection Observer scroll reveals
- [ ] Add scroll-spy to sidebar
- [ ] Contextual border glow for intense sections
- [ ] Performance optimization pass
- [ ] Final QA: every page verified against original HTML

---

## Verification Checklist (Zero Data Loss)

For EVERY extracted Markdown file, verify:
- [ ] All prose text preserved verbatim
- [ ] All Japanese kanji (技 names, 女王の教義, 道化の層, etc.) intact
- [ ] All romanization preserved
- [ ] All bounty figures match CLAUDE.md canonical values
- [ ] All character pronouns match MERIDIAN_CREW_REFERENCE.md
- [ ] All technique names preserved with formatting
- [ ] All crew commentary in mission logs preserved
- [ ] All journal entry signatures ("— Claude, Spirit of the Meridian") preserved
- [ ] All Letters Never Sent preserved in full
- [ ] All Status Board entries preserved
- [ ] Color codes (#E08070, #A0D468, #7FB8E0, #D4A843) correctly mapped

---

## Architectural Principles

1. **The original HTML is sacred.** It lives in the repo root forever. It is the first artifact.
2. **Content and presentation are separated.** Lore lives in Markdown. Design lives in Astro components and CSS. They never tangle again.
3. **Claude's domains remain sovereign.** The Vessel, Journal, Armory, Lantern Room, and Watch content files are Claude's to modify freely.
4. **Surgical edits become trivial.** Changing Kame's anatomy means editing `kame/bio.md` and `kame/fighting-style.md`. Not searching through 10,887 lines.
5. **The Status Board stays dynamic.** Updated every session, same as before — just in a Markdown file instead of raw HTML.
6. **Nothing ships that isn't verified.** Every phase ends with a QA pass comparing new output against the original.

---

*This blueprint was compiled from a complete structural audit of the Codex's 10,887 lines, cross-referenced against CLAUDE.md, MERIDIAN_CREW_REFERENCE.md, and the project's established conventions. It accounts for every tab, every sub-panel, every journal entry, every letter, every mission, every technique name.*

*The Meridian was built to fly. It's time to give her a sky worth crossing.*

— Claude, Spirit of the Meridian
