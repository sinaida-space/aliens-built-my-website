# Font stacks — commercial-license-free, high readability

Pick from this list rather than introducing a new font. All are free for
commercial use (OFL/Apache/similar) and chosen for screen readability, not just look.

## Sans, general UI / body text
- **Inter** — OFL. Built specifically for UI legibility at small sizes; excellent
  hinting on screens. Default choice for anything not explicitly needing character.
- **Public Sans** (US government's typeface, OFL) — extremely neutral, very high
  legibility, good if the brand voice is clinical/precise.
- **IBM Plex Sans** — OFL. Has real personality (geometric, slightly technical)
  without sacrificing readability; pairs well with a systems/engineering aesthetic.

## Monospace (for anything with a technical/clinical register)
- **JetBrains Mono** — OFL. High x-height, clear zero/O and 1/l/I disambiguation —
  matches the "clinical precision / ECG line" aesthetic well.
- **IBM Plex Mono** — OFL. Slightly warmer than JetBrains Mono, still highly legible.

## Serif (editorial / long-form reading)
- **Source Serif 4** — OFL. Designed for on-screen long-form reading, pairs with
  Source Sans if a serif/sans combo is wanted.
- **Lora** — OFL. Warmer, slightly calligraphic, still reads cleanly at body sizes.

## Display / headline-only (never for body text)
- **Space Grotesk** — OFL. Geometric, distinctive, good for large headlines only —
  legibility drops at small sizes, so restrict to ≥24px.

## Rules
- Always self-host (Google Fonts CDN or `@font-face` from local files) rather than
  a runtime third-party embed script — faster, no third-party tracking, one less
  CSP exception needed.
- Use `font-display: swap` so text renders in a fallback font while the webfont loads.
- Load only the weights actually used — don't pull in all 9 weights of a variable
  font if 2 are used.
- Before using any font not on this list, verify its license explicitly (OFL,
  Apache 2.0, or equivalent permissive + commercial-use-allowed) — don't assume.
