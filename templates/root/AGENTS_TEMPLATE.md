---
id: TEMPLATE-ROOT-001
title: Root Agent Instructions Template
version: 0.2.0
status: baseline
template_type: root-agents
---

# Root Agent Instructions Template

## Template metadata

- Template ID: `TEMPLATE-ROOT-AGENTS-001`
- Template version: `0.2.0`
- Intended destination: repository-root `AGENTS.md`

> Replace every documented placeholder before adoption. Remove this note after validation.

## Project identity

- Project: `{{PROJECT_NAME}}`
- Purpose: {{PROJECT_PURPOSE}}
- Non-goals: {{PROJECT_NON_GOALS}}

## Authority and precedence

These project instructions operate under applicable law, contracts, authorized organization requirements, root governance, and selected shared standards.

More-specific nested `AGENTS.md` files may specialize or strengthen local requirements. They may not silently weaken parent governance, authorization, security, evidence, or review controls.

## Selected standards

- Primary profile: `{{PRIMARY_PROFILE}}`
- Secondary profiles: {{SECONDARY_PROFILES}}
- Language packages: {{LANGUAGE_PACKAGES}}
- Discipline packages: {{DISCIPLINE_PACKAGES}}
- Framework packages: {{FRAMEWORK_PACKAGES}}
- Platform packages: {{PLATFORM_PACKAGES}}

## Project facts

- Supported runtimes: {{SUPPORTED_RUNTIMES}}
- Deployment environments: {{DEPLOYMENT_ENVIRONMENTS}}
- Sensitive data: {{SENSITIVE_DATA}}
- Privileged operations: {{PRIVILEGED_OPERATIONS}}
- Compatibility commitments: {{COMPATIBILITY_COMMITMENTS}}
- Required reviewers: {{REQUIRED_REVIEWERS}}

Agents must inspect repository evidence before relying on any project fact. Unknown facts must be reported as unknown rather than invented.

## Required working method

1. Inspect relevant instructions, code, configuration, tests, documentation, and evidence before editing.
2. Confirm scope and classify risk.
3. Identify authorization requirements before privileged, destructive, bulk, production, or external actions.
4. Plan the smallest coherent change.
5. Preserve compatibility unless an approved migration says otherwise.
6. Implement with secure defaults and explicit failure behavior.
7. Run applicable validation.
8. Record commands, results, artifacts, checks not run, limitations, and residual risk.
9. Obtain accountable review where required.
10. Claim completion only at the level supported by evidence.

## Validation

Required project validation:

{{VALIDATION_COMMANDS}}

Validation must identify the environment and artifact tested. A successful command does not by itself prove security, recovery, operational readiness, or production acceptance.

## Evidence

Completion and review evidence is stored at:

`{{EVIDENCE_LOCATION}}`

Evidence must distinguish proposed, authorized, implemented, validated, reviewed, approved, operationally verified, and closed states.

## Prohibited behavior

- Do not expose secrets, private keys, credentials, tokens, or sensitive evidence.
- Do not bypass authorization, review, policy, or validation.
- Do not perform destructive or production-affecting actions without explicit authority.
- Do not broaden target scope implicitly.
- Do not fabricate commands, outputs, citations, test results, reviewers, approvals, or project facts.
- Do not suppress failures to obtain a green result.
- Do not weaken shared standards through nested instructions.
- Do not claim production readiness from implementation evidence alone.

## Escalation

Stop and escalate when:

- instructions conflict materially
- required project facts are unavailable
- scope exceeds authorization
- validation produces unexplained failures
- rollback or recovery is not credible
- the requested action creates unacceptable security, privacy, safety, or operational risk
