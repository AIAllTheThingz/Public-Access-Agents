---
id: DISC-TPL-ARCH-REVIEW
title: Architecture and System Design Review Checklist
version: 0.1.0
status: baseline
---
# Architecture and System Design Review Checklist

## Scope

- [ ] The change states why this discipline applies.
- [ ] The diff is limited to the requested outcome.
- [ ] Affected users, systems, data, contracts, and operators are identified.
- [ ] Hidden assumptions and environment-specific values were not invented.

## Requirements

- [ ] Applicable `AGENTS.md` rules are satisfied.
- [ ] Relevant supporting standards were reviewed.
- [ ] Security, privacy, accessibility, compatibility, reliability, and operational impacts are addressed as applicable.
- [ ] Failure, timeout, retry, rollback, recovery, and partial-success behavior is explicit where relevant.
- [ ] Exceptions are documented and approved.

## Evidence

- [ ] Evidence maps to each material claim.
- [ ] Positive, negative, boundary, and failure behavior was verified proportionate to risk.
- [ ] Commands, environments, results, and checks not run are recorded.
- [ ] Examples and documentation match actual behavior.
- [ ] Limitations, assumptions, residual risks, owners, and follow-up work are visible.

## Final review

- [ ] No unrelated refactoring or formatting is included.
- [ ] No secrets or sensitive data appear in source, tests, logs, errors, examples, or artifacts.
- [ ] Completion language does not exceed the available evidence.
