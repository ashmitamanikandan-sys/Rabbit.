import sys

def check_file(path, label):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read(1500)
    print(f"=== {label} ===")
    print(text[:800])
    print("\n...\n")

check_file(r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app\rabbit-enrichment-engine.js", "rabbit-enrichment-engine.js")
check_file(r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app\rabbit-feed-extension.js", "rabbit-feed-extension.js")
