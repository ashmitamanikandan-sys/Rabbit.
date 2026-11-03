import glob
import os

books_to_check = ['meditations', 'the-courage-to-be-disliked', 'the-mountain-is-you', 'the-power-of-now', 'the-untethered-soul']
for f in glob.glob('scripts/catalog_builder/*.py'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    found = [b for b in books_to_check if f'"{b}"' in txt or f"'{b}'" in txt]
    if found:
        print(f"{os.path.basename(f)}: {found}")
