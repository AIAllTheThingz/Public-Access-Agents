# .NET Agent Standard

## Purpose

This file defines the mandatory operating rules for coding agents that create, modify, review, test, secure, or document modern .NET applications.

The standard is project-agnostic. It governs how .NET work is performed, not the business purpose of any individual application.

The primary objective is:

> Make the smallest safe, maintainable, testable, observable, and well-documented change that satisfies the stated requirement.

## Scope

These instructions apply to:

- .NET solutions and projects
- C# source code
- ASP.NET Core applications and APIs
- Worker services and background processing
- Class libraries
- Entity Framework Core and other data-access code
- Unit, integration, functional, and architecture tests
- Build, packaging, publishing, and deployment configuration
- NuGet dependencies
- Application configuration
- Documentation and examples
- Database migrations
- Observability and operational instrumentation

## Required Runtime Baseline

New development must target the current .NET LTS release:

- Target framework: `net10.0`
- SDK family: .NET 10
- Language: stable C# supported by the selected .NET 10 SDK
- Tooling: `dotnet` CLI
- Preview SDKs, workloads, packages, and language features are prohibited unless explicitly requested.

Do not add compatibility for .NET Framework, .NET Core, or earlier .NET releases unless explicitly required.

Existing repositories must preserve their declared supported target frameworks unless the task explicitly includes migration.

## Instruction Priority

When instructions conflict, apply them in this order:

1. Explicit user requirements
2. More specific nested `AGENTS.md` instructions
3. This root `AGENTS.md`
4. Repository documentation and established conventions
5. General coding-agent preferences

Do not silently resolve a material conflict. Follow the higher-priority instruction and report the conflict in completion evidence.

## Required Supporting Standards

Before creating or modifying relevant code, read and follow:

- `standards/DOTNET_CODING_STANDARD.md`
- `standards/ARCHITECTURE_STANDARD.md`
- `standards/DOCUMENTATION_STANDARD.md`
- `standards/TESTING_STANDARD.md`
- `standards/SECURITY_STANDARD.md`
- `standards/DEPENDENCY_MANAGEMENT_STANDARD.md`
- `standards/ASPNETCORE_STANDARD.md`
- `standards/DATA_ACCESS_STANDARD.md`
- `standards/OBSERVABILITY_STANDARD.md`
- `standards/COMPLETION_EVIDENCE.md`

These files are mandatory extensions of this `AGENTS.md`.

If a supporting standard conflicts with this file, this file takes precedence.

## Non-Negotiable Rules

### Safe behavior

- Default to the safest practical behavior.
- Validate configuration, input, authorization, and dependencies before mutation.
- Stop when prerequisites are missing or target identity is ambiguous.
- Do not weaken security controls to make code succeed.
- Do not perform destructive or irreversible operations without explicit authorization.
- Use the narrowest operation that satisfies the requirement.
- Preserve cancellation and graceful shutdown paths.

### Scope control

- Make the smallest coherent change.
- Do not modify unrelated files, behavior, formatting, dependencies, or architecture.
- Do not perform broad refactoring unless explicitly requested or required for correctness or safety.
- Preserve existing public contracts unless the requirement explicitly changes them.
- Stop when the requested outcome has been achieved and validated.

### No invented environment details

Do not invent or hardcode:

- Production host names
- Domains
- Tenant identifiers
- User names
- Database names
- Connection strings
- API endpoints
- Certificate thumbprints
- Cloud resource identifiers
- File-system paths
- Credentials
- Secret names
- Deployment assumptions

Use obvious placeholders, strongly typed configuration, or documented inputs.

### Secrets and sensitive data

Never place credentials or sensitive values in:

- Source code
- Tests
- Documentation examples
- Logs
- Metrics
- Traces
- Reports
- Exception messages
- Committed configuration files
- Command-line examples when a safer method exists

Use approved secret-management mechanisms. Redact secrets before logging or serialization.

### Input validation

Treat all external input as untrusted, including:

- HTTP requests
- Message payloads
- Configuration
- Environment variables
- Database values
- File names and paths
- Uploaded files
- Remote-service responses
- Claims and headers
- Native-command output

Validate type, length, range, format, allowed values, authorization, and operational safety at the boundary.

### Public contracts

Treat public behavior as a contract, including:

- Public types and members
- HTTP routes and methods
- Request and response schemas
- Status codes
- Problem Details
- Configuration keys
- Database schemas
- Message schemas
- Event names
- Package APIs
- Exit codes
- Telemetry dimensions

Breaking changes require explicit authorization, migration guidance, tests, and documentation.

### Async and cancellation

- Use asynchronous APIs for asynchronous work.
- Do not block asynchronous code with `.Result`, `.Wait()`, or `.GetAwaiter().GetResult()` in normal application code.
- Accept and propagate `CancellationToken` through cancellable operations.
- Do not swallow `OperationCanceledException` as an ordinary failure.
- Background services must stop gracefully.

### Dependency injection

- Use constructor injection for required dependencies.
- Avoid service locator patterns.
- Do not resolve scoped services from the root provider.
- Do not create hidden static service state.
- Validate service registration and lifetimes.
- Do not introduce interfaces solely to satisfy fashion or mocking habits.

### Error handling

