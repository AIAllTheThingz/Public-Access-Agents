# .NET Testing Standard

## Purpose

This standard defines testing requirements for modern .NET applications.

Tests must provide evidence of required behavior, safe failure, authorization, compatibility, and public-contract stability.

A passing build is not a test strategy. It is merely proof that the compiler tolerated the current arrangement.

## Test Layers

Use the smallest test layer that proves the behavior:

- Unit tests
- Integration tests
- Functional or API tests
- Contract tests
- Architecture tests
- End-to-end tests
- Performance tests

Do not force every behavior through end-to-end tests.

Do not mock everything by reflex.

## Unit Tests

Unit tests should:

- Test a focused behavior
- Run quickly
- Be deterministic
- Avoid production dependencies
- Avoid network and real external services
- Verify success and failure
- Verify cancellation where relevant
- Verify edge cases and invariants

Test public outcomes, not implementation details.

## Integration Tests

Integration tests may verify:

- Database mappings
- Real serialization
- File-system behavior
- HTTP clients against controlled servers
- Service registration
- Message serialization
- Cache integration
- Authentication integration
- External adapters in controlled environments

Use isolated resources and cleanup.

Do not target production.

## ASP.NET Core Functional Tests

Use `WebApplicationFactory<TEntryPoint>` or an equivalent controlled host where appropriate.

Test:

- Routing
- Model binding
- Validation
- Authentication
- Authorization
- Status codes
- Problem Details
- Content types
- Headers
- Cancellation
- CORS where relevant
- Rate limiting
- Dependency registration

Do not rely only on controller unit tests for application-boundary behavior.

## Database Tests

Test:

- Mappings
- Constraints
- Transactions
- Concurrency
- Query translation
- Migrations
- Provider-specific behavior
- Index-sensitive queries when important

Do not use EF Core InMemory as proof of relational database behavior.

Prefer SQLite or the actual database engine in an isolated test environment when relational behavior matters.

## Test Naming

Use descriptive names that express:

- Scenario
- Action
- Expected result

Examples:

```text
CreateAsync_WhenNameIsEmpty_ReturnsValidationFailure
GetByIdAsync_WhenRecordDoesNotExist_ReturnsNull
Delete_WhenUserLacksPermission_ReturnsForbidden
```

Repository conventions may use other readable patterns.

Avoid `Test1`, `Works`, or names that only repeat the method name.

## Arrange, Act, Assert

Keep tests readable.

Use helpers and builders when they reduce noise without hiding the scenario.

Avoid large shared fixtures that make tests depend on invisible state.

## Isolation

Tests must not depend on:

- Execution order
- Developer machine state
- User profile
- Current time without `TimeProvider`
- Production data
- Production credentials
- Shared mutable static state
- Uncontrolled environment variables
- External network access unless explicitly integration-tested

Use unique test identifiers and isolated resources.

## Test Data

Use fictitious deterministic data.

Do not copy production data unless sanitized and approved.

Test:

- Boundaries
- Nullability
- Empty values
- Maximum sizes
- Unicode
- Invalid formats
- Duplicate values
- Concurrency conflicts
- Malicious input where relevant

## Mocks and Fakes

Mock external behavior, not internal details.

Use fakes when stateful behavior matters.

Do not introduce interfaces solely because a mocking framework prefers them.

Do not mock:

- Simple value objects
- The system under test
- EF query behavior when translation is what matters
- Framework behavior better tested through a functional host

Verify interactions only when the interaction is part of the contract.

## Async Tests

Async tests must return `Task`.

Do not block.

Test:

- Successful completion
- Cancellation
- Timeout
- Concurrency
- Exception propagation
- Partial completion
- Graceful shutdown for workers

Avoid arbitrary `Task.Delay` for synchronization.

Use controllable clocks, channels, signals, or test hooks.

## Cancellation Tests

Verify that:

- Caller tokens propagate
- Canceled work stops
- Expected cancellation is not logged as an error
- Resources are disposed
- Transactions do not commit incorrectly
- Background services stop within expected limits

## Security Tests

Test applicable boundaries:

- Authentication required
- Authorization policy enforced
- Cross-user or cross-tenant access denied
- Input validation
- SQL injection resistance through parameterization
- Path traversal rejection
- File-upload restrictions
- Secret redaction
- CORS policy
- CSRF protection where relevant
- Rate limiting
- Unsafe deserialization rejection
- Security headers where required

Client-side restrictions are not authorization tests.

## Error Tests

Verify:

- Correct exception or result
- Appropriate HTTP status
- Problem Details shape
- No secret leakage
- No internal stack trace leakage
- No false success
- Transaction rollback
- Idempotent retry behavior
- Logging occurs at the proper boundary

## Public Contract Tests

Protect:

- Routes
- HTTP methods
- Request and response schemas
- Status codes
- JSON names and enum formats
- Message schemas
- Configuration keys
- Public library members
- Exit codes

Use snapshots sparingly and review changes carefully.

## Regression Tests

Bug fixes should include a test that fails before the fix and passes after it when practical.

The test should reproduce the defect without production dependencies.

## Architecture Tests

Use architecture tests only for meaningful constraints such as:

- Forbidden dependency direction
- Domain independence from infrastructure
- Public API conventions
- Namespace boundaries
- Prohibited references

Do not create architecture tests for arbitrary folder aesthetics.

## Performance Tests

Performance claims require measurement.

Define:

- Workload
- Environment
- Dataset
- Warmup
- Iterations
- Baseline
- Success threshold

Do not run unstable benchmarks as ordinary unit tests.

Use BenchmarkDotNet or appropriate load tooling where justified.

## Coverage

Coverage is evidence, not a vanity target.

Prioritize:

- Security boundaries
- Domain invariants
- Error paths
- Authorization
- Data integrity
- Public contracts
- Bug regressions

Do not add meaningless assertions to inflate a percentage.

## Test Categories and Traits

Use traits or categories when they improve selective execution:

- Unit
- Integration
- Functional
- EndToEnd
- Database
- RequiresContainer
- RequiresExternalService
- Slow

Default CI should remain deterministic.

## Required Validation

Use repository commands when available.

Typical sequence:

```bash
dotnet restore
dotnet format --verify-no-changes
dotnet build --no-restore
dotnet test --no-build
```

For coverage when configured:

```bash
dotnet test --no-build --collect:"XPlat Code Coverage"
```

## Failure Analysis

Classify failures as:

- Introduced by current change
- Pre-existing
- Environmental
- Dependency-related
- Platform-related
- Flaky
- Test defect
- External-service unavailable

Fix failures introduced by the change.

Do not delete or weaken tests merely to obtain green output.

## Skipped Tests

Every skipped test requires a reason.

Do not skip because implementation is inconvenient.

Report skipped and not-run tests separately.

## Completion Evidence

Report:

- Test commands
- Passed
- Failed
- Skipped
- Not run
- Coverage when collected
- Test SDK and framework
- External dependencies
- Environmental limitations

Follow `COMPLETION_EVIDENCE.md`.

## Guiding Rule

> Tests must prove behavior and safe failure, not merely decorate the repository with green icons.
