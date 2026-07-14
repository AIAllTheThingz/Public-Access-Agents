---
id: EX-WRK-README-001
title: Worker Service Composition Example
version: 0.1.0
status: baseline
---
# Worker Service Composition Example

## Purpose

A moderate-risk TypeScript worker that consumes messages, calls external systems, and runs in Kubernetes.

This directory demonstrates a complete standards composition, including selection rationale, project tailoring, scoped agent instructions, architecture, risk, tests, operations, and schema-shaped evidence. It contains no production application code.

## Fictitious project summary

- **Profile:** [WORKER_SERVICE](../../profiles/WORKER_SERVICE.md)
- **Risk classification:** `moderate`
- **Implementation status:** documentation-only example
- **Production readiness:** not assessed and not claimed
- **Data:** The fictitious worker processes job identifiers and synthetic payloads. Real customer, patient, employee, or credential data is prohibited.

## Learning goals

Use this example to understand how to:

- select standards based on project shape and risk
- document why each package applies
- convert shared standards into project-specific instructions
- use nested `AGENTS.md` files to narrow scope
- describe architecture and trust boundaries without inventing environment facts
- define validation before implementation
- record limitations, checks not run, and residual risk
- use repository schemas for machine-readable evidence

## Example structure

```text
worker-service/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── project-manifest.json
├── composition/
│   ├── STANDARDS_SELECTION.md
│   └── TAILORING_DECISIONS.md
├── docs/
│   ├── AGENTS.md
│   ├── ARCHITECTURE.md
│   ├── RISK_ASSESSMENT.md
│   ├── TEST_STRATEGY.md
│   ├── OPERATIONS.md
│   └── COMPLETION_EVIDENCE.md
├── evidence/
│   ├── completion-result.example.json
│   ├── test-evidence.example.json
│   └── artifact-record.example.json
└── scoped directories containing nested AGENTS.md files
```

## Selected profile

[WORKER_SERVICE](../../profiles/WORKER_SERVICE.md) provides the project-type overlay. It supplements rather than replaces governance, language, discipline, framework, platform, virtualization, operating-system, and networking standards.

## Selected languages

- [JavaScript and TypeScript](../../languages/javascript-typescript/)

Language packages define runtime, coding, dependency, testing, security, documentation, and completion expectations for implementation work.

## Selected disciplines

- [Architecture and System Design](../../disciplines/architecture/)
- [Testing and Quality Engineering](../../disciplines/testing/)
- [Integration Engineering](../../disciplines/integration/)
- [Application Security](../../disciplines/application-security/)
- [Observability](../../disciplines/observability/)
- [Site Reliability Engineering](../../disciplines/sre/)
- [CI/CD](../../disciplines/ci-cd/)
- [Software Supply Chain](../../disciplines/supply-chain/)
- [Documentation](../../disciplines/documentation/)
- [Release Engineering](../../disciplines/release-engineering/)

The selection rationale is documented in [`composition/STANDARDS_SELECTION.md`](composition/STANDARDS_SELECTION.md). Omitting a discipline requires a reason; absence from a job title is not a reason.

## Selected platforms

- [Containers](../../platforms/containers/)
- [Kubernetes](../../platforms/kubernetes/)

## Selected frameworks

- None selected in this example.

## Selected virtualization

- None selected; the example operates through Kubernetes and does not administer the underlying hypervisor or nodes.

## Selected operating systems

- None selected; host and node operating-system ownership remains outside the fictitious worker scope.

## Selected networking

- None selected; Kubernetes service networking is covered by the platform package, while external network-device control planes are out of scope.

## Architecture summary

- **Message consumer:** Receives work from a fictitious queue.
- **Processing pipeline:** Validates, transforms, and routes work.
- **Integration adapters:** Call external APIs through bounded interfaces.
- **Checkpoint and retry handling:** Supports idempotency, duplicate delivery, and recovery.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for responsibilities, dependencies, trust boundaries, state, and failure behavior.

## Trust boundaries

- Message broker
- External APIs
- Configuration and secret providers
- Container and Kubernetes control planes

Every real adoption must replace these fictitious boundaries with reviewed project facts.

## Root instructions

[`AGENTS.md`](AGENTS.md) defines:

- instruction precedence
- allowed and prohibited scope
- project facts
- mandatory working method
- safety and evidence requirements
- change-classification and completion gates
- links to the selected standards packages

