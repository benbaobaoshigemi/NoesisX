# push-writer Architecture

本文件定义 `push-writer` 与 `writer` 子技能的拆分方案。

## 定位

`push-writer` 不是正文写作 skill，而是 `agent -> writer` 的调度总线。

只要调用 `writer`，目标产出物就默认是正式文档，而不是聊天窗口中的纯文本。正式文档的目标形态只能是：

- `.docx`
- `.pdf`

它负责：

- 判断交付类型
- 计算所需的 `writer` 子技能集合
- 确保这些 skill 已全部安装
- 读取并选择本地 prompt 种子
- 把 prompt 内容注入给 `writer`
- 决定 `writer` 的单实例、级联或并行拓扑
- 注入统一的正式文风约束
- 组织正式输出链中的图像、表格、公式与排版要求
- 回收 `writer` 结果并继续导出链

它不负责：

- 亲自写正文
- 亲自做文风润色
- 亲自做逻辑审查
- 亲自做 reviewer 风格重写

这些工作交给 `writer` 调用自己的子技能完成。

## 用户已经明确的硬规则

### 1. prompt 必须被注入，而不是作为附件甩给 writer

`push-writer` 必须先读取本地 prompt 种子文件，再把它们裁剪并编织进下发给 `writer` 的实际提示词正文。

禁止做法：

- “请参考某某文件”
- “附件里有 prompt，自行阅读”
- “请去 references 目录里选一个”

允许做法：

- 先由 `push-writer` 选择合适种子
- 再把其中有效规则直接写进给 `writer` 的提示词里

### 2. 需要的 skills 必须先装齐

`push-writer` 不允许把“缺 skill”拖到 `writer` 执行阶段才暴露。

流程必须是：

1. 判断本次任务需要哪些 `writer` 子技能
2. 检查本地是否存在
3. 缺失就先安装
4. 全部就绪后再派发 `writer`

### 3. 支持单实例、级联、并行三种 writer 拓扑

- 单实例：默认
- 级联：适合“先起草，后润色”或“先成稿，后 reviewer 风格审视”
- 并行：适合多文风候选、多章节并写、多版本对照

### 4. 所有正式文稿都必须服从统一文风宪章

无论是哪一种 `writer` 子技能，都必须服从来自 `Architecture.md` 的正式表达约束：

- 文本必须能独立站住，不得保留项目“在场感”
- 不得泄露内部文件名、路径与工作流痕迹
- 不得使用聊天腔、辩驳腔、防御腔
- 语言必须准确、客观、书面、优雅
- 不得使用口语化、碎片化表达
- 不得以文风掩盖事实不稳

这些规则必须由 `push-writer` 作为统一约束注入给 `writer`。

### 5. 正式交付必须包含排版与渲染检查

`writer` 的职责不止是写出正文，还包括对交付形态做检查，特别是：

- 版式是否稳定
- 表格是否完整、对齐、可读
- 公式是否使用公式块，而不是行内乱写
- 图文是否匹配，插图是否来自合法来源
- `.docx` / `.pdf` 渲染后是否出现破版、截断、错位

若文稿需要图文并茂，`writer` 还必须能接入 `visualization/` 中已经制作好的图片。

### 6. 只要调用 writer，就必须进入文档导出链

这里不再保留“writer 只产出纯文本草稿”的分支。

一旦调用 `writer`，就意味着：

- 产出物必须落成 `.docx` 或 `.pdf`
- 必须考虑版式与渲染
- 必须接入表格、公式、图像等正式文档检查
- 必须补上 `doc` / `pdf` 与 `writer-render-layout-check`

## 建议运行流

### Step 1. 判定交付模式

至少区分：

- 正式中文报告
- 中文学术论文段落/章节
- 中文 reviewer 式评议
- 中英技术翻译或审校
- 中文学位论文检查
- Word / PDF 导向交付
- 图文并茂正式交付

