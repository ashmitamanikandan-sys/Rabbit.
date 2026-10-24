// ========================================================
// RABBIT SOCIAL & DEMO ENGAGEMENT (Phase 1 Modernization - Part 4)
// ========================================================

import { state, toggleLikeBook } from '../state/store.js';

// Deterministic string hash to generate a stable, natural engagement count
function hashString(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = ((hash << 5) - hash) + str.charCodeAt(i);
    hash |= 0;
  }
  return Math.abs(hash);
}

export function getBookBaseEngagement(bookId) {
  if (!bookId) return 42;
  const hash = hashString(String(bookId));
  // Deterministic count between 28 and 480
  const baseLikes = 28 + (hash % 453);
  return baseLikes;
}

export function getBookTotalLikes(bookId) {
  const base = getBookBaseEngagement(bookId);
  const userLiked = state.likedBookIds.has(bookId);
  return base + (userLiked ? 1 : 0);
}

export function isBookLiked(bookId) {
  return state.likedBookIds.has(bookId);
}

export function handleLikeClick(bookId, buttonEl, countEl) {
  toggleLikeBook(bookId);
  const isNowLiked = state.likedBookIds.has(bookId);
  const newCount = getBookTotalLikes(bookId);

  if (buttonEl) {
    buttonEl.classList.toggle('active', isNowLiked);
    buttonEl.setAttribute('aria-pressed', isNowLiked ? 'true' : 'false');
  }

  if (countEl) {
    countEl.textContent = newCount.toLocaleString();
    countEl.style.transform = 'scale(1.15)';
    setTimeout(() => {
      countEl.style.transform = 'scale(1)';
    }, 180);
  }
}

export function formatDemoBadge() {
  return `
    <span class="rabbit-demo-activity-badge" title="Demo engagement count for prototype demonstration" aria-label="Demo activity indicator">
      <span class="rabbit-demo-dot"></span> Demo activity
    </span>
  `;
}
