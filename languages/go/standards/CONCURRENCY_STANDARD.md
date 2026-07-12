---
id: GO-CONC-001
status: baseline
title: Go Concurrency Standard
---

# Concurrency Standard

- Every goroutine must have an owner, bounded lifetime, and shutdown path.
- Propagate `context.Context` through operation boundaries; do not store it in long-lived structs.
- Avoid unbounded goroutine creation, channels, queues, retries, and fan-out.
- Define channel ownership and closure responsibility.
- Protect shared state through clear ownership or synchronization.
- Prevent goroutine leaks and test cancellation and shutdown behavior.
