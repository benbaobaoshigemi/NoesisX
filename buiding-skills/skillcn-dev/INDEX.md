# skillcn-dev

这个目录用于推进中文写作相关 skill 的开发，不是最终运行时 skill。

当前包含五类内容：

- `github-open-source-scan.md`
  - 已核验的 GitHub 开源来源，以及它们适合转成什么类型的中文写作 skill。
- `push-writer-architecture.md`
  - `push-writer` 与 `writer` 子技能的拆分方案、运行约束与迁移建议。
- `prompt-seeds/`
  - 本地改写过的中文 prompt 种子，偏向最终技能化使用。
- `imported-prompts/`
  - 从外部仓导入并规范化后的 prompt 原料，主要来自 `Kiteflyingee/academic_prompts`。
- `skills/`
  - 开发中的 `push-writer` 与中文 `writer-*` 子技能骨架。

当前开发结论：

- `report-mode` 不再继续保留“再开写作子代理”的流程设计。
- `push-writer` 负责安装依赖 skill、选择并注入 prompt、决定单实例/级联/并行的 `writer` 拓扑。
- 具体文风、检查、翻译与论文规范能力拆到 `writer` 自己调用的 skills。
- 注入给 `writer` 的提示词必须真正吸收本地 prompt 文件内容，而不是把文件名当附件甩过去。
- 本目录已开始按“外部 prompt 原料 -> 本地改写种子 -> 开发中 skills”三层结构推进。
