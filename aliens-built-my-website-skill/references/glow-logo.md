# HDR glow/bloom logo technique — opt-in only

**Never apply this by default.** Only use it when Sinaida explicitly asks for a
bloom/glow/HDR logo effect. A "make it beautiful" or "make it pop" request is not
sufficient — ask her to confirm she means this specific effect first, since it has
real trade-offs (below).

Source: gal.tidhar.org.il/blog/hdr-glow-logo — the effect is not a CSS/SVG/canvas
filter; it's HDR color metadata embedded directly in a PNG.

## How it works
1. Tag the PNG with a `cICP` chunk declaring BT.2020 color primaries and the PQ
   (SMPTE ST 2084) transfer curve.
2. Strip conflicting color profile chunks that would override the HDR encoding.
3. Rescale bright pixels (e.g. the glow/highlight areas) to a much higher nit value
   than standard — background/base color stays around ~60 nits, glow/white
   highlights get encoded around 4,000 (up to 10,000) nits, roughly 20× brighter
   than standard UI white.

## Run it
```
python3 scripts/hdr_glow.py your-logo.png your-logo-hdr.png --nits 4000
```
Verify the tagging:
```
ffprobe -show_entries stream=color_transfer,color_primaries your-logo-hdr.png
```
Expect `color_transfer=smpte2084` and `color_primaries=bt2020`.

## Trade-offs — tell Sinaida these before applying
- **Works**: modern iPhones, MacBooks, and other HDR-capable displays — the glow
  areas will genuinely appear to emit light beyond normal screen brightness.
- **Fails gracefully but looks bad on**: standard SDR monitors (many
  Windows/Dell displays) — can render flat, dull, or visibly "smeared."
- **Screenshots and most social re-encoding pipelines strip it** — a personal
  LinkedIn profile photo gets re-encoded and loses the effect; a company/brand
  page logo is the one placement documented to preserve it. Other platforms may
  patch this out over time (Slack already has).
- Because of the above, this is a **novelty/flex effect for a specific platform
  and specific viewers**, not a general-purpose branding upgrade — say this
  plainly rather than oversell it.

## When to reach for it
Good fit: a one-off brand-page logo upload, an experimental post, a piece she
explicitly wants to feel technically show-offy. Bad fit: the main site logo/favicon
that most visitors need to see correctly on ordinary hardware — use a normal
high-contrast logo there and reserve HDR glow for the specific upload it's proven
to survive.
