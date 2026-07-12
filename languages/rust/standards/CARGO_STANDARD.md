---
id: RUST-CARGO-001
status: baseline
title: Rust Cargo Standard
---

# Cargo and Crate Standard

- Declare edition, rust-version, features, targets, and publishing metadata intentionally.
- Pin the toolchain when reproducibility matters.
- Keep features additive and avoid surprising coupling.
- Treat build scripts and proc macros as privileged code.
- Test supported feature combinations and targets proportionately.
- Document semver and MSRV expectations for published crates.
