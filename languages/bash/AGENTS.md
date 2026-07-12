---
id: BASH-AGENT-001
status: baseline
title: Bash Agent Standard
---

# Bash Agent Standard

## Purpose

Mandatory rules for agents creating, modifying, reviewing, testing, securing, or documenting Bash automation.

> Make the smallest safe, portable, testable, and well-documented change that satisfies the requirement.

## Scope

- Bash scripts, shell libraries, installation scripts, CI scripts, operational automation, tests, and runbooks

## Runtime baseline

Target Bash 5.x unless POSIX shell compatibility is explicitly required. Declare the interpreter in the shebang and do not assume Bash behavior in scripts advertised as `/bin/sh`.

## Required supporting standards

- `standards/BASH_CODING_STANDARD.md`
- `standards/ARCHITECTURE_STANDARD.md`
- `standards/DOCUMENTATION_STANDARD.md`
- `standards/TESTING_STANDARD.md`
- `standards/SECURITY_STANDARD.md`
- `standards/DEPENDENCY_MANAGEMENT_STANDARD.md`
- `standards/OBSERVABILITY_STANDARD.md`
- `standards/COMPLETION_EVIDENCE.md`
- `standards/PORTABILITY_STANDARD.md`
- `standards/SAFE_AUTOMATION_STANDARD.md`

## Non-negotiable rules

- Inspect the script, callers, environment assumptions, external commands, and tests first.
- Choose Bash or POSIX shell explicitly; do not mix dialects accidentally.
- Quote expansions and arguments correctly.
- Validate targets, paths, inputs, command availability, privileges, and current state before mutation.
- Default to discovery, validation, and dry-run behavior for state-changing automation.
- Do not use `eval`, `curl | sh`, untrusted command substitution, or dynamically assembled shell code.
- Never commit or log secrets.
- Use safe temporary files, restrictive permissions, traps, bounded waits, and explicit cleanup.
- Stop on ambiguity rather than guessing at production targets.

## Required working method

1. Discover interpreter, platform, dependencies, callers, and expected privileges.
2. Identify injection, path, temporary-file, concurrency, and destructive-operation risks.
3. Implement the smallest coherent change.
4. Add tests and update documentation.
5. Run syntax checking, ShellCheck, and repository tests.
6. Report exact evidence, limitations, and remaining risk.

## Typical validation

- `bash -n <changed-script>`
- `shellcheck <changed-script>`
- run Bats or repository-defined tests
