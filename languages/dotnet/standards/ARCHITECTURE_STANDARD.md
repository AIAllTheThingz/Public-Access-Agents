# .NET Architecture Standard

## Purpose

This standard governs architectural decisions for project-agnostic .NET development.

Architecture must support the actual requirements. It must not become a collection of fashionable layers created before the problem is understood.

## Core Principles

- Start simple.
- Separate responsibilities at meaningful boundaries.
- Keep dependencies explicit.
- Keep business rules independent of infrastructure where that provides real value.
- Prefer cohesive projects over excessive project fragmentation.
- Preserve public contracts.
- Design for testability without designing only for mocks.
- Record consequential decisions.
- Avoid speculative extensibility.

## Architecture Is Requirement-Driven

Before introducing architecture patterns, determine:

- Application type
- Deployment model
- Expected scale
- Availability needs
- Security boundary
- Data consistency needs
- Integration points
- Team ownership
- Operational model
- Upgrade cadence
- Failure modes

Do not automatically impose:

- Clean Architecture
- Onion Architecture
- Hexagonal Architecture
- CQRS
- Event sourcing
- Mediator libraries
- Repository and unit-of-work wrappers
- Microservices
- Message buses
- Domain-driven design tactical patterns

Use them only when their benefits address concrete requirements.

## Solution and Project Boundaries

Create separate projects when they represent meaningful boundaries such as:

- Independently deployable applications
- Reusable libraries
- Test assemblies
- Platform-specific implementations
- Source generators or analyzers
- Clearly isolated infrastructure adapters

Do not create separate projects for every folder, interface, or service.

Each project must have a clear purpose and dependency direction.

Avoid circular references.

## Dependency Direction

Higher-level policy should not depend directly on lower-level infrastructure when isolation provides real value.

Possible boundaries include:

- Domain
- Application
- Infrastructure
- Presentation
- Worker
- Tests

These are examples, not mandatory project names.

Keep framework and persistence details from leaking into business rules when doing so improves maintainability and testing.

Do not introduce abstractions when direct framework use is simpler and the dependency is not harmful.

## Public Contracts

Define explicit contracts for:

- HTTP APIs
- Messages
- Events
- Configuration
- Persistence migrations
- Public libraries
- File formats
- Reports

Do not expose internal entities accidentally.

Version contracts when consumers require independent evolution.

Breaking changes require migration guidance.

## Domain Modeling

Use domain types when they prevent invalid states or clarify behavior.

Avoid:

- Primitive obsession where values have important constraints
- Anemic layers containing only pass-through methods
- Domain abstractions for trivial CRUD without behavior
- Extremely elaborate aggregates without transactional need

Keep invariants close to the data and operations they govern.

## Application Services

Application services should coordinate use cases.

They may:

- Validate application-level rules
- Authorize actions
- Coordinate domain behavior
- Manage transactions
- Call ports or infrastructure abstractions
- Return explicit outcomes

They should not:

- Contain HTTP-specific concerns
- Return EF entities as external contracts
- Hide arbitrary service location
- Become giant collections of unrelated methods

## Infrastructure

Infrastructure code may contain:

- Database access
- File-system access
- External APIs
- Messaging
- Email
- Caching
- Identity-provider integrations
- Platform services

Infrastructure failures must be translated only when callers benefit from a more meaningful abstraction.

Do not wrap every framework API mechanically.

## Dependency Injection Composition

Register services at a clear composition root.

Requirements:

- Keep registration understandable.
- Validate options.
- Validate lifetimes.
- Avoid registrations scattered unpredictably across unrelated classes.
- Use extension methods to group cohesive registration, not to hide architecture.
- Avoid runtime service location.

## Background Work

Use `BackgroundService`, hosted services, queues, or external schedulers based on reliability requirements.

Background processing must define:

- Ownership
- Startup behavior
- Graceful shutdown
- Cancellation
- Retry
- Idempotency
- Concurrency
- Persistence
- Poison-message handling
- Observability
- Deployment behavior

Do not start untracked background tasks from HTTP requests.

Use durable infrastructure when work must survive process restarts.

## Messaging and Events

Use messaging only when decoupling, durability, scale, or integration requirements justify it.

Define:

- Delivery semantics
- Ordering
- Idempotency
- Retry
- Dead-letter behavior
- Schema versioning
- Correlation
- Security
- Observability

Do not assume exactly-once delivery.

Do not use in-process mediator libraries as a substitute for architecture.

## Transactions and Consistency

Define transactional boundaries explicitly.

Use:

- Local database transactions when atomicity is required
- Outbox or equivalent patterns when durable cross-boundary publication is required
- Compensation only when true rollback is impossible

Do not introduce distributed transactions casually.

Document eventual consistency when it affects user-visible behavior.

## Caching

Introduce caching only with defined:

- Purpose
- Key design
- Scope
- Expiration
- Invalidation
- Consistency tolerance
- Failure behavior
- Security boundary
- Observability

Do not cache sensitive data without protection.

Do not use caching to conceal inefficient or incorrect data access without understanding invalidation.

## Resilience

Resilience behavior must match operation semantics.

Define:

- Timeout
- Retry
- Circuit breaking
- Bulkhead or concurrency limit
- Fallback
- Idempotency
- Cancellation

Do not retry:

- Validation failures
- Authorization failures
- Non-idempotent operations without protection
- Permanent configuration errors

Avoid retry storms.

## Scalability

Design based on evidence and expected load.

Prefer stateless application instances when appropriate.

Identify state that must be externalized.

Bound queues and concurrency.

Avoid in-memory coordination when multiple instances must agree.

Do not claim scalability without load or architecture evidence.

## Deployment Architecture

Document:

- Deployment unit
- Required runtime
- Ports
- Health checks
- Configuration
- Secrets
- Persistent storage
- Database migration process
- Graceful shutdown
- Rollback
- Observability
- Platform assumptions

Application code should not assume one deployment platform unless explicitly scoped.

## Architecture Decision Records

Create an ADR for consequential decisions such as:

- Major framework selection
- Persistence strategy
- Messaging platform
- Authentication model
- Public versioning policy
- Deployment topology
- Significant compatibility break
- Major dependency introduction

An ADR should include:

- Context
- Decision
- Alternatives
- Consequences
- Status

Do not create ADRs for trivial implementation details.

## Refactoring

Architectural refactoring must:

- Be explicitly in scope
- Preserve behavior unless changed intentionally
- Include tests
- Minimize simultaneous unrelated changes
- Document migration
- Avoid mixing dependency upgrades and major redesign without need

## Guiding Rule

> Use the least architecture that safely supports the actual requirements, while preserving a clear path for justified evolution.
