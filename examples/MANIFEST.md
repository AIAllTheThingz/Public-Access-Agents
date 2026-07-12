---
id: EX-MAN-001
title: Examples Collection Manifest
version: 0.1.0
status: baseline
---
# Examples Collection Manifest

## Purpose

This manifest defines the expected inventory and acceptance criteria for the examples collection.

## Collection files

- `AGENTS.md`
- `README.md`
- `MANIFEST.md`

## Complete composition examples

- `minimal/`
- `web-api/`
- `worker-service/`
- `full-stack/`

## Required files in every example

Each example must include:

- `AGENTS.md`
- `README.md`
- `MANIFEST.md`
- `project-manifest.json`
- `composition/STANDARDS_SELECTION.md`
- `composition/TAILORING_DECISIONS.md`
- `docs/AGENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/RISK_ASSESSMENT.md`
- `docs/TEST_STRATEGY.md`
- `docs/OPERATIONS.md`
- `docs/COMPLETION_EVIDENCE.md`
- at least one nested implementation `AGENTS.md`
- `tests/AGENTS.md`
- `evidence/completion-result.example.json`
- `evidence/test-evidence.example.json`
- `evidence/artifact-record.example.json`

Higher-risk examples must add relevant security, data, accessibility, release, deployment, or recovery documents.

## Acceptance checks

- [ ] Every example README is a useful adoption and review guide.
- [ ] Every example has a root `AGENTS.md` and meaningful nested scopes.
- [ ] The project manifest uses only valid schema properties.
- [ ] Selected standards are linked and justified.
- [ ] Tailoring decisions identify owners, assumptions, omissions, and limits.
- [ ] Evidence JSON parses and follows the repository schema shape.
- [ ] No example contains real production values or secrets.
- [ ] No example claims production readiness.
- [ ] All front-matter identifiers are unique.
- [ ] Relative Markdown links resolve.
- [ ] Repository validation passes.
