---
id: DISC-MAN-SUPPLY
title: Software Supply Chain Package Manifest
version: 0.1.0
status: baseline
---
# Software Supply Chain Package Manifest

## Required files

- `AGENTS.md`
- `README.md`
- `MANIFEST.md`
- `standards/DEPENDENCY_INVENTORY_STANDARD.md`
- `standards/DEPENDENCY_REVIEW_STANDARD.md`
- `standards/LOCKFILE_REPRODUCIBILITY_STANDARD.md`
- `standards/SBOM_PROVENANCE_STANDARD.md`
- `standards/BUILD_ENVIRONMENT_STANDARD.md`
- `standards/VULNERABILITY_LICENSE_STANDARD.md`
- `standards/RELEASE_ATTESTATION_STANDARD.md`
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
- language, platform, framework, profile, and companion-discipline packages are composed correctly
- project validation and evidence requirements are executable
- exceptions are reviewed, time-bounded, and traceable
- remaining risks and unsupported claims are visible
