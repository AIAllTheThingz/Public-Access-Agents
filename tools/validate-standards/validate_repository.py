#!/usr/bin/env python3
"""Validate repository structure, JSON, identifiers, and final-branch hygiene."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TOOLS_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_ROOT / "lib"))

from standards_tools import Finding, ToolResult, add_common_arguments, execute_tool  # noqa: E402

TOOL = "validate-standards"
VERSION = "1.0.0"
DEFAULT_ROOT = Path(__file__).resolve().parents[2]
REQUIRED_ROOT = {
    "AGENTS.md",
    "README.md",
    "CATALOG.md",
    "CONTRIBUTING.md",
    "MANIFEST.md",
    "ROADMAP.md",
    "SECURITY.md",
    "SOURCES.md",
}
FRONTMATTER_ID = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
TEMPORARY_NAMES = {
    "profile-build-failure.log",
    "profile-repair-failure.log",
}


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def run(args: argparse.Namespace) -> ToolResult:
    root = args.root.resolve()
    findings: list[Finding] = []
    if not root.is_dir():
        raise ValueError(f"Repository root does not exist or is not a directory: {root}")

    for name in sorted(REQUIRED_ROOT):
        if not (root / name).is_file():
            findings.append(Finding("ROOT_FILE_MISSING", f"Missing required root file: {name}", path=name))

    bootstrap = root / "bootstrap"
    if bootstrap.exists():
        findings.append(Finding(
            "BOOTSTRAP_PRESENT",
            "Temporary bootstrap content remains in the final repository tree.",
            path="bootstrap",
        ))

    for name in sorted(TEMPORARY_NAMES):
        path = root / name
        if path.exists():
            findings.append(Finding("TEMPORARY_ARTIFACT", "Temporary diagnostic artifact remains.", path=name))

    json_count = 0
    for path in sorted(root.rglob("*.json")):
        json_count += 1
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            findings.append(Finding(
                "JSON_INVALID",
                str(exc),
                path=relative(path, root),
                line=getattr(exc, "lineno", None),
            ))

    ids: dict[str, Path] = {}
    markdown_count = 0
    for path in sorted(root.rglob("*.md")):
        markdown_count += 1
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            findings.append(Finding("MARKDOWN_ENCODING", str(exc), path=relative(path, root)))
            continue
        match = FRONTMATTER_ID.search(text)
        if match:
            document_id = match.group(1)
            if document_id in ids:
                findings.append(Finding(
                    "DUPLICATE_ID",
                    f"Duplicate front-matter ID also used by {relative(ids[document_id], root)}: {document_id}",
                    path=relative(path, root),
                ))
            else:
                ids[document_id] = path

    agents_count = 0
    for path in sorted(root.rglob("AGENTS.md")):
        agents_count += 1
        text = path.read_text(encoding="utf-8").strip()
        if len(text) < args.minimum_agents_length:
            findings.append(Finding(
                "AGENTS_INCOMPLETE",
                f"AGENTS.md contains {len(text)} characters; minimum is {args.minimum_agents_length}.",
                path=relative(path, root),
            ))

    summary = {
        "rootFilesRequired": len(REQUIRED_ROOT),
        "jsonFiles": json_count,
        "markdownFiles": markdown_count,
        "identifiedDocuments": len(ids),
        "agentInstructionFiles": agents_count,
        "findings": len(findings),
    }
    return ToolResult.from_findings(tool=TOOL, version=VERSION, findings=findings, summary=summary)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    add_common_arguments(parser, default_root=DEFAULT_ROOT)
    parser.add_argument(
        "--minimum-agents-length",
        type=int,
        default=300,
        help="Minimum non-whitespace character count for AGENTS.md files.",
    )
    parser.add_argument("--debug", action="store_true", help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    return execute_tool(tool=TOOL, version=VERSION, parser=build_parser(), run=run, argv=argv)


if __name__ == "__main__":
    raise SystemExit(main())
