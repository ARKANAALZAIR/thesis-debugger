#!/usr/bin/env python3
"""Evaluate the package's trusted result-trace fixture and captured comparison."""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = ROOT / "tests/fixtures/result-trace"
TRUSTED_ANALYSIS_SHA256 = "82c188ef5377dc3032384d644c97397453e053110035382134c907e35078ad1e"
ALLOWED_REPORTS = {"reported-match.json", "reported-mismatch.json"}
REPRODUCED = "REPRODUCED"
MISMATCH = "MISMATCH"
NOT_REPRODUCIBLE = "NOT REPRODUCIBLE WITH SUPPLIED MATERIALS"
NOT_ASSESSABLE = "NOT ASSESSABLE"
RESULT_STATUSES = {REPRODUCED, MISMATCH, NOT_REPRODUCIBLE, NOT_ASSESSABLE}
MODULE_STATUSES = {"FOUND", "Error Not Found", "NOT ASSESSABLE", "COMPLETED", "NOT APPLICABLE"}
REQUIRED_ROW_FIELDS = {
    "result_id", "thesis_location", "source_data", "procedure", "reported_result",
    "reproduced_result", "discrepancy", "result_status", "limitations", "downstream_impact",
}


@dataclass(frozen=True)
class TraceAssessment:
    row: dict[str, Any]
    finding: dict[str, str] | None = None


def _loads_strict(path: Path) -> dict[str, Any]:
    def reject_constant(value: str) -> None:
        raise ValueError("non-standard numeric constant: " + value)

    value = json.loads(path.read_text(encoding="utf-8"), parse_constant=reject_constant)
    if not isinstance(value, dict):
        raise ValueError("expected a JSON object")
    return value


def _blocked_row(result_id: str, location: str, data_path: str, blocker: str) -> TraceAssessment:
    return TraceAssessment({
        "result_id": result_id,
        "thesis_location": location,
        "source_data": data_path,
        "procedure": "NOT RUN",
        "reported_result": "NOT ASSESSABLE",
        "reproduced_result": "NOT RUN",
        "discrepancy": "NOT ASSESSABLE",
        "result_status": NOT_REPRODUCIBLE,
        "limitations": blocker,
        "downstream_impact": "Not assessed from unavailable reproduction materials.",
    })


