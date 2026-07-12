# JavaScript and TypeScript Agent Standard Package

This package provides a project-agnostic standards framework for current
JavaScript and TypeScript development.

## Baseline

- Node.js 24 LTS
- TypeScript 6.0
- ES2025
- ECMAScript modules
- pnpm 11
- ESLint flat configuration
- Prettier
- Vitest reference test configuration

## Structure

```text
JavaScript-TypeScript-Agent-Standard/
├── AGENTS.md
├── README.md
├── MANIFEST.md
├── standards/
├── templates/
└── examples/
```

The root `AGENTS.md` contains mandatory rules and instructs coding agents to
read the relevant supporting standards.

## Adoption

Copy the package into the root of a JavaScript or TypeScript repository.

Review and adjust:

- Exact Node.js patch
- Package-manager patch
- TypeScript compiler options
- Browser support
- Framework requirements
- Test framework package versions
- Deployment requirements
- Organization security and compliance requirements

The templates are reference starting points. Replace example namespaces, package
names, and placeholders before use.

## Suggested Validation

```bash
node --version
pnpm --version
pnpm install --frozen-lockfile
pnpm format:check
pnpm lint
pnpm typecheck
pnpm test
pnpm build
pnpm audit
```
