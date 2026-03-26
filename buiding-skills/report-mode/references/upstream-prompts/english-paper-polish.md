# Local prompt reference: English academic polish

Source basis: the "表达润色（英文论文）" section of Leey21/awesome-ai-research-writing. This local copy is kept inside the skill so the workflow does not depend on remote access.

Use this reference when the subagent must improve English academic prose for formal research deliverables.

Core rules to enforce:
- Raise academic rigor, clarity, and readability rather than merely fixing typos.
- Prefer standard academic written English over flashy or rare wording.
- Avoid contractions.
- Keep common domain abbreviations such as LLM unchanged.
- Preserve existing LaTeX commands and existing formatting; do not add new emphasis markup.
- Keep paragraph form; do not convert prose into itemized lists unless the user explicitly asks.
- Optimize long or awkward sentences into clear, publication-grade prose.

Output expectation for the subagent:
- return refined text as the main deliverable
- optionally provide a short modification note outside the final saved document if the main agent asked for it
