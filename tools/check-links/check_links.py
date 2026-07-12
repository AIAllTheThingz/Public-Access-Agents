#!/usr/bin/env python3
"""Check relative Markdown file links with the Python standard library."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []

    for document in sorted(ROOT.rglob("*.md")):
        text = document.read_text(encoding="utf-8")
        for raw_target in LINK.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (document.parent / unquote(target)).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"{document.relative_to(ROOT)} links outside repository: {raw_target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"{document.relative_to(ROOT)} has missing link: {raw_target}"
                )

    if errors:
        print("Link validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Relative Markdown links passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
