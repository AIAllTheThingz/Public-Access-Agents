# Repository Manifest

## Stable entry points

- `AGENTS.md`
- `README.md`
- `CATALOG.md`
- `SOURCES.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `ROADMAP.md`

## Complete governance system

- `governance/AGENTS.md`
- `governance/README.md`
- `governance/MANIFEST.md`
- `governance/POLICY_MAP.md`
- `governance/ADOPTION_GUIDE.md`
- `governance/OPERATING_MODEL.md`
- `governance/POLICY_LIFECYCLE.md`
- `governance/CONTROL_EVIDENCE_MODEL.md`
- `governance/GOVERNANCE_DECISION_MATRIX.md`
- eleven governance policies
- governance adoption, authorization, review, risk, exception, readiness, threat, vulnerability, AI-review, evidence, and policy-change templates
- governance workflow and decision examples
- schema-shaped risk, exception, and completion evidence examples

## Complete language packages

- `languages/powershell`
- `languages/dotnet`
- `languages/javascript-typescript`
- `languages/python`
- `languages/java`
- `languages/go`
- `languages/rust`
- `languages/bash`
- `languages/sql`
- `languages/terraform-opentofu`

## Complete discipline packages

- `disciplines/application-security`
- `disciplines/architecture`
- `disciplines/testing`
- `disciplines/api-engineering`
- `disciplines/integration`
- `disciplines/database`
- `disciplines/data-engineering`
- `disciplines/accessibility`
- `disciplines/privacy`
- `disciplines/observability`
- `disciplines/sre`
- `disciplines/documentation`
- `disciplines/ci-cd`
- `disciplines/supply-chain`
- `disciplines/release-engineering`

## Complete framework packages

- `frameworks/aspnet-core`
- `frameworks/react`
- `frameworks/angular`
- `frameworks/spring-boot`
- `frameworks/fastapi`

Each complete framework package includes scoped agent instructions, a useful README, a manifest, framework-specific standards, adoption and review templates, an evidence template, and an adoption example.

## Complete platform packages

- `platforms/containers`
- `platforms/kubernetes`
- `platforms/terraform`
- `platforms/azure`
- `platforms/aws`
- `platforms/gcp`

Each complete platform package includes scoped agent instructions, a useful README, a manifest, platform-specific standards, adoption and review templates, an evidence template, and an adoption example.

The platform collection also includes selection, shared-responsibility, change-lifecycle, and decision-matrix guidance.

## Complete project profile packages

- `profiles/web-api`
- `profiles/web-application`
- `profiles/worker-service`
- `profiles/cli-tool`
- `profiles/desktop-application`
- `profiles/mobile-application`
- `profiles/serverless-function`
- `profiles/data-pipeline`
- `profiles/public-library`
- `profiles/internal-automation`
- `profiles/multi-tenant-saas`
- `profiles/security-tool`
- `profiles/ai-agent-application`

Each complete profile package includes scoped agent instructions, a useful README, a manifest, six profile-specific standards, adoption and review templates, an evidence template, and an adoption example. The uppercase canonical profile files remain stable compatibility entry points.

## Complete schema system

- six rolling Draft 2020-12 schemas under `schemas/`
- six version-pinned schemas under `schemas/v1/`
- schema agent instructions and manifest
- schema catalog
- versioning, compatibility, extension, migration, validation, and design guidance
- positive and negative examples for every contract
- executable schema validation tooling under `tools/validate-schemas/`

The six stable rolling filenames remain present. Long-lived consumers should pin the versioned paths.

## Complete template library

- root and nested agent-instruction templates
- architecture decision records
- risk assessments
- threat models
- standards exception records
- completion reports
- project manifest, test evidence, and artifact record JSON templates
- change authorization and human review records
- production-readiness reviews
- release plans
- rollback and recovery plans
- operational runbooks
- template selection, authoring, customization, placeholder, lifecycle, validation, and completion guidance
- package review checklists and completed fictitious examples
- executable template validation under `tools/validate-templates/`

The seven original template paths remain stable.

## Complete composition examples

- `examples/minimal`
- `examples/web-api`
- `examples/worker-service`
- `examples/full-stack`

Each complete example includes root and nested agent instructions, a project manifest, composition rationale, tailoring decisions, architecture, risk, testing, operations, completion evidence, and schema-shaped JSON evidence.

## Complete repository toolchain

- repository structure validation
- relative Markdown link and anchor validation
- Draft 2020-12 schema and instance validation
- reusable template package validation
- tool package and executable-entry validation
- deterministic project-manifest generation
- traceable agent-standards composition
- unified validation aggregation
- shared result library and JSON result contract
- central unit tests and fixtures
- tool selection, development, testing, security, troubleshooting, and compatibility guidance

The stable validator entry paths remain present. All executable tools support text and JSON results, common exit-code semantics, and offline operation. Writing tools support dry-run and refuse replacement without explicit `--force`.

## Validation

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
python tools/validate-schemas/validate_schemas.py
python tools/validate-templates/validate_templates.py
```
