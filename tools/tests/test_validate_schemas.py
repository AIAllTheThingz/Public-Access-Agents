from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from helpers import REPO_ROOT, json_result, run_tool


class ValidateSchemasTests(unittest.TestCase):
    def test_repository_schema_system_passes(self):
        completed = run_tool("tools/validate-schemas/validate_schemas.py", "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(json_result(completed)["status"], "passed")

    def test_remote_ref_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(REPO_ROOT / "schemas", root / "schemas")
            path = root / "schemas" / "v1" / "artifact-record.schema.json"
            text = path.read_text(encoding="utf-8").replace('"type": "object"', '"$ref": "https://example.invalid/remote.json",\n  "type": "object"', 1)
            path.write_text(text, encoding="utf-8")
            completed = run_tool("tools/validate-schemas/validate_schemas.py", "--format", "json", "--skip-repository-instances", root=root)
            self.assertEqual(completed.returncode, 1)
            codes = {item["code"] for item in json_result(completed)["findings"]}
            self.assertIn("SCHEMA_REMOTE_REF", codes)


if __name__ == "__main__":
    unittest.main()
