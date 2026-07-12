# .NET Dependency Management Standard

## Purpose

This standard governs NuGet packages, SDK selection, workloads, analyzers, tools, and external dependencies.

Dependencies are production code you did not write but still volunteered to operate.

## General Rules

- Add a dependency only when it provides clear value.
- Prefer supported platform libraries when they meet the need.
- Review license, maintenance, security, compatibility, and transitive dependencies.
- Use central package management for multi-project repositories.
- Pin direct package versions.
- Keep dependency upgrades focused and reviewable.
- Remove unused packages.
- Do not add packages solely to avoid a small amount of clear maintainable code.

## SDK Selection

Use `global.json` for reproducible SDK-family selection.

For the .NET 10 LTS baseline:

```json
{
  "sdk": {
    "version": "10.0.100",
    "rollForward": "latestFeature",
    "allowPrerelease": false
  }
}
```

The full version is required by `global.json`.

`latestFeature` permits supported .NET 10 feature-band servicing while preventing automatic roll-forward to a later major release.

Update SDK policy deliberately.

## Target Framework

New applications target:

```xml
<TargetFramework>net10.0</TargetFramework>
```

Multi-target only when consumers require it.

Do not add older targets without tests and compatibility need.

## Central Package Management

For solutions with multiple projects, prefer `Directory.Packages.props`.

Enable:

```xml
<ManagePackageVersionsCentrally>true</ManagePackageVersionsCentrally>
```

Project files should omit versions for centrally managed packages.

Keep versions visible and reviewed.

## Package Sources

- Use trusted sources.
- Minimize source count.
- Avoid package-source mapping ambiguity.
- Do not mark untrusted sources as trusted automatically.
- Do not include credentials in `NuGet.config`.
- Use deployment secret mechanisms for authenticated feeds.
- Review dependency-confusion risk.

## Version Selection

- Prefer stable supported versions.
- Avoid preview packages unless explicitly requested.
- Keep related platform packages aligned.
- Do not use floating versions in committed production projects.
- Avoid broad wildcard ranges.
- Review breaking changes before major updates.
- Do not update unrelated packages during a targeted feature or bug fix.

## Transitive Dependencies

Review transitive dependencies for:

- Vulnerabilities
- Licensing
- Native assets
- Platform restrictions
- Version conflicts
- Size
- Trimming or AOT compatibility
- Maintenance status

Use:

```bash
dotnet package list --include-transitive
```

Use `dotnet nuget why` when investigating why a package is present.

## Vulnerability Audit

Run:

```bash
dotnet package list --vulnerable --include-transitive
```

Also review restore audit warnings.

For each finding:

- Identify direct or transitive origin.
- Determine affected runtime path.
- Upgrade the nearest responsible package where practical.
- Record temporary exceptions.
- Do not suppress broadly.

A zero-result command does not prove the entire software supply chain is risk-free.

## Lock Files

Use package lock files when deployment reproducibility requires them.

If enabled:

- Commit lock files.
- Use locked restore in CI where appropriate.
- Update lock files intentionally.
- Review transitive changes.

Do not use lock files mechanically where central package policy and repository workflow make them unnecessary.

## Tools

Pin repository tools through a tool manifest where appropriate:

```bash
dotnet new tool-manifest
dotnet tool install <tool>
```

Do not require global tool installation when a local manifest provides reproducibility.

Review tool permissions and maintenance.

## Analyzers

Use built-in .NET analyzers and repository-approved analyzers.

- Keep analyzer versions controlled.
- Treat analyzer changes as code-behavior changes.
- Avoid broad suppressions.
- Document exceptions.
- Do not add overlapping analyzer packages without need.

## Source Generators

Review source generators for:

- Build-time execution risk
- Generated code volume
- IDE compatibility
- Trimming and AOT behavior
- Incremental build behavior
- Security and provenance

Do not introduce source generators for trivial boilerplate without measurable benefit.

## Workloads

Install workloads only when required.

Document:

- Workload name
- SDK version
- Platform prerequisites
- CI installation
- Update policy

Do not modify global workloads automatically during application execution.

## Native Dependencies

Document:

- Runtime identifiers
- Supported operating systems
- Native library origin
- Deployment packaging
- Security update process
- Container requirements
- License

Test publish output on supported targets.

## Dependency Upgrades

A dependency upgrade should include:

- Reason
- Old and new versions
- Release-note review
- Breaking-change review
- Vulnerability status
- Test results
- Migration work
- Rollback consideration

Keep large upgrade waves separate from unrelated features.

## Deprecated or Abandoned Packages

When a package is deprecated or abandoned:

- Identify replacement.
- Assess security and maintenance risk.
- Plan migration.
- Avoid adding new use.
- Document temporary retention.
- Remove when safe.

## Completion Evidence

Report:

- Packages added
- Packages removed
- Version changes
- Direct and transitive vulnerability results
- New package sources
- Tool changes
- Workload changes
- Unresolved advisories
- Compatibility assumptions

## Guiding Rule

> Every dependency must justify its operational, security, compatibility, and maintenance cost.
