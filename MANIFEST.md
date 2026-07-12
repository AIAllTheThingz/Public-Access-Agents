# Repository Manifest

## Stable entry points

- `AGENTS.md`
- `README.md`
- `CATALOG.md`
- `SOURCES.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `ROADMAP.md`

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

## Complete composition examples

- `examples/minimal`
- `examples/web-api`
- `examples/worker-service`
- `examples/full-stack`

Each complete example includes root and nested agent instructions, a project manifest, composition rationale, tailoring decisions, architecture, risk, testing, operations, completion evidence, and schema-shaped JSON evidence.

## Baseline governance and supporting standards

- `governance`
- `platforms`
- `profiles`
- `templates`
- `schemas`
- `tools`

## Validation

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```
