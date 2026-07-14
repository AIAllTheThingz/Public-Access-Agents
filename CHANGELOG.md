# Changelog

All notable repository changes are recorded here.

The repository follows [Semantic Versioning 2.0.0](https://semver.org/) as adapted by [`RELEASE_POLICY.md`](RELEASE_POLICY.md) for normative standards, schemas, templates, executable tools, stable paths, and documentation.

Release notes distinguish:

- **breaking changes** that invalidate a supported contract or require migration
- **normative changes** that add or alter requirements or evidence expectations
- **editorial changes** that do not change normative meaning
- **tooling changes** that alter executable validation, generation, composition, or release behavior
- **security changes** that address or disclose security-relevant behavior

## [Unreleased]

### Breaking changes

- None.

### Normative changes

- Added collection-level language, framework, and platform skills that route agent work to the applicable standards packages and require advanced, version-compatible implementation, layered validation, and explicit completion evidence.

### Editorial changes

- None.

### Tooling changes

- None.

### Security

- None.

### Deprecations

- None.

### Migration notes

- Existing adopters may continue using `AGENTS.md` and package entry points directly. Agents that support skills may additionally use `languages/SKILL.md`, `frameworks/SKILL.md`, and `platforms/SKILL.md` without changing existing package paths.

## [0.9.0] - 2026-07-13

### Breaking changes

- None. This is the first repository-level release contract. Existing public paths are treated as the initial pre-1.0 compatibility baseline.

### Normative changes

- Established the repository governance operating model, risk classification, exception process, completion evidence, secure-development expectations, human review, production readiness, threat modeling, and vulnerability response.
- Completed language, discipline, framework, platform, project-profile, template, schema, example, and toolchain collections.
- Added repository licensing under Apache-2.0.
- Added repository maintainer, ownership, CODEOWNERS, specialist-review, merge-authority, emergency-change, inactivity, and succession rules.
- Added repository-wide semantic versioning, deprecation, migration, maturity-promotion, release-evidence, tag, and GitHub Release requirements.

### Editorial changes

- Expanded root and package README files into adoption and maintenance guides.
- Added catalogs, manifests, selection guides, examples, and explicit non-production boundaries throughout the repository.

### Tooling changes

- Added repository, link, schema, template, tool, and release validation.
- Added deterministic project-manifest generation and traceable standards-bundle composition.
- Added deterministic release ZIP and TAR archives, release manifests, migration-note packaging, and SHA-256 checksums.
- Added a unified validation runner and central unit-test suite.

### Security

- Added offline schema validation and remote-reference rejection.
- Added committed-cache and temporary-artifact checks.
- Added path containment, dry-run, overwrite protection, and atomic staging for writing tools.
- Added restricted release workflow permissions and tag validation.

### Deprecations

- None.

### Migration notes

- See [`releases/migrations/0.9.0.md`](releases/migrations/0.9.0.md).

[Unreleased]: https://github.com/AIAllTheThingz/Public-Access-Agents/compare/v0.9.0...HEAD
[0.9.0]: https://github.com/AIAllTheThingz/Public-Access-Agents/releases/tag/v0.9.0
