# Chinese Logic Check

Source basis:

- <https://github.com/lijigang/prompts>
- local adaptation from the existing `logic-check` reference

Use this seed when the text is already relatively mature and the main task is to catch meaningful problems rather than to perform a full rewrite.

Core rules to enforce:

- 只抓实质问题，不做装饰性修改。
- 检查论题、事实、推理、结论之间是否一致。
- 检查术语是否漂移，前后是否存在概念偷换。
- 检查段落之间是否存在逻辑跳跃、因果倒置或前提缺失。
- 检查结论是否超出了证据支撑范围。
- 不把“风格偏好”伪装成“逻辑问题”。
- 若无实质问题，应明确说明，而不是为了显得有贡献而硬挑毛病。

Output expectation:

- 若无重大问题：简明说明“未发现实质性逻辑问题”
- 若有问题：按问题点简洁列出，并指出对应句段或对应论证位置
