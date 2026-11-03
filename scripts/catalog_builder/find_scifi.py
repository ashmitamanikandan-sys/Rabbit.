import glob
import os

scifi_books = [
    'dune', 'frankenstein', '1984-george-orwell', 'brave-new-world',
    'neuromancer', 'the-three-body-problem', 'foundation',
    'do-androids-dream-of-electric-sheep', 'the-time-machine',
    'fahrenheit-451', 'snow-crash', 'i-robot'
]

for f in glob.glob('scripts/catalog_builder/*.py'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    found = [b for b in scifi_books if f'"{b}"' in txt or f"'{b}'" in txt]
    if found:
        print(f"{os.path.basename(f)}: {found}")
