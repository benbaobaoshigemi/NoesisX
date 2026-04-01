# Grammar Error Check

Source basis:

- Repository: <https://github.com/Kiteflyingee/academic_prompts>
- Source file: `/Users/benbaobaoshigemi/Desktop/NoesisX/.tmp-external/academic_prompts/academic_prompt.json`
- Source act: `查找语法错误`
- Category: `check`

Imported prompt:

```text
Can you help me ensure that the grammar and the spelling is correct? Do not try to polish the text, if no mistake is found, tell me that this paragraph is good. If you find grammar or spelling mistakes, please list mistakes you find in a two-column markdown table, put the original text the first column, put the corrected text in the second column and highlight the key words you fixed.
Example:
Paragraph: How is you? Do you knows what is it?
| Original sentence | Corrected sentence |
| Original sentence | Corrected sentence |
| :--- | :--- |
| Do you **knows** what **is** **it**? | Do you **know** what **it** **is** ? |
Below is a paragraph from an academic paper. You need to report all grammar and spelling mistakes as the example before.
```

Import note:

- This file is a normalized local import for skill development.
- It is intended to be read and then injected into runtime prompts, not passed as an attachment hint.
