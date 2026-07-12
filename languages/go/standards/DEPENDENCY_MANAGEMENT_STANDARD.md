---
id: GO-DEP-001
status: baseline
title: Go Dependency Management Standard
---

# Dependency Management Standard

- Use Go modules and commit `go.mod` and `go.sum`.
- Add dependencies only when justified and review provenance, maintenance, license, vulnerabilities, and transitive impact.
- Do not commit local-path `replace` directives for production use.
- Use vendoring only when the repository intentionally adopts it.
- Review module and toolchain changes separately from unrelated code.
