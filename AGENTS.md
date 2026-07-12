# Repository Agent Instructions

## Purpose

This repository contains public engineering standards for coding agents. Changes must improve safety, clarity, maintainability, testability, portability, or evidence quality without silently weakening existing controls.

## Required reading order

Before modifying this repository:

1. Read `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `CATALOG.md`.
2. Read the applicable governance files.
3. Read every scoped `AGENTS.md` between the repository root and the target file.
4. Inspect referenced standards, schemas, examples, and templates.
5. Classify the change as editorial, normative, compatibility-related, security-related, or breaking.

## Mandatory working method

- Define the smallest coherent scope.
- Inspect existing behavior before proposing replacements.
- Preserve stable rule identifiers.
- Keep normative requirements testable.
- Update cross-references, manifests, examples, schemas, and templates affected by the change.
- Validate JSON, YAML, Markdown links, and repository structure.
- Report what was validated and what was not.
- Do not claim completion without evidence.

## Non-negotiable rules

- Do not weaken security controls merely to simplify generated code.
- Do not remove testing, review, documentation, or evidence requirements without documented rationale.
- Do not add credentials, tokens, private keys, production host names, internal identifiers, or sensitive examples.
- Use fictitious values in examples.
- Do not copy incompatible third-party content.
- Summarize external standards and link to authoritative sources.
- Do not create placeholder `AGENTS.md` files that look authoritative but contain incomplete requirements.
- Mark planned packages as planned rather than pretending they are complete.
- Do not reformat unrelated files.
- Do not modify generated or vendored files unless the task requires it.
- Do not bypass repository validation to make checks pass.

## Required governance

All changes are subject to:

- `governance/ORGANIZATION_CONTRACT.md`
- `governance/AGENT_WORKING_METHOD.md`
- `governance/RISK_CLASSIFICATION.md`
- `governance/COMPLETION_EVIDENCE.md`
- `governance/EXCEPTION_PROCESS.md`
- `governance/AI_GENERATED_CODE_POLICY.md`
- `governance/SECURE_DEVELOPMENT_POLICY.md`
- `governance/HUMAN_REVIEW_POLICY.md`

## Completion evidence

The final summary must include:

- files created, modified, or deleted
- normative behavior changed
- security impact
- compatibility impact
- validation performed
- validation not performed
- remaining limitations and risks
