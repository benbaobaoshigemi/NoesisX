---
name: noesisx-graph-build
description: Use when a task may create or update `brain/GRAPH.md` because research topology has actually changed. Do not use for ordinary experiment notes, ordinary reading, ordinary script runs, or current-state summaries.
---

Use this skill only when `brain/GRAPH.md` may need to change.

`brain/GRAPH.md` is the topology ledger, not the status panel. Its job is to preserve structural history in an append-only way.

This skill includes immediate post-update validation. A `brain/GRAPH.md` edit is not complete until the lint step passes.

## Allowed objects

Allowed node types:

- `ROOT`
- `QUESTION`
- `HYPOTHESIS`
- `METHOD`
- `DATA`
- `LITERATURE`
- `SYNTHESIS`
- `DECISION`

Allowed lineage edges:

- `branch_from`
- `decompose_from`
- `refine_from`
- `merge_from`
- `revive_from`
- `supersede_from`

Allowed dependency edges:

- `requires`

Allowed node states:

- `active`
- `paused`
- `blocked`
- `concluded`
- `dead`
- `absorbed`
- `superseded`
- `aborted`

Allowed events:

- new node
- new edge
- state transition
- checkpoint

## Workflow

1. Decide whether the change is really topological.
2. If it is not topological, stop and tell the parent agent not to update `brain/GRAPH.md`.
3. If it is topological, determine whether the event is:
   - new node
   - new edge
   - state transition
   - checkpoint
4. Enforce append-only history. Never rewrite history to make it cleaner.
5. `brain/GRAPH.md` must use node-ledger form with a separate append-only `## State Transitions` section. Do not collapse the formal project format into a pure event-ledger.
6. Keep node content minimal, rigid, and machine-checkable. Do not allow free prose outside the fixed grammar.
7. Each node record should preserve at least:
   - node id
   - type
   - slug
   - `Opened As`
   - lineage edges
   - dependency edges
   - optional `Refs`
   - wrapped text blocks such as `Semantics` and `Notes`
8. Use `- none` when `Lineage`, `Dependencies`, or `Refs` is empty. Do not leave list fields semantically blank.
9. Do not require a node to point to `experiment.md`, `PROJECT.md`, `library/INDEX.md`, or any other file.
10. Additional status changes must be appended under `## State Transitions` as `### ST-XXXX` records. Do not rewrite old node blocks to extend lifecycle history.
11. The node's current status is determined by `Opened As` plus the last appended transition for that node, if any.
12. Terminal nodes are `concluded`, `dead`, `absorbed`, `superseded`, and `aborted`. Do not move them back into active states in place.
13. If an old route comes back, create a new node and connect it with `revive_from`. Do not revive a terminal node in place.
14. If a new frame replaces an old frame, create a new node and connect it with `supersede_from`.
15. If several routes collapse into one new judgment, create a new `SYNTHESIS` or `DECISION` node.
16. Treat checkpoints as read-only compression aids, not as a second truth source.
17. Checkpoints must use fixed ids such as `### CP-0001`; do not use free-form checkpoint titles.
18. Before editing an existing `brain/GRAPH.md`, save the exact pre-edit file as a temporary snapshot.
19. After every write to `brain/GRAPH.md`, run:
    - for a new graph file: `python3 .agents/skills/noesisx-graph-build/scripts/graph_lint.py brain/GRAPH.md`
    - for an existing graph file: `python3 .agents/skills/noesisx-graph-build/scripts/graph_lint.py brain/GRAPH.md --baseline <pre-edit-snapshot>`
20. If lint fails, fix `brain/GRAPH.md` and rerun. Do not leave the file in a failing state.
21. The baseline check exists to enforce append-only maintenance mechanically: old nodes, old state transitions, and old checkpoints must remain unchanged.
22. When changing the linter itself, run:
    - `python3 .agents/skills/noesisx-graph-build/scripts/test_graph_lint.py`
23. The linter only validates `brain/GRAPH.md` itself plus, when provided, the old `GRAPH.md` snapshot. Cross-file coordination belongs to the parent agent and other skills, not to `GRAPH` lint.

## Never do this

- Do not put current-state summary into `brain/GRAPH.md`.
- Do not record ordinary experiment progress.
- Do not record ordinary reading or ordinary script execution.
- Do not use experiment statuses such as `success`, `failed`, or `inconclusive` as graph node states.
- Do not invent node types, edge types, states, or event types.
- Do not put free prose outside wrapped text blocks such as `Semantics` and `Notes`.
- Do not treat appended state-transition records or checkpoint text as a replacement for node records.
- Do not leave flexible containers such as free-form notes, free paragraphs, or ad hoc sections inside `brain/GRAPH.md`.
- Do not declare a graph update complete before the lint step passes.
