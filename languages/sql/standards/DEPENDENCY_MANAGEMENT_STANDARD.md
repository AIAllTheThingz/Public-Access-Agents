---
id: SQL-DEP-001
status: baseline
title: SQL Dependency Management Standard
---

# Dependency Management Standard

- Track object dependencies, extension requirements, compatibility features, migration tool versions, and application driver assumptions.
- Do not introduce engine extensions or privileged features without operational and security review.
- Pin migration tooling and container images when reproducibility matters.
- Review driver and ORM changes for generated SQL and transaction behavior.
- Document external jobs, replication, reporting, and integration dependencies.
