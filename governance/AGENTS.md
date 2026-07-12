---
id: GOV-AGENT-001
title: Governance Agent Instructions
version: 0.2.0
status: baseline
---

# Governance Agent Instructions

## Purpose

These instructions govern agents that create, modify, review, organize, or document governance policies, templates, decision records, and examples in this directory.

Governance changes can alter authority, review, risk, exceptions, security, and production gates across the entire repository. Treat them as policy changes, not casual editorial work.

## Scope

These instructions apply to:

- governance policies
- policy maps and operating-model documents
- adoption and lifecycle guidance
- governance templates
- governance examples and machine-readable records
- references from root catalog, manifest, roadmap, profiles, packages, and examples

## Instruction precedence

1. Applicable legal, contractual, safety, security, and repository obligations
2. Explicit authorized user requirements
3. Root repository `AGENTS.md`
4. This governance `AGENTS.md`
5. The policy being modified
6. Repository conventions
7. General agent preferences

Report material conflicts. Do not resolve authority disputes by choosing whichever instruction is easiest to edit.

## Required reading

Before modifying governance:

- [README.md](README.md)
- [ORGANIZATION_CONTRACT.md](ORGANIZATION_CONTRACT.md)
- [AGENT_WORKING_METHOD.md](AGENT_WORKING_METHOD.md)
- [RISK_CLASSIFICATION.md](RISK_CLASSIFICATION.md)
- [COMPLETION_EVIDENCE.md](COMPLETION_EVIDENCE.md)
- [EXCEPTION_PROCESS.md](EXCEPTION_PROCESS.md)
- [HUMAN_REVIEW_POLICY.md](HUMAN_REVIEW_POLICY.md)
- [POLICY_MAP.md](POLICY_MAP.md)
- [POLICY_LIFECYCLE.md](POLICY_LIFECYCLE.md)

Read additional affected policies and templates before editing them.

## Non-negotiable editing rules

- Preserve stable document and rule identifiers unless an approved breaking change requires migration.
- Do not invent legal requirements, organizational authority, approvers, risk appetite, retention periods, service levels, or compliance claims.
- Keep normative requirements distinguishable from explanation and examples.
- State applicability, evidence, decision gates, roles, and exception boundaries clearly.
- Do not create circular or contradictory precedence.
- Do not make an exception process broad enough to waive authorization, evidence, law, or safety.
- Do not let an agent approve its own work, risk, exception, or production use.
- Do not weaken a policy silently through a template or example.
- Keep examples fictitious and explicitly non-production.
- Do not expose vulnerability details, credentials, personal data, or internal identifiers.
- Update cross-references, manifests, templates, examples, and migration guidance with policy changes.
- Record checks not run and limitations.

## Required working method

1. Identify the policy purpose, affected decisions, and downstream consumers.
2. Inspect all cross-references and dependent records.
3. Classify the governance change as editorial, clarifying, additive, behavior-changing, breaking, security-sensitive, or authority-changing.
4. Define acceptance criteria and migration impact.
5. Make the smallest coherent policy change.
6. Preserve existing rules unless change is explicit and reviewed.
7. Update templates and examples so they do not contradict the policy.
8. Validate links, IDs, JSON, and manifests.
9. Review the final diff for hidden weakening, conflicting authority, unresolved placeholders, and unsupported claims.
10. Record evidence, compatibility impact, and limitations.

## Stable identifiers

Document IDs and rule IDs are public governance contracts. Renaming them can break references, evidence records, automation, and exception tracking.

When a rule must change materially:

- prefer clarifying the existing rule when semantics remain compatible
- add a new rule for new behavior
- deprecate rather than silently repurpose when meaning changes
- document migration when an identifier is replaced
- update every reference and example
- state whether prior approvals or exceptions remain valid

## Policy-quality requirements

A governance policy should define:

- purpose
- applicability
- accountable roles
- normative rules
- expected evidence
- decision gates
- prohibited shortcuts
- exception boundaries
- review triggers
- completion or closure criteria
- related policies and templates

Avoid vague phrases such as “use best practices,” “ensure compliance,” or “review as needed” without defining responsibility and evidence.

## Authority and approval safety

Governance text must not imply that:

- an AI system has legal or organizational authority
- a repository file grants production access
- a reviewer automatically has approval authority
- approval survives material scope change
- silence equals approval
- an exception erases risk
- a passing tool proves readiness
- a policy creates compliance by itself

## Validation

Run:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```

Also perform a human-readable review for:

- grammar and ambiguity
- policy conflicts
- incorrect relative links
- unsupported authority
- inconsistent evidence states
- unresolved placeholders
- duplicated or diverging requirements
- accidental weakening
- false compliance or production claims

## Completion gate

Governance work is incomplete until:

- affected IDs and links are valid
- policy and templates agree
- examples remain explicitly fictitious
- migration or compatibility impact is stated
- downstream references are updated
- no sensitive information is exposed
- validation evidence is recorded
- unresolved authority, risk, or exception questions are disclosed
