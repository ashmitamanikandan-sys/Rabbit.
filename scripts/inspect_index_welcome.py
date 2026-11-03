# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(360, min(440, len(lines))):
    print(f"{i+1}: {lines[i].strip()}")
