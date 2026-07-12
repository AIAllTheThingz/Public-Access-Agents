---
id: EX-INDEX-001
title: Standards Composition Examples
version: 0.1.0
status: baseline
---
# Standards Composition Examples

## Purpose

The examples collection shows how the repository's standards can be assembled into realistic project structures. Each example is a **standards composition**, not an application implementation.

The examples answer practical questions that a list of standards cannot answer by itself:

- Which packages apply to this project type?
- Why were they selected?
- How should root and nested `AGENTS.md` files divide responsibility?
- What project facts must be declared instead of invented?
- What architecture, risk, testing, operations, and evidence documents are expected?
- How should completion evidence distinguish implemented, tested, reviewed, and operationally verified work?
- What remains the responsibility of the adopting organization?

All names, systems, users, endpoints, identifiers, data, and evidence are fictitious.

## Example catalog

| Example | Profile | Languages | Risk | Demonstrates |
|---|---|---|---|---|
| [Minimal CLI](minimal/) | CLI tool | PowerShell | Low | Smallest credible composition, bounded scope, tests, documentation, supply-chain controls |
| [Web API](web-api/) | Web API | .NET | Moderate | API contracts, authorization, privacy, observability, container delivery |
| [Worker Service](worker-service/) | Worker service | JavaScript/TypeScript | Moderate | Message processing, integrations, retries, idempotency, Kubernetes operations |
| [Full-Stack Web Application](full-stack/) | Web application | .NET and JavaScript/TypeScript | High | Multi-language composition, API, database, accessibility, privacy, SRE, release engineering |

## What each example contains

```text
example/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── project-manifest.json
├── composition/
│   ├── STANDARDS_SELECTION.md
│   └── TAILORING_DECISIONS.md
├── docs/
│   ├── AGENTS.md
│   ├── ARCHITECTURE.md
│   ├── RISK_ASSESSMENT.md
│   ├── TEST_STRATEGY.md
│   ├── OPERATIONS.md
│   └── COMPLETION_EVIDENCE.md
├── src/
│   └── .../AGENTS.md
├── tests/
│   └── AGENTS.md
└── evidence/
    ├── completion-result.example.json
    ├── test-evidence.example.json
    └── artifact-record.example.json
```

Higher-risk examples include additional threat-model, data-handling, accessibility, release, or deployment documents.

## How to use an example

1. Choose the example closest to the intended project shape.
2. Read its `README.md` before copying anything.
3. Compare its `project-manifest.json` to the actual project.
4. Replace fictitious project facts with reviewed facts.
5. Re-select profiles, languages, disciplines, platforms, and frameworks based on actual scope.
6. Copy or compose the complete applicable standards packages.
7. Tailor the root `AGENTS.md` without weakening inherited controls.
8. Add nested `AGENTS.md` files only where scope or responsibility changes.
9. Replace example evidence with actual commands, results, reviewers, environments, and limitations.
10. Validate the resulting repository.

Do not copy an example blindly. A copied example with false assumptions is merely a more organized mistake.

## Composition layers

A complete project normally combines:

1. [Governance standards](../governance/)
2. One [project profile](../profiles/README.md)
3. One or more [language packages](../languages/README.md)
4. Relevant [discipline packages](../disciplines/README.md)
5. Applicable [platform standards](../platforms/README.md)
6. Applicable [framework standards](../frameworks/README.md)
7. Project-specific root and nested instructions
8. Machine-readable manifests and evidence

The examples show these layers as references. Adopting repositories may copy, vendor, generate, or otherwise compose the standards according to their governance model.

## Example boundaries

The examples intentionally do not include:

- deployable source code
- production credentials or endpoints
- real users, organizations, or data
- legal or regulatory claims
- cloud accounts, tenants, clusters, registries, or databases
- final tool versions unless the referenced package defines them
- proof of performance, scale, availability, or recovery
- approval from accountable reviewers

Those details belong to the adopting repository and its organization.

## Evidence model

Example evidence files use the repository schemas as shapes:

- [`completion-result.schema.json`](../schemas/completion-result.schema.json)
- [`test-evidence.schema.json`](../schemas/test-evidence.schema.json)
- [`artifact-record.schema.json`](../schemas/artifact-record.schema.json)
- [`project-manifest.schema.json`](../schemas/project-manifest.schema.json)

Evidence must state what was actually run. A command marked `not-run` is more trustworthy than a fabricated success.

## Risk scaling

The examples demonstrate different evidence expectations:

- **Low risk:** focused tests, bounded scope, clear limitations, no implied production validation.
- **Moderate risk:** trust boundaries, security and integration testing, operational signals, rollout and recovery planning.
- **High risk:** cross-discipline review, explicit data and accessibility plans, migration and release controls, recovery and SRE evidence.

Risk classification changes required evidence and review depth. It does not make basic safety optional.

## Validation

From the repository root:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```

An adopting repository must add project-specific validation for its runtime, tests, packaging, deployment, infrastructure, security, accessibility, data, and operational requirements.

## Maintaining examples

When an example changes:

- preserve stable identifiers unless a breaking change is approved
- update its README and manifest
- keep project-manifest selections synchronized with the narrative
- update nested instructions when responsibility changes
- refresh evidence shapes and limitations
- validate links and JSON
- remove obsolete files rather than leaving contradictory examples
- document migration impact

## Non-production warning

These examples are educational compositions. They are not production-ready applications, deployment templates, legal advice, security certification, or operational approval. Copying one does not transfer evidence, accountability, or good judgment, tragically.
