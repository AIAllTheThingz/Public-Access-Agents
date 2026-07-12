---
id: RUST-AGENT-001
status: baseline
title: Rust Agent Standard
---

# Rust Agent Standard

## Purpose

Mandatory rules for agents creating, modifying, reviewing, testing, securing, or documenting Rust code.

> Make the smallest safe, idiomatic, testable, observable, and well-documented change that satisfies the requirement.

## Scope

- Rust crates, services, CLI tools, libraries, FFI boundaries, tests, Cargo workspaces, and release configuration

## Runtime baseline

Use the stable Rust toolchain unless another channel is explicitly required. Pin the toolchain when reproducibility matters and declare the minimum supported Rust version for published libraries.

## Required supporting standards

- `standards/RUST_CODING_STANDARD.md`
- `standards/ARCHITECTURE_STANDARD.md`
- `standards/DOCUMENTATION_STANDARD.md`
- `standards/TESTING_STANDARD.md`
- `standards/SECURITY_STANDARD.md`
- `standards/DEPENDENCY_MANAGEMENT_STANDARD.md`
- `standards/OBSERVABILITY_STANDARD.md`
- `standards/COMPLETION_EVIDENCE.md`
- `standards/OWNERSHIP_UNSAFE_STANDARD.md`
- `standards/CARGO_STANDARD.md`

## Non-negotiable rules

- Inspect existing crates, features, toolchain declarations, tests, and conventions first.
- Prefer designs that make invalid states unrepresentable.
- Do not introduce `unsafe` without a documented safety invariant and focused tests.
- Treat FFI, deserialization, file, network, process, and dependency boundaries as untrusted.
- Preserve public APIs and semver expectations unless change is explicitly authorized.
- Keep secrets out of source, tests, logs, errors, examples, and configuration.
- Do not suppress compiler or Clippy findings broadly.
- Preserve cancellation, resource cleanup, and bounded operation behavior.

## Required working method

1. Discover workspace, crate, feature, MSRV, and platform support.
2. Identify ownership, lifetime, unsafe, FFI, and trust boundaries.
3. Implement the smallest coherent change.
4. Add tests and documentation.
5. Run format, Clippy, tests, and platform-specific checks.
6. Report exact evidence, limitations, and remaining risk.

## Typical validation

- `cargo fmt --check`
- `cargo clippy --all-targets --all-features -- -D warnings`
- `cargo test --all-features`
