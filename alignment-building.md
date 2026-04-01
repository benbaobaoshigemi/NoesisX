# Alignment Audit

本文件用于证明 [Architecture.md](/Users/benbaobaoshigemi/Desktop/NoesisX/Architecture.md) 的要求已经落实到哪些项目文件中，并区分哪些规则属于未来运行时预读面，哪些属于按需加载的 workflow，哪些属于搭建模板。任何关键规则都不应只存在于本文件。

## Runtime Layers

未来去掉后缀后的真实运行面分三层：

1. 预读层
   - `AGENTS.md`
   - `.codex/agents/*.toml`
   - 这些文件必须承载所有开工前就要知道的硬规则。
2. 按需工作流层
   - `.agents/skills/*`
   - 这些文件负责复用型流程，不能承担唯一真相源。
3. 搭建与格式层
   - `brain/*.md`
   - `library/INDEX.md`
   - `experiment/*/experiment.md`
   - 模板只提供结构和格式，不独占行为规则。

当前隔离态对应文件分别是：

- [agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
- [.codex-buiding/config.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/config.toml)
- [.codex-buiding/agents/fetcher.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/fetcher.toml)
- [.codex-buiding/agents/engineer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/engineer.toml)
- [.codex-buiding/agents/writer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/writer.toml)
- [.codex-buiding/agents/professor.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/professor.toml)
- [.agents-buiding/skills/graph-build/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/SKILL.md)
- [.agents-buiding/skills/project-state-sync/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/project-state-sync/SKILL.md)
- [.agents-buiding/skills/library-index-ingest/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/library-index-ingest/SKILL.md)
- [.agents-buiding/skills/engineer-note-keeper/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/engineer-note-keeper/SKILL.md)
- [.agents-buiding/skills/writer-formal-output/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/writer-formal-output/SKILL.md)
- [.agents-buiding/skills/professor-route-check/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/professor-route-check/SKILL.md)
- [templates-building/README-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/README-building.md)
- [templates-building/brain/PROJECT-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/brain/PROJECT-template-building.md)
- [templates-building/brain/ASSIGNMENT-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/brain/ASSIGNMENT-template-building.md)
- [templates-building/brain/GRAPH-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/brain/GRAPH-template-building.md)
- [templates-building/brain/NOTE-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/brain/NOTE-template-building.md)
- [templates-building/library/INDEX-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/library/INDEX-template-building.md)
- [templates-building/experiment/experiment-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/experiment/experiment-template-building.md)

## Constitution And Core Principles

- 首要目标、诚实原则、证据优先、异常不可吞、工程服务研究、长期状态由文件持有：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
- 子代理输出不得直接成为项目结论、原始材料默认受保护、任何绕行必须留下原因和影响：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 角色级补强：[.codex-buiding/agents/fetcher.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/fetcher.toml)
  - 角色级补强：[.codex-buiding/agents/engineer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/engineer.toml)
  - 角色级补强：[.codex-buiding/agents/writer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/writer.toml)
  - 角色级补强：[.codex-buiding/agents/professor.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/professor.toml)

## 1+4+N Architecture

- 主代理持有主线、状态、拓扑与最终责任：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
- `fetcher` / `engineer` / `writer` / `professor` 的边界：
  - 运行时总规则：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 角色专属落点：[.codex-buiding/agents/fetcher.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/fetcher.toml)
  - 角色专属落点：[.codex-buiding/agents/engineer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/engineer.toml)
  - 角色专属落点：[.codex-buiding/agents/writer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/writer.toml)
  - 角色专属落点：[.codex-buiding/agents/professor.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/professor.toml)
- `temp-sub-agent` 是一次性认知器件，不持有长期状态，也不拥有永久技能栈：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)

## Filesystem And Directory Boundaries

- 根目录不出现零散过程文件，职责目录分工明确：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 搭建说明：[templates-building/README-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/README-building.md)
- `brain/`、`inbox/`、`experiment/`、`output/`、`visualization/`、`library/`、`archive/`、`scratch/` 的目录语义：
  - 运行时边界：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 搭建说明：[templates-building/README-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/README-building.md)
- 所有时间命名使用真实本地时间与 `YYYY-MM-DD_HHMMSS`：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 模板体现：[templates-building/experiment/experiment-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/experiment/experiment-template-building.md)

## File Protocols

- `PROJECT.md` 的当前态职责、字段要求、与 `GRAPH.md` 的协同关系：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - Workflow 落点：[.agents-buiding/skills/project-state-sync/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/project-state-sync/SKILL.md)
  - 模板落点：[templates-building/brain/PROJECT-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/brain/PROJECT-template-building.md)
- `ASSIGNMENT.md` 的四种使用情形、`# UNDERSTANDING` 规则与直接命令服从：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 模板落点：[templates-building/brain/ASSIGNMENT-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/brain/ASSIGNMENT-template-building.md)
- `GRAPH.md` 的唯一权威账本地位、允许类型集合、允许事件集合、终态不可原地复活、严格小语法、与 `experiment.md` / `PROJECT.md` 的程序化联动校验：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - Workflow 落点：[.agents-buiding/skills/graph-build/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/SKILL.md)
  - 模板落点：[templates-building/brain/GRAPH-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/brain/GRAPH-template-building.md)
- `GRAPH.md` 的正式格式被钉死为节点账本式，不允许事件账本式：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - Workflow 落点：[.agents-buiding/skills/graph-build/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/SKILL.md)
  - 模板落点：[templates-building/brain/GRAPH-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/brain/GRAPH-template-building.md)
