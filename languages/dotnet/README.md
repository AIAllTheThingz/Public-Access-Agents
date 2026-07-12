# .NET Agent Standard Package

This package provides a project-agnostic standards framework for current .NET LTS development.

## Baseline

- .NET 10 LTS
- `net10.0`
- Stable C#
- `dotnet` CLI
- No preview features by default

## Structure

```text
DotNet-Agent-Standard/
├── AGENTS.md
├── README.md
├── standards/
├── templates/
└── examples/
```

The root `AGENTS.md` contains the mandatory rules and instructs coding agents to read the relevant supporting standards.

## Adoption

Copy the package into the root of a .NET repository.

Review and adjust:

- Minimum SDK feature band
- Analyzer severity
- Test framework package versions
- Deployment-specific requirements
- Database provider requirements
- Organization-specific security and compliance requirements

Do not add production secrets to the examples.

## Suggested First Validation

```bash
dotnet --info
dotnet restore
dotnet format --verify-no-changes
dotnet build --no-restore
dotnet test --no-build
dotnet package list --vulnerable --include-transitive
```

The templates are reference starting points. Replace example namespaces, types, and placeholders before using them in an application.
