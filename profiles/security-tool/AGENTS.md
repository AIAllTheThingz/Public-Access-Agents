---
id: PROFILE-SECTOOL-AGENT-001
title: Security Tool Project Profile Agent Instructions
version: 0.2.0
status: baseline
---
# Security Tool Project Profile Agent Instructions

## Purpose

Defines mandatory behavior for agents working in a repository or scope governed by the Security Tool profile.

## Required reading

- [`../SECURITY_TOOL.md`](../SECURITY_TOOL.md)
- [`README.md`](README.md)
- [`MANIFEST.md`](MANIFEST.md)
- every applicable file in `standards/`
- root governance
- selected language, discipline, framework, platform, virtualization, operating-system, and networking packages
- nearest more-specific `AGENTS.md`

## Instruction precedence

1. External obligations and authorized user requirements
2. Root governance and repository instructions
3. This profile package
4. Selected language, discipline, framework, platform, virtualization, operating-system, and networking packages
5. Nearest scoped instructions, where they are compatible and no weaker
6. Repository conventions
7. General preferences

## Non-negotiable behavior

- Inspect project facts and existing instructions before editing.
- Do not invent users, systems, environments, identities, data, versions, commands, or evidence.
- Classify risk before material implementation.
- Preserve public and operational contracts unless change is authorized.
- Validate trust-boundary input.
- Keep secrets and sensitive data out of source, logs, examples, and evidence.
- Use least privilege and explicit authorization for consequential work.
- Add or update tests and documentation.
- Define rollback, recovery, or safe failure where applicable.
- Report checks not run and limitations.
- Do not claim production readiness from build or unit-test success.

## Required working method

1. Confirm the profile and scope.
2. Identify inherited standards.
3. Discover architecture, users, interfaces, data, identities, dependencies, deployment, and ownership.
4. Classify risk and define evidence.
5. Resolve material uncertainty.
6. Implement the smallest coherent change.
7. Add tests, documentation, and operational evidence.
8. Run project and repository validation.
9. Review for unrelated changes, unsafe defaults, false claims, and missing controls.
10. Record exact evidence and limitations.

## Profile-specific decisions

- authorized scope and target identity
- safe handling of findings and evidence
- false-positive and false-negative limitations
- privilege and data sensitivity
- non-destructive defaults
- remediation authorization
- finding lifecycle and disclosure
- audit, retention, and chain of custody

## Risk focus

Typical starting risk: `high`.

Escalate when privilege, exposure, data sensitivity, tenant boundaries, destructiveness, irreversibility, availability, safety, or evidence weakness increase.

## Required completion evidence

- changed files and scope
- profile and package selection
- risk classification
- architecture and trust boundaries
- security and privacy effects
- exact commands and results
- checks not run
- operations and release impact
- limitations and residual risk
- reviewer and approver

## Completion gate

Do not report work complete until applicable profile decisions, selected standards, validation, evidence, and review requirements are satisfied.
