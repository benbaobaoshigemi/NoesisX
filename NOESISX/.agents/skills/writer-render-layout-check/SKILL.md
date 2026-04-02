---
name: writer-render-layout-check
description: inspect formal document outputs for layout and rendering quality, with special attention to tables, formulas, figure placement, numbering, and export stability in docx or pdf form.
---

Use this skill inside `writer` when the deliverable is a formal document rather than plain raw text.

Before writing, read [references/prompt.md](references/prompt.md).

Core rules:

- review layout as part of the deliverable, not as an optional afterthought
- inspect tables, formulas, headings, numbering, figure placement, and caption consistency
- require display formula blocks for formal formulas
- flag render failures, clipping, misalignment, and broken structure
- use rendered pages as the primary inspection surface rather than plain text extraction

Do not define a separate rendering pipeline here.

- reuse the installed `openai-doc` skill for `.docx` rendering and page-image inspection
- reuse the installed `openai-pdf` skill for `.pdf` page-image inspection
- this skill only adds writer-side acceptance criteria on top of those existing render chains

Writer-specific acceptance criteria:

- headings, numbering, and pagination remain visually stable after rendering
- tables do not show broken headers, clipped cells, unreadable narrow columns, or missing units
- formal formulas use display formula blocks and do not collide with surrounding text
- figures, captions, and in-text references remain correctly matched after rendering
- there are no missing glyphs, encoding artifacts, overlap, or abnormal spacing

Closure rule:

- if a material render defect exists, the document is not yet deliverable
- revise the source, re-render through the existing `openai-doc` / `openai-pdf` chain, and inspect again

Output:

- a render/layout issue list
- or a brief confirmation that no material render/layout issue was found
