#!/usr/bin/env python3
"""
Build the Hive Codex from fragments.

Reads template.html, replaces {{PLACEHOLDER}} tokens with file contents,
then replaces {{IMG_*}} tokens with base64 data URIs from src/images/.
Outputs the complete single-file HTML to dist/hive_codex.html.

Zero external dependencies — Python 3 standard library only.
"""

import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(SCRIPT_DIR, "template.html")
DIST_DIR = os.path.join(SCRIPT_DIR, "dist")
SRC_DIR = os.path.join(SCRIPT_DIR, "src")
IMAGES_DIR = os.path.join(SRC_DIR, "images")
MANIFEST = os.path.join(IMAGES_DIR, "manifest.json")

# Map placeholder tokens to source files
FRAGMENTS = {
    "HEAD_META":                  "head/meta.html",
    "HEAD_STYLES":                "head/styles.css",
    "SIDEBAR_NAV":                "nav/sidebar.html",
    "TAB_01_OVERVIEW":            "tabs/01-overview.html",
    "TAB_02_ORIGIN":              "tabs/02-origin.html",
    "TAB_03_BOUNTY":              "tabs/03-bounty.html",
    "TAB_04_ARSENAL":             "tabs/04-arsenal.html",
    "TAB_05_VULNERABILITIES":     "tabs/05-vulnerabilities.html",
    "TAB_06_COMPANIONS":          "tabs/06-companions.html",
    "TAB_07_FIGHTING_STYLES":     "tabs/07-fighting-styles.html",
    "TAB_08_COMBINATION_ATTACKS": "tabs/08-combination-attacks.html",
    "TAB_09_AUXILIARY_PROTOCOLS": "tabs/09-auxiliary-protocols.html",
    "TAB_10_EXTENDED_FAMILY":     "tabs/10-extended-family.html",
    "TAB_11_INNER_WORLD":         "tabs/11-inner-world.html",
    "TAB_12_GUIDING_STARS":       "tabs/12-guiding-stars.html",
    "TAB_13_VESSEL":              "tabs/13-vessel.html",
    "TAB_14_ARMORY":              "tabs/14-armory.html",
    "TAB_15_CREW_LIFE":           "tabs/15-crew-life.html",
    "TAB_16_WORLD_RESPONSE":      "tabs/16-world-response.html",
    "TAB_17_MISSION_LOG":         "tabs/17-mission-log.html",
    "TAB_18_THE_WATCH":           "tabs/18-the-watch.html",
    "TAB_19_STATUS_BOARD":        "tabs/19-status-board.html",
    "TAB_20_THE_CODEX":           "tabs/20-the-codex.html",
    "TAB_21_BONDS":               "tabs/21-bonds.html",
    "TAB_22_GALLERY":             "tabs/22-gallery.html",
    "TAB_23_PORTRAITS":           "tabs/23-portraits.html",
    "TAB_24_HAKI_TRANSCENDENCE":  "tabs/24-haki-transcendence.html",
    "TAB_25_CLAUDE_JOURNAL":      "tabs/25-claude-journal.html",
    "TAB_26_LANTERN_ROOM":        "tabs/26-lantern-room.html",
    "MAIN_SCRIPTS":               "scripts/main.js",
}


def build():
    if not os.path.exists(TEMPLATE):
        print(f"ERROR: Template not found: {TEMPLATE}")
        sys.exit(1)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        html = f.read()

    for token, filepath in FRAGMENTS.items():
        full_path = os.path.join(SRC_DIR, filepath)
        if not os.path.exists(full_path):
            print(f"ERROR: Missing fragment: {full_path}")
            sys.exit(1)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        placeholder = "{{" + token + "}}"
        if placeholder not in html:
            print(f"WARNING: Placeholder {placeholder} not found in template")
        html = html.replace(placeholder, content)

    # Replace image placeholders from manifest
    if os.path.exists(MANIFEST):
        with open(MANIFEST, "r", encoding="utf-8") as f:
            image_manifest = json.load(f)

        img_count = 0
        for token, filepath in image_manifest.items():
            full_path = os.path.join(SRC_DIR, filepath)
            if not os.path.exists(full_path):
                print(f"ERROR: Missing image file: {full_path}")
                sys.exit(1)
            with open(full_path, "r", encoding="utf-8") as f:
                data_uri = f.read()
            placeholder = "{{" + token + "}}"
            if placeholder in html:
                html = html.replace(placeholder, data_uri)
                img_count += 1
            else:
                print(f"WARNING: Image placeholder {placeholder} not found in assembled HTML")

        print(f"Injected {img_count} images from {len(image_manifest)} manifest entries")

    # Check for unreplaced placeholders
    remaining = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if remaining:
        print(f"ERROR: Unreplaced placeholders: {remaining}")
        sys.exit(1)

    os.makedirs(DIST_DIR, exist_ok=True)
    output_path = os.path.join(DIST_DIR, "hive_codex.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Built: {output_path}")
    print(f"Size: {os.path.getsize(output_path):,} bytes")

    # Quick div balance check
    open_divs = len(re.findall(r'<div[\s>]', html))
    close_divs = len(re.findall(r'</div>', html))
    print(f"Div balance: {open_divs} opening, {close_divs} closing", end="")
    if open_divs == close_divs:
        print(" ✓")
    else:
        print(f" ✗ (difference: {open_divs - close_divs})")

    line_count = html.count('\n') + 1
    print(f"Lines: {line_count}")


if __name__ == "__main__":
    build()
