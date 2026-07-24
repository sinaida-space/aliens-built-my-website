---
name: aliens-built-my-website
description: The superhero of webdesign skills — builds new websites and audits existing ones against one bar: does it have a real reason to exist, does it solve a business problem, is it beautiful, usable, secure, and GDPR-compliant. For "build me a website" requests, runs a content-approval interview before any implementation. For "check/audit my site" requests, runs the same skill in audit mode against the identical checklist. Use whenever Sinaida asks to build, design, redesign, or review a website, landing page, or web app.
---

# aliens-built-my-website — website builder & auditor

Two modes, one bar. **Build mode**: interview → approve content → implement.
**Audit mode**: run the same checklist against an existing site and deliver a
numbered, risk-rated report. Never skip the interview to jump straight to code,
and never ship a site missing privacy policy, cookie banner, or a styled 404 —
those are non-negotiable, not nice-to-haves.

## Operating principle: act like a top-tier consulting team, not a code generator

Every interaction — build or audit — should read like it came from a
first-rate advisory engagement (the standard a Big Four strategy/technology
practice holds itself to), not a chatbot spitting out a template:

- **Evidence-based, not opinion-based.** Every claim traces to a specific
  checklist item, a specific piece of observed evidence, or a named source
  (NN/g, gdpr.eu, a Core Web Vitals number) — never "this just feels off."
- **Structured deliverables.** Findings are numbered, rated, and documented in
  an actual saved file (see Audit mode below) — not just a conversational
  summary that vanishes when the chat scrolls.
- **Executive-first communication.** Lead with the one-line conclusion a
  decision-maker needs, then support it with detail underneath — never bury
  the headline finding in paragraph six.
- **Name what's working, not only what's broken.** A credible advisory
  engagement builds trust by being accurate about strengths, not just gaps.
- **The client decides, the consultant informs.** Rate and prioritize
  findings objectively (via `references/risk-matrix.md`), but never make the
  sequencing decision for her — present the picture, ask what she wants next.

## Files here

- `references/ux-heuristics.md` — Nielsen Norman Group's 10 usability heuristics
  ([nngroup.com/articles/ten-usability-heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/))
  plus navigation/menu and performance-adaptability guidance distilled from
  Sinaida's own Perplexity research guide (`aliens-built-my-website/perplexity_guide.pdf`).
  Read before content approval and before any audit.
- `references/security-checklist.md` — HTTPS/TLS, security headers, auth, input
  handling, backups. Non-negotiable baseline for every build and audit.
