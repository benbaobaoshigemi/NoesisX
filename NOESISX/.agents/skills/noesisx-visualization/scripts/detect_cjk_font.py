#!/usr/bin/env python3
"""Detect a Chinese-safe font family available on the host."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys

SANS_CANDIDATES = [
    "PingFang SC",
    "Hiragino Sans GB",
    "Source Han Sans SC",
    "Noto Sans CJK SC",
    "Microsoft YaHei",
    "Heiti SC",
    "STHeiti",
    "WenQuanYi Zen Hei",
    "SimHei",
]

SERIF_CANDIDATES = [
    "Songti SC",
    "STSong",
    "Source Han Serif SC",
    "Noto Serif CJK SC",
    "SimSun",
]


def fc_match(family: str) -> str | None:
    if shutil.which("fc-match") is None:
        return None
    try:
        result = subprocess.run(
            ["fc-match", family, "--format=%{family[0]}"],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError:
        return None
    value = result.stdout.strip()
    if not value:
        return None
    lowered = value.lower()
    if "lastresort" in lowered or "unknown" in lowered:
        return None
    return value


def detect(style: str) -> dict[str, object]:
    candidates = SANS_CANDIDATES if style == "sans" else SERIF_CANDIDATES
    for candidate in candidates:
        matched = fc_match(candidate)
        if matched:
            return {
                "style": style,
                "requested_family": candidate,
                "resolved_family": matched,
                "fallback": False,
            }
    fallback = "Helvetica" if style == "sans" else "Times New Roman"
    return {
        "style": style,
        "requested_family": None,
        "resolved_family": fallback,
        "fallback": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--style", choices=["sans", "serif"], default="sans")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = detect(args.style)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["resolved_family"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
