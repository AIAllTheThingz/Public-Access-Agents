# .NET Coding Standard

## Purpose

This standard defines coding requirements for current .NET LTS development using C#.

The objective is code that is readable, maintainable, testable, secure, observable, and predictable under failure.

Prefer simple code over clever code.

## Language and Runtime

- Target `net10.0` for new projects.
- Use only stable SDK and language features.
- Do not enable preview features unless explicitly requested.
- Preserve existing target frameworks in established repositories unless migration is in scope.
- Do not add .NET Framework compatibility unless explicitly required.
- Document platform-specific behavior.

## Project Defaults

New projects should normally enable:

```xml
<PropertyGroup>
  <TargetFramework>net10.0</TargetFramework>
  <Nullable>enable</Nullable>
  <ImplicitUsings>enable</ImplicitUsings>
  <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
  <AnalysisLevel>latest</AnalysisLevel>
  <EnforceCodeStyleInBuild>true</EnforceCodeStyleInBuild>
</PropertyGroup>
```

Repository policy may tune warnings and analyzer severity, but broad suppression is prohibited.

## Naming

Follow standard .NET naming conventions:

- PascalCase for namespaces, types, methods, properties, events, and public constants
- camelCase for parameters and local variables
- `_camelCase` for private instance fields
- `I` prefix for interfaces
- `Async` suffix for asynchronous methods returning `Task`, `Task<T>`, `ValueTask`, or `ValueTask<T>`
- `Try` prefix for methods returning success through Boolean result
- `CancellationToken` parameter named `cancellationToken`

Do not use Hungarian notation or type-encoded names.

Use domain language consistently.

Avoid abbreviations unless universally understood in the domain.

## Namespaces and Files

- Prefer one primary public type per file.
- Match file names to the primary type.
- Prefer file-scoped namespaces unless repository conventions differ.
- Keep namespaces aligned with project structure without creating excessive depth.
- Do not reorganize namespaces during unrelated work.

## Types

Choose the simplest appropriate type:

- `class` for reference types with identity or behavior
- `record` for value-like immutable data
- `record struct` or `struct` only when value semantics and allocation characteristics justify them
- `enum` for stable finite value sets
- interfaces for meaningful behavioral contracts, not automatic wrapping of every class

Do not add an interface solely to make a class mockable.

Prefer sealed classes when inheritance is not an intended extension point.

Document intentional inheritance contracts.

## Nullability

Nullable reference types must be enabled.

Requirements:

- Express nullability accurately.
- Do not silence warnings with `!` without a documented invariant.
- Avoid returning `null` collections.
- Validate public inputs.
- Use nullable types only when absence is meaningful.
- Prefer explicit result types when failure or absence has domain meaning.

Use:

```csharp
ArgumentNullException.ThrowIfNull(value);
```

where appropriate.

Do not use empty strings as a universal substitute for missing data.

## Methods

Methods should have one clear responsibility.

Prefer:

- Guard clauses
- Early returns
- Small understandable control-flow blocks
- Explicit domain operations
- Pure functions for transformations

Avoid:

- Deep nesting
- Boolean parameter collections that obscure behavior
- Large methods with unrelated work
- Hidden side effects
- Methods that both mutate state and format presentation without a clear boundary

Do not split methods solely to meet arbitrary line-count targets.

## Parameters

- Keep parameter lists understandable.
- Use parameter objects when a stable group of related values exists.
- Do not use dictionaries as untyped parameter bags.
- Avoid optional parameters for values that materially change behavior unless defaults are safe and obvious.
- Validate public method arguments.
- Place `CancellationToken` last unless an established API convention requires otherwise.

Avoid Boolean flags when named operations or an options type communicate behavior more clearly.

## Properties and Fields

- Prefer read-only properties and fields.
- Avoid public mutable fields.
- Use init-only properties for immutable construction where appropriate.
- Do not expose mutable internal collections directly.
- Use defensive copies or read-only abstractions where required.
- Avoid static mutable state.

Constants should represent true compile-time constants.

Use `static readonly` for runtime-initialized immutable values.

## Async Programming

Use async all the way through asynchronous call chains.

Requirements:

- Do not block with `.Result`, `.Wait()`, or `.GetAwaiter().GetResult()` in normal application code.
- Do not use `Task.Run` to disguise synchronous I/O.
- Do not use `async void` except for required event handlers.
- Await tasks or explicitly own their lifecycle.
- Observe exceptions from all tasks.
- Propagate `CancellationToken`.
- Do not convert cancellation into generic failure.
- Use `Task.WhenAll` only when concurrency is safe and bounded.
- Avoid unbounded parallelism.

Use `ValueTask` only when measurement and API semantics justify it.

## Cancellation

Cancellable operations should:

- Accept `CancellationToken`
- Pass it to downstream APIs
- Check it during long CPU-bound loops
- Respect request-aborted tokens in ASP.NET Core
- Stop background processing gracefully
- Avoid logging expected cancellation as an error

Do not create a new unrelated token when the caller already supplied one.

## Time

Use `TimeProvider` for testable time-sensitive logic.

Prefer UTC internally.

Use `DateTimeOffset` for timestamps with offsets.

Use invariant, ISO 8601 formats for machine-readable timestamps.

Do not call `DateTime.Now` throughout business logic.

Do not compare date strings when date types are available.

## Exceptions

- Throw specific exceptions.
- Include useful context without secrets.
- Do not catch exceptions that cannot be handled.
- Preserve stack traces with `throw;`.
- Avoid `throw exception;`.
- Do not use exceptions for normal branching.
- Do not expose implementation exceptions directly across HTTP or message boundaries.
- Avoid logging and rethrowing at every layer.

