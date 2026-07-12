---
id: GOV-EX-AI-001
title: AI-Generated Code Review Example
version: 0.2.0
status: baseline
---

# AI-Generated Code Review Example

## Fictitious change

An AI assistant proposes a library upgrade and refactors authentication middleware.

## Review findings

- One proposed API exists only in a preview version.
- A new dependency is unnecessary.
- Negative authorization tests are missing.
- Generated comments overstate validation.
- No sensitive prompt input was used.

## Required action

- verify supported APIs
- remove unnecessary dependency
- add denied-access and object-ownership tests
- correct completion claims
- review middleware ordering
- record human approval

## Decision

Not approved until focused security review and tests pass.
