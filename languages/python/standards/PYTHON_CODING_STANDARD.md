---
id: PY-CODE-001
status: baseline
title: Python Coding Standard
---

# Python Coding Standard

## Required design qualities

- Prefer clear, idiomatic code over clever compression.
- Keep units cohesive and interfaces narrow.
- Make side effects, error paths, resource ownership, and state transitions explicit.
- Avoid hidden global state and order-dependent behavior.
- Preserve deterministic behavior where practical.
- Use names that describe intent and domain meaning.
- Remove dead code rather than commenting it out.
- Keep comments focused on intent, constraints, safety, and non-obvious tradeoffs.

## Error handling

- Handle expected failures explicitly.
- Preserve useful context without exposing secrets.
- Do not swallow errors or convert failure into false success.
- Clean up resources on success, failure, cancellation, and timeout.
- Define retry, timeout, and partial-success behavior where operations cross boundaries.

## Input and output

- Validate type, format, range, allowed values, existence, identity, and operational safety.
- Use structured output at reusable boundaries.
- Do not parse human-oriented output when a machine-readable interface exists.
- Keep serialization formats versioned when they cross process or persistence boundaries.

## Change discipline

- Do not reformat or refactor unrelated code.
- Do not add compatibility shims without an explicit requirement.
- Do not introduce new dependencies for trivial behavior.
- Keep generated files reproducible and identify their source.
