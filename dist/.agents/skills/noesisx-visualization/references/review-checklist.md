# Rendered Image Review Checklist

Review the rendered PNG, not just the source code or SVG text.
If you find a problem, write down the defect, fix the figure, and inspect the next render again. The inspection stage is an iteration loop.

## Rendering integrity

- no missing text
- no tofu boxes or broken glyphs
- no clipped title, legend, labels, ticks, or annotations
- no vanished line segments, markers, or bars
- no unintended transparency or white-on-white disappearance

## Readability

- body text is readable at normal viewing size
- axis labels and tick labels are not too small
- axis labels say what is measured and include units when relevant
- color contrast is strong enough without zooming
- dense content is still separable by eye
- multiple series are distinguishable by color, marker, hatch, or line style
- if multiple series need a legend, the legend is clear and complete
- the legend does not block a key trend or cluster
- lines, points, bars, and confidence bands are thick enough to remain visible

## Layout quality

- title, subtitle, plot area, legend, and notes are aligned cleanly
- legend does not cover data
- labels do not collide with each other
- margins are not so tight that export risks cropping
- axis titles, tick labels, captions, and any footer-like text do not overlap
- the figure does not contain internal bookkeeping text that should live outside the image
- the figure does not embed a full "Figure N:" caption inside the chart unless that text is part of the intended visual
- there are no watermarks, logos, or decorative elements unrelated to the analytical task

## Chinese font safety

- Chinese labels display as real glyphs, not fallback boxes
- punctuation and minus signs remain visually stable
- serif or sans choice matches the figure style instead of looking accidental

## Purpose fit

- can the intended reader see the main pattern quickly
- does the figure answer the question stated in the brief
- is the chart type appropriate for the analytical question
- are important comparisons visible without hunting through clutter
- if this is for analysis, does it reduce ambiguity for the main agent
- if this is for delivery, can it enter a report without apology or explanation

## Conciseness

- repeated values are not redundantly shown in multiple places without a reason
- long prose is not stuffed into tick labels, legends, or annotation blocks
- the figure is not split into unnecessary subplots when one plot would communicate the point better
- annotations explain a key point instead of restating what the axis or legend already says

## Style integrity

- the plot does not look like untouched default matplotlib, spreadsheet export, or a low-resolution screenshot
- the background is light unless there is a strong task-specific reason not to be
- the palette is professional and non-jarring
- sequential data does not use rainbow or jet-like colormaps
- decorative effects such as gratuitous shadows or fake 3D perspective are absent unless analytically necessary

## Hard vetoes

If any of the following is true, the figure is not ready:

- wrong chart type for the question
- missing axis labels or missing units where units matter
- missing legend for multi-series content that cannot be directly labeled
- text collisions or legend occlusion hide important content
- poor color discrimination makes series hard to tell apart
- key marks are effectively invisible because of size, transparency, or low contrast
- data labels, captions, or notes overwhelm the actual comparison
- obvious rendering artifacts, pixelation, distortion, or accidental aspect-ratio warping

If any answer is no:

- name the defect plainly
- revise the figure
- rerender
- inspect again

Only stop when no unresolved visual defect remains.
