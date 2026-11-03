# RABBIT 🐇

### "Every chapter is a star."

**[↗ OPEN RABBIT 2.0 — LAUNCH THE APP](http://localhost:8080/index.html)** · **[✦ OPEN DEMO PROFILE (?demo=1)](http://localhost:8080/index.html?demo=1)**

*A mobile-first celestial discovery experience for books, ideas, and the curious mind.*

---

## What is RABBIT 2.0?

**RABBIT 2.0** turns book discovery into a night sky of human curiosity.
- Every chapter a reader finishes becomes a **star in their personal night sky**.
- Every book has its own **constellation** of stars arranged in a unique shape generated deterministically from the book id.
- As a user finishes chapters, the book's constellation lights up star by star. Completing every chapter of a book completes the constellation with a subtle, elegant celestial celebration.
- Genres form **regions of the Sky** (The Human Mind in teal, Self Discovery in rose, Science Fiction in electric blue, Classics in emerald, Philosophy in amethyst, History in amber).

---

## The Signature 5-Card Chapter Deck

Each feed post in **The Burrow** is a deck of 5 cards for one chapter (vertical swipe = next chapter; horizontal swipe = deeper into this chapter):

1. **The Spark (Front Card):** Book cover, title, author, chapter number + title, genre pill, max 16-word hook, and an 8–10 line insight explaining the core idea.
2. **Key Ideas:** 3 core takeaways (bold one-liner + supporting sentence).
3. **The Line:** Memorable line (verbatim quote for public domain classics; original *"RABBIT's take"* for in-copyright books) with *"✦ Share to The Warren"*.
4. **In Your Life:** 2–3 concrete, relatable daily life scenarios (school, friendships, habits, ambition).
5. **Rabbit Hole:** *"This chapter connects to..."* with 1–2 tappable chapters from other books. Reaching Card 5 collects the star and animates a flying star particle into **The Sky** nav icon!

---

## Key Worlds & Navigation

| Name | What it is |
| --- | --- |
| **The Burrow** | Home feed: vertical snap scroll of 5-card Chapter Decks with glowing "Constellations in progress" top rail. |
| **The Sky** | Interactive celestial canvas: pan, zoom, inspect constellations, and view your personal night sky. |
| **Tonight's Sky** | Daily set of 5 hand-picked chapters with a completion recap screen (*"You've lit 5 stars tonight"*). |
| **Nights** | Daily streak unit (consecutive days with at least one star lit). |
| **The Warren** | Reader community: thoughts & reflections attached directly to a specific chapter or line. |
| **Clubs** | Co-reading groups lighting up shared constellations together. |
| **RABBIT Wrapped** | High-res 1080×1920 Instagram/TikTok story card with PNG export & Web Share API. |

---

## Curated Catalog & Quality Gate

The catalog features **1,054 books across 21 genres (3,285 chapters)**:
- **36 Handcrafted Hero Books:** 12 in The Human Mind, 12 in Self Discovery, and 12 in Science Fiction (6 chapters each).
- **Public Domain Classics Included:** *Meditations*, *Thirukkural*, *Siddhartha*, *Gitanjali*, *Frankenstein*, *The Time Machine*.
- **Quality Gate:** Validated by `scripts/validate_catalog.py` ensuring **0 duplicate sentences** of 8+ words, **0 banned phrases**, and **100% valid connections**.

---

## Running Locally

1. Start a local static file server:
   ```bash
   python -m http.server 8080
   ```
2. Open in your browser:
   - Standard app: `http://localhost:8080/index.html`
   - Competition demo mode: `http://localhost:8080/index.html?demo=1`
3. Validate catalog:
   ```bash
   python scripts/validate_catalog.py
   ```

*All work is safely isolated on the `rabbit-2.0` git branch with backup tag `pre-rabbit-2.0`.*
