from __future__ import annotations

import unittest

from helpers import json_result, run_tool


class ValidateAllTests(unittest.TestCase):
    def test_list_contains_all_validators(self):
        completed = run_tool("tools/validate-all/run_all.py", "--list")
        self.assertEqual(completed.returncode, 0)
        self.assertIn("validate-tools", completed.stdout)

    def test_single_validator_aggregates(self):
        completed = run_tool("tools/validate-all/run_all.py", "--tool", "validate-standards", "--format", "json")
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        payload = json_result(completed)
        self.assertEqual(payload["summary"]["validatorsCompleted"], 1)


if __name__ == "__main__":
    unittest.main()
