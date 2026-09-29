#!/usr/bin/env python3
"""v2.2.6 status/finding contract regression tests.

This is a static contract test: it validates the invariant that diagnostic
module status cannot claim FOUND without a qualifying primary finding, and
that suggestion/info-only observations do not force FOUND.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

VALID_TYPES = {"CONFIRMED ERROR", "LIKELY ISSUE", "POTENTIAL ISSUE"}
VALID_SEVERITIES = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}


@dataclass(frozen=True)
class Finding:
    primary_module: str
    finding_type: str
    severity: str


def qualifying_primary_findings(module_id: str, findings: Iterable[Finding]) -> list[Finding]:
    return [
        f for f in findings
        if f.primary_module == module_id
        and f.finding_type in VALID_TYPES
        and f.severity in VALID_SEVERITIES
    ]


def validate_diag_status(module_id: str, status: str, findings: Iterable[Finding], core_assessable: bool) -> bool:
    findings = list(findings)
    qualifying = qualifying_primary_findings(module_id, findings)
    if status == "FOUND":
        return core_assessable and bool(qualifying)
    if status == "Error Not Found":
        return core_assessable and not qualifying
    if status == "NOT ASSESSABLE":
        return not core_assessable
    return False



def derive_counts(module_id: str, findings: Iterable[Finding]) -> tuple[int, int]:
    items = [f for f in findings if f.primary_module == module_id]
    qualifying = sum(1 for f in items if f.finding_type in VALID_TYPES and f.severity in VALID_SEVERITIES)
    observations = sum(1 for f in items if f.finding_type in {"SUGGESTION", "INFO"})
    return qualifying, observations


def validate_reported_counts(module_id: str, reported_key_findings: int, reported_observations: int, findings: Iterable[Finding]) -> bool:
    qualifying, observations = derive_counts(module_id, findings)
    return reported_key_findings == qualifying and reported_observations == observations


def main() -> int:
    cases = [
        ("SF-001", validate_diag_status("M06", "FOUND", [Finding("M06", "SUGGESTION", "LOW")], True), False),
        ("SF-002", validate_diag_status("M02", "FOUND", [Finding("M02", "POTENTIAL ISSUE", "MEDIUM")], False), False),
        ("SF-003", validate_diag_status("M10", "FOUND", [Finding("M08", "CONFIRMED ERROR", "HIGH")], True), False),
        ("SF-004", validate_diag_status("M06", "Error Not Found", [], True), True),
        ("SF-005", validate_diag_status("M08", "FOUND", [Finding("M08", "CONFIRMED ERROR", "CRITICAL")], True), True),
        ("SF-006", validate_diag_status("M02", "NOT ASSESSABLE", [Finding("M02", "POTENTIAL ISSUE", "MEDIUM")], False), True),
        ("SF-007", validate_diag_status("M06", "Error Not Found", [Finding("M06", "INFO", "INFO")], True), True),
        ("SF-008", validate_diag_status("M07", "Error Not Found", [Finding("M07", "SUGGESTION", "LOW")], True), True),
        ("SF-009", validate_diag_status("M02", "FOUND", [Finding("M02", "LIKELY ISSUE", "HIGH")], False), False),
        ("SF-010", validate_reported_counts("M11", 1, 0, [Finding("M11", "LIKELY ISSUE", "HIGH"), Finding("M11", "POTENTIAL ISSUE", "MEDIUM")]), False),
        ("SF-011", validate_reported_counts("M11", 2, 0, [Finding("M11", "LIKELY ISSUE", "HIGH"), Finding("M11", "POTENTIAL ISSUE", "MEDIUM")]), True),
        ("SF-012", validate_reported_counts("M06", 0, 1, [Finding("M06", "INFO", "INFO")]), True),
    ]
    for case_id, actual, expected in cases:
        if actual != expected:
            print(f"FAIL {case_id}: got {actual}, expected {expected}")
            return 1
        print(f"PASS {case_id}")
    print("PASS: status/finding contract regression (including INFO/SUGGESTION observation cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
