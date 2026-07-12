# JavaScript and TypeScript Coding Standard

## Purpose

This standard defines coding requirements shared by JavaScript and TypeScript
projects.

The objective is code that is readable, maintainable, testable, secure,
observable, and predictable under failure.

Prefer simple code over clever code.

## Language Baseline

For new projects:

- Use modern ECMAScript supported by the declared runtime.
- Prefer ECMAScript modules.
- Use TypeScript for applications where static contracts materially improve maintenance.
- Use JavaScript with JSDoc when TypeScript is unnecessary but type guidance is valuable.
- Do not transpile for obsolete runtimes without an explicit support requirement.
- Do not enable experimental syntax casually.

## Naming

Use:

- PascalCase for classes, types, interfaces, enums, and components
- camelCase for functions, methods, variables, parameters, and properties
- UPPER_SNAKE_CASE only for true process-wide constants
- kebab-case for package names and most non-code file names
- descriptive Boolean names beginning with `is`, `has`, `can`, `should`, or `was`

Avoid Hungarian notation and type-encoded names.

Use consistent domain language.

## Variables

- Prefer `const`.
- Use `let` only when reassignment is required.
- Do not use `var`.
- Keep scope narrow.
- Avoid mutable module-level state.
- Avoid shadowing important variables.
- Do not reuse variables for unrelated meanings.

## Functions

Functions should have one clear responsibility.

Prefer:

- Guard clauses
- Early returns
- Explicit inputs and outputs
- Pure transformations
- Small understandable control flow

Avoid:

- Hidden side effects
- Long positional parameter lists
- Boolean flag collections
- Deep nesting
- Functions that mutate, persist, log, and format unrelated concerns together
- Returning unrelated shapes based on arbitrary branches

Use an options object when a stable group of parameters belongs together.

## Objects and Immutability

- Prefer immutable inputs and outputs.
- Avoid mutating caller-owned objects.
- Use shallow copies only when shallow copying is sufficient.
- Do not assume spread syntax performs deep cloning.
- Avoid unsafe merging of untrusted objects.
- Use `Object.create(null)` or `Map` for dictionary-like data when prototype keys are unsafe.
- Do not modify built-in prototypes.

## Equality and Coercion

- Use `===` and `!==`.
- Avoid implicit coercion in security-sensitive or business-critical behavior.
- Parse numbers explicitly.
- Validate `NaN`.
- Use explicit Boolean conversion when necessary.
- Understand that empty arrays and objects are truthy.

Do not use loose equality merely for convenience.

## Strings

- Use template literals for readable interpolation.
- Avoid constructing SQL, shell commands, HTML, or URLs through raw interpolation.
- Use `URL` and `URLSearchParams`.
- Use appropriate output encoding for HTML and other contexts.
- Use explicit locale and comparison behavior where relevant.
- Normalize identifiers only according to a documented protocol or domain rule.

## Numbers

- Validate finite values.
- Use `Number.isFinite()` and `Number.isNaN()`.
- Do not use floating point for exact currency without a defined representation.
- Use `BigInt` only when consumers and serialization can support it.
- Validate integer ranges.
- Avoid bitwise operations for ordinary arithmetic unless intentional and documented.

## Dates and Time

- Prefer ISO 8601 for machine-readable timestamps.
- Store and compare instants in UTC.
- Use explicit time zones for human scheduling.
- Avoid parsing ambiguous date strings.
- Inject or wrap time sources when deterministic testing matters.
- Do not scatter `Date.now()` throughout business logic.
- Review Temporal support before adoption; do not assume runtime availability solely from type definitions.

## Collections

- Return empty arrays or maps instead of `null` when absence is not meaningful.
- Avoid repeated linear scans when a `Map` or `Set` provides a clear lookup.
- Avoid mutating arrays during iteration.
- Use stable sorting when output order is part of a contract.
- Do not rely on incidental object-property order for protocol behavior.
- Avoid materializing large iterables without bounds.

