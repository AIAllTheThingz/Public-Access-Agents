# JavaScript and TypeScript Agent Standard

## Purpose

This file defines the mandatory operating rules for coding agents that create,
modify, review, test, secure, or document JavaScript and TypeScript software.

The standard is project-agnostic. It governs how work is performed, not the
business purpose of any individual application.

The primary objective is:

> Make the smallest safe, maintainable, testable, observable, and well-documented change that satisfies the stated requirement.

## Scope

These instructions apply to:

- Node.js applications and services
- TypeScript projects
- JavaScript projects
- Browser applications
- Front-end applications
- API clients and servers
- Worker processes and background jobs
- Libraries and packages
- Build and bundling configuration
- Tests
- Package dependencies
- Configuration and environment examples
- Documentation
- Observability
- Security-sensitive integrations

## Required Runtime Baseline

New server-side development must use the current Node.js LTS baseline:

- Node.js major version: 24
- Module system: ECMAScript modules by default
- TypeScript baseline: 6.0 for TypeScript projects
- ECMAScript target: ES2025 where supported by the deployment runtime
- Reference package manager: pnpm 11
- Lint configuration: ESLint flat configuration
- Preview, nightly, experimental, or release-candidate tooling is prohibited unless explicitly requested.

Existing repositories must preserve their declared runtime and module-system
contracts unless migration is explicitly in scope.

Do not add CommonJS compatibility, legacy-browser support, or older Node.js
support unless explicitly required.

## Instruction Priority

When instructions conflict, apply them in this order:

1. Explicit user requirements
2. More specific nested `AGENTS.md` instructions
3. This root `AGENTS.md`
4. Repository documentation and established conventions
5. General coding-agent preferences

Do not silently resolve a material conflict. Follow the higher-priority
instruction and report the conflict in completion evidence.

## Required Supporting Standards

Before creating or modifying relevant code, read and follow:

- `standards/JAVASCRIPT_TYPESCRIPT_CODING_STANDARD.md`
- `standards/TYPESCRIPT_STANDARD.md`
- `standards/NODEJS_STANDARD.md`
- `standards/WEB_FRONTEND_STANDARD.md`
- `standards/ARCHITECTURE_STANDARD.md`
- `standards/DOCUMENTATION_STANDARD.md`
- `standards/TESTING_STANDARD.md`
- `standards/SECURITY_STANDARD.md`
- `standards/DEPENDENCY_MANAGEMENT_STANDARD.md`
- `standards/OBSERVABILITY_STANDARD.md`
- `standards/COMPLETION_EVIDENCE.md`

These files are mandatory extensions of this `AGENTS.md`.

If a supporting standard conflicts with this file, this file takes precedence.

## Non-Negotiable Rules

### Safe behavior

- Default to the safest practical behavior.
- Validate input, configuration, authorization, and dependencies before mutation.
- Stop when prerequisites are missing or target identity is ambiguous.
- Do not weaken security controls to make code succeed.
- Do not perform destructive or irreversible work without explicit authorization.
- Preserve cancellation, timeout, cleanup, and graceful-shutdown paths.
- Bound concurrency, queues, payload size, and retries.

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
- Cloud resource identifiers
- File-system paths
- Credentials
- Secret names
- Deployment assumptions

Use obvious placeholders, validated configuration, or documented inputs.

### Secrets and sensitive data

Never place credentials or sensitive values in:

- Source code
- Tests
- Documentation examples
- Logs
- Metrics
- Traces
- Reports
- Exceptions
- Committed environment files
- URLs or command-line examples when safer methods exist

Use approved secret-management mechanisms. Redact before logging or serialization.

### Input validation

Treat all external input as untrusted, including:

- HTTP requests
- Message payloads
- Environment variables
- Configuration files
- Database values
- File names and paths
- Uploaded files
- Browser storage
- URL parameters
- Headers and cookies
- Remote-service responses
- Native-command output

Validate type, length, range, format, allowed values, authorization, and
operational safety at the boundary.

### Public contracts

Treat public behavior as a contract, including:

- Exported functions, classes, and types
- Package exports
- HTTP routes and methods
- Request and response schemas
- Status codes
- Configuration keys
- Message and event schemas
- File formats
- Browser storage keys
- Telemetry names
- Exit codes

Breaking changes require explicit authorization, migration guidance, tests, and
documentation.

### Type safety

For TypeScript:

- Enable strict type checking.
- Do not use `any` as a routine escape hatch.
- Do not use unsafe type assertions to silence errors.
- Narrow `unknown` before use.
- Model absence explicitly.
- Keep runtime validation at trust boundaries.
- Do not confuse compile-time types with runtime validation.

For JavaScript:

- Use clear module boundaries.
- Use JSDoc types when they materially improve maintainability.
- Validate external data at runtime.
- Do not rely on implicit coercion for security-sensitive behavior.

### Async and cancellation

- Use promises and `async`/`await` consistently.
- Do not create unhandled promises.
- Do not use `async` callbacks with APIs that do not await them without deliberate handling.
- Propagate `AbortSignal` through cancellable I/O.
- Apply timeouts to external operations.
- Do not swallow aborts as ordinary failures.
- Do not start unowned fire-and-forget work.
- Background services must stop gracefully.

### Modules

- Use ECMAScript modules for new projects.
- Use explicit package exports.
- Do not mix ESM and CommonJS casually.
- Include file extensions in Node.js ESM relative imports when required.
- Avoid deep imports into package internals.
- Avoid module side effects.
- Do not execute substantial operational work during module import.

