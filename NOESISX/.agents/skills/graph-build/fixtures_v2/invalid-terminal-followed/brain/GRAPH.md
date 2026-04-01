# GRAPH

## GN-0001
- Type: DECISION
- Slug: terminal-followed
- Opened As: active @ 2026-03-31_090000
- Lineage:
  - none
- Dependencies:
  - none
- Refs:
  - none
- Semantics: |
    终态后又继续写状态，应该失败。

## State Transitions

### ST-0001
- Node: GN-0001
- To: dead
- At: 2026-03-31_091000
- Reason: route declared dead

### ST-0002
- Node: GN-0001
- To: active
- At: 2026-03-31_092000
- Reason: 这里故意在终态后继续写状态
