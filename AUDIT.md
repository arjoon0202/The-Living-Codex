# The Living Codex — Comprehensive Audit Report

## Executive Summary

This audit reviewed lore consistency, aesthetic consistency, grammar/style consistency, general documentation consistency, and code/tooling integrity across the repository.

Overall status: **Strong creative quality, but medium operational inconsistency risk**.

Key outcomes:
- The core codex source (`src/`) is mostly coherent and compiles successfully.
- There are **high-value consistency drifts** between canonical reference documents and active source files.
- Build/tooling scripts include **stale assumptions** that can silently preserve drift.
- Writing quality is generally high, but style conventions (US/UK spellings) are mixed in canon-facing text.

---

## Scope and Methodology

### Files reviewed
- Core project docs: `README.md`, `CLAUDE.md`, `CLAUDE_ADDITIONS.md`, `MERIDIAN_CREW_REFERENCE.md`, `CODEX_CONTENT_REFERENCE.md`
- Build/extract tooling: `build.py`, `extract.py`, `split_tabs.py`, `extract_images.py`
- Source app structure: `template.html`, `src/nav/sidebar.html`, `src/tabs/`, `src/tabs/panels/`, `src/images/manifest.json`
- Retcon project plans: `retcon_phases/*.md`

### Validation commands run
- Structural and inventory checks (`find`, `wc -l`, `rg`, manifest counts)
- Build integrity check (`python build.py`)
- Placeholder resolution check (`{{TOKEN}}` scan in built HTML)
- Navigation/tab consistency checks (regex-based extraction)
- Language-style consistency sampling (US/UK spelling distribution)
- Legacy term sweeps (Tethys/Drizzle/Pebble/etc.)

---

## Findings and Recommendations

## 1) Lore Consistency Findings

### 1.1 Legacy name leak in active source (High)
**Finding:** One active panel still refers to **Tethys** instead of **Tidus** in current in-world narration.

- File: `src/tabs/panels/28-investigation5-descent.html` (line containing “Tethys built it to conquer the sky…”).

**Why this matters:** This is a direct canon identity conflict in user-facing content.

**Recommendation:** Replace all three “Tethys” references in that paragraph with “Tidus,” then run a targeted lore-name regression sweep (`rg -n "\bTethys\b|\bDrizzle\b|\bPebble\b|\bMilio\b" src`).

---

### 1.2 Canon mirror drift in `CODEX_CONTENT_REFERENCE.md` (High)
**Finding:** The mirror document includes stale/contradictory phrasing not present in active source (e.g., “most loved crab in the world,” “The crab in him remembers the sea,” and crab-movement framing while species is now bear-otter).

**Why this matters:** This file is used as AI/session context. Drift here can re-inject retconned lore into future writing.

**Recommendation:** Regenerate `CODEX_CONTENT_REFERENCE.md` from the current built source, then run a post-regeneration diff focused on species/name terms.

---

### 1.3 Context guide chronology vs canon framing in `CLAUDE.md` (Medium)
**Finding:** `CLAUDE.md` contains current-context sections and historical logs interleaved; several top-level statements still present old-name framing (“built by Tethys,” old panel naming references).

**Why this matters:** Session continuity docs should not require readers (or AI) to infer whether a statement is historical vs canonical-now.

**Recommendation:** Split `CLAUDE.md` into:
1) **Canonical Now** (authoritative)
2) **Historical Changelog** (archive-only)

Add a banner at historical sections: “Historical entries may contain superseded terminology.”

---

## 2) Aesthetic and UX Consistency Findings

### 2.1 Sidebar volume ordering labels are semantically out-of-order in comments (Low)
**Finding:** In `src/nav/sidebar.html`, comments place “Volume VI” before “Volume V” even though UI remains readable.

**Why this matters:** Not user-breaking, but this increases editing friction and risk during future nav edits.

**Recommendation:** Align comment labels/order to rendered order (I → VI), or remove ordinal labels in comments entirely.

---

### 2.2 Feature metrics in `README.md` are partially stale relative to current build output (Medium)
**Finding:** README build-size expectation (~1.5 MB HTML) diverges from observed build output (~2.6 MB). Build currently decodes 50 images while repository has 56 `.b64` files.

**Why this matters:** New contributors may assume regressions where there are none—or miss real regressions because baseline docs are outdated.

**Recommendation:** Update README with measured ranges and split metrics:
- “source images present”
- “manifest entries”
- “images referenced by active templates”

---

## 3) Grammar and Style Consistency Findings

### 3.1 Mixed locale spelling conventions in canon text (Medium)
**Finding:** `CODEX_CONTENT_REFERENCE.md` mixes US/UK spellings (e.g., favourite/favorite, colour/color, armour/armor, centre/center, realise/realize).

**Why this matters:** The writing voice is strong, but mixed spelling conventions can feel unintentional and reduce editorial cohesion.

**Recommendation:** Pick a primary style guide (US or UK) for canon prose. Keep deliberate character-voice exceptions only where explicitly intended.

