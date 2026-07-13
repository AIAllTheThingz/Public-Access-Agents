from __future__ import annotations

import unittest

from helpers import json_result, run_tool


class ValidateTemplatesTests(unittest.TestCase):
    def test_repository_templates_pass(self):
        completed = run_tool("tools/validate-templates/validate_templates.py", "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(json_result(completed)["status"], "passed")


if __name__ == "__main__":
    unittest.main()
