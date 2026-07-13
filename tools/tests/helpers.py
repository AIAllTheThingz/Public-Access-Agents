from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def run_tool(relative_script: str, *args: str, root: Path | None=None):
    command = [sys.executable, str(REPO_ROOT / relative_script)]
    if root is not None:
        command.extend(["--root", str(root)])
    command.extend(args)
    return subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True, check=False)


def json_result(completed):
    return json.loads(completed.stdout)


def make_required_root(root: Path) -> None:
    for name in ("AGENTS.md", "README.md", "CATALOG.md", "CONTRIBUTING.md", "MANIFEST.md", "ROADMAP.md", "SECURITY.md", "SOURCES.md"):
        content = "# Test\n" if name != "AGENTS.md" else "# Test Agents\n" + ("x" * 400)
        (root / name).write_text(content, encoding="utf-8")
