---
name: writer-chinese-grammar-check
description: perform a bounded grammar and wording error check for Chinese formal writing, reporting concrete mistakes without turning the task into a full rewrite.
---

Use this skill inside `writer` when the task is bounded error checking for Chinese formal prose.

Before writing, read [references/prompt.md](references/prompt.md).

Core rules:

- identify real wording, grammar, or sentence-level errors
- do not perform a full stylistic rewrite
- report problems concretely and locally
- if no real issue exists, say so plainly

Output:

- issue list or corrected version according to the user request
- no decorative rewriting
