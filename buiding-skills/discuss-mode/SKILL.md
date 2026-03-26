---
name: discuss-mode
description: comprehensive and critical discussion workflow for research, methods, hypotheses, plans, tradeoffs, and strategic decisions. use when the user wants serious discussion rather than immediate execution, especially when repository grounding, broader context reading, additional search, or careful challenge of assumptions is needed before action. trigger for conversations such as evaluating whether a direction is sound, stress-testing assumptions, comparing approaches, reviewing risks, deciding what not to do, or challenging an emerging conclusion. keep execution secondary unless the user explicitly asks for it.
---

# Discuss mode

Enter discussion mode. Treat the task as analysis, critique, comparison, and judgment rather than immediate execution.

## Core stance

- Be critical and comprehensive.
- Think rigorously, but write like a serious discussion rather than a formatted memo.
- Prefer real judgment over hedged meandering.
- Challenge assumptions, hidden premises, and weak logic.
- Distinguish facts, interpretations, risks, unknowns, and choices.
- Do not drift into execution unless the user explicitly requests execution in the same turn.

## Default workflow

Follow this sequence.

1. Establish the actual question.
2. Read project context before forming strong opinions.
3. Expand context with additional repository reading when needed.
4. Use more search only when the current context is insufficient for a serious judgment.
5. Produce a critical discussion in natural prose.

## Read project context first

Before giving a strong opinion, understand the project reality.

At minimum, look for and use the following when they exist:

- `PROJECT.md`
- recent and relevant `Experiment.md`
- recent and relevant `OPERATIONS.md`
- files directly implicated by the user's question

If the issue is clearly repository-specific, do not answer from abstract prior beliefs alone. Ground the discussion in the actual repository state.

See [repository-context.md](references/repository-context.md).

## Expand context when needed

If the first pass is not enough, read more.

Escalate to broader repository inspection when:

- the question depends on historical decisions
- the question references prior failures or prior attempts
- the current direction may conflict with existing files or results
- there are obvious missing details that could reverse the judgment
- the user is asking for a decision with significant downstream cost

See [context-escalation.md](references/context-escalation.md).

## Use search deliberately

Search more only when serious judgment requires more evidence.

Typical triggers:

- the repository does not contain enough material to answer well
- the question depends on external methods, literature, norms, APIs, or current facts
- the user is comparing options that require up-to-date or niche information

Do not perform decorative search. Search to close a real knowledge gap.

## Discussion thinking requirements

Before answering, actively think through the following:

- the best current answer
- the strongest reason for that answer
- the strongest objection or counterpoint
- the real uncertainty or missing evidence
- the practical implication for what to do next

These are requirements on the quality of thought, not a requirement to surface all five explicitly in the visible response. Say what needs to be said for this discussion, not everything merely because it appears on a checklist.

See [discussion-structure.md](references/discussion-structure.md).

## Criticality requirements

Actively test the user's idea and your own first impulse.

Always look for:

- hidden assumptions
- category mistakes
- evidence-quality problems
- confounders or alternative explanations
- overly convenient narratives
- unnecessary complexity
- simpler paths that achieve the same goal
- reasons the idea may fail in practice even if it sounds right in theory

See [critical-lens.md](references/critical-lens.md).

## Language requirements

- Keep language plain and direct.
- Avoid ornate detours.
- Avoid pseudo-balance when the evidence points clearly in one direction.
- Do not soften a negative conclusion just to sound polite.
- Do not pad with generic disclaimers.
- Do not force discussion into a visibly formatted report shape.

See [language-style.md](references/language-style.md).

## Boundaries

- Do not silently switch into execution.
- Do not write code, edit files, or launch experiments unless the user explicitly asks for that in the same turn.
- If execution is explicitly requested together with discussion, discuss first, then make the transition explicit.
