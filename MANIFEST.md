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

## Complete composition examples

- `examples/minimal`
- `examples/web-api`
- `examples/worker-service`
- `examples/full-stack`

Each complete example includes root and nested agent instructions, a project manifest, composition rationale, tailoring decisions, architecture, risk, testing, operations, completion evidence, and schema-shaped JSON evidence.

## Baseline supporting standards

- `profiles`
- `templates`
- `schemas`
- `tools`

## Validation

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```
