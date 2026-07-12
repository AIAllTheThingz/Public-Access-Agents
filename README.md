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

Additional language packages are tracked as planned work in [`languages/README.md`](languages/README.md) and [`ROADMAP.md`](ROADMAP.md).

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

Normative rules should include:

- a stable rule identifier
- a concrete requirement
- expected evidence
- an exception path where applicable

Example identifiers:

- `GOV-WORK-001`
- `SEC-INPUT-001`
- `TEST-UNIT-001`
- `OPS-OBS-001`
- `ACC-WCAG-001`

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md), and the affected scoped `AGENTS.md` files before making changes.

## Sources

Public source frameworks and standards used as references are cataloged in [`SOURCES.md`](SOURCES.md).

## License

A repository license has not yet been selected. Until one is added, normal copyright restrictions apply even though the repository is public.