Use domain exceptions sparingly and only when callers can act on them.

## Result Modeling

Use exceptions for exceptional failures and explicit result types for expected domain outcomes.

Do not create a generic `Result<T>` abstraction unless the project has a defined need and consistent policy.

Avoid returning ambiguous tuples from public APIs when named types improve clarity.

## Collections

- Return empty collections instead of `null`.
- Prefer interfaces that match intended usage.
- Avoid unnecessary materialization.
- Avoid multiple enumeration of expensive sequences.
- Use `IReadOnlyCollection<T>` or `IReadOnlyList<T>` for stable read-only outputs where appropriate.
- Do not expose mutable collections directly.
- Use `HashSet<T>` for membership when appropriate.
- Use comparers explicitly where case or culture matters.

Do not use LINQ when a simple loop is clearer or materially more efficient.

## LINQ

LINQ should improve readability.

Avoid:

- Deeply nested expressions
- Hidden repeated database execution
- Multiple enumeration
- Side effects inside projections
- Client-side evaluation of large data sets
- Calling `ToList()` prematurely

For `IQueryable<T>`, understand what executes remotely.

Project only required fields for read operations.

## Strings and Culture

- Use interpolation for readable composition.
- Use structured logging rather than interpolated log messages.
- Use `StringComparison` explicitly for security or protocol-sensitive comparisons.
- Use ordinal comparison for identifiers and protocol values unless culture-aware behavior is intended.
- Use invariant culture for machine-readable parsing and formatting.
- Avoid culture-sensitive case conversion for identifiers.

## Regular Expressions

- Use source-generated regular expressions where appropriate.
- Specify timeouts for runtime regular expressions.
- Comment complex patterns.
- Test malicious or pathological input.
- Do not use regex where simple parsing is clearer.

## Resource Disposal

Dispose `IDisposable` and `IAsyncDisposable` correctly.

Prefer `using` declarations where scope is clear.

Do not dispose dependencies owned by the DI container.

Do not create a new `HttpClient` per request.

Ensure streams and responses are disposed appropriately.

## Dependency Injection

Use constructor injection for required dependencies.

Requirements:

- Avoid service locator patterns.
- Avoid injecting `IServiceProvider` into ordinary business services.
- Validate lifetimes.
- Do not capture scoped services in singletons.
- Avoid static service state.
- Keep constructors focused on actual dependencies.
- Use options abstractions for configuration.
- Use keyed services only when they materially improve the design.

Do not create interfaces around concrete types solely for test mocking.

## Configuration

Use strongly typed options.

Requirements:

- Bind configuration to options classes.
- Validate options at startup.
- Use `ValidateOnStart()` where startup failure is preferable.
- Keep secrets out of committed files.
- Do not access configuration by scattered string keys throughout business code.
- Document precedence among settings.
- Avoid reloading values that cannot be applied safely at runtime.

## HTTP Clients

Use `IHttpClientFactory`, typed clients, or named clients.

Configure:

- Base address
- Timeouts
- Authentication handlers
- Resilience behavior
- Default headers only when safe
- Certificate validation through approved trust, not bypass callbacks

Propagate cancellation tokens.

Dispose response content appropriately.

Do not automatically retry non-idempotent requests without an idempotency strategy.

## Serialization

Prefer `System.Text.Json` unless project requirements justify another serializer.

Requirements:

- Define public JSON contracts deliberately.
- Avoid polymorphic deserialization from untrusted input unless types are allowlisted.
- Do not serialize secrets.
- Use source generation when performance or trimming requirements justify it.
- Test casing, enum, date, and null-handling behavior.
- Avoid changing serializer defaults globally without compatibility review.

## Reflection and Dynamic Code

Avoid reflection, `dynamic`, runtime code compilation, and expression generation unless required.

When used:

- Document why
- Validate inputs
- Consider trimming and AOT
- Cache expensive metadata where safe
- Add tests
- Avoid executing untrusted code

## Native Interop and Processes

When invoking processes:

- Resolve the executable explicitly where practical.
- Use `ProcessStartInfo.ArgumentList`.
- Avoid shell execution unless required.
- Do not concatenate untrusted command strings.
- Capture standard output and error intentionally.
- Check exit codes.
- Propagate cancellation and terminate owned processes safely.
- Do not place secrets in command-line arguments when alternatives exist.

## Thread Safety and Concurrency

- Avoid shared mutable state.
- Document thread-safety expectations.
- Use concurrent collections only when needed.
- Bound channels, queues, and parallel work.
- Use locks narrowly.
- Do not perform async work while holding a synchronous lock.
- Use `SemaphoreSlim` or channels when appropriate.
- Test concurrency-sensitive behavior.

## Performance

Optimize only with evidence.

Consider:

- Allocation
- Query count
- Network calls
- Serialization
- Logging volume
- Lock contention
- Thread-pool starvation
- Large object heap use
- Startup and publish characteristics

Do not sacrifice maintainability for speculative micro-optimization.

Use benchmarks for performance-critical claims.

## Comments

Comments should explain:

- Why
- Risk
- Compatibility constraints
- Non-obvious algorithms
- Workarounds
- Security controls
- Concurrency behavior
- External-system assumptions

Do not narrate obvious syntax.

Remove stale or commented-out code.

Follow `DOCUMENTATION_STANDARD.md`.

## Formatting and Style

- Use `.editorconfig`.
- Run `dotnet format --verify-no-changes`.
- Preserve repository conventions.
- Avoid formatting unrelated files.
- Prefer braces for control-flow blocks.
- Keep expressions readable.
- Do not compress logic into clever one-liners.

## Guiding Rule

> Write code another qualified .NET developer can understand, test, operate, and safely modify without the original author present.
