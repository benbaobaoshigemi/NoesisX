# GRAPH

## GN-0001
- Type: ROOT
- Slug: project-root
- Status: concluded
- Opened By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_090000/experiment.md
- Closed By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_090000/experiment.md
- Lineage:
  - none
- Dependencies:
  - none
- Detailed Semantics: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_090000/experiment.md#topology-delta

## GN-0002
- Type: QUESTION
- Slug: primary-research-question
- Status: active
- Opened By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_091500/experiment.md
- Closed By:
- Lineage:
  - branch_from: GN-0001
- Dependencies:
  - none
- Detailed Semantics: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_091500/experiment.md#topology-delta

## GN-0003
- Type: DATA
- Slug: sample-quality-audit
- Status: concluded
- Opened By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_093000/experiment.md
- Closed By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_093000/experiment.md
- Lineage:
  - decompose_from: GN-0002
- Dependencies:
  - none
- Detailed Semantics: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_093000/experiment.md#topology-delta

## GN-0004
- Type: METHOD
- Slug: baseline-analysis-route
- Status: active
- Opened By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_101500/experiment.md
- Closed By:
- Lineage:
  - branch_from: GN-0002
- Dependencies:
  - requires: GN-0003
- Detailed Semantics: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_101500/experiment.md#topology-delta

## GN-0005
- Type: HYPOTHESIS
- Slug: mechanism-a
- Status: paused
- Opened By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_110000/experiment.md
- Closed By:
- Lineage:
  - refine_from: GN-0004
- Dependencies:
  - requires: GN-0003
- Detailed Semantics: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_110000/experiment.md#topology-delta

## GN-0006
- Type: LITERATURE
- Slug: external-evidence-pass
- Status: concluded
- Opened By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_114500/experiment.md
- Closed By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_114500/experiment.md
- Lineage:
  - branch_from: GN-0002
- Dependencies:
  - requires: GN-0005
- Detailed Semantics: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_114500/experiment.md#topology-delta

## GN-0007
- Type: SYNTHESIS
- Slug: combined-judgment
- Status: blocked
- Opened By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_123000/experiment.md
- Closed By:
- Lineage:
  - merge_from: GN-0004
  - merge_from: GN-0006
- Dependencies:
  - requires: GN-0005
- Detailed Semantics: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_123000/experiment.md#topology-delta

## GN-0008
- Type: DECISION
- Slug: retire-mechanism-a
- Status: dead
- Opened By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_140000/experiment.md
- Closed By: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_140000/experiment.md
- Lineage:
  - supersede_from: GN-0005
- Dependencies:
  - requires: GN-0007
- Detailed Semantics: /Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/fixtures/complex-valid/experiment/2026-03-30_140000/experiment.md#topology-delta

## Checkpoints

### CP-0001
- Created At: 2026-03-30_150000
- Scope: first-week-topology
- Covered Nodes: GN-0001, GN-0002, GN-0003, GN-0004, GN-0005, GN-0006, GN-0007, GN-0008
- Reason: speed up future reads without replacing node ledger
