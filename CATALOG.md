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

Profiles supplement rather than replace governance, language, discipline, platform, and framework standards.

- [Web API](profiles/WEB_API.md)
- [Web application](profiles/WEB_APPLICATION.md)
- [Worker service](profiles/WORKER_SERVICE.md)
- [Command-line tool](profiles/CLI_TOOL.md)
- [Desktop application](profiles/DESKTOP_APPLICATION.md)
- [Mobile application](profiles/MOBILE_APPLICATION.md)
- [Serverless function](profiles/SERVERLESS_FUNCTION.md)
- [Data pipeline](profiles/DATA_PIPELINE.md)
- [Public library](profiles/PUBLIC_LIBRARY.md)
- [Internal automation](profiles/INTERNAL_AUTOMATION.md)
- [Multi-tenant SaaS](profiles/MULTI_TENANT_SAAS.md)
- [Security tool](profiles/SECURITY_TOOL.md)
- [AI agent application](profiles/AI_AGENT_APPLICATION.md)

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
