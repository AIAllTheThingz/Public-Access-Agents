---
id: GO-MOD-001
status: baseline
title: Go Modules and Toolchain Standard
---

# Modules and Toolchain Standard

- Declare the supported Go version in `go.mod`.
- Use the `toolchain` directive only intentionally and document its effect.
- Run `go mod tidy` only when resulting changes are in scope and reviewed.
- Keep generated code and tool dependencies reproducible.
- Define module boundaries deliberately; do not create modules merely to bypass package design problems.
