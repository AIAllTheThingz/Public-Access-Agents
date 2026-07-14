#!/usr/bin/env python3
"""Validate tool package structure, executable entry points, contracts, and tests."""

from __future__ import annotations

import argparse
import json
import py_compile
import re
import subprocess
import sys
from pathlib import Path

TOOLS_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_ROOT / "lib"))

from standards_tools import Finding, ToolResult, add_common_arguments, execute_tool  # noqa: E402

TOOL = "validate-tools"
VERSION = "1.2.0"
DEFAULT_ROOT = Path(__file__).resolve().parents[2]
TOOL_PACKAGES = {
    "validate-standards": "validate_repository.py",
    "check-links": "check_links.py",
    "validate-skills": "validate_skills.py",
    "validate-schemas": "validate_schemas.py",
    "validate-templates": "validate_templates.py",
    "validate-tools": "validate_tools.py",
    "generate-manifest": "generate_manifest.py",
    "compose-agents": "compose_agents.py",
    "validate-all": "run_all.py",
    "release": "validate_release.py",
}
REQUIRED_COLLECTION = [
    "AGENTS.md", "README.md", "MANIFEST.md", "TOOL_CATALOG.md", "TOOL_CONTRACT.md",
    "DEVELOPMENT_GUIDE.md", "TESTING_GUIDE.md", "SECURITY_BOUNDARIES.md",
    "RELEASE_AND_COMPATIBILITY.md", "TROUBLESHOOTING.md",
]
FRONTMATTER_ID = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def run(args: argparse.Namespace) -> ToolResult:
    root = args.root.resolve()
    tools = root / "tools"
    findings: list[Finding] = []
    ids: dict[str, Path] = {}

    for name in REQUIRED_COLLECTION:
        path = tools / name
        if not path.is_file():
            findings.append(Finding("TOOL_COLLECTION_FILE_MISSING", "Missing tools collection file.", path=rel(path, root)))

    for path in sorted(tools.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER_ID.search(text)
        if not match:
            findings.append(Finding("TOOL_DOC_ID_MISSING", "Tool Markdown document lacks front-matter ID.", path=rel(path, root)))
            continue
        document_id = match.group(1)
        if document_id in ids:
            findings.append(Finding(
                "TOOL_DOC_ID_DUPLICATE",
                f"ID also used by {rel(ids[document_id], root)}: {document_id}",
                path=rel(path, root),
            ))
        else:
            ids[document_id] = path

    for slug, script_name in TOOL_PACKAGES.items():
        package = tools / slug
        script = package / script_name
        for path in (package / "README.md", package / "MANIFEST.md", package / "examples" / "README.md", script):
            if not path.is_file():
                findings.append(Finding("TOOL_PACKAGE_FILE_MISSING", "Missing tool package file.", path=rel(path, root)))
        if (package / "README.md").is_file():
            readme_text = (package / "README.md").read_text(encoding="utf-8")
            if len(readme_text.splitlines()) < args.minimum_readme_lines:
                findings.append(Finding("TOOL_README_THIN", f"README has fewer than {args.minimum_readme_lines} lines.", path=rel(package / "README.md", root)))
            if "planned tool" in readme_text.lower():
                findings.append(Finding("TOOL_STILL_PLANNED", "Tool README still describes the package as planned.", path=rel(package / "README.md", root)))
        if script.is_file():
            text = script.read_text(encoding="utf-8")
            if not text.startswith("#!/usr/bin/env python3"):
                findings.append(Finding("TOOL_SHEBANG", "Python entry point lacks the standard shebang.", path=rel(script, root)))

        for python_file in sorted(package.glob("*.py")):
            try:
                py_compile.compile(str(python_file), doraise=True)
            except py_compile.PyCompileError as exc:
                findings.append(Finding("TOOL_COMPILE", str(exc), path=rel(python_file, root)))

    tests = sorted((tools / "tests").glob("test_*.py"))
    if len(tests) < len(TOOL_PACKAGES):
        findings.append(Finding(
            "TOOL_TEST_COVERAGE",
            f"Expected at least {len(TOOL_PACKAGES)} test modules; found {len(tests)}.",
            path="tools/tests",
        ))

    contract = tools / "contracts" / "tool-result.schema.json"
    try:
        json.loads(contract.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        findings.append(Finding("TOOL_CONTRACT_INVALID", str(exc), path=rel(contract, root)))

    if args.run_unit_tests:
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(tools / "tests"), "-p", "test_*.py"],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0:
            findings.append(Finding(
                "TOOL_TESTS_FAILED",
                "Tool unit tests failed.",
                path="tools/tests",
                details={"stdout": completed.stdout[-4000:], "stderr": completed.stderr[-4000:]},
            ))

    return ToolResult.from_findings(
        tool=TOOL,
        version=VERSION,
        findings=findings,
        summary={
            "toolPackages": len(TOOL_PACKAGES),
            "identifiedDocuments": len(ids),
            "testModules": len(tests),
            "unitTestsRun": args.run_unit_tests,
            "findings": len(findings),
        },
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    add_common_arguments(parser, default_root=DEFAULT_ROOT)
    parser.add_argument("--minimum-readme-lines", type=int, default=100)
    parser.add_argument("--run-unit-tests", action="store_true")
    parser.add_argument("--debug", action="store_true", help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    return execute_tool(tool=TOOL, version=VERSION, parser=build_parser(), run=run, argv=argv)


if __name__ == "__main__":
    raise SystemExit(main())
