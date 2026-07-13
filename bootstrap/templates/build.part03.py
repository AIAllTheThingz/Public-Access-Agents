tion, human review, and production-readiness records
  - release, rollback, recovery, and operational runbook templates
  - selection, authoring, customization, placeholder, lifecycle, validation, and completion guidance
  - completed examples and executable template validation"""
if "- Templates" in roadmap_text:
    roadmap_text = roadmap_text.replace("- Templates", template_roadmap, 1)
elif "- Complete template library:" not in roadmap_text:
    raise RuntimeError("Could not locate template roadmap entry")
roadmap.write_text(roadmap_text, encoding="utf-8")

tools_readme = ROOT / "tools" / "README.md"
tools_text = tools_readme.read_text(encoding="utf-8")
tools_text = tools_text.replace(
    "The tools validate repository structure, links, schema contracts, "
    "examples, and machine-readable evidence.",
    "The tools validate repository structure, links, schema contracts, "
    "template packages, examples, and machine-readable evidence.",
)
if "python tools/validate-templates/validate_templates.py" not in tools_text:
    tools_text = tools_text.replace(
        "python tools/validate-schemas/validate_schemas.py",
        "python tools/validate-schemas/validate_schemas.py\n"
        "python tools/validate-templates/validate_templates.py",
        1,
    )
if "[`validate-templates`]" not in tools_text:
    tools_text = tools_text.replace(
        "- [`validate-schemas`](validate-schemas/) checks Draft 2020-12 "
        "schemas, versioned equivalence, positive and negative examples, "
        "formats, and repository instances.",
        "- [`validate-schemas`](validate-schemas/) checks Draft 2020-12 "
        "schemas, versioned equivalence, positive and negative examples, "
        "formats, and repository instances.\n"
        "- [`validate-templates`](validate-templates/) checks template "
        "packages, stable paths, placeholders, examples, and schema-backed "
        "records.",
        1,
    )
tools_readme.write_text(tools_text, encoding="utf-8")

shutil.rmtree(BOOTSTRAP)
bootstrap = ROOT / "bootstrap"
if bootstrap.exists() and not any(bootstrap.iterdir()):
    bootstrap.rmdir()

print("Complete template library restored and root documentation updated.")
