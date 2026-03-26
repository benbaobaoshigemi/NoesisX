# Routing and selection

Choose the smallest set of local references that matches the user's request.

## Default routing

### New formal draft
Use when the user asks for a report, memo, formal summary, paper section, proposal section, or reviewer-facing writeup.

Start with:
- `upstream-prompts/english-paper-polish.md`
- `upstream-prompts/logic-check.md`

Add `upstream-prompts/de-ai-latex-english.md` when the target document is English and the user cares about tone, stiffness, or AI-writing residue.

### Draft plus polish
Use the same drafting references as above.
Then create a second polishing subagent that explicitly uses:
- `upstream-prompts/de-ai-latex-english.md`
- optional local skill `humanizer` if available

### Reviewer-style report
Use:
- `upstream-prompts/reviewer-lens.md`
- `upstream-prompts/logic-check.md`

### Existing draft revision
Use the drafting references that match the target genre, then add `logic-check.md` for the no-regression pass.

### Word / docx oriented deliverable
Check whether `docx` is locally available. If yes, mention it in the subagent brief. If not, continue with the bundled prompt references and write clean document content without blocking.

## Notes

- Prefer adding one extra reference only when it clearly improves the result.
- Do not overload the subagent with every bundled prompt file.
- The user's explicit request overrides the default route.