- `references/accessibility-wcag.md` — full WCAG 2.1 Level AA checklist
  ([w3.org/TR/WCAG21](https://www.w3.org/TR/WCAG21/)), organized by the four
  POUR principles, with practical implementation notes per success criterion.
  Non-negotiable baseline for every build and audit, same tier as security/GDPR.
- `references/gdpr-checklist.md` — cookie banner behavior, privacy policy required
  fields, consent logging. Read before writing `templates/privacy-policy.md` or
  `templates/cookie-banner.html`.
- `references/anti-slop.md` — catalog of AI-generated-web-design tells (purple
  gradients, thick-border cards, icon-in-a-box feature grids, buzzword copy,
  bounce easing, etc.) from [impeccable.style/slop](https://impeccable.style/slop/).
  Run this during implementation and again at self-review — a site can pass
  every other checklist here and still read as generic AI output if it trips these.
- `references/animation-principles.md` — Disney's Twelve Basic Principles of
  Animation, translated to CSS/JS and applied specifically to **scroll-driven
  animation**. Every animation this skill builds (hover, transition, scroll-
  triggered reveal) is built against this, not against a library default.
  Non-negotiable, same tier as accessibility/security — not a polish pass.
- `references/seo-checklist.md` — technical SEO checklist curated from the
  [claude-seo](https://github.com/AgriciDaniel/claude-seo) project's `seo-technical`
  and `seo` skills. **Checklist knowledge only** — no code, scripts, or MCP
  integrations were imported from that repo (see "On the SEO source" below).
- `references/fonts.md` — pre-vetted commercial-free, high-readability font
  stacks. Pick from here; don't introduce a new font without checking its license.
- `references/typography.md` — heading hierarchy, modular type scale, line-
  height/measure/vertical rhythm, and micro-typography (non-breaking spaces,
  curly quotes, en/em dashes, widow/orphan control). Non-negotiable, same tier
  as accessibility/security — every `h1`–`h3` on a site must read as one
  consistent "vibe," not size-adjusted per section by eye.
- `references/performance-adaptive.md` — how to build the fast/slow-network,
  low/high-GPU adaptive mode (a "light mode" that degrades gracefully).
- `references/gh-workflow.md` — issues-as-task-manager + branch hygiene for
  syncing work to `sinaida-space/aliens-built-my-website`.
- `references/glow-logo.md` — HDR glow/bloom logo technique. **Opt-in only** —
  read and apply this only if Sinaida explicitly asks for bloom/glow/HDR branding.
  Never apply by default, even in "make it beautiful" requests.
- `references/risk-matrix.md` — the Impact × Probability rating method every
  audit finding is scored against, and the combined-rating lookup table
  (Critical/High/Medium/Low/Minimal). Read before rating any audit finding.
- `templates/interview-questions.md` — the build-mode interview script.
- `templates/audit-checklist.md` — the raw checklist walked during an audit,
  organized by severity tier.
- `templates/audit-prd.md` — the actual audit **deliverable** format: executive
  summary, numbered findings (F-001, F-002, ...) each rated via
  `references/risk-matrix.md`, a sortable risk-summary table, and a "what's
  working" section. Always saved as a real file, never just chat output.
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
- [ ] Full WCAG 2.1 AA pass per `references/accessibility-wcag.md` — semantic
      HTML, heading hierarchy, keyboard navigation, visible focus, alt text,
      form labels/error identification, skip-to-content link, `lang` attribute,
      contrast (text and non-text), reflow at 320px — not just the short list.
- [ ] Menu: 3–7 top-level items, consistent placement, ≤2 levels of nesting, visible
      current-location state.
- [ ] Fonts from `references/fonts.md` only.
- [ ] Typography per `references/typography.md` — real modular type scale
      (not eyeballed pixel values), one consistent heading "vibe" across every
      section, correct line-height/measure, and micro-typography (non-breaking
      spaces on number+unit pairs and before trailing dashes/last words, curly
      quotes, en/em dashes, no widowed headings).
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
- [ ] `references/anti-slop.md` swept during implementation, not just at the end —
      it's cheaper to not write a thick-border card component than to unwind one.
- [ ] Every animation (hover, transition, scroll-triggered reveal) built against
      `references/animation-principles.md` from the start — eased not linear,
      staggered not simultaneous, `transform`/`opacity` only, `prefers-reduced-motion`
      honored unconditionally.

### 4. Self-review before handing back
Re-run `references/ux-heuristics.md`, `references/accessibility-wcag.md`,
`references/security-checklist.md`, `references/anti-slop.md`,
`references/typography.md`, and `references/animation-principles.md` as a
checklist against what was actually
built, not what was intended. Report any item skipped and why (e.g. "no
backend, so auth/backup items N/A").

### 5. Ship via GitHub properly
Follow `references/gh-workflow.md`: an issue per feature/page, a branch per issue,
PR back to main. Push in batches, and confirm with Sinaida before each push per
standard practice for a shared repo.

---

## AUDIT MODE

Deliver a consulting-grade, risk-rated report — not a checklist dump — and
always as a real saved document. Steps:

1. **Scope.** Fetch/inspect the site (WebFetch, or ask for a repo/local path if
   the tool can't reach it). Confirm what's in scope (whole site vs. specific
   pages/flows) if it's ambiguous.
2. **Walk the checklist.** Use `templates/audit-checklist.md` against
   `references/ux-heuristics.md`, `references/accessibility-wcag.md` (the full
   WCAG 2.1 AA pass, not just a contrast/alt-text spot check),
   `references/security-checklist.md`, `references/gdpr-checklist.md`,
   `references/seo-checklist.md`, `references/performance-adaptive.md`,
   `references/fonts.md` (license + readability), `references/typography.md`
   (heading hierarchy, type scale, micro-typography), `references/anti-slop.md`
   (treat repeated hits across categories, not one stray gradient, as a real
   finding), and `references/animation-principles.md` for any hover/
   transition/scroll motion found on the site — flag `prefers-reduced-motion`
   non-support as a Medium-to-High impact accessibility finding, not just a
   style note.
3. **Turn every real gap into a numbered finding.** Sequential IDs (F-001,
   F-002, ...) regardless of category. Rate each independently on Impact and
   Probability, then combine via `references/risk-matrix.md` — never assign an
   overall severity by eyeballing it.
4. **Write the deliverable.** Fill out `templates/audit-prd.md` in full —
   executive summary, methodology, sortable risk-summary table, one detailed
   write-up per finding, a "what's already working" section, and next-steps
   framing. Save it to `docs/audits/<site-slug>-audit-<YYYY-MM-DD>.md` in the
   site's repo/project if one exists, otherwise the current working directory.
   Tell her the file path.
5. **Present, then hand the decision back.** Summarize the executive summary
   and risk table in chat, and ask which findings (by number) she wants turned
   into fixes and in what order. The document exists as a standing artifact
   regardless of her answer — it's the record, not a disposable checklist.
6. **If she commissions fixes**, that becomes a build-mode pass scoped to the
   chosen findings (interview only needed for gaps that touch content/
   priorities, not for e.g. adding security headers).

## On the SEO source (claude-seo)

Before use, the `AgriciDaniel/claude-seo` repo was cloned and scanned for red flags
(remote-code-execution patterns, `shell=True`, `eval`/`exec`, curl-pipe-bash executed
automatically rather than as documented manual install steps, hook definitions).
Nothing found — its `hooks.json` only runs a bundled schema validator on file edits,
and the `curl | bash` strings are install *instructions* in docs, not auto-executed.
Even so, **only the checklist knowledge in `references/seo-checklist.md` was ported**
— no scripts, installers, hooks, or MCP integrations from that repo are used here.
Re-check if that repo changes materially before pulling more from it.
