# TypeScript Standard

## Purpose

This standard defines TypeScript 6.0 configuration and type-safety
requirements.

TypeScript improves compile-time confidence. It does not validate runtime data
and does not authorize operations.

## Required Compiler Posture

New TypeScript projects must enable strict checking.

Recommended baseline:

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noPropertyAccessFromIndexSignature": true,
    "useUnknownInCatchVariables": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

Do not weaken strictness merely to make a migration compile.

## TypeScript 6.0 Baseline

For Node.js 24 applications, prefer:

- `target`: `ES2025`
- `module`: `NodeNext`
- `moduleResolution`: `NodeNext`
- Explicit `rootDir`
- Explicit `types`
- ESM package metadata
- Stable, non-preview TypeScript

Review TypeScript 6.0 deprecations rather than suppressing them broadly.

Do not set `ignoreDeprecations` as a permanent substitute for migration.

## `any`

`any` is prohibited by default.

Use `unknown` for untrusted or unspecified data, then narrow it.

An `any` exception must be:

- Narrow
- Documented
- Contained at an interoperability boundary
- Covered by tests
- Removed when upstream types improve

Do not spread `any` through public APIs.

## Type Assertions

Avoid `as` assertions used merely to silence the compiler.

Assertions require a proven invariant.

Prefer:

- Runtime validation
- Type guards
- Discriminated unions
- Generic constraints
- `satisfies`
- Exhaustive narrowing

Double assertions such as `value as unknown as Type` are prohibited by default.

## Non-Null Assertions

Avoid `!`.

Use it only when an invariant is established externally and cannot be expressed
more safely.

Document why the value cannot be null.

Do not use `!` to bypass incomplete initialization or missing validation.

## Runtime Validation

Validate all external data at runtime:

- JSON
- HTTP bodies
- Environment variables
- Database records from weak schemas
- Message payloads
- Browser storage
- Third-party API responses
- File content

TypeScript types disappear at runtime.

Use a maintained validation library when its value justifies the dependency, or
write focused validators for small schemas.

Infer static types from runtime schemas where practical to prevent drift.

## Public Types

Public types must:

- Use stable names
- Avoid leaking implementation details
- Model optionality accurately
- Avoid exposing mutable internal objects
- Preserve backward compatibility
- Distinguish expected outcomes
- Avoid enormous generic signatures consumers cannot understand

Do not export persistence or framework types as package contracts by accident.

## Interfaces, Types, and Classes

Use:

- `interface` for extendable object contracts where declaration merging or implementation is useful
- `type` for unions, intersections, mapped types, and aliases
- classes for runtime identity and behavior

Do not turn this into ideology. Choose the clearest appropriate construct.

## Discriminated Unions

Use discriminated unions for finite state or result modeling.

Ensure exhaustive handling.

Example:

```typescript
type OperationResult =
  | { readonly kind: "success"; readonly value: string }
  | { readonly kind: "notFound" }
  | { readonly kind: "failure"; readonly error: Error };
```

Use a `never` check when exhaustive behavior matters.

## Generics

Use generics when relationships between inputs and outputs are real.

Avoid:

- Unnecessary generic parameters
- Unconstrained generics
- Generic abstractions used once
- Type-level puzzles that reduce readability
- Complex conditional types without tests

Name generic parameters descriptively when more than one exists.

## Optional Properties

With `exactOptionalPropertyTypes`, distinguish:

- Property absent
- Property present with `undefined`
- Property present with a value

Do not assume these states are interchangeable in serialization or patch APIs.

## Indexed Access

With `noUncheckedIndexedAccess`, handle potentially missing array and object
entries explicitly.

Do not suppress safety with assertions.

Use maps, validated keys, or guards where appropriate.

## Enums

Prefer string literal unions or `as const` objects for many application
contracts.

Use enums when runtime enum objects or interoperability require them.

Avoid numeric enums in public serialized contracts unless explicitly designed.

## Imports and Exports

Use type-only imports where required:

```typescript
import type { Example } from "./example.js";
```

With `verbatimModuleSyntax`, keep runtime and type imports accurate.

Do not depend on import elision magic.

## Declaration Output

For published TypeScript packages:

- Emit declarations.
- Review declaration files.
- Define package exports.
- Test consumption from supported module systems.
- Avoid leaking private dependency types.
- Run package dry-run validation.

## Build Versus Typecheck

Keep type checking and emit responsibilities clear.

Typical scripts:

```json
{
  "typecheck": "tsc --noEmit",
  "build": "tsc -p tsconfig.build.json"
}
```

Do not pass source-file arguments to `tsc` when a project configuration should
govern compilation.

## JavaScript Interop

When importing untyped JavaScript:

- Add focused declaration files or wrappers.
- Validate runtime behavior.
- Do not declare an overly broad module as `any`.
- Contribute or adopt maintained types when practical.

## Guiding Rule

> Use TypeScript to express valid states and stable contracts, while validating every untrusted value at runtime.
