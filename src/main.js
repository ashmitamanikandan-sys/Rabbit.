// ========================================================
// RABBIT APPLICATION CONTROLLER (Phase 1 Modernization)
// ========================================================

import './styles/responsive.css';
import { 
  state, 
  subscribe, 
  setScreen, 
  completeOnboarding, 
  resetOnboardingForTesting,
  openReader, 
  closeReader 
} from './state/store.js';
import { renderWelcomeScreen, renderGenreSelectionScreen } from './components/welcome.js';
import { renderMainFeed } from './components/feed.js';
import { renderDesktopSidebar, renderDesktopContextPane } from './components/nav.js';
import { renderReaderModal } from './components/reader.js';
import { findBookById } from './data/catalog.js';

const appContainer = document.getElementById('app');

// Expose testing/demo reset helper on window
window.resetRabbitOnboarding = resetOnboardingForTesting;

// Direct Link Handling: Check for ?book=... query parameter
async function handleDirectLinkRoute() {
  try {
    const params = new URLSearchParams(window.location.search);
    const bookId = params.get('book');
    if (bookId) {
      console.log(`[RABBIT] Direct book route requested: ${bookId}`);
      const book = await findBookById(bookId);
      if (book) {
        console.log(`[RABBIT] Found book for direct link:`, book.title);
        openReader(book, 'direct');
        return true;
      }
    }
  } catch (err) {
    console.warn('[RABBIT] Error resolving direct book route:', err);
  }
  return false;
}

// Master Render Function based on state.currentScreen
let isRendering = false;
async function renderApp() {
  if (isRendering) return;
  isRendering = true;

  try {
    const screen = state.currentScreen;
    const isDesktop = window.innerWidth >= 1024;

    if (screen === 'welcome') {
      // Screen 1: Original Welcome Experience (Part 2)
      appContainer.replaceChildren();
      renderWelcomeScreen(appContainer, () => {
        setScreen('interests');
      });
    } else if (screen === 'interests') {
      // Screen 2: Multi-Genre Interest Selection (Part 2)
      appContainer.replaceChildren();
      const initialGenres = state.selectedGenres.size > 0 
        ? Array.from(state.selectedGenres) 
        : [state.activeGenre];
      renderGenreSelectionScreen(appContainer, initialGenres, (selected) => {
        completeOnboarding(selected);
      });
    } else {
      // Screen 3: Personalized Feed & Reading Experience (Part 2 & 5)
      appContainer.replaceChildren();

      if (isDesktop) {
        // Desktop Multi-column Layout: Sidebar + Center Feed + Context Pane
        const desktopShell = document.createElement('div');
        desktopShell.className = 'rabbit-desktop-shell';

        // Left Sidebar
        const sidebar = renderDesktopSidebar(state.activeNavTab || 'for-you', (tab) => {
          renderApp();
        });
        desktopShell.appendChild(sidebar);

        // Center Feed Container
        const feedWrapper = document.createElement('div');
        feedWrapper.className = 'rabbit-desktop-feed-wrapper';
        desktopShell.appendChild(feedWrapper);

        // Right Context Pane
        const contextPane = renderDesktopContextPane();
        desktopShell.appendChild(contextPane);

        appContainer.appendChild(desktopShell);

        // Render feed in center column
        await renderMainFeed(feedWrapper);
      } else {
        // Mobile / Tablet Clean Layout
        await renderMainFeed(appContainer);
      }
    }

    // If a reader modal is currently active, mount the modal
    const bookToRead = state.activeReadingBook || state.activeBook;
    if (bookToRead) {
      renderReaderModal(bookToRead, () => {
        closeReader();
      });
    } else {
      const existingOverlay = document.getElementById('rabbit-reader-overlay');
      if (existingOverlay) existingOverlay.remove();
    }
  } catch (err) {
    console.error('[RABBIT] Render error:', err);
  } finally {
    isRendering = false;
  }
}

// Subscribe to state updates
subscribe(() => {
  renderApp();
});

// Window resize listener to adapt layout seamlessly
let resizeTimer = null;
window.addEventListener('resize', () => {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    if (state.currentScreen === 'home') {
      renderApp();
    }
  }, 150);
});

// App Initialization
async function initApp() {
  console.log('[RABBIT] Modernized modular client initializing...');
  
  // Render initial screen based on onboarding status
  await renderApp();

  // Check if a direct book URL was opened (?book=...)
  await handleDirectLinkRoute();
}

initApp();
