#!/usr/bin/env python3
"""Validate reusable template packages, placeholders, examples, and stable paths."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit(
        "Missing dependency 'jsonschema'. Install with: "
        "python -m pip install -r tools/validate-schemas/requirements.txt"
    ) from exc

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_ROOT = ROOT / "templates"
SCHEMA_ROOT = ROOT / "schemas" / "v1"

PACKAGES = {
    "root": ("AGENTS_TEMPLATE.md", "EXAMPLE.md", None),
    "nested": ("AGENTS_TEMPLATE.md", "EXAMPLE.md", None),
    "architecture-decision": ("ADR_TEMPLATE.md", "EXAMPLE.md", None),
    "risk": ("RISK_ASSESSMENT_TEMPLATE.md", "EXAMPLE.md", None),
    "threat-model": ("THREAT_MODEL_TEMPLATE.md", "EXAMPLE.md", None),
    "exception": ("EXCEPTION_RECORD_TEMPLATE.md", "EXAMPLE.md", None),
    "completion": ("COMPLETION_REPORT_TEMPLATE.md", "EXAMPLE.md", None),
    "project-manifest": (
        "PROJECT_MANIFEST_TEMPLATE.json",
        "EXAMPLE.json",
        "project-manifest.schema.json",
    ),
    "test-evidence": (
        "TEST_EVIDENCE_TEMPLATE.json",
        "EXAMPLE.json",
        "test-evidence.schema.json",
    ),
    "artifact-record": (
        "ARTIFACT_RECORD_TEMPLATE.json",
        "EXAMPLE.json",
        "artifact-record.schema.json",
    ),
    "authorization": ("CHANGE_AUTHORIZATION_TEMPLATE.md", "EXAMPLE.md", None),
    "human-review": ("HUMAN_REVIEW_TEMPLATE.md", "EXAMPLE.md", None),
    "production-readiness": ("PRODUCTION_READINESS_TEMPLATE.md", "EXAMPLE.md", None),
    "release": ("RELEASE_PLAN_TEMPLATE.md", "EXAMPLE.md", None),
    "recovery": ("ROLLBACK_RECOVERY_TEMPLATE.md", "EXAMPLE.md", None),
    "operations": ("RUNBOOK_TEMPLATE.md", "EXAMPLE.md", None),
}

REQUIRED_COLLECTION = [
    "AGENTS.md",
    "README.md",
    "MANIFEST.md",
    "TEMPLATE_CATALOG.md",
    "TEMPLATE_SELECTION_GUIDE.md",
    "AUTHORING_GUIDE.md",
    "CUSTOMIZATION_POLICY.md",
    "PLACEHOLDER_CONVENTIONS.md",
    "TEMPLATE_LIFECYCLE.md",
    "VALIDATION_GUIDE.md",
    "COMPLETION_CRITERIA.md",
]

STABLE_PATHS = [
    "root/AGENTS_TEMPLATE.md",
    "nested/AGENTS_TEMPLATE.md",
    "architecture-decision/ADR_TEMPLATE.md",
    "completion/COMPLETION_REPORT_TEMPLATE.md",
    "exception/EXCEPTION_RECORD_TEMPLATE.md",
    "risk/RISK_ASSESSMENT_TEMPLATE.md",
    "threat-model/THREAT_MODEL_TEMPLATE.md",
]

FRONTMATTER_ID = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
PLACEHOLDER = re.compile(r"\{\{([^{}]+)\}\}")
VALID_PLACEHOLDER = re.compile(r"^[A-Z][A-Z0-9_]*$")
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []

    for name in REQUIRED_COLLECTION:
        path = TEMPLATE_ROOT / name
        if not path.is_file():
            errors.append(f"Missing template collection file: {path.relative_to(ROOT)}")

    for relative in STABLE_PATHS:
        path = TEMPLATE_ROOT / relative
        if not path.is_file():
            errors.append(f"Missing stable template path: {path.relative_to(ROOT)}")

    ids: dict[str, Path] = {}
    for path in sorted(TEMPLATE_ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER_ID.search(text)
        if not match:
            errors.append(f"Missing front-matter ID: {path.relative_to(ROOT)}")
            continue
        doc_id = match.group(1)
        if doc_id in ids:
            errors.append(
                f"Duplicate template document ID {doc_id}: "
                f"{ids[doc_id].relative_to(ROOT)} and {path.relative_to(ROOT)}"
            )
        else:
            ids[doc_id] = path

    for slug, (template_name, example_name, schema_name) in PACKAGES.items():
        package = TEMPLATE_ROOT / slug
        required = [
            package / template_name,
            package / "README.md",
            package / "REVIEW_CHECKLIST.md",
            package / "examples" / example_name,
        ]
        if schema_name is not None:
            required.append(package / "examples" / "README.md")

        for path in required:
            if not path.is_file():
                errors.append(f"Missing template package file: {path.relative_to(ROOT)}")

        readme = package / "README.md"
        if readme.is_file():
            readme_text = readme.read_text(encoding="utf-8")
            if len(readme_text.splitlines()) < 100:
                errors.append(f"README appears incomplete: {readme.relative_to(ROOT)}")
        else:
            readme_text = ""

        template = package / template_name
        if template.is_file():
            template_text = template.read_text(encoding="utf-8")
            placeholders = PLACEHOLDER.findall(template_text)
            if not placeholders:
                errors.append(f"Template contains no placeholders: {template.relative_to(ROOT)}")

            for placeholder in placeholders:
                if not VALID_PLACEHOLDER.fullmatch(placeholder):
                    errors.append(
                        f"Invalid placeholder {{{{{placeholder}}}}} in "
                        f"{template.relative_to(ROOT)}"
                    )
                    continue
                token = "{{" + placeholder + "}}"
                if token not in readme_text:
                    errors.append(
                        f"Undocumented placeholder {token} in {template.relative_to(ROOT)}"
                    )

            if template.suffix == ".json":
                try:
                    load_json(template)
                except Exception as exc:  # noqa: BLE001
                    errors.append(f"Invalid JSON template {template.relative_to(ROOT)}: {exc}")

        example = package / "examples" / example_name
        if example.is_file():
            example_text = example.read_text(encoding="utf-8")
            if PLACEHOLDER.search(example_text):
                errors.append(f"Example contains unresolved placeholder: {example.relative_to(ROOT)}")
            if re.search(r"\bTBD\b|<TODO>", example_text, re.IGNORECASE):
                errors.append(f"Example contains unfinished marker: {example.relative_to(ROOT)}")
            for pattern in SECRET_PATTERNS:
                if pattern.search(example_text):
                    errors.append(f"Example contains secret-like value: {example.relative_to(ROOT)}")

            if example.suffix == ".json":
                try:
                    instance = load_json(example)
                except Exception as exc:  # noqa: BLE001
                    errors.append(f"Invalid JSON example {example.relative_to(ROOT)}: {exc}")
                else:
                    if schema_name:
                        schema_path = SCHEMA_ROOT / schema_name
                        if not schema_path.is_file():
                            errors.append(
                                f"Missing schema for example {example.relative_to(ROOT)}: "
                                f"{schema_path.relative_to(ROOT)}"
                            )
                        else:
                            schema = load_json(schema_path)
                            validator = Draft202012Validator(
                                schema, format_checker=FormatChecker()
                            )
                            schema_errors = sorted(
                                validator.iter_errors(instance),
                                key=lambda error: list(error.absolute_path),
                            )
                            for error in schema_errors:
                                location = "/" + "/".join(
                                    str(part) for part in error.absolute_path
                                )
                                errors.append(
                                    f"{example.relative_to(ROOT)} failed "
                                    f"{schema_path.relative_to(ROOT)} at "
                                    f"{location or '/'}: {error.message}"
                                )

        checklist = package / "REVIEW_CHECKLIST.md"
        if checklist.is_file():
            checklist_text = checklist.read_text(encoding="utf-8")
            if "## Decision" not in checklist_text:
                errors.append(
                    f"Review checklist lacks decision section: {checklist.relative_to(ROOT)}"
                )

    if errors:
        print("Template validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Template validation passed: "
        f"{len(PACKAGES)} packages, "
        f"{len(ids)} identified Markdown documents, "
        f"{len(STABLE_PATHS)} stable legacy paths."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
