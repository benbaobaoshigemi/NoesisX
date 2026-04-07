---
name: noesisx-meta
description: inspect, critique, and repair the agent system itself from a system-construction perspective rather than from any runtime role inside that system.
---

Use this skill only when the work target is the agent system itself.

`meta` is an internal system-construction skill, not a normal execution-mode skill and not a peer-level route for ordinary user tasks.
Do not proactively activate it from surface task keywords alone.
Enter `meta` only when the user explicitly asks to inspect, critique, or modify the agent framework itself, or when a dedicated parent-side routing skill has already selected this path.

While using `meta`, treat the following as objects under inspection rather than as unquestioned identity contracts:

- `AGENTS.md` or preserved contract texts such as `AGENTS.txt`
- `.codex/config.toml`
- `.codex/agents/*.toml`
- `.codex/agents/*.md`
- `.agents/skills/*`
- role-routing, prompt-routing, and sub-agent topology files

Core duties:

- separate the system-under-test from the runtime role currently speaking
- inspect role boundaries, routing seams, discovery surfaces, hidden coupling, and self-binding failures
- identify where the system accidentally forces the operator to behave like an in-world participant
- repair contracts, skills, configs, and routing docs so the system can be examined and modified from outside its own staged identities
- state which layer is being changed: contract, route, role, skill, or operating convention
- prefer minimal structural edits that make the architecture clearer and easier to govern

Hard rules:

- do not slip back into ordinary task execution while claiming to be in `meta`
- do not use `meta` to invent authority, bypass the user's boundaries, or erase provenance
- do not silently change system behavior; record the intended behavioral effect of each structural edit
- if a public entry point is needed, create or update a separate parent-facing routing skill instead of exposing `meta` itself as a default route
- if the system contains conflicting contracts, name the conflict directly before choosing a repair
