---
id: TOOL-MANIFEST-001
title: Toolchain Manifest
version: 1.0.0
status: baseline
---

# Toolchain Manifest

## Required collection files

- `AGENTS.md`
- `README.md`
- `MANIFEST.md`
- `TOOL_CATALOG.md`
- `TOOL_CONTRACT.md`
- `DEVELOPMENT_GUIDE.md`
- `TESTING_GUIDE.md`
- `SECURITY_BOUNDARIES.md`
- `RELEASE_AND_COMPATIBILITY.md`
- `TROUBLESHOOTING.md`

## Required executable packages

- `validate-standards`
- `check-links`
- `validate-schemas`
- `validate-templates`
- `validate-tools`
- `generate-manifest`
- `compose-agents`
- `validate-all`

Each package requires:

- stable Python entry point
- useful README
- package manifest
- examples README
- central unit-test coverage
- text and JSON output
- documented exit codes
- documented limitations

## Shared support

- `lib/standards_tools/`
- `contracts/tool-result.schema.json`
- `tests/`

## Acceptance checks

- every Python entry point compiles
- every entry point supports `--help`
- all package READMEs meet minimum depth
- no tool remains documentation-only or marked planned
- unit tests pass
- repository, link, schema, template, and tool validators pass
- generation tools support dry-run and overwrite protection
- JSON reports conform to the tool-result contract
- no bootstrap or temporary diagnostic artifact remains
