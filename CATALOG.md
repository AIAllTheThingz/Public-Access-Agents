# Standards Catalog

This catalog lists the standards available for composition into a project.

## Governance

| Standard | Purpose |
|---|---|
| Organization Contract | Defines precedence, non-negotiable controls, and accountability |
| Agent Working Method | Defines discovery, planning, implementation, validation, and reporting |
| Risk Classification | Scales review and evidence to change risk |
| Completion Evidence | Defines proof required before claiming completion |
| Exception Process | Provides a time-bounded, reviewed path for deviations |
| AI-Generated Code Policy | Defines responsibility for agent-produced code |
| Secure Development Policy | Integrates security into normal engineering work |
| Human Review Policy | Identifies work that requires accountable human review |
| Production Readiness | Defines operational readiness gates |
| Threat Modeling | Defines when and how threat models are produced |
| Vulnerability Response | Defines handling of suspected and confirmed vulnerabilities |

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

- [Containers](platforms/containers/)
- [Kubernetes](platforms/kubernetes/)
- [Terraform and OpenTofu](platforms/terraform/)
- [Microsoft Azure](platforms/azure/)
- [Amazon Web Services](platforms/aws/)
- [Google Cloud Platform](platforms/gcp/)

## Frameworks

- [ASP.NET Core](frameworks/aspnet-core/)
- [React](frameworks/react/)
- [Angular](frameworks/angular/)
- [Spring Boot](frameworks/spring-boot/)
- [FastAPI](frameworks/fastapi/)

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
