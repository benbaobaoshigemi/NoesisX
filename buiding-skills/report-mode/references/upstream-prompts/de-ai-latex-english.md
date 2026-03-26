# Local prompt reference: De-AI English cleanup

Source basis: the "去 AI 味（LaTeX 英文）" section of Leey21/awesome-ai-research-writing.

Use this reference when the text feels stiff, generic, over-smoothed, or obviously machine-like.

Core rules to enforce:
- Prefer plain, precise academic vocabulary.
- Avoid overused grandiose words and unnecessary sophistication.
- Remove mechanical transition phrases and forced rhetorical scaffolding.
- Reduce dash-heavy phrasing when a cleaner clause structure works.
- Do not add emphasis formatting.
- Preserve LaTeX cleanliness.
- Follow a high threshold for change: if the text is already natural, keep it.

Output expectation for the subagent:
- return the cleaned version
- if little or no change is needed, preserve the original rather than rewriting for its own sake
