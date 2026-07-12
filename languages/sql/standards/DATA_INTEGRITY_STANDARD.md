---
id: SQL-DATA-001
status: baseline
title: SQL Data Integrity Standard
---

# Data Integrity Standard

- Enforce invariants with constraints where practical.
- Use transactions with explicit isolation and retry assumptions.
- Prevent duplicate, orphaned, truncated, silently coerced, or partially migrated data.
- Treat NULL semantics explicitly.
- Validate row counts, affected keys, constraints, checksums, and post-change invariants.
- Do not disable integrity controls without explicit authorization and verified restoration.
