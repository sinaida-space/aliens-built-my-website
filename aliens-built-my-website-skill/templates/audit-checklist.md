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

### High (usability / trust)
- [ ] Styled 404 page matching site's visual language
- [ ] NN/g 10 heuristics spot-check (status visibility, error prevention/recovery,
      consistency, aesthetic minimalism)
- [ ] Accessibility: contrast, keyboard nav, alt text, heading hierarchy
- [ ] Menu: 3–7 items, ≤2 nesting levels, consistent placement

### Medium (performance / reach)
- [ ] Core Web Vitals (LCP/INP/CLS) within target
- [ ] Adaptive/light mode for slow connections or weak GPUs
- [ ] Fonts: commercial-license-free, self-hosted, `font-display: swap`
- [ ] Technical SEO: sitemap, robots.txt, canonical tags, structured data

### Notes
[Anything genuinely N/A — say why, don't silently skip]
```

After presenting, ask whether she wants fixes now (routes to build mode for the
specific gaps) or just the diagnosis for now.
