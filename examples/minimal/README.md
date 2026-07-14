---
id: EX-MIN-README-001
title: Minimal CLI Composition Example
version: 0.1.0
status: baseline
---
# Minimal CLI Composition Example

## Purpose

A low-risk PowerShell command-line utility used to demonstrate the smallest credible standards composition.

This directory demonstrates a complete standards composition, including selection rationale, project tailoring, scoped agent instructions, architecture, risk, tests, operations, and schema-shaped evidence. It contains no production application code.

## Fictitious project summary

- **Profile:** [CLI_TOOL](../../profiles/CLI_TOOL.md)
- **Risk classification:** `low`
- **Implementation status:** documentation-only example
- **Production readiness:** not assessed and not claimed
- **Data:** No personal or regulated data is intentionally processed. Example values are fictitious.

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
minimal/
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

[CLI_TOOL](../../profiles/CLI_TOOL.md) provides the project-type overlay. It supplements rather than replaces governance, language, discipline, framework, platform, virtualization, operating-system, and networking standards.

## Selected languages

- [PowerShell](../../languages/powershell/)

Language packages define runtime, coding, dependency, testing, security, documentation, and completion expectations for implementation work.

## Selected disciplines

- [Testing and Quality Engineering](../../disciplines/testing/)
- [Documentation](../../disciplines/documentation/)
- [Software Supply Chain](../../disciplines/supply-chain/)

The selection rationale is documented in [`composition/STANDARDS_SELECTION.md`](composition/STANDARDS_SELECTION.md). Omitting a discipline requires a reason; absence from a job title is not a reason.

## Selected platforms

- None selected in this example.

## Selected frameworks

- None selected in this example.

## Selected virtualization

- None selected; the example does not administer a hypervisor, manager, host, or virtual machine.

## Selected operating systems

- None selected; PowerShell is used as an implementation language, but the example performs no operating-system administration.

## Selected networking

- None selected; the example does not configure network devices, controllers, routing, switching, or fabrics.

## Architecture summary

- **Command entry point:** Accepts explicit parameters and returns structured output.
- **Core operation:** Performs one bounded, non-destructive transformation.
- **Validation layer:** Rejects ambiguous input before work begins.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for responsibilities, dependencies, trust boundaries, state, and failure behavior.

## Trust boundaries

- User-supplied command-line arguments
- Local file paths supplied by the user

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

- `src/AGENTS.md`: Implementation scope
- `tests/AGENTS.md`: Test scope
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

- No additional risk-specific documents are required beyond the common set.

## Validation baseline

The example proposes the following project validations:

- PowerShell syntax parsing
- PSScriptAnalyzer or repository-equivalent static analysis
- Pester unit tests
- Dry-run behavior for any state-changing extension

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

- The example contains no executable application code.
- Runtime, operating-system, packaging, and signing choices remain project decisions.
- Low risk does not exempt the project from input validation, tests, or truthful evidence.

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

This example is educational. It does not implement minimal cli composition example, prove the selected controls, validate a deployment, or replace accountable engineering review.
