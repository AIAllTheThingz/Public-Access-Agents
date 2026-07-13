---
id: TEMPLATE-MANIFEST-001
title: Template Library Manifest
version: 0.2.0
status: baseline
---

# Template Library Manifest

## Required collection files

- `AGENTS.md`
- `README.md`
- `MANIFEST.md`
- `TEMPLATE_CATALOG.md`
- `TEMPLATE_SELECTION_GUIDE.md`
- `AUTHORING_GUIDE.md`
- `CUSTOMIZATION_POLICY.md`
- `PLACEHOLDER_CONVENTIONS.md`
- `TEMPLATE_LIFECYCLE.md`
- `VALIDATION_GUIDE.md`
- `COMPLETION_CRITERIA.md`

## Required packages

- `root/`: `AGENTS_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `nested/`: `AGENTS_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `architecture-decision/`: `ADR_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `risk/`: `RISK_ASSESSMENT_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `threat-model/`: `THREAT_MODEL_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `exception/`: `EXCEPTION_RECORD_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `completion/`: `COMPLETION_REPORT_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `project-manifest/`: `PROJECT_MANIFEST_TEMPLATE.json`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.json`
- `test-evidence/`: `TEST_EVIDENCE_TEMPLATE.json`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.json`
- `artifact-record/`: `ARTIFACT_RECORD_TEMPLATE.json`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.json`
- `authorization/`: `CHANGE_AUTHORIZATION_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `human-review/`: `HUMAN_REVIEW_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `production-readiness/`: `PRODUCTION_READINESS_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `release/`: `RELEASE_PLAN_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `recovery/`: `ROLLBACK_RECOVERY_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`
- `operations/`: `RUNBOOK_TEMPLATE.md`, `README.md`, `REVIEW_CHECKLIST.md`, `examples/EXAMPLE.md`

JSON template packages also include an example README.

## Required tooling

- `tools/validate-templates/README.md`
- `tools/validate-templates/validate_templates.py`

## Stable compatibility paths

The following original paths must remain present:

- `root/AGENTS_TEMPLATE.md`
- `nested/AGENTS_TEMPLATE.md`
- `architecture-decision/ADR_TEMPLATE.md`
- `completion/COMPLETION_REPORT_TEMPLATE.md`
- `exception/EXCEPTION_RECORD_TEMPLATE.md`
- `risk/RISK_ASSESSMENT_TEMPLATE.md`
- `threat-model/THREAT_MODEL_TEMPLATE.md`

## Acceptance checks

- all required collection files exist
- all package files exist
- stable paths remain present
- every Markdown document has a unique ID
- package READMEs meet minimum depth
- placeholders use the approved syntax
- every placeholder is documented
- examples contain no placeholders
- JSON templates and examples parse
- schema-backed examples validate
- relative links pass
- no secret-like example value is present
- permanent CI runs template validation
