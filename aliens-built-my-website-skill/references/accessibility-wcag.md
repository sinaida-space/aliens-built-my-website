# Accessibility — WCAG 2.1 AA

Source: [W3C WCAG 2.1](https://www.w3.org/TR/WCAG21/). **Level AA is the
compliance bar for every build and audit** — it's the level referenced by most
real-world legal requirements (ADA-adjacent case law, EN 301 549, most
procurement standards), so it's the right default rather than stopping at
minimum-viable Level A. Level AAA items are noted where worth adopting anyway;
this skill doesn't require full AAA by default since some AAA criteria involve
real trade-offs (e.g. sign-language interpretation for every video) that need
a business decision, not a blanket rule.

This supersedes the short "Accessibility baseline" note in
`references/ux-heuristics.md` — that file now points here for detail.

## Perceivable

**1.1.1 Text alternatives (A)** — every meaningful image has real `alt` text
describing its content/function; purely decorative images get `alt=""` (not a
missing attribute, an empty one — a screen reader still needs to know to skip it).

**1.2.x Time-based media (A/AA)** — any prerecorded video has captions (A) and
audio description or an equivalent text alternative (A); live video/audio gets
captions too (AA). If a build has no audio/video, say so explicitly rather than
silently skipping this section.

**1.3.1 Info and relationships (A)** — structure conveyed visually (headings,
lists, tables, form groupings) is also conveyed in the markup: real `<h1>`-`<h6>`,
real `<ul>`/`<ol>`, real `<label>`-to-`<input>` association, real `<table>` with
`<th>` — never a visual heading that's just bold text in a `<div>`.

**1.3.2 Meaningful sequence (A)** — DOM order matches visual reading order; CSS
`order`/absolute positioning never scrambles the order a screen reader or
keyboard-tab encounters content in.

**1.3.3 Sensory characteristics (A)** — instructions never rely only on shape,
color, or position ("click the green button," "see the box on the right") —
pair with text/label that works without seeing the layout.

**1.3.4 Orientation (AA)** — content works in both portrait and landscape;
never lock orientation unless the content is genuinely orientation-specific
(a piano-style widget).

**1.3.5 Identify input purpose (AA)** — common fields (name, email, phone,
address) use the matching `autocomplete` attribute (`autocomplete="email"` etc.)
so browsers/assistive tech can autofill correctly.

**1.4.1 Use of color (A)** — color is never the *only* signal (a red border
alone for a form error; a color-only distinction between visited/unvisited
links) — always pair with text, icon, or pattern.

**1.4.2 Audio control (A)** — any auto-playing audio over 3 seconds has a
visible pause/stop/volume control. Default: don't autoplay audio at all.

**1.4.3 Contrast minimum (AA)** — 4.5:1 for normal text, 3:1 for large text
(≥24px, or ≥19px bold). Check with an actual contrast tool against the real
rendered colors, not by eye.

**1.4.4 Resize text (AA)** — text scales to 200% via browser zoom without
losing content or functionality (no fixed-height containers that clip scaled
text, no horizontal scroll introduced).

**1.4.5 Images of text (AA)** — use real text, not a screenshot/image of text,
except logos or where the exact rendering is essential.

**1.4.10 Reflow (AA)** — content reflows cleanly at 320px width (portrait
mobile) without horizontal scroll or content loss — direct overlap with the
mobile-responsive requirements in `references/ux-heuristics.md` and
`references/seo-checklist.md`.

**1.4.11 Non-text contrast (AA)** — UI components (button borders, form
field outlines, focus indicators, icon-only controls) and meaningful graphics
need ≥3:1 contrast against adjacent colors, not just text.

**1.4.12 Text spacing (AA)** — no content/functionality breaks if a user
overrides line-height to 1.5×, paragraph spacing to 2×, letter-spacing to
0.12em, word-spacing to 0.16em — don't use fixed-height text containers that
would clip under these overrides.

**1.4.13 Content on hover/focus (AA)** — tooltips/popovers triggered by
hover/focus must be dismissible (Esc), hoverable (mouse can move onto the
popover without it disappearing), and persistent (doesn't vanish on its own
before the user's done with it).

## Operable

**2.1.1 Keyboard (A)** / **2.1.2 No keyboard trap (A)** — every interactive
element (nav, forms, custom widgets, modals) is fully operable via keyboard
alone, and focus can always move back out. This is already in the
implementation checklist in `SKILL.md`; this is the spec it's drawn from.

**2.1.4 Character key shortcuts (A)** — if the site defines a single-key
keyboard shortcut, it must be remappable, require a modifier, or only fire
while the relevant component has focus — never a bare single-key shortcut that
fires globally and can't be turned off (breaks speech-input and other AT users).

**2.2.1 Timing adjustable (A)** / **2.2.2 Pause, stop, hide (A)** — any time
limit (session timeout, auto-advancing carousel) can be extended/turned off,
and any auto-updating/moving/auto-playing content (carousels, marquees) has a
visible pause control. Cross-reference `references/anti-slop.md`'s ban on
auto-scrolling marquees — here it's also a hard accessibility requirement, not
just a style preference.

**2.3.1 Three flashes (A)** — nothing flashes more than 3×/second — relevant
to any generative/shader-driven visual content on Sinaida's own sites; check
any animated background against this explicitly, don't assume it's fine.

**2.4.1 Bypass blocks (A)** — a "skip to main content" link (visually hidden
until focused) as the first focusable element on every page.

**2.4.2 Page titled (A)** — every page has a real, unique, descriptive `<title>`
— overlaps directly with `references/seo-checklist.md`'s on-page basics.

**2.4.3 Focus order (A)** — tab order follows visual/reading order; never let
a CSS layout trick (grid/flex reordering) scramble it.

**2.4.4 Link purpose in context (A)** — link text describes its destination
on its own or with immediate surrounding context — never a bare "click here"
or "read more" with no surrounding label for what it leads to.

**2.4.5 Multiple ways (AA)** — more than one way to find a page (nav + search,
or nav + sitemap) once a site has enough pages that this is meaningful; N/A for
a true single-page site.

**2.4.6 Headings and labels (AA)** — headings and form labels describe their
actual content/purpose, not generic filler ("Section 1," "Input").

**2.4.7 Focus visible (AA)** — a visible focus indicator on every interactive
element, always — never `outline: none` without a real custom replacement.
Already in the implementation checklist; this is its source requirement.

**2.5.1 Pointer gestures (A)** / **2.5.4 Motion actuation (A)** — any
multi-touch or device-motion interaction (swipe, shake-to-undo) has a
single-pointer/UI-button equivalent, and motion-triggered functionality can be
disabled (relevant to any TouchDesigner-adjacent interactive/installation-style
web piece Sinaida builds).

**2.5.2 Pointer cancellation (A)** — pressing down doesn't commit an action;
the action fires on release (and can be aborted by dragging off the target
before release) — standard button/link behavior already does this correctly,
just don't override it with `mousedown`-triggered actions.

**2.5.3 Label in name (A)** — a button/link's accessible name contains its
visible text (don't set `aria-label="Submit form"` on a button that visually
says "Send") — voice-control users refer to controls by what they see.

**Target size — worth adopting even though it's AAA (2.5.5):** interactive
targets ≥44×44 CSS px with adequate spacing. Already required as a mobile
usability item in `references/ux-heuristics.md`; treat it as a real requirement
here too even though the WCAG level is technically AAA.

## Understandable

**3.1.1 Language of page (A)** — `<html lang="...">` set correctly (and
`lang` on any embedded passage in a different language) — matters directly for
Sinaida's Russian/English bilingual content.

**3.2.1 On focus (A)** / **3.2.2 On input (A)** — focusing or changing a form
field never triggers an unexpected context change (auto-submitting a form,
auto-navigating away) without the user initiating it or being warned first.

**3.2.3 Consistent navigation (AA)** / **3.2.4 Consistent identification (AA)**
— nav structure and repeated component patterns (icons, buttons) stay
consistent in order and meaning across every page — overlaps directly with
`references/ux-heuristics.md`'s NN/g consistency heuristic and menu-design rules.

**3.3.1 Error identification (A)** — form errors are described in text
(not just a red outline), identify which field, and state what's wrong.

**3.3.2 Labels or instructions (A)** — every input has a visible label or
clear instructions — never a placeholder-as-label with no real `<label>`
(placeholders disappear on input and aren't reliably announced).

**3.3.3 Error suggestion (AA)** — where feasible, tell the user how to fix the
error, not just that one exists ("Email must include @" not just "Invalid").

**3.3.4 Error prevention for legal/financial data (AA)** — anywhere a
submission has legal or financial consequence (checkout, contract-adjacent
form), the data is reviewable/reversible/confirmable before final submission.

## Robust

**4.1.1 Parsing (A)** — valid, well-formed HTML: no duplicate `id`s, properly
nested/closed tags. Run an HTML validator as part of the implementation
checklist, don't assume a framework guarantees this.

**4.1.2 Name, role, value (A)** — every custom interactive component (a
non-native dropdown, tab set, modal, accordion) exposes the correct ARIA
role/name/state so assistive tech can identify and operate it — or, preferably,
use the native HTML element instead of rebuilding one that already exists
(`<select>`, `<details>`, `<dialog>`) since native elements get this for free.

**4.1.3 Status messages (AA)** — dynamic status updates (a form submitted
successfully, a cart updated, a loading state resolved) are announced via
`aria-live`/`role="status"` without requiring focus to move there — relevant
to any AJAX-driven interaction (contact form submission, filtering).

## How this fits the workflow

- **Build mode**: this is the accessibility standard referenced by the
  implementation checklist in `SKILL.md` — treat it as equally non-negotiable
  as GDPR/security, not a nice-to-have.
- **Self-review**: check the build against this file's Level AA items
  specifically (not just the shorter summary in `references/ux-heuristics.md`).
- **Audit mode**: any WCAG gap becomes a numbered finding in the audit PRD
  under category `Accessibility`, rated via `references/risk-matrix.md`.
  Missing keyboard operability, missing alt text, and contrast failures are
  typically **High impact** (they fully block a class of users, and increasingly
  carry real legal exposure) — don't under-rate them as cosmetic.
