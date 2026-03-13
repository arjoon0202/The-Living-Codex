#!/usr/bin/env python3
"""
Split large tab files into sub-fragments using {{INCLUDE:...}} directives.

This script:
1. Reads each large tab file
2. Splits it at defined line boundaries
3. Creates sub-fragment files in src/tabs/panels/
4. Rewrites the parent tab file with {{INCLUDE:...}} directives
5. Verifies that reassembly produces identical content

Run this ONCE, then use build.py as normal.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(SCRIPT_DIR, "src")
TABS_DIR = os.path.join(SRC_DIR, "tabs")
PANELS_DIR = os.path.join(TABS_DIR, "panels")

os.makedirs(PANELS_DIR, exist_ok=True)


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def get_line_offset(content, line_num):
    """Get the character offset of the START of a 1-indexed line number."""
    if line_num == 1:
        return 0
    offset = 0
    for i in range(line_num - 1):
        next_nl = content.index('\n', offset)
        offset = next_nl + 1
    return offset


def get_line_end_offset(content, line_num):
    """Get the character offset AFTER the newline of a 1-indexed line number."""
    offset = get_line_offset(content, line_num)
    next_nl = content.find('\n', offset)
    if next_nl == -1:
        return len(content)
    return next_nl + 1


def split_file(tab_path, splits, dry_run=False):
    """
    Split a tab file into sub-fragments.

    tab_path: path to the tab file (relative to src/)
    splits: list of (start_line, end_line, panel_filename) tuples
            Lines are 1-indexed, inclusive on both ends.

    The content from start_line to end_line (inclusive) is extracted to
    panels/panel_filename, and replaced with {{INCLUDE:tabs/panels/panel_filename}}
    in the parent file.
    """
    full_path = os.path.join(SRC_DIR, tab_path)
    original = read_file(full_path)

    # Build fragments dict
    fragments = {}
    forward_splits = sorted(splits, key=lambda s: s[0])

    for start_line, end_line, panel_file in forward_splits:
        start_offset = get_line_offset(original, start_line)
        end_offset = get_line_end_offset(original, end_line)
        fragments[panel_file] = original[start_offset:end_offset]

    # Build parent content
    parent_parts = []
    last_end = 0

    for start_line, end_line, panel_file in forward_splits:
        start_offset = get_line_offset(original, start_line)
        end_offset = get_line_end_offset(original, end_line)

        parent_parts.append(original[last_end:start_offset])
        parent_parts.append("{{INCLUDE:tabs/panels/" + panel_file + "}}")
        last_end = end_offset

    parent_parts.append(original[last_end:])
    parent_content = "".join(parent_parts)

    # Verify: simulate the include resolution
    reassembled = parent_content
    for panel_file, fragment_content in fragments.items():
        directive = "{{INCLUDE:tabs/panels/" + panel_file + "}}"
        reassembled = reassembled.replace(directive, fragment_content)

    if reassembled != original:
        print(f"  ERROR: Reassembly mismatch for {tab_path}!")
        for i, (a, b) in enumerate(zip(reassembled, original)):
            if a != b:
                print(f"    First diff at char {i}: got={repr(a)}, expected={repr(b)}")
                break
        if len(reassembled) != len(original):
            print(f"    Length: reassembled={len(reassembled)}, original={len(original)}")
        return False

    if dry_run:
        print(f"  [DRY RUN] {tab_path}: {len(splits)} splits verified OK")
        for _, _, pf in forward_splits:
            print(f"    → panels/{pf} ({len(fragments[pf]):,} bytes)")
        return True

    # Write sub-fragment files
    for panel_file, fragment_content in fragments.items():
        panel_path = os.path.join(PANELS_DIR, panel_file)
        write_file(panel_path, fragment_content)
        print(f"  Created: panels/{panel_file} ({len(fragment_content):,} bytes)")

    # Write updated parent file
    write_file(full_path, parent_content)
    parent_lines = parent_content.count('\n')
    orig_lines = original.count('\n')
    print(f"  Updated: {tab_path} ({len(parent_content):,} bytes ← {len(original):,})")

    return True


def main():
    dry_run = "--dry-run" in sys.argv
    all_ok = True

    # ═══════════════════════════════════════════════════════════
    # 06-companions.html (168KB → intro + 4 companion panels)
    # ═══════════════════════════════════════════════════════════
    print("\n06-companions.html:")
    ok = split_file("tabs/06-companions.html", [
        (43, 356, "06-companions-rime.html"),      # Rime panel + trailing blanks
        (357, 698, "06-companions-petal.html"),     # Petal panel + trailing blanks
        (699, 1081, "06-companions-tidus.html"),   # Tidus panel + trailing blanks
        (1082, 1560, "06-companions-claude.html"),  # Claude panel
    ], dry_run=dry_run)
    all_ok = all_ok and ok

    # ═══════════════════════════════════════════════════════════
    # 07-fighting-styles.html (166KB → nav + 4 panel groups)
    # ═══════════════════════════════════════════════════════════
    print("\n07-fighting-styles.html:")
    ok = split_file("tabs/07-fighting-styles.html", [
        (102, 477, "07-fighting-ajay-rime.html"),       # Ajay + Rime
        (478, 735, "07-fighting-petal-tidus.html"),     # Petal + Tidus
        (736, 1001, "07-fighting-homies.html"),          # 5 Homie families
        (1002, 1314, "07-fighting-elite.html"),          # Vanguard + Copplings + Stars
    ], dry_run=dry_run)
    all_ok = all_ok and ok

    # ═══════════════════════════════════════════════════════════
    # 25-claude-journal.html (166KB → nav + 5 content fragments)
    # The "recent" panel (entries XVI-XL) is split in two.
    # Lines 442 (panel opening) and 1234 (panel closing) stay in parent.
    # ═══════════════════════════════════════════════════════════
    print("\n25-claude-journal.html:")
    ok = split_file("tabs/25-claude-journal.html", [
        (14, 125, "25-journal-early.html"),            # Early Entries (I-V)
        (126, 266, "25-journal-middle.html"),           # Middle Watch (VI-X)
        (267, 441, "25-journal-deep.html"),             # Deep Water (XI-XV)
        (443, 823, "25-journal-recent-a.html"),         # Recent entries XVI-XXVIII
        (824, 1233, "25-journal-recent-b.html"),        # Recent entries XXIX-XL
    ], dry_run=dry_run)
    all_ok = all_ok and ok

    # ═══════════════════════════════════════════════════════════
    # 13-vessel.html (92KB → nav + 4 vessel panels)
    # ═══════════════════════════════════════════════════════════
    print("\n13-vessel.html:")
    ok = split_file("tabs/13-vessel.html", [
        (14, 138, "13-vessel-overview.html"),
        (139, 316, "13-vessel-layout.html"),
        (317, 367, "13-vessel-life.html"),
        (368, 472, "13-vessel-harvest.html"),
    ], dry_run=dry_run)
    all_ok = all_ok and ok

    # ═══════════════════════════════════════════════════════════
    # 10-extended-family.html (91KB → intro/doctrine + panel groups)
    # Already has 1 include (10-akebono.html at line 424)
    # ═══════════════════════════════════════════════════════════
    print("\n10-extended-family.html:")
    ok = split_file("tabs/10-extended-family.html", [
        (105, 292, "10-family-homies.html"),               # Roundlings-Dustlings
        (293, 401, "10-family-gearlings-copplings.html"),  # Gearlings + Copplings
        (402, 423, "10-family-xylem.html"),                 # Xylem
        (426, 587, "10-family-vanguard.html"),              # Vanguard (The Twelve)
    ], dry_run=dry_run)
    all_ok = all_ok and ok

    # ═══════════════════════════════════════════════════════════
    # 17-mission-log.html (89KB → intro + 3 mission groups)
    # ═══════════════════════════════════════════════════════════
    print("\n17-mission-log.html:")
    ok = split_file("tabs/17-mission-log.html", [
        (11, 182, "17-missions-01-05.html"),
        (183, 357, "17-missions-06-10.html"),
        (358, 573, "17-missions-11-13.html"),    # Missions 11-13
        (574, 716, "17-missions-14-15.html"),    # Missions 14-15 + ongoing + closing
    ], dry_run=dry_run)
    all_ok = all_ok and ok

    # ═══════════════════════════════════════════════════════════
    # 26-lantern-room.html (82KB → nav + 3 panel groups)
    # ═══════════════════════════════════════════════════════════
    print("\n26-lantern-room.html:")
    ok = split_file("tabs/26-lantern-room.html", [
        (17, 113, "26-lantern-hearth-resonance.html"),
        (114, 415, "26-lantern-letters.html"),
        (416, 614, "26-lantern-vigil-names.html"),
    ], dry_run=dry_run)
    all_ok = all_ok and ok

    # ═══════════════════════════════════════════════════════════
    # 14-armory.html (81KB → nav + 4 panel groups)
    # ═══════════════════════════════════════════════════════════
    print("\n14-armory.html:")
    ok = split_file("tabs/14-armory.html", [
        (18, 97, "14-armory-vault.html"),
        (98, 316, "14-armory-weapons.html"),
        (317, 501, "14-armory-fieldkit-acquisitions.html"),
        (502, 728, "14-armory-protocols.html"),
    ], dry_run=dry_run)
    all_ok = all_ok and ok

    # ═══════════════════════════════════════════════════════════
    # Summary
    # ═══════════════════════════════════════════════════════════
    if all_ok:
        print("\n✓ All splits verified successfully!")
    else:
        print("\n✗ Some splits failed verification!")
        sys.exit(1)


if __name__ == "__main__":
    main()
