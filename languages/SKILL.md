---
name: languages
description: Apply this repository's language-specific engineering standards to implementation, scripting, review, refactoring, debugging, testing, packaging, or migration work involving PowerShell 7.x, .NET or C#, JavaScript or TypeScript, Python, Java, Go, Rust, Bash, SQL, or Terraform and OpenTofu. Use when Codex must select and compose the correct language package, produce advanced production-quality code, or validate language-specific work.
---

# Advanced Language Engineering

Use the strongest language capabilities justified by the repository's declared runtime, toolchain, compatibility contract, and operational environment. Treat “advanced” as greater correctness, clarity, safety, testability, performance, and maintainability—not novelty or unnecessary abstraction.

## Establish authority and scope

1. Read the adopting repository's root and nearest scoped `AGENTS.md` files before editing.
2. Read applicable governance, project-profile, discipline, framework, platform, virtualization, operating-system, networking, and project-specific instructions.
3. Inspect source layout, manifests, lockfiles, build configuration, tests, CI, supported runtimes, and existing conventions.
4. Classify the change and its risk before implementation. Identify public APIs, data, privilege, compatibility, deployment, and destructive-action effects.
5. Resolve material uncertainty before making high-risk, privileged, destructive, or production-affecting changes.

Do not treat this skill as permission to override repository instructions or authorize consequential execution.

## Select language packages

Select every package materially affected by the work. Do not select a package merely because a transitive tool mentions the language.

| Evidence in the repository or request | Package |
|---|---|
| `.ps1`, `.psm1`, `.psd1`, PowerShell modules, remoting, or administrative automation | [`powershell/`](powershell/) |
| `.cs`, `.fs`, `.vb`, `.sln`, `.csproj`, MSBuild, or .NET runtime work | [`dotnet/`](dotnet/) |
| `.js`, `.jsx`, `.ts`, `.tsx`, `package.json`, Node.js, or browser code | [`javascript-typescript/`](javascript-typescript/) |
| `.py`, `pyproject.toml`, Python packages, services, CLIs, or automation | [`python/`](python/) |
| `.java`, Maven, Gradle, JVM applications, services, or libraries | [`java/`](java/) |
| `.go`, `go.mod`, Go services, CLIs, libraries, or concurrent systems | [`go/`](go/) |
| `.rs`, `Cargo.toml`, Rust crates, systems code, services, CLIs, or FFI | [`rust/`](rust/) |
| `.sh`, shell entry points, installers, CI helpers, or operational scripts | [`bash/`](bash/) |
| SQL queries, schemas, migrations, stored code, or data-integrity work | [`sql/`](sql/) |
| `.tf`, `.tofu`, HCL modules, providers, state, plans, or applies | [`terraform-opentofu/`](terraform-opentofu/) |

For each selected package:

1. Read its `README.md`, `AGENTS.md`, and `MANIFEST.md` when present.
2. Read the standards relevant to the requested behavior; do not load unrelated standards merely to inflate context.
3. Use package templates for review and completion evidence when the work requires durable records.
4. Use examples only as composition guidance. Never copy fictitious values into a real environment without deliberate replacement and validation.

For polyglot work, define the boundary between languages and apply the integration, API, database, security, testing, observability, and supply-chain disciplines that cross it.

## Engineer the solution

1. Define acceptance criteria, failure behavior, compatibility constraints, and validation commands.
2. Make the smallest coherent change that satisfies the requirement.
3. Match the existing architecture unless a justified architectural change is part of the request.
4. Use current, idiomatic language features supported by the actual configured version.
5. Prefer explicit types, contracts, invariants, ownership, resource lifetime, cancellation, and error semantics where the language supports them.
6. Design module and API boundaries so that callers cannot easily create invalid or unsafe states.
7. Validate untrusted input at trust boundaries. Protect secrets, credentials, sensitive data, file paths, command arguments, serialization, and network operations.
8. Use structured errors and actionable diagnostics. Preserve useful context without leaking sensitive values.
9. Handle concurrency, retries, timeouts, idempotency, cleanup, and partial failure when the execution model makes them relevant.
10. Keep dependencies necessary, version-compatible, license-compatible, and verified against authoritative sources.
11. Comment non-obvious decisions and constraints. Do not narrate self-evident syntax.
12. Update tests, documentation, examples, configuration, and migration guidance affected by the change.

Do not introduce unsupported syntax, speculative dependencies, metaprogramming, reflection, unsafe operations, or abstraction solely to make the implementation appear sophisticated.

## Test difficult behavior

Cover behavior rather than implementation trivia. Include, as applicable:

- happy paths and contract tests
- invalid, missing, boundary, and hostile input
- authorization and denied paths
- error propagation and partial failure
- concurrency, cancellation, timeout, retry, and idempotency behavior
- resource cleanup and rollback or recovery
- compatibility and migration behavior
- regression tests for the reported defect

An AI-generated test that only mirrors the generated implementation is not independent evidence. Prefer externally defined contracts, fixtures, specifications, or regression cases when available.

## Validate in layers

Run the repository's real commands in this order when applicable:

1. formatting and generated-file checks
2. linting and static analysis
3. type checking or compilation
4. focused unit and regression tests
5. integration, contract, and negative tests
6. security and dependency checks
7. build, packaging, and representative runtime checks

Use the selected package's documented commands and the repository's pinned tools. Do not claim a check passed if it was unavailable, skipped, or run against a different artifact.

## Report completion evidence

Report:

- selected language packages and why they apply
- files and behavior changed
- runtime, toolchain, and compatibility assumptions
- security and operational effects
- exact validation commands and results
- checks not run and why
- limitations, residual risks, and required human review

Distinguish implemented, validated, partially validated, and not validated work.
