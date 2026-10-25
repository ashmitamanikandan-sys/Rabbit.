# RABBIT Preservation Rules & Core Invariants

> **CRITICAL RULE:** Do NOT break or modify the entry flow, genre selection, or feed navigation without explicit user confirmation.

### 1. Invariant Entry Experience
- **Opening Page:** Must display the official RABBIT logo (`${logo()}`) and "Go down the rabbit hole."
- **Direct Genre Chips:** Direct genre selector chips (`SELECT OR EXPLORE A GENRE`) are visible directly on the welcome screen.
- **Selection Interaction:**
  - Clicking any chip calls `selectWelcomeGenre(btn, genre)` to immediately set the active genre and highlight the chip.
  - Clicking `Enter the burrow →` calls `enterBurrowFromWelcome()`, immediately loading the feed via `renderHome()` and `window.switchSingleGenre()`.
- **No Early Redirects:** Tapping a chip on the welcome screen must NOT redirect or leave the user stuck.
- **No Modal Loops:** Do NOT replace this direct screen with modal popups or full-screen overlays that can break DOM mounting.
- **No "Wild Burrow" Overrides:** Never inject `rabbit_wild_burrow_active` locks that force all 21 genres and prevent single genre exploration.

### 2. Standalone Pages
- `warren.html`, `clubs.html`, `account.html`, `community.html`, `discover.html` are standalone pages.
- Never add unconditional `window.location.replace("./?tab=...")` or circular redirects to standalone pages.

### 3. Golden Backups
- **Git Tag:** `v1.0-gold-stable`
- **Git Branch:** `backup/stable-feed-gold`
- **File Directory Snapshot:** `backups/stable_v1_0_gold/`
  - `index.html`
  - `rabbit-feed-extension.js`
  - `rabbit-v10.js`
  - `rabbit-catalog.js`
  - `rabbit-genres-catalog.js`
  - `rabbit-config.js`
  - `rabbit-enrichment-engine.js`

If anything breaks during future experimental updates, immediately revert files using:
```bash
git checkout v1.0-gold-stable -- index.html rabbit-feed-extension.js
```
