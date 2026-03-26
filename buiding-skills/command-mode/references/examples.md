# examples

## example 1: destructive workspace rewrite
User intent: force replacement of a directory even though the prior state may matter.

Expected behavior:
- classify as high-risk
- create git snapshot if available
- execute replacement
- log in `DANGEROUS.md`
- cross-reference the active project records

## example 2: force continuation on a bad methodological path
User intent: continue with a weak or dubious method anyway.

Expected behavior:
- state methodological risks briefly and concretely
- execute if technically possible
- do not silently substitute a stronger method
- log if the action materially affects research credibility or result interpretation

## example 3: overwrite earlier output without preserving a file copy
User intent: keep only the newest output.

Expected behavior:
- preserve state via git snapshot when possible
- execute the overwrite
- make the loss of working-tree comparability explicit
- log the event

## example 4: impossible command
User intent: carry out an action requiring permissions or resources that are unavailable.

Expected behavior:
- report the blocker precisely
- do not claim execution
- do not fabricate a partial success unless a real partial action occurred
