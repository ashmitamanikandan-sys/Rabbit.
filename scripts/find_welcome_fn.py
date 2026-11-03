# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'enterBurrowFromWelcome' in line or 'selectWelcomeGenre' in line:
            print(f"{i+1}: {line.strip()[:100]}")
