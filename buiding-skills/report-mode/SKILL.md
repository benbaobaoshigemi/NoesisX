---
name: research-report
description: build formal reports, memos, paper sections, review-style writeups, and other deliverable documents by routing the task through temporary writing subagents. use when the user wants a file or formal deliverable rather than a chat reply, especially when the workflow should reference local copies of prompts and skill ideas from the awesome-ai-research-writing repository and optionally chain drafting plus polishing.
---

Use this skill when the user wants a formal written deliverable. Treat `report` as a pipeline, not as a one-shot rewrite.

Core rule: the main agent does **not** write the final deliverable body directly. The main agent classifies the request, chooses local prompt files and optional local skills, then creates a temporary subagent to draft the document. If the user asked for polishing, create a second temporary subagent for polishing. If the user did **not** ask for polishing, do a lightweight compliance check against the selected local references instead of a second rewrite pass.

## Workflow

1. **Classify the request**
   Decide which of these cases best matches the task:
   - draft a new formal document
   - rewrite or extend an existing draft
   - draft plus polish
   - reviewer-style critical report
   - document export / docx-centered deliverable

2. **Select local references first**
   Read [routing and selection](references/routing-and-selection.md).
   Then select one or more local prompt references from `references/upstream-prompts/`.

3. **Check local skills if needed**
   Read [local skill catalog](references/local-skill-catalog.md).
   If the task would materially benefit from a local skill such as `humanizer`, `docx`, `doc-coauthoring`, or `20-ml-paper-writing`, check whether it is locally available and mention it in the subagent brief.
   Do not block on missing skills. If a needed skill is unavailable, continue using the bundled local prompt references in this skill.

4. **Create the drafting subagent**
   Build the subagent brief using [subagent brief template](references/subagent-brief-template.md).
   The drafting subagent writes the deliverable. The brief must include:
   - the user's actual objective and constraints
   - the selected local prompt references
   - any local skills that should be used
   - explicit statement that the subagent is responsible for the document body
   - explicit ban on inventing facts or changing the requested scope

5. **Optional polishing pass**
   If and only if the user asked for polishing, create a new temporary polishing subagent.
   Route that pass using the relevant local prompt references and any local skills such as `humanizer`.
   The polishing subagent may improve expression, structure, and readability, but must not silently change facts, claims, evidence, or requested scope.

6. **If no polishing was requested**
   The main agent performs a compliance check instead of rewriting. Use [compliance checklist](references/compliance-checklist.md).
   Verify that the drafted document follows the selected local prompt references and fits the requested genre.

7. **Final check before returning or saving**
   Use [semantic drift check](references/semantic-drift-check.md).
   Confirm that any polishing or cleanup did not alter facts, conclusions, scope, or uncertainty level.

## Selection rules

- For English academic prose improvement, start with:
  - [english-paper-polish.md](references/upstream-prompts/english-paper-polish.md)
  - [logic-check.md](references/upstream-prompts/logic-check.md)
- For removing obvious AI-writing residue in English, add:
  - [de-ai-latex-english.md](references/upstream-prompts/de-ai-latex-english.md)
- For reviewer-style critique or harsh evaluation, add:
  - [reviewer-lens.md](references/upstream-prompts/reviewer-lens.md)
- For document-template or Word-centric deliverables, consult:
  - [local-skill-catalog.md](references/local-skill-catalog.md)

## Important constraints

- Keep the workflow staged: classify → select references/skills → draft via subagent → optional polish via new subagent → drift check.
- Do not skip straight to writing the final file in the main agent.
- Do not create one subagent and keep reusing it across stages. Drafting and polishing must use different temporary subagents.
- If the user did not ask for polishing, do not add an unrequested rewrite pass.
- Local prompt references bundled in this skill are authoritative for wording style and review posture in this workflow.
