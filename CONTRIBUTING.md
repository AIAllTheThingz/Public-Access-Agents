# Contributing

Contributions are welcome when they make the standards clearer, safer, more enforceable, or easier to adopt.

## Contribution principles

A useful change should do at least one of the following:

- prevent a recurring implementation failure
- require evidence for a completion claim
- move security into normal development
- improve runtime or platform accuracy
- strengthen testing or operational readiness
- remove ambiguity
- improve portability
- reduce unnecessary duplication
- add a well-scoped discipline or language package

## Before opening a pull request

1. Read the root `AGENTS.md`.
2. Read [`MAINTAINERS.md`](MAINTAINERS.md) and identify the applicable area owner and review class.
3. Read the affected language, discipline, platform, framework, profile, schema, template, or tool standards.
4. Keep the change focused.
5. Explain whether the change is editorial, normative, compatibility-related, security-related, or breaking.
6. Identify compatibility, security, ownership, and specialist-review impact.
7. Update examples, templates, schemas, manifests, and tests as applicable.
8. Run the permanent validation pipeline.
9. Confirm no secrets or production-specific identifiers are present.
10. Confirm all third-party material is compatible with the repository license and carries required attribution.

## Pull request description

Include:

- what changed
- why it changed
- who or what is affected
- change classification and risk
- applicable CODEOWNER and area owner
- required specialist review and whether it is independent from the author
- security impact
- compatibility impact
- validation performed
- validation not performed
- remaining limitations

## Review and merge

Review and merge authority are defined by [`MAINTAINERS.md`](MAINTAINERS.md). Review routing is defined by [`.github/CODEOWNERS`](.github/CODEOWNERS).

CODEOWNERS does not grant merge authority or prove that a reviewer is independent or qualified. Sensitive normative changes involving governance, security, schemas, executable tools, CI permissions, or breaking releases require the specialist review defined in the maintainer policy.

The current sole maintainer may self-merge only where the maintainer policy explicitly permits it. Self-review must not be represented as independent specialist review.

## Standards writing

Prefer requirements that are:

- specific
- testable
- evidence-based
- proportionate to risk
- technology-aware
- honest about limitations

Avoid vague instructions such as "follow best practices" without defining the expected behavior or evidence.

## External sources

Use authoritative public sources where possible.

Do not copy large sections of third-party material. Summarize requirements and provide attribution.

## Contribution license

This repository is licensed under the Apache License, Version 2.0 (`Apache-2.0`). See [`LICENSE`](LICENSE) and [`LICENSING.md`](LICENSING.md).

Unless explicitly stated otherwise, any contribution intentionally submitted for inclusion in this repository is provided under Apache-2.0, consistent with Section 5 of the license and without additional terms or conditions.

A submission that is not intended as a contribution must be conspicuously marked `Not a Contribution`. Do not submit third-party material whose license is incompatible with Apache-2.0 or whose required notices and attribution cannot be preserved.
