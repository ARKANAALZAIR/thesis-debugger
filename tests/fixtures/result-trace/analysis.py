#!/usr/bin/env python3
"""Trusted fixture analysis: average included rows from observations.csv."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> int:
    with (ROOT / "context.json").open(encoding="utf-8") as handle:
        context = json.load(handle)
    values = []
    excluded = 0
    with (ROOT / "observations.csv").open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["value", "include"]:
            raise ValueError("unexpected fixture columns")
        for row in reader:
            if row["include"] == "yes":
                value = float(row["value"])
                if not math.isfinite(value):
                    raise ValueError("non-finite observation")
                values.append(value)
            elif row["include"] == "no":
                excluded += 1
            else:
                raise ValueError("include must be yes or no")
            if len(values) + excluded > 10000:
                raise ValueError("fixture row limit exceeded")
    if not values:
        raise ValueError("no included observations")
    result = {
        "result_id": context["result_id"],
        "thesis_location": context["thesis_location"],
        "reported_procedure": "read-only CSV; include=yes; arithmetic mean",
        "procedure_id": context["procedure_id"],
        "reproduced_value": sum(values) / len(values),
        "sample_n": len(values),
        "excluded_rows": excluded,
        "unit": context["unit"],
        "dataset_scope": context["dataset_scope"],
    }
    print(json.dumps(result, allow_nan=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
