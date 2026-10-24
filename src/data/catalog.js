// ========================================================
// RABBIT ON-DEMAND CATALOG SERVICE (Phase 1 Modernization)
// ========================================================

export const AUTHORITATIVE_GENRES = [
  "Self Discovery",
  "Fantasy",
  "Romance",
  "History",
  "Science Fiction",
  "The Human Mind",
  "Philosophy",
  "Mystery & Thriller",
  "Horror",
  "Biography & Memoir",
  "Business & Money",
  "Young Adult",
  "Classics",
  "Adventure",
  "Science",
  "True Crime",
  "Politics & Society",
  "Poetry",
  "Literary Fiction",
  "Self-Help",
  "Historical Fiction"
];

export function genreNameToSlug(name) {
  if (!name) return "self-discovery";
  const s = String(name).toLowerCase().trim()
    .replace(/&/g, "and")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
  return s || "self-discovery";
}

export function resolveGenreName(input) {
  if (!input) return "Self Discovery";
  const lower = String(input).toLowerCase().trim();

  if (lower.includes("self discovery") || lower.includes("self-discovery")) return "Self Discovery";
  if (lower.includes("self-help") || lower.includes("self help") || lower.includes("productivity")) return "Self-Help";
  if (lower.includes("human mind") || lower === "the human mind" || lower.includes("psychology") || lower.includes("neuroscience") || lower.includes("behavior")) return "The Human Mind";
  if (lower.includes("sci-fi") || lower.includes("science fiction") || lower.includes("space") || lower.includes("technology") || lower.includes("artificial intelligence")) return "Science Fiction";
  if (lower.includes("fantasy") || lower.includes("mythology")) return "Fantasy";
  if (lower.includes("mystery") || lower.includes("thriller") || (lower.includes("crime") && !lower.includes("true crime"))) return "Mystery & Thriller";
  if (lower.includes("true crime")) return "True Crime";
  if (lower.includes("romance") || lower.includes("relationship") || lower.includes("love")) return "Romance";
  if (lower.includes("horror")) return "Horror";
  if (lower.includes("historical fiction")) return "Historical Fiction";
  if (lower.includes("history") || lower.includes("ancient")) return "History";
  if (lower.includes("young adult") || lower.includes("ya")) return "Young Adult";
  if (lower.includes("classic")) return "Classics";
  if (lower.includes("adventure") || lower.includes("travel")) return "Adventure";
  if (lower.includes("business") || lower.includes("money") || lower.includes("economic") || lower.includes("entrepreneurship") || lower.includes("leadership")) return "Business & Money";
  if (lower.includes("science") || lower.includes("environment") || lower.includes("nature")) return "Science";
  if (lower.includes("philosophy") || lower.includes("ethics")) return "Philosophy";
  if (lower.includes("biography") || lower.includes("memoir")) return "Biography & Memoir";
  if (lower.includes("politic") || lower.includes("society") || lower.includes("culture") || lower.includes("sociology") || lower.includes("feminism")) return "Politics & Society";
  if (lower.includes("poetry")) return "Poetry";
  if (lower.includes("literary") || lower.includes("fiction")) return "Literary Fiction";

  const match = AUTHORITATIVE_GENRES.find(g => g.toLowerCase() === lower);
  return match || "Self Discovery";
}

// In-memory genre cache for instant 0ms subsequent access
const genreCache = new Map();
const inFlightRequests = new Map();

// Helper to determine base path for data assets
function getDataPath(slug) {
  const base = import.meta.env?.BASE_URL || '/Rabbit./';
  const cleanBase = base.endsWith('/') ? base : base + '/';
  return `${cleanBase}data/genres/${slug}.json`;
}

export async function fetchGenreBooks(genreName) {
  const resolved = resolveGenreName(genreName);
  const slug = genreNameToSlug(resolved);

  if (genreCache.has(slug)) {
    return genreCache.get(slug);
  }

  if (inFlightRequests.has(slug)) {
    return inFlightRequests.get(slug);
  }

  const promise = (async () => {
    try {
      const url = getDataPath(slug);
      const res = await fetch(url);
      if (!res.ok) {
        throw new Error(`Failed to load genre data (${res.status}): ${url}`);
      }
      const data = await res.json();
      genreCache.set(slug, data);
      return data;
    } catch (err) {
      console.warn(`[RABBIT CATALOG] Fallback loading for ${slug}:`, err);
      // Fallback: check window.RABBIT_GENRES_CATALOG if present
      if (typeof window !== 'undefined' && window.RABBIT_GENRES_CATALOG) {
        const key = Object.keys(window.RABBIT_GENRES_CATALOG).find(
          k => k.toLowerCase() === resolved.toLowerCase()
        );
        if (key && window.RABBIT_GENRES_CATALOG[key]) {
          const books = window.RABBIT_GENRES_CATALOG[key];
          genreCache.set(slug, books);
          return books;
        }
      }
      return [];
    } finally {
      inFlightRequests.delete(slug);
    }
  })();

  inFlightRequests.set(slug, promise);
  return promise;
}

export async function fetchMultipleGenres(genreNames) {
  const results = new Map();
  const promises = genreNames.map(async (name) => {
    const books = await fetchGenreBooks(name);
    results.set(resolveGenreName(name), books);
  });
  await Promise.all(promises);
  return results;
}

export function buildMixedGenreFeed(genreMap, selectedGenresList) {
  const streams = [];
  selectedGenresList.forEach(g => {
    const resolved = resolveGenreName(g);
    const books = genreMap.get(resolved) || [];
    if (books.length > 0) {
      streams.push({
        genre: resolved,
        books: [...books],
        pointer: 0
      });
    }
  });

  if (streams.length === 0) return [];
  if (streams.length === 1) return streams[0].books;

  const blended = [];
  const seenIds = new Set();
  let exhausted = 0;
  let cycle = 0;

  while (exhausted < streams.length && blended.length < 80) {
    for (let i = 0; i < streams.length; i++) {
      const stream = streams[i];
      if (stream.pointer < stream.books.length) {
        const book = stream.books[stream.pointer++];
        const id = book.id || book.title;
        if (!seenIds.has(id)) {
          seenIds.add(id);
          blended.push({
            ...book,
            mixedGenreBadge: stream.genre
          });
        }
      } else {
        exhausted++;
      }
    }
    cycle++;
  }

  return blended;
}

export function searchCachedBooks(query) {
  if (!query || query.trim().length < 2) return [];
  const q = query.toLowerCase().trim();
  const results = [];
  const seen = new Set();

  for (const books of genreCache.values()) {
    for (const b of books) {
      const matchTitle = (b.title || "").toLowerCase().includes(q);
      const matchAuthor = (b.author || "").toLowerCase().includes(q);
      const matchHook = (b.hook || "").toLowerCase().includes(q);
      const matchGenre = (b.genre || "").toLowerCase().includes(q);
      if (matchTitle || matchAuthor || matchHook || matchGenre) {
        const id = b.id || b.title;
        if (!seen.has(id)) {
          seen.add(id);
          results.push(b);
        }
      }
    }
  }
  return results;
}

export async function findBookById(bookId) {
  if (!bookId) return null;
  // 1. Search existing cached genres
  for (const books of genreCache.values()) {
    const found = books.find(b => b.id === bookId || b.title === bookId);
    if (found) return found;
  }
  // 2. If not found, fetch genres progressively
  for (const g of AUTHORITATIVE_GENRES) {
    const books = await fetchGenreBooks(g);
    const found = books.find(b => b.id === bookId || b.title === bookId);
    if (found) return found;
  }
  return null;
}
