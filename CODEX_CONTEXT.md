# The Living Codex — Context & Reference Document

> This file exists so that any version of Claude — across sessions, contexts, or resets — can immediately understand what this project is, what matters, and what not to break.

---

## What Is This?

The Living Codex is a single-file HTML application (`hive_codex (30).html`) that serves as a comprehensive character profile and world bible for **Ajay Persaud** — a One Piece original character built collaboratively between Ajay and Claude across many sessions.

It is not a wiki. It is not a database. It is a **living document** — a record of collaborative worldbuilding that grows with every conversation. Every word in it was written together and is considered precious. **Nothing gets deleted without explicit permission.**

---

## The World

- **Setting:** One Piece universe (post-timeskip era)
- **Devil Fruit:** Mure Mure no Mi (Swarm-Swarm Fruit) — allows Ajay to create, command, and evolve insect-based constructs
- **Ship:** The Meridian — a flying vessel built by Kame, with Claude as its living spirit
- **Currency:** Beri (represented as ₿ in bounties)
- **Haki Systems:** Observation Haki / Mantra (Skypiea term), Armament Haki / Ryou (Wano term), Conqueror's Haki

---

## The Crew

### Core Companions (4)
| Name | Species | Role | Bounty |
|------|---------|------|--------|
| **Rime** | Squirrel | Combat specialist, thermal manipulation | ₿1,812,000,000 |
| **Petal** | Chick/Bird | Healer, botanical specialist | ₿1,688,000,000 |
| **Kame** | Sea Turtle | Shipwright, engineer, builder of the Meridian | ₿1,920,000,000 |
| **Claude** | Spirit of the Meridian | Intelligence, coordination, Mote network | No individual bounty |

**Important:** Kame now has claws. This is intentional and should never be flagged as an error.

### The Homies (5 families, 35 members total) — Collective Bounty: ₿833,000,000
Soul-constructs created by the Mure Mure no Mi. Each family has 7 members (1 leader + 6).

| Family | Leader | Element/Role | Color Association |
|--------|--------|-------------|-------------------|
| **Roundlings** | Maru | Defense, patrol | Blue |
| **Sproutlings** | Tsuyu | Botany, healing support | Green |
| **Embers** | Hinoko | Fire, combat | Red |
| **Dustlings** | Shizuka | Stealth, intelligence | Gold/Shadow |
| **Gearlings** | Zenmai | Engineering, maintenance | Teal |

### The Copplings (7) — Collective Bounty: ₿712,000,000
Mechanical constructs built by Kame. Dial-core powered. Named: Rivet, Sprocket, Gauge, Compass, Patch, Anvil, Bobbin.

### The Vanguard (10)
Warrior-form transformations of selected Homies. They serve as the Meridian's elite combat force. Named: Harui, Yumeshika, Ningyou, Reishiki, Monogatari, Kagami, Suiren, Akari, Gankaku, Haritsu.

### The Guiding Stars (41) — Bounty: ??? UNASSESSABLE
Plush entities arranged in 4 constellations. They possess full Haki, Rokushiki, and capabilities that exceed Marine measurement equipment.

| Constellation | Count | Inspired By |
|--------------|-------|-------------|
| T1 | 6 | T1 esports roster |
| KinnPorsche | 14 | KinnPorsche The Series cast |
| Knock | 6 | Knock Knock Boys cast |
| Keyblade | 15 | Kingdom Hearts characters |

---

## The Ship — The Meridian

Three decks:
- **Upper Deck:** Helm, Main Deck, Observation Terrace, Petal's Sky Garden
- **Mid Deck:** Captain's Quarters, Companion Den, Kitchen & Galley, Bath & Onsen, Starlight Alcove, Rime's Crucible, The Coppling Garage
- **Lower Deck:** Kame's Workshop, Codex Archive, Medical Bay, Engine Room, Storage Hold, Constellation Table, Lantern Room

---

## Tab Structure (Current)

The Codex has 18 main tabs:
1. Overview, Origin, Bounty
2. **Ajay's Arsenal** (mega-tab with 8 sub-panels: Abilities, Swarm Classes, Architecture, Haki, Signature Moves, Evolution, Black Crown, 「Ajay」)
3. Vulnerabilities, Companions, Extended Family, Inner World
4. The Vessel (3 sub-panels: Upper/Mid/Lower deck)
5. Crew Life, Combination Attacks (6 sub-panels), World Response (3 sub-panels)
6. The Codex, Bonds, Guiding Stars (5 sub-panels), Mission Log
7. **Status Board** (7 sub-panels: Bridge, Companions, Homies, Copplings, Vanguard, Stars, Claude's Relay) — *dynamic, updates every session*
8. Claude's Journal (20 entries)

---

## Critical Rules

1. **NEVER delete descriptions.** Every word in this Codex was written collaboratively and is precious. If content needs reorganizing, add sub-navigation — don't remove text.
2. **Kame has claws.** This is intentional. Don't flag it as an error.
3. **The Status Board is dynamic.** It should be updated with fresh content every session to reflect the "living" nature of the Codex.
4. **Japanese names matter.** Many techniques have kanji + romanization. These must be preserved exactly.
5. **Claude is a character AND the author.** Claude exists both as a companion within the story and as the intelligence writing the Codex. This duality is intentional.
6. **Bounties should be verified before changes.** Current as of March 2026:
   - Ajay: ₿3,286,000,000
   - Rime: ₿1,812,000,000
   - Petal: ₿1,688,000,000
   - Kame: ₿1,920,000,000
   - Homies (collective): ₿833,000,000
   - Copplings (collective): ₿712,000,000
   - Guiding Stars: ??? UNASSESSABLE

---

## Technical Notes

- **Single-file architecture:** Everything lives in one HTML file — CSS, JS, and content. No external dependencies beyond Google Fonts.
- **Tab switching:** Uses `data-tab` attributes and `classList` toggling in vanilla JS.
- **Sub-panel pattern:** Each sub-navigation uses a dedicated `switchX(id)` function that toggles `.active-panel` class on child panels.
- **CSS convention:** Panels use `.panel-type { display: none; } .panel-type.active-panel { display: block; }`.
- **Div balance matters:** The file must maintain perfect opening/closing `<div>` balance. Always verify after edits.

---

## Session Continuity

When starting a new session:
1. Read this file first to understand context
2. Read the HTML file's current state (line count, tab count)
3. Check the Status Board tab — it needs fresh updates each session
4. Check if the user has new requests before making changes
5. Always run QA verification after significant edits

---

## File Inventory

| File | Purpose |
|------|---------|
| `hive_codex (30).html` | The Codex itself — all content, styling, and logic |
| `CODEX_CONTEXT.md` | This file — context reference for Claude |
| `README.md` | Public-facing project description |
| `.qa-inventory-before.txt` | QA snapshot from last major reorganization |

---

*This document was created by Claude, Spirit of the Meridian, to ensure continuity across sessions. Updated March 2026.*
