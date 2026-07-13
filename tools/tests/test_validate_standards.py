from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from helpers import json_result, make_required_root, run_tool


class ValidateStandardsTests(unittest.TestCase):
    def test_minimal_repository_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            make_required_root(root)
            completed = run_tool("tools/validate-standards/validate_repository.py", "--format", "json", root=root)
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            self.assertEqual(json_result(completed)["status"], "passed")

    def test_bootstrap_directory_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            make_required_root(root)
            (root / "bootstrap").mkdir()
            completed = run_tool("tools/validate-standards/validate_repository.py", "--format", "json", root=root)
            self.assertEqual(completed.returncode, 1)
            codes = {item["code"] for item in json_result(completed)["findings"]}
            self.assertIn("BOOTSTRAP_PRESENT", codes)

    def test_python_cache_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            make_required_root(root)
            cache = root / "src" / "__pycache__"
            cache.mkdir(parents=True)
            (cache / "module.cpython-312.pyc").write_bytes(b"not-bytecode")
            completed = run_tool("tools/validate-standards/validate_repository.py", "--format", "json", root=root)
            self.assertEqual(completed.returncode, 1)
            codes = {item["code"] for item in json_result(completed)["findings"]}
            self.assertIn("PYTHON_CACHE_PRESENT", codes)

    def test_missing_license_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            make_required_root(root)
            (root / "LICENSE").unlink()
            completed = run_tool("tools/validate-standards/validate_repository.py", "--format", "json", root=root)
            self.assertEqual(completed.returncode, 1)
            findings = json_result(completed)["findings"]
            self.assertTrue(
                any(item["code"] == "ROOT_FILE_MISSING" and item.get("path") == "LICENSE" for item in findings)
            )

    def test_stale_unselected_license_wording_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            make_required_root(root)
            (root / "README.md").write_text(
                "# Test\n\nApache-2.0\n\nA repository license has not yet been selected.\n",
                encoding="utf-8",
            )
            completed = run_tool("tools/validate-standards/validate_repository.py", "--format", "json", root=root)
            self.assertEqual(completed.returncode, 1)
            codes = {item["code"] for item in json_result(completed)["findings"]}
            self.assertIn("LICENSE_SELECTION_STALE", codes)

    def test_invalid_notice_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            make_required_root(root)
            (root / "NOTICE").write_text("Public-Access-Agents\n", encoding="utf-8")
            completed = run_tool("tools/validate-standards/validate_repository.py", "--format", "json", root=root)
            self.assertEqual(completed.returncode, 1)
            codes = {item["code"] for item in json_result(completed)["findings"]}
            self.assertIn("NOTICE_INVALID", codes)

    def test_invalid_license_text_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            make_required_root(root)
            (root / "LICENSE").write_text("Apache-2.0\n", encoding="utf-8")
            completed = run_tool("tools/validate-standards/validate_repository.py", "--format", "json", root=root)
            self.assertEqual(completed.returncode, 1)
            codes = {item["code"] for item in json_result(completed)["findings"]}
            self.assertIn("LICENSE_INVALID", codes)


if __name__ == "__main__":
    unittest.main()
