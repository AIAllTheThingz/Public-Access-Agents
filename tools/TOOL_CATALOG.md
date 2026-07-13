---
id: TOOL-CATALOG-001
title: Tool Catalog
version: 1.0.0
status: baseline
---

# Tool Catalog

## Catalog

| Tool | Reads | Writes | External dependency | Primary owner |
|---|---|---|---|---|
| Validate Standards | Repository tree | None | None | Repository maintainers |
| Check Links | Markdown files | None | None | Documentation maintainers |
| Validate Schemas | Schemas and JSON instances | None | `jsonschema[format]` | Schema maintainers |
| Validate Templates | Templates, examples, schemas | None | `jsonschema[format]` | Template maintainers |
| Validate Tools | Tool packages and tests | None | None | Tool maintainers |
| Generate Manifest | Profiles, package directories, schema | Manifest file | `jsonschema[format]` | Project adopter |
| Compose Agents | Project manifest and selected standards | Bundle directory | `jsonschema[format]` | Project adopter |
| Validate All | Validator entry points and tests | Optional result file | Validator dependencies | Repository maintainers |

## Stable entry points

The Python entry paths listed in the root README are stable interfaces.

## Selection

Use a specific validator during focused development. Use `validate-all` before review or merge.

Use `generate-manifest` when beginning a project composition. Use `compose-agents` only after the generated manifest is reviewed and accepted as a correct selection record.

## Ownership

Every tool change must identify:

- implementation owner
- contract owner
- CI owner
- affected consumers
- documentation owner
- migration owner for breaking changes

## Evidence

A tool execution record should capture:

- tool path and version
- repository revision
- exact command
- environment
- exit code
- JSON result where practical
- checks not run
- limitations
