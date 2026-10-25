#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
repro = (ROOT / "references/reproducibility-checks.md").read_text(encoding="utf-8")
errors=[]
prod = skill.split("## Production hardening",1)[-1].split("## ",1)[0]
letters = re.findall(r"^### ([A-Z])\.", prod, flags=re.M)
if len(letters) != len(set(letters)):
    errors.append(f"duplicate production-hardening letters: {letters}")
for marker in ["10. Academic Authenticity Risk","11. Consistency Audit","12. Dependency Analysis","17. Defense Risks"]:
    if marker in skill:
        errors.append(f"orphan legacy report fragment remains: {marker}")
for phrase in [
    "Observations: [integer count of non-qualifying INFO/SUGGESTION PRIMARY observations]",
    "sum(M01…M22 Observations)",
    "M02 hard gate",
    "Result Traceability & Reproduction Audit"
]:
    if phrase not in skill:
        errors.append(f"missing canonical observation contract: {phrase}")
for phrase in [
    "REPRODUCED",
    "MISMATCH",
    "NOT REPRODUCIBLE WITH SUPPLIED MATERIALS",
    "NOT ASSESSABLE",
    "exactly one of these labels",
    "do not run code blindly"
]:
    if phrase not in repro:
        errors.append(f"missing result trace contract: {phrase}")
if errors:
    print("FAIL")
    print("\n".join(errors))
    raise SystemExit(1)
print("PASS: spec hygiene")
