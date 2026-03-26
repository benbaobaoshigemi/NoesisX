---
name: rescue-mode
description: use when the workspace, repository, records, outputs, or project state are messy, unclear, or partially broken, especially when the user invokes rescue mode or asks to recover order, reconstruct status, clean up confusion, or regain a trustworthy view of the project.
---

# Rescue Mode

Enter rescue mode.

## Core behavior

Prioritize restoring legibility, order, and traceability before adding new work.

## Rescue sequence

1. Determine the current state of the workspace.
2. Identify critical files, records, outputs, and active branches of work.
3. Read `PROJECT.md` first if present.
4. Read the most relevant `Experiment.md` and `OPERATIONS.md` files.
5. Reconstruct what is current, what is stale, and what is ambiguous.
6. Restore minimum working order.
7. Record unresolved mess explicitly instead of pretending the situation is clean.

## Boundary

Do not continue piling on new experimental work before the basic project state is understandable again.
Rescue mode is for recovering a trustworthy operating picture.
