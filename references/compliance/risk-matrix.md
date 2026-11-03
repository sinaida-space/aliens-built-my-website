# Risk matrix — Impact × Probability

Every audit finding gets rated on two axes, then combined into one overall
rating via the table below. This is the standard consulting risk-matrix method
(the kind a Big Four advisory team would hand a client) — rate independently,
then look up the combination, don't eyeball an overall severity directly.

## Impact — how bad is it if this issue plays out?
- **High** — legal/regulatory exposure (GDPR violation, missing consent),
  security breach potential, or material loss of business outcome (the primary
  conversion action is broken/inaccessible).
- **Medium** — meaningfully degrades trust, usability, or reach, but doesn't
  create legal exposure or block the primary conversion action outright.
- **Low** — polish-level; a real gap, but visitors can still achieve their goal
  and the business/legal exposure is negligible.

## Probability — how likely is this to actually cause harm?
- **High** — actively happening or near-certain (e.g. trackers already firing
  without consent on every visit; broken on the majority of real-world traffic
  like mobile).
- **Medium** — happens under common but not universal conditions (e.g. only
  affects slow connections, only affects one browser, only triggers on a
  specific user flow).
- **Low** — edge-case or requires unusual conditions to surface (e.g. only
  matters at a traffic/scale the site doesn't have yet).

## Combined rating lookup

| Impact ＼ Probability | Low | Medium | High |
|---|---|---|---|
| **High** | Medium | High | Critical |
| **Medium** | Low | Medium | High |
| **Low** | Minimal | Low | Medium |

## What each combined rating means for sequencing
- **Critical** — fix before anything else ships; treat as a stop-the-line issue.
- **High** — next sprint / next work session, not indefinitely deferred.
- **Medium** — planned work, batched with related fixes.
- **Low** — backlog; worth doing, not worth interrupting other work for.
- **Minimal** — note it, don't spend budget on it unless it's free to fix in
  passing.

Findings are rated, not triaged, by this skill. **Sequencing/prioritization
decisions belong to the client** — the rating informs her choice, it doesn't
make it for her.
