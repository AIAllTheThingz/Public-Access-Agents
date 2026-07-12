---
id: RUST-TEST-001
status: baseline
title: Rust Testing Standard
---

# Testing Standard

- Add unit and integration tests at appropriate boundaries.
- Test success, failure, boundary, feature, platform, serialization, cancellation, and cleanup behavior.
- Test unsafe and FFI invariants directly.
- Use property, fuzz, or model testing for parsers and high-risk state logic when proportionate.
- Keep tests deterministic and isolated from production systems.
