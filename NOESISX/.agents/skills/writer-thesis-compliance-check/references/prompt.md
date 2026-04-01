# Injected Prompt Seed

Source basis:

- `../../push-writer/references/prompt-library/prompt-seeds/thesis-compliance-check.md`

Inject these rules into the writer brief:

- 优先检查结构完整性，再检查局部措辞。
- 检查摘要、目录、章节层次、图表、参考文献、附录等是否齐备。
- 检查中英文摘要、术语、图表编号、表题和参考文献格式是否一致。
- 若用户给出学校模板，以学校模板为最高规则。
- 若没有模板，只做通用学位论文规范检查，不伪造校级细则。
- 这是规范检查，不是全文重写。

Output expectation:

- 返回“必须修 / 建议修 / 可保持”的问题清单
