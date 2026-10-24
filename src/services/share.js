// ========================================================
// RABBIT SHARING SERVICE (Phase 1 Modernization - Part 3)
// ========================================================

export function showToast(message, durationMs = 2400) {
  document.querySelectorAll('.rabbit-toast').forEach(el => el.remove());

  const toast = document.createElement('div');
  toast.className = 'rabbit-toast';
  toast.style.cssText = `
    position: fixed;
    bottom: 32px;
    left: 50%;
    transform: translateX(-50%) translateY(20px);
    background: #18181f;
    color: #f3f4f6;
    border: 1px solid rgba(168, 85, 247, 0.45);
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.85);
    padding: 12px 22px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 600;
    z-index: 99999;
    opacity: 0;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    display: inline-flex;
    align-items: center;
    gap: 8px;
    letter-spacing: 0.2px;
  `;
  toast.innerHTML = `<span style="color:#d8b4fe;font-size:15px;">✦</span> ${message}`;
  document.body.appendChild(toast);

  requestAnimationFrame(() => {
    toast.style.opacity = '1';
    toast.style.transform = 'translateX(-50%) translateY(0)';
  });

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(-50%) translateY(10px)';
    setTimeout(() => toast.remove(), 260);
  }, durationMs);
}

export function buildDirectBookUrl(book) {
  const base = window.location.origin + (import.meta.env?.BASE_URL || '/Rabbit./');
  const cleanBase = base.endsWith('/') ? base : base + '/';
  const bookIdentifier = book.id || book.title;
  return `${cleanBase}?book=${encodeURIComponent(bookIdentifier)}`;
}

export async function shareBook(book) {
  if (!book) return;

  const url = buildDirectBookUrl(book);
  const title = `RABBIT: ${book.title}`;
  const text = `${book.title} by ${book.author} — "${book.hook || book.description || 'Ideas worth falling into.'}"`;

  // 1. Try Native Mobile Web Share API
  if (navigator.share && navigator.canShare && navigator.canShare({ title, text, url })) {
    try {
      await navigator.share({
        title,
        text,
        url
      });
      return { success: true, method: 'native' };
    } catch (err) {
      if (err.name === 'AbortError') {
        // User closed the share sheet without picking an app
        return { success: false, method: 'aborted' };
      }
      console.warn('[RABBIT SHARE] Native share error, falling back to clipboard:', err);
    }
  }

  // 2. Desktop Fallback: Copy to Clipboard
  let copied = false;

  if (navigator.clipboard && navigator.clipboard.writeText) {
    try {
      await navigator.clipboard.writeText(url);
      copied = true;
    } catch (clipErr) {
      console.warn('[RABBIT SHARE] navigator.clipboard failed, trying fallback textarea:', clipErr);
    }
  }

  if (!copied) {
    try {
      const textarea = document.createElement('textarea');
      textarea.value = url;
      textarea.style.position = 'fixed';
      textarea.style.left = '-9999px';
      textarea.style.top = '0';
      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();
      const successful = document.execCommand('copy');
      textarea.remove();
      if (successful) copied = true;
    } catch (execErr) {
      console.warn('[RABBIT SHARE] execCommand fallback failed:', execErr);
    }
  }

  if (copied) {
    showToast('Book discovery link copied to clipboard! ↗');
    return { success: true, method: 'clipboard' };
  } else {
    showToast('Link: ' + url);
    return { success: false, method: 'failed' };
  }
}
