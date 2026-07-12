---
id: PY-MAN-001
status: baseline
title: Python Manifest
---

# Python Package Manifest

## Required files

- `AGENTS.md`
- `MANIFEST.md`
- `README.md`
- `examples/ADOPTION_EXAMPLE.md`
- `standards/ARCHITECTURE_STANDARD.md`
- `standards/COMPLETION_EVIDENCE.md`
- `standards/DEPENDENCY_MANAGEMENT_STANDARD.md`
- `standards/DOCUMENTATION_STANDARD.md`
- `standards/OBSERVABILITY_STANDARD.md`
- `standards/PACKAGING_STANDARD.md`
- `standards/PYTHON_CODING_STANDARD.md`
- `standards/SECURITY_STANDARD.md`
- `standards/TESTING_STANDARD.md`
- `standards/TYPING_STANDARD.md`
- `templates/ADOPTION_CHECKLIST.md`
- `templates/AGENTS_TEMPLATE.md`

## Validation checklist

- Every Markdown file has a unique front-matter `id`.
- `AGENTS.md` references every mandatory supporting standard.
- Runtime and toolchain requirements are explicit.
- Security, testing, documentation, dependency, observability, and completion-evidence rules are present.
- Templates and examples contain no production identifiers or secrets.
- Relative links resolve.
- Repository validation tools pass.