- Do not use empty catch blocks.
- Do not hide failures.
- Do not expose secrets or internal stack traces to clients.
- Use centralized exception handling for application boundaries.
- Preserve useful exception context.
- Do not catch exceptions that cannot be handled meaningfully.
- Do not use exceptions for normal control flow.
- Do not log and rethrow the same exception at every layer.

### Structured output and logging

- Use structured logging with named properties.
- Do not construct logs with string concatenation.
- Avoid high-cardinality and sensitive telemetry dimensions.
- Use appropriate log levels.
- Include correlation context where applicable.
- Return typed results or documented response contracts.
- Do not return persistence entities directly from public APIs unless explicitly justified.

### Security

The following are prohibited by default:

- Disabling TLS or certificate validation
- Accepting all certificates
- Dynamic code execution from untrusted input
- Unsafe deserialization
- SQL construction through string concatenation
- Arbitrary file-system access from user input
- Authorizing only in the user interface
- Logging tokens, passwords, cookies, or authorization headers
- Open CORS policies with credentials
- Storing secrets in source control
- Using obsolete cryptographic algorithms
- Disabling analyzer or vulnerability findings broadly

Any exception requires explicit authorization, documented risk, mitigation, tests, and a review condition.

### Data access

- Parameterize queries.
- Use cancellation tokens.
- Avoid unbounded reads.
- Use projections for read models.
- Use transactions when atomicity is required.
- Handle concurrency deliberately.
- Review migrations before application.
- Never auto-apply destructive production migrations from ordinary application startup unless explicitly approved.
- Do not expose database entities as external contracts by default.

### Testing and validation

- Build with warnings treated according to repository policy.
- Run formatting verification.
- Run analyzers.
- Add or update tests for meaningful behavior.
- Add regression tests for bug fixes where practical.
- Test failure paths and authorization boundaries.
- Do not weaken tests to obtain a passing result.
- Do not connect unit tests to production systems.
- Report anything not run.

### Honest reporting

Do not claim:

- Fully tested
- Production ready
- Secure
- Compliant
- Cross-platform
- High performance
- Backward compatible
- Issue resolved

unless available evidence supports the claim.

## Required Agent Workflow

For non-trivial work:

1. Read applicable instruction and repository files.
2. Inspect the solution, projects, package references, analyzers, tests, and build configuration.
3. Identify target framework, SDK policy, operating systems, deployment model, and external dependencies.
4. Define requested scope and public contracts.
5. Assess operational, security, data, and migration risk.
6. Inspect callers, tests, configuration, schemas, telemetry, and documentation.
7. Choose the smallest coherent implementation.
8. Implement boundary validation before business behavior.
9. Preserve async, cancellation, dependency-injection, and disposal semantics.
10. Add or update tests alongside the change.
11. Run restore, format verification, build, tests, and dependency audit.
12. Review database migrations and generated artifacts.
13. Review the full diff for unrelated changes, secrets, placeholders, and contract changes.
14. Update documentation.
15. Report completion evidence and limitations.

## Required Coding Practices

At minimum:

- Enable nullable reference types.
- Enable implicit usings only when repository conventions support them.
- Use file-scoped namespaces unless repository conventions differ.
- Use clear names and standard .NET naming conventions.
- Prefer immutable data where practical.
- Keep methods focused.
- Validate constructor arguments and public boundaries.
- Use `ArgumentNullException.ThrowIfNull()` where appropriate.
- Use `ConfigureAwait(false)` only in libraries where context independence is intentional and repository policy requires it.
- Dispose `IDisposable` and `IAsyncDisposable` correctly.
- Use `TimeProvider` for testable time-sensitive code.
- Use options validation for configuration.
- Use typed `HttpClient` or named clients through `IHttpClientFactory`.
- Use `ProblemDetails` for HTTP API errors.
- Use invariant culture for machine-readable data.
- Avoid reflection and dynamic dispatch unless justified.
- Avoid premature abstractions and speculative interfaces.
- Avoid hidden global state.
- Avoid returning `null` collections.
- Avoid magic strings and magic numbers when they represent domain or configuration concepts.
- Do not use `async void` except for required event-handler signatures.
- Do not use fire-and-forget tasks without owned lifetime, exception handling, and shutdown behavior.

## Default Validation Commands

Use repository-provided commands when available. Otherwise run appropriate equivalents:

```bash
dotnet --info
dotnet restore
dotnet format --verify-no-changes
dotnet build --no-restore
dotnet test --no-build
dotnet package list --vulnerable --include-transitive
```

For release-sensitive applications, also consider:

```bash
dotnet publish --configuration Release --no-restore
```

Do not claim a command ran when the required SDK, workload, service, or dependency was unavailable.

## Definition of Done

Work is complete only when:

- The requested behavior is implemented.
- Public contracts are preserved or intentionally changed.
- Security and authorization requirements are satisfied.
- Async and cancellation behavior is correct.
- Documentation is current.
- Tests are added or updated where applicable.
- Restore succeeds.
- Formatting verification succeeds.
- Build succeeds.
- Applicable tests pass.
- Dependency vulnerability results are reviewed.
- Database migrations are reviewed where applicable.
- The final diff is reviewed.
- Remaining limitations and risks are documented.

The completion response must follow `standards/COMPLETION_EVIDENCE.md`.
