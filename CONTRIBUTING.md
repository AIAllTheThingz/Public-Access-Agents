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
- add a well-scoped discipline, language, platform, virtualization, operating-system, networking, or framework package

## Before opening a pull request

1. Read the root `AGENTS.md`.
2. Read [`MAINTAINERS.md`](MAINTAINERS.md) and identify the applicable area owner and review class.
3. Read [`RELEASE_POLICY.md`](RELEASE_POLICY.md) and [`MATURITY_POLICY.md`](MATURITY_POLICY.md) when the change affects compatibility, versions, deprecations, maturity, tags, release notes, or release automation.
4. Read the affected language, discipline, platform, virtualization, operating-system, networking, framework, profile, schema, template, or tool standards.
5. Keep the change focused.
6. Explain whether the change is editorial, normative, compatibility-related, security-related, breaking, or release-related.
7. Identify the expected patch, minor, major, prerelease, or no-release impact.
8. Identify compatibility, security, ownership, and specialist-review impact.
9. Update examples, templates, schemas, manifests, tests, changelog entries, and migration notes as applicable.
10. Run the permanent validation pipeline.
11. Confirm no secrets or production-specific identifiers are present.
12. Confirm all third-party material is compatible with the repository license and carries required attribution.

## Pull request description

Include:

- what changed
- why it changed
- who or what is affected
- change classification and risk
- repository version and release impact
- applicable CODEOWNER and area owner
- required specialist review and whether it is independent from the author
- security impact
- compatibility impact
- changelog, release-note, deprecation, and migration impact
- validation performed
- validation not performed
- remaining limitations

## Versioning and changelog

Changes with user-visible or adopter-visible impact must update [`CHANGELOG.md`](CHANGELOG.md) under `Unreleased` or the target release section.

Normative and breaking changes must identify affected rules, schemas, templates, tools, packages, or stable paths.

A change must not be labeled editorial when it changes requirement strength, scope, authority, compatibility, evidence, completion criteria, tool behavior, or generated output.

Deprecations and removals must follow the windows and migration requirements in [`RELEASE_POLICY.md`](RELEASE_POLICY.md).

## Release changes

A release pull request must update:

- `VERSION`
- `CHANGELOG.md`
- `releases/<VERSION>.md`
- `releases/migrations/<VERSION>.md`
- affected package, schema, template, tool, and root manifests

Release automation, release tooling, breaking releases, and `1.0.0` require the specialist review defined by `MAINTAINERS.md`.

Tags are created only after the reviewed release commit is merged to `main`. Published tags must not be moved or recreated.

## Maturity changes

Maturity promotion, demotion, or deprecation must follow [`MATURITY_POLICY.md`](MATURITY_POLICY.md) and include a review record under [`maturity-reviews/`](maturity-reviews/README.md).

Promotion to `stable` requires adoption, compatibility, source, validation, ownership, and independent-review evidence. A repository version bump does not automatically promote a component.

## Review and merge

Review and merge authority are defined by [`MAINTAINERS.md`](MAINTAINERS.md). Review routing is defined by [`.github/CODEOWNERS`](.github/CODEOWNERS).

CODEOWNERS does not grant merge authority or prove that a reviewer is independent or qualified. Sensitive normative changes involving governance, security, schemas, executable tools, CI permissions, release automation, or breaking releases require the specialist review defined in the maintainer policy.

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
