# Injected Prompt Seed

Source basis:

- `../../push-writer/references/prompt-library/imported-prompts/latex-chinese-polish.md`

Inject these rules into the writer brief:

- 以下是一篇学术论文中的一段中文内容，请将其润色以满足学术标准，提高语法、清晰度和整体可读性。
- 不修改任何 LaTeX 命令，例如 `\\section`、`\\cite`、公式、标签和交叉引用。
- 不破坏段落结构、编号和环境边界。
- 只改文字表达，不改研究事实、结论和范围。

Output expectation:

- 返回可直接替换回 LaTeX 文档的文本
