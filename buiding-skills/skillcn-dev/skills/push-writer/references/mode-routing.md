# Mode Routing

Use the smallest writer-skill set that fully matches the deliverable.

## Default routes

### 中文正式学术写作

- `writer-chinese-academic-polish`
- optional: `writer-chinese-logic-check`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 中文 reviewer 式评议

- `writer-chinese-reviewer-lens`
- optional: `writer-chinese-logic-check`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 中文表层查错

- `writer-chinese-grammar-check`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 中文逻辑硬检查

- `writer-chinese-logic-check`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 中文 LaTeX 内容润色

- `writer-latex-chinese-polish`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 中文去机械感改写

- `writer-chinese-de-ai`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 中译英

- `writer-zh-to-en-academic`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 英译中

- `writer-en-to-zh-academic`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 中英学术互译

- `writer-bilingual-academic-translation`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 论文阅读报告

- `writer-paper-reading-report`
- if image-rich: `writer-visualization-asset-integration`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 结构优化

- `writer-structure-optimizer`
- `writer-render-layout-check`
- `doc`
- `pdf`

### 中文学位论文规范检查

- `writer-thesis-compliance-check`
- `writer-render-layout-check`
- `doc`
- `pdf`
- if image-rich: `writer-visualization-asset-integration`

### 图文并茂正式交付

- `writer-visualization-asset-integration`
- `writer-render-layout-check`
- `doc`
- `pdf`

## Notes

- If the task is a finished formal document and the user asked for both drafting and later polishing, use a cascade topology.
- If the user asks for multiple candidate versions or multiple sections in parallel, use a parallel topology.
- If the task is simple translation or single-pass polishing, use a single writer by default.
