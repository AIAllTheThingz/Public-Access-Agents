---
id: SQL-MIG-001
status: baseline
title: SQL Migration Standard
---

# Migration Standard

- Migrations must be ordered, traceable, and reproducible in controlled environments.
- Separate schema, backfill, validation, and cleanup phases for risky changes.
- Provide rollback or forward-recovery guidance.
- Avoid long blocking transactions, table rewrites, and unbounded updates without operational review.
- Use batching and resumability for large data changes.
- Test upgrades from realistic prior versions with representative data.
