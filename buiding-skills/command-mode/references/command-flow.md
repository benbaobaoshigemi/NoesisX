# command flow

## Ordered procedure

### 1. Resolve the directive
Pin down the exact user requirement. Preserve its operational meaning. Do not silently reinterpret broad or ugly commands into cleaner research actions.

### 2. Check feasibility
Decide whether the command is executable in the current environment.

Allowed blockers:
- missing permissions
- missing files
- unavailable tools
- unavailable network or external services
- system-level impossibility

If blocked, report the blocker precisely and stop. Do not claim completion.

### 3. Classify risk
Classify the command as ordinary or high-risk.

High-risk includes actions that are destructive, distorting, irreversible, or likely to degrade research traceability or credibility.

### 4. Preserve state
If the action is materially risky and git is available, create a snapshot commit first.

If git is unavailable:
- say so explicitly
- preserve state using the best local means available
- continue only with that limitation made visible

### 5. Execute exactly
Carry out the instruction. Do not swap in a safer substitute unless the user asked for an alternative or the original command is impossible.

### 6. Log danger
If risk is present, append a new entry to `DANGEROUS.md`.

### 7. Cross-reference
When relevant, update:
- `PROJECT.md`
- the active `Experiment.md`

The purpose is not prose elegance. The purpose is auditability.

## Edge cases

### Risky but reversible
Still log it if it materially affected state or credibility.

### Methodologically bad but executable
Execute and log. Methodological disagreement is not a veto in command mode.

### Ambiguous command
Resolve ambiguity only to the minimum extent needed to execute. Do not expand into a discussion unless the ambiguity blocks execution.

### User explicitly wants harm to project quality
Execute if technically possible, but state the likely consequences and log them plainly.
