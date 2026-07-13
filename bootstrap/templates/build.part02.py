(
            "tools",
            "validate-templates",
        ):
            raise RuntimeError(f"Unexpected tool archive path: {member.name}")
        if member.issym() or member.islnk():
            raise RuntimeError(f"Archive links are not allowed: {member.name}")

    tar.extractall(ROOT)

catalog = ROOT / "CATALOG.md"
catalog_text = catalog.read_text(encoding="utf-8")
template_catalog = """## Reusable templates

The template library provides governed, validated starting structures for agent instructions, architecture decisions, risk assessments, threat models, exceptions, completion evidence, machine-readable records, authorization, human review, production readiness, releases, recovery, and operations.

- [Template library index](templates/README.md)
- [Template catalog](templates/TEMPLATE_CATALOG.md)
- [Selection guide](templates/TEMPLATE_SELECTION_GUIDE.md)
- [Placeholder conventions](templates/PLACEHOLDER_CONVENTIONS.md)
- [Customization policy](templates/CUSTOMIZATION_POLICY.md)
- [Validation guide](templates/VALIDATION_GUIDE.md)

The seven original template paths remain stable. Every template package now includes detailed adoption guidance, a review checklist, and a completed fictitious example.
"""
if "## Reusable templates" not in catalog_text:
    marker = "## Composition examples"
    if marker not in catalog_text:
        raise RuntimeError("Could not locate Composition examples in CATALOG.md")
    catalog_text = catalog_text.replace(
        marker, template_catalog + "\n" + marker, 1
    )
catalog.write_text(catalog_text, encoding="utf-8")

manifest = ROOT / "MANIFEST.md"
manifest_text = manifest.read_text(encoding="utf-8")
template_manifest = """## Complete template library

- root and nested agent-instruction templates
- architecture decision records
- risk assessments
- threat models
- standards exception records
- completion reports
- project manifest, test evidence, and artifact record JSON templates
- change authorization and human review records
- production-readiness reviews
- release plans
- rollback and recovery plans
- operational runbooks
- template selection, authoring, customization, placeholder, lifecycle, validation, and completion guidance
- package review checklists and completed fictitious examples
- executable template validation under `tools/validate-templates/`

The seven original template paths remain stable.
"""
if "## Complete template library" not in manifest_text:
    marker = "## Complete composition examples"
    if marker not in manifest_text:
        raise RuntimeError(
            "Could not locate Complete composition examples in MANIFEST.md"
        )
    manifest_text = manifest_text.replace(
        marker, template_manifest + "\n" + marker, 1
    )
manifest_text = re.sub(r"(?m)^- `templates`\s*$\n?", "", manifest_text)
if "python tools/validate-templates/validate_templates.py" not in manifest_text:
    command = "python tools/validate-schemas/validate_schemas.py"
    manifest_text = manifest_text.replace(
        command,
        command + "\npython tools/validate-templates/validate_templates.py",
        1,
    )
manifest.write_text(manifest_text, encoding="utf-8")

roadmap = ROOT / "ROADMAP.md"
roadmap_text = roadmap.read_text(encoding="utf-8")
template_roadmap = """- Complete template library:
  - root and nested agent instructions
  - architecture, risk, threat, exception, and completion records
  - project manifest, test evidence, and artifact record templates
  - authoriza