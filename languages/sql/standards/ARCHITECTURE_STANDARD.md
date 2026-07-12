---
id: SQL-ARCH-001
status: baseline
title: SQL Architecture Standard
---

# Architecture Standard

- Separate schema definition, migration, application query, reporting, security, and operational concerns.
- Define ownership of invariants between database and application layers.
- Keep public database contracts stable and version breaking changes deliberately.
- Use schemas and naming conventions to make boundaries explicit.
- Document replication, partitioning, availability, retention, and deployment assumptions when relevant.
