# Typography — hierarchy, rhythm, and micro-typography

A site with clean layout and bad typography still reads as amateur. This is a
non-negotiable pass, same tier as accessibility/security — not a polish step
done "if there's time." Sources: [Butterick's Practical Typography](https://practicaltypography.com/),
Material Design's [type scale](https://m3.material.io/styles/typography/type-scale-tokens),
[MDN Typography guide](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals),
[Smashing Magazine — Building A Solid Typographic Hierarchy](https://www.smashingmagazine.com/2021/07/building-solid-typographic-hierarchy/),
and W3C WCAG 1.4.8 (visual presentation of text).

## 1. Heading hierarchy is structural, not decorative

- One `<h1>` per page. It states the page's subject, not the site name.
- Headings nest in order — never skip a level to get a size (`h2` → `h4`
  because `h3` "looked too small"). Fix the size in CSS, don't fake it in markup.
  This is a WCAG 1.3.1 (Info and Relationships) requirement, not a style choice.
- Every heading level gets a genuinely distinct size, weight, and (optionally)
  color/spacing treatment — not a 2px difference a visitor can't perceive.
  A reader should be able to tell `h2` from `h3` from across the room.
- All section headers on the same page share one "voice": same font, same
  weight, same case treatment (sentence case vs. ALL CAPS vs. Title Case —
  pick one and hold it), same relationship to the body text below it. Mixing
  treatments per-section is the single most common thing that makes a site
  feel unplanned.

## 2. Use a real type scale, not arbitrary pixel values

Pick a ratio and generate every size from it, rather than eyeballing each
heading individually. A modular scale keeps every section "vibe-matched"
because the math enforces it.

Common ratios (base 16px):

| Ratio | Name | h3 | h2 | h1 |
|---|---|---|---|---|
| 1.200 | Minor Third | 23px | 27px | 33px |
| 1.250 | Major Third | 25px | 31px | 39px |
| 1.333 | Perfect Fourth | 28px | 38px | 51px |
| 1.500 | Perfect Fifth | 36px | 54px | 81px |

- Editorial/content-dense sites (blogs, docs): 1.2–1.25 — keeps hierarchy calm.
- Marketing/portfolio/hero-driven sites: 1.333–1.5 — bigger jumps read as confident.
- Implement with CSS custom properties so the whole scale is one source of truth:

```css
:root {
  --step-0: 1rem;
  --step-1: 1.25rem;   /* h4 */
  --step-2: 1.563rem;  /* h3 */
  --step-3: 1.953rem;  /* h2 */
  --step-4: 2.441rem;  /* h1 */
  --step-5: 3.052rem;  /* hero display, used sparingly */
}
```

- Make the scale fluid with `clamp()` so headings don't need separate
  breakpoint overrides:

```css
h1 { font-size: clamp(2rem, 1.5rem + 2vw, 3.5rem); }
```

## 3. Line-height, measure, and spacing (vertical rhythm)

- **Body text line-height**: 1.4–1.6 (unitless, e.g. `line-height: 1.5`).
  Below 1.4 reads as cramped; matches the anti-slop rule against "crushed
  line-height" (`references/anti-slop.md`).
- **Heading line-height**: tighter than body, 1.1–1.3 — headings are short
  enough that generous leading just adds dead space.
- **Measure (line length)**: 45–75 characters per line for body text (66 is
  the commonly cited optimum). Constrain body copy with `max-width: 65ch`,
  not a raw pixel value — `ch` scales with the font actually in use.
- **Spacing before/after headings**: more space *above* a heading than
  *below* it (e.g. `margin-top: 2em; margin-bottom: 0.5em`). This visually
  groups a heading with the content it introduces rather than the content
  above it — a rule from classic print typography that still holds on screen.
- **Paragraph spacing**: pick one convention — margin between paragraphs
  *or* first-line indent — never both.

## 4. Font pairing and weight

- Maximum two typefaces per site: one for headings/UI, one for body — or a
  single variable font used across both via weight/size contrast alone.
  A third typeface needs a specific justification (e.g. a monospace for code).
- Use weight and size to create contrast, not more typefaces. A heading in
  700 and body in 400 of the *same* family is often cleaner than two families.
- Pick fonts from `references/fonts.md` — license and legibility already vetted.

## 5. Micro-typography — the details that separate "designed" from "typed"

These are cheap to get right and their absence is what makes text feel
machine-generated rather than composed.

- **Non-breaking spaces (`&nbsp;` or ` `)** — insert between elements
  that must never wrap onto separate lines:
  - Between a number and its unit: `100&nbsp;%`, `24&nbsp;px`, `10&nbsp;GB`.
  - Between a numeral and a following short word: `1&nbsp;day`, `Step&nbsp;3`.
  - Inside names/titles that read badly split: `Sinaida&nbsp;K.`, `Fig.&nbsp;3`.
  - Before a dash that introduces a clause, so the dash doesn't start a line:
    `the result&nbsp;— not the intention`.
  - Between the last two words of a heading or short line so a single word
    never orphans alone on the final line (a widow) — e.g.
    `We build for people,&nbsp;not funnels.`
  - Don't overuse it in long body paragraphs — reserve it for headings, short
    labels, and numeral/unit pairs where a bad break is visually obvious;
    forcing it everywhere fights the browser's normal reflow.
- **Real typographic characters, not their ASCII stand-ins**:
  - Curly quotes `“ ”` / `‘ ’` instead of straight `" '` (use the
    `quotes` CSS property or actual Unicode characters in copy, not
    `&quot;`-escaped straight quotes).
  - En dash `–` for ranges (`2020–2024`), em dash `—` for a parenthetical
    break — but per the skill's anti-slop rule, use em dashes sparingly, not
    as a tic.
  - Real ellipsis `…` (one character) instead of three periods `...`.
  - True multiplication sign `×` for dimensions (`1920×1080`), not a lowercase `x`.
  - Minus sign `−` (U+2212) for actual negative numbers in data displays,
    distinct from a hyphen.
- **Widows and orphans**: no heading or pull-quote should end with a single
  word alone on its last line. Fix with a non-breaking space between the
  last two words (see above), or `text-wrap: balance` (supported in modern
  Chromium/Firefox) for headings:

```css
h1, h2, h3 { text-wrap: balance; }
p { text-wrap: pretty; } /* where supported — orphan control for body text */
```

- **Hanging punctuation** for pull-quotes/blockquotes so opening quote marks
  sit outside the text block edge (`hanging-punctuation` where supported, or
  a negative-margin/`::before` trick as fallback).
- **Ordinal and fraction handling**: use `<sup>` sparingly and real fraction
  characters (`½`) where available rather than `1/2`, if the brand voice is
  precise/clinical (matches Sinaida's ECG/lab-note aesthetic).

## 6. Contrast and accessibility (ties to `references/accessibility-wcag.md`)

- Body text: 4.5:1 contrast minimum against its background (WCAG 1.4.3).
- Large text (24px+/19px+bold): 3:1 minimum.
- Never rely on color alone to distinguish a heading from body — size/weight
  must carry the hierarchy independently (WCAG 1.4.1).
- Respect `prefers-color-scheme` and `prefers-contrast` — don't hardcode a
  single palette that breaks in the user's OS-level high-contrast mode.
- Don't justify body text (`text-align: justify`) without hyphenation — it
  creates uneven "rivers" of whitespace that hurt readability (WCAG 1.4.8
  explicitly flags unjustified text as the accessible default).

## 7. Self-check before shipping

- [ ] Only one `<h1>`; heading levels never skip.
- [ ] Every heading level is visually distinct at a glance.
- [ ] All section headers across the page share one consistent treatment
      (font, weight, case, spacing) — no per-section drift.
- [ ] Sizes come from a defined scale/CSS variables, not ad hoc pixel values.
- [ ] Body line-height 1.4–1.6, measure ≤75ch.
- [ ] `&nbsp;` (or ` `) used between number+unit pairs, short label+numeral
      pairs, and before dashes/last-two-words of headings to prevent bad breaks.
- [ ] Curly quotes, en/em dashes, real ellipsis used instead of ASCII stand-ins.
- [ ] No orphaned single words on headings/pull-quotes (`text-wrap: balance`
      or manual `&nbsp;`).
- [ ] Contrast meets WCAG AA (4.5:1 body / 3:1 large text).
- [ ] Maximum two typefaces, both from `references/fonts.md`.
