- [Public library](profiles/PUBLIC_LIBRARY.md) ([complete package](profiles/public-library/))
- [Internal automation](profiles/INTERNAL_AUTOMATION.md) ([complete package](profiles/internal-automation/))
- [Multi-tenant SaaS](profiles/MULTI_TENANT_SAAS.md) ([complete package](profiles/multi-tenant-saas/))
- [Security tool](profiles/SECURITY_TOOL.md) ([complete package](profiles/security-tool/))
- [AI agent application](profiles/AI_AGENT_APPLICATION.md) ([complete package](profiles/ai-agent-application/))

See the [profiles index](profiles/README.md) for selection, primary and secondary composition, risk scaling, adoption, evidence, lifecycle, and maintenance guidance.

## Machine-readable schemas

The schema system defines versioned Draft 2020-12 contracts for project manifests, risk classifications, standards exceptions, test evidence, artifact records, and completion results.

- [Schema index](schemas/README.md)
- [Schema catalog](schemas/SCHEMA_CATALOG.md)
- [Versioning policy](schemas/VERSIONING_POLICY.md)
- [Compatibility policy](schemas/COMPATIBILITY_POLICY.md)
- [Validation guide](schemas/VALIDATION_GUIDE.md)
- [Executable examples](schemas/examples/)

Long-lived consumers should pin `schemas/v1/` contracts. Rolling top-level paths remain convenience entry points.

## Composition examples

The examples demonstrate how standards are selected, tailored, scoped, and supported by architecture, risk, testing, operations, and evidence documents.

- [Minimal CLI composition](examples/minimal/)
- [Web API composition](examples/web-api/)
- [Worker service composition](examples/worker-service/)
- [Full-stack web application composition](examples/full-stack/)

See the [examples index](examples/README.md) for selection guidance, boundaries, evidence shapes, and adaptation instructions.

## Status terminology

- `baseline`: usable minimum standard
- `stable`: mature and broadly reviewed
- `draft`: usable for review but expected to change
- `planned`: catalog entry only; not an enforceable standard
- `deprecated`: retained for migration only
"""
(root/'CATALOG.md').write_text(catalog_current, encoding='utf-8')

manifest_current = """# Repository Manifest

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

