#!/usr/bin/env python3
"""Validate schema documents, examples, and repository instances."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit(
        "Missing dependency 'jsonschema'. Install with: "
        "python -m pip install -r tools/validate-schemas/requirements.txt"
    ) from exc

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_ROOT = ROOT / "schemas"

SCHEMA_NAMES = [
    "artifact-record",
    "completion-result",
    "exception-record",
    "project-manifest",
    "risk-classification",
    "test-evidence",
]

INSTANCE_RULES = [
    ("project-manifest.json", "project-manifest"),
    ("completion-result", "completion-result"),
    ("test-evidence", "test-evidence"),
    ("artifact-record", "artifact-record"),
    ("exception-record", "exception-record"),
    ("risk-classification", "risk-classification"),
]


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Invalid JSON in {path.relative_to(ROOT)} at line {exc.lineno}, "
            f"column {exc.colno}: {exc.msg}"
        ) from exc


def json_pointer(parts: list[Any]) -> str:
    if not parts:
        return "/"
    encoded = []
    for part in parts:
        text = str(part).replace("~", "~0").replace("/", "~1")
        encoded.append(text)
    return "/" + "/".join(encoded)


def normalized_schema(schema: dict[str, Any]) -> dict[str, Any]:
    value = json.loads(json.dumps(schema))
    value.pop("$id", None)
    value.pop("x-versionedSchema", None)
    return value


def validate_instance(instance_path: Path, schema_path: Path, expect_valid: bool) -> list[str]:
    instance = load_json(instance_path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.absolute_path))

    relative_instance = instance_path.relative_to(ROOT)
    relative_schema = schema_path.relative_to(ROOT)

    if expect_valid and errors:
        return [
            f"{relative_instance} failed {relative_schema} at "
            f"{json_pointer(list(error.absolute_path))}: {error.message}"
            for error in errors
        ]

    if not expect_valid and not errors:
        return [f"{relative_instance} unexpectedly passed {relative_schema}"]

    return []


def discover_schema(instance_path: Path) -> str | None:
    name = instance_path.name.lower()
    for marker, schema_name in INSTANCE_RULES:
        if marker == "project-manifest.json" and name == marker:
            return schema_name
        if marker != "project-manifest.json" and marker in name:
            return schema_name
    return None


def main() -> int:
    errors: list[str] = []

    for name in SCHEMA_NAMES:
        rolling_path = SCHEMA_ROOT / f"{name}.schema.json"
        versioned_path = SCHEMA_ROOT / "v1" / f"{name}.schema.json"

        if not rolling_path.is_file():
            errors.append(f"Missing rolling schema: {rolling_path.relative_to(ROOT)}")
            continue
        if not versioned_path.is_file():
            errors.append(f"Missing versioned schema: {versioned_path.relative_to(ROOT)}")
            continue

        rolling = load_json(rolling_path)
        versioned = load_json(versioned_path)

        try:
            Draft202012Validator.check_schema(rolling)
        except jsonschema.SchemaError as exc:
            errors.append(f"Invalid schema {rolling_path.relative_to(ROOT)}: {exc.message}")

        try:
            Draft202012Validator.check_schema(versioned)
        except jsonschema.SchemaError as exc:
            errors.append(f"Invalid schema {versioned_path.relative_to(ROOT)}: {exc.message}")

        if normalized_schema(rolling) != normalized_schema(versioned):
            errors.append(
                f"Rolling and versioned schemas differ beyond identifier metadata: {name}"
            )

        example_root = SCHEMA_ROOT / "examples" / name
        valid_path = example_root / "valid.example.json"
        invalid_path = example_root / "invalid.example.json"

        if not valid_path.is_file():
            errors.append(f"Missing positive example: {valid_path.relative_to(ROOT)}")
        else:
            errors.extend(validate_instance(valid_path, versioned_path, True))

        if not invalid_path.is_file():
            errors.append(f"Missing negative example: {invalid_path.relative_to(ROOT)}")
        else:
            errors.extend(validate_instance(invalid_path, versioned_path, False))

    for path in sorted(ROOT.rglob("*.json")):
        if SCHEMA_ROOT in path.parents:
            continue
        schema_name = discover_schema(path)
        if schema_name is None:
            continue
        schema_path = SCHEMA_ROOT / "v1" / f"{schema_name}.schema.json"
        errors.extend(validate_instance(path, schema_path, True))

    if errors:
        print("Schema validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Schema validation passed: "
        f"{len(SCHEMA_NAMES)} rolling schemas, "
        f"{len(SCHEMA_NAMES)} versioned schemas, "
        f"{len(SCHEMA_NAMES)} positive examples, "
        f"{len(SCHEMA_NAMES)} negative examples."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
