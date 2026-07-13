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


if __name__ == "__main__":
    unittest.main()
