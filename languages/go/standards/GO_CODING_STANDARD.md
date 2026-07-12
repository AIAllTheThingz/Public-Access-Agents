---
id: GO-CODE-001
status: baseline
title: Go Coding Standard
---

# Go Coding Standard

- Write idiomatic Go formatted with `gofmt`.
- Keep packages cohesive, dependency direction clear, and exported APIs minimal.
- Return useful errors with context; do not compare error strings when typed or sentinel errors are available.
- Avoid panic for expected runtime conditions.
- Make resource ownership, closure, cancellation, and state transitions explicit.
- Prefer composition and small interfaces defined by consumers.
- Do not introduce hidden global mutable state or initialization-order dependencies.
- Keep generated code reproducible and separate from hand-maintained code.
- Avoid unrelated formatting or refactoring.
