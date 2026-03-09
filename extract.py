#!/usr/bin/env python3
"""
Extract fragments from the monolithic hive_codex__35_.html.

Strategy: Single pass through the file. Identify known structural regions
(style, sidebar, tabs, scripts) and replace each with a placeholder token
to produce the template. Extract the content of each region into its own file.

The build.py script reassembles these into an identical HTML file.
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MONOLITH = os.path.join(SCRIPT_DIR, "hive_codex__35_.html")
SRC_DIR = os.path.join(SCRIPT_DIR, "src")
TEMPLATE_PATH = os.path.join(SCRIPT_DIR, "template.html")

# Tab ID -> fragment filename. The order here doesn't matter for extraction
# (we discover order from the HTML), but it defines the file naming.
TAB_FILENAMES = {
    "overview":       "01-overview",
    "origin":         "02-origin",
    "bounty":         "03-bounty",
    "arsenal":        "04-arsenal",
    "martial":        "07-fighting-styles",
    "vulnerabilities":"05-vulnerabilities",
    "companions":     "06-companions",
    "family":         "10-extended-family",
    "innerworld":     "11-inner-world",
    "vessel":         "13-vessel",
    "armory":         "14-armory",
    "crewlife":       "15-crew-life",
    "synergy":        "08-combination-attacks",
    "auxiliary":      "09-auxiliary-protocols",
    "portraits":      "23-portraits",
    "transcendence":  "24-haki-transcendence",
    "reputation":     "16-world-response",
    "codexartifact":  "20-the-codex",
    "bonds":          "21-bonds",
    "stars":          "12-guiding-stars",
    "missions":       "17-mission-log",
    "watch":          "18-the-watch",
    "statusboard":    "19-status-board",
    "gallery":        "22-gallery",
    "journal":        "25-claude-journal",
    "lantern":        "26-lantern-room",
}


def placeholder_for_tab(tab_id):
    fname = TAB_FILENAMES[tab_id]
    return "TAB_" + fname.upper().replace("-", "_")


def find_closing_div(lines, start_idx):
    """
    Given the index of a line containing an opening <div>, track div depth
    to find the line containing its matching </div>.
    Returns the line index of the closing </div>.
    """
    depth = 0
    for j in range(start_idx, len(lines)):
        line = lines[j]
        opens = len(re.findall(r'<div[\s>]', line))
        closes = len(re.findall(r'</div>', line))
        depth += opens - closes
        if depth <= 0:
            return j
    raise ValueError(f"Could not find closing </div> for div starting at line {start_idx + 1}")


def extract():
    if not os.path.exists(MONOLITH):
        print(f"ERROR: Monolith not found: {MONOLITH}")
        sys.exit(1)

    with open(MONOLITH, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split('\n')
    total_lines = len(lines)
    print(f"Monolith: {total_lines} lines, {len(content):,} bytes")

    # Create output directories
    for d in ["head", "nav", "tabs", "scripts"]:
        os.makedirs(os.path.join(SRC_DIR, d), exist_ok=True)

    # === Identify all regions to extract ===
    # Each region: (start_line_idx, end_line_idx, type, identifier)
    # type: 'style', 'nav', 'tab', 'script'

    regions = []

    # Find <style> block (content only, between <style> and </style>)
    style_start = None
    style_end = None
    for i, line in enumerate(lines):
        if '<style>' in line and style_start is None:
            style_start = i
        if '</style>' in line and style_start is not None:
            style_end = i
            break

    if style_start is not None:
        # Extract CSS content (lines between <style> and </style>)
        css_lines = lines[style_start + 1:style_end]
        css_content = '\n'.join(css_lines)
        write_fragment("head/styles.css", css_content)
        regions.append((style_start + 1, style_end - 1, 'style_content'))

    # Find <head> content (meta tags, minus style block)
    head_start = None
    head_end = None
    for i, line in enumerate(lines):
        if '<head>' in line:
            head_start = i
        if '</head>' in line:
            head_end = i
            break

    meta_lines = lines[head_start + 1:style_start]
    meta_content = '\n'.join(meta_lines)
    write_fragment("head/meta.html", meta_content)

    # Find body start
    body_start = None
    for i, line in enumerate(lines):
        if '<body>' in line:
            body_start = i
            break

    # Find sidebar region: from after <body> to </aside>
    aside_end = None
    for i, line in enumerate(lines):
        if '</aside>' in line:
            aside_end = i
            break

    # Nav region: everything from body+1 to aside_end (inclusive)
    nav_lines = lines[body_start + 1:aside_end + 1]
    nav_content = '\n'.join(nav_lines)
    write_fragment("nav/sidebar.html", nav_content)

    # Find <script> block at end of document
    script_start = None
    script_end = None
    for i in range(len(lines) - 1, -1, -1):
        if '</script>' in lines[i] and script_end is None:
            script_end = i
        if '<script>' in lines[i] and script_end is not None:
            script_start = i
            break

    js_lines = lines[script_start + 1:script_end]
    js_content = '\n'.join(js_lines)
    write_fragment("scripts/main.js", js_content)

    # === Find all tab-content divs ===
    tab_pattern = re.compile(r'<div[^>]*class="tab-content[^"]*"[^>]*id="tab-([^"]+)"')
    tab_pattern2 = re.compile(r'<div[^>]*id="tab-([^"]+)"[^>]*class="tab-content[^"]*"')

    tab_regions = []  # (start, end, tab_id) in file order

    i = 0
    while i < len(lines):
        line = lines[i]
        m = tab_pattern.search(line) or tab_pattern2.search(line)
        if m:
            tab_id = m.group(1)
            end_idx = find_closing_div(lines, i)
            tab_regions.append((i, end_idx, tab_id))

            # Extract the tab content
            tab_lines = lines[i:end_idx + 1]
            tab_content = '\n'.join(tab_lines)
            fname = TAB_FILENAMES.get(tab_id)
            if fname:
                write_fragment(f"tabs/{fname}.html", tab_content)
            else:
                print(f"  WARNING: Unknown tab ID '{tab_id}', writing as tabs/{tab_id}.html")
                write_fragment(f"tabs/{tab_id}.html", tab_content)

            i = end_idx + 1
        else:
            i += 1

    print(f"\nExtracted {len(tab_regions)} tabs")

    # === Build template by replacing extracted content with placeholders ===
    # We rebuild the file line by line, replacing known regions with placeholders

    template_lines = []
    skip_until = -1

    for i in range(total_lines):
        if i <= skip_until:
            continue

        # Check if this line is the start of a known region

        # HEAD meta region: replace lines between <head> and <style> with placeholder
        if i == head_start + 1 and style_start is not None:
            template_lines.append("{{HEAD_META}}")
            skip_until = style_start - 1
            continue

        # Style content: replace lines between <style> and </style> with placeholder
        if i == style_start + 1:
            template_lines.append("{{HEAD_STYLES}}")
            skip_until = style_end - 1
            continue

        # Nav region: replace body+1 through aside_end with placeholder
        if i == body_start + 1:
            template_lines.append("{{SIDEBAR_NAV}}")
            skip_until = aside_end
            continue

        # Tab regions: replace each tab div block with placeholder
        tab_match = None
        for ts, te, tid in tab_regions:
            if i == ts:
                tab_match = (ts, te, tid)
                break

        if tab_match:
            ts, te, tid = tab_match
            fname = TAB_FILENAMES.get(tid, tid)
            pname = "TAB_" + fname.upper().replace("-", "_")
            template_lines.append("{{" + pname + "}}")
            skip_until = te
            continue

        # Script content: replace lines between <script> and </script> with placeholder
        if i == script_start + 1:
            template_lines.append("{{MAIN_SCRIPTS}}")
            skip_until = script_end - 1
            continue

        # Default: keep the line as-is
        template_lines.append(lines[i])

    template_content = '\n'.join(template_lines)
    with open(TEMPLATE_PATH, "w", encoding="utf-8") as f:
        f.write(template_content)
    print(f"\n  Wrote: template.html ({os.path.getsize(TEMPLATE_PATH):,} bytes)")

    print(f"\nExtraction complete!")
    print(f"  Template: {TEMPLATE_PATH}")
    print(f"  Fragments: {SRC_DIR}/")


def write_fragment(rel_path, content):
    full_path = os.path.join(SRC_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    size = os.path.getsize(full_path)
    print(f"  Wrote: src/{rel_path} ({size:,} bytes)")


if __name__ == "__main__":
    extract()
