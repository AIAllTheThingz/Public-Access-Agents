# Repository Agent Instructions

## Purpose

This repository contains public engineering standards for coding agents.

Changes must improve the quality, safety, maintainability, testability, portability, or evidence requirements of the standards without silently weakening existing controls.

## Required working method

Before modifying this repository:

1. Read `README.md`, `CONTRIBUTING.md`, and the affected package's `AGENTS.md`.
2. Inspect all supporting standards referenced by the affected package.
3. Identify whether the change is:
   - editorial
   - behavioral
   - security-related
   - compatibility-related
   - breaking
4. Make the smallest coherent change.
5. Update cross-references, manifests, examples, and templates affected by the change.
6. Validate Markdown links and structured configuration.
7. Report exactly what was changed and what was not validated.

## Non-negotiable rules

- Do not weaken security controls merely to simplify generated code.
- Do not remove testing or completion-evidence requirements without documented rationale.
- Do not claim a standard guarantees security, correctness, compliance, or production readiness.
- Do not add environment-specific production values.
- Do not include credentials, tokens, private keys, internal host names, or sensitive identifiers.
- Use fictitious values in examples.
- Do not copy proprietary standards or copyrighted material into the repository without compatible permission.
- Cite public authoritative sources when a rule depends on an external standard.
- Keep normative requirements separate from explanatory rationale where practical.
- Avoid duplicating the same rule across many files when a referenced shared rule is sufficient.
- Preserve stable rule identifiers when they are introduced.
- Do not reformat unrelated files.

## Package boundaries

Language packages live under `languages/`.

Each language package should contain:

- `AGENTS.md`
- `README.md`
- `MANIFEST.md`
- `standards/`
- `templates/`
- `examples/` where applicable

A package must remain usable independently after being copied into another repository.

## Completion evidence

The completion summary must include:

- files created, modified, or deleted
- standards or behavior changed
- security impact
- compatibility impact
- validation performed
- links or references checked
- limitations
- remaining risks
