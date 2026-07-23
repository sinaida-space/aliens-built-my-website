# GDPR / cookie banner / privacy policy checklist

## Cookie consent rules
- No non-essential cookie/tracker (analytics, ads, social embeds) fires before
  explicit consent.
- Strictly necessary cookies (session, security, load-balancing) don't need consent
  but must be disclosed.
- Choices offered: **Accept all**, **Reject all**, **Customize by category** — all
  equally easy to reach. Reject-all must not be buried, smaller, or harder to click
  than Accept-all (no dark patterns).
- No pre-ticked boxes; consent is opt-in, not opt-out.
- Withdrawing consent is as easy as giving it (a persistent "Cookie settings" link
  in the footer, not just a one-time banner).
- Log what was chosen, when, and against which policy version.

## Cookie banner UX
- Appears on first visit, unobtrusive but clear; plain-language explanation of what
  and why.
- Links to the Privacy Policy (and Cookie Policy if separate).
- Never blocks core site functionality for strictly-necessary-cookie use cases.

`templates/cookie-banner.html` implements all of the above out of the box —
default to it rather than writing a new banner from scratch.

## Privacy policy — required content
1. Who you are (name/company, contact, data controller).
2. What data is collected (name, email, IP, usage data, cookies, form submissions).
3. Why (purpose per category: service delivery, analytics, marketing).
4. Legal basis per purpose (consent / contract / legitimate interest / legal obligation).
5. Retention period or the criteria used to set one.
6. Who data is shared with (processors: hosting, analytics, email, payment) and
   whether any transfer is outside the EU/EEA.
7. User rights: access, correction, deletion, restriction, portability, objection,
   consent withdrawal — and how to exercise each.
8. Security measures, described in general (not implementation-revealing) terms.
9. Contact for privacy questions (and DPO if one exists).

`templates/privacy-policy.md` has this structure with placeholders — fill every
placeholder with the real business's facts before shipping; never leave a
placeholder live on a real site.

## When it doesn't apply
A purely static portfolio/art site with zero cookies, zero forms, zero analytics
technically doesn't need a cookie banner — but state that explicitly during the
interview/audit rather than silently omitting the privacy policy. A privacy policy
is still good practice even with no tracking (it builds trust and covers contact-form
data if one exists).
