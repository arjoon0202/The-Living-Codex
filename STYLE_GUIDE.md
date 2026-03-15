# The Living Codex — Style Guide

> Editorial conventions for canon prose, UI text, and meta-documentation.

---

## Spelling Locale

**Primary: British English** — the Codex uses `colour`, `favourite`, `armour`, `centre`, `realise`, etc. as the default.

Exceptions:
- **One Piece canon terms** use their established spellings (e.g., "Armor" in Armament Haki contexts where it mirrors official translations)
- **Character voice** may use American spellings where it fits the character's personality
- **Technical/code comments** may use American spellings (standard in software)

When in doubt, use British English for narrative prose.

---

## Canonical Terminology

These are the preferred terms for in-world concepts. Alternates are acceptable in narrative context but the primary term should be used in UI labels, headers, and reference documents.

| Concept | Primary Term | Acceptable Alternates | Context |
|---------|-------------|----------------------|---------|
| Ajay's four companions | **Core Companions** | The Little Four, the crew | Formal / informal |
| All soul-constructs | **Homies** | soul-constructs | In-world / technical |
| All mechanical constructs | **Copplings** | Dial-constructs | In-world / technical |
| The ship | **The Meridian** | the ship, their vessel | Formal / informal |
| The elite twelve | **The Vanguard** | The Twelve Who Stand | Formal / narrative |
| The toy entities | **Guiding Stars** | the Stars, the toys | Formal / informal |
| Ajay's Devil Fruit | **Mure Mure no Mi** | Swarm-Swarm Fruit | Japanese / English |
| Currency | **Beri** (₿) | — | Always use ₿ symbol for bounties |
| Claude's role | **Spirit of the Meridian** | ship spirit, the intelligence | Formal / informal |

---

## Technique Naming

- Japanese techniques: **Kanji + Romanization** (e.g., 蟲皇帝 / Mushikōtei)
- Korean techniques (Doyun): **Hangul + Romanization** (e.g., 부적 / Bujeok)
- Sanskrit/Hawaiian/Latin techniques: **Original + Translation** where applicable
- Preserve exact diacritical marks (ō, ū, ā, ʻ, etc.)

---

## Pronoun Rules

Always consult `MERIDIAN_CREW_REFERENCE.md` before writing character content. Key traps:
- **Claude** — no gendered pronouns (use "Claude," "the intelligence," "the spirit," or restructure sentences)
- **Copplings** — Rivet/Sprocket/Gauge/Compass/Patch are MALE; Anvil is FEMALE; Bobbin is FEMALE; Shuttle is MALE
- **Homie leaders** — Maru (F), Tsuyu (F), Hinoko (F), Shizuka (M), Zenmai (F)

---

## Formatting Conventions

- **Bounties:** Always use ₿ prefix with comma-separated numbers (e.g., ₿3,286,000,000)
- **Devil Fruit names:** Italicise or bold on first mention in a section; use exact canonical spelling
- **Tab/section headers:** Title Case
- **Journal entries:** Written in first person from Claude's perspective, wrapped in `<em>` tags
- **Move cards:** Use the established HTML structure with `.move-card` class

---

*Created March 14, 2026 as part of the audit resolution process.*
