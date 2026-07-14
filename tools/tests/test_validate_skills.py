from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from helpers import json_result, run_tool


def write(root: Path, path: str, content: str) -> None:
    destination = root / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")


def skill(name: str, description: str | None = None, body: str | None = None) -> str:
    description = description or f"Route advanced {name} engineering work. Use when Codex must apply {name} package standards."
    body = body or f"# {name.title()} Engineering\n\nApply the selected package guidance.\n"
    return f"---\nname: {name}\ndescription: {description}\n---\n\n{body}"


def manifest(*paths: str) -> str:
    entries = "\n".join(f"- `{path}`" for path in paths)
    return f"# Repository Manifest\n\n## Agent skill entry points\n\n{entries}\n\n## Other\n"


class ValidateSkillsTests(unittest.TestCase):
    def test_repository_skills_pass(self):
        completed = run_tool("tools/validate-skills/validate_skills.py", "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        payload = json_result(completed)
        self.assertEqual(payload["status"], "passed")
        self.assertEqual(payload["summary"]["skillFiles"], 6)
        self.assertEqual(payload["summary"]["registeredSkills"], 6)
        self.assertEqual(payload["summary"]["packageRoutes"], 43)

    def test_text_output_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root, "sample/SKILL.md", skill("sample"))
            write(root, "MANIFEST.md", manifest("sample/SKILL.md"))
            completed = run_tool("tools/validate-skills/validate_skills.py", root=root)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("validate-skills: passed", completed.stdout)

    def test_frontmatter_failures_have_stable_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root, "missing/SKILL.md", "# Missing Frontmatter\n")
            write(root, "unterminated/SKILL.md", "---\nname: unterminated\ndescription: no closing delimiter\n")
            write(root, "MANIFEST.md", manifest("missing/SKILL.md", "unterminated/SKILL.md"))
            completed = run_tool("tools/validate-skills/validate_skills.py", "--format", "json", root=root)
        self.assertEqual(completed.returncode, 1)
        codes = {item["code"] for item in json_result(completed)["findings"]}
        self.assertIn("SKILL_FRONTMATTER_MISSING", codes)
        self.assertIn("SKILL_FRONTMATTER_UNTERMINATED", codes)

    def test_name_description_and_frontmatter_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            content = """---
name: Wrong_Name
description: Too short and has no trigger.
metadata: forbidden
---

# Bad Skill
"""
            write(root, "bad/SKILL.md", content)
            write(root, "MANIFEST.md", manifest("bad/SKILL.md"))
            completed = run_tool("tools/validate-skills/validate_skills.py", "--format", "json", root=root)
        codes = {item["code"] for item in json_result(completed)["findings"]}
        self.assertIn("SKILL_NAME_INVALID", codes)
        self.assertIn("SKILL_NAME_DIRECTORY_MISMATCH", codes)
        self.assertIn("SKILL_DESCRIPTION_TOO_SHORT", codes)
        self.assertIn("SKILL_DESCRIPTION_TRIGGER_MISSING", codes)
        self.assertIn("SKILL_FRONTMATTER_KEY_UNSUPPORTED", codes)

    def test_duplicate_names_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root, "first/SKILL.md", skill("shared"))
            write(root, "second/SKILL.md", skill("shared"))
            write(root, "MANIFEST.md", manifest("first/SKILL.md", "second/SKILL.md"))
            completed = run_tool("tools/validate-skills/validate_skills.py", "--format", "json", root=root)
        codes = [item["code"] for item in json_result(completed)["findings"]]
        self.assertEqual(codes.count("SKILL_NAME_DUPLICATE"), 2)

    def test_package_routes_must_be_complete_and_unique(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root, "collection/one/AGENTS.md", "# One\n")
            write(root, "collection/one/MANIFEST.md", "# One\n")
            write(root, "collection/two/AGENTS.md", "# Two\n")
            write(root, "collection/two/MANIFEST.md", "# Two\n")
            body = """# Collection Engineering

- [One](one/)
- [One again](one/)
"""
            write(root, "collection/SKILL.md", skill("collection", body=body))
            write(root, "MANIFEST.md", manifest("collection/SKILL.md"))
            completed = run_tool("tools/validate-skills/validate_skills.py", "--format", "json", root=root)
        codes = {item["code"] for item in json_result(completed)["findings"]}
        self.assertIn("SKILL_PACKAGE_ROUTE_DUPLICATE", codes)
        self.assertIn("SKILL_PACKAGE_ROUTE_MISSING", codes)

    def test_registry_is_bidirectional(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root, "actual/SKILL.md", skill("actual"))
            write(root, "MANIFEST.md", manifest("ghost/SKILL.md"))
            completed = run_tool("tools/validate-skills/validate_skills.py", "--format", "json", root=root)
        codes = {item["code"] for item in json_result(completed)["findings"]}
        self.assertIn("SKILL_NOT_REGISTERED", codes)
        self.assertIn("SKILL_REGISTRY_TARGET_MISSING", codes)

    def test_unsafe_and_missing_links_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            body = """# Links

- [Absolute](/tmp/file)
- [Windows absolute](C:\\temp\\file)
- [Escape](../../outside)
- [Missing](missing.md)
- [Unsafe](javascript:alert)
"""
            write(root, "links/SKILL.md", skill("links", body=body))
            write(root, "MANIFEST.md", manifest("links/SKILL.md"))
            completed = run_tool("tools/validate-skills/validate_skills.py", "--format", "json", root=root)
        codes = {item["code"] for item in json_result(completed)["findings"]}
        self.assertIn("SKILL_LINK_ABSOLUTE", codes)
        self.assertIn("SKILL_LINK_ESCAPE", codes)
        self.assertIn("SKILL_LINK_MISSING", codes)
        self.assertIn("SKILL_LINK_UNSAFE_SCHEME", codes)

    def test_body_constraints_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            body = "# Body\n\n## When to Use This Skill\n\nTODO replace me\nExtra line\n"
            write(root, "body/SKILL.md", skill("body", body=body))
            write(root, "MANIFEST.md", manifest("body/SKILL.md"))
            completed = run_tool(
                "tools/validate-skills/validate_skills.py",
                "--max-body-lines",
                "3",
                "--format",
                "json",
                root=root,
            )
        codes = {item["code"] for item in json_result(completed)["findings"]}
        self.assertIn("SKILL_BODY_TOO_LONG", codes)
        self.assertIn("SKILL_BODY_TRIGGER_HEADING", codes)
        self.assertIn("SKILL_PLACEHOLDER", codes)

    def test_optional_agent_metadata_is_validated(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root, "sample/SKILL.md", skill("sample"))
            write(root, "sample/agents/openai.yaml", "interface:\n  display_name: Sample\n  short_description: short\n  default_prompt: Use this skill.\n  icon_small: ../outside.png\n")
            write(root, "MANIFEST.md", manifest("sample/SKILL.md"))
            completed = run_tool("tools/validate-skills/validate_skills.py", "--format", "json", root=root)
        codes = {item["code"] for item in json_result(completed)["findings"]}
        self.assertIn("SKILL_METADATA_SHORT_DESCRIPTION_LENGTH", codes)
        self.assertIn("SKILL_METADATA_PROMPT_REFERENCE", codes)
        self.assertIn("SKILL_METADATA_ICON_ESCAPE", codes)

    def test_agent_metadata_can_be_required(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root, "sample/SKILL.md", skill("sample"))
            write(root, "MANIFEST.md", manifest("sample/SKILL.md"))
            completed = run_tool(
                "tools/validate-skills/validate_skills.py",
                "--require-agent-metadata",
                "--format",
                "json",
                root=root,
            )
        codes = {item["code"] for item in json_result(completed)["findings"]}
        self.assertEqual(completed.returncode, 1)
        self.assertIn("SKILL_METADATA_MISSING", codes)

    def test_invalid_limits_return_input_error(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            completed = run_tool(
                "tools/validate-skills/validate_skills.py",
                "--max-body-lines",
                "0",
                "--format",
                "json",
                root=root,
            )
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(json_result(completed)["status"], "error")

    def test_json_output_is_deterministic(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write(root, "sample/SKILL.md", skill("sample"))
            write(root, "MANIFEST.md", manifest("sample/SKILL.md"))
            first = run_tool("tools/validate-skills/validate_skills.py", "--format", "json", root=root)
            second = run_tool("tools/validate-skills/validate_skills.py", "--format", "json", root=root)
        self.assertEqual(first.returncode, 0)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
