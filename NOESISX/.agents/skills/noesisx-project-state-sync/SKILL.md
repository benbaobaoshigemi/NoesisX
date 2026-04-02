---
name: noesisx-project-state-sync
description: Use when a stage of work requires coordinated updates across `experiment.md`, `brain/GRAPH.md`, and `brain/PROJECT.md`. Do not use for single-file edits that do not affect project state.
---

Use this skill when a formal experiment or stage closure changes project memory.

This skill exists to protect the update order and the division of responsibilities across the three memory files.

## File roles

- `experiment.md` records experiment facts, process, observations, interpretation, outputs, and `Topology Delta`.
- `brain/GRAPH.md` records topology only.
- `brain/PROJECT.md` records current state only.

## Required order

Always use this order:

1. update `experiment.md`
2. update `brain/GRAPH.md` if and only if topology truly changed
3. update `brain/PROJECT.md`

## Workflow

1. Confirm the experiment boundary is clear enough for a formal record.
2. Write facts into `experiment.md` first.
3. Decide whether the experiment justifies a topology change.
4. If yes, call `noesisx-graph-build` logic and update `brain/GRAPH.md`.
5. Sync `brain/PROJECT.md` so its current-state summary matches the new reality.
6. In the user-facing reply, state which files changed and which expected files did not change, with reasons.
7. If `experiment.md` changed, report the experiment directory and the main facts, results, interpretations, or `Topology Delta` additions.
8. If `brain/GRAPH.md` changed, report the node, edge, state-transition, or checkpoint additions.
9. If `brain/PROJECT.md` changed, report the mainline, active-route, anomaly, or next-priority changes.
10. If `brain/PROJECT.md` compresses the situation for readability, verify that high-risk anomalies and key unresolved issues were not lost.

## Never do this

- Do not update `brain/PROJECT.md` before `experiment.md`.
- Do not write topology details into `brain/PROJECT.md`.
- Do not write current-state summary into `brain/GRAPH.md`.
- Do not skip `experiment.md` when a formal experiment actually happened.
- Do not let a user-facing summary replace the file updates themselves.
