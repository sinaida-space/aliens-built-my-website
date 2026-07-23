#!/usr/bin/env python3
"""HDR glow/bloom logo tagger — opt-in only, see references/glow-logo.md.

Tags a PNG with a cICP chunk (BT.2020 primaries + PQ/SMPTE ST 2084 transfer
curve) so bright pixels read as far above standard-dynamic-range white on
HDR-capable displays. Does not touch base pixel data beyond an optional
highlight boost; the effect is primarily the color-metadata declaration.

Usage:
    python3 hdr_glow.py input.png output.png --nits 4000 --threshold 235

Requires: Pillow (pip install pillow). No network access, no other deps.
"""
import argparse
import struct
import zlib
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:
    raise SystemExit("This script requires Pillow: pip install pillow") from exc

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

# cICP (Coding-independent Code Points) chunk, per PNG third-edition ext.:
# colour_primaries=9 (BT.2020), transfer_function=16 (PQ/SMPTE ST 2084),
# matrix_coefficients=0 (RGB, not used for still images), video_full_range=1.
CICP_PAYLOAD = bytes([9, 16, 0, 1])


def build_chunk(tag: bytes, payload: bytes) -> bytes:
    length = struct.pack(">I", len(payload))
    crc = struct.pack(">I", zlib.crc32(tag + payload) & 0xFFFFFFFF)
    return length + tag + payload + crc


def boost_highlights(img: Image.Image, threshold: int, boost: float) -> Image.Image:
    """Push near-white pixels brighter pre-encoding so the PQ curve has more to work with."""
    img = img.convert("RGBA")
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if min(r, g, b) >= threshold:
                r = min(255, int(r * boost))
                g = min(255, int(g * boost))
                b = min(255, int(b * boost))
                px[x, y] = (r, g, b, a)
    return img


def inject_cicp(input_path: Path, output_path: Path) -> None:
    """Write output_path as a copy of input_path with a cICP chunk inserted
    immediately after IHDR, and any existing sRGB/gAMA/cHRM chunks removed so
    they don't conflict with the HDR declaration."""
    data = input_path.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("Not a PNG file")

    out = bytearray(PNG_SIGNATURE)
    pos = len(PNG_SIGNATURE)
    ihdr_written = False
    conflicting_tags = {b"sRGB", b"gAMA", b"cHRM", b"iCCP"}

    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        tag = data[pos + 4:pos + 8]
        chunk_end = pos + 8 + length + 4
        chunk = data[pos:chunk_end]

        if tag in conflicting_tags:
            pos = chunk_end
            continue

        out += chunk
        if tag == b"IHDR" and not ihdr_written:
            out += build_chunk(b"cICP", CICP_PAYLOAD)
            ihdr_written = True
        pos = chunk_end

    output_path.write_bytes(bytes(out))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--nits", type=int, default=4000,
                         help="Documented target peak brightness for highlights (metadata-level intent, not embedded per-pixel).")
    parser.add_argument("--threshold", type=int, default=235,
                         help="Pixel channel value (0-255) above which a highlight boost is applied before tagging.")
    parser.add_argument("--boost", type=float, default=1.08,
                         help="Multiplier applied to channels at/above --threshold.")
    parser.add_argument("--no-boost", action="store_true", help="Skip the pixel highlight boost, tag metadata only.")
    args = parser.parse_args()

    if args.no_boost:
        img_path = args.input
    else:
        img = Image.open(args.input)
        boosted = boost_highlights(img, args.threshold, args.boost)
        tmp_path = args.output.with_suffix(".tmp.png")
        boosted.save(tmp_path)
        img_path = tmp_path

    inject_cicp(img_path, args.output)

    if not args.no_boost:
        img_path.unlink(missing_ok=True)

    print(f"Wrote {args.output} — verify with:")
    print(f"  ffprobe -show_entries stream=color_transfer,color_primaries {args.output}")
    print("Expect: color_transfer=smpte2084, color_primaries=bt2020")
    print(f"Documented target highlight brightness: {args.nits} nits (~20x standard UI white).")


if __name__ == "__main__":
    main()
