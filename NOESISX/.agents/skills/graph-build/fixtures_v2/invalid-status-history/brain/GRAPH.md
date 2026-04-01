# GRAPH

## GN-0001
- Type: ROOT
- Slug: bad-status-history
- Opened As: active @ 2026-03-31_090000
- Lineage:
  - none
- Dependencies:
  - none
- Refs:
  - none
- Semantics: |
    这里故意写入非法状态转移。

## State Transitions

### ST-0001
- Node: GN-0001
- To: success
- At: 2026-03-31_091000
- Reason: 这里故意写入非法状态
