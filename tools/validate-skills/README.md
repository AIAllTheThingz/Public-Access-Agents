---
id: TOOL-PKG-VALIDATE-SKILLS-001
title: Validate Skills Tool
version: 1.0.0
status: baseline
---

# Validate Skills Tool

## Purpose

Validate repository `SKILL.md` entry points, progressive-disclosure constraints, package-routing coverage, root-manifest registration, safe local references, and optional agent UI metadata.

Status: **baseline**

## Stable entry point

[`validate_skills.py`](validate_skills.py)

The stable path is part of the repository tooling contract. Moving or renaming it requires migration guidance, release classification, test updates, and CI review.

## Operating mode

- Reads: `SKILL.md`, repository `MANIFEST.md`, collection manifests, routed package directories, linked local paths, and optional `agents/openai.yaml`
- Writes: only an optional result file supplied with `--output`
- Network: none
- Default behavior: safe, deterministic, and non-destructive

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
python tools/validate-skills/validate_skills.py --help
```

## Skill contract

Every discovered `SKILL.md` must:

- begin with delimited YAML frontmatter
- contain only the `name` and `description` frontmatter keys
- provide nonempty single-line scalar values for both keys
- use a lowercase, hyphen-separated name no longer than 64 characters
- use a name identical to the skill directory name
- use a repository-unique skill name
- explain both capability and triggering in the description
- include the phrase `Use when` in the description
- contain a nonempty Markdown instruction body
- contain an H1 title
- remain within the configured progressive-disclosure line limit
- avoid unresolved placeholder markers
- keep trigger guidance out of a dedicated `When to use` body section

The default body limit is 500 lines. The default description range is 40 through 1,024 characters.

## Progressive disclosure

Skill metadata is always available to the agent. The instruction body is loaded only after the skill triggers. Linked resources are loaded only when needed.

The validator enforces this boundary by keeping triggering language in the description and bounding body length. It does not require every possible detail to appear in `SKILL.md`.

Large variant-specific material should remain in linked standards, references, scripts, templates, or assets.

## Package-routing contract

A collection skill is a router for the packages immediately below it.

The validator identifies packages from:

- immediate child directories containing `AGENTS.md` and either `MANIFEST.md` or `README.md`
- package paths declared beneath a collection manifest heading such as `Complete packages` or `Complete platform packages`

Every identified package must be linked exactly once from the skill body. Missing routes and duplicate routes are failures.

This check establishes routing coverage. It does not decide which package is semantically correct for a particular user request.

## Registry contract

The root [`../../MANIFEST.md`](../../MANIFEST.md) is the canonical skill registry.

Its `Agent skill entry points` section must:

- exist
- register every discovered `SKILL.md`
- reference existing paths inside the repository root
- register each skill exactly once

Registration is bidirectional: a registered path must exist, and every discovered skill must be registered.

## Link safety

The validator checks local links in each skill body.

It rejects:

- absolute filesystem paths
- Windows absolute filesystem paths
- relative paths that escape the repository root
- missing local targets
- unsafe or unsupported URI schemes

HTTP, HTTPS, mail, and telephone links are not fetched. The separate link validator remains responsible for repository-wide Markdown anchors and documents outside skills.

## Optional agent metadata

Skills may provide `agents/openai.yaml` for UI-facing metadata.

When the file exists, the validator checks:

- an `interface` mapping is present
- `display_name` is present
- `short_description` is present and contains 25 through 64 characters
- `default_prompt` is present and references `$skill-name`
- declared small and large icon paths remain within the skill directory
- declared icon files exist

Metadata is recommended but optional by default. Use `--require-agent-metadata` when a consuming environment requires it for every skill.

## Examples

Run the validator with human-readable output:

```bash
python tools/validate-skills/validate_skills.py
```

Emit machine-readable output:

```bash
python tools/validate-skills/validate_skills.py \
  --format json \
  --output reports/skills.json
```

Require agent UI metadata:

```bash
python tools/validate-skills/validate_skills.py \
  --require-agent-metadata
```

Test a stricter body limit during development:

```bash
python tools/validate-skills/validate_skills.py \
  --max-body-lines 300
