---
id: GO-TEST-001
status: baseline
title: Go Testing Standard
---

# Testing Standard

- Use table-driven tests when they improve coverage and readability.
- Test success, failure, boundary, cancellation, timeout, and idempotency behavior.
- Keep tests deterministic and isolated from production systems.
- Run race detection for concurrency changes.
- Use integration tests for network, storage, process, and serialization boundaries.
- Report skipped tests and unavailable coverage honestly.
