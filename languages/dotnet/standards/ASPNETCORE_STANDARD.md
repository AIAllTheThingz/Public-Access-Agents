# ASP.NET Core Standard

## Purpose

This standard governs ASP.NET Core APIs, web applications, middleware, controllers, minimal APIs, authentication, authorization, and hosting.

## Application Model

Choose controllers or minimal APIs based on project needs and existing conventions.

Do not mix styles randomly.

Use controllers when:

- Filters and conventions matter
- API surface is large
- Established controller organization exists

Use minimal APIs when:

- Endpoint surface is focused
- Direct route composition improves clarity
- The repository already uses them coherently

Neither style is inherently more mature, scalable, or morally superior.

## Startup and Composition

Keep startup understandable.

- Register services in cohesive groups.
- Validate options.
- Configure middleware in deliberate order.
- Avoid substantial business logic in `Program.cs`.
- Do not hide all registration inside opaque extension methods.
- Fail startup when required configuration is invalid.

## Routing

- Use consistent route naming.
- Use correct HTTP methods.
- Avoid action verbs in resource routes unless modeling commands.
- Validate route constraints.
- Preserve established routes.
- Document breaking changes.
- Avoid ambiguous route matches.

## Request Models

Use explicit request DTOs.

Do not bind public APIs directly to persistence entities.

Validate:

- Required fields
- Length
- Range
- Allowed values
- Cross-field rules
- Resource ownership
- File size and type

Do not rely solely on client validation.

## Response Models

Use explicit response DTOs.

Return appropriate status codes.

Do not leak:

- Internal entities
- Secrets
- Stack traces
- Internal database keys when not part of the contract
- Implementation-specific exceptions

Use stable JSON contracts.

## Problem Details

Use RFC-style Problem Details for API errors.

Include safe fields such as:

- Type
- Title
- Status
- Detail when safe
- Instance
- Trace or correlation identifier

Do not expose internal stack traces or secrets.

Centralize exception mapping.

## Model Validation

Use platform validation, endpoint filters, or application validators consistently.

Return clear validation errors.

Avoid duplicate validation scattered across layers.

Domain invariants must remain protected even when validation exists at the HTTP boundary.

## Authentication and Authorization

- Configure authentication explicitly.
- Require authorization by default where appropriate.
- Use policies.
- Apply resource-based authorization for ownership.
- Test unauthorized and forbidden behavior.
- Do not rely on UI restrictions.
- Do not trust client-supplied role or tenant data.

## Middleware Order

Review middleware order carefully.

Common concerns include:

- Forwarded headers
- Exception handling
- HSTS
- HTTPS redirection
- Static files
- Routing
- CORS
- Authentication
- Authorization
- Rate limiting
- Endpoints

Do not copy a middleware order without understanding the deployment proxy and authentication model.

## Forwarded Headers and Proxies

Trust forwarded headers only from known proxies or networks.

Incorrect configuration can affect:

- Scheme
- Client IP
- Host
- Redirects
- Authentication callbacks
- Security logs

Document proxy assumptions.

## CORS

- Use explicit origins.
- Limit methods and headers.
- Do not combine wildcard origin with credentials.
- Do not treat CORS as authentication or authorization.
- Keep development policies separate from production.

## Rate Limiting

Apply rate limiting where abuse, expensive work, or fairness requires it.

Define:

- Partition key
- Limit
- Window or algorithm
- Queue behavior
- Rejection status
- Retry guidance
- Exemptions
- Telemetry

Avoid unbounded queues.

## Request Cancellation

Propagate `HttpContext.RequestAborted`.

Do not continue expensive work after client cancellation unless the operation is deliberately detached and durably owned elsewhere.

## File Uploads

- Set size limits.
- Validate content.
- Generate storage names.
- Avoid executable web roots.
- Prevent traversal.
- Scan when required.
- Stream large files.
- Do not buffer unbounded content.
- Clean up failures.

## OpenAPI

Keep OpenAPI aligned with runtime behavior.

Document:

- Authentication
- Request and response schemas
- Status codes
- Problem Details
- Deprecation
- Versioning

Do not expose development-only endpoints unintentionally.

## API Versioning

Add versioning only when independently deployed consumers require compatibility.

Define:

- Version location
- Support duration
- Deprecation
- Migration
- Default behavior

Do not version preemptively without a consumer need.

## Health Checks

Separate meanings:

- Liveness: process is alive
- Readiness: instance can serve traffic
- Dependency health: operational insight

Do not make liveness depend on every external service.

Protect detailed health output.

## Background Work

Do not start untracked fire-and-forget work from request handlers.

Use:

- Durable queues
- Hosted services
- External schedulers
- Explicit background-job systems

when work must survive request completion or process restart.

## Static Files and Browser Security

Where applicable configure:

- Content security policy
- Secure cookies
- HSTS
- MIME handling
- Cache control
- Antiforgery
- Clickjacking protection
- Referrer policy

Avoid inline script exceptions that weaken CSP without review.

## Hosting and Shutdown

- Respect cancellation.
- Stop accepting work during shutdown.
- Drain owned queues within limits.
- Dispose resources.
- Define termination grace periods.
- Avoid long synchronous shutdown work.

## Testing

Test:

- Routing
- Validation
- Authentication
- Authorization
- Problem Details
- Middleware behavior
- CORS where relevant
- Rate limiting
- Request cancellation
- File limits
- Health endpoints

## Guiding Rule

> HTTP boundaries must validate, authorize, and translate behavior without leaking internal implementation or weakening domain invariants.
