# GRAPH

## GN-0001
- Type: ROOT
- Slug: root-question
- Status History:
  - active @ 2026-03-31_090000
- Lineage:
  - none
- Dependencies:
  - none
- Refs:
  - none
- Semantics: |
    根问题节点。

## GN-0002
- Type: HYPOTHESIS
- Slug: first-route
- Status History:
  - active @ 2026-03-31_100000
- Lineage:
  - branch_from: GN-0001
- Dependencies:
  - none
- Refs:
  - none
- Semantics: |
    第一条候选路线。

## Checkpoints

### CP-0001
- Created At: 2026-03-31_091500
- Scope: bootstrap
- Covered Nodes: GN-0001
- Reason: baseline snapshot

### CP-0002
- Created At: 2026-03-31_101500
- Scope: branch-opened
- Covered Nodes: GN-0001, GN-0002
- Reason: append-only expansion
