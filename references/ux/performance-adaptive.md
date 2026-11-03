# Adaptive / light-mode performance strategy

Goal: the same site should feel instant on fiber + a fast GPU, and still be usable
on a slow connection or a weak/integrated GPU — never just "slow for some people."

## Detect, don't assume
- `navigator.connection.effectiveType` / `saveData` (Network Information API,
  Chromium-based browsers) — when `effectiveType` is `'slow-2g'`/`'2g'` or
  `saveData` is true, serve the light path.
- `prefers-reduced-motion` media query — always honor it regardless of detected
  network/GPU; treat it as a hard requirement, not a performance nicety.
- Feature-detect GPU-heavy capability (e.g. WebGL context creation, or a quick
  `requestAnimationFrame` timing probe) before enabling particle systems, shader
  backgrounds, or heavy canvas/WebGL work — don't rely on network speed as a GPU proxy.
- No API is fully reliable/universal (Safari lacks Network Information API) — always
  pair detection with a manual "Lite mode" toggle the user can pick themselves.

## What the light path drops, in order
1. Heavy background video/animation → static image or CSS gradient.
2. WebGL/canvas/particle effects → disabled entirely, replaced with a static visual.
3. Custom webfonts → system font stack (`-apple-system, Segoe UI, Roboto, sans-serif`).
4. Non-critical JS (chat widgets, heavy analytics, embeds) → deferred or removed.
5. Large/hero images → served at reduced resolution (see below), never removed
   entirely — content parity matters more than a smaller diff.

## Always, on both paths
- Modern image formats (WebP/AVIF) with a fallback, `srcset`/`sizes` for responsive
  serving, lazy-loading below the fold.
- Critical CSS inlined, everything else deferred; JS split so nothing blocks first paint.
- Aggressive caching (`Cache-Control`, and a service worker only if the added
  complexity is justified by the site's actual repeat-visit pattern).
- Text-first: the page must be readable and navigable even if JS fails entirely.

## Implementation pattern
```js
const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
const prefersLite = localStorage.getItem('lite-mode') === '1';
const isSlow = conn && (conn.saveData || ['slow-2g', '2g'].includes(conn.effectiveType));
const liteMode = prefersLite || isSlow;
document.documentElement.classList.toggle('lite', liteMode);
```
Gate heavy features (WebGL init, animation start) behind `!document.documentElement.classList.contains('lite')`,
and always expose a visible toggle (e.g. a footer "Lite mode" switch) so the choice
isn't only ever made silently by a heuristic.
