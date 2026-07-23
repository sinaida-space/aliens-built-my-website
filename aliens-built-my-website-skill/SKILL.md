---
name: aliens-built-my-website
description: The superhero of webdesign skills — builds new websites and audits existing ones against one bar: does it have a real reason to exist, does it solve a business problem, is it beautiful, usable, secure, and GDPR-compliant. For "build me a website" requests, runs a content-approval interview before any implementation. For "check/audit my site" requests, runs the same skill in audit mode against the identical checklist. Use whenever Sinaida asks to build, design, redesign, or review a website, landing page, or web app.
---

# aliens-built-my-website — website builder & auditor

Two modes, one bar. **Build mode**: interview → approve content → implement.
**Audit mode**: run the same checklist against an existing site and report gaps.
Never skip the interview to jump straight to code, and never ship a site missing
privacy policy, cookie banner, or a styled 404 — those are non-negotiable, not nice-to-haves.

## Files here

- `references/ux-heuristics.md` — Nielsen Norman Group's 10 usability heuristics
  ([nngroup.com/articles/ten-usability-heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/))
  plus navigation/menu and performance-adaptability guidance distilled from
  Sinaida's own Perplexity research guide (`aliens-built-my-website/perplexity_guide.pdf`).
  Read before content approval and before any audit.
- `references/security-checklist.md` — HTTPS/TLS, security headers, auth, input
  handling, backups. Non-negotiable baseline for every build and audit.
- `references/gdpr-checklist.md` — cookie banner behavior, privacy policy required
  fields, consent logging. Read before writing `templates/privacy-policy.md` or
  `templates/cookie-banner.html`.