def _resource_limits() -> None:
    if os.name != "posix":
        return
    import resource

    resource.setrlimit(resource.RLIMIT_CPU, (3, 3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_NOFILE, (32, 32))


def _execute_trusted_fixture(fixture_dir: Path) -> dict[str, Any]:
    script = fixture_dir / "analysis.py"
    expected_script = FIXTURE_ROOT / "analysis.py"
    if not script.is_file() or hashlib.sha256(script.read_bytes()).hexdigest() != TRUSTED_ANALYSIS_SHA256:
        raise RuntimeError("trusted fixture analysis script is missing or has changed; execution refused")
    for name in ("observations.csv", "context.json"):
        path = fixture_dir / name
        if not path.is_file():
            raise FileNotFoundError(name + " was not supplied")
        if path.stat().st_size > 65536:
            raise RuntimeError(name + " exceeds the fixture input-size limit")

    with tempfile.TemporaryDirectory(prefix="thesis-trace-") as temporary:
        workdir = Path(temporary)
        for name in ("analysis.py", "observations.csv", "context.json"):
            shutil.copyfile(fixture_dir / name, workdir / name)
        command = [sys.executable, "-I", "-B", str(workdir / "analysis.py")]
        try:
            completed = subprocess.run(
                command,
                cwd=str(workdir),
                env={"PATH": os.defpath, "PYTHONDONTWRITEBYTECODE": "1"},
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
                start_new_session=(os.name == "posix"),
                preexec_fn=_resource_limits if os.name == "posix" else None,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError("trusted fixture analysis exceeded the 5-second limit") from exc
        if completed.returncode != 0:
            raise RuntimeError("trusted fixture analysis exited {}: {}".format(completed.returncode, completed.stderr[:1000]))
        if len(completed.stdout) > 16384:
            raise RuntimeError("trusted fixture analysis output exceeded 16 KiB")
        result = json.loads(completed.stdout, parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
        if not isinstance(result, dict):
            raise RuntimeError("trusted fixture analysis did not return an object")
        return result


def evaluate_trace_fixture(fixture_dir: Path = FIXTURE_ROOT, report_name: str = "reported-match.json") -> TraceAssessment:
    """Run only the pinned package fixture script; treat all fixture values as data."""
    if report_name not in ALLOWED_REPORTS:
        raise ValueError("report name is not an allowlisted fixture")
    report_path = fixture_dir / report_name
    if not report_path.is_file():
        return _blocked_row("NOT IDENTIFIED", "NOT IDENTIFIED", "observations.csv", report_name + " was not supplied")
    try:
        report = _loads_strict(report_path)
        context = _loads_strict(fixture_dir / "context.json")
    except FileNotFoundError as exc:
        return _blocked_row("RT-001", "Chapter 4, Table 4.2", "observations.csv", str(exc))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return _blocked_row("RT-001", "Chapter 4, Table 4.2", "observations.csv", "fixture metadata is invalid: " + str(exc))

    result_id = context.get("result_id", "NOT IDENTIFIED")
    location = context.get("thesis_location", "NOT IDENTIFIED")
    try:
        reproduced = _execute_trusted_fixture(fixture_dir)
    except (OSError, RuntimeError, json.JSONDecodeError, ValueError) as exc:
        return _blocked_row(result_id, location, "observations.csv", str(exc))

    reported_value = report.get("reported_value")
    reproduced_value = reproduced.get("reproduced_value")
    tolerance = report.get("tolerance")
    numeric = lambda value: isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
    if not numeric(reported_value) or not numeric(reproduced_value) or not numeric(tolerance) or tolerance < 0:
        return TraceAssessment({
            "result_id": result_id, "thesis_location": location, "source_data": "observations.csv",
            "procedure": reproduced.get("reported_procedure", "UNKNOWN"), "reported_result": reported_value,
            "reproduced_result": reproduced_value, "discrepancy": "Required numeric value or tolerance is invalid",
            "result_status": NOT_ASSESSABLE, "limitations": "reported value, reproduced value, or tolerance is not assessable",
            "downstream_impact": report.get("downstream_impact", "NOT ASSESSED"),
        })

    context_fields = ("sample_n", "excluded_rows", "unit", "procedure_id")
    context_matches = all(report.get(field) == reproduced.get(field) for field in context_fields)
    difference = reproduced_value - reported_value
    numeric_matches = abs(difference) <= tolerance
    status = REPRODUCED if context_matches and numeric_matches else MISMATCH
    limitations = []
    if not context_matches:
        limitations.append("sample, exclusions, unit, or procedure differs")
    interpretation_supported = report.get("reported_population_scope") == reproduced.get("dataset_scope")
    if not interpretation_supported:
        limitations.append("reported population interpretation exceeds the supplied dataset scope")
    row = {
        "result_id": result_id,
        "thesis_location": location,
        "source_data": "tests/fixtures/result-trace/observations.csv (3 included rows; 1 excluded row)",
        "procedure": "analysis.py: read-only CSV; include=yes; arithmetic mean",
        "reported_result": {"value": reported_value, "unit": report.get("unit"), "n": report.get("sample_n"), "excluded": report.get("excluded_rows")},
        "reproduced_result": {"value": reproduced_value, "unit": reproduced.get("unit"), "n": reproduced.get("sample_n"), "excluded": reproduced.get("excluded_rows")},
        "discrepancy": {"value_difference": difference, "tolerance": tolerance, "context_matches": context_matches},
        "result_status": status,
        "limitations": "; ".join(limitations) if limitations else "No fixture-specific limitation detected.",
        "downstream_impact": report.get("downstream_impact", "NOT ASSESSED"),
        "trace_chain": ["observations.csv", "include=yes filter", "analysis.py arithmetic mean", "JSON intermediate", location, "reported population interpretation"],
        "interpretation_status": "SUPPORTED WITHIN SUPPLIED SCOPE" if interpretation_supported else "UNSUPPORTED BY SUPPLIED SCOPE",
    }
    if set(row) & REQUIRED_ROW_FIELDS != REQUIRED_ROW_FIELDS:
        raise AssertionError("trace row is missing a canonical matrix field")
    finding = None
    if status == MISMATCH:
        finding = {
            "finding_id": "TD-014",
            "primary_module": "M06",
            "related_modules": "M07, M10, M12",
            "root_cause": "reported mean differs from the supplied calculation",
            "evidence_location": location,
            "corrective_action": "reconcile the table against the supplied included sample and procedure",
        }
    return TraceAssessment(row, finding)


def assess_blocked_execution(blocker: str, identifiable: bool = True) -> str:
    if not identifiable:
        return NOT_ASSESSABLE
    return NOT_REPRODUCIBLE if blocker else NOT_ASSESSABLE


def deduplicate_findings(findings: list[dict[str, str]]) -> list[dict[str, str]]:
    unique: dict[tuple[str, str, str], dict[str, str]] = {}
    for finding in findings:
        key = (finding["root_cause"], finding["evidence_location"], finding["corrective_action"])
        unique.setdefault(key, finding)
    return list(unique.values())


def evaluate_captured_report(markdown: str, report_name: str = "reported-match.json") -> list[str]:
    """Compare a captured agent report row with the independently computed fixture."""
    errors = []
    assessment = evaluate_trace_fixture(FIXTURE_ROOT, report_name)
    text = markdown.split("### Result Traceability & Reproduction Audit", 1)
    if len(text) != 2:
        return ["captured report is missing the result traceability section"]
    matrix = text[1].split("## 7.", 1)[0]
    lines = [line.strip() for line in matrix.splitlines() if line.strip().startswith("|")]
    expected_headers = [
        "Result/claim ID", "Thesis location", "Source data/artifact", "Script/formula/method",
        "Reported result", "Reproduced result", "Discrepancy", "Result status", "Limitations", "Downstream impact",
    ]
    if not lines:
        return ["captured report result matrix is empty"]
    headers = [cell.strip().strip("`") for cell in lines[0].strip("|").split("|")]
    if headers != expected_headers:
        return ["captured report result matrix columns do not match the canonical contract"]
    rows = []
    for line in lines[2:]:
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if len(cells) == len(expected_headers):
            rows.append(dict(zip(expected_headers, cells)))
    matching = [row for row in rows if row["Result/claim ID"] == assessment.row["result_id"]]
    if len(matching) != 1:
        return ["captured report must contain exactly one row for {}".format(assessment.row["result_id"])]
    row = matching[0]
    if row["Result status"] != assessment.row["result_status"]:
        errors.append("captured result status does not match the independent fixture comparison")
    for column, key in (("Thesis location", "thesis_location"), ("Source data/artifact", "source_data"), ("Script/formula/method", "procedure")):
        expected = str(assessment.row[key])
        if expected not in row[column]:
            errors.append("captured {} does not trace the supplied fixture".format(column))
    for column, key in (("Reported result", "reported_result"), ("Reproduced result", "reproduced_result")):
        expected_value = assessment.row[key]["value"]
        numeric_cells = [float(item) for item in re.findall(r"(?<![A-Za-z])[-+]?(?:\d+\.\d+|\d+)(?![A-Za-z])", row[column])]
        if not any(abs(value - expected_value) <= 0.005 for value in numeric_cells):
            errors.append("captured {} does not include the expected numeric value".format(column))
    return errors


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-report", type=Path, help="captured full Markdown report to evaluate")
    parser.add_argument("--fixture-result", choices=sorted(ALLOWED_REPORTS), default="reported-match.json")
    args = parser.parse_args(argv)
    if args.capture_report is None:
        print("CAPTURE EVALUATION BLOCKED: provide --capture-report from an actual target-runtime run")
        return 2
    try:
        if not args.capture_report.is_file() or args.capture_report.stat().st_size > 2_000_000:
            print("CAPTURE EVALUATION FAILED: report is missing or exceeds the 2 MiB limit")
            return 1
        errors = evaluate_captured_report(args.capture_report.read_text(encoding="utf-8"), args.fixture_result)
    except (OSError, UnicodeError, RuntimeError, ValueError) as exc:
        print("CAPTURE EVALUATION FAILED: {}".format(exc))
        return 1
    if errors:
        print("CAPTURE EVALUATION FAILED")
        for error in errors:
            print("- " + error)
        return 1
    print("CAPTURED REPORT PASSED: result matrix matches the independent fixture oracle")
    print("Capture provenance is supplied by the caller and is not independently authenticated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