## Iteration

Use the clearest construct:

- `for...of` for sequential async-aware iteration
- array methods for pure transformations
- ordinary loops for performance-sensitive or complex control flow

Do not use `forEach(async () => ...)` when the promises must be awaited.

Do not use `Promise.all()` over an unbounded input.

## Async Code

- Prefer `async`/`await`.
- Await or explicitly own every promise.
- Handle rejection.
- Propagate `AbortSignal`.
- Apply timeouts to external operations.
- Use bounded concurrency.
- Avoid `new Promise()` around APIs already returning promises.
- Do not make a promise executor `async`.
- Do not swallow abort errors.
- Avoid fire-and-forget tasks.

Document intentionally detached work and give it an owner.

## Errors

Throw `Error` instances or defined subclasses.

Do not throw strings or plain objects.

Requirements:

- Include useful context.
- Preserve the original cause using `cause` where appropriate.
- Avoid secrets.
- Do not catch errors that cannot be handled.
- Do not convert every error into a generic message.
- Do not use errors for routine expected results when a result type is clearer.
- Avoid logging and rethrowing at every layer.

## Resource Cleanup

Use `try/finally`, disposal APIs, stream teardown, and abort handling.

Clean up:

- File handles
- Streams
- Timers
- Sockets
- Child processes
- Event listeners
- Temporary files
- Browser observers
- Database clients owned by the caller

Do not leave process-liveness timers accidentally active.

## Modules

For new projects:

- Use ESM.
- Use explicit exports.
- Avoid circular dependencies.
- Avoid import-time side effects.
- Keep package boundaries stable.
- Use package `exports`.
- Use `node:` prefixes for Node built-ins.
- Do not deep import package internals.
- Do not rely on undeclared transitive dependencies.

Use default exports only when repository or framework convention gives them
clear value.

## Classes and Composition

Prefer functions and composition for stateless behavior.

Use classes when identity, encapsulated state, lifecycle, or framework contracts
justify them.

Avoid:

- Deep inheritance
- Classes containing only static utility methods
- Getter methods with surprising expensive work
- Public mutable fields
- Constructors performing network or filesystem I/O

## Regular Expressions

- Prefer simple parsing when possible.
- Comment complex expressions.
- Bound input length.
- Avoid catastrophic backtracking.
- Test adversarial input.
- Escape user-provided fragments.
- Do not use a global regular expression object in a stateful unsafe way across calls.

## JSON and Serialization

- Treat parsed JSON as untrusted.
- Validate schema after parsing.
- Do not serialize secrets.
- Define stable public field names.
- Handle dates explicitly.
- Handle `BigInt` deliberately.
- Avoid circular structures.
- Avoid unsafe polymorphic reconstruction.

## JavaScript-Specific Guidance

For JavaScript projects:

- Use `"type": "module"` for new Node.js packages.
- Use JSDoc for public contracts when it improves maintainability.
- Enable `checkJs` in `jsconfig.json` or TypeScript tooling where practical.
- Avoid type-like comments that drift from runtime behavior.
- Keep runtime validators at trust boundaries.

## Formatting

- Use Prettier or the repository formatter.
- Use ESLint for correctness and maintainability rules.
- Do not use the formatter as a substitute for linting.
- Do not mix large formatting changes with unrelated behavior.
- Preserve repository line endings.
- Use UTF-8.
- Keep lines readable.
- Use braces for multi-line control flow.

## Comments

Comments should explain:

- Why
- Risk
- Compatibility constraints
- External-system behavior
- Security decisions
- Concurrency
- Abort and cleanup behavior
- Workarounds
- Non-obvious algorithms

Do not narrate obvious syntax.

Remove stale or commented-out code.

Follow `DOCUMENTATION_STANDARD.md`.

## Guiding Rule

> Write JavaScript and TypeScript another qualified developer can understand, test, operate, and safely modify without the original author present.
