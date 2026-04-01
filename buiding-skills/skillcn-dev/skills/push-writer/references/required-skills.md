# Required Skills

`push-writer` must resolve required skills before dispatching `writer`.

## Hard dependencies by mode

- 中文正式学术写作:
  - `writer-chinese-academic-polish`
- 中文 reviewer 式评议:
  - `writer-chinese-reviewer-lens`
- 中文表层查错:
  - `writer-chinese-grammar-check`
- 中文逻辑硬检查:
  - `writer-chinese-logic-check`
- 中文 LaTeX 润色:
  - `writer-latex-chinese-polish`
- 中文去机械感改写:
  - `writer-chinese-de-ai`
- 中译英:
  - `writer-zh-to-en-academic`
- 英译中:
  - `writer-en-to-zh-academic`
- 学术中英互译:
  - `writer-bilingual-academic-translation`
- 论文阅读报告:
  - `writer-paper-reading-report`
- 结构优化:
  - `writer-structure-optimizer`
- 学位论文规范检查:
  - `writer-thesis-compliance-check`

## Format-linked dependencies

- Since `writer` always produces formal documents, always require `doc`.
- Since `writer` always produces formal documents, always require `pdf`.
- Since `writer` always produces formal documents, always require `writer-render-layout-check`.
- If the deliverable should include images from `visualization/`, require `writer-visualization-asset-integration`.

## Rule

- Missing hard dependencies must be installed first.
- Do not downgrade by silently skipping unavailable skills.
- Do not keep a “plain text only” branch under `writer`.
