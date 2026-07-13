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
    files = {
        "AGENTS.md": "# Test Agents\n" + ("x" * 400),
        "README.md": "# Test\n\nLicense: Apache-2.0\n",
        "CATALOG.md": "# Test\n",
        "CONTRIBUTING.md": "# Test\n\nContributions are licensed under Apache-2.0.\n",
        "LICENSE": (
            "Apache License\n"
            "Version 2.0, January 2004\n"
            "TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n"
            "END OF TERMS AND CONDITIONS\n"
            "APPENDIX: How to apply the Apache License to your work.\n"
        ),
        "LICENSING.md": (
            "# Licensing\n\n"
            "Apache-2.0\n\n"
            "Copyright 2026 Metello Zuccolini\n\n"
            "See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).\n"
        ),
        "MANIFEST.md": "# Test\n",
        "NOTICE": (
            "Public-Access-Agents\n"
            "Copyright 2026 Metello Zuccolini\n\n"
            "Licensed under the Apache License, Version 2.0.\n"
        ),
        "ROADMAP.md": "# Test\n",
        "SECURITY.md": "# Test\n",
        "SOURCES.md": "# Test\n",
    }
    for name, content in files.items():
        (root / name).write_text(content, encoding="utf-8")
