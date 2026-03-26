# discover subagent policy

Discover mode has the highest subagent privilege level.

## two classes of subagents

### a. one-shot subagents

Purpose:

- audit a promising line
- rebut the current favorite explanation
- test feasibility
- search for blind spots
- help judge whether a stopping boundary is actually real

Rules:

- return a compressed answer
- end immediately after returning
- do not get reused later
- each new perturbation should use a fresh instance

### b. exploratory subagents

Purpose:

- act like temporary local researchers exploring a specific branch
- pursue a direction across multiple local steps
- compare multiple branches in parallel
- continue probing where the main agent would otherwise become bottlenecked

Rules:

- may persist within the life of the current discover run
- must stay inside their assigned local direction
- must not silently assume control of the global research narrative
- final integration authority always belongs to the main agent

## mandatory perturbation rule

When the main agent thinks either of the following:

- "I think this is done"
- "I don't know what to do next"

it must not stop immediately. It must first trigger at least one fresh one-shot subagent, then re-evaluate.

## when to prefer exploratory subagents

Prefer exploratory subagents when:

- multiple plausible directions exist at once
- one branch would take too long and block the main agent
- the project benefits from genuine branch diversification
- a sustained local research loop is needed

## when not to overuse subagents

Do not create subagents just for theater.

Avoid unnecessary proliferation when:

- the task is still simple and single-threaded
- the new branch is not meaningfully distinct
- the expected gain is mostly cosmetic
- the main agent has not yet done enough direct work to justify branching
