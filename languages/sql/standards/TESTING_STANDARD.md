---
id: SQL-TEST-001
status: baseline
title: SQL Testing Standard
---

# Testing Standard

- Test migrations from supported prior states in isolated databases.
- Test success, failure, boundary, NULL, constraint, concurrency, transaction, and permission behavior.
- Verify result sets, affected rows, data types, ordering guarantees, and post-change invariants.
- Use representative data volume and distribution for performance-sensitive changes.
- Test rollback or forward recovery proportionately.
- Keep tests isolated from production data and systems.
