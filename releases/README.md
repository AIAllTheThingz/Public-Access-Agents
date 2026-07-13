---
id: RELEASE-INDEX-001
title: Repository Releases
version: 0.9.0
status: baseline
---

# Repository Releases

## Purpose

This directory contains version-specific release notes and migration guidance for Public-Access-Agents.

Repository release requirements are defined by [`../RELEASE_POLICY.md`](../RELEASE_POLICY.md). Package maturity requirements are defined by [`../MATURITY_POLICY.md`](../MATURITY_POLICY.md).

## Structure

```text
releases/
├── README.md
├── <VERSION>.md
└── migrations/
    └── <VERSION>.md
```

## Release notes

Every repository version requires `releases/<VERSION>.md` containing:

- breaking changes
- normative changes
- editorial changes
- tooling changes where applicable
- deprecations
- migration notes
- security changes
- known limitations

A section must remain present even when it contains `None`.

## Migration notes

Every repository version requires `releases/migrations/<VERSION>.md`.

Migration notes identify affected adopters, required actions, validation, downgrade or rollback considerations, and unresolved limitations.

## Release artifacts

The release workflow attaches:

- deterministic ZIP archive
- deterministic TAR.GZ archive
- SHA-256 checksum file
- release manifest
- release notes
- migration notes

## Boundary

A GitHub Release identifies a reviewed source and compatibility boundary. It does not certify adopting systems or prove that every baseline package has reached stable maturity.
