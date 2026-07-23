---
name: csharp
description: Apply advanced C# language engineering standards to implementation, scripting, review, refactoring, debugging, testing, API design, performance, interoperability, source generation, or migration work. Use when Codex is working with .cs or .csx source, Roslyn/compiler behavior, nullable reference types, async and concurrency, generics, records, pattern matching, unsafe code, or C# language compatibility.
---

# Advanced C# Engineering

Apply this skill to C# language work. Compose it with the [.NET package](../dotnet/) when the .NET SDK, target frameworks, CLR behavior, MSBuild, NuGet, ASP.NET Core, data access, hosting, publishing, or deployment are in scope.

## Establish the compiler boundary

1. Read the repository root and nearest scoped `AGENTS.md` files.
2. Read this package's [agent standard](AGENTS.md), [manifest](MANIFEST.md), and only the supporting standards relevant to the task.
3. Inspect the selected SDK/compiler, target framework, `LangVersion`, nullable context, implicit usings, analyzer configuration, warning policy, generated code, package graph, and build commands.
4. Preserve the repository's declared compatibility boundary unless migration is explicitly requested.
5. For new modern .NET work, use the stable C# version associated with the selected supported target framework. Do not use `latest` or preview merely to obtain newer syntax.

Treat `.csproj`, `Directory.Build.props`, `global.json`, analyzer packages, editor configuration, and generated-source inputs as behavior-bearing code.

## Design before implementation

- Define public contracts, invariants, nullability, ownership, lifetime, thread-safety, cancellation, error semantics, serialization behavior, and compatibility requirements.
- Make invalid states difficult to represent, but do not add abstraction without a concrete maintenance or correctness benefit.
- Prefer clear types and ordinary language features over reflection, `dynamic`, unsafe code, expression compilation, or generated machinery.
- Identify trust boundaries and side effects before writing code that performs I/O, native interop, process execution, deserialization, cryptography, or privileged operations.

## Implement deliberately

- Enable and honor nullable reference analysis; suppress diagnostics only with a locally proven invariant.
- Treat warnings and analyzers as engineering feedback. Do not broadly disable them to make a build pass.
- Propagate `CancellationToken` through genuinely cancellable asynchronous work.
- Avoid sync-over-async, fire-and-forget work without an owner, hidden shared mutable state, and unbounded concurrency.
- Dispose owned `IDisposable` and `IAsyncDisposable` resources deterministically. Do not dispose borrowed resources.
- Preserve exception context and use exceptions for exceptional failure, not routine control flow.
- Keep public APIs, serialized shapes, generic constraints, default parameter values, and observable exception behavior compatible unless a reviewed change says otherwise.
- Use spans, pooling, ref-like types, custom allocation strategies, and unsafe code only when measurement and ownership justify the complexity.
- Keep secrets and sensitive values out of source, exceptions, logs, diagnostics, generated files, test artifacts, and command lines.

## Handle scripting and automation safely

For `.csx`, file-based apps, compiler scripting hosts, or C# automation:

- declare and pin the execution host and dependency mechanism
- separate discovery, validation, preview, execution, and verification for state-changing work
- require explicit authorization and confirmation for destructive or consequential actions
- validate paths, URLs, process arguments, input files, and remote responses
- return structured results and meaningful exit codes
- do not download and immediately execute code or resolve floating dependencies during operational execution

Read the [scripting and tooling standard](standards/SCRIPTING_AND_TOOLING_STANDARD.md) for detailed requirements.

## Test difficult behavior

Test externally meaningful contracts, including invalid and hostile input, null and boundary cases, cancellation, timeout, concurrent access, disposal, partial failure, serialization compatibility, generated-code behavior, native failure, and safe rerun where applicable.

Do not use tests that merely restate the implementation as proof of correctness. Use contract examples, regression cases, deterministic fixtures, and controlled integration boundaries.

## Validate in layers

Use repository-pinned commands when present. A typical modern .NET sequence is:

1. inspect SDK and compiler resolution
2. restore with the approved dependency configuration
3. verify formatting and generated files
4. run analyzers and compile without unexpected warnings
5. run focused unit and regression tests
6. run integration, contract, concurrency, and negative tests
7. run dependency and security checks
8. build or publish the representative deliverable

Do not claim C# compatibility from documentation review alone. Record exact tool versions and any validation that was unavailable.

## Report completion evidence

Report changed files and contracts, compiler/language/runtime assumptions, security and compatibility impact, exact commands and results, checks not run, generated artifacts, remaining limitations, and required C#/.NET specialist review.
