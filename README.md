# Public Access Agents

Public, reusable `AGENTS.md` standards designed to reduce low-quality AI-generated code, make security part of implementation, and require evidence before an agent claims work is complete.

## Purpose

AI coding agents are capable of producing useful software quickly, but speed without engineering discipline produces fragile code, hidden security assumptions, weak testing, and completion claims unsupported by evidence.

This repository provides composable standards that require agents to treat the following as implementation requirements rather than optional cleanup:

- secure defaults
- input validation
- least privilege
- dependency and supply-chain review
- maintainable code
- meaningful documentation
- testing and static analysis
- runtime compatibility
- operational readiness
- honest completion evidence

These standards reduce slop. They do not guarantee that software is secure, correct, compliant, or production ready.

## Available language standards

| Standard | Baseline | Location |
|---|---|---|
| PowerShell | PowerShell 7.x | [`languages/powershell`](languages/powershell) |
| .NET | .NET 10 LTS | [`languages/dotnet`](languages/dotnet) |
| JavaScript and TypeScript | Node.js 24 LTS and TypeScript 6.0 | [`languages/javascript-typescript`](languages/javascript-typescript) |

Each language directory contains:

- a root `AGENTS.md`
- detailed supporting standards
- implementation templates
- configuration examples
- a manifest

## How to use a package

1. Select the language package that matches the repository.
2. Copy its `AGENTS.md`, `standards`, and applicable templates into the target repository.
3. Review runtime versions, package versions, operating-system support, and organization-specific requirements.
4. Remove templates that do not apply.
5. Add project-specific requirements without weakening the inherited security or evidence requirements.
6. Keep the standard versioned and review changes through pull requests.

The language `AGENTS.md` files explicitly require coding agents to read their supporting standards.

## Layered standards

A mature repository can combine:

```text
Repository/
├── AGENTS.md
├── standards/
├── src/
│   └── AGENTS.md
├── tests/
│   └── AGENTS.md
└── docs/
    └── AGENTS.md
```

Use nested `AGENTS.md` files only when rules apply to a specific directory. Do not duplicate the entire root standard into every folder.

## Repository direction

Planned cross-discipline standards include:

- core agent governance
- application security
- testing and quality engineering
- software supply chain
- CI/CD and GitHub Actions
- API and integration engineering
- database and data engineering
- infrastructure as code
- containers and Kubernetes
- observability and site reliability
- accessibility and privacy
- AI and agentic systems

See [`ROADMAP.md`](ROADMAP.md).

## Contributing

Contributions should improve enforceability, clarity, evidence requirements, security awareness, or portability. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting changes.

## Security reports

Do not disclose exploitable security issues in a public issue. Follow [`SECURITY.md`](SECURITY.md).

## License

A repository license has not yet been selected. Until a license is added, normal copyright restrictions apply even though the repository is public.
