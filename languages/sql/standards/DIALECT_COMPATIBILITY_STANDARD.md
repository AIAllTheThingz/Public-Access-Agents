---
id: SQL-DIALECT-001
status: baseline
title: SQL Dialect and Compatibility Standard
---

# Dialect and Compatibility Standard

- Name the database engine and supported versions for every reusable script.
- Do not assume syntax or functions are portable across engines.
- Use schema-qualified object names where appropriate.
- Declare collation, case sensitivity, time zone, encoding, compatibility, and session-setting assumptions.
- Verify execution plans on representative supported versions for performance-sensitive changes.
