# Anti-slop checklist

Source: [impeccable.style/slop](https://impeccable.style/slop/) — a catalog of
the visual/copy/motion tells that mark a site as AI-generated rather than
designed. Run this against every build before handoff, and against every audit
target. A site can pass every other checklist here and still read as generic
if it trips these.

## Visual design
- **No purple/violet gradients, no cyan-on-dark** — the single most recognizable
  AI-UI tell. If the brand palette genuinely calls for purple or cyan, use it as
  a flat color, not a gradient glow.
- No radial-gradient halos behind hero content "for atmosphere."
- No cream/beige page background chosen by default as the "tasteful neutral" —
  pick a background color for a reason tied to the brand, not because it's the
  safe option.
- No thick colored accent border on one side of a rounded card — the single most
  recognizable card-level tell. If a card needs emphasis, use weight, spacing, or
  a real shadow, not a stripe.
- No hairline border + wide soft shadow combo stacked together — pick one
  elevation technique, not both.
- No border-radius ≥24px that makes a card read as a blob rather than a
  rectangle with corners.
- No cards nested inside cards inside cards — flatten the hierarchy or use
  spacing/dividers instead.
- No repeating-gradient stripe patterns as decorative surface texture.
- No glassmorphism/blur used decoratively — blur is fine when it serves an actual
  focus/depth purpose (a modal backdrop), not as default surface treatment.

## Typography
- Font sizes must have real contrast between levels — if a heading and its body
  text are within a few px of each other, the hierarchy isn't working. Check
  against `references/fonts.md`'s stacks, but the *sizes* need deliberate jumps
  (e.g. a type scale, not arbitrary close values).
- Don't default to a single typeface for everything — a heading/body pairing (or
  a deliberate single-family choice with real weight/size contrast) reads as
  designed; a flat one-size-fits-all doesn't.
- Avoid italic serif display headlines as the default hero treatment — it's
  become a cliché "editorial" signal, not an actual editorial choice.
- Avoid tiny uppercase letter-spaced eyebrow labels above oversized headlines as
  a reflexive pattern — use them only when they carry real information
  (a category, a date), not as decoration.
- Watch for **Inter / Geist / Space Grotesk + Instrument Serif** specifically —
  not because they're bad fonts, but because that exact pairing has become the
  default "AI startup" look. If using one, make sure the rest of the page doesn't
  also match every other pattern on this list, or the font choice reads as more
  of the same.
- No all-caps for body text — kills readability, fine for short labels only.
- Letter spacing must stay at or above the legibility threshold; no crushed
  tracking on body text.
- Line height ≥1.3× font size for body text — no crushed line spacing.

## Layout & spacing
- Don't reach for the generic "hero → 3-up metric row → feature grid" template
  by default — that structure got cloned onto thousands of sites with only the
  color swapped. If it genuinely fits, fine, but choose it deliberately, not as
  the unexamined default.
- Icon-in-a-box + heading + one line of text, repeated identically for every
  feature card, is the single most overused content pattern — vary the treatment
  or justify why uniform repetition actually serves this content.
- Icons should never be visually larger than the heading/content they introduce.
- No tiny numbered section labels ("01 / 02 / 03") imitating editorial structure
  without an actual editorial reason for numbering.
- Spacing needs rhythm and variation appropriate to content grouping — not a
  single uniform gap value applied everywhere regardless of relationship between
  elements.
- Body text lines should wrap at roughly 60–80 characters for readability — not
  full-viewport-width paragraphs.
- Never let body text touch the viewport edge — always real padding/margin.
- No column stretching far past its neighbors leaving obviously dead space — if
  a grid has uneven content, fix the grid, don't leave a gap.
- Headings need real breathing room from the block above them — don't crowd a
  heading directly against the previous section's last line.

## Copy
- Ban generic buzzwords: "streamline," "empower," "supercharge," "world-class,"
  "enterprise-grade," and their close cousins — say what the thing actually does.
  This is consistent with Sinaida's own anti-voice rules already (no LinkedIn-speak,
  no "passionate about") — treat both as one standard, not two.
- Don't reflexively frame a competing idea as "theater" or dismiss it with a
  manufactured contrast ("this isn't X, it's Y") as a rhetorical crutch —
  Sinaida's own writing rules already ban the "A, not B" construction outright;
  this is the same tell showing up in web copy specifically.
- More than a couple of em-dashes in body copy reads as an AI cadence tell —
  restructure into separate sentences instead.
- No redundant repetition across a label, a subheader, and helper text all
  saying the same thing three ways — say it once, clearly.
- Never justify body text (full justification) — it creates uneven word spacing
  and hurts readability; left-align.

## Motion & animation
- No decorative pulsing status dot on content that isn't actually live/real-time.
- No fake blinking cursor on non-editable hero text.
- No auto-scrolling marquee demanding attention for content that doesn't need
  constant motion (logos, testimonials) — let it be static or user-controlled.
- No bounce/elastic easing on standard interface elements (buttons, menus) —
  reserve springy motion for moments that actually warrant delight, not as a
  default transition curve.
- Never animate `width`/`height`/`padding`/`margin` — animate `transform`/`opacity`
  instead, both for the layout-jank reason and because it's also a raw
  performance requirement (see `references/performance-adaptive.md`).
- Avoid reflexive image scale/rotate-on-hover as the default "interactive" tell
  for every image on a page.

## Imagery
- No generic shape-assembled SVG illustrations that read as stock/placeholder
  filler rather than actual content.
- No amateurish hand-coded SVG mascots/scenes unless that's a deliberate part of
  the brand's visual language (check with Sinaida — her own aesthetic runs
  toward cyberpunk/gothic/clinical, not cutesy SVG mascots, so this would almost
  always be a mismatch for her work specifically).
- No broken or missing image sources shipped to production — verify every asset
  resolves before handoff.

## Baseline content quality (these overlap with accessibility/security checks
elsewhere but restate here because they're also slop tells)
- No uncaught script errors on page load.
- No content left at `opacity: 0` at rest (a common animation-library mistake
  that leaves text invisible if JS fails or hasn't fired yet).
- Contrast must clear WCAG AA (4.5:1 body text) — already required in
  `references/ux-heuristics.md`, restated because low-contrast text is also a
  specific slop tell (the "washed out AI pastel" look).
- No skipped heading levels.
- Body text never below 12px.
- No excessively wide letter-spacing on body text that breaks up word/character
  grouping.

## How to use this during a build
Run through this list at the same point as the implementation checklist in
`SKILL.md` — after content is approved, during/after implementation, before
handoff. During an audit, treat repeated hits across multiple categories here
(not just one stray gradient) as a real finding, since it's the accumulation of
these patterns — not any single one — that makes a site read as generic AI
output rather than a designed site.
