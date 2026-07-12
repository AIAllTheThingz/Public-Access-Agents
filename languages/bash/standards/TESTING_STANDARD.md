---
id: BASH-TEST-001
status: baseline
title: Bash Testing Standard
---

# Testing Standard

- Run syntax checking and ShellCheck on changed scripts.
- Add Bats or repository-equivalent tests for parsing, branching, failures, cleanup, idempotency, and dry-run behavior.
- Mock external commands at controlled boundaries.
- Test paths containing spaces, empty values, special characters, and failed commands.
- Keep tests isolated from production systems and report unsupported platforms honestly.
