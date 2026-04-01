#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_JSON = ROOT.parents[1] / ".tmp-external" / "academic_prompts" / "academic_prompt.json"
OUTPUT_DIR = ROOT / "imported-prompts"

PROMPT_MAP = {
    "中文学术润色": {
        "slug": "chinese-academic-polish",
        "title": "Chinese Academic Polish",
        "category": "polish",
    },
    "英语学术润色": {
        "slug": "english-academic-polish",
        "title": "English Academic Polish",
        "category": "polish",
    },
    "查找语法错误": {
        "slug": "grammar-error-check",
        "title": "Grammar Error Check",
        "category": "check",
    },
    "Latex英文润色": {
        "slug": "latex-english-polish",
        "title": "LaTeX English Polish",
        "category": "polish",
    },
    "Latex中文润色": {
        "slug": "latex-chinese-polish",
        "title": "LaTeX Chinese Polish",
        "category": "polish",
    },
    "AIGC内容“降AI味”": {
        "slug": "aigc-de-ai",
        "title": "AIGC De-AI Rewrite",
        "category": "rewrite",
    },
    "中译英": {
        "slug": "zh-to-en-academic",
        "title": "Chinese to English Academic Translation",
        "category": "translation",
    },
    "英译中": {
        "slug": "en-to-zh-academic",
        "title": "English to Chinese Academic Translation",
        "category": "translation",
    },
    "学术中英互译": {
        "slug": "bilingual-academic-translation",
        "title": "Bilingual Academic Translation",
        "category": "translation",
    },
    "高效阅读论文": {
        "slug": "paper-reading-report",
        "title": "Paper Reading Report",
        "category": "reading",
    },
    "优化文章结构": {
        "slug": "structure-optimizer",
        "title": "Structure Optimizer",
        "category": "writing-support",
    },
}


def normalize_prompt(text: str) -> str:
    return text.strip().replace("\r\n", "\n").replace("\r", "\n")


def main() -> None:
    data = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    by_act = {item["act"]: item["prompt"] for item in data}

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    generated = []
    for act, meta in PROMPT_MAP.items():
        prompt = by_act.get(act)
        if not prompt:
            raise SystemExit(f"Missing prompt act in source json: {act}")

        path = OUTPUT_DIR / f"{meta['slug']}.md"
        body = "\n".join(
            [
                f"# {meta['title']}",
                "",
                "Source basis:",
                "",
                "- Repository: <https://github.com/Kiteflyingee/academic_prompts>",
                f"- Source file: `{SOURCE_JSON}`",
                f"- Source act: `{act}`",
                f"- Category: `{meta['category']}`",
                "",
                "Imported prompt:",
                "",
                "```text",
                normalize_prompt(prompt),
                "```",
                "",
                "Import note:",
                "",
                "- This file is a normalized local import for skill development.",
                "- It is intended to be read and then injected into runtime prompts, not passed as an attachment hint.",
            ]
        )
        path.write_text(body + "\n", encoding="utf-8")
        generated.append(path.name)

    manifest = ROOT / "imported-prompts" / "INDEX.md"
    manifest.write_text(
        "\n".join(
            [
                "# Imported Prompts",
                "",
                "These files are normalized local imports from `Kiteflyingee/academic_prompts`.",
                "",
                "Current generated files:",
                "",
                *[f"- `{name}`" for name in generated],
                "",
                "These are source materials for `skillcn-dev` and are meant to be injected into writer prompts after adaptation.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
