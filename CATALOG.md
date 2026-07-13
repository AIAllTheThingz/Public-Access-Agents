# Standards Catalog

This catalog lists the standards available for composition into a project.

## Governance

The governance system defines authority, precedence, risk, evidence, review, exceptions, secure development, production readiness, threat modeling, vulnerability response, and policy lifecycle across every package in this repository.

| Standard | Purpose |
|---|---|
| [Governance index](governance/README.md) | Selection, precedence, operating model, adoption, evidence states, and maintenance |
| [Organization Contract](governance/ORGANIZATION_CONTRACT.md) | Defines precedence, non-negotiable controls, authority, and accountability |
| [Agent Working Method](governance/AGENT_WORKING_METHOD.md) | Defines discovery, planning, implementation, validation, and reporting |
| [Risk Classification](governance/RISK_CLASSIFICATION.md) | Scales review, testing, authorization, rollback, and evidence |
| [Completion Evidence](governance/COMPLETION_EVIDENCE.md) | Defines proof required before claiming completion |
| [Exception Process](governance/EXCEPTION_PROCESS.md) | Provides a time-bounded, reviewed path for deviations |
| [AI-Generated Code Policy](governance/AI_GENERATED_CODE_POLICY.md) | Defines responsibility, verification, provenance, and review for AI-assisted work |
| [Human Review Policy](governance/HUMAN_REVIEW_POLICY.md) | Defines work requiring accountable human review and approval |
| [Production Readiness](governance/PRODUCTION_READINESS.md) | Defines operational, recovery, support, and go-live gates |
| [Secure Development Policy](governance/SECURE_DEVELOPMENT_POLICY.md) | Integrates security into design, implementation, testing, delivery, and maintenance |
| [Threat Modeling Policy](governance/THREAT_MODELING_POLICY.md) | Defines threat-model triggers, contents, mitigations, and residual risk |
| [Vulnerability Response](governance/VULNERABILITY_RESPONSE.md) | Defines confidential intake, triage, containment, remediation, verification, and closure |

See the [governance policy map](governance/POLICY_MAP.md), [adoption guide](governance/ADOPTION_GUIDE.md), [operating model](governance/OPERATING_MODEL.md), and [decision matrix](governance/GOVERNANCE_DECISION_MATRIX.md).

## Engineering disciplines

- [Application Security](disciplines/application-security/)
- [Architecture and System Design](disciplines/architecture/)
- [Testing and Quality Engineering](disciplines/testing/)
- [API Engineering](disciplines/api-engineering/)
- [Integration Engineering](disciplines/integration/)
- [Database Engineering](disciplines/database/)
- [Data Engineering](disciplines/data-engineering/)
- [Accessibility](disciplines/accessibility/)
- [Privacy and Data Governance](disciplines/privacy/)
- [Observability](disciplines/observability/)
- [Site Reliability Engineering](disciplines/sre/)
- [Documentation](disciplines/documentation/)
- [CI/CD](disciplines/ci-cd/)
- [Software Supply Chain](disciplines/supply-chain/)
- [Release Engineering](disciplines/release-engineering/)

## Languages

- [PowerShell 7.x](languages/powershell/)
- [.NET 10 LTS](languages/dotnet/)
- [JavaScript and TypeScript](languages/javascript-typescript/)
- [Python](languages/python/)
- [Java](languages/java/)
- [Go](languages/go/)
- [Rust](languages/rust/)
- [Bash](languages/bash/)
- [SQL](languages/sql/)
- [Terraform and OpenTofu](languages/terraform-opentofu/)

## Platforms

Platform packages are complete, independently adoptable overlays for execution, deployment, identity, network, data, state, policy, observability, resilience, recovery, cost, capacity, quota, and operational ownership.

- [Containers](platforms/containers/)
- [Kubernetes](platforms/kubernetes/)
- [Terraform and OpenTofu](platforms/terraform/)
- [Microsoft Azure](platforms/azure/)
- [Amazon Web Services](platforms/aws/)
- [Google Cloud Platform](platforms/gcp/)

See the [platforms index](platforms/README.md) for selection, shared responsibility, change lifecycle, decision scaling, adoption, validation, and maintenance guidance.

## Frameworks

Framework packages are complete, independently adoptable overlays with framework-specific agent instructions, standards, templates, manifests, examples, adoption guidance, and completion evidence.

- [ASP.NET Core](frameworks/aspnet-core/)
- [React](frameworks/react/)
- [Angular](frameworks/angular/)
- [Spring Boot](frameworks/spring-boot/)
- [FastAPI](frameworks/fastapi/)

See the [frameworks index](frameworks/README.md) for selection, composition, tailoring, validation, maturity, and maintenance guidance.

## Project profiles

Project profiles are complete composition packages that select and organize governance, language, discipline, framework, platform, project-decision, evidence, and operational expectations for a project shape. Canonical uppercase files remain stable compatibility entry points; lowercase directories contain the complete packages.

- [Web API](profiles/WEB_API.md) ([complete package](profiles/web-api/))
- [Web application](profiles/WEB_APPLICATION.md) ([complete package](profiles/web-application/))
- [Worker service](profiles/WORKER_SERVICE.md) ([complete package](profiles/worker-service/))
- [Command-line tool](profiles/CLI_TOOL.md) ([complete package](profiles/cli-tool/))
- [Desktop application](profiles/DESKTOP_APPLICATION.md) ([complete package](profiles/desktop-application/))
- [Mobile application](profiles/MOBILE_APPLICATION.md) ([complete package](profiles/mobile-application/))
- [Serverless function](profiles/SERVERLESS_FUNCTION.md) ([complete package](profiles/serverless-function/))
- [Data pipeline](profiles/DATA_PIPELINE.md) ([complete package](profiles/data-pipeline/))
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

## Reusable templates

The template library provides governed, validated starting structures for agent instructions, architecture decisions, risk assessments, threat models, exceptions, completion evidence, machine-readable records, authorization, human review, production readiness, releases, recovery, and operations.

- [Template library index](templates/README.md)
- [Template catalog](templates/TEMPLATE_CATALOG.md)
- [Selection guide](templates/TEMPLATE_SELECTION_GUIDE.md)
- [Placeholder conventions](templates/PLACEHOLDER_CONVENTIONS.md)
- [Customization policy](templates/CUSTOMIZATION_POLICY.md)
- [Validation guide](templates/VALIDATION_GUIDE.md)

The seven original template paths remain stable. Every template package now includes detailed adoption guidance, a review checklist, and a completed fictitious example.

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
