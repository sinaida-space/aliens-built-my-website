# Audit-mode report format

Report grouped by category, most severe first. Use ✅ present / ⚠️ present but weak
/ ❌ missing for each line. Missing privacy policy or cookie banner outranks a
suboptimal font choice — order the report by actual severity, not checklist order.

```
## [Site name] — aliens-built-my-website Audit

### Critical (legal/security exposure)
- [ ] GDPR: cookie banner present, blocks trackers pre-consent, offers
      Accept/Reject/Customize
- [ ] GDPR: privacy policy present and complete (9-point checklist)
- [ ] HTTPS enforced, valid cert
- [ ] Security headers present (CSP, HSTS, X-Content-Type-Options, Referrer-Policy)
- [ ] No exposed secrets/API keys in client-shipped code

### High (usability / trust / accessibility)
- [ ] Styled 404 page matching site's visual language
- [ ] NN/g 10 heuristics spot-check (status visibility, error prevention/recovery,
      consistency, aesthetic minimalism)
- [ ] WCAG 2.1 AA pass per `references/accessibility-wcag.md`: keyboard
      operability + no trap, focus visible, contrast (text 4.5:1, non-text 3:1),
      alt text, heading hierarchy, form labels + error identification, `lang`
      attribute, skip-to-content link, reflow at 320px
- [ ] Menu: 3–7 items, ≤2 nesting levels, consistent placement

### Medium (performance / reach)
- [ ] Core Web Vitals (LCP/INP/CLS) within target
- [ ] Adaptive/light mode for slow connections or weak GPUs
- [ ] Fonts: commercial-license-free, self-hosted, `font-display: swap`
- [ ] Technical SEO: sitemap, robots.txt, canonical tags, structured data

### Low (generic-AI-look tells — see references/anti-slop.md)
- [ ] Visual: no purple/violet gradients, cyan-on-dark, thick one-side card
      borders, or blob-radius cards
- [ ] Typography (`references/typography.md`): real modular size hierarchy
      (not eyeballed), one consistent heading "vibe" across every section, no
      italic-serif-hero-by-default, no crushed line-height/letter-spacing,
      non-breaking spaces on number+unit pairs and before trailing dashes/
      last words, curly quotes/en-em dashes, no widowed headings
- [ ] Layout: not the generic hero→3-metrics→icon-feature-grid template applied
      unexamined; no icon-in-a-box repeated identically across every card
- [ ] Copy: no buzzword filler (streamline/empower/supercharge/world-class), no
      "A, not B" construction, no excessive em-dashes
- [ ] Motion: no decorative pulsing dots/fake cursors/auto-marquees/bounce
      easing on standard UI

### Animation (see references/animation-principles.md — Disney's 12 principles)
- [ ] Easing: no `linear` on entrance/exit/hover motion; real acceleration/
      deceleration curves used
- [ ] Follow-through: multi-element entrances are staggered, not simultaneous
- [ ] Performance/Solid Drawing: only `transform`/`opacity` animated, never
      `width`/`height`/`margin`/`padding`/`top`/`left`
- [ ] `prefers-reduced-motion` honored on every scroll/hover/transition effect
      (flag missing support as Medium-High impact — it's an accessibility gap,
      not a style nitpick)
- [ ] Scroll-triggered effects use `IntersectionObserver`/`scroll-timeline`, not
      raw scroll-event style recalculation; no scroll-jacking

### Notes
[Anything genuinely N/A — say why, don't silently skip]
```

After presenting, ask whether she wants fixes now (routes to build mode for the
specific gaps) or just the diagnosis for now.
