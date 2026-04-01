#!/usr/bin/env python3
"""Validate strict node-ledger GRAPH.md files."""

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
CHECKPOINT_SECTION_RE = re.compile(r"^##\s+Checkpoints\s*$")
CHECKPOINT_HEADING_RE = re.compile(r"^###\s+(CP-\d{4,})\s*$")
KEY_VALUE_RE = re.compile(r"^- ([A-Za-z ]+):\s*(.*)$")
RELATION_ITEM_RE = re.compile(r"^- ([a-z_]+):\s*(GN-\d{4,})\s*$")
STATE_ITEM_RE = re.compile(r"^- ([a-z]+)(?:\s+@\s+([0-9_-]+))?\s*$")
REF_ITEM_RE = re.compile(r"^- (.+)$")
NONE_ITEM_RE = re.compile(r"^- none\s*$")
COMMENT_RE = re.compile(r"^\s*<!--.*-->\s*$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{6}$")

NODE_KEYS = {
    "Type",
    "Slug",
    "Status History",
    "Lineage",
    "Dependencies",
    "Refs",
    "Semantics",
    "Notes",
}

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
    status_history: list[StatusEntry] = field(default_factory=list)
    lineage: list[tuple[str, str]] = field(default_factory=list)
    dependencies: list[tuple[str, str]] = field(default_factory=list)
    refs: list[str] = field(default_factory=list)
    semantics_lines: list[str] = field(default_factory=list)
    notes_lines: list[str] = field(default_factory=list)
    saw_status_history: bool = False
    saw_lineage: bool = False
    saw_dependencies: bool = False
    saw_refs: bool = False
    saw_semantics: bool = False
    saw_notes: bool = False
    status_none: bool = False
    lineage_none: bool = False
    dependencies_none: bool = False
    refs_none: bool = False


@dataclass
class Checkpoint:
    label: str
    created_at: str | None = None
    scope: str | None = None
    covered_nodes: str | None = None
    reason: str | None = None


def parse_graph(text: str) -> tuple[list[Node], list[Checkpoint], list[str]]:
    lines = text.splitlines()
    nodes: list[Node] = []
    checkpoints: list[Checkpoint] = []
    errors: list[str] = []
    saw_header = False
    in_checkpoints = False
    current_node: Node | None = None
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
            if saw_header or nodes or checkpoints:
                errors.append(f"line {lineno}: '# GRAPH' must appear exactly once at the top")
            saw_header = True
            i += 1
            continue

        node_heading = NODE_HEADING_RE.match(line)
        if node_heading:
            if not saw_header:
                errors.append(f"line {lineno}: '# GRAPH' header must appear before nodes")
            in_checkpoints = False
            current_checkpoint = None
            current_list = None
            current_node = Node(node_id=node_heading.group(1))
            nodes.append(current_node)
            i += 1
            continue

        if CHECKPOINT_SECTION_RE.match(line):
            if not saw_header:
                errors.append(f"line {lineno}: '# GRAPH' header must appear before checkpoints")
            in_checkpoints = True
            current_node = None
            current_checkpoint = None
            current_list = None
            i += 1
            continue

        if in_checkpoints:
            checkpoint_heading = CHECKPOINT_HEADING_RE.match(line)
            if checkpoint_heading:
                current_checkpoint = Checkpoint(label=checkpoint_heading.group(1))
                checkpoints.append(current_checkpoint)
                i += 1
                continue

            if current_checkpoint is None:
                errors.append(f"line {lineno}: checkpoint content must be inside a '### CP-XXXX' block")
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
            elif key == "Status History":
                if value:
                    errors.append(f"line {lineno}: Status History must not carry an inline value")
                current_node.saw_status_history = True
                current_node.status_none = False
                current_list = "status_history"
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

        if current_list == "status_history":
            if NONE_ITEM_RE.match(stripped):
                if current_node.status_history:
                    errors.append(f"line {lineno}: '- none' cannot appear after status history entries")
                current_node.status_none = True
                i += 1
                continue
            match = STATE_ITEM_RE.match(stripped)
            if not match:
                errors.append(f"line {lineno}: invalid status history entry in node {current_node.node_id}")
                i += 1
                continue
            if current_node.status_none:
                errors.append(f"line {lineno}: status history entries cannot appear after '- none'")
            current_node.status_history.append(StatusEntry(match.group(1), match.group(2)))
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
                errors.append(f"line {lineno}: invalid dependency entry in node {current_node.node_id}")
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
    return nodes, checkpoints, errors


def validate_graph(nodes: list[Node], checkpoints: list[Checkpoint]) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    seen_node_ids: set[str] = set()
    seen_checkpoint_ids: set[str] = set()
    nodes_by_id = {node.node_id: node for node in nodes}
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

        if not node.saw_status_history:
            errors.append(f"{node.node_id}: missing Status History field")
        elif not node.status_history and not node.status_none:
            errors.append(f"{node.node_id}: Status History must contain entries")
        elif node.status_none:
            errors.append(f"{node.node_id}: Status History cannot be '- none'")

        for index, entry in enumerate(node.status_history):
            if entry.state not in ALLOWED_STATES:
                errors.append(f"{node.node_id}: invalid status history state '{entry.state}'")
            if entry.timestamp and not TIMESTAMP_RE.match(entry.timestamp):
                errors.append(f"{node.node_id}: invalid status history timestamp '{entry.timestamp}'")
            if index < len(node.status_history) - 1 and entry.state in TERMINAL_STATES:
                errors.append(
                    f"{node.node_id}: terminal state '{entry.state}' cannot be followed by later states"
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
        "checkpoint_count": len(checkpoints),
    }
    return errors, summary


def node_signature(node: Node) -> tuple[object, ...]:
    return (
        node.node_id,
        node.type,
        node.slug,
        tuple((entry.state, entry.timestamp) for entry in node.status_history),
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
    baseline_checkpoints: list[Checkpoint],
    nodes: list[Node],
    checkpoints: list[Checkpoint],
) -> list[str]:
    errors: list[str] = []

    if len(nodes) < len(baseline_nodes):
        errors.append(
            "append-only violation: node count is smaller than the baseline; old nodes appear to have been removed"
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
        help="Path to the exact pre-edit GRAPH.md snapshot. When provided, existing nodes/checkpoints must remain unchanged.",
    )
    args = parser.parse_args()

    if not args.graph_path.exists():
        print(f"GRAPH file does not exist: {args.graph_path}", file=sys.stderr)
        return 1

    text = args.graph_path.read_text(encoding="utf-8")
    nodes, checkpoints, parse_errors = parse_graph(text)
    validation_errors, summary = validate_graph(nodes, checkpoints)
    errors = parse_errors + validation_errors

    if args.baseline is not None:
        if not args.baseline.exists():
            errors.append(f"baseline GRAPH file does not exist: {args.baseline}")
        else:
            baseline_text = args.baseline.read_text(encoding="utf-8")
            baseline_nodes, baseline_checkpoints, baseline_parse_errors = parse_graph(
                baseline_text
            )
            baseline_validation_errors, _ = validate_graph(
                baseline_nodes,
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
                        baseline_checkpoints,
                        nodes,
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
        f"checkpoints={summary['checkpoint_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
