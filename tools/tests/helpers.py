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
    maintainers = """# Maintainers and Repository Ownership

## Current maintainer roster

Metello Zuccolini @AIAllTheThingz

### Current coverage limitation

The repository currently has one active maintainer.

## Area ownership

### Independent specialist review

The specialist reviewer must not be the author.

## Merge authority

## Author self-merge

## Emergency changes

## Inactivity

## Appointment and succession

## Branch protection and enforcement

## Review cadence
"""
    codeowners = """* @AIAllTheThingz
/MAINTAINERS.md @AIAllTheThingz
/.github/CODEOWNERS @AIAllTheThingz
/governance/ @AIAllTheThingz
/SECURITY.md @AIAllTheThingz
/schemas/ @AIAllTheThingz
/tools/ @AIAllTheThingz
/.github/workflows/ @AIAllTheThingz
"""
    files = {
        "AGENTS.md": (
            "# Test Agents\n"
            "Read `MAINTAINERS.md` and `.github/CODEOWNERS`.\n"
            + ("x" * 400)
        ),
        "README.md": (
            "# Test\n\n"
            "License: Apache-2.0\n\n"
            "See [`MAINTAINERS.md`](MAINTAINERS.md) and "
            "[`.github/CODEOWNERS`](.github/CODEOWNERS).\n"
        ),
        "CATALOG.md": "# Test\n",
        "CONTRIBUTING.md": (
            "# Test\n\n"
            "Contributions are licensed under Apache-2.0.\n\n"
            "See [`MAINTAINERS.md`](MAINTAINERS.md) and "
            "[`.github/CODEOWNERS`](.github/CODEOWNERS).\n"
        ),
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
        "MAINTAINERS.md": maintainers,
        ".github/CODEOWNERS": codeowners,
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
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
