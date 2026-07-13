---
id: TOOL-CONTRACT-002
title: Tool Command and Result Contract
version: 1.0.0
status: baseline
---

# Tool Command and Result Contract

## Command-line baseline

Every executable tool supports:

```text
--root PATH
--format text|json
--output PATH
--quiet
--help
```

The default root is the repository containing the tool.

## Exit-code contract

| Code | Meaning |
|---:|---|
| `0` | Completed successfully with no error-level findings. |
| `1` | Completed but validation findings caused failure. |
| `2` | Input, configuration, or dependency prevented valid execution. |
| `3` | Unexpected internal failure. |

## Output contract

Text output is intended for humans. JSON output is intended for CI and automation and conforms to `contracts/tool-result.schema.json`.

Findings use stable codes. Message wording may improve without constituting a breaking change, but code meaning may not change silently.

## Filesystem contract

Read-only tools must not modify the inspected root.

Writing tools must:

- document every output
- support dry-run
- refuse replacement without `--force`
- validate before committing output
- avoid partial multi-file output through staging and atomic replacement
- reject path traversal

## Determinism

Given identical inputs, repository content, tool version, and options, generated semantic output must be identical. Timestamps and environment-specific values are excluded unless explicitly requested.

## Network behavior

Tools are offline by default. External URLs may be documented but are not fetched by repository validators.

## Compatibility

Stable paths, exit codes, result fields, finding codes, and generated file meanings are public interfaces. Breaking changes require migration guidance and a major tool version change.
