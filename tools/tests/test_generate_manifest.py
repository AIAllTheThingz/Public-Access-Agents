from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from helpers import REPO_ROOT, json_result, run_tool


class GenerateManifestTests(unittest.TestCase):
    def test_dry_run_manifest_validates(self):
        completed = run_tool(
            "tools/generate-manifest/generate_manifest.py",
            "--name", "example-service",
            "--profile", "WEB_API",
            "--language", "python",
            "--include-profile-required",
            "--dry-run",
            "--format", "json",
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        payload = json_result(completed)
        self.assertEqual(payload["metadata"]["manifest"]["profile"], "WEB_API")
        self.assertIn("testing", payload["metadata"]["manifest"]["disciplines"])

    def test_refuses_overwrite_without_force(self):
        with tempfile.TemporaryDirectory(dir=REPO_ROOT) as temp:
            output = Path(temp) / "manifest.json"
            output.write_text("{}\n", encoding="utf-8")
            completed = run_tool(
                "tools/generate-manifest/generate_manifest.py",
                "--name", "example-service",
                "--profile", "WEB_API",
                "--language", "python",
                "--manifest-output", str(output),
                "--format", "json",
            )
            self.assertEqual(completed.returncode, 2)


if __name__ == "__main__":
    unittest.main()
