#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Iterable

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "markdown-protection-manifest.txt"
SKIP_SCAN_PREFIXES = (
    ".git/",
    ".agents/skills/graph-build/archive/legacy-fixtures-v1/",
    ".agents/skills/graph-build/fixtures_v2/",
)
REQUIRED_DIRS = [
    ".codex",
    ".codex/agents",
    ".agents/skills",
    "brain",
    "experiment",
    "writer-output",
    "visualization",
    "library",
    "archive",
    "scratch",
    "inbox",
]
REQUIRED_FILES = [
    "AGENTS.md",
    "brain/PROJECT.md",
    "brain/ASSIGNMENT.md",
    "brain/GRAPH.md",
    "brain/NOTE.md",
    "library/INDEX.md",
    ".codex/config.toml",
    ".codex/agents/fetcher.toml",
    ".codex/agents/engineer.toml",
    ".codex/agents/writer.toml",
    ".codex/agents/professor.toml",
]
REQUIRED_SKILLS = [
    "graph-build",
    "project-state-sync",
    "library-index-ingest",
    "engineer-note-keeper",
    "push-writer",
    "professor-route-check",
]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CODE_PATH_RE = re.compile(r"`([^`\n]+?\.[A-Za-z0-9_-]+(?:#[^`\s]+)?)`")
CODE_PREFIXES = ("./", "../", "references/", "scripts/", "assets/", "agents/")
ROOT_PATH_PREFIXES = (
    ".agents/",
    ".codex/",
    "brain/",
    "library/",
    "archive/",
    "scratch/",
    "inbox/",
    "writer-output/",
    "visualization/",
    "experiment/",
)
ROOT_FILES = {
    "AGENTS.md",
}


def rel(path: Path, base: Path) -> str:
    return path.relative_to(base).as_posix()


def restore_copy() -> Path:
    temp_root = Path(tempfile.mkdtemp(prefix="noesisx-arch-audit-"))
    temp_repo = temp_root / ROOT.name
    shutil.copytree(
        ROOT,
        temp_repo,
        ignore=shutil.ignore_patterns(".git", "__pycache__"),
    )
    for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw.startswith("./"):
            continue
        source = temp_repo / raw[2:]
        if source.suffix != ".txt" or not source.exists():
            continue
        source.rename(source.with_suffix(".md"))
    return temp_repo


def local_target(token: str, base_file: Path, repo_root: Path) -> Path | None:
    token = token.strip().strip("<>").split("#", 1)[0]
    if not token or token.startswith(("http://", "https://", "mailto:", "data:")):
        return None
    if (
        " " in token
        or "*" in token
        or "YYYY-MM-DD_HHMMSS" in token
        or "<" in token
        or ">" in token
    ):
        return None
    if token.startswith("/"):
        path = Path(token)
        return path if str(path).startswith(str(repo_root)) else None
    if token in ROOT_FILES or token.startswith(ROOT_PATH_PREFIXES):
        return repo_root / token
    if "/" not in token and not token.startswith(("./", "../")):
        return None
    resolved = (base_file.parent / token).resolve()
    return resolved if str(resolved).startswith(str(repo_root)) else None


def scan_paths(temp_repo: Path) -> list[str]:
    issues: list[str] = []
    for path in temp_repo.rglob("*.md"):
        rel_path = rel(path, temp_repo)
        if any(rel_path.startswith(prefix) for prefix in SKIP_SCAN_PREFIXES):
            continue
        text = path.read_text(encoding="utf-8")
        tokens: list[str] = []
        in_fence = False
        for line in text.splitlines():
            if line.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for match in LINK_RE.finditer(line):
                token = match.group(1).strip()
                if token.startswith("#") or "*" in token:
                    continue
                tokens.append(token)
            stripped = line.lstrip()
            if not stripped.startswith("- "):
                continue
            if stripped.startswith("- **Example") or stripped.startswith("- **Examples"):
                continue
            for match in CODE_PATH_RE.finditer(line):
                token = match.group(1).strip()
                if " " in token or "*" in token or not token.startswith(CODE_PREFIXES):
                    continue
                tokens.append(token)
        seen: set[str] = set()
        for token in tokens:
            if token in seen:
                continue
            seen.add(token)
            target = local_target(token, path, temp_repo)
            if target is None:
                continue
            if not target.exists():
                issues.append(f"PATH_MISSING {rel_path} -> {token}")
    return issues


def check_structure(temp_repo: Path) -> list[str]:
    issues: list[str] = []
    for item in REQUIRED_DIRS:
        if not (temp_repo / item).is_dir():
            issues.append(f"DIR_MISSING {item}")
    for item in REQUIRED_FILES:
        if not (temp_repo / item).exists():
            issues.append(f"FILE_MISSING {item}")
    for skill in REQUIRED_SKILLS:
        if not (temp_repo / ".agents" / "skills" / skill / "SKILL.md").exists():
            issues.append(f"SKILL_MISSING .agents/skills/{skill}/SKILL.md")
    return issues


def check_config(temp_repo: Path) -> list[str]:
    issues: list[str] = []
    config = tomllib.loads((temp_repo / ".codex" / "config.toml").read_text(encoding="utf-8"))
    agents = config.get("agents", {})
    for name in ("fetcher", "engineer", "writer", "professor"):
        section = agents.get(name)
        if not isinstance(section, dict):
            issues.append(f"AGENT_SECTION_MISSING {name}")
            continue
        config_file = section.get("config_file")
        if not isinstance(config_file, str):
            issues.append(f"AGENT_CONFIG_FILE_MISSING {name}")
            continue
        target = temp_repo / ".codex" / config_file
        if not target.exists():
            issues.append(f"AGENT_CONFIG_PATH_MISSING {name} -> .codex/{config_file}")
    if config.get("features", {}).get("multi_agent") is not True:
        issues.append("FEATURE_MISMATCH multi_agent must be true")
    if config.get("features", {}).get("js_repl") is not True:
        issues.append("FEATURE_MISMATCH js_repl must be true")
    return issues


def run_cmd(temp_repo: Path, args: Iterable[str]) -> list[str]:
    proc = subprocess.run(args, cwd=temp_repo, capture_output=True, text=True)
    if proc.returncode == 0:
        return []
    detail = (proc.stdout + proc.stderr).strip().splitlines()
    suffix = f": {detail[0]}" if detail else ""
    return [f"CMD_FAILED {' '.join(args)}{suffix}"]


def check_runtime(temp_repo: Path) -> list[str]:
    return (
        run_cmd(temp_repo, ["python3", ".agents/skills/graph-build/scripts/test_graph_lint.py"])
        + run_cmd(temp_repo, ["python3", ".agents/skills/graph-build/scripts/graph_lint.py", "brain/GRAPH.md"])
    )


def main() -> int:
    temp_repo = restore_copy()
    issues = []
    issues.extend(check_structure(temp_repo))
    issues.extend(check_config(temp_repo))
    issues.extend(scan_paths(temp_repo))
    issues.extend(check_runtime(temp_repo))
    print(f"TEMP_REPO={temp_repo}")
    if issues:
        for issue in sorted(set(issues)):
            print(issue)
        print(f"TOTAL_ISSUES={len(sorted(set(issues)))}")
        return 1
    print("TOTAL_ISSUES=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
