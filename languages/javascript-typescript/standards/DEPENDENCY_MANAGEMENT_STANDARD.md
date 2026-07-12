# JavaScript and TypeScript Dependency Management Standard

## Purpose

This standard governs Node.js versions, package managers, registries,
dependencies, lockfiles, lifecycle scripts, build plugins, and package
publication.

Dependencies are code somebody else wrote, published, and then quietly handed
you the pager for.

## Package Manager

The reference package manager is pnpm 11.

Requirements:

- Pin the package-manager version in `package.json`.
- Commit `pnpm-lock.yaml`.
- Use `pnpm install --frozen-lockfile` in CI.
- Use workspaces deliberately.
- Preserve pnpm security defaults unless an exception is documented.
- Do not switch package managers during unrelated work.

Existing repositories may retain npm, Yarn, or another approved manager.

## Runtime Pinning

Declare:

- Node engine
- Package-manager version
- Runtime file such as `.node-version` or `.nvmrc`

Keep the Node patch current.

Do not pin production to an end-of-life release.

## Registry Trust

- Use trusted registries.
- Minimize registry count.
- Configure authentication through secrets.
- Do not commit tokens.
- Review dependency-confusion risk.
- Use package-source scopes or mapping where appropriate.
- Do not disable TLS validation.

## Version Ranges

- Avoid floating `latest` in committed production dependencies.
- Use deliberate semver ranges.
- Pin toolchains when reproducibility requires it.
- Review major updates.
- Keep related framework packages compatible.
- Do not update unrelated packages during a targeted change.

## Lockfiles

The lockfile is part of the source-controlled dependency contract.

Review lockfile changes for:

- Unexpected packages
- Registry changes
- Integrity changes
- Native binaries
- Lifecycle scripts
- Major transitive changes
- Duplicate versions
- Git or URL dependencies

Do not regenerate lockfiles casually.

## Lifecycle Scripts

Dependency lifecycle scripts can execute code during installation.

Requirements:

- Review packages requiring builds.
- Use pnpm allow-build controls.
- Do not approve broad arbitrary build execution.
- Document required native builds.
- Avoid packages using unnecessary postinstall behavior.
- Run installation in controlled CI.

## Dependency Selection

Before adding a package, review:

- Necessity
- Maintenance
- Release cadence
- Security history
- License
- Download provenance
- Maintainer changes
- Transitive dependencies
- Bundle impact
- Runtime compatibility
- Browser compatibility
- ESM compatibility
- Types
- Tree shaking
- Native code

Do not add a package to avoid a few lines of clear built-in code.

## Auditing

Run:

```bash
pnpm audit
```

Also review:

- Direct and transitive packages
- Registry advisories
- Runtime advisories
- Build-plugin advisories
- Browser supply-chain exposure

For each finding:

- Identify affected path.
- Determine runtime reachability.
- Upgrade or remove where practical.
- Document temporary exceptions.
- Do not suppress broadly.

## Package Updates

A package update should include:

- Reason
- Old and new versions
- Release-note review
- Breaking-change review
- Security impact
- Test results
- Bundle or runtime impact
- Migration
- Rollback consideration

Keep large dependency waves separate from features.

## Build Tools and Plugins

Build plugins execute trusted code.

Review:

- Origin
- Maintenance
- Filesystem access
- Environment access
- Network access
- Generated output
- Source-map behavior
- CI compatibility

Do not install arbitrary plugins because a tutorial did.

## Workspaces and Monorepos

Define:

- Package boundaries
- Allowed dependencies
- Versioning
- Release strategy
- Build order
- Shared configuration
- CI scope
- Cache behavior

Do not rely on undeclared workspace leakage.

## Package Publication

Before publishing:

- Review package files.
- Define `exports`.
- Define `types`.
- Define supported runtime.
- Exclude secrets and internal files.
- Run tests and build.
- Run `pnpm pack --dry-run`.
- Review provenance and signing options.
- Protect release credentials.
- Use scoped access and two-factor controls where available.

## Deprecated or Abandoned Packages

- Avoid new use.
- Identify replacement.
- Assess risk.
- Plan migration.
- Document temporary retention.
- Remove when safe.

## Completion Evidence

Report:

- Dependencies added
- Removed
- Updated
- Lockfile changes
- Build-script approvals
- Audit findings
- Registry changes
- Runtime and package-manager changes
- Unresolved advisories

## Guiding Rule

> Every dependency must justify its security, bundle, runtime, compatibility, and maintenance cost.
