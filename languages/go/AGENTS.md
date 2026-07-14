---
id: GO-AGENT-001
status: baseline
title: Go Agent Standard
---

# Go Agent Standard

## Purpose

Mandatory rules for agents creating, modifying, reviewing, testing, securing, or documenting Go code. This package supplements repository governance and applicable discipline, framework, platform, virtualization, operating-system, networking, and project-profile standards.

> Make the smallest safe, idiomatic, testable, observable, and well-documented change that satisfies the requirement.

## Scope

- Go modules, services, CLI tools, libraries, concurrent workers, tests, and release configuration

## Runtime baseline

Declare the supported Go version in `go.mod` and, when used, the `toolchain` directive. New code must use a supported stable release and remain compatible with the repository baseline.

## Required supporting standards

- `standards/GO_CODING_STANDARD.md`
- `standards/ARCHITECTURE_STANDARD.md`
- `standards/DOCUMENTATION_STANDARD.md`
- `standards/TESTING_STANDARD.md`
- `standards/SECURITY_STANDARD.md`
- `standards/DEPENDENCY_MANAGEMENT_STANDARD.md`
- `standards/OBSERVABILITY_STANDARD.md`
- `standards/COMPLETION_EVIDENCE.md`
- `standards/CONCURRENCY_STANDARD.md`
- `standards/MODULES_STANDARD.md`

## Non-negotiable rules

- Inspect existing code, tests, module declarations, generated files, and conventions first.
- Do not invent environment values, endpoints, identities, credentials, versions, or operational assumptions.
- Validate external input and use least privilege.
- Preserve public APIs unless change is explicitly authorized.
- Keep secrets out of source, tests, logs, errors, examples, and committed configuration.
- Every goroutine must have ownership, bounded lifetime, and a shutdown path.
- Propagate cancellation and deadlines through `context.Context`.
- Do not hide errors, panic for expected failures, or report false success.
- Keep generated code reproducible and identify its generator.

## Required working method

1. Discover the module and runtime baseline.
2. Classify risk and identify trust and concurrency boundaries.
3. Implement the smallest coherent change.
4. Add tests and documentation.
5. Run formatting, vetting, tests, and race detection when concurrency changes.
6. Review the diff and report exact evidence and limitations.

## Typical validation

- `gofmt` on changed files
- `go vet ./...`
- `go test ./...`
- `go test -race ./...` when concurrency changes
