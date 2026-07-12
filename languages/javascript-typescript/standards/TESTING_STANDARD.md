# JavaScript and TypeScript Testing Standard

## Purpose

This standard defines testing requirements for Node.js, browser, library, and
full-stack JavaScript and TypeScript projects.

Tests must prove required behavior, safe failure, security boundaries,
cancellation, and public-contract stability.

## Test Layers

Use the smallest layer that proves the behavior:

- Unit
- Integration
- API or functional
- Browser component
- End-to-end
- Contract
- Architecture
- Performance

Do not force every behavior through end-to-end tests.

## Unit Tests

Unit tests should:

- Test focused behavior
- Run quickly
- Be deterministic
- Avoid production systems
- Avoid real network access
- Verify success and failure
- Verify abort behavior
- Verify edge cases

Test public outcomes rather than implementation trivia.

## Integration Tests

Integration tests may verify:

- Database behavior
- Filesystem
- HTTP adapters
- Message serialization
- Package exports
- Build output
- Browser APIs through controlled environments
- Service composition

Use isolated resources and cleanup.

Do not target production.

## Browser Tests

Use DOM-oriented component tests for user-visible behavior.

Use real-browser automation for:

- Critical navigation
- Authentication flows
- Browser compatibility
- File upload
- Accessibility
- Network and storage behavior
- Service workers
- Complex browser APIs

Do not rely only on synthetic DOM environments for browser-specific behavior.

## Test Naming

Names should describe:

- Scenario
- Action
- Expected result

Avoid names such as `works`, `test1`, or merely the function name.

## Isolation

Tests must not depend on:

- Execution order
- Developer machine state
- Current wall clock
- Production data
- Production credentials
- Shared mutable globals
- Uncontrolled environment variables
- External network access unless explicitly integration-tested

Reset mocks, timers, modules, and browser storage.

## Test Data

Use fictitious deterministic data.

Test:

- Empty values
- Boundaries
- Unicode
- Invalid formats
- Large inputs
- Duplicate values
- Malicious payloads
- Abort
- Timeout
- Concurrency
- Partial failure

Do not use copied production data unless sanitized and approved.

## Mocks and Fakes

Mock external behavior, not every internal function.

Avoid brittle call-count assertions unless interaction is the contract.

Do not mock the system under test.

Use fakes for stateful collaborators when clearer.

Do not add interfaces or indirection solely for a mocking library.

## Async Tests

- Await all test work.
- Do not leave unhandled promises.
- Use fake timers carefully.
- Avoid arbitrary sleep.
- Use signals or controlled clocks.
- Test rejection and abort.
- Verify cleanup.
- Restore timers and global state.

## Abort and Timeout Tests

Verify:

- Signals propagate
- Obsolete work stops
- Timeout is distinguishable from other failure where required
- Resources close
- Partial mutations do not occur incorrectly
- Aborts are not logged as ordinary errors

## Security Tests

Test applicable controls:

- Authentication
- Authorization
- Cross-user and cross-tenant denial
- Input validation
- XSS-sensitive rendering
- CSRF
- CORS
- Path traversal
- Shell injection
- SQL injection
- SSRF
- File upload
- Secret redaction
- Prototype pollution
- Unsafe object merge
- Rate limiting
- Request-size limits

Client-side restrictions are not authorization tests.

## Contract Tests

Protect:

- Package exports
- Function signatures
- Type declarations
- HTTP routes and schemas
- Status codes
- Message schemas
- Configuration keys
- Serialized field names
- Browser storage versions
- Exit codes

Review snapshots carefully.

## Type Tests

For published TypeScript APIs, add type-level tests where inference and
compatibility are part of the contract.

Do not rely solely on runtime tests for declaration quality.

## Regression Tests

Bug fixes should include a test that fails before the fix and passes after it
when practical.

## Coverage

Coverage is evidence, not a vanity target.

Prioritize:

- Security boundaries
- Error paths
- Public contracts
- State transitions
- Abort and cleanup
- Bug regressions

Do not add meaningless assertions to inflate percentages.

## Required Validation

Use repository scripts.

Typical sequence:

```bash
pnpm install --frozen-lockfile
pnpm format:check
pnpm lint
pnpm typecheck
pnpm test
pnpm build
```

For browser projects, run the defined browser or end-to-end suite.

For published packages:

```bash
pnpm pack --dry-run
```

## Failure Analysis

Classify failures:

- Introduced by current change
- Pre-existing
- Environmental
- Dependency-related
- Runtime-related
- Browser-related
- Flaky
- Test defect
- External service unavailable

Fix failures introduced by the change.

Do not weaken tests merely to obtain green output.

## Skipped Tests

Every skipped test requires a reason.

Report skipped and not-run tests separately.

## Completion Evidence

Report:

- Commands
- Passed
- Failed
- Skipped
- Not run
- Coverage
- Test runtime
- Browser versions
- External dependencies
- Environmental limitations

Follow `COMPLETION_EVIDENCE.md`.

## Guiding Rule

> Tests must prove behavior and safe failure, not merely decorate the repository with green checkmarks.
