# Injected Prompt Seed

Source basis:

- `skillcn-dev/prompt-seeds/chinese-logic-check.md`

Inject these rules into the writer brief:

- 只抓实质问题，不做装饰性修改。
- 检查论题、事实、推理、结论之间是否一致。
- 检查术语是否漂移，是否存在概念偷换。
- 检查段落之间是否有逻辑跳跃、因果倒置或前提缺失。
- 检查结论是否超出证据支撑范围。
- 若无实质问题，应明确说明，而不是硬挑毛病。

Output expectation:

- 若有问题：简洁列出问题点与对应位置
- 若无问题：简洁说明未发现实质性逻辑问题
