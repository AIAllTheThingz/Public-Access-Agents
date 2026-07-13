# Public Access Agents

Public, reusable `AGENTS.md` standards for secure, maintainable, testable, and evidence-based AI-assisted engineering.

## Why this repository exists

AI coding agents can generate useful software quickly. They can also generate fragile code, unsafe defaults, vague documentation, weak tests, and confident completion claims unsupported by evidence. This repository provides composable standards that turn engineering discipline into explicit agent instructions.

These standards improve behavior. They do not guarantee security, correctness, compliance, or production readiness.

## Start here

1. Read the root [`AGENTS.md`](AGENTS.md).
2. Select one or more standards from the [`CATALOG.md`](CATALOG.md).
3. Select a project profile from [`profiles/`](profiles/README.md).
4. Copy the relevant language package from [`languages/`](languages/README.md).
5. Add scoped standards for applicable disciplines, platforms, and frameworks.
6. Tailor the result without weakening security, validation, testing, or completion-evidence requirements.
7. Validate the repository with the tools under [`tools/`](tools/README.md).

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
| [`tools/`](tools/README.md) | Repository validation and composition utilities |

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

## Rule format

Normative rules should include a stable identifier, a concrete requirement, expected evidence, and an exception path where applicable.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md), and the affected scoped `AGENTS.md` files before making changes.

## Sources

Public source frameworks and standards used as references are cataloged in [`SOURCES.md`](SOURCES.md).

## License

This repository is licensed under the Apache License, Version 2.0 (`Apache-2.0`).

Copyright 2026 Metello Zuccolini.

See [`LICENSE`](LICENSE), [`NOTICE`](NOTICE), and [`LICENSING.md`](LICENSING.md).
