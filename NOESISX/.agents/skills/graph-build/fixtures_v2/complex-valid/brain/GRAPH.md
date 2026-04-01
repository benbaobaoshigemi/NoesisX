# GRAPH

## GN-0001
- Type: ROOT
- Slug: project-root
- Opened As: active @ 2026-03-31_090000
- Lineage:
  - none
- Dependencies:
  - none
- Refs:
  - none
- Semantics: |
    项目根节点。
    只描述该节点自身，不描述全局当前态。
- Notes: |
    初始问题已从该节点分叉出去。

## GN-0002
- Type: QUESTION
- Slug: primary-question
- Opened As: active @ 2026-03-31_091500
- Lineage:
  - branch_from: GN-0001
- Dependencies:
  - requires: GN-0003
- Refs:
  - user-instruction: continue-the-project
- Semantics: |
    主问题节点。
    当前状态由最后一条状态历史决定。
- Notes: |
    等待数据质量审查路线返回结果。

## GN-0003
- Type: DATA
- Slug: data-quality-audit
- Opened As: active @ 2026-03-31_092000
- Lineage:
  - decompose_from: GN-0002
- Dependencies:
  - none
- Refs:
  - none
- Semantics: |
    数据质量核查路线。
- Notes: |
    保留最小备注。

## GN-0004
- Type: HYPOTHESIS
- Slug: mechanism-a
- Opened As: active @ 2026-03-31_104500
- Lineage:
  - refine_from: GN-0002
- Dependencies:
  - requires: GN-0003
- Refs:
  - literature: paper-a
- Semantics: |
    机制解释路线。
- Notes: |
    仅保留节点内局部备注。

## State Transitions

### ST-0001
- Node: GN-0001
- To: concluded
- At: 2026-03-31_091000
- Reason: root question split into explicit sub-route

### ST-0002
- Node: GN-0003
- To: concluded
- At: 2026-03-31_101500
- Reason: data quality audit completed

### ST-0003
- Node: GN-0002
- To: blocked
- At: 2026-03-31_103000
- Reason: waiting for audit result absorption

### ST-0004
- Node: GN-0004
- To: paused
- At: 2026-03-31_111000
- Reason: route parked after initial framing

## Checkpoints

### CP-0001
- Created At: 2026-03-31_120000
- Scope: first-pass
- Covered Nodes: GN-0001, GN-0002, GN-0003, GN-0004
- Reason: first stable checkpoint
