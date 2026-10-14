# Security checklist (non-negotiable baseline)

## Transport
- HTTPS everywhere, no HTTP fallback; redirect `http://` → `https://`.
- Valid, auto-renewing TLS cert (Let's Encrypt via host is usually sufficient);
  TLS 1.2/1.3 only.

## HTTP security headers (minimum set)
- `Strict-Transport-Security` (HSTS) — enforce HTTPS on repeat visits.
- `Content-Security-Policy` — restrict script/style/resource origins; avoid inline
  `<script>` where practical, or use nonces/hashes if unavoidable.
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy` — e.g. `strict-origin-when-cross-origin`.
- `X-Frame-Options: DENY` or CSP `frame-ancestors 'none'` — prevent clickjacking,
  unless the page must be embeddable.

## Auth & access (only relevant if the site has accounts/CMS/admin)
- Strong password policy + 2FA/passkeys for any admin or user account.
- Least privilege — no default-admin roles; scope editor/author roles narrowly.
- Rate-limit and lock out repeated failed logins; consider a non-default admin path.

## Input handling & code
- Validate and sanitize all input server-side; encode all output — never trust
  client-side validation alone.
- Parameterized queries only — never string-concatenate SQL.
- Keep CMS/plugins/dependencies current; remove anything unused.
- Subresource Integrity (SRI) hashes on any third-party CDN script.
- Never hardcode secrets/API keys in client-shipped code or in the repo — use env
  vars / a secrets manager, and confirm `.gitignore` covers them before any commit.

## Backups & monitoring
- Automated, off-site backups with a tested restore process (only relevant once
  there's dynamic content/a database to lose).
- Basic uptime/error monitoring; watch for anomalous traffic or failed-login spikes.

## Static-site note
Most builds from this skill are static HTML/CSS/JS with no backend — most of
"auth," "input handling," and "backups" sections are then N/A. Say so explicitly in
the self-review rather than silently skipping; don't invent backend security theater
for a site that has no backend.
