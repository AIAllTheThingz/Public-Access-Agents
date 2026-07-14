---
id: DISC-MAN-CICD
title: CI/CD Package Manifest
version: 0.1.0
status: baseline
---
# CI/CD Package Manifest

## Required files

- `AGENTS.md`
- `README.md`
- `MANIFEST.md`
- `standards/WORKFLOW_DESIGN_STANDARD.md`
- `standards/PERMISSIONS_SECRETS_STANDARD.md`
- `standards/DEPENDENCY_PINNING_STANDARD.md`
- `standards/BUILD_TEST_GATES_STANDARD.md`
- `standards/ARTIFACT_PROVENANCE_STANDARD.md`
- `standards/DEPLOYMENT_ENVIRONMENT_STANDARD.md`
- `standards/ROLLBACK_RECOVERY_STANDARD.md`
- `standards/COMPLETION_EVIDENCE.md`
- `templates/ADOPTION_CHECKLIST.md`
- `templates/REVIEW_CHECKLIST.md`
- `templates/EVIDENCE_RECORD_TEMPLATE.md`
- `examples/ADOPTION_EXAMPLE.md`

## Package acceptance checks

- `AGENTS.md` preserves stable discipline rule identifiers and references the supporting standards.
- `README.md` explains scope, adoption, tailoring, evidence, validation, companion disciplines, and limitations.
- Every supporting standard has unique front matter and a completion gate.
- Templates contain placeholders rather than environment-specific production values.
- The example uses fictitious context and demonstrates composition rather than claiming universal applicability.
- Relative Markdown links resolve.
- No credentials, tokens, private keys, internal hostnames, production endpoints, or sensitive identifiers are present.
- The package status and version are consistent across maintained entry points.
- Changes include validation evidence and disclose checks not run.

## Repository validation

Run from the repository root:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```

## Adoption validation

The adopting repository must also verify:

- applicable requirements were selected and omissions were documented
- project owners and reviewers are named
- language, framework, platform, virtualization, operating-system, networking, profile, and companion-discipline packages are composed correctly
- project validation and evidence requirements are executable
- exceptions are reviewed, time-bounded, and traceable
- remaining risks and unsupported claims are visible
