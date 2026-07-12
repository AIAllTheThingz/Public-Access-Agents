---
id: EX-WRK-TAILOR-001
title: Worker Service Composition Example Tailoring Decisions
version: 0.1.0
status: baseline
---
# Worker Service Composition Example Tailoring Decisions

## Purpose

This record shows how shared standards are tailored to the fictitious **Worker Service Composition Example** project.

Tailoring records project facts and stricter requirements. It must not quietly delete inconvenient controls.

## Declared project facts

- Project name: `example-worker-service`
- Profile: `WORKER_SERVICE`
- Risk: `moderate`
- Production environments: none
- Production access: prohibited
- Data: The fictitious worker processes job identifiers and synthetic payloads. Real customer, patient, employee, or credential data is prohibited.
- Owners: fictitious maintainers
- Approval authority: not assigned
- Evidence storage: this example directory
- Exception process: no active exceptions

## Scope

In scope:

- standards composition
- root and nested agent instructions
- architecture and trust-boundary documentation
- risk and test planning
- operations and completion-evidence examples
- schema-shaped JSON evidence

Out of scope:

- deployable application code
- production credentials, endpoints, accounts, clusters, databases, or users
- legal, regulatory, contractual, or compliance approval
- production performance, availability, recovery, or incident evidence
- real artifact publication

## Tailored requirements

- All example values must be fictitious.
- No state-changing production operation is permitted.
- Example evidence must be clearly illustrative.
- `not-run` must be used when a validation was not executed.
- Root and nested instructions must remain consistent.
- Any real adoption must replace project facts and evidence.
- The example must pass repository structure and link validation.

## Conditionally applicable controls

Controls tied to real deployment, identity, data classification, recovery, performance, or external systems remain illustrative until an adopting project supplies reviewed facts.

## Inapplicable controls

No control is marked permanently inapplicable. Controls omitted from the manifest are omitted only for the current example shape and must be reconsidered when scope changes.

## Open decisions

- Exact runtime patch versions
- Hosting and deployment environment
- Identity and secret providers
- Data-store technology
- Monitoring backend
- Release and approval workflow
- Support ownership
- Recovery objectives
- Compliance obligations

## Exceptions

None.

## Review and expiration

This tailoring record must be reviewed when the example's manifest, architecture, risk, or directory structure changes.
