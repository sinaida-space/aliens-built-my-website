# GitHub hygiene for site work synced to sinaida-space/aliens-built-my-website

Issues are the task manager; branches map to issues; PRs merge to main. Push in
batches, and confirm with Sinaida before every push to the shared repo — standard
practice, not specific distrust of this workflow.

## Issues as task list
- One issue per meaningful unit of work: a page, a feature (cookie banner, 404,
  audit-fix batch), or a bug. Title imperative ("Add cookie consent banner", not
  "Cookie banner").
- Label by category where useful: `content`, `design`, `security`, `gdpr`, `seo`,
  `bug`.
- Close an issue via its merging PR (`Closes #12` in the PR body) rather than
  closing manually — keeps the audit trail intact.

## Branches
- One branch per issue: `feature/<short-slug>` or `fix/<short-slug>`, e.g.
  `feature/cookie-consent-banner`, `fix/404-page-styling`.
- Never commit directly to `main` for anything beyond a trivial one-line fix — even
  solo, a PR gives a reviewable diff and a clean history.
- Rebase or merge `main` into the feature branch before opening the PR if it's gone
  stale, rather than letting conflicts pile up.

## PRs
- PR description: what changed, why, and a test-plan checklist (does it load, does
  the cookie banner block trackers pre-consent, does Lighthouse/axe pass).
- Reference the issue it closes.
- Squash-merge by default to keep `main` history readable, unless she wants full
  history preserved for a specific PR.

## Push discipline
- Batch related commits into one push rather than pushing after every file edit.
- Before any push: `git status`, review the diff, confirm nothing sensitive
  (API keys, `.env`, credentials) is staged, then ask Sinaida to confirm the push.
- Never force-push to `main`; only force-push a feature branch, and only after
  confirming she's not mid-review on it.
