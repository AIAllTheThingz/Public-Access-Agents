---
id: TOOL-PKG-VALIDATE-STANDARDS-001
title: Validate Standards Tool
version: 1.2.0
status: baseline
---

# Validate Standards Tool

## Purpose

Validate repository root files, licensing, maintainer ownership, CODEOWNERS routing, JSON parsing, unique document IDs, AGENTS.md depth, and final-branch hygiene.

Status: **baseline**

## Stable entry point

[`validate_repository.py`](validate_repository.py)

The stable path is part of the repository tooling contract. Moving or renaming it requires migration guidance and CI updates.

## Operating mode

- Reads: repository files and paths
- Writes: only an optional result file
- Network: none
- Default behavior: safe and non-destructive

## Common options

```text
--root PATH
--format text|json
--output PATH
--quiet
--help
```

Tool-specific options are shown by:

```bash
python tools/validate-standards/validate_repository.py --help
```

## Checks and behavior

- required root files
- Apache-2.0 license text markers
- required `NOTICE` copyright and license statements
- `LICENSING.md` SPDX identifier, copyright, and stable links
- stale “license not selected” wording
- required `MAINTAINERS.md`
- required `.github/CODEOWNERS`
- current maintainer name and GitHub account
- maintainer-policy sections for area ownership, specialist review, merge authority, emergencies, inactivity, succession, and enforcement
- disclosure of the current single-maintainer limitation
- CODEOWNERS default and sensitive-area routes
- ownership references in `README.md`, `CONTRIBUTING.md`, and `AGENTS.md`
- stale roadmap ownership language
- JSON syntax
- duplicate front-matter IDs
- minimum AGENTS.md depth
- temporary bootstrap and diagnostic artifacts
- committed Python bytecode and cache artifacts

## Licensing checks

The repository requires:

- `LICENSE`
- `NOTICE`
- `LICENSING.md`
- SPDX identifier `Apache-2.0`
- copyright statement `Copyright 2026 Metello Zuccolini`
- Apache License declarations in `README.md` and `CONTRIBUTING.md`

The validator confirms required markers and repository declarations. It does not provide legal advice or determine whether every third-party dependency or referenced work is license-compatible.

## Ownership checks

The repository requires:

- `MAINTAINERS.md`
- `.github/CODEOWNERS`
- current maintainer `Metello Zuccolini` / `@AIAllTheThingz`
- a visible single-maintainer limitation
- an explicit independent-specialist-review requirement
- review routes for governance, security, schemas, tools, workflows, and ownership files
- references to the ownership contracts from root repository guidance

The validator checks repository files. It cannot inspect private GitHub rulesets, repository permissions, administrator bypass settings, private vulnerability-reporting configuration, or whether a reviewer is actually qualified and independent. Those settings and facts require administrative and human review.

## Examples

```bash
python tools/validate-standards/validate_repository.py
```

```bash
python tools/validate-standards/validate_repository.py --format json --output reports/structure.json
```

## Text and JSON results

Text output is for interactive use. JSON output conforms to [`../contracts/tool-result.schema.json`](../contracts/tool-result.schema.json).

Finding codes are intended for automation. Message wording may improve, but a finding code must not silently change meaning.

## Exit codes

- `0`: completed and passed
- `1`: completed with validation failures
- `2`: invalid input, missing configuration, or dependency issue
- `3`: unexpected internal failure

## Safety requirements

- Repository paths are resolved from `--root`.
- The tool does not fetch external content.
- Sensitive values must not be included in findings.
- A passed result must not be described as proof beyond the implemented checks.
- Wrappers must preserve nonzero exit codes.
- Ownership checks must not imply that CODEOWNERS grants authority or independent review.

## Failure behavior

Input and configuration failures produce status `error`. Validation findings produce status `failed`. Unexpected exceptions produce status `error` and exit code `3`.

Do not catch and discard failures merely to keep CI green. Green output created by suppressing errors is not validation. It is interior decoration.

## Test coverage

Central tests live under [`../tests/`](../tests/).

Focused tests cover:

- minimal repository success
- bootstrap rejection
- Python cache rejection
- required license files
- stale unlicensed wording
- NOTICE contents
- Apache-2.0 license markers
- required maintainer policy
- required CODEOWNERS file
- sensitive CODEOWNERS routes
- required maintainer-policy sections
- stale ownership roadmap wording

Run focused tests:

```bash
python -m unittest discover -s tools/tests -p "test_validate_standards*.py"
```

Run the complete suite:

```bash
python tools/validate-all/run_all.py --include-tests
```

## Compatibility

Backward-compatible changes may add optional flags, summary fields, metadata, or new finding codes.

Breaking changes include:

- changing the stable entry path
- changing exit-code meaning
- removing JSON fields
- changing default write or overwrite behavior
- changing generated file semantics
- silently narrowing accepted input
- changing the required maintainer identity or ownership routes without a reviewed ownership transition

## Limitations

- does not require front matter on every Markdown file
- does not validate semantic correctness
- does not determine third-party license compatibility
- does not inspect GitHub rulesets or private repository permissions
- does not prove reviewer competence, independence, or approval authority
- does not replace schema, template, tool, or link validation

## Review checklist

Reviewers should confirm:

- documented behavior matches code
- positive and negative tests exist
- license checks reflect repository policy without modifying Apache-2.0 terms
- ownership checks reflect `MAINTAINERS.md` and CODEOWNERS
- private GitHub settings are reviewed separately
- output and exit codes are stable
- filesystem and subprocess handling are safe
- dependency changes are pinned and justified
- compatibility impact is documented
- the complete pipeline passes

## Maintenance

Update the script, README, manifest, examples, tests, catalog, licensing policy, maintainer policy, CODEOWNERS, and CI together when behavior changes.

## Completion boundary

A successful execution establishes only the outcome of this tool's implemented checks against the identified input. It does not grant authority, prove review independence, inspect private repository configuration, provide legal advice, certify compliance, or prove production readiness.
