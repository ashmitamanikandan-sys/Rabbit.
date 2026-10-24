// ========================================================
// RABBIT RESTORED ORIGINAL WELCOME EXPERIENCE (Part 2)
// ========================================================

import { AUTHORITATIVE_GENRES } from '../data/catalog.js';
import { completeOnboarding } from '../state/store.js';

export function renderWelcomeScreen(container, onTakeMeToRabbitHole) {
  container.innerHTML = `
    <main class="page welcome">
      <div class="eyebrow">WELCOME TO RABBIT</div>
      <div style="font-size:70px;margin-top:25px;color:var(--lilac);line-height:1;">↘</div>
      <h1 style="margin:20px 0 16px;">Go down<br>the <span class="accent">rabbit hole.</span></h1>
      <p style="max-width:380px;line-height:1.6;color:var(--muted);font-size:15px;margin:0 auto 28px;">
        A feed of ideas worth getting lost in. Find your next obsession, one chapter at a time.
      </p>
      <button type="button" class="primary rabbit-welcome-cta" id="rabbit-welcome-cta" style="padding:14px 32px;font-size:16px;font-weight:600;border-radius:30px;cursor:pointer;letter-spacing:-0.2px;">
        Take me to the rabbit hole →
      </button>
      <p class="subtle" style="margin-top:24px;font-size:12px;color:#71717a;">Stories are everywhere. Follow your curiosity.</p>
    </main>
  `;

  const btn = container.querySelector('#rabbit-welcome-cta');
  if (btn) {
    btn.onclick = () => {
      onTakeMeToRabbitHole();
    };
  }
}

export function renderGenreSelectionScreen(container, initialSelected = [], onConfirm) {
  const selectedSet = new Set(initialSelected.length ? initialSelected : ['Self Discovery']);

  function render() {
    container.innerHTML = `
      <main class="page rabbit-onboarding-genres-page">
        <header class="top" style="padding:18px 24px;display:flex;align-items:center;justify-content:space-between;">
          <div class="wordmark" aria-label="RABBIT">
            <span style="font-size:18px;font-weight:800;letter-spacing:1px;color:#fff;">RABBIT <span style="color:var(--lilac)">✦</span></span>
          </div>
          <button type="button" class="subtle-btn" id="rabbit-skip-onboarding-btn" style="background:none;border:none;color:var(--muted);font-size:13px;cursor:pointer;">
            Explore with defaults →
          </button>
        </header>

        <div class="interests" style="padding:24px 20px 120px;max-width:680px;margin:0 auto;text-align:center;">
          <div class="eyebrow" style="color:var(--lilac);letter-spacing:1.5px;font-size:11px;font-weight:700;">THE FIRST HOP / 01</div>
          <h1 style="font-size:32px;margin:12px 0 10px;font-family:var(--reading-font);">What pulls you in?</h1>
          <p class="muted" style="font-size:14px;color:var(--muted);max-width:440px;margin:0 auto 28px;line-height:1.5;">
            Pick your rabbit holes. Explore as many worlds as you like.
          </p>

          <div class="chips" id="rabbit-onboarding-chips" style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:30px;">
            ${AUTHORITATIVE_GENRES.map(g => {
              const active = selectedSet.has(g);
              return `
                <button type="button" 
                  class="chip ${active ? 'active' : ''}" 
                  data-genre="${g}"
                  style="padding:10px 18px;font-size:14px;border-radius:24px;cursor:pointer;transition:all 0.18s ease;"
                >
                  ${active ? '✓ ' : ''}${g}
                </button>
              `;
            }).join('')}
          </div>
        </div>

        <div class="sticky-cta" style="position:fixed;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(to top, rgba(0,0,0,0.95) 70%, transparent);display:flex;justify-content:center;z-index:90;">
          <button type="button" class="primary" id="rabbit-confirm-interests-btn" style="width:100%;max-width:420px;padding:15px;font-size:16px;font-weight:700;border-radius:30px;cursor:pointer;">
            Enter the burrow (${selectedSet.size} ${selectedSet.size === 1 ? 'genre' : 'genres'}) →
          </button>
        </div>
      </main>
    `;

    // Chip click handlers
    container.querySelectorAll('#rabbit-onboarding-chips .chip').forEach(btn => {
      btn.onclick = () => {
        const g = btn.dataset.genre;
        if (selectedSet.has(g)) {
          if (selectedSet.size > 1) {
            selectedSet.delete(g);
          }
        } else {
          selectedSet.add(g);
        }
        render();
      };
    });

    const confirmBtn = container.querySelector('#rabbit-confirm-interests-btn');
    if (confirmBtn) {
      confirmBtn.onclick = () => {
        const picked = Array.from(selectedSet);
        onConfirm(picked);
      };
    }

    const skipBtn = container.querySelector('#rabbit-skip-onboarding-btn');
    if (skipBtn) {
      skipBtn.onclick = () => {
        onConfirm(Array.from(selectedSet));
      };
    }
  }

  render();
}
