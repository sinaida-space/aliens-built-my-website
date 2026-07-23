<!--
  Audit deliverable template. This is a real saved document, not just a chat
  summary — write the finished report to
  `docs/audits/<site-slug>-audit-<YYYY-MM-DD>.md` in the site's own repo/project
  if one exists, or the current working directory if it doesn't, and tell
  Sinaida the file path when done. The document exists regardless of what she
  decides to do about the findings — diagnosis and action are separate steps.
-->

# [Site name] — Website Audit
**Prepared for:** [Client/Sinaida] &nbsp;·&nbsp; **Date:** [DATE] &nbsp;·&nbsp; **Scope:** [URL(s) / repo audited]

## Executive summary
[2-4 sentences, written the way a top-tier consulting deliverable opens: what
was assessed, the overall posture in one line (e.g. "solid UX foundation,
critical GDPR gap, no immediate security exposure"), and the single most
consequential finding. A reader who stops here should know exactly what
matters most.]

## Methodology
Audited against this skill's standard checklists: Nielsen Norman Group's 10
usability heuristics, GDPR (cross-checked against gdpr.eu), the security
baseline, technical SEO, adaptive-performance strategy, font licensing, and the
anti-slop catalog. Each finding below is rated independently on **Impact** and
**Probability** and combined into one rating via `references/risk-matrix.md` —
see that file for the rating definitions.

## Risk summary

| # | Finding | Category | Impact | Probability | Rating |
|---|---|---|---|---|---|
| F-001 | [short title] | GDPR | High | High | **Critical** |
| F-002 | [short title] | Security | ... | ... | ... |
| ... | | | | | |

_(Sort this table by rating, most severe first — Critical, then High, then
Medium, Low, Minimal. This table is the one page a client reads if they read
nothing else.)_

## Findings in detail

### F-001 — [Short title]
- **Category:** [GDPR / Security / UX / SEO / Performance / Anti-slop / Animation / Content]
- **Impact:** [High/Medium/Low] — [one line why]
- **Probability:** [High/Medium/Low] — [one line why]
- **Rating:** [combined rating from the matrix]
- **Evidence:** [what was observed — a URL, a missing header, a screenshot
  description, a quote from the page]
- **Why it matters:** [plain-language consequence, no jargon]
- **Recommended remediation:** [what fixing it actually involves — described
  at solution level, not a full implementation spec unless she asks for one]

_(Repeat per finding, numbered sequentially F-001, F-002, ... regardless of
category — one continuous numbering scheme makes the findings referenceable
in follow-up conversation ("let's fix F-003 next").)_

## What's already working
[A short section naming what's solid — a real audit isn't only a list of
problems; name the things that would be a mistake to change.]

## Recommended next steps
[1-3 sentences framing options at the level a strategy consultant would: e.g.
"the Critical and High items are the ones I'd address before this site
represents you publicly; the Medium/Low items are worth a batched pass when
you have a slower week." Do not decide the sequencing for her — present the
picture, let her choose what happens next, and say so explicitly:]

**This is a diagnosis, not a work order — tell me which findings (by number)
you want turned into fixes, and in what order.**
