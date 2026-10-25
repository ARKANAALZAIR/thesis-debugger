#!/usr/bin/env python3
"""End-to-end local tests for the supplied-material result-trace workflow."""

from __future__ import annotations

import csv
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from result_trace_eval import (
    FIXTURE_ROOT,
    MISMATCH,
    MODULE_STATUSES,
    NOT_ASSESSABLE,
    NOT_REPRODUCIBLE,
    REPRODUCED,
    RESULT_STATUSES,
    assess_blocked_execution,
    deduplicate_findings,
    evaluate_captured_report,
    evaluate_trace_fixture,
)


class ResultTraceWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="thesis-trace-test-")
        self.fixture = Path(self.temporary.name) / "fixture"
        shutil.copytree(FIXTURE_ROOT, self.fixture)

    def tearDown(self):
        self.temporary.cleanup()

    def _captured_report(self, report_name="reported-match.json", status=REPRODUCED):
        assessment = evaluate_trace_fixture(self.fixture, report_name)
        reported = assessment.row["reported_result"]["value"]
        reproduced = assessment.row["reproduced_result"]["value"]
        row = "| RT-001 | Chapter 4, Table 4.2 | tests/fixtures/result-trace/observations.csv (3 included rows; 1 excluded row) | analysis.py: read-only CSV; include=yes; arithmetic mean | {} score points (n=3, 1 excluded) | {} score points (n=3, 1 excluded) | {} | {} | fixture scope limitation | discussion impact |".format(
            reported, reproduced, reproduced - reported, status
        )
        return "\n".join([
            "### Result Traceability & Reproduction Audit",
            "| Result/claim ID | Thesis location | Source data/artifact | Script/formula/method | Reported result | Reproduced result | Discrepancy | Result status | Limitations | Downstream impact |",
            "|---|---|---|---|---|---|---|---|---|---|---|",
            row,
            "",
            "## 7. Dependency Analysis",
        ])

    def test_supplied_csv_is_executed_and_independently_recomputed(self):
        assessment = evaluate_trace_fixture(self.fixture, "reported-match.json")
        row = assessment.row
        with (self.fixture / "observations.csv").open(newline="", encoding="utf-8") as handle:
            values = [float(record["value"]) for record in csv.DictReader(handle) if record["include"] == "yes"]
        independent_mean = sum(values) / len(values)
        self.assertEqual(independent_mean, 20.0)
        self.assertEqual(row["reproduced_result"]["value"], independent_mean)
        self.assertEqual(row["reproduced_result"]["n"], 3)
        self.assertEqual(row["reproduced_result"]["excluded"], 1)
        self.assertEqual(row["result_status"], REPRODUCED)
        self.assertEqual(row["interpretation_status"], "UNSUPPORTED BY SUPPLIED SCOPE")
        self.assertEqual(len(row["trace_chain"]), 6)

    def test_deliberate_table_mismatch_is_detected_and_owned_once(self):
        assessment = evaluate_trace_fixture(self.fixture, "reported-mismatch.json")
        self.assertEqual(assessment.row["result_status"], MISMATCH)
        self.assertEqual(assessment.row["discrepancy"]["value_difference"], -5.0)
        self.assertEqual(assessment.finding["primary_module"], "M06")
        self.assertEqual(assessment.finding["related_modules"], "M07, M10, M12")
        duplicate = dict(assessment.finding, primary_module="M10", finding_id="TD-099")
        findings = deduplicate_findings([assessment.finding, duplicate])
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["finding_id"], "TD-014")

    def test_harmless_display_rounding_is_accepted(self):
        report_path = self.fixture / "reported-match.json"
        report = json.loads(report_path.read_text(encoding="utf-8"))
        report["reported_value"] = 20.004
        report_path.write_text(json.dumps(report), encoding="utf-8")
        self.assertEqual(evaluate_trace_fixture(self.fixture).row["result_status"], REPRODUCED)

    def test_missing_data_and_missing_script_are_blocked_without_false_claims(self):
        (self.fixture / "observations.csv").unlink()
        result = evaluate_trace_fixture(self.fixture)
        self.assertEqual(result.row["result_status"], NOT_REPRODUCIBLE)
        self.assertIn("observations.csv was not supplied", result.row["limitations"])

        shutil.copytree(FIXTURE_ROOT, self.fixture, dirs_exist_ok=True)
        (self.fixture / "analysis.py").unlink()
        result = evaluate_trace_fixture(self.fixture)
        self.assertEqual(result.row["result_status"], NOT_REPRODUCIBLE)
        self.assertIn("execution refused", result.row["limitations"])

    def test_unavailable_dependency_and_unsafe_execution_are_blocked(self):
        self.assertEqual(assess_blocked_execution("numpy is unavailable"), NOT_REPRODUCIBLE)
        self.assertEqual(assess_blocked_execution("execution permission is absent"), NOT_REPRODUCIBLE)
        self.assertEqual(assess_blocked_execution("", identifiable=False), NOT_ASSESSABLE)
        self.assertNotIn(NOT_REPRODUCIBLE, MODULE_STATUSES)

    def test_changed_analysis_script_is_never_executed(self):
        path = self.fixture / "analysis.py"
        path.write_text("raise RuntimeError('must not execute')\n", encoding="utf-8")
        result = evaluate_trace_fixture(self.fixture)
        self.assertEqual(result.row["result_status"], NOT_REPRODUCIBLE)
        self.assertIn("changed; execution refused", result.row["limitations"])

    def test_result_and_module_status_taxonomies_remain_separate(self):
        self.assertEqual(RESULT_STATUSES, {REPRODUCED, MISMATCH, NOT_REPRODUCIBLE, NOT_ASSESSABLE})
        self.assertNotIn(REPRODUCED, MODULE_STATUSES)
        self.assertNotIn(MISMATCH, MODULE_STATUSES)
        self.assertEqual(MODULE_STATUSES, {"FOUND", "Error Not Found", "NOT ASSESSABLE", "COMPLETED", "NOT APPLICABLE"})

    def test_captured_report_row_is_checked_against_the_independent_oracle(self):
        self.assertEqual(evaluate_captured_report(self._captured_report()), [])
        errors = evaluate_captured_report(self._captured_report(status=MISMATCH))
        self.assertIn("captured result status does not match the independent fixture comparison", errors)

    def test_captured_report_must_detect_deliberate_mismatch(self):
        self.assertEqual(evaluate_captured_report(self._captured_report("reported-mismatch.json", MISMATCH), "reported-mismatch.json"), [])
        errors = evaluate_captured_report(self._captured_report("reported-mismatch.json", REPRODUCED), "reported-mismatch.json")
        self.assertIn("captured result status does not match the independent fixture comparison", errors)


if __name__ == "__main__":
    unittest.main(verbosity=2)
