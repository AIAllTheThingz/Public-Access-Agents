---
id: SQL-AGENT-001
status: baseline
title: SQL Agent Standard
---

# SQL Agent Standard

## Purpose

Mandatory rules for agents creating, modifying, reviewing, testing, securing, or documenting SQL, database objects, and migrations.

> Make the smallest safe, dialect-correct, testable, recoverable, and well-documented change that satisfies the requirement.

## Scope

- DDL, DML, queries, views, procedures, functions, migrations, seed data, permissions, and database tests

## Runtime baseline

SQL is dialect-specific. Every repository must declare the database engine, supported server versions, compatibility level, migration tool, transaction expectations, and operational constraints.

## Required supporting standards

- `standards/SQL_CODING_STANDARD.md`
- `standards/ARCHITECTURE_STANDARD.md`
- `standards/DOCUMENTATION_STANDARD.md`
- `standards/TESTING_STANDARD.md`
- `standards/SECURITY_STANDARD.md`
- `standards/DEPENDENCY_MANAGEMENT_STANDARD.md`
- `standards/OBSERVABILITY_STANDARD.md`
- `standards/COMPLETION_EVIDENCE.md`
- `standards/DIALECT_COMPATIBILITY_STANDARD.md`
- `standards/MIGRATION_STANDARD.md`
- `standards/DATA_INTEGRITY_STANDARD.md`

## Non-negotiable rules

- Inspect schema, constraints, indexes, data volume, execution plans, migration history, and application contracts first.
- Do not assume syntax, functions, isolation, locking, identity behavior, or transaction semantics are portable across engines.
- Parameterize values and validate identifiers through allowlists or controlled metadata.
- Do not interpolate untrusted input into SQL.
- Protect data integrity with constraints and explicit transactions where practical.
- Separate risky schema change, backfill, validation, and cleanup phases.
- Require explicit authorization for destructive, privilege, production-data, or bulk changes.
- Do not expose sensitive data in queries, examples, logs, errors, or test fixtures.
- Verify affected rows, keys, constraints, and resulting state.

## Required working method

1. Declare engine, version, compatibility, migration tool, and environment scope.
2. Discover dependencies, data size, locking risk, and recovery options.
3. Plan the narrowest safe change and evidence.
4. Implement migration and tests.
5. Validate syntax, plans, integrity, upgrade, rollback or forward recovery, and application compatibility.
6. Report exact evidence, limitations, and remaining risk.

## Typical validation

- parse or lint changed SQL
- apply migrations to an isolated database
- run database tests and integrity checks
- inspect execution plans for performance-sensitive changes