## Nested instructions

- `src/worker/AGENTS.md`: Worker implementation scope
- `src/integrations/AGENTS.md`: Integration adapter scope
- `tests/AGENTS.md`: Test scope
- `deploy/AGENTS.md`: Deployment scope
- `docs/AGENTS.md`: Documentation scope

Nested instructions add local constraints. They do not weaken root or shared standards.

## Composition and tailoring

- [`STANDARDS_SELECTION.md`](composition/STANDARDS_SELECTION.md) explains why packages were selected.
- [`TAILORING_DECISIONS.md`](composition/TAILORING_DECISIONS.md) records project facts, owners, assumptions, inapplicable controls, and unresolved decisions.
- [`project-manifest.json`](project-manifest.json) provides the machine-readable package selection.

A real project must review all three together. Contradictory narrative and manifest files are not “flexibility”; they are drift.

## Common documentation

- [`ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- [`RISK_ASSESSMENT.md`](docs/RISK_ASSESSMENT.md)
- [`TEST_STRATEGY.md`](docs/TEST_STRATEGY.md)
- [`OPERATIONS.md`](docs/OPERATIONS.md)
- [`COMPLETION_EVIDENCE.md`](docs/COMPLETION_EVIDENCE.md)

Additional example-specific documents:

- [`THREAT_MODEL.md`](docs/THREAT_MODEL.md)
- [`DATA_HANDLING.md`](docs/DATA_HANDLING.md)
- [`RELEASE_PLAN.md`](docs/RELEASE_PLAN.md)

## Validation baseline

The example proposes the following project validations:

- Frozen dependency installation
- Formatting, linting, type checking, unit tests, and integration tests
- Duplicate-delivery and retry tests
- Graceful shutdown and cancellation tests
- Container and Kubernetes manifest validation

The commands and outcomes in this example are illustrative. An adopting project must use actual repository commands and record whether each check passed, failed, or was not run.

## Evidence files

- [`completion-result.example.json`](evidence/completion-result.example.json) follows the [completion-result schema](../../schemas/completion-result.schema.json).
- [`test-evidence.example.json`](evidence/test-evidence.example.json) follows the [test-evidence schema](../../schemas/test-evidence.schema.json).
- [`artifact-record.example.json`](evidence/artifact-record.example.json) follows the [artifact-record schema](../../schemas/artifact-record.schema.json).

Example digests, commits, runs, timestamps, and reviewers are fictitious or explicitly marked as not verified.

## How to adapt this example

1. Replace the fictitious project name and summary.
2. Reclassify risk using actual impact and reversibility.
3. Re-select the profile, languages, disciplines, frameworks, platforms, virtualization systems, operating systems, and networking systems.
4. Replace architecture and trust-boundary assumptions with reviewed facts.
5. Define actual owners and approval paths.
6. Replace example commands with repository commands.
7. Define real environments and test data.
8. Add or remove nested scopes based on the real directory structure.
9. Replace example evidence with actual results.
10. Record exceptions, limitations, and checks not run.
11. Validate the repository.
12. Obtain accountable review.

## What not to copy

Do not copy:

- fictitious names or identifiers as though they were approved
- example risk classifications without reassessment
- placeholder ownership or reviewer values
- example evidence as proof
- framework, platform, virtualization, operating-system, or networking selections that do not apply
- operational claims that were not tested
- any statement implying certification, compliance, or production approval

## Known limitations

- No real broker, external API, or cluster is used.
- Throughput, backpressure, disaster recovery, and on-call procedures are illustrative.
- Exactly-once delivery is not claimed.

## Review checklist

Before using the composition:

- [ ] The manifest matches the actual project.
- [ ] Every selected standard is applicable.
- [ ] Every omitted standard has a defensible reason.
- [ ] Root and nested instructions do not conflict.
- [ ] Architecture and trust boundaries are accurate.
- [ ] Risk and evidence requirements are proportionate.
- [ ] Validation commands are executable.
- [ ] Example evidence has been replaced.
- [ ] No secrets or sensitive production values are present.
- [ ] Limitations and residual risks are explicit.
- [ ] Accountable reviewers are identified.

## Validation of this standards repository

From the repository root:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```

## Non-production warning

This example is educational. It does not implement worker service composition example, prove the selected controls, validate a deployment, or replace accountable engineering review.
