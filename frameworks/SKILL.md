---
name: frameworks
description: Apply this repository's framework-specific engineering standards to implementation, review, refactoring, debugging, testing, security, performance, accessibility, observability, or migration work involving Angular, ASP.NET Core, FastAPI, React, or Spring Boot. Use when Codex must select and compose the correct framework and underlying language packages or produce advanced production-quality framework code.
---

# Advanced Framework Engineering

Use framework capabilities to improve architecture, correctness, security, accessibility, operability, performance, and developer experience. Prefer the most capable pattern supported by the repository's actual framework version and constraints; do not force a major upgrade or a fashionable abstraction into unrelated work.

## Establish authority and inspect the application

1. Read the adopting repository's root and nearest scoped `AGENTS.md` files.
2. Inspect framework, language, runtime, package, lock, build, test, deployment, and CI configuration.
3. Identify application boundaries, request or rendering flow, dependency injection or state ownership, data access, background work, authentication, authorization, and external integrations.
4. Identify applicable governance, project-profile, language, discipline, platform, and project-specific standards.
5. Classify risk and compatibility impact before implementation.

Do not infer that a framework default satisfies security, accessibility, privacy, testing, observability, resilience, or production-readiness obligations.

## Select and compose packages

Select every framework materially involved in the requested behavior.

| Framework evidence | Framework package | Required language package |
|---|---|---|
| Angular workspace, components, directives, services, signals, RxJS, routing, or forms | [`angular/`](angular/) | [`../languages/javascript-typescript/`](../languages/javascript-typescript/) |
| ASP.NET Core hosts, middleware, endpoints, controllers, Razor, services, or background workers | [`aspnet-core/`](aspnet-core/) | [`../languages/dotnet/`](../languages/dotnet/) |
| FastAPI applications, routers, dependencies, Pydantic models, lifespan, or ASGI behavior | [`fastapi/`](fastapi/) | [`../languages/python/`](../languages/python/) |
| React components, hooks, rendering, state, routing, or data fetching | [`react/`](react/) | [`../languages/javascript-typescript/`](../languages/javascript-typescript/) |
| Spring Boot configuration, beans, web, data, messaging, actuator, or lifecycle behavior | [`spring-boot/`](spring-boot/) | [`../languages/java/`](../languages/java/) |

For each selected framework:

1. Read its `README.md`, `AGENTS.md`, and `MANIFEST.md`.
2. Read the standards relevant to the requested behavior.
3. Read the underlying language package and apply its implementation and validation rules.
4. Add applicable application-security, architecture, testing, API, database, accessibility, privacy, observability, SRE, CI/CD, supply-chain, and release-engineering disciplines.
5. Add container, orchestration, infrastructure, and cloud platform packages when deployment behavior is affected.

In a mixed-framework repository, define ownership and contracts between applications instead of blending framework conventions across boundaries.

## Design before editing

1. Trace the affected user or system flow from entry point through side effects and response.
2. Define acceptance criteria, failure behavior, lifecycle behavior, compatibility, and observability.
3. Identify trust boundaries and security-sensitive operations.
4. Check framework-version constraints and migration requirements.
5. Choose the smallest design that fits existing architecture and remains testable.

For behavior that may have changed since the repository's pinned version or that is not declared locally, verify current official framework documentation before relying on it.

## Implement production-quality framework code

Apply the selected package standards and, as relevant:

- keep application, domain, infrastructure, presentation, and integration responsibilities explicit
- make dependency lifetimes, ownership, disposal, and test seams deliberate
- use typed models and validate data at trust boundaries
- propagate cancellation and timeouts through asynchronous work
- keep background work observable, idempotent where required, and safe during shutdown
- make authentication and authorization explicit at every protected boundary
- preserve framework protections for encoding, CSRF or antiforgery, CORS, headers, serialization, and secret handling
- prevent data-access, transaction, loading, and concurrency behavior from remaining accidental
- design state and data flow to avoid hidden mutation, stale data, race conditions, and unnecessary rendering or work
- implement accessible semantics, keyboard behavior, focus management, error messaging, and test coverage for user interfaces
- produce structured logs, traces, metrics, health signals, and diagnostics without leaking sensitive data
- handle configuration by environment with startup validation and safe failure
- avoid reflection, magic registration, global state, middleware abuse, or framework extension points without a concrete need

Do not replace framework-native capabilities with custom infrastructure unless the repository requires it and the tradeoff is documented.

## Test the real framework boundary

Test at the lowest level that proves the behavior, then add boundary tests where framework behavior matters. Include, as applicable:

- pure unit tests for domain and transformation logic
- component, endpoint, middleware, dependency, routing, and serialization tests
- authentication, authorization, validation, and hostile-input tests
- data-access and transaction integration tests
- rendering, accessibility, interaction, and state-transition tests
- background-work, startup, shutdown, cancellation, and recovery tests
- performance regression tests for materially affected hot paths
- compatibility and migration tests

Mock external boundaries deliberately. Do not mock away the framework behavior the test claims to verify.

## Validate in layers

Use repository-pinned commands and the selected package's guidance:

1. formatting, linting, and generated-file checks
2. language static analysis and type checking
3. focused unit and regression tests
4. framework integration, accessibility, and security tests
5. build and packaging
6. representative startup and health checks
7. dependency, supply-chain, and vulnerability checks

Record exact commands, results, environment constraints, and checks not run. A successful build does not prove authorization, accessibility, data integrity, operational readiness, or production behavior.

## Report completion evidence

Report:

- selected framework and language packages
- affected application boundaries and user or system flows
- framework and runtime versions used
- architecture, security, accessibility, data, lifecycle, and observability effects
- exact validation commands and results
- compatibility and migration impact
- checks not run, limitations, residual risks, and required reviewers

Distinguish implemented, tested, reviewed, and operationally verified work.
