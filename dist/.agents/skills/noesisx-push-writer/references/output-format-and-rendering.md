# Output Format and Rendering

Formal deliverables must be treated as rendered outputs, not just text bodies.

Within this architecture, once `writer` is invoked, the output is always a formal document.
That means `.docx`, `.pdf`, or both are not optional side branches but the default destination.

## Obligations

- ensure layout is stable and readable after export
- check tables for alignment, completeness, and header clarity
- check formulas for proper display rendering
- ensure headings, lists, captions, and numbering are consistent
- if exporting to `.docx` or `.pdf`, inspect the rendered result rather than trusting raw source

## Formula rule

- formal formulas must use display formula blocks
- do not leave important formulas as broken inline text
- do not mix prose lines and formula syntax in a way that damages readability

## Table rule

- tables must remain readable after rendering
- avoid broken headers, wrapped chaos, or missing units
- ensure captions and references are consistent when used

## Escalation

- if rendering or layout issues dominate the problem, `writer` may require `openai-doc`, `openai-pdf`, or engineer-side support
- but `writer` still owns the final output check for the deliverable
