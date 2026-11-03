import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app\index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
m = re.search(r'function selectWelcomeGenre.*?function enterBurrowFromWelcome.*?function renderWelcome.*?function toggleRabbitInterest', text, re.DOTALL)
if m:
    print(m.group(0))
