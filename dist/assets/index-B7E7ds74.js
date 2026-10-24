(function(){let e=document.createElement(`link`).relList;if(e&&e.supports&&e.supports(`modulepreload`))return;for(let e of document.querySelectorAll(`link[rel="modulepreload"]`))n(e);new MutationObserver(e=>{for(let t of e)if(t.type===`childList`)for(let e of t.addedNodes)e.tagName===`LINK`&&e.rel===`modulepreload`&&n(e)}).observe(document,{childList:!0,subtree:!0});function t(e){let t={};return e.integrity&&(t.integrity=e.integrity),e.referrerPolicy&&(t.referrerPolicy=e.referrerPolicy),t.credentials=e.crossOrigin===`use-credentials`?`include`:e.crossOrigin===`anonymous`?`omit`:`same-origin`,t}function n(e){if(e.ep)return;e.ep=!0;let n=t(e);fetch(e.href,n)}})();var e={ENTERED:`rabbit_entered`,SELECTED_GENRE:`rabbit_selected_genre`,SELECTED_GENRES:`rabbit_selected_genres`,ONBOARDING_INTERESTS:`rabbit_onboarding_interests`,SAVED:`rabbit_saved`,LIKED:`rabbit_likes_v101`,FOLLOWED:`rabbit_followed`,TASTE:`rabbit_taste_v101`};function t(e,t){try{let n=localStorage.getItem(e);return n?JSON.parse(n):t}catch{return t}}function n(e,t){try{localStorage.setItem(e,JSON.stringify(t))}catch{}}var r=new URLSearchParams(window.location.search).get(`genre`),i=localStorage.getItem(e.SELECTED_GENRE),a=t(e.SELECTED_GENRES,[]),o=t(e.ONBOARDING_INTERESTS,[]),s=r||i||(a.length?a[0]:`Self Discovery`),c=new Set(a.length?a:o.length?o:[s]),l={onboardingComplete:localStorage.getItem(e.ENTERED)===`true`,currentScreen:localStorage.getItem(e.ENTERED)===`true`?`home`:`welcome`,activeGenre:s,selectedGenres:c,mixMode:c.size>1,savedBookIds:new Set(t(e.SAVED,[])),likedBookIds:new Set(t(e.LIKED,[])),followedBookIds:new Set(t(e.FOLLOWED,[])),activeNavTab:`for-you`,activeReadingBook:null,readingOrigin:`home`,searchTerm:``,demoActivityNoticeDismissed:!1},u=new Set;function d(e){return u.add(e),()=>u.delete(e)}function f(e,t=null){u.forEach(n=>n(l,e,t))}function p(t=[]){l.onboardingComplete=!0,l.currentScreen=`home`,t.length>0&&(l.selectedGenres=new Set(t),l.activeGenre=t[0],l.mixMode=t.length>1);try{localStorage.setItem(e.ENTERED,`true`),localStorage.setItem(e.SELECTED_GENRE,l.activeGenre),n(e.SELECTED_GENRES,Array.from(l.selectedGenres)),n(e.ONBOARDING_INTERESTS,Array.from(l.selectedGenres))}catch{}w(),f(`ONBOARDING_COMPLETE`)}function m(){l.onboardingComplete=!1,l.currentScreen=`welcome`;try{localStorage.removeItem(e.ENTERED)}catch{}console.log(`[RABBIT TEST] Onboarding reset for testing. Saved and liked books preserved.`),f(`ONBOARDING_RESET`)}window.resetRabbitOnboarding=m;function h(e){l.currentScreen=e,f(`SCREEN_CHANGE`,e)}function g(t,r=!0){if(t){l.mixMode=!1,l.selectedGenres=new Set([t]),l.activeGenre=t,l.currentScreen=`home`,l.activeNavTab=`for-you`;try{localStorage.setItem(e.SELECTED_GENRE,t),n(e.SELECTED_GENRES,[t])}catch{}r&&w(),f(`GENRE_SWITCH`,t)}}function _(t){if(t){l.selectedGenres.has(t)?l.selectedGenres.size>1&&l.selectedGenres.delete(t):l.selectedGenres.add(t),l.mixMode=l.selectedGenres.size>1,l.activeGenre=Array.from(l.selectedGenres)[0],l.currentScreen=`home`;try{localStorage.setItem(e.SELECTED_GENRE,l.activeGenre),n(e.SELECTED_GENRES,Array.from(l.selectedGenres))}catch{}w(),f(`GENRE_TOGGLE`,t)}}function v(){l.mixMode=!1;let t=Array.from(l.selectedGenres)[0]||l.activeGenre||`Self Discovery`;l.selectedGenres=new Set([t]),l.activeGenre=t;try{localStorage.setItem(e.SELECTED_GENRE,t),n(e.SELECTED_GENRES,[t])}catch{}w(),f(`GENRE_RESET`,t)}function y(e){l.activeNavTab=e,e===`for-you`?l.currentScreen=`home`:e===`library`?l.currentScreen=`library`:e===`following`&&(l.currentScreen=`following`),f(`NAV_CHANGE`,e)}function b(t){let r=l.likedBookIds.has(t);r?l.likedBookIds.delete(t):l.likedBookIds.add(t),n(e.LIKED,Array.from(l.likedBookIds)),f(`LIKE_TOGGLE`,{bookId:t,isLiked:!r})}function x(t){let r=l.savedBookIds.has(t);r?l.savedBookIds.delete(t):l.savedBookIds.add(t),n(e.SAVED,Array.from(l.savedBookIds)),f(`SAVE_TOGGLE`,{bookId:t,isSaved:!r})}function S(e,t=`home`){l.activeReadingBook=e,l.readingOrigin=t,l.currentScreen=`reader`,w(),f(`READER_OPEN`,e)}function C(){l.activeReadingBook=null,l.currentScreen=l.readingOrigin||`home`,w(),f(`READER_CLOSE`)}function w(){try{let e=new URL(window.location.href);l.activeReadingBook?e.searchParams.set(`book`,l.activeReadingBook.id||l.activeReadingBook.title):(e.searchParams.delete(`book`),l.mixMode?e.searchParams.set(`genre`,Array.from(l.selectedGenres).join(`,`)):e.searchParams.set(`genre`,l.activeGenre)),history.replaceState({genre:l.activeGenre,genres:Array.from(l.selectedGenres),bookId:l.activeReadingBook?.id||null},``,e.toString())}catch{}}window.addEventListener(`popstate`,e=>{if(l.currentScreen===`reader`){C();return}let t=new URLSearchParams(window.location.search).get(`genre`);if(t){if(t.includes(`,`)){let e=t.split(`,`).map(e=>e.trim()).filter(Boolean);l.selectedGenres=new Set(e),l.activeGenre=e[0],l.mixMode=e.length>1,f(`GENRE_SWITCH`,l.activeGenre)}else g(t,!1)}});var T=[`Self Discovery`,`Fantasy`,`Romance`,`History`,`Science Fiction`,`The Human Mind`,`Philosophy`,`Mystery & Thriller`,`Horror`,`Biography & Memoir`,`Business & Money`,`Young Adult`,`Classics`,`Adventure`,`Science`,`True Crime`,`Politics & Society`,`Poetry`,`Literary Fiction`,`Self-Help`,`Historical Fiction`];function ee(e){return e&&String(e).toLowerCase().trim().replace(/&/g,`and`).replace(/[^a-z0-9]+/g,`-`).replace(/^-+|-+$/g,``)||`self-discovery`}function E(e){if(!e)return`Self Discovery`;let t=String(e).toLowerCase().trim();return t.includes(`self discovery`)||t.includes(`self-discovery`)?`Self Discovery`:t.includes(`self-help`)||t.includes(`self help`)||t.includes(`productivity`)?`Self-Help`:t.includes(`human mind`)||t===`the human mind`||t.includes(`psychology`)||t.includes(`neuroscience`)||t.includes(`behavior`)?`The Human Mind`:t.includes(`sci-fi`)||t.includes(`science fiction`)||t.includes(`space`)||t.includes(`technology`)||t.includes(`artificial intelligence`)?`Science Fiction`:t.includes(`fantasy`)||t.includes(`mythology`)?`Fantasy`:t.includes(`mystery`)||t.includes(`thriller`)||t.includes(`crime`)&&!t.includes(`true crime`)?`Mystery & Thriller`:t.includes(`true crime`)?`True Crime`:t.includes(`romance`)||t.includes(`relationship`)||t.includes(`love`)?`Romance`:t.includes(`horror`)?`Horror`:t.includes(`historical fiction`)?`Historical Fiction`:t.includes(`history`)||t.includes(`ancient`)?`History`:t.includes(`young adult`)||t.includes(`ya`)?`Young Adult`:t.includes(`classic`)?`Classics`:t.includes(`adventure`)||t.includes(`travel`)?`Adventure`:t.includes(`business`)||t.includes(`money`)||t.includes(`economic`)||t.includes(`entrepreneurship`)||t.includes(`leadership`)?`Business & Money`:t.includes(`science`)||t.includes(`environment`)||t.includes(`nature`)?`Science`:t.includes(`philosophy`)||t.includes(`ethics`)?`Philosophy`:t.includes(`biography`)||t.includes(`memoir`)?`Biography & Memoir`:t.includes(`politic`)||t.includes(`society`)||t.includes(`culture`)||t.includes(`sociology`)||t.includes(`feminism`)?`Politics & Society`:t.includes(`poetry`)?`Poetry`:t.includes(`literary`)||t.includes(`fiction`)?`Literary Fiction`:T.find(e=>e.toLowerCase()===t)||`Self Discovery`}var D=new Map,O=new Map;function k(e){let t=`/Rabbit./`;return`${t.endsWith(`/`)?t:t+`/`}data/genres/${e}.json`}async function A(e){let t=E(e),n=ee(t);if(D.has(n))return D.get(n);if(O.has(n))return O.get(n);let r=(async()=>{try{let e=k(n),t=await fetch(e);if(!t.ok)throw Error(`Failed to load genre data (${t.status}): ${e}`);let r=await t.json();return D.set(n,r),r}catch(e){if(console.warn(`[RABBIT CATALOG] Fallback loading for ${n}:`,e),typeof window<`u`&&window.RABBIT_GENRES_CATALOG){let e=Object.keys(window.RABBIT_GENRES_CATALOG).find(e=>e.toLowerCase()===t.toLowerCase());if(e&&window.RABBIT_GENRES_CATALOG[e]){let t=window.RABBIT_GENRES_CATALOG[e];return D.set(n,t),t}}return[]}finally{O.delete(n)}})();return O.set(n,r),r}async function j(e){let t=new Map,n=e.map(async e=>{let n=await A(e);t.set(E(e),n)});return await Promise.all(n),t}function M(e,t){let n=[];if(t.forEach(t=>{let r=E(t),i=e.get(r)||[];i.length>0&&n.push({genre:r,books:[...i],pointer:0})}),n.length===0)return[];if(n.length===1)return n[0].books;let r=[],i=new Set,a=0,o=0;for(;a<n.length&&r.length<80;){for(let e=0;e<n.length;e++){let t=n[e];if(t.pointer<t.books.length){let e=t.books[t.pointer++],n=e.id||e.title;i.has(n)||(i.add(n),r.push({...e,mixedGenreBadge:t.genre}))}else a++}o++}return r}function N(e){if(!e||e.trim().length<2)return[];let t=e.toLowerCase().trim(),n=[],r=new Set;for(let e of D.values())for(let i of e){let e=(i.title||``).toLowerCase().includes(t),a=(i.author||``).toLowerCase().includes(t),o=(i.hook||``).toLowerCase().includes(t),s=(i.genre||``).toLowerCase().includes(t);if(e||a||o||s){let e=i.id||i.title;r.has(e)||(r.add(e),n.push(i))}}return n}async function P(e){if(!e)return null;for(let t of D.values()){let n=t.find(t=>t.id===e||t.title===e);if(n)return n}for(let t of T){let n=(await A(t)).find(t=>t.id===e||t.title===e);if(n)return n}return null}function F(e,t){e.innerHTML=`
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
  `;let n=e.querySelector(`#rabbit-welcome-cta`);n&&(n.onclick=()=>{t()})}function I(e,t=[],n){let r=new Set(t.length?t:[`Self Discovery`]);function i(){e.innerHTML=`
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
            ${T.map(e=>{let t=r.has(e);return`
                <button type="button" 
                  class="chip ${t?`active`:``}" 
                  data-genre="${e}"
                  style="padding:10px 18px;font-size:14px;border-radius:24px;cursor:pointer;transition:all 0.18s ease;"
                >
                  ${t?`✓ `:``}${e}
                </button>
              `}).join(``)}
          </div>
        </div>

        <div class="sticky-cta" style="position:fixed;bottom:0;left:0;right:0;padding:20px;background:linear-gradient(to top, rgba(0,0,0,0.95) 70%, transparent);display:flex;justify-content:center;z-index:90;">
          <button type="button" class="primary" id="rabbit-confirm-interests-btn" style="width:100%;max-width:420px;padding:15px;font-size:16px;font-weight:700;border-radius:30px;cursor:pointer;">
            Enter the burrow (${r.size} ${r.size===1?`genre`:`genres`}) →
          </button>
        </div>
      </main>
    `,e.querySelectorAll(`#rabbit-onboarding-chips .chip`).forEach(e=>{e.onclick=()=>{let t=e.dataset.genre;r.has(t)?r.size>1&&r.delete(t):r.add(t),i()}});let t=e.querySelector(`#rabbit-confirm-interests-btn`);t&&(t.onclick=()=>{n(Array.from(r))});let a=e.querySelector(`#rabbit-skip-onboarding-btn`);a&&(a.onclick=()=>{n(Array.from(r))})}i()}function L(e=`for-you`){return`
    <nav class="rabbit-top-nav" id="rabbit-top-main-nav" aria-label="Main Navigation">
      <div class="rabbit-top-nav-inner">
        <button type="button" class="rabbit-top-nav-item ${e===`for-you`?`active`:``}" data-nav="for-you" aria-label="For You Feed">
          <svg class="rabbit-nav-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2L14.2 9.2L21.4 11.4L14.2 13.6L12 21L9.8 13.6L2.6 11.4L9.8 9.2L12 2Z"></path>
          </svg>
          <span>For You</span>
        </button>

        <button type="button" class="rabbit-top-nav-item ${e===`genres`?`active`:``}" data-nav="genres" aria-label="Browse Genres">
          <svg class="rabbit-nav-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon>
          </svg>
          <span>Genres</span>
        </button>

        <button type="button" class="rabbit-top-nav-item ${e===`library`?`active`:``}" data-nav="library" aria-label="My Saved Library">
          <svg class="rabbit-nav-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
          </svg>
          <span>My Library</span>
        </button>

        <button type="button" class="rabbit-top-nav-item ${e===`following`?`active`:``}" data-nav="following" aria-label="Following Books">
          <svg class="rabbit-nav-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
            <path d="M12 7.5a1.5 1.5 0 0 1 3 0c0 1.5-2.2 2.5-3 3.5-.8-1-3-2-3-3.5a1.5 1.5 0 0 1 3 0z" fill="currentColor"></path>
          </svg>
          <span>Following</span>
        </button>
      </div>
    </nav>
  `}function te(e,t){e.querySelectorAll(`.rabbit-top-nav-item`).forEach(e=>{e.onclick=()=>{let n=e.dataset.nav;if(n===`genres`){let e=document.querySelector(`.rabbit-genre-nav-bar`);e?(e.scrollIntoView({behavior:`smooth`,block:`center`}),e.classList.add(`rabbit-pulse-highlight`),setTimeout(()=>e.classList.remove(`rabbit-pulse-highlight`),1200)):h(`interests`)}else y(n),t&&t(n)}})}function ne(e=`for-you`,t){let n=document.createElement(`aside`);n.className=`rabbit-desktop-sidebar`,n.setAttribute(`aria-label`,`Desktop Navigation`),n.innerHTML=`
    <div class="sidebar-brand" style="padding:24px 20px 20px;border-bottom:1px solid rgba(255,255,255,0.08);">
      <div style="font-size:22px;font-weight:900;letter-spacing:1px;color:#fff;display:flex;align-items:center;gap:8px;">
        RABBIT <span style="color:var(--lilac);font-size:16px;">✦</span>
      </div>
      <p style="font-size:12px;color:var(--muted);margin:6px 0 0;">Ideas worth getting lost in</p>
    </div>

    <nav class="sidebar-links" style="padding:16px 12px;display:flex;flex-direction:column;gap:6px;">
      <button type="button" class="sidebar-link ${e===`for-you`?`active`:``}" data-nav="for-you">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L14.2 9.2L21.4 11.4L14.2 13.6L12 21L9.8 13.6L2.6 11.4L9.8 9.2L12 2Z"></path></svg>
        <span>For You Feed</span>
      </button>

      <button type="button" class="sidebar-link ${e===`library`?`active`:``}" data-nav="library">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
        <span>My Saved Library</span>
      </button>

      <button type="button" class="sidebar-link ${e===`following`?`active`:``}" data-nav="following">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
        <span>Following Books</span>
      </button>

      <button type="button" class="sidebar-link" id="rabbit-sidebar-reset-onboarding-btn" style="margin-top:20px;opacity:0.65;font-size:12px;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path></svg>
        <span>Reset Onboarding (Demo)</span>
      </button>
    </nav>
  `,n.querySelectorAll(`.sidebar-link[data-nav]`).forEach(e=>{e.onclick=()=>{let n=e.dataset.nav;y(n),t&&t(n)}});let r=n.querySelector(`#rabbit-sidebar-reset-onboarding-btn`);return r&&(r.onclick=()=>{m()}),n}function re(){let e=document.createElement(`aside`);e.className=`rabbit-desktop-context-pane`,e.setAttribute(`aria-label`,`Context & Rabbit Hole Stats`);let t=l.savedBookIds?l.savedBookIds.size:0,n=l.likedBooks?l.likedBooks.size:0,r=l.mixMode&&l.selectedGenres.size>1,i=Array.from(l.selectedGenres);return e.innerHTML=`
    <!-- Active Genre Status Card -->
    <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(188,166,255,0.18);border-radius:16px;padding:18px;">
      <div style="font-size:10px;font-weight:700;letter-spacing:1.5px;color:var(--lilac);text-transform:uppercase;margin-bottom:6px;">ACTIVE EXPLORATION</div>
      <div style="font-size:18px;font-weight:700;color:#fff;line-height:1.2;font-family:var(--reading-font);margin-bottom:8px;">${r?`${i.slice(0,3).join(` + `)}${i.length>3?` +${i.length-3}`:``} (Mix)`:l.activeGenre}</div>
      <p style="font-size:12px;color:var(--muted);line-height:1.5;margin:0;">
        ${r?`Naturally interleaved from your custom genre selection.`:`Landmark masterworks curated for depth and clarity.`}
      </p>
    </div>

    <!-- Rabbit Hole Stats -->
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:18px;">
      <div style="font-size:11px;font-weight:700;letter-spacing:1px;color:#d1d5db;margin-bottom:14px;display:flex;align-items:center;gap:6px;">
        <span>✦</span> RABBIT HOLE STATS
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
        <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.05);">
          <div style="font-size:20px;font-weight:800;color:var(--lilac);">1,050</div>
          <div style="font-size:11px;color:var(--muted);margin-top:2px;">Landmark Books</div>
        </div>
        <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.05);">
          <div style="font-size:20px;font-weight:800;color:var(--lilac);">21</div>
          <div style="font-size:11px;color:var(--muted);margin-top:2px;">Curated Genres</div>
        </div>
        <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.05);">
          <div style="font-size:20px;font-weight:800;color:#f472b6;">${n}</div>
          <div style="font-size:11px;color:var(--muted);margin-top:2px;">Liked Insights</div>
        </div>
        <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.05);">
          <div style="font-size:20px;font-weight:800;color:#c084fc;">${t}</div>
          <div style="font-size:11px;color:var(--muted);margin-top:2px;">Saved in Library</div>
        </div>
      </div>
    </div>

    <!-- Quick Genre Switcher -->
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:16px;padding:18px;">
      <div style="font-size:11px;font-weight:700;letter-spacing:1px;color:#d1d5db;margin-bottom:12px;">QUICK HOP</div>
      <div class="chips" id="rabbit-context-genre-chips" style="display:flex;flex-wrap:wrap;gap:6px;">
        ${T.map(e=>`
            <button type="button" 
              class="chip ${l.activeGenre===e?`active`:``}" 
              data-genre="${e}" 
              style="padding:5px 11px;font-size:11px;border-radius:16px;cursor:pointer;"
            >
              ${e}
            </button>
          `).join(``)}
      </div>
    </div>

    <!-- Inspiration Quote -->
    <div style="padding:14px;border-left:2px solid var(--lilac);background:rgba(188,166,255,0.05);border-radius:0 12px 12px 0;">
      <p style="font-family:var(--reading-font);font-style:italic;font-size:13px;line-height:1.6;color:#e5e7eb;margin:0 0 6px;">
        "Follow your curiosity wherever it leads. The deepest leverage comes from the books you didn't expect to read."
      </p>
      <span style="font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:1px;">— RABBIT EDITORIAL</span>
    </div>
  `,e.querySelectorAll(`#rabbit-context-genre-chips .chip`).forEach(e=>{e.onclick=()=>{let t=e.dataset.genre;g(t)}}),e}function ie(e){let t=0;for(let n=0;n<e.length;n++)t=(t<<5)-t+e.charCodeAt(n),t|=0;return Math.abs(t)}function ae(e){return e?28+ie(String(e))%453:42}function R(e){return ae(e)+ +!!l.likedBookIds.has(e)}function z(e){return l.likedBookIds.has(e)}function B(e,t,n){b(e);let r=l.likedBookIds.has(e),i=R(e);t&&(t.classList.toggle(`active`,r),t.setAttribute(`aria-pressed`,r?`true`:`false`)),n&&(n.textContent=i.toLocaleString(),n.style.transform=`scale(1.15)`,setTimeout(()=>{n.style.transform=`scale(1)`},180))}function V(){return`
    <span class="rabbit-demo-activity-badge" title="Demo engagement count for prototype demonstration" aria-label="Demo activity indicator">
      <span class="rabbit-demo-dot"></span> Demo activity
    </span>
  `}function H(e,t=2400){document.querySelectorAll(`.rabbit-toast`).forEach(e=>e.remove());let n=document.createElement(`div`);n.className=`rabbit-toast`,n.style.cssText=`
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
  `,n.innerHTML=`<span style="color:#d8b4fe;font-size:15px;">✦</span> ${e}`,document.body.appendChild(n),requestAnimationFrame(()=>{n.style.opacity=`1`,n.style.transform=`translateX(-50%) translateY(0)`}),setTimeout(()=>{n.style.opacity=`0`,n.style.transform=`translateX(-50%) translateY(10px)`,setTimeout(()=>n.remove(),260)},t)}function U(e){let t=window.location.origin+`/Rabbit./`,n=t.endsWith(`/`)?t:t+`/`,r=e.id||e.title;return`${n}?book=${encodeURIComponent(r)}`}async function W(e){if(!e)return;let t=U(e),n=`RABBIT: ${e.title}`,r=`${e.title} by ${e.author} — "${e.hook||e.description||`Ideas worth falling into.`}"`;if(navigator.share&&navigator.canShare&&navigator.canShare({title:n,text:r,url:t}))try{return await navigator.share({title:n,text:r,url:t}),{success:!0,method:`native`}}catch(e){if(e.name===`AbortError`)return{success:!1,method:`aborted`};console.warn(`[RABBIT SHARE] Native share error, falling back to clipboard:`,e)}let i=!1;if(navigator.clipboard&&navigator.clipboard.writeText)try{await navigator.clipboard.writeText(t),i=!0}catch(e){console.warn(`[RABBIT SHARE] navigator.clipboard failed, trying fallback textarea:`,e)}if(!i)try{let e=document.createElement(`textarea`);e.value=t,e.style.position=`fixed`,e.style.left=`-9999px`,e.style.top=`0`,document.body.appendChild(e),e.focus(),e.select();let n=document.execCommand(`copy`);e.remove(),n&&(i=!0)}catch(e){console.warn(`[RABBIT SHARE] execCommand fallback failed:`,e)}return i?(H(`Book discovery link copied to clipboard! ↗`),{success:!0,method:`clipboard`}):(H(`Link: `+t),{success:!1,method:`failed`})}function G(e,t,n={}){let r=n.isFirstSlot||!1,i=e.id||e.title,a=l.savedBookIds.has(i),o=z(i),s=R(i),c=document.createElement(`article`);c.className=r?`feature rabbit-first-slot-card`:`feedpost rabbit-expanded-post`,c.dataset.bookId=i,c.style.scrollSnapAlign=`start`;let u=e.cover_url||e.cover||`https://covers.openlibrary.org/b/id/8231998-M.jpg`,d=(e.mixedGenreBadge||e.genre||l.activeGenre||`Curiosity`).toUpperCase(),f=e.hook||e.landmark_hook||e.title,p=e.preview||e.editorial_preview||e.description||e.original_summary||`An original insight inspired by this landmark masterwork.`;c.innerHTML=`
    ${r?``:`
      <div class="top" style="display:flex;align-items:center;justify-content:space-between;padding:12px 20px 0;">
        <span class="muted" style="font-size:11px;letter-spacing:1px;font-weight:700;color:#9ca3af;">RABBIT DISCOVERY</span>
        <span style="font-size:13px;color:var(--lilac);font-weight:700;">✦</span>
      </div>
    `}

    <div class="postbody" style="padding:${r?`16px 0 24px`:`20px 20px 30px`};">
      <div class="postmeta" style="font-size:11px;font-weight:700;letter-spacing:1.2px;color:#a855f7;margin-bottom:12px;">
        ${d} · HOP ${String(t+1).padStart(2,`0`)}
      </div>

      <div class="bookrow" style="display:flex;gap:16px;align-items:flex-start;margin-bottom:14px;">
        <img class="cover" 
          src="${u}" 
          alt="Cover of ${e.title}" 
          loading="lazy" 
          decoding="async" 
          style="width:58px;height:86px;object-fit:cover;border-radius:6px;box-shadow:0 6px 16px rgba(0,0,0,0.5);flex-shrink:0;"
        >
        <div style="flex:1;min-width:0;">
          <h3 style="font-size:18px;margin:0 0 4px;font-weight:700;line-height:1.25;color:#f9fafb;">${e.title}</h3>
          <p style="font-size:13px;color:#9ca3af;margin:0 0 6px;">${e.author}</p>
          <span style="display:inline-block;padding:2px 8px;border-radius:12px;background:rgba(255,255,255,0.06);font-size:10px;font-weight:600;color:#d1d5db;">
            Landmark Work
          </span>
        </div>
      </div>

      <div class="eyebrow" style="color:var(--lilac);letter-spacing:1.5px;font-size:10px;font-weight:700;margin-top:10px;">THE CORE INSIGHT</div>
      <h2 style="font-size:21px;letter-spacing:-0.4px;line-height:1.28;margin:8px 0 14px;color:#ffffff;font-family:var(--reading-font);">
        ${f}
      </h2>

      <div class="insight teaser" style="font-size:14px;line-height:1.75;color:#d1d5db;margin-bottom:20px;white-space:pre-line;">
        ${p}
      </div>

      <!-- Action Bar with Real Share, Interactive Likes, Save, and Read More -->
      <div class="actions" style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding-top:10px;border-top:1px solid rgba(255,255,255,0.07);">
        <!-- Interactive Like Button with Live Counter -->
        <button type="button" 
          class="rabbit-action-btn rabbit-like-btn ${o?`active`:``}" 
          aria-label="Like insight" 
          aria-pressed="${o?`true`:`false`}"
          style="display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:20px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#e5e7eb;font-size:13px;cursor:pointer;transition:all 0.18s ease;"
        >
          <svg viewBox="0 0 24 24" class="rabbit-action-icon" style="width:16px;height:16px;fill:${o?`#ec4899`:`none`};stroke:${o?`#ec4899`:`currentColor`};stroke-width:2;">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
          <span class="rabbit-like-counter" style="font-weight:600;font-variant-numeric:tabular-nums;">${s.toLocaleString()}</span>
        </button>

        <!-- Save / Bookmark Button -->
        <button type="button" 
          class="rabbit-action-btn rabbit-save-btn ${a?`active`:``}" 
          aria-label="Save to My Library"
          aria-pressed="${a?`true`:`false`}"
          style="display:inline-flex;align-items:center;gap:6px;padding:8px 12px;border-radius:20px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#e5e7eb;font-size:13px;cursor:pointer;transition:all 0.18s ease;"
        >
          <svg viewBox="0 0 24 24" class="rabbit-action-icon" style="width:16px;height:16px;fill:${a?`#a855f7`:`none`};stroke:${a?`#a855f7`:`currentColor`};stroke-width:2;">
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
          </svg>
          <span style="font-size:12px;font-weight:500;">${a?`Saved`:`Save`}</span>
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
        ${V()}
        <span style="font-size:10px;color:#71717a;">Swipe for next discovery ↓</span>
      </div>
    </div>
  `;let m=c.querySelector(`.rabbit-like-btn`),h=c.querySelector(`.rabbit-like-counter`);m&&(m.onclick=e=>{e.stopPropagation(),B(i,m,h)});let g=c.querySelector(`.rabbit-save-btn`);g&&(g.onclick=e=>{e.stopPropagation(),x(i);let t=l.savedBookIds.has(i);g.classList.toggle(`active`,t),g.setAttribute(`aria-pressed`,t?`true`:`false`);let n=g.querySelector(`span`);n&&(n.textContent=t?`Saved`:`Save`);let r=g.querySelector(`svg`);r&&(r.style.fill=t?`#a855f7`:`none`,r.style.stroke=t?`#a855f7`:`currentColor`)});let _=c.querySelector(`.rabbit-share-btn`);_&&(_.onclick=t=>{t.stopPropagation(),W(e)});let v=c.querySelector(`.rabbit-readmore-btn`);return v&&n.onReadMore&&(v.onclick=t=>{t.stopPropagation(),n.onReadMore(e)}),c}async function K(e,t={}){let n=l.activeNavTab||`for-you`,r=l.mixMode&&l.selectedGenres.size>1,i=Array.from(l.selectedGenres),a=r?`${i.join(` + `).toUpperCase()} (MIXED FEED)`:l.activeGenre.toUpperCase();e.innerHTML=`
    <div class="page home-scroll" id="homeScroll">
      <section class="home-first">
        <header class="top" style="padding:14px 20px;display:flex;align-items:center;justify-content:space-between;">
          <div class="wordmark" aria-label="RABBIT">
            <span style="font-size:20px;font-weight:900;letter-spacing:1px;color:#fff;">RABBIT <span style="color:var(--lilac);">✦</span></span>
          </div>
          <button type="button" class="rabbit-menu-trigger" id="rabbit-onboarding-restart-trigger" title="Reset onboarding flow for testing" style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);padding:6px 12px;border-radius:20px;color:#9ca3af;font-size:11px;font-weight:600;cursor:pointer;">
            ↺ Reset Onboarding
          </button>
        </header>

        ${L(n)}

        <div class="home-body">
          <!-- Stories Carousel -->
          <div class="stories" id="rabbit-stories-rail" aria-label="Book Stories"></div>

          <div class="section" style="padding-top:4px;">
            <!-- Autocomplete Instant Search Form -->
            <form class="rabbit-library-search" id="rabbit-search-form" style="margin-bottom:12px;position:relative;display:flex;gap:6px;align-items:center;">
              <div style="position:relative;flex:1;">
                <input type="search" id="rabbit-search-input" placeholder="Search 1,050+ masterworks, authors, concepts…" aria-label="Search books" autocomplete="off" style="width:100%;box-sizing:border-box;padding:10px 14px;border-radius:24px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);color:#fff;font-size:14px;outline:none;">
                <div class="rabbit-search-autocomplete" id="rabbit-search-dropdown" style="display:none;position:absolute;top:100%;left:0;right:0;margin-top:6px;background:#131318;border:1px solid rgba(168,85,247,0.3);border-radius:14px;box-shadow:0 12px 30px rgba(0,0,0,0.8);z-index:999;max-height:320px;overflow-y:auto;padding:6px 0;"></div>
              </div>
              <button type="submit" class="primary" style="padding:9px 16px;border-radius:24px;cursor:pointer;flex-shrink:0;font-size:13px;font-weight:600;">Search ↗</button>
              <button type="button" id="rabbit-search-clear" style="display:none;padding:8px 12px;border-radius:20px;background:rgba(239,68,68,0.15);color:#fca5a5;border:1px solid rgba(239,68,68,0.3);font-size:12px;font-weight:600;cursor:pointer;flex-shrink:0;">✕ Clear</button>
            </form>

            <!-- Horizontal Genre Bar -->
            <div class="rabbit-genre-nav-bar" id="rabbit-genre-pill-bar" style="display:flex;overflow-x:auto;white-space:nowrap;gap:8px;padding:8px 0 16px;scrollbar-width:none;-webkit-overflow-scrolling:touch;align-items:center;"></div>

            <div class="section-head" style="margin-top:14px;display:flex;align-items:baseline;justify-content:space-between;">
              <h2 style="font-size:20px;margin:0;font-weight:700;">For your curiosity <span class="accent">✦</span></h2>
              <span class="muted" id="rabbit-active-genre-heading" style="font-size:11px;font-weight:700;letter-spacing:1px;color:#a855f7;">${a}</span>
            </div>

            <!-- First Book Slot -->
            <div class="rabbit-first-book-slot" id="rabbit-first-book-slot">
              <div class="feature" style="padding:40px 20px;text-align:center;">
                <div class="muted">Loading ${a} landmark works…</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Container for rest of the feed cards -->
      <div id="rabbit-cards-container"></div>
    </div>
  `,te(e,t=>{t===`library`?se(e):t===`following`?ce(e):K(e)});let o=e.querySelector(`#rabbit-onboarding-restart-trigger`);o&&(o.onclick=()=>{window.resetRabbitOnboarding()}),q(e.querySelector(`#rabbit-genre-pill-bar`)),oe(e),await J(e)}function q(e){if(e){if(e.replaceChildren(),l.mixMode&&l.selectedGenres.size>1){let t=document.createElement(`button`);t.type=`button`,t.className=`chip rabbit-mix-clear-chip`,t.style.cssText=`flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 14px;border-radius:20px;background:rgba(239,68,68,0.18);color:#fca5a5;border:1px solid rgba(239,68,68,0.4);font-weight:700;display:inline-flex;align-items:center;gap:5px;`,t.innerHTML=`<span>✕</span> Clear Mix (${l.selectedGenres.size})`,t.onclick=()=>{v()},e.appendChild(t)}else{let t=document.createElement(`button`);t.type=`button`,t.className=`chip rabbit-mix-toggle-chip`,t.style.cssText=`flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 12px;border-radius:20px;background:rgba(168,85,247,0.12);color:#d8b4fe;border:1px dashed rgba(168,85,247,0.45);font-weight:600;`,t.innerHTML=l.mixMode?`✓ Mixing Active`:`<span>+</span> Mix Genres`,t.onclick=()=>{l.mixMode=!l.mixMode,q(e)},e.appendChild(t)}T.forEach(t=>{let n=l.selectedGenres.has(t),r=document.createElement(`button`);r.type=`button`,r.className=`chip ${n?`active`:``}`,r.style.cssText=`flex-shrink:0;cursor:pointer;font-size:12px;padding:6px 14px;border-radius:20px;transition:all 0.18s ease;`,r.textContent=t,r.onclick=e=>{e.shiftKey||e.ctrlKey||e.metaKey||l.mixMode?_(t):g(t)},e.appendChild(r)})}}async function J(e){let t=l.mixMode&&l.selectedGenres.size>1,n=Array.from(l.selectedGenres),r=[];r=t?M(await j(n),n):await A(l.activeGenre);let i=e.querySelector(`#rabbit-stories-rail`);i&&(i.replaceChildren(),r.slice(0,24).forEach(e=>{if(!e.cover_url&&!e.cover)return;let t=document.createElement(`button`);t.type=`button`,t.className=`story`,t.innerHTML=`
        <img loading="lazy" decoding="async" src="${e.cover_url||e.cover}" alt="${e.title}">
        <span>${e.title}</span>
      `,t.onclick=()=>S(e,`home`),i.appendChild(t)}));let a=e.querySelector(`#rabbit-first-book-slot`);if(a&&r.length>0){a.replaceChildren();let e=G(r[0],0,{isFirstSlot:!0,onReadMore:e=>S(e,`home`)});a.appendChild(e)}let o=e.querySelector(`#rabbit-cards-container`);if(o&&(o.replaceChildren(),r.length>1)){let e=r.slice(1),t=document.createDocumentFragment();e.forEach((e,n)=>{let r=G(e,n+1,{isFirstSlot:!1,onReadMore:e=>S(e,`home`)});t.appendChild(r)}),o.appendChild(t)}}function oe(e){let t=e.querySelector(`#rabbit-search-form`),n=e.querySelector(`#rabbit-search-input`),r=e.querySelector(`#rabbit-search-dropdown`),i=e.querySelector(`#rabbit-search-clear`);if(!t||!n||!r)return;let a=null;n.oninput=()=>{let e=n.value.trim();i&&(i.style.display=e?`inline-block`:`none`),clearTimeout(a),e.length<2?(r.style.display=`none`,r.replaceChildren()):a=setTimeout(()=>{let t=N(e).slice(0,6);t.length===0?r.style.display=`none`:(r.replaceChildren(),t.forEach(e=>{let t=document.createElement(`div`);t.style.cssText=`display:flex;align-items:center;gap:10px;padding:8px 14px;cursor:pointer;border-bottom:1px solid rgba(255,255,255,0.04);`,t.innerHTML=`
          <img src="${e.cover_url||e.cover||``}" style="width:28px;height:40px;object-fit:cover;border-radius:4px;flex-shrink:0;">
          <div style="flex:1;min-width:0;">
            <div style="font-size:13px;font-weight:600;color:#f3f4f6;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${e.title}</div>
            <div style="font-size:11px;color:#9ca3af;">${e.author} · ${e.genre||`Landmark`}</div>
          </div>
        `,t.onclick=()=>{r.style.display=`none`,S(e,`home`)},r.appendChild(t)}),r.style.display=`block`)},180)},i&&(i.onclick=()=>{n.value=``,r.style.display=`none`,i.style.display=`none`,J(e)}),t.onsubmit=t=>{t.preventDefault(),r.style.display=`none`;let i=n.value.trim();if(!i)return;let a=N(i),o=e.querySelector(`#rabbit-active-genre-heading`);o&&(o.textContent=`SEARCH: "${i.toUpperCase()}" (${a.length})`);let s=e.querySelector(`#rabbit-cards-container`),c=e.querySelector(`#rabbit-first-book-slot`);a.length>0?(c&&(c.replaceChildren(),c.appendChild(G(a[0],0,{isFirstSlot:!0,onReadMore:e=>S(e,`home`)}))),s&&(s.replaceChildren(),a.length>1&&a.slice(1).forEach((e,t)=>{s.appendChild(G(e,t+1,{onReadMore:e=>S(e,`home`)}))}))):(c&&(c.innerHTML=`<div style="padding:40px;text-align:center;color:#9ca3af;">No masterworks matching "${i}" found in current cache.</div>`),s&&s.replaceChildren())},document.addEventListener(`click`,e=>{t.contains(e.target)||(r.style.display=`none`)})}async function se(e){if(!e.querySelector(`#homeScroll`))return;let t=e.querySelector(`#rabbit-cards-container`),n=e.querySelector(`#rabbit-first-book-slot`),r=e.querySelector(`#rabbit-active-genre-heading`);if(r&&(r.textContent=`MY LIBRARY (${l.savedBookIds.size})`),l.savedBookIds.size===0){if(n){n.innerHTML=`
        <div class="feedpost" style="padding:48px 24px;text-align:center;background:rgba(20,20,24,0.7);border-radius:18px;border:1px solid rgba(255,255,255,0.08);margin-top:20px;">
          <div style="font-size:36px;margin-bottom:14px;">📚</div>
          <h2 style="font-size:20px;color:#f3f4f6;margin-bottom:8px;">Your Library Burrow is Empty</h2>
          <p style="font-size:14px;color:#9ca3af;line-height:1.6;max-width:380px;margin:0 auto 20px;">
            Tap <strong style="color:#c4b5fd;">Save</strong> on any book insight card or reader overlay to preserve your favorite reads here.
          </p>
          <button type="button" class="primary" id="rabbit-library-explore-btn" style="padding:10px 20px;border-radius:24px;cursor:pointer;font-weight:600;">
            ✦ Explore Masterworks Feed
          </button>
        </div>
      `;let t=n.querySelector(`#rabbit-library-explore-btn`);t&&(t.onclick=()=>K(e))}t&&t.replaceChildren()}else{let e=[];for(let t of l.savedBookIds){let n=await findBookById(t);n&&e.push(n)}n&&e.length>0&&n.replaceChildren(G(e[0],0,{isFirstSlot:!0,onReadMore:e=>S(e,`home`)})),t&&e.length>1&&(t.replaceChildren(),e.slice(1).forEach((e,n)=>{t.appendChild(G(e,n+1,{onReadMore:e=>S(e,`home`)}))}))}}async function ce(e){let t=e.querySelector(`#rabbit-cards-container`),n=e.querySelector(`#rabbit-first-book-slot`),r=e.querySelector(`#rabbit-active-genre-heading`);if(r&&(r.textContent=`FOLLOWED BOOKS (${l.followedBookIds.size})`),l.followedBookIds.size===0){if(n){n.innerHTML=`
        <div class="feedpost" style="padding:48px 24px;text-align:center;background:rgba(20,20,24,0.7);border-radius:18px;border:1px solid rgba(255,255,255,0.08);margin-top:20px;">
          <div style="font-size:36px;margin-bottom:14px;">♥</div>
          <h2 style="font-size:20px;color:#f3f4f6;margin-bottom:8px;">No Followed Books Yet</h2>
          <p style="font-size:14px;color:#9ca3af;line-height:1.6;max-width:380px;margin:0 auto 20px;">
            Follow your favorite authors and landmark works to track future chapter releases and community conversations.
          </p>
          <button type="button" class="primary" id="rabbit-following-explore-btn" style="padding:10px 20px;border-radius:24px;cursor:pointer;font-weight:600;">
            ✦ Explore Masterworks Feed
          </button>
        </div>
      `;let t=n.querySelector(`#rabbit-following-explore-btn`);t&&(t.onclick=()=>K(e))}t&&t.replaceChildren()}}function le(e,t){let n=document.getElementById(`rabbit-reader-overlay`);n&&n.remove();let r=e.id||e.title,i=l.savedBookIds.has(r),a=z(r),o=R(r),s=e.cover_url||e.cover||`https://covers.openlibrary.org/b/id/8231998-M.jpg`,c=document.createElement(`div`);c.id=`rabbit-reader-overlay`,c.className=`rabbit-reader-overlay`,c.setAttribute(`role`,`dialog`),c.setAttribute(`aria-modal`,`true`),c.setAttribute(`aria-label`,`Reading ${e.title}`),c.style.cssText=`
    position: fixed;
    inset: 0;
    z-index: 9999;
    background: #09090b;
    overflow-y: auto;
    overscroll-behavior: contain;
    -webkit-overflow-scrolling: touch;
    display: flex;
    flex-direction: column;
  `;let u=e.hook||e.landmark_hook||e.title,d=e.preview||e.editorial_preview||e.description||`Explore the landmark ideas of this book.`,f=e.takeaway||`True mastery comes from understanding the underlying mental model, not from blindly copying external techniques. In ${e.title}, the highest leverage comes from cultivating deliberate awareness and small, consistent adjustments.`;c.innerHTML=`
    <header class="reader-header" style="position:sticky;top:0;background:rgba(9,9,11,0.92);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,0.08);padding:14px 20px;display:flex;align-items:center;justify-content:space-between;z-index:10;">
      <button type="button" class="back-btn" id="rabbit-reader-back-btn" style="background:none;border:none;color:#d8b4fe;font-size:14px;font-weight:700;display:inline-flex;align-items:center;gap:6px;cursor:pointer;">
        ← Back to your rabbit hole
      </button>

      <div class="reader-actions" style="display:flex;gap:8px;align-items:center;">
        <!-- Like -->
        <button type="button" class="rabbit-like-btn ${a?`active`:``}" id="rabbit-reader-like-btn" style="background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.1);padding:6px 12px;border-radius:18px;color:#fff;cursor:pointer;display:inline-flex;align-items:center;gap:5px;font-size:12px;">
          <svg viewBox="0 0 24 24" style="width:14px;height:14px;fill:${a?`#ec4899`:`none`};stroke:${a?`#ec4899`:`currentColor`};stroke-width:2;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          <span class="rabbit-like-counter">${o.toLocaleString()}</span>
        </button>

        <!-- Save -->
        <button type="button" class="rabbit-save-btn ${i?`active`:``}" id="rabbit-reader-save-btn" style="background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.1);padding:6px 12px;border-radius:18px;color:#fff;cursor:pointer;display:inline-flex;align-items:center;gap:5px;font-size:12px;">
          <svg viewBox="0 0 24 24" style="width:14px;height:14px;fill:${i?`#a855f7`:`none`};stroke:${i?`#a855f7`:`currentColor`};stroke-width:2;"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
          <span>${i?`Saved`:`Save`}</span>
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
        <img src="${s}" alt="${e.title}" style="width:68px;height:102px;object-fit:cover;border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,0.6);">
        <div>
          <div class="eyebrow" style="color:var(--lilac);font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:4px;">${(e.genre||`LANDMARK`).toUpperCase()} · ESSENTIAL CHAPTER</div>
          <h1 style="font-size:24px;font-weight:800;margin:0 0 6px;line-height:1.2;font-family:var(--reading-font);color:#f9fafb;">${e.title}</h1>
          <p style="font-size:14px;color:#9ca3af;margin:0;">By ${e.author}</p>
        </div>
      </div>

      <div class="hook-box" style="padding:18px 20px;border-radius:12px;background:rgba(168,85,247,0.08);border:1px solid rgba(168,85,247,0.22);margin-bottom:28px;">
        <div style="font-size:11px;font-weight:700;letter-spacing:1px;color:#c084fc;margin-bottom:6px;">THE CENTRAL CONVERSATION</div>
        <div style="font-size:17px;font-weight:600;line-height:1.45;color:#f3f4f6;">${u}</div>
      </div>

      <div class="prose" style="font-size:16px;line-height:1.85;color:#e5e7eb;font-family:var(--reading-font);margin-bottom:36px;white-space:pre-line;">
        ${d}

        Think about where this paradox manifests in your immediate environment. The value of deep reading is never passive retention of catchphrases; it is the calibration of your attention toward previously invisible leverage points.

        When you examine your daily decisions through this lens, the friction between what you consciously intend and what your habits actually deliver begins to dissolve. Small, thoughtful adjustments sustained over time generate outsized clarity.
      </div>

      <div class="takeaway-card" style="padding:22px;border-radius:14px;background:#131318;border-left:4px solid var(--lilac);margin-bottom:36px;">
        <div class="eyebrow" style="color:var(--lilac);font-size:11px;font-weight:700;letter-spacing:1px;margin-bottom:8px;">THE TAKEAWAY</div>
        <p style="font-size:15px;line-height:1.6;color:#f3f4f6;margin:0;">${f}</p>
      </div>

      <button type="button" class="primary" id="rabbit-reader-bottom-close" style="width:100%;padding:14px;border-radius:24px;font-size:15px;font-weight:700;cursor:pointer;margin-top:20px;">
        ← Back to your rabbit hole
      </button>
    </main>
  `,document.body.appendChild(c);let p=c.querySelector(`#rabbit-reader-back-btn`),m=c.querySelector(`#rabbit-reader-bottom-close`),h=()=>{c.remove(),t&&t()};p&&(p.onclick=h),m&&(m.onclick=h);let g=c.querySelector(`#rabbit-reader-like-btn`),_=c.querySelector(`.rabbit-like-counter`);g&&(g.onclick=()=>{B(r,g,_)});let v=c.querySelector(`#rabbit-reader-save-btn`);v&&(v.onclick=()=>{x(r);let e=l.savedBookIds.has(r);v.classList.toggle(`active`,e),v.querySelector(`span`).textContent=e?`Saved`:`Save`;let t=v.querySelector(`svg`);t&&(t.style.fill=e?`#a855f7`:`none`)});let y=c.querySelector(`#rabbit-reader-share-btn`);y&&(y.onclick=()=>{W(e)});let b=e=>{e.key===`Escape`&&(document.removeEventListener(`keydown`,b),h())};document.addEventListener(`keydown`,b)}var Y=document.getElementById(`app`);window.resetRabbitOnboarding=m;async function X(){try{let e=new URLSearchParams(window.location.search).get(`book`);if(e){console.log(`[RABBIT] Direct book route requested: ${e}`);let t=await P(e);if(t)return console.log(`[RABBIT] Found book for direct link:`,t.title),S(t,`direct`),!0}}catch(e){console.warn(`[RABBIT] Error resolving direct book route:`,e)}return!1}var Z=!1;async function Q(){if(!Z){Z=!0;try{let e=l.currentScreen,t=window.innerWidth>=1024;if(e===`welcome`)Y.replaceChildren(),F(Y,()=>{h(`interests`)});else if(e===`interests`)Y.replaceChildren(),I(Y,l.selectedGenres.size>0?Array.from(l.selectedGenres):[l.activeGenre],e=>{p(e)});else if(Y.replaceChildren(),t){let e=document.createElement(`div`);e.className=`rabbit-desktop-shell`;let t=ne(l.activeNavTab||`for-you`,e=>{Q()});e.appendChild(t);let n=document.createElement(`div`);n.className=`rabbit-desktop-feed-wrapper`,e.appendChild(n);let r=re();e.appendChild(r),Y.appendChild(e),await K(n)}else await K(Y);let n=l.activeReadingBook||l.activeBook;if(n)le(n,()=>{C()});else{let e=document.getElementById(`rabbit-reader-overlay`);e&&e.remove()}}catch(e){console.error(`[RABBIT] Render error:`,e)}finally{Z=!1}}}d(()=>{Q()});var $=null;window.addEventListener(`resize`,()=>{clearTimeout($),$=setTimeout(()=>{l.currentScreen===`home`&&Q()},150)});async function ue(){console.log(`[RABBIT] Modernized modular client initializing...`),await Q(),await X()}ue();
//# sourceMappingURL=index-B7E7ds74.js.map