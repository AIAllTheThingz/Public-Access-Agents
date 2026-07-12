# .NET Security Standard

## Purpose

This standard defines security requirements for modern .NET applications.

Security applies to code, configuration, dependencies, data, APIs, deployment examples, logging, telemetry, and tests.

## Core Principles

- Default deny.
- Authenticate and authorize at server-side boundaries.
- Use least privilege.
- Validate untrusted input.
- Preserve TLS and certificate validation.
- Minimize secret exposure.
- Parameterize data access.
- Bound resource consumption.
- Fail safely.
- Record auditable outcomes without sensitive data.
- Keep dependencies supported and reviewed.

## Secrets

Never hardcode or commit:

- Passwords
- Tokens
- API keys
- Private keys
- Client secrets
- Connection strings containing credentials
- Signing keys
- Session secrets
- Certificate private material

Use approved secret stores or deployment injection.

Do not place secrets in logs, metrics, traces, exceptions, URLs, or command-line arguments when safer mechanisms exist.

## Authentication

- Use established platform authentication middleware.
- Validate issuer, audience, signature, lifetime, and intended token type.
- Do not write custom cryptographic token validation without a concrete requirement.
- Do not trust identity headers unless a trusted proxy boundary is configured.
- Protect refresh tokens and session cookies.
- Use secure cookie settings.
- Document clock-skew and revocation assumptions.

## Authorization

- Enforce authorization server-side.
- Prefer policies and resource-based checks.
- Verify tenant and ownership boundaries.
- Avoid role-name checks scattered throughout business code.
- Do not rely on hidden UI controls.
- Deny by default.
- Test forbidden and cross-boundary access.

Authentication alone is not authorization.

## Input Validation

Validate:

- Length
- Range
- Format
- Allowed values
- Resource ownership
- File path boundaries
- URI scheme and host
- Uploaded content
- Pagination
- Sort fields
- Filter expressions
- Deserialized types

Use allowlists where practical.

Validation does not replace output encoding or authorization.

## HTTP and TLS

- Require HTTPS in production.
- Preserve certificate and hostname validation.
- Do not accept all certificates.
- Configure proxy forwarding only for trusted proxies.
- Validate redirect behavior.
- Avoid tokens in query strings.
- Apply appropriate HSTS and secure headers.
- Set request-size limits.
- Set timeouts.
- Bound response sizes from external services.

## CORS

- Configure explicit origins.
- Do not combine wildcard origins with credentials.
- Limit methods and headers.
- Do not treat CORS as authorization.
- Test deployed proxy and origin behavior.

## CSRF

Use CSRF protection for cookie-authenticated state-changing browser requests.

Do not assume JSON automatically eliminates CSRF.

Token-authenticated APIs may use different protections based on how credentials are transported.

## File Uploads

For uploads:

- Enforce size limits.
- Validate extension and content type.
- Inspect file signatures where relevant.
- Generate server-side storage names.
- Store outside executable web roots.
- Prevent traversal.
- Scan when required.
- Avoid trusting client file names.
- Restrict permissions.
- Do not execute uploaded content.
- Clean up failed uploads.

## Path Traversal

Before file access:

- Normalize paths.
- Resolve against an approved root.
- Verify the result remains within that root.
- Handle symbolic links or reparse points.
- Avoid concatenating paths from raw input.
- Use safe generated file names.

## SQL and Data Injection

- Use parameterized queries.
- Use LINQ or provider parameters safely.
- Do not concatenate user input into SQL.
- Allowlist dynamic sort columns or identifiers.
- Review raw SQL.
- Use least-privileged database accounts.
- Protect connection strings.
- Test malicious input.

## Deserialization

Prefer `System.Text.Json`.

- Avoid unbounded polymorphic deserialization.
- Allowlist derived types.
- Limit payload size and depth.
- Do not deserialize executable types or delegates.
- Validate objects after deserialization.
- Treat external messages as untrusted.
- Version message contracts.

## Cryptography

Use platform cryptography APIs and modern algorithms.

Do not invent cryptographic protocols.

Avoid obsolete algorithms such as MD5 or SHA-1 for security decisions.

Use:

- RandomNumberGenerator for security randomness
- Password hashing designed for passwords
- Authenticated encryption
- Managed key storage

Document key rotation and ownership.

## Data Protection

Use ASP.NET Core Data Protection for protected application data where appropriate.

Define:

- Key storage
- Key protection
- Application name or isolation
- Rotation
- Multi-instance sharing
- Backup
- Deployment behavior

Do not store keys ephemerally when protected data must survive restarts.

## Logging and Telemetry

Never log:

- Passwords
- Tokens
- Cookies
- Authorization headers
- Private keys
- Sensitive connection strings
- Full payment or health data
- Unnecessary personal data

Use structured redaction.

Avoid high-cardinality identity data in metrics.

Protect telemetry access.

## Error Handling

Clients must receive safe errors.

Do not expose:

- Stack traces
- Connection strings
- SQL text
- Internal paths
- Secret identifiers
- Internal host names unnecessarily

Use Problem Details for HTTP APIs.

Log diagnostic detail only at the controlled server boundary.

## Rate Limiting and Resource Exhaustion

Apply limits where abuse or accidental load is possible:

- Request rate
- Concurrent work
- Queue depth
- Payload size
- Pagination size
- Upload size
- Regex timeout
- External call duration
- Database query size

Reject or degrade safely.

## SSRF

For server-side outbound requests:

- Validate schemes.
- Allowlist hosts where practical.
- Prevent access to loopback, link-local, metadata, or private networks unless required.
- Revalidate redirects.
- Avoid forwarding credentials across hosts.
- Bound response size and timeout.

## Dependency Security

- Use trusted package sources.
- Review direct and transitive dependencies.
- Run vulnerability audit.
- Do not ignore advisories without documented analysis.
- Remove unused packages.
- Avoid abandoned packages for critical functions.
- Pin versions through central package management.
- Update vulnerabilities in focused changes.

## Native Code and Process Execution

- Avoid shell execution.
- Use `ProcessStartInfo.ArgumentList`.
- Validate executable path and arguments.
- Check exit codes.
- Do not pass secrets on command lines.
- Limit execution identity.
- Treat output as untrusted.
- Avoid loading untrusted native libraries.

## Background Processing

- Authenticate message sources.
- Authorize actions represented by messages.
- Validate schemas.
- Use idempotency.
- Bound retries.
- Handle poison messages.
- Protect dead-letter content.
- Preserve correlation without leaking sensitive data.

## Multi-Tenancy

- Include tenant scope in authorization and data access.
- Do not trust tenant identifiers from clients without authorization.
- Prevent cross-tenant cache keys and query leakage.
- Test cross-tenant access denial.
- Partition secrets and data appropriately.

## Security Testing

Test relevant controls:

- Unauthorized and forbidden access
- Cross-user and cross-tenant access
- SQL injection
- Path traversal
- Unsafe file upload
- SSRF
- Secret redaction
- CORS
- CSRF
- Rate limiting
- Unsafe deserialization
- Request size
- Error leakage
- Dependency vulnerabilities

## Security Exceptions

An exception requires:

- Explicit requirement
- Threat description
- Alternatives considered
- Narrow scope
- Mitigation
- Tests
- Documentation
- Owner and review condition

Do not create exceptions merely because secure implementation requires more effort.

## Guiding Rule

> When identity, authorization, trust, or target scope is uncertain, deny the operation and report what must be resolved.
