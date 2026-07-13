---
id: TOOL-AGENT-001
title: Tooling Agent Instructions
version: 1.0.0
status: baseline
---

# Tooling Agent Instructions

## Purpose

These instructions govern executable validation, generation, and composition tools under `tools/`.

Tool changes can alter repository gates, generated records, selected standards, or machine-readable evidence. Treat them as product code with public command-line contracts, not as incidental maintenance scripts.

## Scope

These instructions apply to:

- Python entry points under `tools/`
- shared libraries and result contracts
- unit tests and fixtures
- tool READMEs and manifests
- CI invocation of repository tools
- generated manifests and composition bundles

## Authority and precedence

1. Applicable law, contracts, safety, and security requirements
2. Explicit authorized repository requirements
3. Root `AGENTS.md`
4. Governance standards
5. These tooling instructions
6. More-specific local instructions
7. Existing implementation conventions

More-specific instructions may strengthen requirements. They may not silently weaken validation, reporting, compatibility, or safety boundaries.

## Required behavior

- Preserve stable executable paths unless migration is explicitly documented.
- Default to read-only behavior except for tools whose documented purpose is generation or composition.
- Require `--force` before replacing existing output.
- Support dry-run behavior for writing tools.
- Keep output deterministic unless nondeterminism is explicitly required and recorded.
- Use structured findings and stable exit codes.
- Never suppress a failure merely to produce a green CI result.
- Keep tools offline by default. Network access requires explicit design and review.
- Resolve paths within the declared repository root.
- Reject path traversal and unsafe output targets.
- Do not log secrets, credentials, tokens, private keys, or sensitive evidence.
- Do not infer authorization from access or successful execution.
- Do not claim semantic truth from structural validation.
- Pin external validation dependencies used by CI.
- Test both passing and failing behavior.

## Working method

1. Inspect the tool contract, callers, CI, tests, fixtures, and affected repository content.
2. Define intended behavior and compatibility impact.
3. Classify the change as compatible, conditionally compatible, or breaking.
4. Implement the smallest coherent change.
5. Add or update positive, negative, and error-path tests.
6. Run unit tests and the complete validation pipeline.
7. Review JSON output, text output, exit codes, and filesystem side effects.
8. Record commands, results, checks not run, and limitations.
9. Update README, manifest, examples, catalog, and compatibility guidance together.
10. Obtain accountable review.

## Completion gate

Tool work is incomplete until:

- executable behavior and documentation agree
- stable paths are preserved or migrated
- unit tests pass
- the complete repository validation pipeline passes
- negative cases are exercised
- output and exit-code contracts are verified
- writing tools preserve safe defaults
- no temporary build or bootstrap artifact remains
- limitations and compatibility impact are recorded
