# Agentic readiness — is the site legible to AI agents?

Checklist distilled from [isitagentready.com](https://isitagentready.com), covering
the emerging standards that let AI agents discover, read, authenticate with, and
(for commerce sites) transact on a website programmatically. This is a **new,
low-tier layer** on top of technical SEO — treat it as Low priority for a personal
portfolio/art site, Medium-High for any site with a paid offering, API, or booking
flow. Never let it displace accessibility/security/GDPR, which stay non-negotiable.

## 1. Discoverability
- [ ] `robots.txt` at site root, valid syntax, references the sitemap
      (`Sitemap: https://example.com/sitemap.xml`).
- [ ] XML sitemap present and current (matches `references/growth/seo-checklist.md`'s
      sitemap item — same file serves both SEO and agent crawlers).
- [ ] Homepage response includes useful discovery metadata: `Link` headers or
      `<link>` tags pointing agents at machine-readable resources (sitemap,
      llms.txt, API catalog) rather than making them guess paths.
- [ ] DNS-AID ("DNS for AI Discovery") — an emerging DNS-record convention for
      advertising agent-facing endpoints at the domain level. Spec is early/thin;
      note it as "watch, don't block a launch on it."

## 2. Content accessibility
- [ ] Markdown content negotiation — serving a Markdown version of a page when
      requested (Cloudflare's emerging convention: agent requests `Accept:
      text/markdown` or hits a `.md` variant of the URL, gets clean content
      instead of full HTML/CSS/JS). Optional for a static site; skip if the
      hosting stack can't do content negotiation — don't build a bespoke server
      just for this.
- [ ] Consider a plain `llms.txt` at site root (community convention, not yet
      formalized) — a short Markdown summary of what the site is and links to
      its key pages, written for an LLM context window rather than a browser.
      Cheap to add, useful even where the fancier protocols below aren't.

## 3. Bot access control
- [ ] AI-specific rules inside `robots.txt` — explicit `User-agent` blocks for
      known AI crawlers (e.g. `GPTBot`, `ClaudeBot`, `Google-Extended`,
      `CCBot`) stating allow/disallow, rather than leaving them to fall through
      a wildcard rule that may say something you didn't intend.
- [ ] Content Signals — Cloudflare's emerging protocol for expressing
      machine-readable *preferences* about how crawled content may be used
      (e.g. "index yes, train no") beyond simple allow/disallow.
- [ ] Web Bot Auth — cryptographic bot-authentication mechanism so verified
      agents can be distinguished from spoofed/malicious traffic. Relevant if
      the site wants to grant elevated access to authenticated agents; skip for
      a simple public portfolio.

## 4. Protocol discovery
- [ ] MCP Server Card — a discoverable manifest describing an MCP server the
      site exposes (only applicable if the project *has* an MCP server to
      expose — most portfolio/art sites won't).
- [ ] Agent Skills registry entry, per the [agentskills.io](https://agentskills.io)
      convention — only relevant if this project publishes a reusable agent
      skill.
- [ ] WebMCP — an emerging in-browser protocol letting a page expose actions
      directly to an agent operating the browser (distinct from a server-side
      MCP server).
- [ ] API Catalog — if the site has a public API, a discoverable, documented
      catalog of its endpoints (OpenAPI/Swagger doc linked from a
      well-known path) rather than docs buried in a README.
- [ ] OAuth discovery — standard `/.well-known/oauth-authorization-server`
      (or equivalent) metadata endpoint, if the site has any OAuth-protected
      resource.
- [ ] OAuth Protected Resource metadata (RFC 9728) — if an API requires OAuth,
      expose the protected-resource metadata so an agent client can complete
      the flow without hardcoded assumptions.

## 5. Commerce (only if the site sells something)
- [ ] x402 — HTTP 402-based machine payment standard.
- [ ] MPP (Machine-Payable Protocol).
- [ ] UCP (Universal Commerce Protocol).
- [ ] ACP (Agentic Commerce Protocol).

These four are early-stage and mutually competing standards for letting an
agent complete a purchase autonomously. Do not implement speculatively — flag
as "watch" unless Sinaida is explicitly building a storefront/checkout an
agent should be able to transact against.

## Quick wins (do these on every build/audit regardless of site type)
1. Valid `robots.txt` with explicit AI-bot rules + sitemap directive.
2. A current XML sitemap.
3. A short `llms.txt` at site root.
4. Semantic HTML and real heading hierarchy (already required by
   `references/compliance/accessibility-wcag.md` and `references/growth/seo-checklist.md` — it's
   also what makes a page parseable by an agent with no special protocol at all).

## What to skip for a personal art/portfolio site
Bot Access Control's cryptographic Web Bot Auth, all of Protocol Discovery
(no API/MCP server to expose), and all of Commerce — call these explicitly
N/A in an audit rather than silently omitting them, so it's clear they were
considered and ruled out, not missed.
