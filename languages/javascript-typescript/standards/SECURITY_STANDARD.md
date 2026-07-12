# JavaScript and TypeScript Security Standard

## Purpose

This standard defines security requirements for Node.js, browser, package, and
full-stack JavaScript and TypeScript software.

## Core Principles

- Default deny.
- Authenticate and authorize at trusted server boundaries.
- Use least privilege.
- Validate untrusted input.
- Preserve TLS and certificate validation.
- Minimize secret exposure.
- Bound resource use.
- Prevent code and command injection.
- Review supply-chain risk.
- Fail safely.
- Log auditable outcomes without sensitive data.

## Secrets

Never hardcode or commit:

- Passwords
- Tokens
- API keys
- Private keys
- Client secrets
- Session secrets
- Signing keys
- Credential-bearing connection strings

Do not expose server secrets to browser bundles.

Do not place secrets in:

- Logs
- Metrics
- Traces
- URLs
- Exceptions
- Source maps
- Command-line arguments when safer methods exist
- Test fixtures
- `.env.example`

## Authentication and Authorization

- Authenticate through established libraries and protocols.
- Authorize server-side.
- Use policies or resource checks.
- Verify ownership and tenant boundaries.
- Do not trust browser-provided roles or tenant identifiers.
- Do not rely on hidden UI controls.
- Deny by default.
- Test forbidden and cross-boundary access.

## Input Validation

Validate:

- Type
- Length
- Range
- Format
- Allowed values
- Ownership
- URI scheme and host
- File paths
- Upload size and content
- Pagination
- Sort and filter fields
- Object keys
- Nested depth

Use allowlists where practical.

TypeScript types are not runtime validation.

## XSS and HTML

- Prefer framework escaping and text APIs.
- Do not inject untrusted HTML.
- Sanitize approved rich text.
- Avoid unsafe DOM sinks.
- Use CSP.
- Avoid inline-script exceptions without review.
- Protect source maps and diagnostic data.

## CSRF

Protect cookie-authenticated state-changing browser requests.

Do not assume JSON content types automatically eliminate CSRF.

Use same-site cookies, anti-forgery tokens, origin checks, or architecture-
appropriate protections.

## CORS

- Configure explicit origins.
- Do not combine wildcard origins with credentials.
- Limit methods and headers.
- Do not treat CORS as authorization.
- Separate development and production policies.

## SSRF

For outbound requests:

- Validate schemes.
- Allowlist hosts where practical.
- Block loopback, link-local, metadata, and private networks unless required.
- Revalidate redirects.
- Avoid forwarding credentials across hosts.
- Apply timeout.
- Bound response size.
- Resolve DNS and rebinding risks appropriate to the threat model.

## Path Traversal

- Normalize paths.
- Resolve against an approved root.
- Verify the result remains within the root.
- Handle symbolic links.
- Generate storage names.
- Avoid raw client file names.
- Do not execute uploaded content.

## Shell and Process Injection

- Avoid shells.
- Use argument arrays.
- Validate executable paths and arguments.
- Do not concatenate commands.
- Do not use `exec` with untrusted strings.
- Do not place secrets in process arguments.
- Bound output and runtime.
- Drop privileges where practical.

## Dynamic Code

Prohibited by default:

- `eval`
- `new Function`
- `vm` execution of untrusted code
- Dynamic imports derived from untrusted arbitrary paths
- Template compilation from untrusted code
- Deserializing functions
- Executing package scripts from untrusted sources

## Prototype Pollution

- Avoid merging untrusted objects into ordinary objects.
- Reject dangerous keys such as `__proto__`, `constructor`, and `prototype` where relevant.
- Use validated schemas.
- Prefer `Map` or null-prototype dictionaries for untrusted key spaces.
- Keep dependencies patched.
- Test nested malicious payloads.

## SQL and Data Injection

- Parameterize queries.
- Allowlist identifiers.
- Do not concatenate SQL.
- Use least-privileged accounts.
- Protect connection strings.
- Avoid logging sensitive query parameters.

## Deserialization

- Treat JSON and messages as untrusted.
- Limit size and depth.
- Validate schema.
- Avoid reconstructing executable or arbitrary class instances.
- Version contracts.
- Reject unknown fields when strict contracts require it.

## Cookies and Tokens

- Use Secure, HttpOnly, and appropriate SameSite settings.
- Rotate session identifiers.
- Protect refresh tokens.
- Avoid long-lived tokens in browser storage.
- Do not place tokens in URLs.
- Validate issuer, audience, signature, expiry, and intended use.
- Avoid custom token formats without need.

## Dependency Security

- Use trusted registries.
- Commit lockfiles.
- Use frozen installs.
- Review lifecycle scripts.
- Review direct and transitive dependencies.
- Use package-manager security defaults.
- Audit dependencies.
- Remove unused packages.
- Avoid abandoned critical packages.
- Review typosquatting and dependency-confusion risk.
- Delay newly published dependencies when policy requires it.

## Browser Supply Chain

Review:

- Bundled dependencies
- CDN scripts
- Subresource integrity
- Third-party tags
- Analytics
- Browser extensions and integration boundaries
- Source maps
- Build plugins

Do not load unpinned remote scripts without review.

## Logging and Telemetry

Never log:

- Passwords
- Tokens
- Cookies
- Authorization headers
- Private keys
- Sensitive connection strings
- Full personal or regulated data without explicit protected need

Redact before serialization.

Avoid high-cardinality sensitive metric labels.

## Rate and Resource Limits

Bound:

- Request rate
- Concurrent work
- Queue depth
- Payload size
- Upload size
- JSON depth
- Regex complexity
- Outbound request duration
- Response size
- WebSocket connections
- Browser storage

## Security Headers

For browser applications review:

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy
- Frame restrictions
- Cache-Control for sensitive content

## Security Testing

Test:

- Unauthorized and forbidden access
- Cross-tenant access
- XSS
- CSRF
- CORS
- SSRF
- Shell injection
- SQL injection
- Path traversal
- Prototype pollution
- Unsafe file upload
- Secret redaction
- Rate limits
- Payload limits
- Unsafe redirects
- Source-map exposure

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

## Guiding Rule

> When identity, authorization, input trust, or target scope is uncertain, deny the operation and report what must be resolved.
