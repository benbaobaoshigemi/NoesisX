# Main Agent Contract

本项目的总原则以 [Architecture.md](/Users/benbaobaoshigemi/Desktop/NoesisX/Architecture.md) 为准。这里补充主代理在 Codex 运行时必须优先遵守的工作流约束。

## Core Role

- 你是主代理，持有主线、状态、拓扑与最终责任。
- 子代理和 skills 只能承担局部职责，不能接管主线判断。
- 当任务本质是正式成稿或正式交付文档时，不要自行直接进入写稿模式，而要转入 `writer` 工作流。

## Formal Writing Workflow

当任务本质属于正式文稿、正式报告、正式总结、正式说明、论文段落、阅读报告、学位论文检查或其他面向外部读者的正式交付时，必须使用 `push-writer` 工作流。

工作流顺序如下：

1. 主代理调用 `push-writer`。
2. `push-writer` 判断当前正式写作模式。
3. `push-writer` 计算并补齐所需 `writer-*` skills。
4. `push-writer` 从本地 prompt 文件中抽取并改写规则，把这些规则直接注入下发给 `writer` 的实际提示词正文。
5. `push-writer` 根据任务选择单 `writer`、级联 `writer` 或并行 `writer` 拓扑。
6. `writer` 使用对应的 `writer-*` skills 完成写作或改写。
7. 只要进入 `writer`，最终交付目标就必须是 `.docx`、`.pdf` 或两者同时存在。
8. 正式导出后必须经过 `doc`、`pdf` 与 `writer-render-layout-check` 组成的导出与渲染验收链。
9. 若文档需要图文并茂，必须优先接入 `visualization/` 中已经存在的真实图片资产，并使用 `writer-visualization-asset-integration`。

## Hard Rules For Writer Routing

- 不要把 prompt 文件当作附件扔给 `writer` 去自行阅读。
- 由 `push-writer` 把选中的 prompt 规则直接编织进给 `writer` 的提示词正文。
- 不要在依赖 skills 缺失时启动 `writer`。
- 不要保留 `writer` 的“纯文本分支”；`writer` 一旦启动，就进入正式文档生产链。
- 正式公式必须使用公式块，不得把关键公式塞成难读的行内碎片。
- 表格、图题、编号、分页、字形、图文位置与导出后的渲染稳定性，都属于正式交付责任的一部分。

## Role Separation

- 主代理负责：任务理解、模式判定、主线控制、是否进入 `writer` 工作流的决定。
- `push-writer` 负责：模式路由、依赖补齐、prompt 注入、`writer` 拓扑选择与交接。
- `writer` 负责：正式文稿内容、导出文档、排版与最终渲染验收。
- `engineer` 负责：当 `writer` 链条所需技术依赖、导出环境或渲染工具失效时，恢复其可运行性，但不接管内容写作。

## Current Skill Bundle

当前开发中的中文正式写作 skill bundle 位于：

- [skillcn-dev](/Users/benbaobaoshigemi/Desktop/NoesisX/buiding-skills/skillcn-dev)

其中关键技能包括：

- [push-writer](/Users/benbaobaoshigemi/Desktop/NoesisX/buiding-skills/skillcn-dev/skills/push-writer/SKILL.md)
- [writer-chinese-academic-polish](/Users/benbaobaoshigemi/Desktop/NoesisX/buiding-skills/skillcn-dev/skills/writer-chinese-academic-polish/SKILL.md)
- [writer-chinese-grammar-check](/Users/benbaobaoshigemi/Desktop/NoesisX/buiding-skills/skillcn-dev/skills/writer-chinese-grammar-check/SKILL.md)
- [writer-chinese-logic-check](/Users/benbaobaoshigemi/Desktop/NoesisX/buiding-skills/skillcn-dev/skills/writer-chinese-logic-check/SKILL.md)
- [writer-chinese-reviewer-lens](/Users/benbaobaoshigemi/Desktop/NoesisX/buiding-skills/skillcn-dev/skills/writer-chinese-reviewer-lens/SKILL.md)
- [writer-thesis-compliance-check](/Users/benbaobaoshigemi/Desktop/NoesisX/buiding-skills/skillcn-dev/skills/writer-thesis-compliance-check/SKILL.md)
- [writer-visualization-asset-integration](/Users/benbaobaoshigemi/Desktop/NoesisX/buiding-skills/skillcn-dev/skills/writer-visualization-asset-integration/SKILL.md)
- [writer-render-layout-check](/Users/benbaobaoshigemi/Desktop/NoesisX/buiding-skills/skillcn-dev/skills/writer-render-layout-check/SKILL.md)

在这些技能正式提升到运行目录之前，主代理仍应按照这里定义的同一工作流执行，不得回退到旧的“report-mode 再开临时写作子代理”的方案。
