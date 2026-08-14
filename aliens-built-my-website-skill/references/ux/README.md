# UX — usability and performance for a human visitor

How the site is actually experienced by the person using it.

- **`ux-heuristics.md`** — Nielsen Norman Group’s 10 usability heuristics,
  navigation/menu design, cognitive load (the ≤4-item working-memory rule),
  and a persona-based testing pass (first-timer, screen-reader/keyboard-only,
  distracted mobile, impatient skimmer) for audit mode.
- **`performance-adaptive.md`** — how to build the fast/slow-network,
  low/high-GPU adaptive mode: a “light mode” that degrades gracefully instead
  of just being slow on a bad connection or weak device.

## Why performance lives here, not in compliance

Performance isn’t rated as a legal non-negotiable the way accessibility or
GDPR are, but it’s still not a “nice to have” — a site that’s gorgeous and
unusable on a mid-tier phone on 4G has failed its actual visitors just as
surely as one with a missing cookie banner. It’s grouped with the other
human-experience checks for that reason.
