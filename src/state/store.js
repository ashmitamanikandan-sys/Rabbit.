// ========================================================
// RABBIT CENTRALIZED STATE STORE (Phase 1 Modernization)
// ========================================================

const STORAGE_KEYS = {
  ENTERED: 'rabbit_entered',
  SELECTED_GENRE: 'rabbit_selected_genre',
  SELECTED_GENRES: 'rabbit_selected_genres',
  ONBOARDING_INTERESTS: 'rabbit_onboarding_interests',
  SAVED: 'rabbit_saved',
  LIKED: 'rabbit_likes_v101',
  FOLLOWED: 'rabbit_followed',
  TASTE: 'rabbit_taste_v101'
};

function safeGetJSON(key, fallback) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : fallback;
  } catch (e) {
    return fallback;
  }
}

function safeSetJSON(key, val) {
  try {
    localStorage.setItem(key, JSON.stringify(val));
  } catch (e) {}
}

// Initial state loaded cleanly from storage and URL parameters
const urlParams = new URLSearchParams(window.location.search);
const urlGenre = urlParams.get('genre');
const savedGenre = localStorage.getItem(STORAGE_KEYS.SELECTED_GENRE);
const savedGenresList = safeGetJSON(STORAGE_KEYS.SELECTED_GENRES, []);
const savedInterests = safeGetJSON(STORAGE_KEYS.ONBOARDING_INTERESTS, []);

const initialGenre = urlGenre || savedGenre || (savedGenresList.length ? savedGenresList[0] : 'Self Discovery');
const initialSelectedSet = new Set(
  savedGenresList.length ? savedGenresList : (savedInterests.length ? savedInterests : [initialGenre])
);

export const state = {
  onboardingComplete: localStorage.getItem(STORAGE_KEYS.ENTERED) === 'true',
  currentScreen: (localStorage.getItem(STORAGE_KEYS.ENTERED) === 'true') ? 'home' : 'welcome',
  activeGenre: initialGenre,
  selectedGenres: initialSelectedSet,
  mixMode: initialSelectedSet.size > 1,
  savedBookIds: new Set(safeGetJSON(STORAGE_KEYS.SAVED, [])),
  likedBookIds: new Set(safeGetJSON(STORAGE_KEYS.LIKED, [])),
  followedBookIds: new Set(safeGetJSON(STORAGE_KEYS.FOLLOWED, [])),
  activeNavTab: 'for-you',
  activeReadingBook: null,
  readingOrigin: 'home',
  searchTerm: '',
  demoActivityNoticeDismissed: false
};

const listeners = new Set();

export function subscribe(fn) {
  listeners.add(fn);
  return () => listeners.delete(fn);
}

export function notify(event, payload = null) {
  listeners.forEach(fn => fn(state, event, payload));
}

// State Mutation Actions
export function completeOnboarding(pickedGenres = []) {
  state.onboardingComplete = true;
  state.currentScreen = 'home';
  if (pickedGenres.length > 0) {
    state.selectedGenres = new Set(pickedGenres);
    state.activeGenre = pickedGenres[0];
    state.mixMode = pickedGenres.length > 1;
  }
  try {
    localStorage.setItem(STORAGE_KEYS.ENTERED, 'true');
    localStorage.setItem(STORAGE_KEYS.SELECTED_GENRE, state.activeGenre);
    safeSetJSON(STORAGE_KEYS.SELECTED_GENRES, Array.from(state.selectedGenres));
    safeSetJSON(STORAGE_KEYS.ONBOARDING_INTERESTS, Array.from(state.selectedGenres));
  } catch (e) {}
  updateUrlHistory();
  notify('ONBOARDING_COMPLETE');
}

export function resetOnboardingForTesting() {
  // Safe test helper: resets onboarding screen without deleting saved or liked books!
  state.onboardingComplete = false;
  state.currentScreen = 'welcome';
  try {
    localStorage.removeItem(STORAGE_KEYS.ENTERED);
  } catch (e) {}
  console.log('[RABBIT TEST] Onboarding reset for testing. Saved and liked books preserved.');
  notify('ONBOARDING_RESET');
}

// Expose reset helper globally for developers / testing
window.resetRabbitOnboarding = resetOnboardingForTesting;

export function setScreen(screenName) {
  state.currentScreen = screenName;
  notify('SCREEN_CHANGE', screenName);
}

export function switchGenre(targetGenre, updateHistory = true) {
  if (!targetGenre) return;
  state.mixMode = false;
  state.selectedGenres = new Set([targetGenre]);
  state.activeGenre = targetGenre;
  state.currentScreen = 'home';
  state.activeNavTab = 'for-you';
  try {
    localStorage.setItem(STORAGE_KEYS.SELECTED_GENRE, targetGenre);
    safeSetJSON(STORAGE_KEYS.SELECTED_GENRES, [targetGenre]);
  } catch (e) {}
  if (updateHistory) updateUrlHistory();
  notify('GENRE_SWITCH', targetGenre);
}

