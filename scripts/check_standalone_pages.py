# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['warren.html', 'clubs.html', 'account.html', 'community.html', 'discover.html']:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            first_few = [f.readline().strip() for _ in range(6)]
            print(f"=== {fname} ===")
            print("  ", first_few[0])
            print("  ", first_few[1] if len(first_few) > 1 else "")
    except Exception as e:
        print(f"Error {fname}:", e)
