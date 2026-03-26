# discover stopping boundaries

Discover mode may stop only when one of the following five boundaries is reached.

## 1. information exhaustion boundary

Use this boundary when the available materials have already been examined, cross-compared, reorganized, and squeezed to the point that additional work would mostly repeat the same observations.

Typical signs:

- the same files, logs, plots, tables, and notes keep yielding the same signal
- re-reading mostly rewrites the same observation in different words
- external information that is reachable has already been checked and integrated
- the expected information gain from more passes is extremely low

A valid stop note must say:

- which materials have already been examined
- why the expected information gain is near zero

## 2. path exhaustion boundary

Use this boundary when the available methods have been substantially exhausted under current constraints.

Typical signs:

- the reasonable statistical tests have already been run
- the plausible hypothesis cuts have already been tried
- obvious alternative explanations have already been compared
- relevant one-shot subagents have already been used
- remaining actions would mostly be cosmetic variants of earlier attempts

A valid stop note must say:

- which methods or paths were tried
- why remaining paths are only superficial variants

## 3. critical missing input boundary

Use this boundary when continued progress depends on a decisive input that does not exist in the current environment.

Typical examples:

- missing raw data
- missing variable definitions
- missing experimental conditions
- missing permissions
- missing upstream records
- missing metadata needed for interpretation

A valid stop note must say:

- what is missing
- why it is decisive rather than merely helpful

## 4. contamination-risk boundary

Use this boundary when continuing would significantly increase the risk of misinterpretation, overfitting, pseudo-discovery, or historical contamination.

Typical signs:

- the sample is too small for the remaining claims
- the records are too dirty
- encoding or parsing integrity is still unresolved
- variable definitions are no longer trustworthy
- remaining analysis would become increasingly opportunistic

A valid stop note must say:

- what kind of contamination or distortion risk is increasing
- why stopping preserves research quality better than continuing

## 5. no-net-new-signal after external perturbation boundary

Use this boundary only after the main agent has reached a local end state, then deliberately invoked at least one fresh one-shot subagent for audit, rebuttal, feasibility testing, or blind-spot search.

If the external perturbation still produces no meaningful new direction, discover mode may stop.

A valid stop note must say:

- what type of external perturbation was used
- what it checked
- why it failed to produce a meaningful new direction
