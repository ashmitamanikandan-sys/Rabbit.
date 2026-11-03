import re

with open(r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app\rabbit-genres-catalog.js", "r", encoding="utf-8") as f:
    text = f.read()

genres = re.findall(r'window\.RABBIT_GENRES_CATALOG\["([^"]+)"\]', text)
print("Total genres:", len(genres))
print("Genres:", genres)

# Let's count books per genre
for g in genres:
    m = re.search(r'window\.RABBIT_GENRES_CATALOG\["' + re.escape(g) + r'"\]\s*=\s*\[(.*?)\];', text, re.DOTALL)
    if m:
        # count occurrences of "id":
        count = len(re.findall(r'"id":', m.group(1)))
        print(f"  {g}: {count} books")
