---
name: research-report
description: build formal reports, memos, paper sections, review-style writeups, and other deliverable documents by selecting and applying local writing prompt references directly. use when the user wants a file or formal deliverable rather than a chat reply, especially when the workflow should reuse local prompt ideas derived from the awesome-ai-research-writing repository.
---

Use this skill when the user wants a formal written deliverable. Treat `report` as a pipeline, not as a one-shot rewrite.

Core rule: this skill exists to route the writer's own work through the right local prompt references. Do not introduce an extra temporary writing subagent layer. The writer already is the writing role. The workflow is: classify the request, select the smallest useful set of local prompt references, draft or revise directly, then run lightweight checks so that style cleanup does not distort substance.

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
   If the task would materially benefit from a local skill such as `humanizer`, `docx`, `doc-coauthoring`, or `20-ml-paper-writing`, check whether it is locally available and use it directly if appropriate.
   Do not block on missing skills. If a needed skill is unavailable, continue using the bundled local prompt references in this skill.

4. **Draft or revise directly**
   Write the document body directly in the writer workflow using the selected local prompt references.
   Keep the user's actual objective and constraints fixed throughout the drafting pass.
   Do not invent facts, data, sources, or experimental outcomes.
   Do not silently broaden or narrow the requested scope.

5. **Optional polishing pass**
   If and only if the user asked for polishing, run a distinct polishing pass in the same writer workflow.
   Route that pass using the relevant local prompt references and any local skills such as `humanizer`.
   The polishing pass may improve expression, structure, and readability, but must not silently change facts, claims, evidence, or requested scope.

6. **If no polishing was requested**
   Perform a compliance check instead of adding an unrequested rewrite pass. Use [compliance checklist](references/compliance-checklist.md).
   Verify that the drafted document follows the selected local references and fits the requested genre.

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

- Keep the workflow staged: classify → select references/skills → draft directly → optional polish → drift check.
- This skill is for direct writer execution, not for spawning another writing subagent layer.
- If the user did not ask for polishing, do not add an unrequested rewrite pass.
- Local prompt references bundled in this skill are authoritative for wording style and review posture in this workflow.
