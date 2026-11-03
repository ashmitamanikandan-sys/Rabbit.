import os

for fname in ['gen_hero_self.py', 'hero_self_all_complete.py']:
    path = os.path.join('scripts/catalog_builder', fname)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            print(f"=== {fname} ===")
            for line in f:
                if 'add_b(' in line or 'b(' in line:
                    print("  ", line.strip()[:80])
