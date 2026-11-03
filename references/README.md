# References — the knowledge this skill builds and audits against

Sixteen reference files, grouped into five folders by *what kind of bar they
enforce*, not by when they were written. Every file is read the same way in
both modes: build mode applies it during implementation, audit mode scores an
existing site against it. `SKILL.md` is the only file that decides *when*
each reference gets loaded — these folders exist so a human (or an agent
re-reading this repo cold) can find the right file without opening `SKILL.md`
first.

## Folders

- **`compliance/`** — the non-negotiables with legal or trust consequences if
  skipped: accessibility (WCAG 2.1 AA), security, GDPR, and the risk-rating
  method every audit finding is scored against. These are never optional,
  never “nice to have,” and never traded off against beauty or speed.
- **`design/`** — the visual and motion craft bar: what NOT to build
  (`anti-slop.md`), typography, fonts, animation (principles + concrete
  values), where to pull real design references from, and the opt-in glow-
  logo technique. This is where “beautiful” gets defined precisely enough to
  build and check against, instead of staying a vibe.
- **`growth/`** — how a site gets found and used by things that aren’t a
  human visitor: technical SEO and agentic-readiness (robots.txt AI-bot
  rules, `llms.txt`, MCP/agent-facing surfaces). Lower priority than
  compliance or design for a plain portfolio site, higher for anything with
  an API, booking flow, or storefront.
- **`ux/`** — usability and performance as experienced by a human visitor:
  Nielsen Norman Group’s heuristics, cognitive load, persona-based testing,
  and the adaptive/light-mode performance strategy.
- **`process/`** — how work actually ships: issue-per-feature, branch-per-
  issue, PR-back-to-main hygiene for this repo specifically.

## Why grouped this way

Each folder answers a different question a build or audit has to answer:
*is this legal and safe* (compliance), *is this actually good design*
(design), *can it be found and used by non-human visitors* (growth), *is it
usable by a human* (ux), *how does the work get shipped* (process). A flat
list of 16 files mixing WCAG success criteria with WebGL effect links made it
easy to skim past the non-negotiable items; grouping by consequence makes the
priority order visible from the folder name alone.

## How to use this

Read `SKILL.md` first — it’s the router. It names the exact file (with its
full path) to read at each step of build mode and audit mode, and states
which references are non-negotiable versus opt-in. Don’t just browse these
folders and start applying things out of order.
