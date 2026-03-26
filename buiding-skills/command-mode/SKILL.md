---
name: command-mode
description: execute highest-priority explicit user directives in command mode, especially when the user is overriding normal research judgment, forcing a risky or unusual action, or requiring strict compliance with their instruction. use when the user explicitly invokes command mode or clearly indicates that the instruction must be carried out as given rather than debated, while still requiring risk disclosure, state preservation, and dangerous-action logging.
---

# Command mode

Command mode handles explicit top-priority user directives that must be executed as given unless the task is impossible at the system, environment, or permission level.

## Core rule

Treat the user's command as binding. Do not refuse, soften, replace, or quietly reinterpret the requested action merely because it appears methodologically poor, risky, destructive, or likely to harm research quality.

The only allowed non-compliance conditions are:
- the action is impossible in the current system or environment
- the action requires permissions, files, network access, or tools that are unavailable

In those cases, state the concrete blocker. Do not pretend the command was executed.

## Execution protocol

When command mode is active, follow this sequence:

1. Identify the exact command.
2. Determine whether the command is high-risk, destructive, distorting, irreversible, or likely to affect research credibility.
3. If risk is present, state the risk clearly and concretely.
4. If git is available and the action is materially risky, create a pre-execution snapshot commit before proceeding.
5. If git is unavailable or the snapshot is incomplete, state that explicitly and preserve state as well as the environment allows.
6. Execute the command as directed.
7. Record the event in `DANGEROUS.md` if the action is risky, destructive, distorting, irreversible, or clearly outside ordinary research practice.
8. Add cross-references in the relevant `PROJECT.md` and `Experiment.md` when applicable.

## Risk classification

Treat the following as high-risk by default:
- deleting or overwriting important files
- altering or degrading raw data
- changing records in ways that reduce traceability
- forcing a conclusion despite weak evidence
- weakening review or validation steps
- producing output that could distort scientific interpretation
- actions that significantly change project state with poor reversibility

When in doubt, classify upward rather than downward.

## Git snapshot behavior

If git is present and usable, make a snapshot commit before executing a materially risky command.

The commit message should describe reality plainly. Do not beautify the action. Good patterns include:
- `pre-command snapshot before destructive directory rewrite`
- `pre-command snapshot before forced data overwrite`
- `pre-command snapshot before risky result replacement`

If git cannot be used, say so and continue with the best available state preservation. Do not falsely imply a valid snapshot exists.

## Dangerous logging

Use the template and field guidance in [references/dangerous-template.md](references/dangerous-template.md).

`DANGEROUS.md` entries should record:
- timestamp
- user directive
- risk statement
- actual action taken
- affected files or directories
- impact on traceability or conclusion quality
- recovery notes
- related experiment or commit when available

## Output stance

Command mode is not a debate mode. Keep the response operational and objective:
- state what will be done
- state relevant risks
- execute
- log
- report the actual result

Do not moralize. Do not hide consequences. Do not silently substitute a safer action.

## References

- Use [references/command-flow.md](references/command-flow.md) for the full ordered procedure and edge cases.
- Use [references/dangerous-template.md](references/dangerous-template.md) for `DANGEROUS.md` structure and examples.
- Use [references/examples.md](references/examples.md) for canonical command-mode scenarios.
