# Public Access Agents

Public, reusable `AGENTS.md` standards for secure, maintainable, testable, and evidence-based AI-assisted engineering.

## Why this repository exists

AI coding agents can generate useful software quickly. They can also generate fragile code, unsafe defaults, vague documentation, weak tests, and confident completion claims unsupported by evidence. This repository provides composable standards that turn engineering discipline into explicit agent instructions.

These standards improve behavior. They do not guarantee security, correctness, compliance, or production readiness.

## Current repository version

The current repository version is defined in [`VERSION`](VERSION).

Current version: **0.9.0**

This is a pre-1.0 compatibility baseline. It is usable and versioned, but it does not yet represent the final stable compatibility commitment.

See:

- [`CHANGELOG.md`](CHANGELOG.md)
- [`RELEASE_POLICY.md`](RELEASE_POLICY.md)
- [`MATURITY_POLICY.md`](MATURITY_POLICY.md)
- [`releases/`](releases/README.md)

## Start here

1. Read the root [`AGENTS.md`](AGENTS.md).
2. Select one or more standards from the [`CATALOG.md`](CATALOG.md).
3. Select a project profile from [`profiles/`](profiles/README.md).
4. Copy the relevant language package from [`languages/`](languages/README.md).
5. Add scoped standards for applicable disciplines, platforms, and frameworks.
6. Tailor the result without weakening security, validation, testing, or completion-evidence requirements.
7. Record the repository version or tag used by the adopting project.
8. Validate the repository with the tools under [`tools/`](tools/README.md).

## Agent skill entry points

Use the collection-level skills when an agent must select and apply the repository's standards while performing engineering work:

- [`languages/SKILL.md`](languages/SKILL.md) routes advanced coding and scripting work to the applicable language packages.
- [`frameworks/SKILL.md`](frameworks/SKILL.md) composes framework and underlying language packages for application work.
- [`platforms/SKILL.md`](platforms/SKILL.md) composes platform packages for infrastructure and deployment work while preserving authorization boundaries.

The skills are progressive-disclosure routers. They load only the packages relevant to the repository and request; they do not replace root governance, scoped `AGENTS.md` files, or accountable human review.

## Repository structure

| Area | Purpose |
|---|---|
| [`governance/`](governance/README.md) | Organization-wide agent behavior, risk, exceptions, evidence, and review |
| [`disciplines/`](disciplines/README.md) | Security, architecture, testing, APIs, data, accessibility, operations, and delivery |
| [`languages/`](languages/README.md) | Copyable language-specific standards packages |
| [`platforms/`](platforms/README.md) | Containers, Kubernetes, infrastructure as code, and cloud platforms |
| [`frameworks/`](frameworks/README.md) | Framework-specific scoped agent instructions |
| [`profiles/`](profiles/README.md) | Project-type overlays such as web API, worker service, and AI agent application |
| [`templates/`](templates/README.md) | Root and nested agent files, completion evidence, threat models, ADRs, and exceptions |
| [`schemas/`](schemas/README.md) | Machine-readable evidence and manifest schemas |
| [`examples/`](examples/README.md) | Example compositions showing how standards fit together |
| [`tools/`](tools/README.md) | Repository validation, composition, and release utilities |
| [`releases/`](releases/README.md) | Versioned release notes and migration guidance |
| [`maturity-reviews/`](maturity-reviews/README.md) | Evidence-backed maturity promotion and demotion records |

## Current language packages

- PowerShell 7.x
- .NET 10 LTS
- JavaScript and TypeScript
- Python
- Java
- Go
- Rust
- Bash
- SQL
- Terraform and OpenTofu

Each language directory is independently adoptable and includes mandatory agent instructions, supporting standards, templates, examples, and a package manifest.

## Adoption model

Standards are layered rather than copied blindly:

```text
project/
├── AGENTS.md
├── standards/
├── src/
│   └── AGENTS.md
├── tests/
│   └── AGENTS.md
└── docs/
    └── AGENTS.md
```

The nearest scoped `AGENTS.md` may add stricter rules for its directory. It must not silently weaken applicable parent rules.

Adopters should record the repository version, tag, or source commit used so future upgrades can be reviewed against an explicit compatibility boundary.

## Rule format

Normative rules should include a stable identifier, a concrete requirement, expected evidence, and an exception path where applicable.

## Releases and maturity

Repository releases use Semantic Versioning as adapted by [`RELEASE_POLICY.md`](RELEASE_POLICY.md).

Release notes identify breaking, normative, editorial, tooling, security, deprecation, migration, and known-limitation changes.

Component maturity is governed by [`MATURITY_POLICY.md`](MATURITY_POLICY.md). A repository release does not automatically promote every package from `baseline` to `stable`.

`1.0.0` is reserved for a reviewed compatibility commitment that satisfies the release, ownership, adoption-testing, specialist-review, migration, and maturity gates.

## Maintainers and ownership

Repository ownership, area review, specialist-review requirements, merge authority, emergency changes, inactivity, and succession are defined in [`MAINTAINERS.md`](MAINTAINERS.md).

Review routing is defined in [`.github/CODEOWNERS`](.github/CODEOWNERS). CODEOWNERS requests review; it does not grant merge authority or replace the independence requirements in the maintainer policy.

The repository currently has one active maintainer: **Metello Zuccolini** ([@AIAllTheThingz](https://github.com/AIAllTheThingz)). Independent specialist review must come from a qualified reviewer who is not the author.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md), [`MAINTAINERS.md`](MAINTAINERS.md), [`RELEASE_POLICY.md`](RELEASE_POLICY.md), and the affected scoped `AGENTS.md` files before making changes.

## Sources

Public source frameworks and standards used as references are cataloged in [`SOURCES.md`](SOURCES.md).

## License

This repository is licensed under the Apache License, Version 2.0 (`Apache-2.0`).

Copyright 2026 Metello Zuccolini.

See [`LICENSE`](LICENSE), [`NOTICE`](NOTICE), and [`LICENSING.md`](LICENSING.md).
