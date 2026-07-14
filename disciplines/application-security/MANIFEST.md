---
id: DISC-MAN-APPSEC
title: Application Security Package Manifest
version: 0.1.0
status: baseline
---
# Application Security Package Manifest

## Required files

- `AGENTS.md`
- `README.md`
- `MANIFEST.md`
- `standards/THREAT_MODELING_STANDARD.md`
- `standards/AUTHENTICATION_AUTHORIZATION_STANDARD.md`
- `standards/INPUT_OUTPUT_SECURITY_STANDARD.md`
- `standards/SECRETS_CRYPTOGRAPHY_STANDARD.md`
- `standards/SECURITY_TESTING_STANDARD.md`
- `standards/VULNERABILITY_MANAGEMENT_STANDARD.md`
- `standards/SECURE_OPERATIONS_STANDARD.md`
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