- `references/seo-checklist.md` — technical SEO checklist curated from the
  [claude-seo](https://github.com/AgriciDaniel/claude-seo) project's `seo-technical`
  and `seo` skills. **Checklist knowledge only** — no code, scripts, or MCP
  integrations were imported from that repo (see "On the SEO source" below).
- `references/fonts.md` — pre-vetted commercial-free, high-readability font
  stacks. Pick from here; don't introduce a new font without checking its license.
- `references/performance-adaptive.md` — how to build the fast/slow-network,
  low/high-GPU adaptive mode (a "light mode" that degrades gracefully).
- `references/gh-workflow.md` — issues-as-task-manager + branch hygiene for
  syncing work to `sinaida-space/aliens-built-my-website`.
- `references/glow-logo.md` — HDR glow/bloom logo technique. **Opt-in only** —
  read and apply this only if Sinaida explicitly asks for bloom/glow/HDR branding.
  Never apply by default, even in "make it beautiful" requests.
- `templates/interview-questions.md` — the build-mode interview script.
- `templates/audit-checklist.md` — the audit-mode report format.
- `templates/privacy-policy.md` — GDPR privacy policy template with placeholders.
- `templates/cookie-banner.html` — accessible, dark-pattern-free consent banner
  (vanilla HTML/CSS/JS, no dependencies, no tracking loaded before consent).
- `templates/404.md` — how to design a site-styled 404 (not a generic template,
  since it must inherit each site's actual visual language).
- `scripts/hdr_glow.py` — implements the glow-logo technique. Only run this if
  Sinaida explicitly asked for glow/bloom branding this session.

## Mode detection

- "Build me a site / landing page / web app for X" → **Build mode**.
- "Check / audit / review my website at X" or "is my site compliant/secure/good" → **Audit mode**.
- Ambiguous ("what do you think of X") → ask which mode she wants via AskUserQuestion
  (Audit as the recommended option, since the site already exists).

---

## BUILD MODE

### 1. Interview first — always, no exceptions
Before writing a single line of code, run the interview in
`templates/interview-questions.md`. Ask through **AskUserQuestion**, one topic per
question, always with a recommended option marked. Core questions, adapt order/wording
to context but don't skip the substance:

1. **Why does this need to be a website at all** (vs. a landing page, a social profile,
   a PDF, nothing)? If there's no real answer, say so before building anything.
2. **What business/personal outcome does it serve** — sell something, book something,
   get hired, build an audience, host a portfolio? Pick the single primary outcome.
3. **Who is the visitor and what's the one action they should take?**
4. **Tech stack** — static HTML/CSS/JS (recommended default: no build step, fastest,
   easiest to secure/audit), Astro, Next.js, or "you decide based on what I described."
5. **Content status** — does she have copy/images ready, or does content need to be
   drafted as part of this? Never invent business facts (pricing, credentials,
   testimonials) — ask for them or mark them as `[NEEDS CONTENT]` placeholders.
6. **Priority ranking** for this specific build: beauty/aesthetic, speed, SEO,
   conversion, accessibility — ask her to rank so trade-offs (e.g. a hero video vs.
   fast load) have a clear tie-breaker.
7. **Bloom/glow branding?** — default is no; only proceed to `references/glow-logo.md`
   if she explicitly says yes here or elsewhere.

### 2. Content approval gate
Draft the actual page content (headlines, copy, structure, image/asset list) as
plain text/markdown first — no HTML, no styling. Present it and get explicit sign-off
("looks good" / edits requested) before touching implementation. This is the gate:
implementation does not start on unapproved content.

### 3. Implementation checklist (apply to every build, no matter how small)
- [ ] Semantic HTML, heading hierarchy, keyboard navigation, focus states, alt text —
      see `references/ux-heuristics.md` §Accessibility.
- [ ] Menu: 3–7 top-level items, consistent placement, ≤2 levels of nesting, visible
      current-location state.
- [ ] Fonts from `references/fonts.md` only.
- [ ] Adaptive/light mode per `references/performance-adaptive.md`.
- [ ] Security headers + HTTPS assumptions per `references/security-checklist.md`.
- [ ] `templates/cookie-banner.html` wired in, blocking non-essential
      scripts/cookies until consent, with Accept all / Reject all / Customize.
- [ ] `templates/privacy-policy.md` filled in with this site's real facts (never
      leave placeholder text live), and **linked from the footer of every page** —
      not buried a click deeper.
- [ ] A styled 404 page built per `templates/404.md` — must visually match the
      site, not a generic error page.
- [ ] SEO basics per `references/seo-checklist.md` (semantic structure, meta tags,
      sitemap, robots.txt).
- [ ] Glow-logo technique applied **only if explicitly requested this session**.

### 4. Self-review before handing back
Re-run `references/ux-heuristics.md` and `references/security-checklist.md` as a
checklist against what was actually built, not what was intended. Report any item
skipped and why (e.g. "no backend, so auth/backup items N/A").

### 5. Ship via GitHub properly
Follow `references/gh-workflow.md`: an issue per feature/page, a branch per issue,
PR back to main. Push in batches, and confirm with Sinaida before each push per
standard practice for a shared repo.

---

## AUDIT MODE

Run the identical checklist as build mode, but against the live site:

1. Fetch/inspect the site (WebFetch, or ask for a repo/local path if the tool can't
   reach it).
2. Walk `templates/audit-checklist.md`, checking off each item against
   `references/ux-heuristics.md`, `references/security-checklist.md`,
   `references/gdpr-checklist.md`, `references/seo-checklist.md`,
   `references/performance-adaptive.md`, and `references/fonts.md` (license + readability).
3. Report as: ✅ present / ⚠️ present but weak / ❌ missing, grouped by category,
   most severe first (missing privacy policy or cookie banner outranks a font choice).
4. Ask before fixing anything — audit is diagnosis, not an automatic rewrite. If she
   wants fixes, that becomes a build-mode pass on the specific gaps (interview only
   needed for gaps that touch content/priorities, not for e.g. adding security headers).

## On the SEO source (claude-seo)

Before use, the `AgriciDaniel/claude-seo` repo was cloned and scanned for red flags
(remote-code-execution patterns, `shell=True`, `eval`/`exec`, curl-pipe-bash executed
automatically rather than as documented manual install steps, hook definitions).
Nothing found — its `hooks.json` only runs a bundled schema validator on file edits,
and the `curl | bash` strings are install *instructions* in docs, not auto-executed.
Even so, **only the checklist knowledge in `references/seo-checklist.md` was ported**
— no scripts, installers, hooks, or MCP integrations from that repo are used here.
Re-check if that repo changes materially before pulling more from it.
