# Usability & UX reference

## Nielsen Norman Group — 10 Usability Heuristics
(nngroup.com/articles/ten-usability-heuristics) — the baseline for every review.

1. **Visibility of system status** — the site always tells the user what's happening
   (loading states, form submission feedback, current nav location).
2. **Match between system and the real world** — plain language, familiar
   conventions, no internal jargon in labels or errors.
3. **User control and freedom** — clear "back"/"cancel", no forced flows, undo where
   destructive actions exist.
4. **Consistency and standards** — one visual language, one interaction pattern,
   across every page. Don't reinvent a control users already know.
5. **Error prevention** — confirm before destructive/irreversible actions; validate
   forms before submit, not just after.
6. **Recognition rather than recall** — don't make users remember information across
   screens; keep options and instructions visible.
7. **Flexibility and efficiency of use** — works for first-time and repeat visitors
   alike; don't force a novice-only flow.
8. **Aesthetic and minimalist design** — every element earns its place; remove
   anything not directly serving the primary action.
9. **Help users recognize, diagnose, and recover from errors** — plain-language
   error messages that state the problem and the fix, no raw error codes.
10. **Help and documentation** — findable when needed, but a well-designed site
    should need it rarely.

## Navigation & menu design
- 3–7 top-level items; group anything else under a footer or "more."
- Descriptive labels over clever/internal ones ("Pricing" not "Solutions").
- Conversion-critical pages (pricing, contact, book) live in primary nav, not buried.
- Menu position stays fixed across pages; ≤2 levels of dropdown nesting.
- Active section is visually marked; breadcrumbs on deep pages.
- Fully keyboard-operable (Tab/Enter/Arrows), announced correctly by screen readers.
- Mobile: hamburger or bottom nav, 44px+ tap targets, secondary links moved to footer.

## Accessibility
Full WCAG 2.1 AA checklist lives in `references/accessibility-wcag.md` — read
that before implementation and before any audit; it's the non-negotiable
accessibility standard for this skill, not a summary bullet list.

## Performance targets (part of UX, not separate from it)
- First Contentful Paint < 1.5s on 4G.
- Largest Contentful Paint < 2.5s.
- Time to Interactive < 3.5s on mid-tier devices.
- Measure with Lighthouse / PageSpeed Insights / WebPageTest before calling a build done.

## Content and trust signals
- Clear one-to-two-sentence value proposition on the homepage: what, for whom, why.
- Scannable structure: headings, short paragraphs, bullets — people scan before reading.
- Real contact info, real About content, no stock-photo-fake energy, no unfounded
  superlative claims ("best in class") without evidence.
- Keep content current — stale dates/news signal neglect.

Source distillation: Sinaida's Perplexity research guide
(`aliens-built-my-website/perplexity_guide.pdf`), cross-checked against NN/g's
published heuristics.
