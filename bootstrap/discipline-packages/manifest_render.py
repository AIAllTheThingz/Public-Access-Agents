"""Supporting renderers for discipline package generation."""

from __future__ import annotations

from common import DISCIPLINES_ROOT, ROOT, frontmatter, sentence

def render_manifest(key: str, data: dict) -> str:
    required = ["AGENTS.md", "README.md", "MANIFEST.md"]
    required += [f"standards/{item[0]}" for item in data["standards"]]
    required += [
        "templates/ADOPTION_CHECKLIST.md",
        "templates/REVIEW_CHECKLIST.md",
        "templates/EVIDENCE_RECORD_TEMPLATE.md",
        "examples/ADOPTION_EXAMPLE.md",
    ]
    text = frontmatter(f'DISC-MAN-{data["prefix"]}', f'{data["title"]} Package Manifest')
    text += f"""# {data["title"]} Package Manifest

## Required files

"""
    text += "\n".join(f"- `{item}`" for item in required)
    text += """

## Package acceptance checks

- `AGENTS.md` preserves stable discipline rule identifiers and references the supporting standards.
- `README.md` explains scope, adoption, tailoring, evidence, validation, companion disciplines, and limitations.
- Every supporting standard has unique front matter and a completion gate.
- Templates contain placeholders rather than environment-specific production values.
- The example uses fictitious context and demonstrates composition rather than claiming universal applicability.
- Relative Markdown links resolve.
- No credentials, tokens, private keys, internal hostnames, production endpoints, or sensitive identifiers are present.
- The package status and version are consistent across maintained entry points.
- Changes include validation evidence and disclose checks not run.

## Repository validation

Run from the repository root:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```

## Adoption validation

The adopting repository must also verify:

- applicable requirements were selected and omissions were documented
- project owners and reviewers are named
- language, platform, framework, profile, and companion-discipline packages are composed correctly
- project validation and evidence requirements are executable
- exceptions are reviewed, time-bounded, and traceable
- remaining risks and unsupported claims are visible
"""
    return text


