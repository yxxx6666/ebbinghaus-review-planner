#!/usr/bin/env python3
"""Preflight a PDF for A4 page size, orientation, readability, and near-blank pages."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError as exc:
    raise SystemExit("pypdf is required: pip install pypdf") from exc

A4_WIDTH_PT = 595.276
A4_HEIGHT_PT = 841.890


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--tolerance-pt", type=float, default=4.0)
    parser.add_argument("--allow-landscape", action="store_true")
    parser.add_argument("--min-text-chars", type=int, default=8)
    parser.add_argument("--json-out", type=Path)
    return parser.parse_args()


def near(value: float, target: float, tolerance: float) -> bool:
    return abs(value - target) <= tolerance


def main() -> int:
    args = parse_args()
    if not args.pdf.is_file():
        print(f"ERROR: file not found: {args.pdf}")
        return 2

    try:
        reader = PdfReader(str(args.pdf))
    except Exception as exc:
        print(f"ERROR: cannot open PDF: {exc}")
        return 2

    results = []
    failures = []
    for index, page in enumerate(reader.pages, start=1):
        box = page.mediabox
        width = float(box.width)
        height = float(box.height)
        portrait_a4 = near(width, A4_WIDTH_PT, args.tolerance_pt) and near(height, A4_HEIGHT_PT, args.tolerance_pt)
        landscape_a4 = near(width, A4_HEIGHT_PT, args.tolerance_pt) and near(height, A4_WIDTH_PT, args.tolerance_pt)
        size_ok = portrait_a4 or (args.allow_landscape and landscape_a4)
        orientation = "portrait" if height >= width else "landscape"
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        text_chars = len("".join(text.split()))
        near_blank = text_chars < args.min_text_chars
        item = {
            "page": index,
            "width_pt": round(width, 2),
            "height_pt": round(height, 2),
            "orientation": orientation,
            "a4_ok": size_ok,
            "text_chars": text_chars,
            "near_blank": near_blank,
        }
        results.append(item)
        if not size_ok:
            failures.append(f"page {index}: not allowed A4 size ({width:.2f} x {height:.2f} pt)")
        if near_blank:
            failures.append(f"page {index}: near-blank page ({text_chars} extracted characters)")

    report = {
        "file": str(args.pdf),
        "pages": len(reader.pages),
        "passed": not failures and len(reader.pages) > 0,
        "failures": failures,
        "page_results": results,
    }

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
