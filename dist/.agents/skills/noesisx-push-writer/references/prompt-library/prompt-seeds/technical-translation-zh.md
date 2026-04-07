# Technical Translation to Chinese

Source basis:

- <https://github.com/01-ai/Yi/wiki/%E7%BF%BB%E8%AF%91%E4%B8%8E%E5%AE%A1%E6%A0%A1%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF>

Use this seed when translating technical or research material into Chinese, especially Markdown, HTML, README, API docs, model docs, or AI-related technical writing.

Core rules to enforce:

- 先理解原文，再逐段翻译，不逐词硬对。
- 优先保证术语准确、逻辑通顺、中文读者易懂。
- 保持 Markdown、HTML、列表、表格、标题层级和代码块结构不被破坏。
- 代码、命令、路径、配置键名、标识符通常保持原样。
- 对专有名词、模型名、库名、接口名保持一致。
- 不擅自添加原文没有的解释性扩写，除非任务明确要求。
- 若原文有歧义，应保留其谨慎程度，不擅自替作者下判断。
- 翻译后的中文应自然，不要生硬照搬英语语序。

Output expectation:

- 返回格式保真的中文译文
- 若任务要求审校，可额外指出原文不清或术语不一致之处
