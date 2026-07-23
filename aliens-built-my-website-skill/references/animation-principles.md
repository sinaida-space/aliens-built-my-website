# Animation principles for the web

Source: Disney's [Twelve Basic Principles of Animation](https://en.wikipedia.org/wiki/Twelve_basic_principles_of_animation)
(Frank Thomas & Ollie Johnston, *The Illusion of Life*). Every animation this
skill builds — micro-interactions, page transitions, hover states, and
**scroll-driven animation specifically** — is built against these, not against
whatever a CSS animation library defaults to. This is also a direct extension
of `references/anti-slop.md`: most of the motion tells cataloged there (bounce
easing on standard UI, fake cursors, decorative pulsing) are exactly what you
get from ignoring these principles and reaching for a library default instead.

## The twelve principles, translated to CSS/JS

1. **Squash and stretch** — an element keeps its perceived "volume": a button
   that scales on press should compress slightly on one axis and expand
   slightly on the other (`scaleX`/`scaleY` asymmetry), not scale uniformly
   like a static zoom. Use sparingly on real interface elements — this is
   about weight, not a bounce toy.
2. **Anticipation** — a state change reads better with a tiny counter-motion
   before the main motion (a card that will expand down first eases up 2-3px,
   then expands). On scroll: content entering can hold a beat at 0 velocity
   before accelerating in, rather than instantly matching scroll speed.
3. **Staging** — animate to direct attention, not to decorate. Only one thing
   should be animating to draw the eye at a time in a given viewport; if
   three elements fade/slide in simultaneously with no relationship, the
   viewer doesn't know where to look. Stage entrances with a clear reading
   order (see Timing below).
4. **Straight ahead vs. pose to pose** — for scroll-driven animation, prefer
   **pose to pose**: define the start state and end state (keyframes) tied to
   scroll progress via `IntersectionObserver` or `scroll-timeline`, and let the
   browser/GPU interpolate — don't hand-animate every intermediate frame with
   a scroll-position listener recalculating styles on every pixel (that's also
   a performance problem, see Timing/perf note below).
5. **Follow through and overlapping action** — when a container moves/appears,
   its children shouldn't all move in perfect lockstep. Stagger child
   transitions (e.g. 40-80ms delay increments across a list) so the motion
   reads as one thing settling into place, with looser elements (an icon, a
   badge) settling a beat after the main body. This is the single most
   effective principle for making a page feel "designed" instead of "CSS
   `transition: all 0.3s`" everywhere.
6. **Slow in and slow out** — never use `linear` easing for anything the user
   perceives as physical motion (entrances, exits, drags). Use easing curves
   with real acceleration/deceleration: `cubic-bezier(0.4, 0, 0.2, 1)`
   (standard "ease-in-out" feel) for most UI motion, `cubic-bezier(0, 0, 0.2, 1)`
   for things entering, `cubic-bezier(0.4, 0, 1, 1)` for things exiting.
   `linear` is only correct for continuous/looping motion (a spinner) where
   there's no start/stop to feel.
7. **Arcs** — natural motion curves; mechanical motion is straight. A card
   sliding into place should ease along a slight curve (combine a translateY
   and translateX/scale change) rather than a single-axis linear slide, unless
   the object being animated is meant to read as mechanical/rigid (e.g. a
   progress bar, a strict grid snap) — then a straight line is correct and
   intentional, not a shortcut.
8. **Secondary action** — small supporting motion that reinforces without
   competing: a hover state that both lifts a card *and* deepens its shadow,
   or a button press that both scales down *and* dims 5% — not a single
   isolated property change. Never let secondary action be louder than the
   primary action (see anti-slop's ban on decorative pulsing dots — that's
   secondary action with no primary action to support).
9. **Timing** — the number/duration of frames conveys weight and mood: fast
   duration reads as light/urgent (120-200ms for micro-interactions like
   hover/press), moderate duration reads as normal UI motion (200-400ms for
   panel/menu transitions), slow duration reads as deliberate/heavy (400-700ms,
   used rarely, for a hero moment). Never animate at a single blanket duration
   for every kind of motion on a site — that flatness is itself an anti-slop
   tell. On scroll specifically: tie timing to scroll *progress*, not wall-clock
   duration, so it never feels laggy relative to the user's actual scroll speed.
10. **Exaggeration** — a *little* overshoot on entrance (a card that settles
    1-2% past its final scale before easing back) reads as alive; this is the
    one principle to apply with the most restraint on a professional/clinical
    site — exaggerate by single-digit percentages and short overshoot windows,
    not a cartoonish bounce. Match the amount of exaggeration to the site's own
    aesthetic register (a gallery/portfolio site can push further than a
    utility/business tool).
11. **Solid drawing** — animated elements should keep believable weight and
    proportion through the motion: don't let a card's aspect ratio distort
    non-uniformly unless that's the deliberate squash/stretch; don't let text
    reflow/jump mid-transition (animate opacity/transform, not layout
    properties — this is also a hard performance requirement, see
    `references/performance-adaptive.md` and `references/anti-slop.md`'s ban
    on animating width/height/padding/margin).
12. **Appeal** — the motion should feel like it belongs to this specific site,
    not like a generic animation-library default applied uniformly. Match
    easing/timing/staging choices to the actual brand register (clinical/
    precise vs. playful vs. cinematic) rather than reaching for whatever a
    component library ships by default.

## Scroll-specific application (the part this skill treats as non-negotiable)

Any scroll-triggered animation on a site built or audited by this skill must:
- Use `IntersectionObserver` (or native `scroll-timeline`/`animation-timeline: view()`
  where supported, with an IO fallback) to trigger enter/exit states — never a
  raw `scroll` event handler recalculating inline styles on every tick.
- Respect **slow in/slow out** (principle 6) on the enter/exit transition itself.
- Respect **follow through** (principle 5) when multiple elements enter together
  — stagger them, don't fire simultaneously.
- Respect **staging** (principle 3) — no more than one scroll-triggered "moment"
  competing for attention within a single viewport at a time.
- Honor `prefers-reduced-motion` unconditionally — when set, scroll-triggered
  animation reduces to a simple opacity fade (or nothing) with no
  translate/scale motion, full stop, regardless of how good the fuller version
  looks (see `references/performance-adaptive.md`).
- Never block scroll or hijack scroll position (no scroll-jacking a native
  scrollbar to force a slower narrative pace) unless this is an explicitly
  commissioned art-direction piece and Sinaida has confirmed she wants that
  specific, unusual trade-off.
- Animate only `transform` and `opacity` — never properties that trigger
  layout/paint (`top`/`left`/`width`/`height`/`margin`) — for both the Solid
  Drawing principle above and the raw 60fps performance requirement.

## Where this fits in the workflow
- **Build mode**: apply this during implementation for every animated element,
  not as a later polish pass — it's cheaper to build staggered, eased motion
  from the start than to retrofit it onto a `transition: all` codebase.
- **Self-review**: re-check animated elements against these twelve principles
  specifically, in addition to `references/anti-slop.md`'s motion section.
- **Audit mode**: any scroll/hover/transition motion found on an audited site
  gets evaluated against this file; findings go into the audit PRD
  (`templates/audit-prd.md`) under category `Animation`, rated via
  `references/risk-matrix.md` like any other finding (usually Low/Medium impact
  unless the motion actively breaks usability or accessibility, e.g. ignoring
  `prefers-reduced-motion`, which is a Medium-to-High impact accessibility gap).
