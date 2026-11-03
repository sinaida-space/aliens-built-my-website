# External design references — where to pull inspiration and components from

A curated list of sites for finding real, current design patterns instead of
inventing generic ones from training data. Use these **during the interview
and design-plan step** (offer 2–3 concrete reference options instead of
describing a direction in the abstract) and **during implementation** (pull
actual tokens/components/animation techniques, then adapt them to this site's
own `tokens.css` and voice — never ship a copy-pasted block unchanged).

Always disclose which site inspired a direction when presenting options to
the user, and adapt rather than clone — a reference is a starting point, and
`references/design/anti-slop.md` still applies to whatever comes out the other end.

## Full design systems / component + token libraries
- [aura.build](https://www.aura.build/) — ready-made design systems, skills,
  templates. Can export whole HTML or pull design tokens individually.
- [neuform.ai](https://neuform.ai/) — full design systems and individual
  blocks, copy component-by-component.
- [21st.dev/community/components](https://21st.dev/community/components) —
  large library of frontend elements: individual blocks, buttons, animations.
- [magicui.design](https://magicui.design/) — animated UI building blocks
  (React + Tailwind + Motion), copy-in source.
- [obsidianui.dev](https://www.obsidianui.dev/) — free MIT React component
  library of animated, interactive components (buttons, menus, galleries).
  Full source files, so markup and styling are yours to adapt.
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
- [refero.design](https://styles.refero.design/) — full design.md examples for agents.

## Type and color
- [fontshare.com](https://www.fontshare.com/) — 100+ quality typefaces from
  Indian Type Foundry, free for commercial use.
- [realtimecolors.com](https://www.realtimecolors.com/) — try a palette and a
  font pairing on a live mock layout before committing them to `tokens.css`.
- [utopia.fyi](https://utopia.fyi/) — fluid type and space scales with
  `clamp()`, generated as CSS custom properties.

## Mobile / app screens
- [mobbin.com](https://mobbin.com/) — large archive of mobile design examples
  and full app flows. Good for onboarding, empty states, nav patterns beyond
  what a marketing site needs.

## Web design galleries by category
- [curated.design](http://curated.design) — general web design gallery.
- [land-book.com](https://land-book.com/) — large website design gallery.
- [inspora.design](https://inspora.design/) — web, branding and motion inspiration.
- [godly.website](https://godly.website/) — curated gallery of current web
  design, every entry shown as a live video.
- [inspomcp.dev](https://inspomcp.dev/) — archive of ~830 production sites
  (2,300+ screenshots) with design notes per site. Also an MCP server
  (`npx -y inspo-mcp install`) so the agent can pull real references directly.
- [landing.love](http://landing.love) — landing page patterns.
- [saaspo.com](http://saaspo.com) — SaaS marketing site patterns.
- [navbar.gallery](http://navbar.gallery) — navigation bar patterns.
- [cta.gallery](http://cta.gallery) — call-to-action section patterns.
- [footer.design](https://footer.design/) — footer patterns.
- [rebrand.gallery](http://rebrand.gallery) — brand identity/rebrand case studies.
- [hugeicons.com](http://hugeicons.com) — icon sets.
- [icons0.dev](https://icons0.dev/) — search across ~200k icons from 150 sets
  in one place instead of hunting per-library; one-command install.

## Award sites (current best-in-class work)
- [awwwards.com](https://www.awwwards.com/) — daily Site of the Day, juried
  by designers; filter by category, technology and color.
- [cssdesignawards.com](https://www.cssdesignawards.com/) — daily awards with
  separate UI, UX and innovation scores.
- [thefwa.com](https://thefwa.com/) — FWA, the long-running award for
  experimental and interactive work.
- [csswinner.com](https://www.csswinner.com/) — daily web design awards.
- Use these to see what the current top bar looks like and to name a
  concrete reference in the design plan, never as a source to copy from.

## Animation and motion
- [appmotion.design](http://appmotion.design) — app motion-design reference
  reel. Cross-check anything pulled from here against
  `references/design/animation-principles.md` — a slick reference clip isn't
  automatically eased/staggered/reduced-motion-safe.
- [transitions.dev](https://transitions.dev/) — baseline web-app transition
  patterns.
- [easings.net](https://easings.net/) — every standard easing curve shown
  moving, with the CSS to copy.
- [cubic-bezier.com](https://cubic-bezier.com/) — build and compare custom
  `cubic-bezier()` curves side by side.
- [kinetik.ink](https://kinetik.ink/) — smooth UI animation references.
- [60fps.design](https://60fps.design/) — mobile UI animation library.

## Effects and interactive primitives (use sparingly, opt-in only)
- [canvasui.dev](https://canvasui.dev/) — WebGL effects layered over live HTML.
- [beam.jakubantalik.com](https://beam.jakubantalik.com/) — animated glowing
  border effect.
- [metal.jakubantalik.com](https://metal.jakubantalik.com/) — liquid-metal
  button effect.
- [orbs.jakubantalik.com](https://orbs.jakubantalik.com/) — animated orb
  effects for AI-style interfaces.
- [originkit.dev](https://originkit.dev/) — free library of animated components.
- [shaders.com](https://shaders.com/) — open-source WebGPU shader components
  plus a free visual editor.
- [scrollshaders.com](https://scrollshaders.com/) — 117 animated shader
  backgrounds in 11 styles, as code, video or still; pause off screen.
- [webdev.teknium.io](https://webdev.teknium.io/) — Uncommon Web, a field
  guide to stylistically unusual web libraries.
- These are high-novelty/high-cost effects — treat like `references/design/glow-logo.md`:
  only pull one in if the user explicitly wants that specific look, not by
  default for "make it beautiful." Check performance cost against
  `references/ux/performance-adaptive.md` before shipping any WebGL/canvas effect.

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
