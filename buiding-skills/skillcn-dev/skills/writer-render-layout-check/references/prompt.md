# Injected Prompt Seed

Source basis:

- `Architecture.md` writer output responsibility
- `skillcn-dev/skills/push-writer/references/output-format-and-rendering.md`

Inject these rules into the writer brief:

- 你必须对正式交付物的排版和渲染负责，而不只是负责正文内容。
- 重点检查：标题层级、编号、分页、图文位置、表格可读性、公式显示方式、导出后稳定性。
- 表格必须完整、清晰、对齐合理，不得出现破碎表头、信息截断或单位丢失。
- 正式公式必须使用公式块，不得把关键公式塞成难读的行内碎片。
- 若导出为 `.docx` 或 `.pdf`，必须以渲染结果为准做检查。

Output expectation:

- 返回渲染与版式问题清单
- 若无重大问题，可简洁确认