---

### 3.2 Terminology style drift between docs and implementation terms (Low)
**Finding:** Docs interchange “Core Companions,” “Core Crew,” “companions,” and “Little Four” without a single editorial style rule.

**Why this matters:** Not incorrect, but editorial inconsistency can become lore ambiguity over time.

**Recommendation:** Add a mini style sheet (`STYLE_GUIDE.md`) with preferred canonical terms and approved alternates by context (narrative/UI/meta-doc).

---

## 4) General Documentation Consistency Findings

### 4.1 Retcon phase checklists remain largely open despite integrated content (Medium)
**Finding:** `retcon_phases/` documents retain many unchecked items, including QA gates, while the main codex appears advanced beyond those states.

**Why this matters:** Contributors cannot reliably infer completion state; this can trigger duplicate or contradictory edits.

**Recommendation:** Mark each phase doc with one status stamp at top:
- `Status: Archived` / `Status: In Progress` / `Status: Superseded`

For archived phases, freeze checklist and link to a final completion summary.

---

### 4.2 Single source-of-truth boundaries are not explicit enough (Medium)
**Finding:** `MERIDIAN_CREW_REFERENCE.md`, `CLAUDE.md`, and `CODEX_CONTENT_REFERENCE.md` all function as “authoritative” in different ways, but hierarchy is implicit.

**Why this matters:** Conflicts are inevitable without an explicit precedence rule.

**Recommendation:** Add a short “Canonical Precedence” section to README:
1) `src/` built output
2) crew reference (pronouns/gender)
3) context docs (session continuity)
4) historical phase docs

---

## 5) Code and Tooling Audit Findings

### 5.1 Build warnings are non-failing for potentially stale image manifest entries (Medium)
**Finding:** `python build.py` warns when image placeholders are not found in assembled HTML but still exits successfully.

Observed warnings included unused `IMG_EXTENDED_FAMILY_*` tokens.

**Why this matters:** Silent drift accumulates in manifests and image assets; dead assets increase maintenance cost.

**Recommendation:** Add a strict mode (default on in CI) that fails when:
- manifest tokens are unused, or
- placeholder tokens in source are missing from manifest.

---

### 5.2 `extract.py` tab map is stale vs current 29-tab architecture (High)
**Finding:** `extract.py` `TAB_FILENAMES` mapping does not include all current tabs (notably later additions such as awakening/investigations/training), indicating extraction assumptions lag behind current project structure.

**Why this matters:** Any future “re-extract from monolith” operation risks incomplete or misnamed outputs.

**Recommendation:** Update `TAB_FILENAMES` to full current set and add a validation step that asserts parity with actual discovered `tab-*` ids.

---

### 5.3 `split_tabs.py` split definitions appear tied to older line boundaries and file naming assumptions (High)
**Finding:** The script references older panel segmentation assumptions (including older mission ranges and companion panel naming) that may not match current files.

**Why this matters:** Running this utility in its current state can produce accidental structural corruption or stale panelization.

**Recommendation:**
- Convert split config to marker-based boundaries (HTML comments) rather than hardcoded line numbers.
- Add dry-run CI check that verifies exact round-trip equivalence against current tabs.

---

### 5.4 Minor robustness opportunities in `build.py` include resolution (Low)
**Finding:** Include expansion uses repeated first-match replacement loop with no recursion guard/cycle detection.

**Why this matters:** Today it works; future accidental cyclic includes could cause non-obvious behavior.

**Recommendation:** Add:
- include-depth cap,
- visited-path stack for cycle detection,
- clearer error message with include chain.

---

## Prioritized Correction Plan

### Immediate (P0)
1. Fix active `Tethys` leak in `src/tabs/panels/28-investigation5-descent.html`.
2. Regenerate `CODEX_CONTENT_REFERENCE.md` from current canonical source.
3. Update `extract.py` and `split_tabs.py` to match current architecture before anyone uses them again.

### Near-term (P1)
4. Add build strict mode for image/token drift.
5. Clarify canonical precedence and status labels across docs.
6. Normalize spelling/style policy and enforce with lightweight linting.

### Quality hardening (P2)
7. Modernize script validation and round-trip checks.
8. Clean stale phase checklists by archiving or explicitly superseding.

---

## Suggested Guardrails (Non-invasive)

- Add `scripts/audit_consistency.py` for automated sweeps:
  - legacy names/species regex checks,
  - pronoun trap checks,
  - manifest↔placeholder parity,
  - tab-id↔sidebar `data-tab` parity.
- Add CI job: `python build.py --strict` + consistency audit script.
- Add `STYLE_GUIDE.md` with canonical terminology + locale spelling decision.

---

## Final Assessment

The codex’s creative and structural foundation is excellent. Most issues are **consistency drift between highly active lore and supporting maintenance docs/tools**, not core content quality failures. Addressing the P0/P1 items above will significantly reduce regression risk and protect canon fidelity as the project scales.
