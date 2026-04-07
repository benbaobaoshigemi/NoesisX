---
name: fetcher-library-index-ingest
description: Use when material enters `library/` or when `library/INDEX.md` must be created or updated with provenance, purpose, and status metadata. Do not use for materials that are only glanced at and not formally kept.
---

Use this skill when something is being formally admitted into `library/`.

The goal is not to hoard files. The goal is to keep materials traceable and reusable.

## Required metadata

For each item entering `library/INDEX.md`, capture at least:

- file or directory name
- material type
- source or acquisition method
- acquisition time
- reason for keeping it
- related route, graph node, or experiment
- current status
- short note on credibility or usage cautions

Managed statuses:

- `仅收藏`
- `待阅读`
- `已阅读`
- `已引用`
- `已弃用`

## Workflow

1. Confirm the material is being kept formally rather than inspected transiently.
2. Save or identify the stable path under `library/`.
3. Capture provenance before interpretation.
4. Record the minimum metadata in `library/INDEX.md`.
5. Distinguish clearly between:
   - `仅收藏`
   - `待阅读`
   - `已阅读`
   - `已引用`
   - `已弃用`

## Never do this

- Do not treat ingestion as acceptance into the main line.
- Do not omit source information when it exists.
- Do not hide weak credibility; record the caution.
- Do not silently discard contradictory materials.
- Do not invent a route or graph relation when it is still unknown; record the uncertainty instead.
