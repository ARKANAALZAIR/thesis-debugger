#!/usr/bin/env python3
"""Static regression fixtures for the v2.2.6 runtime reconciliation contract.

This does not execute Claude. It validates the exact edge cases that previously
escaped the runtime self-check: M02 with missing theory evidence and module-count
mismatch when a module owns multiple qualifying findings.
"""
from __future__ import annotations

from dataclasses import dataclass

VALID_TYPES = {"CONFIRMED ERROR", "LIKELY ISSUE", "POTENTIAL ISSUE"}
VALID_SEVERITIES = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}

@dataclass(frozen=True)
class Item:
    primary_module: str
    kind: str
    severity: str

def derive_key_findings(module: str, items: list[Item]) -> int:
    return sum(1 for x in items if x.primary_module == module and x.kind in VALID_TYPES and x.severity in VALID_SEVERITIES)

def derive_observations(module: str, items: list[Item]) -> int:
    return sum(1 for x in items if x.primary_module == module and x.kind in {"INFO", "SUGGESTION"})

def m02_status(core_theory_present: bool, qualifying_findings: int) -> str:
    if not core_theory_present:
        return "NOT ASSESSABLE"
    return "FOUND" if qualifying_findings else "Error Not Found"


def main() -> int:
    # M02: missing core theory evidence must force NOT ASSESSABLE even if a
    # model tries to create a likely issue from the hypothesis alone.
    assert m02_status(False, 1) == "NOT ASSESSABLE"
    assert m02_status(False, 0) == "NOT ASSESSABLE"
    assert m02_status(True, 1) == "FOUND"
    assert m02_status(True, 0) == "Error Not Found"
    # Count integrity: two qualifying M11 findings means Key findings MUST be 2.
    items = [
        Item("M11", "LIKELY ISSUE", "HIGH"),
        Item("M11", "POTENTIAL ISSUE", "MEDIUM"),
        Item("M11", "SUGGESTION", "LOW"),
    ]
    assert derive_key_findings("M11", items) == 2
    assert derive_observations("M11", items) == 1
    assert derive_key_findings("M06", [Item("M06", "INFO", "INFO")]) == 0
    print("PASS: runtime reconciliation fixtures")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
