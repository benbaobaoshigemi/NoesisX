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
- color contrast is strong enough without zooming
- dense content is still separable by eye

## Layout quality

- title, subtitle, plot area, legend, and notes are aligned cleanly
- legend does not cover data
- labels do not collide with each other
- margins are not so tight that export risks cropping
- axis titles, tick labels, captions, and any footer-like text do not overlap
- the figure does not contain internal bookkeeping text that should live outside the image

## Chinese font safety

- Chinese labels display as real glyphs, not fallback boxes
- punctuation and minus signs remain visually stable
- serif or sans choice matches the figure style instead of looking accidental

## Purpose fit

- can the intended reader see the main pattern quickly
- does the figure answer the question stated in the brief
- if this is for analysis, does it reduce ambiguity for the main agent
- if this is for delivery, can it enter a report without apology or explanation

If any answer is no:

- name the defect plainly
- revise the figure
- rerender
- inspect again

Only stop when no unresolved visual defect remains.
