# RABBIT 2.0 — Master Build Changelog

> **Identity:** *"Every chapter is a star."*  
> **Release Branch:** `rabbit-2.0`  
> **Backup Reference:** `pre-rabbit-2.0`  
> **Demo Ready:** National & International Student Innovation Competition Grade

---

## 1. Executive Summary

RABBIT 2.0 transforms the prototype into an award-worthy, mobile-first book discovery platform centered on a signature metaphor: **Every chapter a user finishes becomes a star in their personal night sky.**

### World Terminology & Core Architecture
- **The Burrow:** The home feed featuring vertical snap-scroll chapter decks.
- **The Sky:** The celestial profile screen featuring an interactive, high-DPI pannable night sky canvas displaying deterministic book constellations grouped into colored genre regions.
- **Tonight's Sky:** A daily set of 5 hand-picked chapter decks with a completion recap screen (*"You've lit 5 stars tonight"*).
- **Nights:** Daily streak counter (consecutive days with $\ge 1$ star lit).
- **The Warren:** Reader community posts attached directly to a specific chapter or Line card.
- **Clubs:** Shared reading groups lighting up shared constellations together.
- **RABBIT Wrapped:** 1080×1920 exportable high-resolution Instagram/TikTok story card.

---

## 2. Signature Chapter Deck Format

Each feed post is an interactive deck of 5 horizontal cards for one chapter:
1. **The Spark (Front Card):** Book cover, title, author, chapter number + title, genre pill, max 16-word hook, and an 8–10 line insight explaining the chapter's core idea.
2. **Key Ideas:** 3 core takeaways, each as a bold one-liner plus a supporting explanation. (Spoiler-protected on fiction).
3. **The Line:** Memorable quote (verbatim with attribution for public domain; original *"RABBIT's take"* for in-copyright titles) with a *"✦ Share to The Warren"* action.
4. **In Your Life:** 2–3 concrete, relatable daily life applications (school, friendships, phone habits, ambition).
5. **Rabbit Hole:** *"This chapter connects to..."* with 1–2 tappable chapters from other books. Reaching Card 5 collects the star, triggers the flying star particle micro-interaction to the Sky nav icon, and updates the constellation progress ring.

---

## 3. Catalog Rebuild & Quality Gate Validation

The catalog was upgraded from generic templated sections into a curated, verified catalog across all 21 genres (**1,054 books, 3,285 chapters**).

### Quality Gate Results (`scripts/validate_catalog.py`)
- **Total Books:** 1,054
- **Handcrafted Hero Books:** 36 (12 Human Mind, 12 Self Discovery, 12 Science Fiction) with 6 chapters each.
- **Public Domain Classics Included:** *Meditations*, *Thirukkural*, *Siddhartha*, *Gitanjali*, *Frankenstein*, *The Time Machine*.
- **Duplicate Sentences (8+ words):** **0** across all books.
- **Banned Phrases:** **0** (*masterwork*, *unmask*, *dismantle*, *radical clarity*, *architecture of your attention*, *safely mediocre*, *the rabbit hole runs deep*, *superficial trivia*, *hyper-modern algorithmic world*).
- **Missing Required Deck Fields:** **0**.
- **Sparks < 6 lines:** **0**.
- **Invalid `connects_to` pointers:** **0**.

---

## 4. Celestial Sky Engine (`rabbit-sky-engine.js` & `rabbit-sky-canvas.js`)

- **State Management:** Stored under LocalStorage key `rabbit_sky_v2` with automatic migration from legacy `rabbit_taste_v101`.
- **Deterministic Constellations:** Mathematical PRNG seeded from `book.id` generates repeatable star coordinates and connecting line topologies.
- **Interactive Celestial Canvas:** Touch and mouse pan/zoom navigation with smooth inertia, genre nebulae glow, guide stars, and click-to-inspect constellation modal.
- **Constellation Celebration:** Subtle, elegant line-drawing animation, soft glow, and book title fade-in on completion (no cartoon confetti).
- **Demo Mode:** Accessible via `?demo=1` pre-populating *"Curious Reader"* with 42 stars, 2 completed constellations (*Atomic Habits*, *Meditations*), and a 12-night streak.
- **Database Schema:** Local-first offline architecture with exported PostgreSQL/Supabase schema in `sql/rabbit_sky_v2.sql`.

---

## 5. Viewport & Device Testing

Verified responsive layouts with zero horizontal overflow:
- **Small Mobile:** 360×800
- **Standard Mobile:** 390×844
- **Large Mobile:** 430×932
- **Tablet Portrait:** 768×1024
- **Tablet Landscape:** 1024×768
- **Compact Laptop:** 1366×768
- **Standard Laptop:** 1440×900
- **Desktop:** 1920×1080

Screenshots preserved in `docs/screenshots/` and `docs/screenshots/devices/`.

---

## 6. Safety & Preservation Rules Compliance

1. **Rule 0 Invariants Maintained:**
   - Welcome screen retains official RABBIT logo (`${logo()}`), headline *"Go down the rabbit hole."*, direct genre chips (*"SELECT OR EXPLORE A GENRE"*), `selectWelcomeGenre(btn, genre)`, and `Enter the burrow →` calling `enterBurrowFromWelcome()`.
   - Standalone pages (`warren.html`, `clubs.html`, `account.html`, `community.html`, `discover.html`) have zero circular redirects.
   - Zero service-role keys exposed in client files.
   - Clean, local-first operation with zero console errors.