export function toggleGenre(targetGenre) {
  if (!targetGenre) return;
  if (state.selectedGenres.has(targetGenre)) {
    if (state.selectedGenres.size > 1) {
      state.selectedGenres.delete(targetGenre);
    }
  } else {
    state.selectedGenres.add(targetGenre);
  }
  state.mixMode = state.selectedGenres.size > 1;
  state.activeGenre = Array.from(state.selectedGenres)[0];
  state.currentScreen = 'home';
  try {
    localStorage.setItem(STORAGE_KEYS.SELECTED_GENRE, state.activeGenre);
    safeSetJSON(STORAGE_KEYS.SELECTED_GENRES, Array.from(state.selectedGenres));
  } catch (e) {}
  updateUrlHistory();
  notify('GENRE_TOGGLE', targetGenre);
}

export function resetToSingleGenre() {
  state.mixMode = false;
  const first = Array.from(state.selectedGenres)[0] || state.activeGenre || 'Self Discovery';
  state.selectedGenres = new Set([first]);
  state.activeGenre = first;
  try {
    localStorage.setItem(STORAGE_KEYS.SELECTED_GENRE, first);
    safeSetJSON(STORAGE_KEYS.SELECTED_GENRES, [first]);
  } catch (e) {}
  updateUrlHistory();
  notify('GENRE_RESET', first);
}

export function setActiveNavTab(tabName) {
  state.activeNavTab = tabName;
  if (tabName === 'for-you') {
    state.currentScreen = 'home';
  } else if (tabName === 'library') {
    state.currentScreen = 'library';
  } else if (tabName === 'following') {
    state.currentScreen = 'following';
  }
  notify('NAV_CHANGE', tabName);
}

export function toggleLikeBook(bookId) {
  const isLiked = state.likedBookIds.has(bookId);
  if (isLiked) {
    state.likedBookIds.delete(bookId);
  } else {
    state.likedBookIds.add(bookId);
  }
  safeSetJSON(STORAGE_KEYS.LIKED, Array.from(state.likedBookIds));
  notify('LIKE_TOGGLE', { bookId, isLiked: !isLiked });
}

export function toggleSaveBook(bookId) {
  const isSaved = state.savedBookIds.has(bookId);
  if (isSaved) {
    state.savedBookIds.delete(bookId);
  } else {
    state.savedBookIds.add(bookId);
  }
  safeSetJSON(STORAGE_KEYS.SAVED, Array.from(state.savedBookIds));
  notify('SAVE_TOGGLE', { bookId, isSaved: !isSaved });
}

export function toggleFollowBook(bookId) {
  const isFollowed = state.followedBookIds.has(bookId);
  if (isFollowed) {
    state.followedBookIds.delete(bookId);
  } else {
    state.followedBookIds.add(bookId);
  }
  safeSetJSON(STORAGE_KEYS.FOLLOWED, Array.from(state.followedBookIds));
  notify('FOLLOW_TOGGLE', { bookId, isFollowed: !isFollowed });
}

export function openReader(book, origin = 'home') {
  state.activeReadingBook = book;
  state.readingOrigin = origin;
  state.currentScreen = 'reader';
  updateUrlHistory();
  notify('READER_OPEN', book);
}

export function closeReader() {
  state.activeReadingBook = null;
  state.currentScreen = state.readingOrigin || 'home';
  updateUrlHistory();
  notify('READER_CLOSE');
}

export function setSearchTerm(term) {
  state.searchTerm = term;
  notify('SEARCH_CHANGE', term);
}

function updateUrlHistory() {
  try {
    const url = new URL(window.location.href);
    if (state.activeReadingBook) {
      url.searchParams.set('book', state.activeReadingBook.id || state.activeReadingBook.title);
    } else {
      url.searchParams.delete('book');
      if (state.mixMode) {
        url.searchParams.set('genre', Array.from(state.selectedGenres).join(','));
      } else {
        url.searchParams.set('genre', state.activeGenre);
      }
    }
    history.replaceState({
      genre: state.activeGenre,
      genres: Array.from(state.selectedGenres),
      bookId: state.activeReadingBook?.id || null
    }, '', url.toString());
  } catch (e) {}
}

// Window popstate event listener for browser Back/Forward
window.addEventListener('popstate', (e) => {
  if (state.currentScreen === 'reader') {
    closeReader();
    return;
  }
  const params = new URLSearchParams(window.location.search);
  const genreParam = params.get('genre');
  if (genreParam) {
    if (genreParam.includes(',')) {
      const parts = genreParam.split(',').map(s => s.trim()).filter(Boolean);
      state.selectedGenres = new Set(parts);
      state.activeGenre = parts[0];
      state.mixMode = parts.length > 1;
      notify('GENRE_SWITCH', state.activeGenre);
    } else {
      switchGenre(genreParam, false);
    }
  }
});
