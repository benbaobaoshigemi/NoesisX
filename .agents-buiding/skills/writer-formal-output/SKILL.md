---
name: writer-formal-output
description: Use when the task is a formal external-facing deliverable such as a report, memo, summary, or statement. Do not use while facts are still unstable or while the task is still primarily route exploration.
---

Use this skill when the work has entered the formal-deliverable stage.

The deliverable must stand on its own for an outside reader who does not know the project files, the chat history, or the internal workflow.

## Core rule

Transform internal research material into external prose. Do not leak internal scaffolding.

## Workflow

1. Confirm that the factual basis is stable enough for formal writing.
2. Identify the deliverable type and audience.
3. Draft with clear structure, accurate wording, and honest uncertainty.
4. If the task includes export, place outputs under `output/YYYY-MM-DD_HHMMSS/`.
5. Before finishing, verify that the text can be read independently from project internals.
6. Remove any sentence that depends on hidden project context, such as "as discussed above" or "according to the project record".

## Never do this

- Do not invent facts or smooth over contradictory evidence.
- Do not leak internal file names, private paths, or internal record-keeping machinery.
- Do not name `PROJECT.md`, `GRAPH.md`, `ASSIGNMENT.md`, `NOTE.md`, `experiment.md`, or `library/INDEX.md` in the deliverable.
- Do not preserve chat-tone filler, defense, or debate posture.
- Do not write as if the document is arguing with an invisible opponent.
- Do not use polished wording to hide unstable facts.

If facts are still unstable, stop and return that instability to the parent agent.
