# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['rabbit-v10.js', 'rabbit-feed-extension.js', 'rabbit-loader.js']:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            print(f"=== {fname} ===")
            for line in f:
                if 'function ' in line or 'render' in line or 'burrow' in line.lower():
                    if len(line.strip()) < 100:
                        print("  ", line.strip())
    except Exception as e:
        print(f"Error {fname}:", e)
