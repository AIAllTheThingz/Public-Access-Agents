from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from helpers import REPO_ROOT, json_result, run_tool


class ComposeAgentsTests(unittest.TestCase):
    def test_dry_run_builds_traceable_plan(self):
        with tempfile.TemporaryDirectory(dir=REPO_ROOT) as temp:
            manifest = Path(temp) / "project-manifest.json"
            manifest.write_text(json.dumps({
                "schemaVersion": "1.0.0",
                "name": "example-service",
                "profile": "WEB_API",
                "languages": ["python"],
                "disciplines": ["testing"],
            }), encoding="utf-8")
            completed = run_tool(
                "tools/compose-agents/compose_agents.py",
                "--manifest", str(manifest),
                "--dry-run",
                "--format", "json",
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            payload = json_result(completed)
            self.assertGreater(payload["summary"]["sources"], 5)
            self.assertFalse(payload["summary"]["written"])


if __name__ == "__main__":
    unittest.main()
