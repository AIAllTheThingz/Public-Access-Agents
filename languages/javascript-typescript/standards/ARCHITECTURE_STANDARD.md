# JavaScript and TypeScript Architecture Standard

## Purpose

This standard governs architecture for Node.js, browser, library, and full-stack
JavaScript and TypeScript projects.

Architecture must support actual requirements rather than accumulate fashionable
layers and packages.

## Core Principles

- Start simple.
- Keep dependencies explicit.
- Separate responsibilities at meaningful boundaries.
- Preserve public contracts.
- Prefer cohesive modules over excessive fragmentation.
- Design for testability without designing only for mocks.
- Avoid hidden global state.
- Record consequential decisions.
- Avoid speculative extensibility.

## Requirement-Driven Architecture

Before introducing a pattern, determine:

- Runtime and deployment model
- Browser versus server trust boundary
- Expected scale
- Availability needs
- Data consistency
- Security boundary
- Integration points
- Team ownership
- Package-publication needs
- Failure modes
- Upgrade cadence

Do not automatically impose:

- Microservices
- Monorepos
- Event sourcing
- CQRS
- Message buses
- Repository patterns
- Dependency-injection frameworks
- State-management libraries
- Schema libraries
- Framework migrations
- Universal server rendering
- Plugin systems

Use them only when they solve concrete requirements.

## Package and Module Boundaries

Create packages when they represent meaningful boundaries:

- Independently published libraries
- Independently deployed applications
- Shared contracts with clear ownership
- Platform-specific implementations
- Tooling packages
- Test utilities with broad reuse

Do not create a package for every folder or service.

Avoid circular dependencies.

Use package exports to define the supported surface.

## Front-End and Back-End Boundaries

Do not share privileged server code into browser bundles.

Separate:

- Public shared schemas
- Server-only implementation
- Browser-only implementation
- Environment-specific configuration

Audit bundler output for accidental secrets and server dependencies.

## Domain and Application Logic

Keep business rules independent from transport and framework details where that
improves testability and reuse.

Do not add domain layers for trivial CRUD without meaningful behavior.

Keep invariants close to the operations they govern.

## Infrastructure

Infrastructure modules may contain:

- Databases
- Filesystem
- HTTP clients
- Messaging
- Browser storage
- Email
- Caching
- Cloud SDKs
- Native processes

Wrap infrastructure when it creates a meaningful boundary, not merely because a
library exists.

## Configuration Boundary

Read and validate environment-specific configuration in one clear boundary.

Pass typed, validated configuration into application modules.

Do not read `process.env` throughout business logic.

Do not allow browser bundles to receive server secrets.

## Dependency Injection

Constructor or parameter injection is usually sufficient.

Do not introduce a DI container unless lifecycle, composition scale, or framework
requirements justify it.

Avoid service locators.

Keep composition roots understandable.

## Background Work

Define:

- Ownership
- Durability
- Retry
- Idempotency
- Concurrency
- Shutdown
- Poison-work handling
- Observability
- Deployment behavior

Do not start untracked promises from request handlers.

Use durable queues when work must survive process restart.

## Messaging

Define:

- Delivery semantics
- Ordering
- Idempotency
- Schema versioning
- Retry
- Dead-letter behavior
- Authentication
- Correlation
- Observability

Do not assume exactly-once delivery.

## Caching

Introduce caching only with defined:

- Purpose
- Key
- Scope
- Expiration
- Invalidation
- Consistency tolerance
- Security boundary
- Failure behavior
- Observability

Do not cache sensitive data carelessly.

## Resilience

Define:

- Timeout
- Abort
- Retry
- Backoff
- Jitter
- Circuit breaking
- Concurrency limits
- Fallback
- Idempotency

Do not retry permanent failures or unsafe mutations without protection.

## Monorepos

Use a monorepo only when shared change coordination and ownership justify it.

Define:

- Workspace boundaries
- Dependency constraints
- Build graph
- Versioning
- Release model
- CI scope
- Cache behavior
- Ownership

Do not allow arbitrary cross-package imports.

## Architecture Decisions

Create an ADR for consequential choices such as:

- Runtime or framework
- Package manager
- Module format
- Monorepo adoption
- Persistence strategy
- Authentication model
- Public package contract
- Messaging
- Deployment topology
- Major compatibility break

Do not create ADRs for trivial formatting choices.

## Guiding Rule

> Use the least architecture that safely supports the actual runtime, deployment, security, and ownership requirements.
