#!/usr/bin/env python3
"""Validate the structure and machine-readable files in the standards repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIRED_ROOT = {
    "AGENTS.md",
    "README.md",
    "CATALOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "ROADMAP.md",
    "SOURCES.md",
}
FRONTMATTER_ID = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)


def main() -> int:
    errors: list[str] = []

    for name in sorted(REQUIRED_ROOT):
        if not (ROOT / name).is_file():
            errors.append(f"Missing required root file: {name}")

    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - validation tool reports parser error
            errors.append(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")

    ids: dict[str, Path] = {}
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER_ID.search(text)
        if match:
            rule_id = match.group(1)
            if rule_id in ids:
                errors.append(
                    f"Duplicate front-matter id {rule_id}: "
                    f"{ids[rule_id].relative_to(ROOT)} and {path.relative_to(ROOT)}"
                )
            else:
                ids[rule_id] = path

    for path in sorted(ROOT.rglob("AGENTS.md")):
        text = path.read_text(encoding="utf-8").strip()
        if len(text) < 300:
            errors.append(
                f"AGENTS.md appears incomplete: {path.relative_to(ROOT)}"
            )

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Validation passed: {len(ids)} standard IDs, "
        f"{sum(1 for _ in ROOT.rglob('*.json'))} JSON files."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
