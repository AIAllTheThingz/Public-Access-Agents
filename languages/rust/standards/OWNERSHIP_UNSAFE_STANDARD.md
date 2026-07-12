---
id: RUST-SAFE-001
status: baseline
title: Rust Ownership and Unsafe Code Standard
---

# Ownership, Memory Safety, and Unsafe Code Standard

- Prefer ownership and borrowing designs that prevent invalid states.
- Introduce `unsafe` only when no safe design satisfies the requirement.
- Every unsafe block requires a documented safety invariant and focused tests.
- Minimize raw pointers, transmute operations, unchecked indexing, and manual allocation.
- Validate layout, lifetimes, nullability, aliasing, thread safety, and ownership at FFI boundaries.
- Keep unsafe code in the smallest reviewable module.
