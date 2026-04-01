# Experiment

## Metadata

- Experiment ID: EXP-0008
- Created At: 2026-03-30_140000
- Status: success
- Primary Graph Nodes: GN-0008
- Secondary Graph Nodes: GN-0005, GN-0007
- Topology Impact Candidate: yes

## Topology Delta

- Graph Nodes Mentioned: GN-0005, GN-0007, GN-0008
- Actions:
  - open_node: GN-0008
  - add_lineage: GN-0008 supersede_from GN-0005
  - add_dependency: GN-0008 requires GN-0007
  - transition_state: GN-0008 active -> dead
- Rationale: retire mechanism-a under the current decision frame.
- Evidence: the synthesis route no longer supports mechanism-a.
