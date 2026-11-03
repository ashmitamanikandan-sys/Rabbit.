with open(r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app\index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'(function\s+(?:renderWelcome|selectWelcomeGenre|enterBurrowFromWelcome|renderHome|renderFeed|chooseInterest|toggleRabbitInterest)[^{]*\{.*?\n\})', text, re.DOTALL)
for m in matches:
    print(m[:300])
    print("="*40)
