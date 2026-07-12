# JavaScript and TypeScript Documentation Standard

## Purpose

This standard defines documentation requirements for JavaScript and TypeScript
applications, libraries, APIs, browser code, configuration, and operations.

## Repository README

Document, where applicable:

- Purpose
- Node.js version
- Browser support
- TypeScript version
- Package manager
- Installation
- Locked-install command
- Development command
- Lint, typecheck, test, and build commands
- Configuration
- Secret-management expectations
- API behavior
- Deployment
- Health and observability
- Known limitations
- Troubleshooting
- Package publication

Keep commands current and executable.

## Public APIs

Document exported library APIs where consumers need guidance.

For TypeScript, types communicate structure but not all behavior.

Use TSDoc or JSDoc to document:

- Purpose
- Parameters
- Return value
- Rejection or thrown errors
- Cancellation
- Side effects
- Security considerations
- Examples
- Stability and deprecation

Do not merely repeat names.

## JavaScript JSDoc

Use JSDoc when it materially improves public JavaScript contracts.

Keep annotations synchronized with runtime behavior.

Do not use JSDoc as a substitute for runtime validation.

## Inline Comments

Comment non-obvious logic, especially:

- Security boundaries
- Authorization
- Abort behavior
- Cleanup
- Retry
- Concurrency
- External-service quirks
- Serialization
- Cache invalidation
- Browser compatibility
- Regular expressions
- Package interoperability
- Workarounds
- Performance-sensitive decisions

Explain why and risk, not obvious syntax.

## Commented-Out Code

Remove obsolete code.

Do not leave:

- Old implementations
- Debug output
- Disabled validation
- Disabled authorization
- Alternate package imports
- Temporary secrets
- Failed experiments

in source files.

## TODO and FIXME

Each marker must include:

- Specific work
- Reason
- Tracking reference when available
- Removal condition

Do not hide required incomplete behavior behind TODO comments.

## Configuration Documentation

Document:

- Key
- Type
- Required or optional status
- Default
- Allowed values
- Secret classification
- Source and precedence
- Runtime versus build-time exposure
- Restart or reload behavior
- Validation

Use fictitious values.

## API Documentation

Document:

- Route and method
- Authentication
- Authorization
- Request schema
- Validation
- Response schema
- Status codes
- Error shape
- Idempotency
- Pagination
- Rate limiting
- Timeout and abort behavior
- Versioning

Generated API documentation does not replace contract review.

## Package Documentation

For published packages, document:

- Supported runtimes
- ESM/CommonJS support
- Package exports
- Type declarations
- Installation
- Examples
- Tree-shaking expectations
- Side effects
- Peer dependencies
- Breaking-change policy
- Deprecation

## Operational Documentation

Document:

- Startup
- Graceful shutdown
- Health checks
- Logs, metrics, and traces
- Background work
- Retry and dead-letter behavior
- Deployment
- Rollback
- Persistent state
- Native dependencies
- Environment variables

## Documentation Synchronization

When behavior changes, update:

- README
- TSDoc/JSDoc
- OpenAPI
- Examples
- Environment reference
- ADRs
- Runbooks
- Test names
- Release notes
- Package metadata

Outdated documentation is a defect.

## Review

Before completion verify:

- Commands are current.
- Public behavior matches documentation.
- Examples use safe fictitious data.
- No secrets are present.
- Runtime and browser claims are accurate.
- Package exports match documentation.
- Errors and cancellation are described where relevant.
- New and removed behavior is reflected.

## Guiding Rule

> Document enough behavior, intent, risk, and operating context that another qualified developer can safely maintain and run the software.
