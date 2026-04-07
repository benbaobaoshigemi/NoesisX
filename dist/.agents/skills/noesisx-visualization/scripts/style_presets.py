#!/usr/bin/env python3
"""Matplotlib style presets adapted from the reference scientific visualization skill."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib as mpl
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
ASSETS_DIR = SCRIPT_DIR.parent / "assets"

OKABE_ITO = [
    "#E69F00",
    "#56B4E9",
    "#009E73",
    "#F0E442",
    "#0072B2",
    "#D55E00",
    "#CC79A7",
    "#000000",
]

ACADEMIC_MUTED = [
    "#4C78A8",
    "#F58518",
    "#54A24B",
    "#E45756",
    "#72B7B2",
    "#B279A2",
    "#9D755D",
    "#BAB0AC",
]

SOFT_PASTELS = [
    "#FF9DA6",
    "#7DB7FF",
    "#8EE38E",
    "#FFCC8A",
    "#C4A7E7",
    "#73D2DE",
    "#B8B8FF",
    "#C9ADA7",
]

EARTH_TONES = [
    "#6B8E23",
    "#C2A878",
    "#708090",
    "#355070",
    "#BC6C25",
    "#A3B18A",
    "#7F5539",
    "#6D597A",
]

HIGH_CONTRAST = [
    "#0072B2",
    "#D55E00",
    "#009E73",
    "#CC79A7",
    "#E69F00",
    "#56B4E9",
    "#000000",
    "#7F3C8D",
]

PALETTES = {
    "okabe-ito": OKABE_ITO,
    "academic-muted": ACADEMIC_MUTED,
    "soft-pastels": SOFT_PASTELS,
    "earth-tones": EARTH_TONES,
    "high-contrast": HIGH_CONTRAST,
}

CJK_SANS = [
    "PingFang SC",
    "Hiragino Sans GB",
    "Source Han Sans SC",
    "Noto Sans CJK SC",
    "Microsoft YaHei",
    "Heiti SC",
    "STHeiti",
    "Arial",
    "Helvetica",
    "DejaVu Sans",
]

CJK_SERIF = [
    "Songti SC",
    "STSong",
    "Source Han Serif SC",
    "Noto Serif CJK SC",
    "Times New Roman",
    "DejaVu Serif",
]


def _apply_font_preferences(family: str, resolved_family: str | None = None) -> None:
    if family == "serif":
        mpl.rcParams["font.family"] = "serif"
        font_list = [resolved_family] if resolved_family else []
        mpl.rcParams["font.serif"] = font_list + CJK_SERIF
    else:
        mpl.rcParams["font.family"] = "sans-serif"
        font_list = [resolved_family] if resolved_family else []
        mpl.rcParams["font.sans-serif"] = font_list + CJK_SANS
    mpl.rcParams["axes.unicode_minus"] = False
    mpl.rcParams["svg.fonttype"] = "none"
    mpl.rcParams["pdf.fonttype"] = 42
    mpl.rcParams["ps.fonttype"] = 42


def set_palette(colors: Iterable[str] = ACADEMIC_MUTED) -> None:
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=list(colors))


def _set_spines(style: str) -> None:
    if style == "boxed":
        mpl.rcParams["axes.spines.top"] = True
        mpl.rcParams["axes.spines.right"] = True
    else:
        mpl.rcParams["axes.spines.top"] = False
        mpl.rcParams["axes.spines.right"] = False


def _set_grid(style: str) -> None:
    if style == "none":
        mpl.rcParams["axes.grid"] = False
        return
    mpl.rcParams["axes.grid"] = True
    mpl.rcParams["grid.color"] = "#D1D5DB"
    mpl.rcParams["grid.linewidth"] = 0.7
    if style == "dotted":
        mpl.rcParams["grid.linestyle"] = ":"
    else:
        mpl.rcParams["grid.linestyle"] = "--"
    mpl.rcParams["axes.axisbelow"] = True


def set_image_colormaps(sequential: str = "viridis", diverging: str = "coolwarm") -> None:
    mpl.rcParams["image.cmap"] = sequential


def apply_publication_style(
    style_name: str = "default",
    font_family: str = "sans",
    resolved_family: str | None = None,
    palette: str = "academic-muted",
    sequential_cmap: str = "viridis",
    diverging_cmap: str = "coolwarm",
    spine_style: str = "open",
    grid_style: str = "dashed",
) -> None:
    if style_name == "nature":
        plt.style.use(str(ASSETS_DIR / "nature.mplstyle"))
    else:
        plt.style.use(str(ASSETS_DIR / "publication.mplstyle"))
    _apply_font_preferences(font_family, resolved_family=resolved_family)
    set_palette(PALETTES.get(palette, ACADEMIC_MUTED))
    set_image_colormaps(sequential=sequential_cmap, diverging=diverging_cmap)
    _set_spines(spine_style)
    _set_grid(grid_style)


def configure_for_journal(
    journal: str = "default",
    font_family: str = "sans",
    resolved_family: str | None = None,
    palette: str = "academic-muted",
    sequential_cmap: str = "viridis",
    diverging_cmap: str = "coolwarm",
    spine_style: str = "open",
    grid_style: str = "dashed",
) -> None:
    apply_publication_style(
        "nature" if journal.lower() == "nature" else "default",
        font_family=font_family,
        resolved_family=resolved_family,
        palette=palette,
        sequential_cmap=sequential_cmap,
        diverging_cmap=diverging_cmap,
        spine_style=spine_style,
        grid_style=grid_style,
    )