### Step 2. 解析所需 writer 子技能

示例：

- 中文学术润色：
  - `writer-chinese-academic-polish`
  - `writer-chinese-logic-check`
- 中文 reviewer 评议：
  - `writer-chinese-reviewer-lens`
  - `writer-chinese-logic-check`
- 技术翻译：
  - `writer-tech-translation-zh`
  - 必要时 `writer-chinese-logic-check`
- 学位论文交付：
  - `writer-thesis-compliance-check`
  - `doc`
  - `pdf`
  - `writer-render-layout-check`
- 图文并茂交付：
  - `writer-visualization-asset-integration`
  - `writer-render-layout-check`
  - `doc`
  - `pdf`

### Step 3. 安装缺失 skill

若本地没有所需 skill，`push-writer` 先走安装链，不带着残缺环境往下推。

### Step 4. 组装注入式 prompt

`push-writer` 读取本地 prompt 种子文件，选出与当前模式最匹配的规则，并把它们整理成一个真正可执行的提示词正文。

注入内容至少应包含：

- 用户真实目标
- 文档类型
- 目标语言
- 事实边界
- 不允许改变的范围
- 选中的 prompt 规则
- 输出格式要求
- 最终交付使用 `.docx`、`.pdf`，或二者同时存在
- 统一正式文风约束
- 图像是否需要从 `visualization/` 引用
- 表格与公式的排版约束
- 渲染检查责任

### Step 5. 决定 writer 拓扑

#### 单实例

适用：

- 单次正式成稿
- 纯翻译
- 单轮润色

#### 级联

适用：

- 起草后润色
- 成稿后 reviewer 式审视
- 翻译后审校

#### 并行

适用：

- 多版本文风对照
- 多章并写
- reviewer 与作者式说明并行生成

### Step 6. 接入排版与渲染检查链

只要进入 `writer`，就必须补上：

- 图像接入检查
  - 需要使用 `visualization/` 下已有图片时，由 `writer-visualization-asset-integration` 负责
- 渲染与版式检查
  - 由 `writer-render-layout-check` 负责
- Word / PDF 导出检查
  - 默认接 `doc` 与 `pdf`

其中公式必须使用公式块，不能以普通段落或破碎行内格式替代正式公式展示。

## 建议拆出的 writer 子技能

### 中文向

- `writer-chinese-academic-polish`
- `writer-chinese-logic-check`
- `writer-chinese-reviewer-lens`
- `writer-tech-translation-zh`
- `writer-thesis-compliance-check`
- `writer-visualization-asset-integration`
- `writer-render-layout-check`

### 英文向

原 `report-mode` 中的以下材料可继续保留并独立成 skill：

- `writer-english-paper-polish`
- `writer-logic-check`
- `writer-de-ai-english`
- `writer-reviewer-lens`

## 从 report-mode 的迁移建议

### 直接废除的部分

- “主代理不写正文，再起一个临时写作子代理，再起一个临时润色子代理”的流程性描述
- `subagent-brief-template.md`

### 保留并转化的部分

- `english-paper-polish.md`
  - 转成 `writer-english-paper-polish`
- `logic-check.md`
  - 转成 `writer-logic-check`
- `de-ai-latex-english.md`
  - 转成 `writer-de-ai-english`
- `reviewer-lens.md`
  - 转成 `writer-reviewer-lens`
- `compliance-checklist.md`
  - 作为 `push-writer` 或 `writer` 的轻检查逻辑
- `semantic-drift-check.md`
  - 作为级联和并行回收后的保底检查逻辑

## 当前结论

后续技能栈不再保留 `report-mode` 作为总写作流水线 skill。

新的结构应该是：

- `push-writer`
  - 装配、安装、注入、派发、回收，以及正式输出链的风格/渲染控制
- `writer-*`
  - 执行具体文风、翻译、检查、交付模式

这样最符合当前架构中“writer 本来就是固定子代理”的设定。
