# External design references — where to pull inspiration and components from

A curated list of sites for finding real, current design patterns instead of
inventing generic ones from training data. Use these **during the interview
and design-plan step** (offer 2–3 concrete reference options instead of
describing a direction in the abstract) and **during implementation** (pull
actual tokens/components/animation techniques, then adapt them to this site's
own `tokens.css` and voice — never ship a copy-pasted block unchanged).

Always disclose which site inspired a direction when presenting options to
Sinaida, and adapt rather than clone — a reference is a starting point, and
`references/anti-slop.md` still applies to whatever comes out the other end.

## Full design systems / component + token libraries
- [aura.build](https://www.aura.build/) — ready-made design systems, skills,
  templates. Can export whole HTML or pull design tokens individually.
- [neuform.ai](https://neuform.ai/) — full design systems and individual
  blocks, copy component-by-component.
- [21st.dev/community/components](https://21st.dev/community/components) —
  large library of frontend elements: individual blocks, buttons, animations.
- [component.gallery](http://component.gallery) — design systems from real
  products, organized by component type.
- [designmd.supply](https://www.designmd.supply/) — paste any site's URL, get
  back a `DESIGN.md` of its colors/fonts/spacing/components. Useful when a
  client says "make it like [existing site]" — generate the spec, then match
  the *system*, not a pixel-for-pixel copy (mind the copyright line in
  `## Copyright` at the top level — never reproduce another site's actual
  copy/branding, only its structural design language).
- [getdesign.md](https://getdesign.md/) — design systems from major brands.
  The "make it like Apple" reference point — extract the underlying system,
  don't clone the brand.

## Mobile / app screens
- [mobbin.com](https://mobbin.com/) — large archive of mobile design examples
  and full app flows. Good for onboarding, empty states, nav patterns beyond
  what a marketing site needs.

## Web design galleries by category
- [curated.design](http://curated.design) — general web design gallery.
- [landing.love](http://landing.love) — landing page patterns.
- [saaspo.com](http://saaspo.com) — SaaS marketing site patterns.
- [navbar.gallery](http://navbar.gallery) — navigation bar patterns.
- [cta.gallery](http://cta.gallery) — call-to-action section patterns.
- [rebrand.gallery](http://rebrand.gallery) — brand identity/rebrand case studies.
- [hugeicons.com](http://hugeicons.com) — icon sets.

## Animation and motion
- [appmotion.design](http://appmotion.design) — app motion-design reference
  reel. Cross-check anything pulled from here against
  `references/animation-principles.md` — a slick reference clip isn't
  automatically eased/staggered/reduced-motion-safe.
- [transitions.dev](https://transitions.dev/) — baseline web-app transition
  patterns.

## Effects and interactive primitives (use sparingly, opt-in only)
- [canvasui.dev](https://canvasui.dev/) — WebGL effects layered over live HTML.
- [beam.jakubantalik.com](https://beam.jakubantalik.com/) — animated glowing
  border effect.
- [metal.jakubantalik.com](https://metal.jakubantalik.com/) — liquid-metal
  button effect.
- [orbs.jakubantalik.com](https://orbs.jakubantalik.com/) — animated orb
  effects for AI-style interfaces.
- [originkit.dev](https://originkit.dev/) — free library of animated components.
- These are high-novelty/high-cost effects — treat like `references/glow-logo.md`:
  only pull one in if Sinaida explicitly wants that specific look, not by
  default for "make it beautiful." Check performance cost against
  `references/performance-adaptive.md` before shipping any WebGL/canvas effect.

## AI-agent-facing UI (relevant only if the site has a chat/agent interface)
- [aicss.dev](https://aicss.dev/) — UI components for AI chat interfaces.
- [beautiful-ui-five.vercel.app](https://beautiful-ui-five.vercel.app/) —
  primitives for AI interfaces.
- [agentation.com](https://agentation.com/) — UI markup/briefing conventions
  for agent-facing products.
- Only relevant if the build actually includes a chat/agent UI — most
  portfolio/gallery sites won't need this section at all.

## How to use these during a build
1. **Interview / design-plan step**: instead of describing a visual direction
   in the abstract, pull 2–3 concrete reference links from the categories
   above that match her stated priorities, present them via AskUserQuestion,
   and get a pick before implementing.
2. **Implementation**: extract tokens/components/animation timing from the
   chosen reference(s), translate into this site's own `tokens.css`
   (see the design-tokens checklist item in `SKILL.md`) — don't leave
   another site's class names, comments, or literal asset URLs in the code.
3. **Audit mode**: these aren't part of the audit checklist itself — they're
   a build-time input, not something to score an existing site against.


Sources: https://tochkicamp.ru/
