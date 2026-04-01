# Visualization Asset Integration

When a formal deliverable should be image-rich, `push-writer` must route visualization assets explicitly.

## Source rule

- prefer images already produced under `visualization/`
- do not invent figures that do not exist
- do not describe a figure as inserted unless the file is real and usable

## Writer-side obligations

- identify which visualization assets belong in the document
- make captions and in-text references match the inserted images
- place images where they support the argument rather than as decoration
- ensure image sizing does not break layout

## Rule

- if visualization assets are part of the deliverable, require `writer-visualization-asset-integration`
