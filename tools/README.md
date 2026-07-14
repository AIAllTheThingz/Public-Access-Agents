---
id: TOOL-INDEX-001
title: Repository Toolchain
version: 1.2.0
status: baseline
---

# Repository Toolchain

## Purpose

The repository toolchain makes standards, schemas, templates, manifests, composition decisions, and repository releases executable and reviewable.

It provides:

- repository structure validation
- Markdown link and anchor validation
- skill entry-point and package-routing validation
- JSON Schema validation
- template package validation
- tool package validation
- release-policy and tag validation
- project manifest generation
- traceable agent-standards composition
- deterministic release artifact generation
- a unified validation runner

The tools are deliberately conservative. They validate implemented contracts and produce traceable plans, files, or artifacts. They do not grant authorization, prove evidence is truthful, certify compliance, or decide that a system is production-ready. Humans remain annoyingly involved in all the consequential parts.

## Tool catalog

| Tool | Entry point | Mode | Primary responsibility |
|---|---|---|---|
| [Validate Standards](validate-standards/) | `validate_repository.py` | read-only | Validate root files, licensing, ownership, JSON parsing, unique IDs, AGENTS depth, and final-branch hygiene. |
| [Check Links](check-links/) | `check_links.py` | read-only | Validate relative Markdown targets and local heading anchors without network access. |
| [Validate Skills](validate-skills/) | `validate_skills.py` | read-only | Validate skill metadata, progressive disclosure, package routing, registration, local links, and optional UI metadata. |
| [Validate Schemas](validate-schemas/) | `validate_schemas.py` | read-only | Validate Draft 2020-12 contracts, examples, versioned equivalence, and repository instances. |
| [Validate Templates](validate-templates/) | `validate_templates.py` | read-only | Validate template packages, placeholders, examples, stable paths, and schema-backed JSON. |
| [Validate Tools](validate-tools/) | `validate_tools.py` | read-only | Validate tool package structure, executable entry points, contracts, documentation, and tests. |
| [Validate Release](release/) | `validate_release.py` | read-only | Validate VERSION, changelog, release notes, migration notes, release policy, maturity policy, workflow, and tag matching. |
| [Build Release](release/) | `build_release.py` | writes output | Build deterministic archives, SHA-256 checksums, release notes, migration notes, and a release manifest. |
| [Generate Manifest](generate-manifest/) | `generate_manifest.py` | writes output | Produce a schema-valid project manifest from explicit profile, language, discipline, framework, platform, virtualization, operating-system, and networking selections. |
| [Compose Agents](compose-agents/) | `compose_agents.py` | writes output | Create a traceable standards bundle, including selected virtualization, operating-system, and networking packages, without flattening or rewriting source standards. |
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

Validate the release program:

```bash
python tools/release/validate_release.py
```

Build release artifacts safely:

```bash
python tools/release/build_release.py \
  --tag v0.9.0 \
  --output-dir dist
```

Generate a project manifest safely:

```bash
python tools/generate-manifest/generate_manifest.py \
  --name example-service \
  --profile WEB_API \
  --language python \
  --operating-system ubuntu \
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

Remove `--dry-run` only after reviewing the planned output. Generation tools refuse to overwrite existing output unless `--force` is explicit. The release builder refuses to replace an existing distribution directory without `--force`.

## Common command-line contract

Shared validators and generators support:

- `--root PATH`
- `--format text|json`
- `--output PATH`
- `--quiet`
- `--help`

The release builder uses a narrower artifact-generation interface documented in [`release/README.md`](release/README.md).

Tool-specific options are documented in each package README.

See [`TOOL_CONTRACT.md`](TOOL_CONTRACT.md).

## Exit codes

Shared tools use:

- `0`: tool completed and passed
- `1`: tool completed and found validation failures
- `2`: invalid input, missing configuration, or dependency problem
- `3`: unexpected internal failure

The release builder uses `0` for success and `2` for invalid release input or build state.

A nonzero exit code must not be converted to success by a wrapper unless the wrapper explicitly records and reports the failure.

## Structured output

JSON output from shared tools conforms to [`contracts/tool-result.schema.json`](contracts/tool-result.schema.json).

A result contains:

- tool name and version
- `passed`, `failed`, or `error` status
- summary counters
- structured findings
- tool-specific metadata

`passed` means only that the tool's implemented checks passed against the supplied input.

The release builder emits a release manifest describing the source commit and artifact digests.

## Safety model

Read-only validators:

- do not modify repository content
- do not require network access
- report all identified failures unless fail-fast behavior is explicitly selected

Writing tools:

- require explicit output paths
- support dry-run where planning is meaningful
- refuse overwrite without `--force`
- validate inputs before writing
- write deterministically
- use atomic staging where multiple files are produced
- stay within the declared repository root unless an explicit absolute output is supplied

Release tooling additionally:

- packages Git-tracked files only
- validates the tag against `VERSION`
- normalizes archive metadata
- emits SHA-256 checksums
- does not create or push tags
- does not publish releases outside the tag-triggered GitHub workflow

See [`SECURITY_BOUNDARIES.md`](SECURITY_BOUNDARIES.md).

## Development workflow

1. Read `tools/AGENTS.md` and the package README.
2. Identify callers and stable paths.
3. Define compatibility and release impact.
4. Implement the smallest coherent change.
5. Add positive, negative, and error-path tests.
6. Run the affected tool directly.
7. Run all unit tests.
8. Run `validate-all`.
9. Review text and JSON output.
10. Update documentation, examples, changelog, release notes, and migration notes as applicable.

See [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md) and [`TESTING_GUIDE.md`](TESTING_GUIDE.md).

## Validation pipeline

Permanent CI runs:

```bash
python tools/validate-all/run_all.py --include-tests
```

The runner executes validators in this order:

1. repository structure
2. Markdown links and anchors
3. skill entry points and package routes
4. schemas and instances
5. templates
6. tools
7. release program
8. unit tests

Order matters because later validators rely on contracts established by earlier ones.

## Release pipeline

Pushing a valid `v*` tag starts `.github/workflows/release.yml`.

The workflow:

1. verifies the tagged commit is on `main`
2. runs the complete validation pipeline
3. verifies the tag matches `VERSION`
4. builds deterministic ZIP and TAR.GZ archives
5. verifies SHA-256 checksums
6. creates the GitHub Release
7. attaches archives, checksums, release manifest, and migration notes

Tag creation and release publication remain subject to `MAINTAINERS.md` and `RELEASE_POLICY.md`.

## Compatibility

Stable executable paths are public repository interfaces.

Breaking changes include:

- moving or renaming an entry point
- changing exit-code meaning
- removing JSON fields
- changing a writing tool's overwrite behavior
- narrowing accepted input without migration
- changing generated file semantics
- changing release artifact names, archive roots, checksum format, or tag interpretation

See [`RELEASE_AND_COMPATIBILITY.md`](RELEASE_AND_COMPATIBILITY.md) and [`../RELEASE_POLICY.md`](../RELEASE_POLICY.md).

## Troubleshooting

Common failures include:

- missing `jsonschema` dependency
- running from an incomplete checkout
- stale placeholders in completed examples
- broken relative links or anchors
- unknown profile or package selections
- output already existing without `--force`
- a bundle source missing from the selected package
- a tag that does not match `VERSION`
- missing release or migration notes
- a tagged commit that is not on `main`
- checksum verification failure

See [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md).

## Completion boundary

A green toolchain proves that the repository satisfied the implemented automated checks at that revision. It does not prove every standard is correct, every package is stable, every approval is authoritative, every release note is complete, or every production risk is controlled.
