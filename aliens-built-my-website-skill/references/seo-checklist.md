# Technical SEO checklist

Curated from the `AgriciDaniel/claude-seo` project's `seo-technical` and `seo`
skills — checklist knowledge only, no scripts/code/MCP integrations imported
(see the security note in `SKILL.md`).

## Crawlability
- Valid `robots.txt` that doesn't accidentally block important paths.
- XML sitemap present and linked from `robots.txt`.
- Intentional vs accidental `noindex` — audit for the latter.
- Important pages reachable within 3 clicks of the homepage.
- Keep critical content and structured data within the first ~2MB of HTML —
  Googlebot only fetches that much per page.

## Indexability
- Self-referencing canonical tags, no conflicts with `noindex`.
- No near-duplicate content or unmanaged parameter URLs (`?utm=...`, `?sort=...`).
- Consistent `www` vs non-`www`, trailing-slash usage.

## URL structure
- Descriptive, hyphenated, human-readable paths — no query-string content URLs.
- Redirect chains capped at one hop; use 301 for permanent moves.
- Keep URLs under ~100 characters.

## Mobile / page experience
- Responsive layout, correct viewport meta tag, no horizontal scroll.
- Touch targets ≥48×48px with adequate spacing.
- Base font size ≥16px.
- Content parity between mobile and desktop — don't hide primary content behind
  interaction-only reveals on mobile.
- No intrusive interstitials or consent-redirect pages blocking content.

## Core Web Vitals (feeds ranking directly — treat as required, not aspirational)
- LCP ≤ 2.5s
- INP ≤ 200ms
- CLS ≤ 0.1

## Structured data
- JSON-LD (preferred over microdata/RDFa) for Organization/Person, WebSite, and
  any content type that has a matching schema.org type (Article, Event, Product).
- Validate against Google's supported structured-data types before shipping.

## On-page basics
- Unique, descriptive `<title>` and meta description per page.
- Semantic HTML: correct heading hierarchy, `<nav>`/`<main>`/`<footer>` landmarks.
- Descriptive alt text (also an accessibility requirement, not just SEO).

## AI crawlers (2025–2026 consideration)
- Decide deliberately whether to allow AI training/citation crawlers
  (`GPTBot`, `ClaudeBot`, `Google-Extended`, `PerplexityBot`, `Bytespider`) via
  `robots.txt` — blocking training crawlers doesn't block citation/browsing
  crawlers (e.g. blocking `GPTBot` doesn't block `ChatGPT-User`). For an artist's
  portfolio/personal-brand site, being cited by AI answers is usually a net
  positive for discovery — default to allowing unless she says otherwise.

## Security-adjacent SEO signals
- HTTPS is a confirmed (if lightweight) ranking signal — already required by
  `references/security-checklist.md`.
- Flag any script that hijacks the back button via `history.pushState`/`replaceState`
  abuse — a Google spam-policy violation, not just bad UX.
