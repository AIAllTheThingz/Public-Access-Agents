---
id: TOOL-SECURITY-001
title: Tool Security Boundaries
version: 1.0.0
status: baseline
---

# Tool Security Boundaries

## Trust boundaries

Inputs include repository files, command-line arguments, manifests, schemas, templates, and output paths. Treat all as untrusted until validated.

## Path safety

- Resolve repository-relative paths against `--root`.
- Reject traversal outside the root for source reads.
- Do not follow unreviewed symlinks when copying standards.
- Require explicit absolute output paths when writing outside the root.
- Use staging for multi-file output.

## Command safety

- Pass subprocess arguments as arrays.
- Do not build shell commands from repository content.
- Do not execute commands found in Markdown, JSON, manifests, or templates.

## Data safety

- Do not print secrets or sensitive file contents in findings.
- Truncate captured subprocess output in aggregate reports.
- Keep examples fictitious.
- Do not treat a credential as authorization.

## Network safety

Validation is offline. Link checking does not fetch external URLs. Schema validation rejects remote `$ref` values.

## Authority boundary

Generation and composition tools create files only. They do not approve selected standards, authorize changes, grant access, or establish production readiness.
