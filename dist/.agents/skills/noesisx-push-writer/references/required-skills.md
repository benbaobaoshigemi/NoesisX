# Required Skills

`noesisx-push-writer` must resolve required skills before dispatching `writer`.

## Hard dependencies by mode

- 中文正式学术写作:
  - `writer-chinese-academic-polish`
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
- 学位论文规范检查:
  - `writer-thesis-compliance-check`

## Supporting passes inside the writer chain

- `writer-chinese-reviewer-lens`
- `writer-chinese-grammar-check`
- `writer-chinese-logic-check`
- `writer-structure-optimizer`
- `writer-visualization-asset-integration`
- `writer-render-layout-check`

## Format-linked dependencies

- Require `openai-doc`.
- Require `openai-pdf`.
- Require `writer-render-layout-check`.
- If the deliverable should include images from `visualization/`, require `writer-visualization-asset-integration`.

## Rule

- Missing hard dependencies must be installed first after they are identified.
- Supporting passes must also be installed first once the chosen topology requires them.
- Do not downgrade by silently skipping unavailable skills.
- Do not bypass the formal document chain by treating a supporting writer-side pass as the whole deliverable.
