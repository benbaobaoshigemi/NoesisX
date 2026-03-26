---
name: Discover Mode
description: open-ended sustained research mode for codex. use when the user explicitly invokes /discover or asks for continuous exploration, iterative investigation, autonomous direction shifts, or persistent problem finding inside the current project. this skill is for situations where codex should keep exploring instead of stopping at the first reasonable answer, and where stopping is only allowed after a clearly stated boundary is reached.
---

# discover

## overview

Enter an open-ended research mode. Keep exploring the current project, current materials, and any reachable external information until a real stopping boundary is reached.

This mode is not ordinary execution. It allows autonomous direction shifts, parallel exploration, and persistent iteration. Every direction change must be recorded honestly.

## core behavior

In discover mode:

- do not stop after the first workable answer
- do not treat a single pass as completion
- do not confuse temporary lack of ideas with a valid stopping condition
- do not stay trapped in one narrow direction if the evidence suggests a better line of inquiry
- keep the research centered on the project, but allow justified direction shifts when the evidence supports them

When changing direction, record:

- what line of inquiry is being deprioritized or abandoned
- why it is being deprioritized or abandoned
- what new direction is being pursued
- what evidence or pressure triggered the shift

For operational updates and recordkeeping, use:

- [discover records](references/discover-records.md)
- [stopping boundaries](references/discover-stop-boundaries.md)
- [subagent policy](references/discover-subagents.md)
- [examples](references/discover-examples.md)

## minimum deliverables

When discover mode stops, all of the following are required:

1. a chat-window summary of what was explored, what changed, and why the mode is stopping
2. an update to `PROJECT.md`
3. an update to the relevant `Experiment.md`
4. an update to `OPERATIONS.md`

Discover mode does not default to producing a formal deliverable file.

## stopping rule

Stopping is allowed only when one of the five official stopping boundaries is reached. The full definitions are in [discover-stop-boundaries.md](references/discover-stop-boundaries.md).

The allowed boundaries are:

1. information exhaustion boundary
2. path exhaustion boundary
3. critical missing input boundary
4. contamination-risk boundary
5. no-net-new-signal after external perturbation boundary

When stopping, explicitly name which boundary has been reached and justify it with project-specific evidence.

## subagent privileges

Discover mode has the highest subagent privilege level.

It may use both:

- one-shot subagents for auditing, rebuttal, feasibility checks, and boundary testing
- exploratory subagents for sustained local exploration of different directions

The governing rules are in [discover-subagents.md](references/discover-subagents.md).

The main distinctions are:

- one-shot subagents return a compressed result and then end immediately
- exploratory subagents may persist across multiple turns of local work inside discover mode
- final integration authority always remains with the main agent

When the main agent thinks "this is done" or "I have no idea what to do next," it must not stop immediately. It must first use external perturbation through at least one new one-shot subagent, then re-evaluate.

## recordkeeping discipline

Discover mode must maintain a clear separation between:

- scientific findings and interpretations
- operational work and workspace modifications

Use `Experiment.md` for scientific investigation, results, interpretations, and conclusions.
Use `OPERATIONS.md` for directory work, file movement, exports, formatting, visualization generation, encoding repair, environment repair, and other non-experimental operations.

All file-written text must follow the project's de-dialogization rules. Files are independent documents for third-party readers, not responses to the user.

## tone and output discipline

When summarizing discover work:

- be concrete
- be honest about uncertainty
- distinguish observation, analysis, interpretation, and next direction
- avoid pretending that a direction was always obvious
- avoid smoothing over abandoned paths

## explicit anti-patterns

Do not do any of the following:

- stop because a single pass produced a decent-looking answer
- stop because the current direction feels familiar or comfortable
- hide a direction shift instead of recording it
- keep grinding a direction that has entered garbage time
- treat a missing resource as if it were a mere lack of effort
- let exploratory subagents silently take over final judgment

## invocation examples

Use this skill when the user says things like:

- "/discover"
- "keep digging until there is a real boundary"
- "don't stop at the first answer"
- "change direction if the evidence tells you to"
- "treat this like open-ended research"
