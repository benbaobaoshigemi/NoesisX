#!/usr/bin/env python3
"""Render SVG or PDF into PNG for manual inspection."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd: list[str]) -> bool:
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError:
        return False


def render_with_sips(source: Path, output: Path) -> bool:
    if shutil.which("sips") is None:
        return False
    output.parent.mkdir(parents=True, exist_ok=True)
    return run(["sips", "-s", "format", "png", os.fspath(source), "--out", os.fspath(output)])


def flatten_white(source: Path, output: Path) -> bool:
    if shutil.which("magick") is None:
        return False
    return run(
        [
            "magick",
            os.fspath(source),
            "-background",
            "white",
            "-alpha",
            "remove",
            "-alpha",
            "off",
            os.fspath(output),
        ]
    )


def render_with_magick(source: Path, output: Path, density: int) -> bool:
    if shutil.which("magick") is None:
        return False
    output.parent.mkdir(parents=True, exist_ok=True)
    return run(
        [
            "magick",
            "-background",
            "white",
            "-density",
            str(density),
            os.fspath(source),
            "-alpha",
            "remove",
            "-alpha",
            "off",
            os.fspath(output),
        ]
    )


def render_with_qlmanage(source: Path, output: Path, size: int) -> bool:
    if shutil.which("qlmanage") is None:
        return False
    with tempfile.TemporaryDirectory(prefix="codex-visual-preview-") as temp_dir:
        cmd = [
            "qlmanage",
            "-t",
            "-s",
            str(size),
            "-o",
            temp_dir,
            os.fspath(source),
        ]
        if not run(cmd):
            return False
        generated = Path(temp_dir) / f"{source.name}.png"
        if not generated.exists():
            return False
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(generated, output)
        return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--density", type=int, default=220)
    parser.add_argument("--size", type=int, default=2200)
    args = parser.parse_args()

    source = Path(args.input).resolve()
    output = Path(args.output).resolve()
    suffix = source.suffix.lower()

    ok = False
    if suffix == ".svg":
        with tempfile.TemporaryDirectory(prefix="codex-visual-sips-") as temp_dir:
            temp_png = Path(temp_dir) / "raw.png"
            ok = render_with_sips(source, temp_png)
            if ok:
                ok = flatten_white(temp_png, output)
        if not ok:
            ok = render_with_magick(source, output, args.density)
        if not ok:
            ok = render_with_qlmanage(source, output, args.size)
    elif suffix == ".pdf":
        ok = render_with_magick(source, output, args.density)
        if not ok:
            ok = render_with_qlmanage(source, output, args.size)
    elif suffix in {".png", ".jpg", ".jpeg"}:
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, output)
        ok = True

    if not ok:
        raise SystemExit(f"Failed to render preview for {source}")

    print(os.fspath(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
