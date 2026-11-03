# Design — the visual and motion craft bar

Where “beautiful” and “not generic AI output” get defined precisely enough
to build against and check against, instead of staying a vibe.

- **`anti-slop.md`** — catalog of AI-generated-web-design tells (purple
  gradients, thick-border cards, icon-in-a-box feature grids, buzzword copy,
  bounce easing) to avoid during implementation and catch at self-review.
- **`typography.md`** — heading hierarchy, modular type scale, line-height/
  measure/vertical rhythm, and micro-typography (non-breaking spaces, curly
  quotes, widow/orphan control).
- **`fonts.md`** — pre-vetted commercial-free, high-readability font stacks.
- **`animation-principles.md`** — Disney’s Twelve Basic Principles of
  Animation translated to CSS/JS, applied specifically to scroll-driven
  motion. The *why* and shape of every animation this skill builds.
- **`motion-craft.md`** — the concrete numbers that pair with the principles
  above: the “should this even animate” frequency gate, exact easing/
  duration tokens, spring configs, and a literal never-ship table (Emil
  Kowalski’s animation philosophy + Apple’s WWDC fluid-interfaces guidance).
- **`design-resources.md`** — curated external references (Aura, 21st.dev,
  Mobbin, designmd.supply, and others) for pulling real design directions
  and components instead of inventing generic ones.
- **`glow-logo.md`** — HDR glow/bloom logo technique. Opt-in only — read and
  apply only if explicitly requested, never by default.

## Why these two (“what to build” and “what to avoid”) sit together

Animation, typography, and fonts describe what *to* build; `anti-slop.md`
describes what *not* to build. Keeping both in one folder is deliberate —
they’re two halves of the same craft standard, checked at the same points in
the workflow (during implementation, and again at self-review/audit).
