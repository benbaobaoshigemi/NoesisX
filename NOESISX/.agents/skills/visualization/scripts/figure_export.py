#!/usr/bin/env python3
"""Export helpers for publication-style matplotlib figures."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt


def save_publication_figure(
    fig: plt.Figure,
    output_base: str | Path,
    formats: Iterable[str] = ("png", "svg", "pdf"),
    dpi: int = 300,
) -> list[Path]:
    output_base = Path(output_base)
    output_base.parent.mkdir(parents=True, exist_ok=True)
    saved: list[Path] = []
    for fmt in formats:
        target = output_base.with_suffix(f".{fmt}")
        fig.savefig(
            target,
            format=fmt,
            dpi=dpi if fmt in {"png", "tiff"} else min(dpi, 300),
            bbox_inches="tight",
            pad_inches=0.08,
            facecolor="white",
            transparent=False,
        )
        saved.append(target)
    return saved
