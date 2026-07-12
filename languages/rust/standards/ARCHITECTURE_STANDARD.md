---
id: RUST-ARCH-001
status: baseline
title: Rust Architecture Standard
---

# Architecture Standard

- Keep crate and module boundaries cohesive.
- Separate domain logic from transport, persistence, process, platform, and FFI concerns.
- Keep dependency direction explicit and public APIs narrow.
- Use traits at true abstraction boundaries, not merely to imitate class hierarchies.
- Document feature, target, and deployment tradeoffs.
