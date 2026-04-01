# 模板说明

本目录存放项目文件系统的隔离态模板，用于搭建新项目时复制、去除后缀并放入正式目录。

当前模板覆盖：

- 根目录与职责目录的搭建说明
- `brain/PROJECT.md`
- `brain/ASSIGNMENT.md`
- `brain/GRAPH.md`
- `brain/NOTE.md`
- `library/INDEX.md`
- `experiment/YYYY-MM-DD_HHMMSS/experiment.md`

本目录中的模板文件名带有 `-template-building` 后缀，仅用于避免当前工作区误读。内容本身对应未来正式项目中的运行时文件。

未来正式项目至少应建立以下结构：

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/agents/*.toml`
- `.agents/skills/*`
- `brain/PROJECT.md`
- `brain/ASSIGNMENT.md`
- `brain/GRAPH.md`
- `brain/NOTE.md`
- `inbox/`
- `experiment/`
- `output/`
- `visualization/`
- `library/INDEX.md`
- `archive/`
- `scratch/`

模板只负责提供格式与初始骨架，不承担唯一行为真相源。真正必须在运行前被代理读到的硬规则，应保留在未来的 `AGENTS.md` 与各子代理 `.toml` 中。
