#!/usr/bin/env python3
from pathlib import Path
import re, sys, zipfile

ROOT = Path(__file__).resolve().parents[1]
required = [
"SKILL.md","README.md","LICENSE","CHANGELOG.md","CONTRIBUTING.md","QUALITY-GATES.md",
"references/audit-framework.md","references/error-taxonomy.md","references/methodology-checks.md",
"references/evidence-checks.md","references/literature-review-checks.md","references/citation-integrity-checks.md",
"references/paraphrase-risk-checks.md","references/authenticity-checks.md","references/statistical-checks.md",
"references/consistency-checks.md","references/dependency-model.md","references/severity-rubric.md","references/output-schema.md",
"templates/debug-report.md","templates/decision-log.md","templates/action-plan.md",
"examples/broken-thesis.md","examples/expected-debug-report.md","examples/integrity-test-pack.md","examples/auto-trigger-contract.md",
"examples/benchmark.md","examples/benchmark-manifest.csv","scripts/validate.py"]
errors=[]
s=(ROOT/"SKILL.md").read_text(encoding="utf-8")
if not re.match(r"\A---\nname: [a-z0-9-]+\ndescription: .+\n---\n",s): errors.append("invalid frontmatter")
m=re.search(r"^description: (.+)$",s,re.M)
if m and len(m.group(1))>1024: errors.append("description too long")
required_phrases = [
    "FULL THESIS DEBUG",
    "audit thesis berikut",
    "Status: Error Not Found",
    "all 22 modules",
    "Change Impact Analysis baseline",
]
for phrase in required_phrases:
    if phrase not in s:
        errors.append(f"missing auto-full-audit contract phrase: {phrase}")
for f in required:
    if not (ROOT/f).is_file(): errors.append("missing "+f)
rows=(ROOT/"examples/benchmark-manifest.csv").read_text(encoding="utf-8").splitlines()
if len(rows)<41: errors.append("benchmark has fewer than 40 cases")
if rows:
    header=rows[0]
    ids=[r.split(',',1)[0] for r in rows[1:] if r.strip()]
    if len(ids)!=len(set(ids)): errors.append("benchmark contains duplicate case ids")
    if header!="id,category,title,expected_severity": errors.append("unexpected benchmark manifest header")
if errors:
    print("FAIL")
    print("\n".join(errors)); sys.exit(1)
print("PASS")
print("required_files",len(required))
print("total_files",sum(1 for p in ROOT.rglob("*") if p.is_file()))
print("benchmark_cases",len(rows)-1)
