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


def set_palette(colors: Iterable[str] = OKABE_ITO) -> None:
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=list(colors))


def apply_publication_style(style_name: str = "default", font_family: str = "sans", resolved_family: str | None = None) -> None:
    if style_name == "nature":
        plt.style.use(str(ASSETS_DIR / "nature.mplstyle"))
    else:
        plt.style.use(str(ASSETS_DIR / "publication.mplstyle"))
    _apply_font_preferences(font_family, resolved_family=resolved_family)
    set_palette()


def configure_for_journal(journal: str = "default", font_family: str = "sans", resolved_family: str | None = None) -> None:
    apply_publication_style(
        "nature" if journal.lower() == "nature" else "default",
        font_family=font_family,
        resolved_family=resolved_family,
    )
