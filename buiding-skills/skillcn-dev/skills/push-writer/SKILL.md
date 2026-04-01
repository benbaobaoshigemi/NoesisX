---
name: push-writer
description: route formal writing tasks from the main agent into the writer sub-agent by selecting the right writer-side skills, ensuring required skills are installed, injecting local prompt content into the writer brief, and choosing single, cascade, or parallel writer topology.
---

Use this skill when the main agent has decided the task belongs to `writer`.

`push-writer` is an orchestration skill, not a prose-writing skill.

Calling `writer` always means entering the formal document production chain.
The output target is always `.docx`, `.pdf`, or both.

Core obligations:

- determine the target deliverable mode
- compute the required `writer-*` skills
- ensure all required skills are available before dispatch
- read local prompt files and inject their content into the actual writer prompt
- choose single, cascade, or parallel writer topology
- inject the formal writing style charter
- attach rendering, layout, table, and formula requirements when the task is a deliverable
- route visualization image usage when the document should be image-rich
- require document-export skills because `writer` outputs are always documents
- hand off a complete brief to `writer`

## Workflow

1. Read [mode routing](references/mode-routing.md).
2. Read [required skills](references/required-skills.md).
3. Read [prompt injection contract](references/prompt-injection-contract.md).
4. Read [writer topologies](references/writer-topologies.md).
5. Read [formal style charter](references/formal-style-charter.md).
6. Read [output format and rendering](references/output-format-and-rendering.md).
7. Read [visualization asset integration](references/visualization-asset-integration.md) when the deliverable should include images.
8. Install any missing required skills before dispatch.
9. Build one complete writer prompt body by embedding the selected local prompt seeds.
10. Dispatch to `writer` with the chosen topology.

## Hard rules

- Never pass prompt files as loose attachments or as “please go read these files”.
- Always inject the relevant prompt content into the actual writer brief.
- Do not start `writer` work while required skills are still missing.
- Use single writer by default. Escalate to cascade or parallel only when the mode clearly needs it.
- All formal deliverables must obey the formal style charter.
- Since `writer` outputs are always documents, always include rendering and layout checks in the workflow.
- Always include document-export requirements for `.docx`, `.pdf`, or both.
- Formulas must be rendered as display formula blocks where formal formulas are required.
- `push-writer` does not write the formal body itself.
