#!/usr/bin/env python3
"""Generate complete engineering-discipline standards packages."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from common import DISCIPLINES_ROOT, ROOT, load_catalog, render_agents, render_readme, render_standard
from manifest_render import render_manifest
from template_render import render_adoption_checklist, render_evidence_template, render_example, render_review_checklist
from root_render import render_root_docs

def write_package(key: str, data: dict, catalog: dict[str, dict]) -> None:
    package = DISCIPLINES_ROOT / key
    if package.exists():
        shutil.rmtree(package)
    (package / "standards").mkdir(parents=True)
    (package / "templates").mkdir()
    (package / "examples").mkdir()

    (package / "AGENTS.md").write_text(render_agents(key, data), encoding="utf-8")
    readme = render_readme(key, data, catalog).replace(
        '{data["title"].lower()}', data["title"].lower()
    )
    (package / "README.md").write_text(readme, encoding="utf-8")
    (package / "MANIFEST.md").write_text(render_manifest(key, data), encoding="utf-8")

    for filename, title, summary in data["standards"]:
        (package / "standards" / filename).write_text(
            render_standard(key, data, filename, title, summary),
            encoding="utf-8",
        )

    (package / "templates" / "ADOPTION_CHECKLIST.md").write_text(
        render_adoption_checklist(data), encoding="utf-8"
    )
    (package / "templates" / "REVIEW_CHECKLIST.md").write_text(
        render_review_checklist(data), encoding="utf-8"
    )
    (package / "templates" / "EVIDENCE_RECORD_TEMPLATE.md").write_text(
        render_evidence_template(data), encoding="utf-8"
    )
    (package / "examples" / "ADOPTION_EXAMPLE.md").write_text(
        render_example(key, data, catalog), encoding="utf-8"
    )


def validate_generated(catalog: dict[str, dict]) -> None:
    expected_files = 1 + (15 * 15)
    actual_files = sum(1 for path in DISCIPLINES_ROOT.rglob("*.md"))
    if actual_files != expected_files:
        raise RuntimeError(
            f"Expected {expected_files} discipline Markdown files, found {actual_files}"
        )

    identifiers: dict[str, Path] = {}
    pattern = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
    for path in DISCIPLINES_ROOT.rglob("*.md"):
        match = pattern.search(path.read_text(encoding="utf-8"))
        if not match:
            if path == DISCIPLINES_ROOT / "README.md":
                continue
            raise RuntimeError(f"Missing front-matter id: {path.relative_to(ROOT)}")
        identifier = match.group(1)
        if identifier in identifiers:
            raise RuntimeError(
                f"Duplicate id {identifier}: "
                f"{identifiers[identifier].relative_to(ROOT)} and "
                f"{path.relative_to(ROOT)}"
            )
        identifiers[identifier] = path

    if len(identifiers) != 225:
        raise RuntimeError(f"Expected 225 discipline ids, found {len(identifiers)}")


def main() -> int:
    catalog = load_catalog()
    DISCIPLINES_ROOT.mkdir(exist_ok=True)
    for key, data in catalog.items():
        write_package(key, data, catalog)
    render_root_docs(catalog)
    validate_generated(catalog)
    print("Generated 15 complete discipline packages with 225 unique ids.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
