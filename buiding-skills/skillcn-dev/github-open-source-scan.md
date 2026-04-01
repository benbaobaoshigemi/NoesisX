# GitHub Open-Source Scan

本文件记录已经核验过、适合吸收到中文写作技能栈中的 GitHub 开源来源。

原则：

- 只记录对当前 `push-writer -> writer` 架构有直接价值的来源。
- 优先保留可以转成 prompt、checklist、结构规则或交付规范的材料。
- 本地后续若要落文件，应做改写和重组，不直接把远端内容整段复制进 skill。

## A. 直接高价值来源

### 0. Kiteflyingee/academic_prompts

- URL: <https://github.com/Kiteflyingee/academic_prompts>
- 类型：学术写作常用 prompt 集合仓
- 当前价值：
  - 是目前 `skillcn-dev` 里最适合程序化导入的 prompt 来源
  - 很适合转成中文润色、翻译、结构优化、论文阅读报告等 `writer` 子技能
  - 仓库结构极简单，主资产集中在 `academic_prompt.json`
- 已吸收方式：
  - 在本项目中导入为 `skillcn-dev/imported-prompts/`
  - 再根据模式转成 `writer-*` 子技能的本地 prompt 注入源
- 适合吸收的内容类型：
  - 中文学术润色
  - 中文/英文学术翻译
  - LaTeX 中英文润色
  - AIGC 文本去机械感
  - 论文阅读报告
  - 文章结构优化
- 不适合直接照搬的部分：
  - 与当前 `writer` 技能栈无关的代码类与通用辅助类条目

### 1. SYSUSELab/academic-writing-guide

- URL: <https://github.com/SYSUSELab/academic-writing-guide>
- 类型：中文论文写作规范与常见低级错误清单
- 当前价值：
  - 很适合转成 `writer-thesis-compliance-check`
  - 很适合转成 `writer-chinese-academic-polish` 的结构与检查规则
  - 很适合为中文摘要、参考文献、图表、术语统一提供 checklist
- 适合吸收的内容类型：
  - 论文结构规范
  - 图表与参考文献检查项
  - 中文学术表达中的低级错误规避
- 不适合直接照搬的部分：
  - 外部教程链接列表
  - 过于项目无关的视频课程目录

### 2. 01-ai/Yi Wiki: 翻译与审校的正确姿势

- URL: <https://github.com/01-ai/Yi/wiki/%E7%BF%BB%E8%AF%91%E4%B8%8E%E5%AE%A1%E6%A0%A1%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF>
- 类型：技术文档翻译与审校 prompt 方法页
- 当前价值：
  - 适合转成 `writer-tech-translation-zh`
  - 适合转成中英技术文本、Markdown/HTML 文档翻译规则
  - 对“保持格式不变、术语统一、代码块不乱动”很有帮助
- 适合吸收的内容类型：
  - 角色设定方式
  - 技术翻译流程
  - 格式保真规则
  - 审校关注点
- 不适合直接照搬的部分：
  - 过长的原始 prompt 话术
  - 与 01-ai 场景强绑定的品牌语境

### 3. lijigang/prompts

- URL: <https://github.com/lijigang/prompts>
- 类型：中文结构化 prompts 仓库
- 当前价值：
  - 适合转成 `writer-chinese-logic-check`
  - 适合给中文 writer skills 提供更稳的结构化提示框架
  - 适合补强“逻辑分析”“术语漂移检查”“结构化角色设定”
- 适合吸收的内容类型：
  - 中文结构化 prompt 写法
  - 逻辑分析角色
  - 约束、目标、工作流分区方式
- 不适合直接照搬的部分：
  - 与正式科研写作无关的通用 prompt 场景

## B. 中高价值来源

### 4. langgptai/wonderful-prompts

- URL: <https://github.com/langgptai/wonderful-prompts>
- 类型：中文 prompt 大仓
- 当前价值：
  - 适合作为中文 prompt 风格、结构写法的素材库
  - 适合抽取“角色/目标/约束/工作流”形式
- 局限：
  - 太杂，不适合直接作为 `writer` 的主依据
  - 与学术写作强相关的部分不够集中
- 适合定位：
  - 作为 prompt 写法参考，不作为主要学术规范来源

## C. 交付格式与模板价值来源

### 5. tuna/thuthesis

- URL: <https://github.com/tuna/thuthesis>
- 类型：中文学位论文 LaTeX 模板
- 当前价值：
  - 不适合做 prompt 主体
  - 适合作为论文交付规范、结构检查、模板对接的来源
- 适合吸收的内容类型：
  - 中文学位论文结构层次
  - 模板约束意识
  - 学校模板驱动的交付边界

### 6. JingWangTW/NYCU-Thesis-Template

- URL: <https://github.com/JingWangTW/NYCU-Thesis-Template>
- 类型：中文硕士论文 LaTeX 模板
- 当前价值：
  - 适合补充中文学位论文模板的真实使用视角
  - 有助于 `writer-thesis-compliance-check` 理解“中文模板不是只查格式，还查结构完整性”

### 7. CSUcse/CSUthesis

- URL: <https://github.com/CSUcse/CSUthesis>
- 类型：中文研究生学位论文 LaTeX 模板
- 当前价值：
  - 与前两项相同，主要是模板与规范层参考

## 筛选结论

如果只保留最值得继续吸收的来源，优先级如下：

1. `Kiteflyingee/academic_prompts`
2. `SYSUSELab/academic-writing-guide`
3. `01-ai/Yi Wiki`
4. `lijigang/prompts`
5. `tuna/thuthesis`
6. `JingWangTW/NYCU-Thesis-Template`
7. `CSUcse/CSUthesis`
8. `langgptai/wonderful-prompts`

## 对应到本项目的建议产物

- `push-writer`
  - 不直接吸收远端 prompt 内容，但负责把本地 prompt 种子注入给 `writer`
- `writer-chinese-academic-polish`
  - 主要来源：`academic_prompts` + `academic-writing-guide`
- `writer-chinese-logic-check`
  - 主要来源：`lijigang/prompts` + 现有 `logic-check`
- `writer-chinese-reviewer-lens`
  - 主要来源：`academic-writing-guide` 中投稿返修意识 + 现有 `reviewer-lens`
- `writer-tech-translation-zh`
  - 主要来源：`academic_prompts` + `01-ai/Yi Wiki`
- `writer-thesis-compliance-check`
  - 主要来源：`academic-writing-guide` + 各类中文学位论文模板仓
