# Motion craft — concrete values

`references/design/animation-principles.md` gives the *why* (Disney’s Twelve Principles).
This file gives the *numbers* — distilled from Emil Kowalski’s animation
philosophy ([animations.dev](https://animations.dev)) and Apple’s WWDC design
talks (*Designing Fluid Interfaces*, *The Details of UI Typography*). Use both
together: principles decide the shape of the motion, this file decides the
exact tokens. Never invent a curve or duration by eye when a table below
covers the case.

## 1. Should this animate at all? (the gate)

Run this before picking any value. Failing it means writing zero lines of
motion code — that’s a correct outcome, not a shortcut skipped.

| Frequency the user sees it | Verdict |
| --- | --- |
| 100+ times/day (keyboard shortcuts, command palette, core nav) | **No animation. Ever.** |
| Tens of times/day (hover states, list nav, frequent toggles) | Near-imperceptible only, or nothing |
| Occasional (modals, drawers, toasts, settings) | Standard animation |
| Rare / first-time (onboarding, empty states, success) | The delight budget lives here |

Name the purpose in one word before writing code: **feedback**, **spatial
consistency**, **state indication**, **preventing a jarring change**,
**explanation** (marketing/onboarding only), or **delight** (rare-tier only).
“It looks cool” is not a purpose — reject the animation.

Also check **function**: content the visitor is reading or acting on
(pricing, a form, body copy) should not move for style. Decoration belongs on
marketing/hero sections, not on data or text being read.

## 2. Pick the cheapest tool that works

| Need | Tool |
| --- | --- |
| Hover, press, color, a class/attribute toggle | CSS transition |
| Entry animation on mount, no JS state | CSS `@starting-style` |
| Predetermined motion that must stay smooth under load | CSS `@keyframes` animation (off main thread) |
| Programmatic control with CSS performance | WAAPI (`element.animate()`) |
| Springs, drag, gesture-driven, exit animations | A JS motion library (e.g. Motion/Framer Motion) |

Don’t add a motion library dependency for a fade.

## 3. Properties — GPU only

- Animate **`transform` and `opacity` only**. `width`/`height`/`margin`/
  `padding`/`top`/`left` trigger layout and paint on every frame.
  `clip-path` is the sanctioned exception (reveals, wipes). `height` is
  tolerated only for accordions, where no transform equivalent exists.
- **Never `scale(0)`.** Nothing in the real world appears from nothing —
  start from `scale(0.9–0.97)` + `opacity: 0`.
- **`transform-origin` at the trigger** for popovers/dropdowns/menus/
  tooltips, so they visibly grow out of what opened them. **Modals are
  exempt** — they aren’t anchored to a trigger, so they stay centered.
- Prefer `translate()` **percentages** (`translateY(100%)`, relative to the
  element’s own size) over hardcoded pixels.
- In JS motion libraries, use the full `transform` string, not `x`/`y`/
  `scale` shorthands — shorthands aren’t hardware-accelerated and drop
  frames when the page is busy.

## 4. Easing and duration tokens

Put these in `tokens.css` alongside color/spacing tokens — never approximate
a cubic-bezier by eye:

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);        /* entering / exiting */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);    /* moving on screen */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);     /* drawer / sheet feel */
```

| Situation | Easing |
| --- | --- |
| Entering or exiting | `--ease-out` |
| Moving / morphing on screen | `--ease-in-out` |
| Hover / color change | `ease` (built-in is fine here) |
| Constant motion (marquee, spinner, progress) | `linear` |
| Default when unsure | `--ease-out` |

**Never `ease-in` on a UI element** — it starts slow, delaying the exact
moment the visitor is watching. `ease-out` at 200ms reads as faster than
`ease-in` at 200ms even at equal duration.

| Element | Duration |
| --- | --- |
| Button press feedback | 100–160ms |
| Tooltips, small popovers | 125–200ms |
| Dropdowns, selects | 150–250ms |
| Modals, drawers | 200–500ms |
| Marketing / explanatory / hero moment | Can run longer |

**UI motion stays under 300ms.** A 180ms dropdown reads as responsive; a
400ms one reads as sluggish.

## 5. Springs (drag, gesture, “alive” elements)

Reach for a spring instead of a fixed duration when the motion is drag with
momentum, a gesture the visitor can interrupt or reverse, or a flick/throw.
Springs are interruptible and velocity-aware — a fixed-duration transition
can’t respond to new input mid-flight, a spring can.

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }              // Apple-style — easier to reason about
{ type: "spring", mass: 1, stiffness: 100, damping: 10 }    // physics-parameter form
```

Apple’s two designer-facing parameters (damping ratio + response time) map
onto this:

| Interaction | Damping | Response |
| --- | --- | --- |
| Move / reposition (no gesture momentum) | `1.0` (critically damped, no bounce) | `0.3–0.4` |
| Rotation | `0.8` | `0.4` |
| Drawer / sheet | `0.8` | `0.3` |

Default UI to `damping: 1.0` (no overshoot). Add bounce (`~0.8`, i.e.
`bounce: 0.1–0.3` in the duration+bounce API) **only when the gesture itself
carried momentum** — a flick, a throw, a drag release. Overshoot on a menu
that just faded in reads as a mistake; overshoot on a card the visitor just
flicked reads as physical.

