---
id: PROFILE-MANIFEST-001
title: Project Profiles Manifest
version: 0.2.0
status: baseline
---
# Project Profiles Manifest

## Collection files

- `AGENTS.md`
- `README.md`
- `MANIFEST.md`
- `PROFILE_SELECTION_GUIDE.md`
- `PROFILE_COMPOSITION_MODEL.md`
- `PROFILE_RISK_EVIDENCE_MATRIX.md`
- `PROFILE_LIFECYCLE.md`
- `PROFILE_DECISION_MATRIX.md`

## Complete profile packages

- `WEB_API.md`
- `web-api/`
- `WEB_APPLICATION.md`
- `web-application/`
- `WORKER_SERVICE.md`
- `worker-service/`
- `CLI_TOOL.md`
- `cli-tool/`
- `DESKTOP_APPLICATION.md`
- `desktop-application/`
- `MOBILE_APPLICATION.md`
- `mobile-application/`
- `SERVERLESS_FUNCTION.md`
- `serverless-function/`
- `DATA_PIPELINE.md`
- `data-pipeline/`
- `PUBLIC_LIBRARY.md`
- `public-library/`
- `INTERNAL_AUTOMATION.md`
- `internal-automation/`
- `MULTI_TENANT_SAAS.md`
- `multi-tenant-saas/`
- `SECURITY_TOOL.md`
- `security-tool/`
- `AI_AGENT_APPLICATION.md`
- `ai-agent-application/`

## Package acceptance

Each profile package must include:

- canonical top-level profile file with stable ID
- `AGENTS.md`
- useful `README.md`
- `MANIFEST.md`
- six profile-specific standards
- adoption checklist
- review checklist
- evidence-record template
- adoption example
- unique identifiers
- valid relative links
- explicit non-production boundary

## Validation

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```
