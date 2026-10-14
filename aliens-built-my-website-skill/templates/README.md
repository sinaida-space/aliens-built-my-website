# Templates — the actual deliverables and scripts this skill fills in

Unlike `references/` (knowledge to check against), these are files meant to
be copied, filled in with a specific site’s real content, and shipped —
or, for the two audit files, the actual format of the audit deliverable.

- **`interview-questions.md`** — the build-mode interview script (why does
  this need to be a site, what outcome, who’s visiting, tech stack, content
  status, priority ranking, glow/bloom opt-in).
- **`audit-checklist.md`** — the raw checklist walked during an audit,
  organized by severity tier.
- **`audit-prd.md`** — the audit **deliverable** format itself: executive
  summary, numbered findings (F-001, F-002,…) each rated via
  `references/compliance/risk-matrix.md`, a sortable risk-summary table, and
  a “what’s working” section. Always saved as a real file, never just chat
  output.
- **`privacy-policy.md`** — GDPR privacy policy template with placeholders,
  filled in with the site’s real facts before shipping (per
  `references/compliance/gdpr-checklist.md`) and linked from every page’s
  footer.
- **`cookie-banner.html`** — accessible, dark-pattern-free consent banner
  (vanilla HTML/CSS/JS, no dependencies, no tracking loaded before consent).
- **`404.md`** — how to design a site-styled 404 page — inherits the actual
  site’s visual language, not a generic error template.

## Why these are separate from `references/`

A reference file answers “does this meet the bar.” A template *is* something
that ships, or the exact shape of a report that ships. Mixing the two would
make it unclear which files in this skill get read for judgment versus
copied and edited.
