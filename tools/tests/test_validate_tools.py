from __future__ import annotations

import unittest

from helpers import json_result, run_tool


class ValidateToolsTests(unittest.TestCase):
    def test_tool_packages_pass(self):
        completed = run_tool("tools/validate-tools/validate_tools.py", "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(json_result(completed)["status"], "passed")


if __name__ == "__main__":
    unittest.main()
