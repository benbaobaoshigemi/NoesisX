# Chart Selection

Choose the simplest figure that makes the intended comparison obvious.

## Use a line chart when

- the x axis is ordered or continuous
- the reader should notice trend, convergence, drift, or turning points
- repeated measurements belong to the same evolving process
- markers help the reader see actual sampled points instead of implying false continuity
- secondary or baseline series can be differentiated with dashed lines rather than only color

## Use a bar chart when

- the main job is comparing category magnitudes
- order is categorical rather than continuous
- exact rank or relative gap matters more than continuity
- grouped bars are still few enough that the reader can compare them without scanning a wall of labels
- error bars or direct labels add meaning rather than duplicating what the axis already makes obvious

## Use a scatter plot when

- the question is about correlation, clustering, separation, or outliers
- each point is an observation rather than a time step
- uncertainty or spread matters more than aggregate totals
- shape coding may help when color alone is not sufficient

## Use a heatmap when

- the task is comparing values over a 2D grid of categories or conditions
- relative intensity matters more than precise point-to-point trajectories
- square cells and a perceptually uniform colormap support the comparison

## Do not do this

- do not use pie charts for precise comparison
- do not use pie or donut charts when the reader must compare many similar proportions precisely
- do not use stacked bars when the key question is accurate part-to-part comparison across many groups
- do not use dual y axes unless the alternative would be materially worse
- do not encode too many series in one chart just because the data exists
- do not let decorative color outrun analytical value
- do not use rainbow or jet-like colormaps for quantitative gradients
- do not add extra subplots if one unified chart would show the answer more directly
- do not repeat the same number in bars, labels, caption text, and legend unless the redundancy is clearly useful

## Labeling guidance

- title: answer "what is this figure showing?"
- axis labels: say what the axis measures and include units when relevant
- legend labels: use reader-facing names, not internal variable names
- annotation: use sparingly, only where it clarifies a key point
- direct labeling can replace a legend when it makes the comparison faster and does not create collisions

## Simplicity guidance

- cleaner means less redundant, not less informative
- grid lines, spines, error bars, and uncertainty bands are allowed when they help interpretation
- if you remove an element, verify that the intended comparison is still easier to see afterward
