#!/usr/bin/env python3
"""Regression tests for graph_lint.py."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "graph_lint.py"
FIXTURES = ROOT / "fixtures_v2"


def resolve_markdown_fixture(path_without_suffix: Path) -> Path:
    md_path = path_without_suffix.with_suffix(".md")
    txt_path = path_without_suffix.with_suffix(".txt")
    if md_path.exists():
        return md_path
    return txt_path


class GraphLintRegressionTests(unittest.TestCase):
    def test_all_fixtures(self) -> None:
        fixture_dirs = sorted(path for path in FIXTURES.iterdir() if path.is_dir())
        self.assertTrue(fixture_dirs, "expected at least one graph-lint fixture")

        for fixture_dir in fixture_dirs:
            graph_path = resolve_markdown_fixture(fixture_dir / "brain" / "GRAPH")
            self.assertTrue(graph_path.exists(), f"missing GRAPH fixture: {graph_path}")
            baseline_path = resolve_markdown_fixture(fixture_dir / "baseline" / "GRAPH")

            cmd = [sys.executable, str(SCRIPT), str(graph_path)]
            if baseline_path.exists():
                cmd.extend(["--baseline", str(baseline_path)])

            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=False,
            )

            stdout = proc.stdout.strip()
            stderr = proc.stderr.strip()

            with self.subTest(fixture=fixture_dir.name):
                if fixture_dir.name.endswith("-valid"):
                    self.assertEqual(
                        proc.returncode,
                        0,
                        f"expected valid fixture to pass\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}",
                    )
                    self.assertIn("GRAPH_LINT_OK", stdout)
                elif fixture_dir.name.startswith("invalid-"):
                    self.assertNotEqual(
                        proc.returncode,
                        0,
                        f"expected invalid fixture to fail\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}",
                    )
                    self.assertIn("GRAPH_LINT_FAILED", stderr)

                    expected_errors = fixture_dir / "expected-errors.txt"
                    self.assertTrue(
                        expected_errors.exists(),
                        f"missing expected-errors.txt for {fixture_dir.name}",
                    )
                    for expected_line in expected_errors.read_text(encoding="utf-8").splitlines():
                        expected_line = expected_line.strip()
                        if expected_line:
                            self.assertIn(expected_line, stderr)
                else:
                    self.fail(
                        "fixture name must either end with '-valid' or start with 'invalid-'"
                    )


if __name__ == "__main__":
    unittest.main()