When a gesture ends, hand the release velocity to the spring as its initial
velocity so there’s no visible seam between dragging and animating.

At a drag boundary, resist progressively instead of stopping hard
(rubber-banding):

```js
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot));
}
```

## 6. Interruption and exit

- **Transitions or springs, not keyframes**, for anything a visitor can
  trigger rapidly — toasts, toggles, anything fired twice in a second.
  Transitions/springs retarget from the current value; keyframes restart
  from zero and stutter under repeated triggers.
- **Exit the way it entered.** A toast that slides in from the bottom leaves
  through the bottom. Symmetric paths are what makes a dismiss feel obvious.
- **Asymmetric timing where the visitor is deciding, symmetric where the
  system is responding.** A hold-to-confirm press can run slow and
  deliberate (2s linear fill); the release/response snaps (150–200ms
  `ease-out`).
- **Always animate from the live on-screen value**, never the logical target
  — reading the current computed transform before starting a new animation
  is what makes an interrupted animation feel continuous instead of jumpy.

## 7. Reduced motion and pointer gating — ships with the animation, not after

```css
@media (prefers-reduced-motion: reduce) {
  .element { transition: opacity 0.2s ease; transform: none !important; }
}

@media (hover: hover) and (pointer: fine) {
  .element:hover { transform: scale(1.05); } /* touch fires false hovers on tap */
}
```

Reduced motion means **fewer and gentler** animations, not zero — keep
opacity/color transitions that aid comprehension, drop translate/scale/
parallax movement. This is already required by
`references/design/animation-principles.md`; this section just gives the exact
media-query pattern.

## 8. Stagger, not simultaneous

Elements entering together (a card grid, a list, nav items) get a 30–80ms
delay increment between them — this is Disney’s “follow through” principle
(`animation-principles.md` #5) with a concrete number attached. Everything
firing at once is a top self-review flag.

## 9. Never ship — self-check before handing back

| Never | Instead |
| --- | --- |
| `transition: all` | Name the exact properties |
| `transform: scale(0)` entrance | `scale(0.95)` + `opacity: 0` |
| `ease-in` on a UI element | `--ease-out` or a custom curve |
| Built-in `ease-out` on a deliberate/marketing animation | `cubic-bezier(0.23, 1, 0.32, 1)` |
| Animation on a keyboard shortcut or 100+/day action | No animation |
| UI duration over 300ms with no stated reason | 150–250ms |
| `transform-origin: center` on a trigger-anchored popover | `var(--transform-origin)` at the trigger (modals exempt) |
| Keyframes on toasts/toggles/rapidly-triggered elements | Transitions or springs |
| Animating `width`/`height`/`margin`/`padding`/`top`/`left` | `transform` / `opacity` |
| Motion-library `x`/`y`/`scale` shorthand props | Full `transform` string |
| Ungated `:hover` motion | `@media (hover: hover) and (pointer: fine)` |
| Missing `prefers-reduced-motion` handling | Gentler variant, never zero if it aids comprehension |
| Everything entering at once | 30–80ms stagger |

## 10. Materials — translucent surfaces (nav bars, sheets, floating chrome)

If a site uses `backdrop-filter` for a sticky nav or floating panel:

- Content scrolls **under** the material; it isn’t an opaque bar consuming a
  fixed strip.
- Never stack a light translucent surface on another translucent surface —
  legibility collapses.
- Text over a blurred surface needs higher contrast and slightly heavier
  weight than the same text on solid background — flat gray text over glass
  under-reads. Put strong color on a solid layer, not the translucent
  foreground.
- Fade a small blur/gradient mask where floating chrome overlaps content,
  rather than a hard 1px border under a sticky header.

```css
.nav {
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid rgba(255, 255, 255, 0.4);
}
```

## 11. Typography motion detail — tracking and leading are size-specific

From Apple’s *The Details of UI Typography* — relevant alongside
`references/design/typography.md`'s modular scale:

- **Tracking (letter-spacing) is never one fixed value across all sizes.**
  Large display text wants slightly *negative* tracking (`-0.01em` to
  `-0.03em` as size grows); body text stays near `0`.
- **Leading tracks size inversely** — tight on large headings (`1.0–1.15`),
  looser on body copy (`1.5–1.7`, matching `references/design/typography.md`).

```css
.display {
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.05;
  letter-spacing: -0.02em;
}
```

## Where this fits in the workflow

- **Build mode**: every hover/transition/scroll-reveal gets run through the
  gate (§1) before any code is written, then built with the exact tokens
  from §4–§6. This is part of the same non-negotiable checklist item as
  `references/design/animation-principles.md`, not a separate optional pass.
- **Self-review / Audit mode**: run the Never Ship table (§9) as a literal
  grep-able checklist against the built or observed site. A hit on any row
  is a finding — rate via `references/compliance/risk-matrix.md` (usually Low/Medium,
  escalate to Medium/High if it’s a missing `prefers-reduced-motion` or a
  keyboard-shortcut animation, since those are accessibility/usability gaps
  not style notes).
