#!/usr/bin/env python3
"""
OBSIDIAN // AETHER — Instant Multi-Theme Switcher & Automated Daily Rotator
Engineered for Deep Radadiya's Minimalist GitHub Profile Repository.

Usage:
    python switch_theme.py <theme_name | rotate>

Available commands:
    teal    : Quantum Teal (Cyber-minimalist default)
    violet  : Electric Violet (Sophisticated architectural style)
    emerald : Emerald Matrix (Core developer terminal aesthetic)
    gold    : Minimal Gold (Timeless monochrome & luxury finish)
    rotate  : Automatically selects today's scheduled rotating palette!
"""

import sys
import os
import glob
import datetime

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

THEMES = {
    "teal": {
        "name": "Quantum Teal [TEAL]",
        "primary": "#00F0FF",
        "secondary": "#00A3FF",
        "status": "#00FFA3",
        "readme_theme": "tokyonight",
        "graph_line": "00F0FF",
        "graph_point": "00FFA3",
        "badge_color": "00F0FF"
    },
    "violet": {
        "name": "Electric Violet [VIOLET]",
        "primary": "#A78BFA",
        "secondary": "#8B5CF6",
        "status": "#34D399",
        "readme_theme": "radical",
        "graph_line": "A78BFA",
        "graph_point": "F472B6",
        "badge_color": "A78BFA"
    },
    "emerald": {
        "name": "Emerald Matrix [EMERALD]",
        "primary": "#10B981",
        "secondary": "#059669",
        "status": "#22C55E",
        "readme_theme": "merko",
        "graph_line": "10B981",
        "graph_point": "34D399",
        "badge_color": "10B981"
    },
    "gold": {
        "name": "Minimal Gold [GOLD]",
        "primary": "#FACC15",
        "secondary": "#EAB308",
        "status": "#38BDF8",
        "readme_theme": "vision-friendly-dark",
        "graph_line": "FACC15",
        "graph_point": "F97316",
        "badge_color": "FACC15"
    }
}

def get_all_target_files(root_dir):
    svg_files = glob.glob(os.path.join(root_dir, "assets", "**", "*.svg"), recursive=True)
    readme_path = os.path.join(root_dir, "README.md")
    files = svg_files
    if os.path.exists(readme_path):
        files.append(readme_path)
    return files

def switch_theme(target_theme_key):
    # Handle automated schedule rotation mode for GitHub Actions CI/CD
    if target_theme_key in ["rotate", "auto"]:
        theme_keys = list(THEMES.keys())
        # Cycle systematically based on the day of the year
        day_index = datetime.datetime.now().toordinal() % len(theme_keys)
        target_theme_key = theme_keys[day_index]
        print(f"[AUTOMATED ROTATOR] Today's calendar rotation index chose theme: '{target_theme_key}'.")

    if target_theme_key not in THEMES:
        print(f"[ERROR] Unknown theme '{target_theme_key}'.")
        print(f"--> Available choices: {', '.join(list(THEMES.keys()) + ['rotate', 'auto'])}")
        sys.exit(1)

    target_theme = THEMES[target_theme_key]
    root_dir = os.path.dirname(os.path.abspath(__file__))
    files = get_all_target_files(root_dir)

    print(f"[THEME SHIFT] Transforming profile aesthetics to: {target_theme['name']} ...")

    # Step 1: Gather all known values across all themes to map to generic tokens
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Phase 1: Convert known theme hexes and parameters to tokens
        for t_key, t_val in THEMES.items():
            content = content.replace(t_val["primary"], "__TOKEN_PRIMARY__")
            content = content.replace(t_val["secondary"], "__TOKEN_SECONDARY__")
            content = content.replace(t_val["status"], "__TOKEN_STATUS__")
            
            content = content.replace(t_val["primary"].lstrip("#"), "__TOKEN_RAW_PRIMARY__")
            content = content.replace(t_val["secondary"].lstrip("#"), "__TOKEN_RAW_SECONDARY__")
            content = content.replace(t_val["status"].lstrip("#"), "__TOKEN_RAW_STATUS__")
            
            content = content.replace(f"theme={t_val['readme_theme']}", "theme=__TOKEN_README_THEME__")
            content = content.replace(f"color={t_val['graph_line']}&line={t_val['graph_line']}", "color=__TOKEN_LINE__&line=__TOKEN_LINE__")
            content = content.replace(f"point={t_val['graph_point']}", "point=__TOKEN_POINT__")
            content = content.replace(f"logoColor={t_val['badge_color']}", "logoColor=__TOKEN_BADGE_COLOR__")

        # Phase 2: Substitute tokens with the newly targeted theme values
        content = content.replace("__TOKEN_PRIMARY__", target_theme["primary"])
        content = content.replace("__TOKEN_SECONDARY__", target_theme["secondary"])
        content = content.replace("__TOKEN_STATUS__", target_theme["status"])
        
        content = content.replace("__TOKEN_RAW_PRIMARY__", target_theme["primary"].lstrip("#"))
        content = content.replace("__TOKEN_RAW_SECONDARY__", target_theme["secondary"].lstrip("#"))
        content = content.replace("__TOKEN_RAW_STATUS__", target_theme["status"].lstrip("#"))

        content = content.replace("__TOKEN_README_THEME__", target_theme["readme_theme"])
        content = content.replace("__TOKEN_LINE__", target_theme["graph_line"])
        content = content.replace("__TOKEN_POINT__", target_theme["graph_point"])
        content = content.replace("__TOKEN_BADGE_COLOR__", target_theme["badge_color"])

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"[SUCCESS] Successfully updated {len(files)} files to {target_theme['name']}.")
    print("[TIP] Commit and push your changes to immediately see your refreshed profile live on GitHub!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python switch_theme.py [teal | violet | emerald | gold | rotate]")
        sys.exit(1)
    
    switch_theme(sys.argv[1].lower())
