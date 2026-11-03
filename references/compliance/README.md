# Compliance — the non-negotiable baseline

What’s here has legal, regulatory, or user-trust consequences if skipped.
None of these trade off against beauty, speed, or a tight deadline — they’re
the same tier as each other, checked on every build and every audit, full
stop.

- **`accessibility-wcag.md`** — the full WCAG 2.1 Level AA checklist,
  organized by the four POUR principles (Perceivable, Operable,
  Understandable, Robust), with implementation notes per success criterion.
- **`security-checklist.md`** — HTTPS/TLS, security headers, auth, input
  handling, backups.
- **`gdpr-checklist.md`** — cookie banner behavior, privacy policy required
  fields, consent logging. Read alongside `templates/privacy-policy.md` and
  `templates/cookie-banner.html`.
- **`risk-matrix.md`** — the Impact × Probability method every audit finding
  gets rated against (Critical/High/Medium/Low/Minimal), so severity is
  never assigned by eyeballing it.
