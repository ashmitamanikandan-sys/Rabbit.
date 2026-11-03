# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('rabbit-feed-extension.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Total lines in rabbit-feed-extension.js:", len(lines))
for i in range(max(0, len(lines) - 45), len(lines)):
    print(f"{i+1}: {lines[i].strip()[:100]}")
