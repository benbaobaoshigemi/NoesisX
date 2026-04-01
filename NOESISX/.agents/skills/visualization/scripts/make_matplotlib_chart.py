#!/usr/bin/env python3
"""Create simple scientific charts with matplotlib."""

from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path

import matplotlib.pyplot as plt

from detect_cjk_font import detect
from figure_export import save_publication_figure
from style_presets import configure_for_journal


def read_rows(path: Path, delimiter: str) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        return [dict(row) for row in reader]


def parse_columns(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def as_float(value: str) -> float:
    return float(value.strip())


def parse_optional_labels(raw: str | None, expected: int) -> list[str] | None:
    if raw is None:
        return None
    labels = [item.strip() for item in raw.split(",")]
    if len(labels) != expected:
        raise SystemExit(f"--legend-labels expects {expected} labels, got {len(labels)}.")
    return labels


def build_series(rows: list[dict[str, str]], x_field: str, y_fields: list[str], series_field: str | None) -> tuple[list[str], dict[str, tuple[list[str], list[float]]]]:
    if series_field:
        grouped: dict[str, tuple[list[str], list[float]]] = {}
        order: list[str] = []
        for row in rows:
            name = row[series_field]
            if name not in grouped:
                grouped[name] = ([], [])
                order.append(name)
            xs, ys = grouped[name]
            xs.append(row[x_field])
            ys.append(as_float(row[y_fields[0]]))
        return order, grouped

    grouped = {
        field: ([row[x_field] for row in rows], [as_float(row[field]) for row in rows])
        for field in y_fields
    }
    return y_fields, grouped


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chart", choices=["line", "bar", "scatter"], required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--delimiter", default=",")
    parser.add_argument("--x", required=True)
    parser.add_argument("--y", required=True)
    parser.add_argument("--series")
    parser.add_argument("--legend-labels")
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--xlabel", default="")
    parser.add_argument("--ylabel", default="")
    parser.add_argument("--scenario", choices=["analysis", "deliverable"], required=True)
    parser.add_argument("--purpose", required=True)
    parser.add_argument("--audience", default="main-agent")
    parser.add_argument("--journal", default="default")
    parser.add_argument("--font-family", choices=["sans", "serif"], default="sans")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--basename")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    basename = args.basename or output_dir.name
    output_base = output_dir / basename

    rows = read_rows(input_path, args.delimiter)
    if not rows:
        raise SystemExit("Input table is empty.")

    font_info = detect(args.font_family)
    resolved_family = str(font_info["resolved_family"])
    configure_for_journal(args.journal, font_family=args.font_family, resolved_family=resolved_family)
    y_fields = parse_columns(args.y)
    series_names, grouped = build_series(rows, args.x, y_fields, args.series)
    display_labels = parse_optional_labels(args.legend_labels, len(series_names))
    label_map = {
        series_name: (display_labels[index] if display_labels else series_name)
        for index, series_name in enumerate(series_names)
    }

    previous_constrained = plt.rcParams.get("figure.constrained_layout.use", False)
    plt.rcParams["figure.constrained_layout.use"] = False
    fig, ax = plt.subplots()
    plt.rcParams["figure.constrained_layout.use"] = previous_constrained
    fig.subplots_adjust(left=0.12, right=0.97, bottom=0.16, top=0.84)

    if args.chart == "bar":
        x_labels = grouped[series_names[0]][0]
        x_positions = list(range(len(x_labels)))
        width = 0.8 / max(len(series_names), 1)
        for idx, name in enumerate(series_names):
            _, ys = grouped[name]
            shifted = [x + (idx - (len(series_names) - 1) / 2) * width for x in x_positions]
            ax.bar(shifted, ys, width=width * 0.9, label=label_map[name])
        ax.set_xticks(x_positions, x_labels)
    else:
        for name in series_names:
            xs, ys = grouped[name]
            if args.chart == "scatter":
                ax.scatter(xs, ys, label=label_map[name], s=28)
            else:
                ax.plot(xs, ys, marker="o", label=label_map[name])

    fig.suptitle(args.title, x=0.12, y=0.965, ha="left", va="top")
    if args.subtitle:
        fig.text(0.12, 0.905, args.subtitle, ha="left", va="top", fontsize=9, color="#4B5563")
    ax.set_xlabel(args.xlabel)
    ax.set_ylabel(args.ylabel)
    if len(series_names) > 1:
        ax.legend()

    saved = save_publication_figure(fig, output_base, formats=("png", "svg", "pdf"), dpi=600 if args.journal == "nature" else 300)
    meta_path = output_dir / f"{basename}.json"
    meta_path.write_text(
        json.dumps(
            {
                "scenario": args.scenario,
                "purpose": args.purpose,
                "audience": args.audience,
                "chart": args.chart,
                "input": os.fspath(input_path),
                "x_field": args.x,
                "y_fields": y_fields,
                "series_field": args.series,
                "legend_labels": label_map,
                "title": args.title,
                "subtitle": args.subtitle,
                "xlabel": args.xlabel,
                "ylabel": args.ylabel,
                "journal": args.journal,
                "font_family": args.font_family,
                "resolved_font_family": resolved_family,
                "font_fallback": bool(font_info["fallback"]),
                "saved_files": [os.fspath(path) for path in saved],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    plt.close(fig)
    for path in saved:
        print(os.fspath(path))
    print(os.fspath(meta_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
