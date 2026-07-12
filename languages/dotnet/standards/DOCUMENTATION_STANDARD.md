# .NET Documentation Standard

## Purpose

This standard defines documentation requirements for .NET applications, libraries, APIs, configuration, operations, and code.

Documentation must explain behavior, constraints, risks, operation, and maintenance without merely translating syntax into prose.

## Documentation Levels

Documentation may include:

- Repository README
- Architecture documentation
- ADRs
- Public API documentation
- XML documentation comments
- Inline comments
- Configuration reference
- Deployment guide
- Database migration guide
- Operational runbook
- Troubleshooting
- Completion evidence

Do not duplicate all information at every level.

## Repository README

Document, where applicable:

- Purpose
- Application type
- .NET SDK and target framework
- Supported operating systems
- Solution structure
- Build commands
- Test commands
- Run commands
- Configuration
- Secret-management expectations
- Database setup
- Migration process
- Authentication and authorization
- Health checks
- Logging and telemetry
- Deployment and publishing
- Known limitations
- Troubleshooting
- License and contribution guidance

Keep commands current and executable.

## Public API Documentation

Document public libraries and contracts where consumers need guidance.

XML documentation should describe:

- Purpose
- Parameters
- Return value
- Exceptions
- Nullability
- Cancellation
- Side effects
- Thread safety
- Examples when valuable

Do not repeat type names without adding meaning.

Example:

```csharp
/// <summary>
/// Retrieves the current status for a managed resource.
/// </summary>
/// <param name="resourceId">The stable resource identifier.</param>
/// <param name="cancellationToken">
/// Cancels the operation before the remote request completes.
/// </param>
/// <returns>The resource status, or <see langword="null"/> when it does not exist.</returns>
/// <exception cref="ArgumentException">
/// Thrown when <paramref name="resourceId"/> is empty.
/// </exception>
```

## Inline Comments

Comment non-obvious logic, especially:

- Security boundaries
- Authorization decisions
- Retry behavior
- Idempotency
- Concurrency
- Cancellation
- Workarounds
- Compatibility constraints
- Complex algorithms
- Regular expressions
- Serialization behavior
- Database concurrency
- Transaction boundaries
- Cache invalidation
- External-system quirks
- Migration safety
- Performance-sensitive decisions

Comments should explain why and risk, not narrate code.

Bad:

```csharp
// Increment count.
count++;
```

Better:

```csharp
// Count only accepted records so the checkpoint matches the durable batch,
// not the number of messages read from the queue.
acceptedCount++;
```

## Commented-Out Code

Remove obsolete code rather than commenting it out.

Use source control history.

Do not leave:

- Old implementations
- Debug statements
- Disabled authorization
- Disabled validation
- Temporary secrets
- Alternate queries
- Failed experiments

in source files.

## TODO and FIXME

Each TODO or FIXME must include:

- Specific work
- Reason it remains
- Tracking reference when available
- Removal condition

Do not use TODO comments to conceal required incomplete behavior.

## Configuration Documentation

Document:

- Key name
- Type
- Required or optional status
- Default
- Allowed values
- Secret classification
- Source and precedence
- Reload behavior
- Environment-specific considerations
- Validation behavior

Use fictitious examples.

Do not commit live secrets.

## API Documentation

For HTTP APIs, document:

- Route
- Method
- Authentication
- Authorization
- Request schema
- Validation
- Response schema
- Status codes
- Problem Details
- Idempotency
- Rate limits
- Pagination
- Cancellation and timeout
- Versioning
- Breaking-change policy

OpenAPI should reflect actual runtime behavior.

Do not treat generated OpenAPI as a substitute for design review.

## Data Documentation

Document:

- Schema ownership
- Migration process
- Backward compatibility
- Retention
- Sensitive classifications
- Concurrency behavior
- Transaction boundaries
- Recovery and rollback
- Index or performance assumptions when operationally important

## Operational Documentation

Document:

- Start and stop behavior
- Graceful shutdown
- Health endpoints
- Readiness and liveness meaning
- Logs, metrics, and traces
- Alerting expectations
- Background jobs
- Retry and dead-letter behavior
- Maintenance mode
- Backup and restore dependencies
- Deployment rollback
- Database migration sequence

## Security Documentation

Document:

- Authentication scheme
- Authorization model
- Required roles or scopes
- Secret sources
- Data-protection requirements
- Certificate prerequisites
- CORS policy
- File-upload restrictions
- Rate limiting
- Audit behavior
- Known security assumptions

Do not reveal secrets or unnecessarily expose sensitive implementation details.

## Test Documentation

Tests should communicate behavior through descriptive names.

Comment tests only when:

- Setup is non-obvious
- A regression requires context
- A mock represents unusual failure
- Platform-specific behavior is simulated
- A test limitation requires explanation

Do not narrate every assertion.

## Documentation Synchronization

When behavior changes, update all affected documentation in the same change.

Review:

- README
- XML comments
- OpenAPI annotations
- Examples
- Configuration reference
- ADRs
- Migrations
- Runbooks
- Troubleshooting
- Test names
- Release notes

Outdated documentation is a defect.

## Documentation Review

Before completion verify:

- Commands are current.
- Public behavior matches documentation.
- Configuration keys are accurate.
- Examples use safe fictitious values.
- No secrets are present.
- Runtime and platform claims are accurate.
- Error and status behavior is documented.
- Removed behavior is removed from documentation.
- New behavior is documented.
- Links and paths are valid.

## Guiding Rule

> Document enough behavior, intent, risk, and operating context that another qualified developer or administrator can safely maintain and run the system.
