#!/usr/bin/env python3
"""Validate strict node-ledger GRAPH.md files with append-only state transitions."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


ALLOWED_NODE_TYPES = {
    "ROOT",
    "QUESTION",
    "HYPOTHESIS",
    "METHOD",
    "DATA",
    "LITERATURE",
    "SYNTHESIS",
    "DECISION",
}

ALLOWED_LINEAGE = {
    "branch_from",
    "decompose_from",
    "refine_from",
    "merge_from",
    "revive_from",
    "supersede_from",
}

ALLOWED_DEPENDENCIES = {"requires"}

ALLOWED_STATES = {
    "active",
    "paused",
    "blocked",
    "concluded",
    "dead",
    "absorbed",
    "superseded",
    "aborted",
}

TERMINAL_STATES = {"concluded", "dead", "absorbed", "superseded", "aborted"}

TOP_HEADER_RE = re.compile(r"^#\s+GRAPH\s*$")
NODE_HEADING_RE = re.compile(r"^##\s+(GN-\d{4,})\s*$")
TRANSITION_SECTION_RE = re.compile(r"^##\s+State Transitions\s*$")
TRANSITION_HEADING_RE = re.compile(r"^###\s+(ST-\d{4,})\s*$")
CHECKPOINT_SECTION_RE = re.compile(r"^##\s+Checkpoints\s*$")
CHECKPOINT_HEADING_RE = re.compile(r"^###\s+(CP-\d{4,})\s*$")
KEY_VALUE_RE = re.compile(r"^- ([A-Za-z ]+):\s*(.*)$")
RELATION_ITEM_RE = re.compile(r"^- ([a-z_]+):\s*(GN-\d{4,})\s*$")
REF_ITEM_RE = re.compile(r"^- (.+)$")
NONE_ITEM_RE = re.compile(r"^- none\s*$")
INLINE_STATE_RE = re.compile(r"^([a-z]+)(?:\s+@\s+([0-9_-]+))?$")
COMMENT_RE = re.compile(r"^\s*<!--.*-->\s*$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{6}$")

NODE_KEYS = {
    "Type",
    "Slug",
    "Opened As",
    "Lineage",
    "Dependencies",
    "Refs",
    "Semantics",
    "Notes",
}

TRANSITION_KEYS = {"Node", "To", "At", "Reason"}
CHECKPOINT_KEYS = {"Created At", "Scope", "Covered Nodes", "Reason"}


@dataclass
class StatusEntry:
    state: str
    timestamp: str | None = None


@dataclass
class Node:
    node_id: str
    type: str | None = None
    slug: str | None = None
    opened_as: StatusEntry | None = None
    lineage: list[tuple[str, str]] = field(default_factory=list)
    dependencies: list[tuple[str, str]] = field(default_factory=list)
    refs: list[str] = field(default_factory=list)
    semantics_lines: list[str] = field(default_factory=list)
    notes_lines: list[str] = field(default_factory=list)
    saw_opened_as: bool = False
    saw_lineage: bool = False
    saw_dependencies: bool = False
    saw_refs: bool = False
    saw_semantics: bool = False
    saw_notes: bool = False
    lineage_none: bool = False
    dependencies_none: bool = False
    refs_none: bool = False


@dataclass
class StateTransition:
    label: str
    node_id: str | None = None
    to_state: str | None = None
    at: str | None = None
    reason: str | None = None


@dataclass
class Checkpoint:
    label: str
    created_at: str | None = None
    scope: str | None = None
    covered_nodes: str | None = None
    reason: str | None = None


def parse_inline_state(value: str) -> StatusEntry | None:
    match = INLINE_STATE_RE.match(value.strip())
    if not match:
        return None
    return StatusEntry(match.group(1), match.group(2))


def parse_graph(
    text: str,
) -> tuple[list[Node], list[StateTransition], list[Checkpoint], list[str]]:
    lines = text.splitlines()
    nodes: list[Node] = []
    transitions: list[StateTransition] = []
    checkpoints: list[Checkpoint] = []
    errors: list[str] = []
    saw_header = False
    section = "nodes"
    current_node: Node | None = None
    current_transition: StateTransition | None = None
    current_checkpoint: Checkpoint | None = None
    current_list: str | None = None
    current_block: str | None = None
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        lineno = i + 1

        if current_block is not None:
            if not stripped:
                if current_block == "semantics":
                    current_node.semantics_lines.append("")
                else:
                    current_node.notes_lines.append("")
                i += 1
                continue
            if line.startswith("  "):
                content = line[2:]
                if current_block == "semantics":
                    current_node.semantics_lines.append(content)
                else:
                    current_node.notes_lines.append(content)
                i += 1
                continue
            current_block = None
            continue

        if not stripped:
            current_list = None
            i += 1
            continue
        if COMMENT_RE.match(stripped):
            i += 1
            continue

        if TOP_HEADER_RE.match(line):
            if saw_header or nodes or transitions or checkpoints:
                errors.append(f"line {lineno}: '# GRAPH' must appear exactly once at the top")
            saw_header = True
            i += 1
            continue

        node_heading = NODE_HEADING_RE.match(line)
        if node_heading:
            if not saw_header:
                errors.append(f"line {lineno}: '# GRAPH' header must appear before nodes")
            if section != "nodes":
                errors.append(
                    f"line {lineno}: node blocks must appear before '## State Transitions' and '## Checkpoints'"
                )
            current_list = None
            current_transition = None
            current_checkpoint = None
            current_node = Node(node_id=node_heading.group(1))
            nodes.append(current_node)
            i += 1
            continue

        if TRANSITION_SECTION_RE.match(line):
            if not saw_header:
                errors.append(
                    f"line {lineno}: '# GRAPH' header must appear before state transitions"
                )
            if section == "checkpoints":
                errors.append(
                    f"line {lineno}: '## State Transitions' must appear before '## Checkpoints'"
                )
            section = "transitions"
            current_list = None
            current_node = None
            current_checkpoint = None
            current_transition = None
            i += 1
            continue

        if CHECKPOINT_SECTION_RE.match(line):
            if not saw_header:
                errors.append(f"line {lineno}: '# GRAPH' header must appear before checkpoints")
            section = "checkpoints"
            current_list = None
            current_node = None
            current_transition = None
            current_checkpoint = None
            i += 1
            continue

        if section == "transitions":
            transition_heading = TRANSITION_HEADING_RE.match(line)
            if transition_heading:
                current_transition = StateTransition(label=transition_heading.group(1))
                transitions.append(current_transition)
                i += 1
                continue

            if current_transition is None:
                errors.append(
                    f"line {lineno}: state transition content must be inside a '### ST-XXXX' block"
                )
                i += 1
                continue

            key_value = KEY_VALUE_RE.match(stripped)
            if not key_value:
                errors.append(f"line {lineno}: unrecognized state transition content: {stripped}")
                i += 1
                continue

            key, value = key_value.groups()
            if key not in TRANSITION_KEYS:
                errors.append(f"line {lineno}: unknown state transition key '{key}'")
                i += 1
                continue
            if key == "Node":
                current_transition.node_id = value.strip()
            elif key == "To":
                current_transition.to_state = value.strip()
            elif key == "At":
                current_transition.at = value.strip()
            elif key == "Reason":
                current_transition.reason = value.strip()
            i += 1
            continue

        if section == "checkpoints":
            checkpoint_heading = CHECKPOINT_HEADING_RE.match(line)
            if checkpoint_heading:
                current_checkpoint = Checkpoint(label=checkpoint_heading.group(1))
                checkpoints.append(current_checkpoint)
                i += 1
                continue

            if current_checkpoint is None:
                errors.append(
                    f"line {lineno}: checkpoint content must be inside a '### CP-XXXX' block"
                )
                i += 1
                continue

            key_value = KEY_VALUE_RE.match(stripped)
            if not key_value:
                errors.append(f"line {lineno}: unrecognized checkpoint content: {stripped}")
                i += 1
                continue

            key, value = key_value.groups()
            if key not in CHECKPOINT_KEYS:
                errors.append(f"line {lineno}: unknown checkpoint key '{key}'")
                i += 1
                continue
            if key == "Created At":
                current_checkpoint.created_at = value.strip()
            elif key == "Scope":
                current_checkpoint.scope = value.strip()
            elif key == "Covered Nodes":
                current_checkpoint.covered_nodes = value.strip()
            elif key == "Reason":
                current_checkpoint.reason = value.strip()
            i += 1
            continue

        if current_node is None:
            errors.append(f"line {lineno}: unrecognized top-level content: {stripped}")
            i += 1
            continue

        key_value = KEY_VALUE_RE.match(stripped)
        if key_value and key_value.group(1) in NODE_KEYS:
            key, value = key_value.groups()
            value = value.strip()
            current_list = None
            if key == "Type":
                current_node.type = value
            elif key == "Slug":
                current_node.slug = value
            elif key == "Opened As":
                current_node.saw_opened_as = True
                if not value:
                    errors.append(f"line {lineno}: Opened As must carry an inline state value")
                else:
                    entry = parse_inline_state(value)
                    if entry is None:
                        errors.append(f"line {lineno}: invalid Opened As value '{value}'")
                    else:
                        current_node.opened_as = entry
            elif key == "Lineage":
                if value:
                    errors.append(f"line {lineno}: Lineage must not carry an inline value")
                current_node.saw_lineage = True
                current_node.lineage_none = False
                current_list = "lineage"
            elif key == "Dependencies":
                if value:
                    errors.append(f"line {lineno}: Dependencies must not carry an inline value")
                current_node.saw_dependencies = True
                current_node.dependencies_none = False
                current_list = "dependencies"
            elif key == "Refs":
                if value:
                    errors.append(f"line {lineno}: Refs must not carry an inline value")
                current_node.saw_refs = True
                current_node.refs_none = False
                current_list = "refs"
            elif key == "Semantics":
                current_node.saw_semantics = True
                if value != "|":
                    errors.append(f"line {lineno}: Semantics must use a wrapped block with '|'")
                else:
                    current_block = "semantics"
            elif key == "Notes":
                current_node.saw_notes = True
                if value != "|":
                    errors.append(f"line {lineno}: Notes must use a wrapped block with '|'")
                else:
                    current_block = "notes"
            i += 1
            continue

        if current_list == "lineage":
            if NONE_ITEM_RE.match(stripped):
                if current_node.lineage:
                    errors.append(f"line {lineno}: '- none' cannot appear after lineage entries")
                current_node.lineage_none = True
                i += 1
                continue
            match = RELATION_ITEM_RE.match(stripped)
            if not match:
                errors.append(f"line {lineno}: invalid lineage entry in node {current_node.node_id}")
                i += 1
                continue
            if current_node.lineage_none:
                errors.append(f"line {lineno}: lineage entries cannot appear after '- none'")
            current_node.lineage.append((match.group(1), match.group(2)))
            i += 1
            continue

        if current_list == "dependencies":
            if NONE_ITEM_RE.match(stripped):
                if current_node.dependencies:
                    errors.append(f"line {lineno}: '- none' cannot appear after dependency entries")
                current_node.dependencies_none = True
                i += 1
                continue
            match = RELATION_ITEM_RE.match(stripped)
            if not match:
                errors.append(
                    f"line {lineno}: invalid dependency entry in node {current_node.node_id}"
                )
                i += 1
                continue
            if current_node.dependencies_none:
                errors.append(f"line {lineno}: dependency entries cannot appear after '- none'")
            current_node.dependencies.append((match.group(1), match.group(2)))
            i += 1
            continue

        if current_list == "refs":
            if NONE_ITEM_RE.match(stripped):
                if current_node.refs:
                    errors.append(f"line {lineno}: '- none' cannot appear after refs entries")
                current_node.refs_none = True
                i += 1
                continue
            match = REF_ITEM_RE.match(stripped)
            if not match:
                errors.append(f"line {lineno}: invalid refs entry in node {current_node.node_id}")
                i += 1
                continue
            if current_node.refs_none:
                errors.append(f"line {lineno}: refs entries cannot appear after '- none'")
            current_node.refs.append(match.group(1).strip())
            i += 1
            continue

        if key_value:
            errors.append(f"line {lineno}: unknown key '{key_value.group(1)}' in node {current_node.node_id}")
            i += 1
            continue

        errors.append(f"line {lineno}: unrecognized content in node {current_node.node_id}: {stripped}")
        i += 1

    if not saw_header:
        errors.append("missing '# GRAPH' header")
    if not nodes:
        errors.append("no node-ledger entries found; GRAPH.md must use node-ledger form")

    return nodes, transitions, checkpoints, errors


def validate_graph(
    nodes: list[Node],
    transitions: list[StateTransition],
    checkpoints: list[Checkpoint],
) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    seen_node_ids: set[str] = set()
    seen_transition_ids: set[str] = set()
    seen_checkpoint_ids: set[str] = set()
    nodes_by_id = {node.node_id: node for node in nodes}
    transitions_by_node: dict[str, list[StateTransition]] = {}
    edge_count = 0

    for node in nodes:
        if node.node_id in seen_node_ids:
            errors.append(f"{node.node_id}: duplicate node id")
        seen_node_ids.add(node.node_id)

        if not node.type:
            errors.append(f"{node.node_id}: missing Type")
        elif node.type not in ALLOWED_NODE_TYPES:
            errors.append(f"{node.node_id}: invalid Type '{node.type}'")

        if not node.slug:
            errors.append(f"{node.node_id}: missing Slug")
        elif not SLUG_RE.match(node.slug):
            errors.append(f"{node.node_id}: Slug must use lowercase kebab-case")

        if not node.saw_opened_as:
            errors.append(f"{node.node_id}: missing Opened As field")
        elif node.opened_as is None:
            errors.append(f"{node.node_id}: Opened As must contain a valid state")
        else:
            if node.opened_as.state not in ALLOWED_STATES:
                errors.append(f"{node.node_id}: invalid opened state '{node.opened_as.state}'")
            if node.opened_as.timestamp and not TIMESTAMP_RE.match(node.opened_as.timestamp):
                errors.append(
                    f"{node.node_id}: invalid opened timestamp '{node.opened_as.timestamp}'"
                )

        if not node.saw_lineage:
            errors.append(f"{node.node_id}: missing Lineage field")
        elif not node.lineage and not node.lineage_none:
            errors.append(f"{node.node_id}: Lineage must contain entries or '- none'")

        if not node.saw_dependencies:
            errors.append(f"{node.node_id}: missing Dependencies field")
        elif not node.dependencies and not node.dependencies_none:
            errors.append(f"{node.node_id}: Dependencies must contain entries or '- none'")

        if node.saw_refs and not node.refs and not node.refs_none:
            errors.append(f"{node.node_id}: Refs must contain entries or '- none'")

        if not node.saw_semantics:
            errors.append(f"{node.node_id}: missing Semantics field")
        elif not any(line.strip() for line in node.semantics_lines):
            errors.append(f"{node.node_id}: Semantics block must not be empty")

        if node.saw_notes and not any(line.strip() for line in node.notes_lines):
            errors.append(f"{node.node_id}: Notes block must not be empty")

        for relation, target in node.lineage:
            if relation not in ALLOWED_LINEAGE:
                errors.append(f"{node.node_id}: invalid lineage relation '{relation}'")
            if target not in nodes_by_id:
                errors.append(f"{node.node_id}: lineage target does not exist: {target}")
            edge_count += 1

        for relation, target in node.dependencies:
            if relation not in ALLOWED_DEPENDENCIES:
                errors.append(f"{node.node_id}: invalid dependency relation '{relation}'")
            if target not in nodes_by_id:
                errors.append(f"{node.node_id}: dependency target does not exist: {target}")
            edge_count += 1

    for transition in transitions:
        if transition.label in seen_transition_ids:
            errors.append(f"state transition '{transition.label}': duplicate transition id")
        seen_transition_ids.add(transition.label)

        missing = []
        if not transition.node_id:
            missing.append("Node")
        if not transition.to_state:
            missing.append("To")
        if not transition.at:
            missing.append("At")
        if not transition.reason:
            missing.append("Reason")
        if missing:
            errors.append(
                f"state transition '{transition.label}': missing required fields: {', '.join(missing)}"
            )
            continue

        if transition.node_id not in nodes_by_id:
            errors.append(
                f"state transition '{transition.label}': node does not exist: {transition.node_id}"
            )
        else:
            transitions_by_node.setdefault(transition.node_id, []).append(transition)

        if transition.to_state not in ALLOWED_STATES:
            errors.append(
                f"state transition '{transition.label}': invalid target state '{transition.to_state}'"
            )
        if not TIMESTAMP_RE.match(transition.at):
            errors.append(f"state transition '{transition.label}': invalid At '{transition.at}'")

    for node in nodes:
        if node.opened_as is None:
            continue

        lifecycle = [node.opened_as]
        for transition in transitions_by_node.get(node.node_id, []):
            lifecycle.append(StatusEntry(transition.to_state, transition.at))

        for index, entry in enumerate(lifecycle[:-1]):
            if entry.state in TERMINAL_STATES:
                errors.append(
                    f"{node.node_id}: terminal state '{entry.state}' cannot be followed by later states"
                )

    for checkpoint in checkpoints:
        if checkpoint.label in seen_checkpoint_ids:
            errors.append(f"checkpoint '{checkpoint.label}': duplicate checkpoint id")
        seen_checkpoint_ids.add(checkpoint.label)

        missing = []
        if not checkpoint.created_at:
            missing.append("Created At")
        elif not TIMESTAMP_RE.match(checkpoint.created_at):
            errors.append(
                f"checkpoint '{checkpoint.label}': invalid Created At '{checkpoint.created_at}'"
            )
        if not checkpoint.scope:
            missing.append("Scope")
        if not checkpoint.covered_nodes:
            missing.append("Covered Nodes")
        if not checkpoint.reason:
            missing.append("Reason")
        if missing:
            errors.append(
                f"checkpoint '{checkpoint.label}': missing required fields: {', '.join(missing)}"
            )
            continue

        covered = [part.strip() for part in checkpoint.covered_nodes.split(",") if part.strip()]
        for node_id in covered:
            if node_id not in nodes_by_id:
                errors.append(
                    f"checkpoint '{checkpoint.label}': covered node does not exist: {node_id}"
                )

    summary = {
        "node_count": len(nodes),
        "edge_count": edge_count,
        "transition_count": len(transitions),
        "checkpoint_count": len(checkpoints),
    }
    return errors, summary


def node_signature(node: Node) -> tuple[object, ...]:
    opened_state = None
    opened_at = None
    if node.opened_as is not None:
        opened_state = node.opened_as.state
        opened_at = node.opened_as.timestamp

    return (
        node.node_id,
        node.type,
        node.slug,
        opened_state,
        opened_at,
        tuple(node.lineage),
        tuple(node.dependencies),
        tuple(node.refs),
        tuple(node.semantics_lines),
        tuple(node.notes_lines),
        node.saw_refs,
        node.saw_notes,
        node.lineage_none,
        node.dependencies_none,
        node.refs_none,
    )


def transition_signature(transition: StateTransition) -> tuple[object, ...]:
    return (
        transition.label,
        transition.node_id,
        transition.to_state,
        transition.at,
        transition.reason,
    )


def checkpoint_signature(checkpoint: Checkpoint) -> tuple[object, ...]:
    return (
        checkpoint.label,
        checkpoint.created_at,
        checkpoint.scope,
        checkpoint.covered_nodes,
        checkpoint.reason,
    )


def validate_append_only(
    baseline_nodes: list[Node],
    baseline_transitions: list[StateTransition],
    baseline_checkpoints: list[Checkpoint],
    nodes: list[Node],
    transitions: list[StateTransition],
    checkpoints: list[Checkpoint],
) -> list[str]:
    errors: list[str] = []

    if len(nodes) < len(baseline_nodes):
        errors.append(
            "append-only violation: node count is smaller than the baseline; old nodes appear to have been removed"
        )
        return errors

    if len(transitions) < len(baseline_transitions):
        errors.append(
            "append-only violation: state transition count is smaller than the baseline; old transitions appear to have been removed"
        )
        return errors

    if len(checkpoints) < len(baseline_checkpoints):
        errors.append(
            "append-only violation: checkpoint count is smaller than the baseline; old checkpoints appear to have been removed"
        )
        return errors

    for index, baseline_node in enumerate(baseline_nodes):
        current_node = nodes[index]
        if node_signature(current_node) != node_signature(baseline_node):
            errors.append(
                "append-only violation: "
                f"existing node changed at position {index + 1} ({baseline_node.node_id})"
            )

    for index, baseline_transition in enumerate(baseline_transitions):
        current_transition = transitions[index]
        if transition_signature(current_transition) != transition_signature(baseline_transition):
            errors.append(
                "append-only violation: "
                f"existing state transition changed at position {index + 1} ({baseline_transition.label})"
            )

    for index, baseline_checkpoint in enumerate(baseline_checkpoints):
        current_checkpoint = checkpoints[index]
        if checkpoint_signature(current_checkpoint) != checkpoint_signature(baseline_checkpoint):
            errors.append(
                "append-only violation: "
                f"existing checkpoint changed at position {index + 1} ({baseline_checkpoint.label})"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph_path", type=Path)
    parser.add_argument(
        "--baseline",
        type=Path,
        help="Path to the exact pre-edit GRAPH.md snapshot. When provided, existing nodes, state transitions, and checkpoints must remain unchanged.",
    )
    args = parser.parse_args()

    if not args.graph_path.exists():
        print(f"GRAPH file does not exist: {args.graph_path}", file=sys.stderr)
        return 1

    text = args.graph_path.read_text(encoding="utf-8")
    nodes, transitions, checkpoints, parse_errors = parse_graph(text)
    validation_errors, summary = validate_graph(nodes, transitions, checkpoints)
    errors = parse_errors + validation_errors

    if args.baseline is not None:
        if not args.baseline.exists():
            errors.append(f"baseline GRAPH file does not exist: {args.baseline}")
        else:
            baseline_text = args.baseline.read_text(encoding="utf-8")
            baseline_nodes, baseline_transitions, baseline_checkpoints, baseline_parse_errors = (
                parse_graph(baseline_text)
            )
            baseline_validation_errors, _ = validate_graph(
                baseline_nodes,
                baseline_transitions,
                baseline_checkpoints,
            )
            if baseline_parse_errors or baseline_validation_errors:
                errors.append("baseline GRAPH file is invalid; cannot enforce append-only check")
                errors.extend(f"baseline: {error}" for error in baseline_parse_errors)
                errors.extend(f"baseline: {error}" for error in baseline_validation_errors)
            else:
                errors.extend(
                    validate_append_only(
                        baseline_nodes,
                        baseline_transitions,
                        baseline_checkpoints,
                        nodes,
                        transitions,
                        checkpoints,
                    )
                )

    if errors:
        print("GRAPH_LINT_FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "GRAPH_LINT_OK "
        f"nodes={summary['node_count']} "
        f"edges={summary['edge_count']} "
        f"transitions={summary['transition_count']} "
        f"checkpoints={summary['checkpoint_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
