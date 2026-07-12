---
id: RUST-DEP-001
status: baseline
title: Rust Dependency Management Standard
---

# Dependency Management Standard

- Add crates only when justified and review maintenance, provenance, license, vulnerabilities, features, build scripts, proc macros, and transitive impact.
- Commit `Cargo.lock` for applications and binaries.
- Use workspace dependencies consistently.
- Disable unnecessary default features and document feature coupling.
- Review dependency upgrades separately from unrelated behavior.
