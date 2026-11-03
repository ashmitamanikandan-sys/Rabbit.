import json

def ch(n, title, hook, spark, ideas, line, life, connects, spoiler="none"):
    return {
        "n": n, "title": title, "hook": hook, 
        "spark": "\n".join(spark) if isinstance(spark, list) else spark,
        "key_ideas": [{"idea": i[0], "why": i[1]} for i in ideas],
        "line": {"text": line[0], "type": line[1]},
        "in_your_life": life,
        "connects_to": [{"book_id": c[0], "chapter": c[1], "reason": c[2]} for c in connects],
        "spoiler_level": spoiler
    }

with open("catalog/hero_mind.json", "r", encoding="utf-8") as f:
    books = json.load(f)

for b in books:
    if b["id"] == "deep-work":
        new_chs = []
        for item in b["chapters"]:
            if isinstance(item, list):
                new_chs.append(ch(*item))
            else:
                new_chs.append(item)
        b["chapters"] = new_chs
        print("Fixed deep-work chapters!")

with open("catalog/hero_mind.json", "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2, ensure_ascii=False)

print("Updated hero_mind.json.")