- `GRAPH.md` 更新后立即进行程序化 lint，并由固定夹具回归测试守护：
  - Workflow 落点：[.agents-buiding/skills/graph-build/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/SKILL.md)
  - 脚本落点：[graph_lint.py](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/scripts/graph_lint.py)
  - 测试落点：[test_graph_lint.py](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/graph-build/scripts/test_graph_lint.py)
- `NOTE.md` 只由 engineer 维护，只记录工程连续性：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - Workflow 落点：[.agents-buiding/skills/engineer-note-keeper/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/engineer-note-keeper/SKILL.md)
  - 模板落点：[templates-building/brain/NOTE-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/brain/NOTE-template-building.md)
- `library/INDEX.md` 的最小元信息与受管状态集合：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - Workflow 落点：[.agents-buiding/skills/library-index-ingest/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/library-index-ingest/SKILL.md)
  - 模板落点：[templates-building/library/INDEX-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/library/INDEX-template-building.md)
- `experiment.md` 的最低留痕单位地位、字段要求、`Topology Delta` 责任与追加式书写：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 协同更新 workflow：[.agents-buiding/skills/project-state-sync/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/project-state-sync/SKILL.md)
  - 模板落点：[templates-building/experiment/experiment-template-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/templates-building/experiment/experiment-template-building.md)

## Agent Interaction And Output Rules

- 执行优先 vs 讨论优先、讨论态中不得立刻修改、应更积极阅读项目与补充外证：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
- 用户直接命令必须服从，但错误研究前提必须被指出：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
- 回复风格必须准确、克制、书面化，不滥用英文或内部命名，并给出完整文件目录：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
- 文件更新说明必须具体到实验目录、graph 节点变化和项目当前态变化：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - Workflow 补强：[.agents-buiding/skills/project-state-sync/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/project-state-sync/SKILL.md)

## Research Loop, Execution Discipline, And Closure

- 每轮形成小闭环，不在细枝末节上停机等命令：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
- 正式脚本先写文件再运行，禁止 heredoc、`python -c`、管道注入；控制台短探针仅限局部诊断；单次代码写入不超过 200 行：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 工程执行补强：[.codex-buiding/agents/engineer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/engineer.toml)
- 不把无关步骤揉成巨型脚本：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
- 默认更新顺序 `experiment.md -> GRAPH.md -> PROJECT.md`：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - Workflow 落点：[.agents-buiding/skills/project-state-sync/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/project-state-sync/SKILL.md)
- 收束检查：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)

## Open-Ended Mode

- 触发条件、持续推进义务、价值判断维度、强制纠偏触发器、阶段收束与外部硬边界：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 路线纠偏配套：[.codex-buiding/agents/professor.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/professor.toml)
  - 路线纠偏 workflow：[.agents-buiding/skills/professor-route-check/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/professor-route-check/SKILL.md)

## Subagent Use Protocol

- 四类固定子代理与 `temp-sub-agent` 异质、不可套同一模板理解：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
- `fetcher` 的取材原则、入库交还、禁止静默筛料：
  - 运行时总规则：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 角色落点：[.codex-buiding/agents/fetcher.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/fetcher.toml)
- `engineer` 的最小扰动修复、`NOTE.md` 责任、不可把研究问题伪装成技术问题：
  - 运行时总规则：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 角色落点：[.codex-buiding/agents/engineer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/engineer.toml)
- `writer` 是正式成稿链上的独立角色，不是边缘润色工具：
  - 运行时总规则：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 角色落点：[.codex-buiding/agents/writer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/writer.toml)
  - 写作 workflow：[.agents-buiding/skills/writer-formal-output/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/writer-formal-output/SKILL.md)
- `professor` 是请教接口，不是执行者：
  - 运行时总规则：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 角色落点：[.codex-buiding/agents/professor.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/professor.toml)
  - 判断 workflow：[.agents-buiding/skills/professor-route-check/SKILL.md](/Users/benbaobaoshigemi/Desktop/NoesisX/.agents-buiding/skills/professor-route-check/SKILL.md)
- 子代理回收时必须做存在性检查、事实/解释/推测分类、必要复核和文件吸收：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)

## Skill Stack Principles

- skills 是能力入口，不是角色本体，不能反向扩权：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
- 主代理、四个固定子代理和 `temp-sub-agent` 的保底能力栈原则：
  - 运行时主落点：[agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md)
  - 角色级实现：[.codex-buiding/agents/fetcher.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/fetcher.toml)
  - 角色级实现：[.codex-buiding/agents/engineer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/engineer.toml)
  - 角色级实现：[.codex-buiding/agents/writer.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/writer.toml)
  - 角色级实现：[.codex-buiding/agents/professor.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/agents/professor.toml)

## Runtime Configuration

- 主模型、推理强度、多代理开关、`agents.max_depth = 2`、OpenAI Docs MCP 入口：
  - [.codex-buiding/config.toml](/Users/benbaobaoshigemi/Desktop/NoesisX/.codex-buiding/config.toml)

## Integrity Check

- 任何需要在任务开始前就知道的规则，现已落在 [agents-building.md](/Users/benbaobaoshigemi/Desktop/NoesisX/agents-building.md) 或对应子代理 `.toml`，不依赖模板或本审计稿本身。
- 任何需要复用但不必预读的流程，现已落在 project skills 中，并且主合同中保留了调用入口。
- 任何模板字段都已经有运行时上位规则支撑；模板不是唯一真相源。
- 本轮审计未保留“只存在于 `Architecture.md`、却没有落入项目文件”的核心要求。