### Error handling

- Do not use empty catch blocks.
- Do not hide failures.
- Preserve useful error context.
- Do not expose secrets or internal stack traces to clients.
- Do not use exceptions for ordinary expected branching when an explicit result is clearer.
- Do not log and rethrow the same error at every layer.
- Use `Error` objects, not string throws.

### Logging and output

- Use structured logging.
- Do not build production logs through string concatenation.
- Avoid sensitive and high-cardinality fields.
- Use appropriate levels.
- Propagate correlation where applicable.
- Keep library output separate from console presentation.
- Do not use `console.log` as an application logging architecture.

### Security

The following are prohibited by default:

- Disabling TLS or certificate validation
- Executing code from untrusted strings
- `eval`
- `new Function` with untrusted input
- Unsafe shell construction
- SQL construction through string concatenation
- Arbitrary path access from user input
- Unsafe HTML injection
- Trusting browser-side authorization
- Logging tokens, passwords, cookies, or authorization headers
- Open CORS with credentials
- Unsafe deserialization
- Prototype-pollution-prone object merging
- Broad dependency-audit suppression
- Shipping source maps publicly without deliberate review

Any exception requires explicit authorization, documented risk, mitigation,
tests, and a review condition.

### Dependency management

- Commit the lockfile.
- Use frozen-lockfile installs in CI.
- Review direct and transitive dependencies.
- Do not run arbitrary dependency lifecycle scripts without review.
- Keep package sources trusted and minimal.
- Pin the package-manager version.
- Avoid floating dependency versions.
- Do not update unrelated packages during a targeted change.
- Run dependency and provenance checks supported by the chosen package manager.

### Testing and validation

- Run formatting verification.
- Run linting.
- Run TypeScript type checking when TypeScript is used.
- Run tests.
- Build or bundle production output where applicable.
- Run dependency audit.
- Add or update tests for meaningful behavior.
- Add regression tests for bug fixes where practical.
- Test failure, authorization, and cancellation paths.
- Do not weaken tests to obtain a passing result.
- Report anything not run.

### Honest reporting

Do not claim:

- Fully tested
- Production ready
- Secure
- Compliant
- Cross-platform
- Browser compatible
- Backward compatible
- High performance
- Issue resolved

unless available evidence supports the claim.

## Required Agent Workflow

For non-trivial work:

1. Read applicable instruction and repository files.
2. Inspect package metadata, lockfiles, runtime declarations, module format, TypeScript configuration, linting, tests, and build tools.
3. Identify Node.js, browser, package-manager, operating-system, and deployment requirements.
4. Define requested scope and public contracts.
5. Assess security, supply-chain, data, browser, and operational risks.
6. Inspect callers, tests, schemas, configuration, telemetry, and documentation.
7. Choose the smallest coherent implementation.
8. Implement runtime validation at trust boundaries.
9. Preserve async, abort, cleanup, module, and resource-lifetime behavior.
10. Add or update tests alongside the change.
11. Install with the locked dependency graph.
12. Run format, lint, typecheck, test, build, and dependency audit.
13. Review generated bundles and source maps where applicable.
14. Review the full diff for unrelated changes, secrets, placeholders, and contract changes.
15. Update documentation.
16. Report completion evidence and limitations.

## Required Coding Practices

At minimum:

- Prefer `const`; use `let` only for reassignment.
- Do not use `var`.
- Use strict equality.
- Avoid implicit coercion in critical logic.
- Use explicit exports.
- Avoid default exports for shared libraries unless repository convention requires them.
- Keep functions focused.
- Prefer immutable data.
- Use pure functions for transformations where practical.
- Validate constructor and public-boundary inputs.
- Use `unknown` for untrusted TypeScript data.
- Return empty collections rather than `null` when absence is not meaningful.
- Use `AbortController` and `AbortSignal` for cancellable operations.
- Use Web Platform APIs where supported and appropriate.
- Use `node:` prefixes for built-in Node.js imports.
- Use `URL` and `URLSearchParams` rather than manual URL concatenation.
- Use path APIs rather than manual separators.
- Avoid hidden global state.
- Avoid monkey patching.
- Avoid prototype mutation.
- Avoid unbounded `Promise.all`.
- Avoid synchronous filesystem and crypto APIs in request-serving paths.
- Avoid date and time logic tied directly to the wall clock when testability matters.
- Use UTF-8.
- Preserve repository formatting and line endings.

## Default Validation Commands

Use repository-provided scripts when available. Otherwise use appropriate
equivalents:

```bash
node --version
pnpm --version
pnpm install --frozen-lockfile
pnpm format:check
pnpm lint
pnpm typecheck
pnpm test
pnpm build
pnpm audit
```

For a published package, also validate:

```bash
pnpm pack --dry-run
```

Do not claim a command ran when the required runtime, browser, service, or
dependency was unavailable.

## Definition of Done

Work is complete only when:

- The requested behavior is implemented.
- Public contracts are preserved or intentionally changed.
- Runtime validation and security controls are present.
- Async, abort, cleanup, and shutdown behavior is correct.
- Documentation is current.
- Tests are added or updated where applicable.
- Locked installation succeeds.
- Formatting verification succeeds.
- Linting succeeds.
- Type checking succeeds where applicable.
- Applicable tests pass.
- Production build succeeds where applicable.
- Dependency-audit results are reviewed.
- Generated output and package contents are reviewed.
- The final diff is reviewed.
- Remaining limitations and risks are documented.

The completion response must follow `standards/COMPLETION_EVIDENCE.md`.
