---
name: writer-chinese-logic-check
description: perform a hard Chinese logic and consistency review for relatively mature drafts, focusing on substantive reasoning problems instead of ornamental edits.
---

Use this skill inside `writer` when the draft is already mature and the task is to catch substantive reasoning problems.

Before writing, read [references/prompt.md](references/prompt.md).

Core rules:

- report only material logic or consistency issues
- check concept drift, unsupported conclusions, and argument gaps
- avoid style churn and ornamental edits
- if no material problem exists, say so briefly

Output:

- concise issue list with location-aware commentary
- or a brief no-major-issue judgment
