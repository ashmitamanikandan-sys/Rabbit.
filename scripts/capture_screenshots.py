# -*- coding: utf-8 -*-
"""
capture_screenshots.py
Captures required device and key screen screenshots using headless Edge.
"""

import os
import subprocess
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
SCREENSHOTS_DIR = os.path.join(DOCS_DIR, "screenshots")
DEVICES_DIR = os.path.join(SCREENSHOTS_DIR, "devices")

os.makedirs(DEVICES_DIR, exist_ok=True)

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

VIEWPORTS = [
    (360, 800, "360x800.png"),
    (390, 844, "390x844.png"),
    (430, 932, "430x932.png"),
    (768, 1024, "768x1024.png"),
    (1024, 768, "1024x768.png"),
    (1366, 768, "1366x768.png"),
    (1440, 900, "1440x900.png"),
    (1920, 1080, "1920x1080.png"),
]

# 1. Device Viewports (Welcome & Burrow)
print("Capturing device viewports...")
for w, h, fname in VIEWPORTS:
    out_path = os.path.join(DEVICES_DIR, fname)
    url = f"http://localhost:8080/index.html?demo=1"
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={w},{h}",
        f"--screenshot={out_path}",
        url
    ]
    try:
        subprocess.run(cmd, check=True, timeout=15)
        print(f"Captured: {fname} ({w}x{h})")
    except Exception as e:
        print(f"Error capturing {fname}:", e)

# 2. Key Screen Captures
KEY_SCREENS = [
    ("http://localhost:8080/index.html", 390, 844, "welcome.png"),
    ("http://localhost:8080/index.html?demo=1", 390, 844, "burrow_feed.png"),
    ("http://localhost:8080/warren.html", 390, 844, "the_warren.html.png"),
    ("http://localhost:8080/clubs.html", 390, 844, "clubs.html.png"),
    ("http://localhost:8080/community.html", 390, 844, "community.html.png"),
    ("http://localhost:8080/account.html", 390, 844, "account.html.png")
]

print("\nCapturing key screens...")
for url, w, h, fname in KEY_SCREENS:
    out_path = os.path.join(SCREENSHOTS_DIR, fname)
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={w},{h}",
        f"--screenshot={out_path}",
        url
    ]
    try:
        subprocess.run(cmd, check=True, timeout=15)
        print(f"Captured key screen: {fname}")
    except Exception as e:
        print(f"Error capturing {fname}:", e)

print("\nAll screenshot captures complete!")
