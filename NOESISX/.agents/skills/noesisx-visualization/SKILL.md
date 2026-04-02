---
name: noesisx-visualization
description: Use when the main agent must create or validate figures directly, either to understand data during analysis or to produce real visual assets for reports, writer handoff, and user-facing delivery. Build figures with matplotlib first, then inspect rendered images for readability, layout defects, missing content, Chinese font failures, and whether the figure actually serves the intended analytical or communication goal.
---

# Visualization

Use this skill directly from the main agent.

This is a two-stage skill built around `matplotlib`:

1. draw the figure with `matplotlib`
2. inspect the rendered image, record defects, and iterate until the image is usable

Use it in two scenarios:

- the main agent needs a figure to think with, compare patterns, or reduce analysis ambiguity
- the project needs a real figure asset for `visualization/`, writer handoff, or direct user reporting

## Output placement

- exploratory drafts may live in `scratch/`
- formal retained figures belong in `visualization/YYYY-MM-DD_HHMMSS/`
- when the figure will enter a formal document, store the final asset in `visualization/` before invoking `noesisx-push-writer`

## Workflow

1. Decide the scenario:
   - `analysis`: the figure is mainly for the main agent's own reasoning
   - `deliverable`: the figure is meant to survive into user-facing output
2. Write a tiny visual brief before drawing:
   - what question the figure should answer
   - what claim, contrast, or pattern it should make visible
   - who will read it
   - what the reader should notice in the first few seconds
   - whether the labels must support Chinese
   - which labels are only internal field names and must be replaced by reader-facing display names
   - which failures would make the figure unusable even if it rendered successfully
3. Read [references/chart-selection.md](references/chart-selection.md) when chart choice is not obvious.
4. If `matplotlib` is missing, install the figure stack first:
   ```bash
   uv pip install matplotlib seaborn plotly pandas pillow
   ```
   If `uv` is unavailable:
   ```bash
   python3 -m pip install matplotlib seaborn plotly pandas pillow
   ```
5. Detect an available Chinese-safe font:
   ```bash
   python3 <path-to-skill>/scripts/detect_cjk_font.py --style sans
   ```
   Use serif only when the figure clearly needs a serif family.
6. Build the figure with the bundled matplotlib chart script:
   ```bash
   python3 <path-to-skill>/scripts/make_matplotlib_chart.py \
     --chart line \
     --input data.csv \
     --x epoch \
     --y accuracy,loss \
     --legend-labels "准确率,损失" \
     --title "训练过程概览" \
     --xlabel "轮次" \
     --ylabel "数值" \
     --palette academic-muted \
     --grid-style dashed \
     --spine-style open \
     --scenario analysis \
     --purpose "比较模型随轮次变化的主要指标" \
     --output-dir scratch/visuals/training_overview
   ```
   This writes at least `PNG`, `SVG`, and metadata. Use `--journal nature` or `--journal default` when needed.
7. Render or reuse a PNG preview immediately:
   ```bash
   python3 <path-to-skill>/scripts/render_visual.py \
     --input scratch/visuals/training_overview/training_overview.png \
     --output scratch/visuals/training_overview.png
   ```
   When the chart script already wrote a correct PNG, this step can simply normalize the inspection path.
8. Read [references/review-checklist.md](references/review-checklist.md), then inspect the rendered PNG with the image viewer tool. Do not skip this step.
9. If you find any defect, record it in plain language, revise the figure code or parameters, and regenerate the figure. Treat inspection as an iteration loop, not a one-shot veto.
10. Only after the rendered image has no unresolved defects may you:
   - keep it as an analysis artifact
   - promote it into `visualization/`
   - hand it to `noesisx-push-writer` or mention it in a user-facing report

## Hard rules

- Do not treat code-level success as figure success. The rendered image is the real object.
- Do not assume Chinese text is safe unless the detected font actually supports it.
- Do not hand writer a planned figure, only a real exported asset.
- Do not accept clipping, tiny labels, overlapped legends, broken minus signs, missing glyphs, or faded low-contrast content.
- Do not accept a technically valid figure that uses the wrong chart type, hides the intended comparison, or leaves the reader unsure what matters.
- Do not confuse "cleaner" with "emptier". Remove redundant labels, unnecessary subplots, and verbose annotations before removing useful structure.
- Do not accept a chart type merely because it was easy to generate. It must match the question being asked.
- If the figure does not help the main agent answer the intended question, redraw it instead of explaining it away.
- Do not silently fall back to a non-Chinese-safe font when the figure contains Chinese labels.
- Do not burn internal workflow metadata such as scenario, purpose, or file bookkeeping into the figure by default. Keep those in sidecar metadata, notes, or report text.
- Treat hard defects and style choices differently. A different-but-clear palette can still be acceptable; collisions, occlusion, invisible marks, missing labels, and misleading encodings are not.
- Avoid "default software appearance". If the result looks like untouched matplotlib, spreadsheet export, or a low-effort screenshot, keep iterating.

## Bundled resources

- [references/chart-selection.md](references/chart-selection.md): quick chart-choice guidance
- [references/review-checklist.md](references/review-checklist.md): mandatory rendered-image inspection checklist
- `scripts/detect_cjk_font.py`: detect a Chinese-safe font family available on the host
- `scripts/style_presets.py`: publication and journal style presets built on matplotlib
- `scripts/figure_export.py`: stable export helpers for png/svg/pdf outputs
- `scripts/make_matplotlib_chart.py`: create scientific charts with matplotlib and Chinese-safe font handling
- `scripts/render_visual.py`: render SVG or PDF into PNG for visual inspection
- `assets/publication.mplstyle`: base publication style
- `assets/nature.mplstyle`: Nature-oriented style variant
