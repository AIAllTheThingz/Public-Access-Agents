---
id: TOOL-PKG-VALIDATE-SKILLS-001-MANIFEST
title: Validate Skills Tool Manifest
version: 1.0.0
status: baseline
---

# Validate Skills Tool Manifest

## Required files

- `validate_skills.py`
- `README.md`
- `MANIFEST.md`
- `examples/README.md`

## Shared contracts

- `../TOOL_CONTRACT.md`
- `../contracts/tool-result.schema.json`
- `../tests/test_validate_skills.py`
- `../../MANIFEST.md`
- `../../RELEASE_POLICY.md`

## Required checks

- skill discovery
- frontmatter structure and allowed keys
- required name and description fields
- name syntax, length, uniqueness, and directory alignment
- explicit description trigger clause
- nonempty, titled, bounded instruction body
- unresolved placeholder detection
- safe and existing local links
- complete, nonduplicate package routing
- bidirectional root-manifest registration
- optional `agents/openai.yaml` interface validation when present
- deterministic structured output

## Acceptance checks

- entry point compiles
- `--help` exits successfully
- text output is readable
- JSON output conforms to the result contract
- exit codes match the common contract
- the repository's real skills pass
- positive, boundary, negative, and deterministic tests pass
- stable path remains unchanged
- documentation and examples match behavior
- `validate-all` runs the validator
- permanent CI reaches the validator through `validate-all`
