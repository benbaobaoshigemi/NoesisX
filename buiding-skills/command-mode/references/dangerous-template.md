# dangerous.md template

Use minute-level timestamps by default.

## entry template

```md
## YYYY-MM-DD HH:MM - command event
- user directive:
- risk statement:
- action taken:
- affected paths:
- impact on traceability or conclusion quality:
- recovery notes:
- related experiment:
- related commit:
```

## guidance

### user directive
Quote the operative instruction faithfully. Do not paraphrase away the dangerous part.

### risk statement
State concrete risks, for example:
- overwrites raw intermediate files
- weakens result traceability
- increases chance of misinterpretation
- removes ability to compare against prior output

### action taken
Describe what was actually done, not what was intended.

### affected paths
List specific files or directories when possible.

### impact
Say whether the action changed:
- auditability
- reproducibility
- interpretability
- confidence in conclusions

### recovery notes
State how to revert, reconstruct, or mitigate when possible.

## example

```md
## 2026-03-21 14:32 - command event
- user directive: overwrite the processed results directory with the new run and do not keep the previous outputs
- risk statement: destroys direct comparability with the previous processed outputs and weakens short-term traceability
- action taken: replaced `outputs/processed/` with the new run output after creating a git snapshot
- affected paths: `outputs/processed/`
- impact on traceability or conclusion quality: prior processed state no longer exists in the working tree; comparison now depends on the snapshot commit
- recovery notes: restore from the pre-command snapshot commit if comparison is needed
- related experiment: experiments/2026-03-21_exp-reprocess-results/Experiment.md
- related commit: abc1234
```
