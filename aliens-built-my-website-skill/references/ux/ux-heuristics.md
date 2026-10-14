# Usability & UX reference

## Nielsen Norman Group — 10 Usability Heuristics
(nngroup.com/articles/ten-usability-heuristics) — the baseline for every review.

1. **Visibility of system status** — the site always tells the user what’s happening
   (loading states, form submission feedback, current nav location).
2. **Match between system and the real world** — plain language, familiar
   conventions, no internal jargon in labels or errors.
3. **User control and freedom** — clear “back”/“cancel”, no forced flows, undo where
   destructive actions exist.
4. **Consistency and standards** — one visual language, one interaction pattern,
   across every page. Don’t reinvent a control users already know.
5. **Error prevention** — confirm before destructive/irreversible actions; validate
   forms before submit, not just after.
6. **Recognition rather than recall** — don’t make users remember information across
   screens; keep options and instructions visible.
7. **Flexibility and efficiency of use** — works for first-time and repeat visitors
   alike; don’t force a novice-only flow.
8. **Aesthetic and minimalist design** — every element earns its place; remove
   anything not directly serving the primary action.
9. **Help users recognize, diagnose, and recover from errors** — plain-language
   error messages that state the problem and the fix, no raw error codes.
10. **Help and documentation** — findable when needed, but a well-designed site
    should need it rarely.

## Navigation & menu design
- 3–7 top-level items; group anything else under a footer or “more.”
- Descriptive labels over clever/internal ones (“Pricing” not “Solutions”).
- Conversion-critical pages (pricing, contact, book) live in primary nav, not buried.
- Menu position stays fixed across pages; ≤2 levels of dropdown nesting.
- Active section is visually marked; breadcrumbs on deep pages.
- Fully keyboard-operable (Tab/Enter/Arrows), announced correctly by screen readers.
- Mobile: hamburger or bottom nav, 44px+ tap targets, secondary links moved to footer.

## Accessibility
Full WCAG 2.1 AA checklist lives in `references/compliance/accessibility-wcag.md` — read
that before implementation and before any audit; it’s the non-negotiable
accessibility standard for this skill, not a summary bullet list.

## Performance targets (part of UX, not separate from it)
- First Contentful Paint < 1.5s on 4G.
- Largest Contentful Paint < 2.5s.
- Time to Interactive < 3.5s on mid-tier devices.
- Measure with Lighthouse / PageSpeed Insights / WebPageTest before calling a build done.

## Content and trust signals
- Clear one-to-two-sentence value proposition on the homepage: what, for whom, why.
- Scannable structure: headings, short paragraphs, bullets — people scan before reading.
- Real contact info, real About content, no stock-photo-fake energy, no unfounded
  superlative claims (“best in class”) without evidence.
- Keep content current — stale dates/news signal neglect.

## Cognitive load — the working-memory rule

Humans hold **≤4 items** in working memory at once (Miller’s Law, revised by
Cowan 2001). At any single decision point on the site, count the distinct
options/actions/pieces of information a visitor must weigh simultaneously:

- ≤4 items — fine.
- 5–7 — pushing the limit; group or add progressive disclosure.
- 8+ — overloaded; visitors skip, misclick, or leave.

Applied to a marketing/portfolio site specifically:
- 1 primary action per screen/section, 1–2 secondary, rest in a menu.
- ≤5 top-level nav items (already covered above, same root cause).
- One reading path per article — gather related links at the end, don’t
  scatter them mid-flow.
- A gallery/portfolio index asks one decision at a time (which piece to
  open) — don’t stack filter, sort, and tag controls in front of that.

Quick 8-item scan for a finding, not just a vibe check: single focus, ≤4-item
chunking, related items visually grouped, clear hierarchy of what matters
most, one decision at a time, ≤4 visible options per decision point, no
requirement to remember info from a previous screen, complexity revealed
only when needed. 0–1 failures is fine; 2–3 is worth fixing soon; 4+ is a
real finding, not a nitpick.

## Persona pass (audit mode)

Before closing an audit, walk the primary conversion action (book a call,
buy, contact, view a case study) through 2–3 of these lenses and note
specific breaks — not “accessibility could be better,” but the exact element
that fails:

- **First-timer** — never seen this kind of site. Is the first action
  obvious within 5 seconds? Any icon-only nav with no label? Any jargon in a
  label or error?
- **Screen-reader / keyboard-only visitor** — can the entire primary flow
  (read hero → find nav → reach contact/booking) complete with Tab/Enter
  alone? Any meaning conveyed by color alone? Any custom component that
  breaks the reading order? (Full checklist: `references/compliance/accessibility-wcag.md`.)
- **Distracted mobile visitor** — one-handed, on the go, maybe interrupted
  mid-visit. Are primary actions reachable by thumb (bottom half of a
  mobile viewport)? Do touch targets meet 44×44px? Does the page stay usable
  on a throttled connection?
- **Impatient/skimming visitor** — will not read paragraphs. Is the value
  proposition legible from headings and the first screen alone, without
  reading body copy?

A finding here still goes through the normal audit pipeline: numbered,
rated via `references/compliance/risk-matrix.md`, written into `templates/audit-prd.md`
— this is a lens for finding gaps, not a separate report format.

Source distillation: Sinaida’s Perplexity research guide
(`assets/research/perplexity_guide.pdf`), cross-checked against NN/g's
published heuristics; cognitive-load and persona framing adapted from
[pbakaus/impeccable](https://github.com/pbakaus/impeccable)'s critique
methodology (checklist knowledge only — no code or scripts imported).