```

## Result summary

The result summary reports:

- discovered skill files
- skills registered exactly once
- package routes linked exactly once
- optional metadata files inspected
- total findings

JSON output conforms to [`../contracts/tool-result.schema.json`](../contracts/tool-result.schema.json).

## Finding codes

Finding codes are stable automation interfaces. Major groups include:

- `SKILL_FRONTMATTER_*`
- `SKILL_NAME_*`
- `SKILL_DESCRIPTION_*`
- `SKILL_BODY_*`
- `SKILL_LINK_*`
- `SKILL_PACKAGE_*`
- `SKILL_REGISTRY_*`
- `SKILL_METADATA_*`

Message wording may improve, but a finding code must not silently change meaning.

## Exit codes

- `0`: completed and passed
- `1`: completed with validation failures
- `2`: invalid input, missing configuration, or dependency issue
- `3`: unexpected internal failure

Warnings do not fail a run unless accompanied by an error finding.

## Failure behavior

Input and configuration failures produce status `error`. Contract findings produce status `failed`. Unexpected exceptions produce status `error` and exit code `3`.

The validator reports all identified findings in deterministic path, line, code, and message order.

## Safety requirements

- Resolve all local paths against the supplied repository root.
- Reject links and declarations that escape the root.
- Do not fetch external content.
- Do not execute skill-linked scripts.
- Do not parse or expose secrets from linked resources.
- Do not describe a passed structural result as proof of semantic correctness.
- Preserve nonzero exit codes through wrappers and CI.

## Permanent CI

The complete runner includes `validate-skills` in its permanent sequence:

```bash
python tools/validate-all/run_all.py --include-tests
```

The workflow YAML invokes the aggregate runner, so validator ordering remains in one executable contract.

## Test coverage

Central tests live in [`../tests/test_validate_skills.py`](../tests/test_validate_skills.py).

Run focused tests:

```bash
python -m unittest discover \
  -s tools/tests \
  -p "test_validate_skills.py"
```

The suite covers:

- the repository's real skill collection
- text and JSON output
- missing and unterminated frontmatter
- invalid and duplicate names
- inadequate trigger descriptions
- missing and duplicate package routes
- unregistered and stale registry entries
- absolute, escaping, and missing links
- body line, heading, and placeholder constraints
- malformed optional agent metadata
- deterministic JSON output

## Compatibility

This tool is introduced as version `1.0.0`. Adding it to `validate-all` is a backward-compatible toolchain feature that can reveal previously unenforced repository defects.

Backward-compatible changes may add optional flags, summary fields, metadata fields, or finding codes.

Breaking changes include:

- moving the stable entry path
- changing exit-code meaning
- removing required JSON result fields
- changing existing finding-code meaning
- turning the validator into a writing tool
- requiring optional agent metadata by default
- narrowing accepted skill syntax without release classification and migration guidance

## Limitations

- frontmatter validation intentionally accepts only the repository's simple scalar contract, not general YAML
- semantic trigger quality still requires human review
- correct package routing does not prove correct package selection during use
- local target existence does not prove linked content is accurate
- optional metadata validation checks the supported interface subset, not every possible YAML feature
- the validator does not execute skills or measure their real-world effectiveness
- the validator does not inspect private repository rules or external skill installation state

## Review checklist

Reviewers should confirm:

- documented behavior matches executable behavior
- current repository skills pass
- positive, boundary, negative, and deterministic tests pass
- path containment is preserved
- no network access or linked-script execution was introduced
- finding codes and exit codes remain stable
- the aggregate runner includes the validator
- the tool-package validator includes the package
- catalog, manifests, changelog, and roadmap remain synchronized
- compatibility and release impact are classified
- the complete validation pipeline passes

## Maintenance

Update the script, README, manifest, examples, tests, catalog, changelog, aggregate runner, and compatibility classification together when behavior changes.

## Completion boundary

A successful execution establishes that the discovered skill files satisfy the implemented structural, routing, registration, link, and metadata checks. It does not prove the instructions are optimal, guarantee that an agent will trigger correctly, certify every routed standard, grant merge authority, or establish production readiness.
