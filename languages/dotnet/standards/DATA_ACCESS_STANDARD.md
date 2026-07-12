# .NET Data Access Standard

## Purpose

This standard governs Entity Framework Core, Dapper, ADO.NET, SQL, migrations, transactions, and persistence boundaries.

## General Principles

- Choose data access based on requirements.
- Parameterize all values.
- Keep external contracts separate from persistence entities.
- Bound reads.
- Use cancellation.
- Define transaction and concurrency behavior.
- Review generated queries.
- Treat migrations as production changes.
- Protect sensitive data.

## Entity Framework Core

Use EF Core when its unit-of-work, mapping, change tracking, and query capabilities fit the application.

Do not wrap EF Core automatically in generic repository and unit-of-work abstractions. `DbContext` already represents those patterns.

Add abstractions only when they create a meaningful application boundary.

## DbContext Lifetime

- Register `DbContext` with a scoped lifetime for request-based applications.
- Do not share a context across threads.
- Do not store it in singletons.
- Use `IDbContextFactory<TContext>` for appropriate background or multi-unit workflows.
- Keep context lifetime short.
- Dispose contexts owned directly by the caller.

## Queries

For read operations:

- Use projections.
- Use `AsNoTracking()` when tracking is unnecessary.
- Select only needed columns.
- Apply pagination.
- Avoid unbounded `ToListAsync()`.
- Avoid N+1 queries.
- Review includes.
- Pass cancellation tokens.
- Understand query translation.
- Avoid client evaluation of large data.

Do not return `IQueryable<T>` across architectural boundaries unless intentionally exposing query composition.

## Commands

For writes:

- Validate invariants.
- Define transaction boundaries.
- Handle concurrency.
- Save once per coherent unit where practical.
- Verify critical outcomes.
- Avoid loading entire graphs for small updates.
- Use bulk operations only with clear semantics and tests.

## Raw SQL

Use raw SQL only when needed.

Requirements:

- Parameterize values.
- Allowlist identifiers that cannot be parameters.
- Review injection risk.
- Test against the actual provider.
- Document why LINQ is insufficient.
- Avoid string interpolation into SQL.
- Preserve transactions and cancellation.

## Dapper and ADO.NET

- Parameterize commands.
- Open connections late and close early.
- Dispose connections, commands, and readers.
- Use async methods.
- Propagate cancellation.
- Define transaction ownership.
- Map nullability explicitly.
- Avoid dynamic results for stable contracts.

## Transactions

Use transactions when atomicity is required.

Document:

- Scope
- Isolation
- Retry interaction
- External side effects
- Rollback behavior
- Timeout

Do not hold transactions across slow remote calls.

Do not retry a transaction blindly when external effects may have occurred.

## Concurrency

Use optimistic concurrency when appropriate.

Handle concurrency conflicts explicitly.

Do not overwrite changes silently.

Return a meaningful conflict outcome to application or HTTP boundaries.

Test concurrent update behavior.

## Migrations

Migrations must be:

- Reviewed
- Named meaningfully
- Tested on representative data
- Backward-compatible during rolling deployments when required
- Separated into expand and contract phases for risky schema changes
- Included in deployment planning
- Reversible where practical

Do not auto-apply destructive production migrations during ordinary application startup unless explicitly approved.

Review generated SQL for destructive or locking behavior.

## Schema Changes

Consider:

- Table size
- Lock duration
- Default constraints
- Nullability transition
- Backfill
- Index creation
- Deployment ordering
- Application compatibility
- Rollback

A migration compiling is not proof that it is operationally safe.

## Indexes and Performance

Add indexes based on query patterns.

Review:

- Selectivity
- Write cost
- Storage
- Included columns
- Duplicate indexes
- Provider behavior

Use query plans or measurements for performance claims.

## Connection Resiliency

Configure retries only for transient failures.

Account for transaction replay.

Do not retry:

- Authentication failures
- Invalid SQL
- Constraint violations
- Permanent configuration errors

Avoid retry storms.

## Sensitive Data

- Encrypt transport.
- Protect connection strings.
- Avoid logging parameters containing sensitive data.
- Disable sensitive-data logging outside controlled development.
- Apply least-privileged database permissions.
- Classify sensitive columns.
- Avoid returning unnecessary personal data.

## Multi-Tenancy

Enforce tenant boundaries in:

- Authorization
- Queries
- Unique constraints
- Cache keys
- Migrations
- Background processing

Do not rely on client-provided tenant identifiers alone.

Test cross-tenant denial.

## Testing

Use actual provider behavior when it matters.

Test:

- Mappings
- Constraints
- Transactions
- Concurrency
- Query translation
- Migration application
- Pagination
- Tenant boundaries
- Failure rollback

Do not use EF InMemory as proof of relational behavior.

## Completion Evidence

Report:

- Schema changes
- Migration names
- Generated SQL review
- Data backfill
- Transaction behavior
- Concurrency behavior
- Provider tested
- Rollback limitations
- Production application method

## Guiding Rule

> Data changes must preserve integrity, security, compatibility, and operational safety, not merely satisfy the object model.
