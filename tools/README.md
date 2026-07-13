---
id: TOOL-INDEX-001
title: Repository Toolchain
version: 1.0.0
status: baseline
---

# Repository Toolchain

## Purpose

The repository toolchain makes standards, schemas, templates, manifests, and composition decisions executable and reviewable.

It provides:

- repository structure validation
- Markdown link and anchor validation
- JSON Schema validation
- template package validation
- tool package validation
- project manifest generation
- traceable agent-standards composition
- a unified validation runner

The tools are deliberately conservative. They validate implemented contracts and produce traceable plans or files. They do not grant authorization, prove evidence is truthful, certify compliance, or decide that a system is production-ready. Humans remain annoyingly involved in all the consequential parts.

## Tool catalog

| Tool | Entry point | Mode | Primary responsibility |
|---|---|---|---|
| [Validate Standards](validate-standards/) | `validate_repository.py` | read-only | Validate root files, JSON parsing, unique IDs, AGENTS depth, and final-branch hygiene. |
| [Check Links](check-links/) | `check_links.py` | read-only | Validate relative Markdown targets and local heading anchors without network access. |
| [Validate Schemas](validate-schemas/) | `validate_schemas.py` | read-only | Validate Draft 2020-12 contracts, examples, versioned equivalence, and repository instances. |
| [Validate Templates](validate-templates/) | `validate_templates.py` | read-only | Validate template packages, placeholders, examples, stable paths, and schema-backed JSON. |
| [Validate Tools](validate-tools/) | `validate_tools.py` | read-only | Validate tool package structure, executable entry points, contracts, documentation, and tests. |
| [Generate Manifest](generate-manifest/) | `generate_manifest.py` | writes output | Produce a schema-valid project manifest from explicit selections. |
| [Compose Agents](compose-agents/) | `compose_agents.py` | writes output | Create a traceable standards bundle without flattening or rewriting source standards. |
| [Validate All](validate-all/) | `run_all.py` | read-only | Run and aggregate the complete validation pipeline. |

See [`TOOL_CATALOG.md`](TOOL_CATALOG.md) for inputs, outputs, dependencies, and ownership.

## Quick start

Install the pinned validation dependency:

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
```

Run the complete validation pipeline:

```bash
python tools/validate-all/run_all.py --include-tests
```

Run one validator:

```bash
python tools/check-links/check_links.py
```

Generate a project manifest safely:

```bash
python tools/generate-manifest/generate_manifest.py \
  --name example-service \
  --profile WEB_API \
  --language python \
  --include-profile-required \
  --risk moderate \
  --dry-run
```

Compose a traceable bundle after reviewing the manifest:

```bash
python tools/compose-agents/compose_agents.py \
  --manifest project-manifest.json \
  --output-dir generated/standards-bundle \
  --dry-run
```

Remove `--dry-run` only after reviewing the planned output. Generation tools refuse to overwrite existing output unless `--force` is explicit.

## Common command-line contract

All executable tools support:

- `--root PATH`
- `--format text|json`
- `--output PATH`
- `--quiet`
- `--help`

Tool-specific options are documented in each package README.

See [`TOOL_CONTRACT.md`](TOOL_CONTRACT.md).

## Exit codes

- `0`: tool completed and passed
- `1`: tool completed and found validation failures
- `2`: invalid input, missing configuration, or dependency problem
- `3`: unexpected internal failure

A nonzero exit code must not be converted to success by a wrapper unless the wrapper explicitly records and reports the failure.

## Structured output

JSON output conforms to [`contracts/tool-result.schema.json`](contracts/tool-result.schema.json).

A result contains:

- tool name and version
- `passed`, `failed`, or `error` status
- summary counters
- structured findings
- tool-specific metadata

`passed` means only that the tool's implemented checks passed against the supplied input.

## Safety model

Read-only validators:

- do not modify repository content
- do not require network access
- report all identified failures unless fail-fast behavior is explicitly selected

Writing tools:

- require explicit output paths
- support dry-run
- refuse overwrite without `--force`
- validate inputs before writing
- write deterministically
- use atomic staging where multiple files are produced
- stay within the declared repository root unless an explicit absolute output is supplied

See [`SECURITY_BOUNDARIES.md`](SECURITY_BOUNDARIES.md).

## Development workflow

1. Read `tools/AGENTS.md` and the package README.
2. Identify callers and stable paths.
3. Define compatibility impact.
4. Implement the smallest coherent change.
5. Add positive, negative, and error-path tests.
6. Run the affected tool directly.
7. Run all unit tests.
8. Run `validate-all`.
9. Review text and JSON output.
10. Update documentation and examples.

See [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md) and [`TESTING_GUIDE.md`](TESTING_GUIDE.md).

## Validation pipeline

Permanent CI runs:

```bash
python tools/validate-all/run_all.py --include-tests
```

The runner executes validators in this order:

1. repository structure
2. Markdown links and anchors
3. schemas and instances
4. templates
5. tools
6. unit tests

Order matters because later validators rely on contracts established by earlier ones.

## Compatibility

Stable executable paths are public repository interfaces.

Breaking changes include:

- moving or renaming an entry point
- changing exit-code meaning
- removing JSON fields
- changing a writing tool's overwrite behavior
- narrowing accepted input without migration
- changing generated file semantics

See [`RELEASE_AND_COMPATIBILITY.md`](RELEASE_AND_COMPATIBILITY.md).

## Troubleshooting

Common failures include:

- missing `jsonschema` dependency
- running from an incomplete checkout
- stale placeholders in completed examples
- broken relative links or anchors
- unknown profile or package selections
- output already existing without `--force`
- a bundle source missing from the selected package

See [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md).

## Completion boundary

A green toolchain proves that the repository satisfied the implemented automated checks at that revision. It does not prove every standard is correct, every example is safe for a real environment, every approval is authoritative, or every production risk is controlled.
