# Build-mode interview script

Ask each of these via **AskUserQuestion**, one topic per question, always with a
recommended option marked and reasoning in the description. Adapt wording to the
specific project, but don't skip the substance. Don't proceed to content drafting
until all of these have real answers (not defaults you invented).

1. **Reason to exist** — "Why does this need to be a website, specifically?"
   Options: sell a product/service, book appointments/gigs, build a portfolio/CV
   presence, host a specific project (e.g. an art piece), other. If the honest
   answer is "no clear reason," say that back to her before building anything.

2. **Primary outcome** — "What's the one thing success looks like for this site?"
   Options tailored to her context: get booked for a show/collab, sell a piece,
   get hired/contracted, grow an audience/following, other.

3. **Primary visitor & their one action** — "Who lands here, and what's the single
   thing they should do?" (e.g. "a gallery curator, and they should book a call" vs.
   "a fan, and they should follow on Instagram").

4. **Tech stack** — recommended: static HTML/CSS/JS (no build step, fastest, easiest
   to secure). Alternatives: Astro (component reuse across future sites), Next.js
   (only if server logic/auth/forms-with-backend are actually needed), or "you decide."

5. **Content readiness** — "Do you have copy and images ready, or should I draft
   placeholder copy for you to edit?" If drafting: never invent real facts (pricing,
   credentials, testimonials, dates) — mark unknowns as `[NEEDS CONTENT: ...]`.

6. **Priority ranking** — ask her to rank: aesthetic/beauty, load speed, SEO,
   conversion, accessibility. Use this as the tie-breaker later (e.g. a heavy hero
   animation vs. fast load time).

7. **Bloom/glow branding** — default no. Only proceed to `references/glow-logo.md`
   if she says yes here (or asked for it earlier in the conversation).

8. **GitHub workflow** — confirm scope for this session: new issue(s) to open, which
   branch to work from, whether this is a fresh feature or a fix to something already
   in flight. See `references/gh-workflow.md`.
