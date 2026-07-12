---
id: RUST-CODE-001
status: baseline
title: Rust Coding Standard
---

# Rust Coding Standard

- Write idiomatic stable Rust and format with `rustfmt`.
- Prefer explicit domain types, enums, and ownership over primitive obsession and shared mutable state.
- Use `Result` and meaningful error types; do not panic for expected failures.
- Keep modules cohesive and public APIs minimal.
- Avoid unnecessary cloning, allocation, boxing, and dynamic dispatch.
- Do not use `unwrap` or `expect` in production paths unless impossibility is locally proven and explained.
- Preserve drop, cancellation, and cleanup behavior.
- Keep generated code reproducible and avoid unrelated refactoring.
