#!/usr/bin/env python3
"""
Build the Hive Codex from fragments.

Reads template.html, replaces {{PLACEHOLDER}} tokens with file contents,
then decodes {{IMG_*}} base64 images to separate files in dist/images/
and replaces placeholders with relative paths.

Outputs HTML to dist/hive_codex.html + dist/index.html, with images
in dist/images/. This keeps the HTML well under GitHub's 100 MB limit.

Zero external dependencies — Python 3 standard library only.
"""

import base64
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
DIST_IMAGES_DIR = os.path.join(DIST_DIR, "images")

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
    "TAB_27_AWAKENING":           "tabs/27-awakening.html",
    "TAB_28_INVESTIGATIONS":      "tabs/28-investigations.html",
    "TAB_29_TRAINING_LOG":        "tabs/29-training-log.html",
    "TAB_30_GLOSSARY":            "tabs/30-glossary.html",
    "MAIN_SCRIPTS":               "scripts/main.js",
}

# MIME type to file extension mapping
MIME_TO_EXT = {
    "png": "png",
    "jpeg": "jpg",
    "jpg": "jpg",
    "gif": "gif",
    "webp": "webp",
    "svg+xml": "svg",
}


def decode_b64_file(b64_path):
    """Read a .b64 file and return (raw_bytes, extension).

    Handles both formats:
    - Full data URI: data:image/png;base64,iVBOR...
    - Raw base64: iVBOR...
    """
    with open(b64_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if content.startswith("data:"):
        # Parse data URI: data:image/<type>;base64,<payload>
        match = re.match(r"data:image/([^;]+);base64,(.*)", content, re.DOTALL)
        if not match:
            print(f"ERROR: Could not parse data URI in {b64_path}")
            sys.exit(1)
        mime_sub = match.group(1)
        raw_b64 = match.group(2).strip()
        ext = MIME_TO_EXT.get(mime_sub, mime_sub)
    else:
        # Raw base64 — detect format from magic bytes
        raw_b64 = content
        if raw_b64.startswith("/9j/"):
            ext = "jpg"
        else:
            # Default to png (covers iVBOR... and others)
            ext = "png"

    img_bytes = base64.b64decode(raw_b64)
    return img_bytes, ext


def build(strict=False):
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

    # Resolve sub-includes: {{INCLUDE:relative/path.html}} within assembled content
    # This allows large tab files to split panels into separate sub-fragment files.
    # Paths are relative to the src/ directory.
    # Cycle detection: track visited paths per include chain; depth cap at 10.
    MAX_INCLUDE_DEPTH = 10
    include_pattern = re.compile(r"\{\{INCLUDE:([^}]+)\}\}")
    include_count = 0
    visited_paths = set()
    while True:
        match = include_pattern.search(html)
        if not match:
            break
        include_path = match.group(1).strip()
        full_path = os.path.join(SRC_DIR, include_path)
        canonical = os.path.realpath(full_path)
        if canonical in visited_paths:
            print(f"ERROR: Include cycle detected: {include_path} has already been included")
            print(f"  Include chain so far: {visited_paths}")
            sys.exit(1)
        if not os.path.exists(full_path):
            print(f"ERROR: Missing sub-include: {full_path}")
            sys.exit(1)
        visited_paths.add(canonical)
        include_count += 1
        if include_count > MAX_INCLUDE_DEPTH * len(visited_paths) + 200:
            print(f"ERROR: Include depth exceeded ({include_count} expansions, {len(visited_paths)} unique files)")
            sys.exit(1)
        with open(full_path, "r", encoding="utf-8") as f:
            include_content = f.read()
        html = html[:match.start()] + include_content + html[match.end():]
    if include_count:
        print(f"Resolved {include_count} sub-includes ({len(visited_paths)} unique files)")

    # Decode images to dist/images/ and replace placeholders with paths
    if os.path.exists(MANIFEST):
        with open(MANIFEST, "r", encoding="utf-8") as f:
            image_manifest = json.load(f)

        os.makedirs(DIST_IMAGES_DIR, exist_ok=True)

        img_count = 0
        total_img_bytes = 0
        for token, filepath in image_manifest.items():
            full_path = os.path.join(SRC_DIR, filepath)
            if not os.path.exists(full_path):
                print(f"ERROR: Missing image file: {full_path}")
                sys.exit(1)

            # Decode base64 to binary image file
            img_bytes, ext = decode_b64_file(full_path)

            # Output filename: token without IMG_ prefix, lowercased, with extension
            img_name = token.lower().replace("img_", "").replace("_", "-") + "." + ext
            img_out_path = os.path.join(DIST_IMAGES_DIR, img_name)

            with open(img_out_path, "wb") as f:
                f.write(img_bytes)

            total_img_bytes += len(img_bytes)

            # Replace placeholder in HTML with relative path
            placeholder = "{{" + token + "}}"
            relative_path = "images/" + img_name
            if placeholder in html:
                html = html.replace(placeholder, relative_path)
                img_count += 1
            else:
                msg = f"Image placeholder {placeholder} not found in assembled HTML"
                if strict:
                    print(f"ERROR (strict): {msg}")
                    sys.exit(1)
                else:
                    print(f"WARNING: {msg}")

        print(f"Decoded {img_count} images to dist/images/ ({total_img_bytes:,} bytes total)")

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
    print(f"HTML size: {os.path.getsize(output_path):,} bytes")

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

    # Size guard: warn if HTML exceeds 50 MB (should be ~7-8 MB without inline images)
    html_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    if html_size_mb > 50:
        print(f"WARNING: HTML is {html_size_mb:.1f} MB — images may still be inlined!")


if __name__ == "__main__":
    strict_mode = "--strict" in sys.argv
    if strict_mode:
        print("Running in strict mode")
    build(strict=strict_mode)
