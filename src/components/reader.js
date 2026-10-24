// ========================================================
// RABBIT INTERACTIVE READER MODAL COMPONENT (Part 1, 3, 4)
// ========================================================

import { state, toggleSaveBook } from '../state/store.js';
import { getBookTotalLikes, isBookLiked, handleLikeClick } from '../services/social.js';
import { shareBook } from '../services/share.js';

export function renderReaderModal(book, onClose) {
  const existing = document.getElementById('rabbit-reader-overlay');
  if (existing) existing.remove();

  const bookId = book.id || book.title;
  const isSaved = state.savedBookIds.has(bookId);
  const isLiked = isBookLiked(bookId);
  const totalLikes = getBookTotalLikes(bookId);
  const coverUrl = book.cover_url || book.cover || 'https://covers.openlibrary.org/b/id/8231998-M.jpg';

  const overlay = document.createElement('div');
  overlay.id = 'rabbit-reader-overlay';
  overlay.className = 'rabbit-reader-overlay';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-modal', 'true');
  overlay.setAttribute('aria-label', `Reading ${book.title}`);
  overlay.style.cssText = `
    position: fixed;
    inset: 0;
    z-index: 9999;
    background: #09090b;
    overflow-y: auto;
    overscroll-behavior: contain;
    -webkit-overflow-scrolling: touch;
    display: flex;
    flex-direction: column;
  `;

  // Synthesize rich chapter reading content if not present
  const hook = book.hook || book.landmark_hook || book.title;
  const preview = book.preview || book.editorial_preview || book.description || 'Explore the landmark ideas of this book.';
  const takeaway = book.takeaway || `True mastery comes from understanding the underlying mental model, not from blindly copying external techniques. In ${book.title}, the highest leverage comes from cultivating deliberate awareness and small, consistent adjustments.`;

  overlay.innerHTML = `
    <header class="reader-header" style="position:sticky;top:0;background:rgba(9,9,11,0.92);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,0.08);padding:14px 20px;display:flex;align-items:center;justify-content:space-between;z-index:10;">
      <button type="button" class="back-btn" id="rabbit-reader-back-btn" style="background:none;border:none;color:#d8b4fe;font-size:14px;font-weight:700;display:inline-flex;align-items:center;gap:6px;cursor:pointer;">
        ← Back to your rabbit hole
      </button>

      <div class="reader-actions" style="display:flex;gap:8px;align-items:center;">
        <!-- Like -->
        <button type="button" class="rabbit-like-btn ${isLiked ? 'active' : ''}" id="rabbit-reader-like-btn" style="background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.1);padding:6px 12px;border-radius:18px;color:#fff;cursor:pointer;display:inline-flex;align-items:center;gap:5px;font-size:12px;">
          <svg viewBox="0 0 24 24" style="width:14px;height:14px;fill:${isLiked ? '#ec4899' : 'none'};stroke:${isLiked ? '#ec4899' : 'currentColor'};stroke-width:2;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          <span class="rabbit-like-counter">${totalLikes.toLocaleString()}</span>
        </button>

        <!-- Save -->
        <button type="button" class="rabbit-save-btn ${isSaved ? 'active' : ''}" id="rabbit-reader-save-btn" style="background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.1);padding:6px 12px;border-radius:18px;color:#fff;cursor:pointer;display:inline-flex;align-items:center;gap:5px;font-size:12px;">
          <svg viewBox="0 0 24 24" style="width:14px;height:14px;fill:${isSaved ? '#a855f7' : 'none'};stroke:${isSaved ? '#a855f7' : 'currentColor'};stroke-width:2;"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
          <span>${isSaved ? 'Saved' : 'Save'}</span>
        </button>

        <!-- Share -->
        <button type="button" class="rabbit-share-btn" id="rabbit-reader-share-btn" style="background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.1);padding:6px 12px;border-radius:18px;color:#fff;cursor:pointer;display:inline-flex;align-items:center;gap:5px;font-size:12px;">
          <svg viewBox="0 0 24 24" style="width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2;"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>
          <span>Share</span>
        </button>
      </div>
    </header>

    <main class="reader-content" style="max-width:680px;width:100%;margin:0 auto;padding:32px 24px 80px;">
      <div class="bookrow" style="display:flex;gap:18px;align-items:center;margin-bottom:28px;">
        <img src="${coverUrl}" alt="${book.title}" style="width:68px;height:102px;object-fit:cover;border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,0.6);">
        <div>
          <div class="eyebrow" style="color:var(--lilac);font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:4px;">${(book.genre || 'LANDMARK').toUpperCase()} · ESSENTIAL CHAPTER</div>
          <h1 style="font-size:24px;font-weight:800;margin:0 0 6px;line-height:1.2;font-family:var(--reading-font);color:#f9fafb;">${book.title}</h1>
          <p style="font-size:14px;color:#9ca3af;margin:0;">By ${book.author}</p>
        </div>
      </div>

      <div class="hook-box" style="padding:18px 20px;border-radius:12px;background:rgba(168,85,247,0.08);border:1px solid rgba(168,85,247,0.22);margin-bottom:28px;">
        <div style="font-size:11px;font-weight:700;letter-spacing:1px;color:#c084fc;margin-bottom:6px;">THE CENTRAL CONVERSATION</div>
        <div style="font-size:17px;font-weight:600;line-height:1.45;color:#f3f4f6;">${hook}</div>
      </div>

      <div class="prose" style="font-size:16px;line-height:1.85;color:#e5e7eb;font-family:var(--reading-font);margin-bottom:36px;white-space:pre-line;">
        ${preview}

        Think about where this paradox manifests in your immediate environment. The value of deep reading is never passive retention of catchphrases; it is the calibration of your attention toward previously invisible leverage points.

        When you examine your daily decisions through this lens, the friction between what you consciously intend and what your habits actually deliver begins to dissolve. Small, thoughtful adjustments sustained over time generate outsized clarity.
      </div>

      <div class="takeaway-card" style="padding:22px;border-radius:14px;background:#131318;border-left:4px solid var(--lilac);margin-bottom:36px;">
        <div class="eyebrow" style="color:var(--lilac);font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:8px;">THE TAKEAWAY</div>
        <p style="font-size:15px;line-height:1.6;color:#f3f4f6;margin:0;">${takeaway}</p>
      </div>

      <button type="button" class="primary" id="rabbit-reader-bottom-close" style="width:100%;padding:14px;border-radius:24px;font-size:15px;font-weight:700;cursor:pointer;margin-top:20px;">
        ← Back to your rabbit hole
      </button>
    </main>
  `;

  document.body.appendChild(overlay);

  // Wire event handlers
  const closeBtn = overlay.querySelector('#rabbit-reader-back-btn');
  const bottomClose = overlay.querySelector('#rabbit-reader-bottom-close');
  const handleClose = () => {
    overlay.remove();
    if (onClose) onClose();
  };
  if (closeBtn) closeBtn.onclick = handleClose;
  if (bottomClose) bottomClose.onclick = handleClose;

  // Like button
  const likeBtn = overlay.querySelector('#rabbit-reader-like-btn');
  const countEl = overlay.querySelector('.rabbit-like-counter');
  if (likeBtn) {
    likeBtn.onclick = () => {
      handleLikeClick(bookId, likeBtn, countEl);
    };
  }

  // Save button
  const saveBtn = overlay.querySelector('#rabbit-reader-save-btn');
  if (saveBtn) {
    saveBtn.onclick = () => {
      toggleSaveBook(bookId);
      const isNowSaved = state.savedBookIds.has(bookId);
      saveBtn.classList.toggle('active', isNowSaved);
      saveBtn.querySelector('span').textContent = isNowSaved ? 'Saved' : 'Save';
      const icon = saveBtn.querySelector('svg');
      if (icon) icon.style.fill = isNowSaved ? '#a855f7' : 'none';
    };
  }

  // Share button
  const shareBtn = overlay.querySelector('#rabbit-reader-share-btn');
  if (shareBtn) {
    shareBtn.onclick = () => {
      shareBook(book);
    };
  }

  // Escape key handler
  const handleKeydown = (e) => {
    if (e.key === 'Escape') {
      document.removeEventListener('keydown', handleKeydown);
      handleClose();
    }
  };
  document.addEventListener('keydown', handleKeydown);
}
