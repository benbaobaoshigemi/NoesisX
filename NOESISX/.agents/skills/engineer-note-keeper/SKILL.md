---
name: engineer-note-keeper
description: Use when technical maintenance changes environment conventions, dependency expectations, encoding or rendering rules, or creates a pitfall that should be recorded in `brain/NOTE.md`. Do not use for research judgments.
---

Use this skill when the engineering layer has learned something that future work must remember.

`brain/NOTE.md` belongs to technical continuity, not research continuity.

## Record in `brain/NOTE.md`

- environment assumptions
- dependency expectations
- encoding and transcoding conventions
- rendering conventions
- reusable repair procedures
- repeated pitfalls and how to avoid them

## Workflow

1. Confirm the discovery is technical rather than research-semantic.
2. Phrase the note as a reusable convention or warning, not as a one-off chat recap.
3. Keep the note specific enough that a later agent can act on it.
4. Avoid duplicating material that belongs in `brain/PROJECT.md`, `brain/GRAPH.md`, or `experiment.md`.
5. Record the impact scope when a repair changes how later work should read, write, render, or execute files.

## Never do this

- Do not write route judgments into `brain/NOTE.md`.
- Do not write user intent into `brain/NOTE.md`.
- Do not use `brain/NOTE.md` as a dumping ground for general progress logs.
- Do not turn `brain/NOTE.md` into a mixed research-and-engineering notebook.
