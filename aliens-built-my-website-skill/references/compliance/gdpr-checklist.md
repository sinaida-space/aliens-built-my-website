# GDPR / cookie banner / privacy policy checklist

Cross-checked against [gdpr.eu](https://gdpr.eu)'s compliance checklist, cookie
guidance, and privacy-notice guidance — see "gdpr.eu cross-check" at the bottom
for what changed and why.

## Cookie consent rules
- No non-essential cookie/tracker (analytics, ads, social embeds) fires before
  explicit consent.
- Strictly necessary cookies (session, security, load-balancing) don't need consent
  but must be disclosed.
- Consent is **specific and informed per purpose** — the banner/customize panel
  states what each category of cookie actually tracks and why, not just a category
  label with no explanation.
- Choices offered: **Accept all**, **Reject all**, **Customize by category** — all
  equally easy to reach. Reject-all must not be buried, smaller, or harder to click
  than Accept-all (no dark patterns).
- No pre-ticked boxes; consent is opt-in, not opt-out.
- **The service must remain fully usable if non-essential cookies are refused** —
  never gate core content/functionality behind analytics/marketing consent.
- Withdrawing consent is as easy as giving it (a persistent "Cookie settings" link
  in the footer, not just a one-time banner).
- Log what was chosen, when, and against which policy version — this skill's
  `cookie-banner.html` does this via `localStorage` for static sites; if the site
  has a backend, log it server-side too so the record survives a cleared browser.

## Cookie banner UX
- Appears on first visit, unobtrusive but clear; plain-language explanation of what
  and why.
- Links to the Privacy Policy (and Cookie Policy if separate).
- Never blocks core site functionality for strictly-necessary-cookie use cases.

`templates/cookie-banner.html` implements all of the above out of the box —
default to it rather than writing a new banner from scratch.

## Privacy policy — required content
1. Who you are (name/company, contact, data controller) **and DPO contact if one
   exists** (only mandatory for public authorities or large-scale systematic
   monitoring — most of Sinaida's client sites won't need one; say so rather than
   inventing a DPO).
2. What data is collected (name, email, IP, usage data, cookies, form submissions),
   and **which fields are mandatory vs. optional** on any form, with the
   consequence of not providing an optional field.
3. Why (purpose per category: service delivery, analytics, marketing) — stated
   concretely, not with vague qualifiers ("may," "some," "personalised services").
4. Legal basis per purpose (consent / contract / legitimate interest / legal
   obligation). If legitimate interest is the basis for anything non-trivial,
   note that a balancing/impact assessment was considered.
5. Retention period or the criteria used to set one.
6. Who data is shared with (processors: hosting, analytics, email, payment) and
   whether any transfer is outside the EU/EEA, with the safeguard used (e.g.
   Standard Contractual Clauses).
7. User rights: access, correction, deletion, restriction, portability, objection,
   consent withdrawal, and the right to lodge a complaint with a supervisory
   authority — and how to exercise each. Access/erasure requests get a response
   within **one month**; the first copy of personal data is free.
8. Whether the site uses **automated decision-making or profiling** with legal or
   similarly significant effects — state plainly if it doesn't (true for nearly
   every site this skill builds), rather than omitting the section.
9. Security measures, described in general (not implementation-revealing) terms,
   and — only if the site actually has a backend/database that could be
   breached — a note that affected users and the relevant supervisory authority
   are notified promptly (regulatory deadline: within 72 hours) in the event of a
   breach likely to risk their rights.
10. Contact for privacy questions.

`templates/privacy-policy.md` has this structure with placeholders — fill every
placeholder with the real business's facts before shipping; never leave a
placeholder live on a real site. Write it in plain, active-voice language — avoid
legalese and vague qualifiers; gdpr.eu specifically flags phrasing like "we may
use your data to develop new services" as too vague to be compliant.

## Presentation, not just content
- The Privacy Policy is **linked from every page** of the site (footer, not
  buried one click deeper) — this is itself a build-checklist item, not optional.
- Available free of charge, without requiring login or a data request just to read it.

## When it doesn't apply
A purely static portfolio/art site with zero cookies, zero forms, zero analytics
technically doesn't need a cookie banner — but state that explicitly during the
interview/audit rather than silently omitting the privacy policy. A privacy policy
is still good practice even with no tracking (it builds trust and covers contact-form
data if one exists).

## gdpr.eu cross-check (what this checklist added after reviewing gdpr.eu)
Fetched gdpr.eu's compliance checklist, cookie guidance, and privacy-notice
guidance and compared against this file and `templates/privacy-policy.md`. Added:
purpose-specific (not just category-level) cookie consent; the explicit
"service must stay usable if cookies are refused" rule; 1-month/free-first-copy
timing on access/erasure; automated-decision-making disclosure (even when it's a
"not applicable" statement); mandatory-vs-optional field disclosure on forms;
72-hour breach notification timing (backend sites only); DPO-is-conditional
clarification; footer-link placement as a presentation requirement; and the
plain-language/no-vague-qualifiers writing standard. Nothing in the prior version
was found to be non-compliant — these are additions for completeness, not
corrections of an error.
