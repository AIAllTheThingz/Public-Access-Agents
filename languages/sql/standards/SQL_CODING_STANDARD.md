---
id: SQL-CODE-001
status: baseline
title: SQL Coding Standard
---

# SQL Coding Standard

- Use consistent formatting and explicit object names.
- Prefer set-based, deterministic operations over row-by-row processing unless justified.
- Avoid `SELECT *` in stable interfaces and production queries.
- Specify column lists for inserts and durable projections.
- Use explicit joins, predicates, ordering, data types, and conversion behavior.
- Handle NULL, collation, time zone, precision, truncation, and overflow intentionally.
- Keep transactions as short as correctness permits.
- Do not hide errors or treat partial application as success.
- Avoid unrelated reformatting and preserve application contracts.
