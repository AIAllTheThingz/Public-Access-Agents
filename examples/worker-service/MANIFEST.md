---
id: EX-WRK-MAN-001
title: Worker Service Composition Example Manifest
version: 0.1.0
status: baseline
---
# Worker Service Composition Example Manifest

## Purpose

This manifest defines the complete file inventory and acceptance checks for the **Worker Service Composition Example** example.

## Required files

- `AGENTS.md`
- `MANIFEST.md`
- `README.md`
- `composition/STANDARDS_SELECTION.md`
- `composition/TAILORING_DECISIONS.md`
- `deploy/AGENTS.md`
- `docs/AGENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/COMPLETION_EVIDENCE.md`
- `docs/DATA_HANDLING.md`
- `docs/OPERATIONS.md`
- `docs/RELEASE_PLAN.md`
- `docs/RISK_ASSESSMENT.md`
- `docs/TEST_STRATEGY.md`
- `docs/THREAT_MODEL.md`
- `evidence/artifact-record.example.json`
- `evidence/completion-result.example.json`
- `evidence/test-evidence.example.json`
- `project-manifest.json`
- `src/integrations/AGENTS.md`
- `src/worker/AGENTS.md`
- `tests/AGENTS.md`

## Composition

- Profile: `WORKER_SERVICE`
- Languages: `javascript-typescript`
- Disciplines: `architecture`, `testing`, `integration`, `application-security`, `observability`, `sre`, `ci-cd`, `supply-chain`, `documentation`, `release-engineering`
- Platforms: `containers`, `kubernetes`
- Frameworks: none
- Risk: `moderate`

## Acceptance checks

- [ ] Every listed file exists.
- [ ] `project-manifest.json` matches the documented composition.
- [ ] Root and nested `AGENTS.md` files are consistent.
- [ ] Standards selection explains inclusion and meaningful omission.
- [ ] Tailoring decisions identify fictitious facts, owners, assumptions, and open decisions.
- [ ] Architecture, risk, testing, and operations documents agree.
- [ ] Evidence JSON parses and uses the repository schema shape.
- [ ] No production values, credentials, or sensitive data are present.
- [ ] No unresolved placeholders remain.
- [ ] Relative Markdown links resolve.
- [ ] Repository validation passes.
