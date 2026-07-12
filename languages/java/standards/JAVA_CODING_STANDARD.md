---
id: JAVA-CODE-001
status: baseline
title: Java Coding Standard
---

# Java Coding Standard

## Required design qualities

- Prefer clear, idiomatic Java over clever compression.
- Keep classes cohesive, interfaces narrow, and mutability controlled.
- Make side effects, error paths, resource ownership, and state transitions explicit.
- Use try-with-resources for closeable resources.
- Preserve interruption and cancellation semantics.
- Avoid hidden global state and order-dependent behavior.
- Use names that describe intent and domain meaning.
- Remove dead code rather than commenting it out.

## Error handling

- Handle expected failures explicitly and preserve useful context without exposing secrets.
- Do not swallow exceptions or convert failure into false success.
- Do not catch `Throwable` or broad exceptions without a documented boundary reason.
- Define retry, timeout, and partial-success behavior where operations cross boundaries.

## Change discipline

- Do not reformat or refactor unrelated code.
- Do not add compatibility shims without an explicit requirement.
- Do not introduce new dependencies for trivial behavior.
- Keep generated files reproducible and identify their source.
