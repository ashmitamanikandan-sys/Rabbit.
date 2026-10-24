// ========================================================
// RABBIT BOOK INSIGHT CARD COMPONENT (Phase 1 Modernization)
// ========================================================

import { state, toggleSaveBook } from '../state/store.js';
import { getBookTotalLikes, isBookLiked, handleLikeClick, formatDemoBadge } from '../services/social.js';
import { shareBook } from '../services/share.js';

export function createBookCard(book, index, options = {}) {
  const isFirstSlot = options.isFirstSlot || false;
  const bookId = book.id || book.title;
  const isSaved = state.savedBookIds.has(bookId);
  const isLiked = isBookLiked(bookId);
  const totalLikes = getBookTotalLikes(bookId);

  const article = document.createElement('article');
  article.className = isFirstSlot ? 'feature rabbit-first-slot-card' : 'feedpost rabbit-expanded-post';
  article.dataset.bookId = bookId;
  article.style.scrollSnapAlign = 'start';

  const coverUrl = book.cover_url || book.cover || 'https://covers.openlibrary.org/b/id/8231998-M.jpg';
  const displayGenre = (book.mixedGenreBadge || book.genre || state.activeGenre || 'Curiosity').toUpperCase();
  const hook = book.hook || book.landmark_hook || book.title;
  const preview = book.preview || book.editorial_preview || book.description || book.original_summary || 'An original insight inspired by this landmark masterwork.';

  article.innerHTML = `
    ${!isFirstSlot ? `
      <div class="top" style="display:flex;align-items:center;justify-content:space-between;padding:12px 20px 0;">
        <span class="muted" style="font-size:11px;letter-spacing:1px;font-weight:700;color:#9ca3af;">RABBIT DISCOVERY</span>
        <span style="font-size:13px;color:var(--lilac);font-weight:700;">✦</span>
      </div>
    ` : ''}

    <div class="postbody" style="padding:${isFirstSlot ? '16px 0 24px' : '20px 20px 30px'};">
      <div class="postmeta" style="font-size:11px;font-weight:700;letter-spacing:1.2px;color:#a855f7;margin-bottom:12px;">
        ${displayGenre} · HOP ${String(index + 1).padStart(2, '0')}
      </div>

      <div class="bookrow" style="display:flex;gap:16px;align-items:flex-start;margin-bottom:14px;">
        <img class="cover" 
          src="${coverUrl}" 
          alt="Cover of ${book.title}" 
          loading="lazy" 
          decoding="async" 
          style="width:58px;height:86px;object-fit:cover;border-radius:6px;box-shadow:0 6px 16px rgba(0,0,0,0.5);flex-shrink:0;"
        >
        <div style="flex:1;min-width:0;">
          <h3 style="font-size:18px;margin:0 0 4px;font-weight:700;line-height:1.25;color:#f9fafb;">${book.title}</h3>
          <p style="font-size:13px;color:#9ca3af;margin:0 0 6px;">${book.author}</p>
          <span style="display:inline-block;padding:2px 8px;border-radius:12px;background:rgba(255,255,255,0.06);font-size:10px;font-weight:600;color:#d1d5db;">
            Landmark Work
          </span>
        </div>
      </div>

      <div class="eyebrow" style="color:var(--lilac);letter-spacing:1.5px;font-size:10px;font-weight:700;margin-top:10px;">THE CORE INSIGHT</div>
      <h2 style="font-size:21px;letter-spacing:-0.4px;line-height:1.28;margin:8px 0 14px;color:#ffffff;font-family:var(--reading-font);">
        ${hook}
      </h2>

      <div class="insight teaser" style="font-size:14px;line-height:1.75;color:#d1d5db;margin-bottom:20px;white-space:pre-line;">
        ${preview}
      </div>

      <!-- Action Bar with Real Share, Interactive Likes, Save, and Read More -->
      <div class="actions" style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding-top:10px;border-top:1px solid rgba(255,255,255,0.07);">
        <!-- Interactive Like Button with Live Counter -->
        <button type="button" 
          class="rabbit-action-btn rabbit-like-btn ${isLiked ? 'active' : ''}" 
          aria-label="Like insight" 
          aria-pressed="${isLiked ? 'true' : 'false'}"
          style="display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:20px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#e5e7eb;font-size:13px;cursor:pointer;transition:all 0.18s ease;"
        >
          <svg viewBox="0 0 24 24" class="rabbit-action-icon" style="width:16px;height:16px;fill:${isLiked ? '#ec4899' : 'none'};stroke:${isLiked ? '#ec4899' : 'currentColor'};stroke-width:2;">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
          <span class="rabbit-like-counter" style="font-weight:600;font-variant-numeric:tabular-nums;">${totalLikes.toLocaleString()}</span>
        </button>

        <!-- Save / Bookmark Button -->
        <button type="button" 
          class="rabbit-action-btn rabbit-save-btn ${isSaved ? 'active' : ''}" 
          aria-label="Save to My Library"
          aria-pressed="${isSaved ? 'true' : 'false'}"
          style="display:inline-flex;align-items:center;gap:6px;padding:8px 12px;border-radius:20px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#e5e7eb;font-size:13px;cursor:pointer;transition:all 0.18s ease;"
        >
          <svg viewBox="0 0 24 24" class="rabbit-action-icon" style="width:16px;height:16px;fill:${isSaved ? '#a855f7' : 'none'};stroke:${isSaved ? '#a855f7' : 'currentColor'};stroke-width:2;">
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
          </svg>
          <span style="font-size:12px;font-weight:500;">${isSaved ? 'Saved' : 'Save'}</span>
        </button>

        <!-- Real Web Share Button (Part 3) -->
        <button type="button" 
          class="rabbit-action-btn rabbit-share-btn" 
          aria-label="Share insight link"
          style="display:inline-flex;align-items:center;gap:6px;padding:8px 12px;border-radius:20px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#e5e7eb;font-size:13px;cursor:pointer;transition:all 0.18s ease;"
        >
          <svg viewBox="0 0 24 24" class="rabbit-action-icon" style="width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2;">
            <circle cx="18" cy="5" r="3"></circle>
            <circle cx="6" cy="12" r="3"></circle>
            <circle cx="18" cy="19" r="3"></circle>
            <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line>
            <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>
          </svg>
          <span style="font-size:12px;font-weight:500;">Share</span>
        </button>

        <!-- Read More Button -->
        <button type="button" 
          class="readmore rabbit-readmore-btn" 
          style="margin-left:auto;padding:8px 16px;border-radius:20px;background:rgba(168,85,247,0.15);color:#d8b4fe;border:1px solid rgba(168,85,247,0.35);font-size:12px;font-weight:600;cursor:pointer;transition:all 0.18s ease;"
        >
          Read more ↗
        </button>
      </div>

      <!-- Demo activity badge explaining prototype counts -->
      <div style="margin-top:12px;display:flex;align-items:center;justify-content:space-between;">
        ${formatDemoBadge()}
        <span style="font-size:10px;color:#71717a;">Swipe for next discovery ↓</span>
      </div>
    </div>
  `;

  // Attach event listeners
  const likeBtn = article.querySelector('.rabbit-like-btn');
  const countEl = article.querySelector('.rabbit-like-counter');
  if (likeBtn) {
    likeBtn.onclick = (e) => {
      e.stopPropagation();
      handleLikeClick(bookId, likeBtn, countEl);
    };
  }

  const saveBtn = article.querySelector('.rabbit-save-btn');
  if (saveBtn) {
    saveBtn.onclick = (e) => {
      e.stopPropagation();
      toggleSaveBook(bookId);
      const isNowSaved = state.savedBookIds.has(bookId);
      saveBtn.classList.toggle('active', isNowSaved);
      saveBtn.setAttribute('aria-pressed', isNowSaved ? 'true' : 'false');
      const textSpan = saveBtn.querySelector('span');
      if (textSpan) textSpan.textContent = isNowSaved ? 'Saved' : 'Save';
      const icon = saveBtn.querySelector('svg');
      if (icon) {
        icon.style.fill = isNowSaved ? '#a855f7' : 'none';
        icon.style.stroke = isNowSaved ? '#a855f7' : 'currentColor';
      }
    };
  }

  const shareBtn = article.querySelector('.rabbit-share-btn');
  if (shareBtn) {
    shareBtn.onclick = (e) => {
      e.stopPropagation();
      shareBook(book);
    };
  }

  const readmoreBtn = article.querySelector('.rabbit-readmore-btn');
  if (readmoreBtn && options.onReadMore) {
    readmoreBtn.onclick = (e) => {
      e.stopPropagation();
      options.onReadMore(book);
    };
  }

  return article;
}
