# Injected Prompt Seed

Source basis:

- `../../noesisx-push-writer/references/prompt-library/imported-prompts/grammar-error-check.md`

Inject these rules into the writer brief:

- 你要做的是查错，不是全面润色。
- 如果没有明显问题，应明确说明文本整体良好。
- 如果发现问题，应逐项指出原句中的错误位置，并给出更正版本。
- 不把风格偏好伪装成错误。
- 重点检查语法、搭配、错别字、句法不通和明显歧义。

Output expectation:

- 优先输出“问题点 -> 修正建议”
- 若用户要求直接改正文，可返回修正后的文本，但仍保持最小改动
