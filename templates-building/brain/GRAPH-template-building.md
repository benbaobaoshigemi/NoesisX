# GRAPH

> 只增不减。只记录拓扑动作，不记录当前态摘要，不记录普通实验细节。

## Usage Rules

- Allowed Node Types: `ROOT`, `QUESTION`, `HYPOTHESIS`, `METHOD`, `DATA`, `LITERATURE`, `SYNTHESIS`, `DECISION`
- Allowed Lineage Edges: `branch_from`, `decompose_from`, `refine_from`, `merge_from`, `revive_from`, `supersede_from`
- Allowed Dependency Edges: `requires`
- Allowed Node States: `active`, `paused`, `blocked`, `concluded`, `dead`, `absorbed`, `superseded`, `aborted`
- Allowed Events: 新节点开启、新边建立、节点状态转移、只读 checkpoint 压缩记录
- Terminal States: `concluded`, `dead`, `absorbed`, `superseded`, `aborted`
- Terminal nodes must not be revived in place. Use `revive_from` or `supersede_from` on a new node when needed.
- Checkpoints are read-only compression aids, not a second source of truth.
- `GRAPH.md` must use node-ledger style as the formal format.
- `GRAPH.md` is a strict small grammar. In the real file, only `# GRAPH`, node blocks, the `## Checkpoints` section, `### CP-XXXX` checkpoint blocks, blank lines, and comments are allowed.
- `Lineage` and `Dependencies` must always be present. If empty, write `- none`.
- `Opened By`, `Closed By`, and `Detailed Semantics` must point to absolute `experiment.md` paths.
- `Detailed Semantics` must use the `#topology-delta` anchor.

## Node Ledger

### Node Template

```md
## GN-0007
- Type: HYPOTHESIS
- Slug: data-quality-route
- Status: active
- Opened By: /absolute/path/to/experiment/2026-03-28_135210/experiment.md
- Closed By:
- Lineage:
  - branch_from: GN-0003
- Dependencies:
  - requires: GN-0005
- Detailed Semantics: /absolute/path/to/experiment/2026-03-28_135210/experiment.md#topology-delta
```

## Nodes

<!-- 在此处追加节点，不回删旧节点 -->

## Checkpoints

### Checkpoint Template

```md
### CP-0001
- Created At:
- Scope: first-week-topology
- Covered Nodes: GN-0001, GN-0002
- Reason:
```
