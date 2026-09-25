#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md","README.md","LICENSE","CHANGELOG.md","CONTRIBUTING.md","QUALITY-GATES.md",
    "references/audit-framework.md","references/error-taxonomy.md","references/methodology-checks.md",
    "references/evidence-checks.md","references/literature-review-checks.md","references/citation-integrity-checks.md",
    "references/paraphrase-risk-checks.md","references/authenticity-checks.md","references/statistical-checks.md",
    "references/consistency-checks.md","references/dependency-model.md","references/severity-rubric.md",
    "references/output-schema.md","references/audit-integrity.md",
    "templates/debug-report.md","templates/decision-log.md","templates/action-plan.md",
    "examples/broken-thesis.md","examples/expected-debug-report.md","examples/integrity-test-pack.md",
    "examples/auto-trigger-contract.md","examples/benchmark.md","examples/benchmark-manifest.csv",
    "examples/full-audit-regression.md","scripts/validate.py"
]
MODULES = [
    ("M01", "Research structure & RQ/objective alignment"),("M02", "Theory / hypothesis / model alignment"),
    ("M03", "Methodology / research-question fit"),("M04", "Variable and definition drift"),
    ("M05", "Measurement & operationalization"),("M06", "Sample / dataset / numeric consistency"),
    ("M07", "Statistical interpretation"),("M08", "Logic / causality"),
    ("M09", "Evidence / claim support"),("M10", "Internal consistency / contradictions"),
    ("M11", "Scope / completeness"),("M12", "Results / discussion / conclusion alignment"),
    ("M13", "Research dead ends / fragile dependencies"),("M14", "Change Impact Analysis baseline"),
    ("M15", "Supervisor feedback translator"),("M16", "Literature Review Auditor"),
    ("M17", "Reference & Citation Integrity"),("M18", "Plagiarism / Paraphrase Risk"),
    ("M19", "Academic Authenticity / Provenance Risk"),("M20", "Research Decisions Ledger"),
    ("M21", "Defense Risk Simulation"),("M22", "Prioritized Action Plan")]
errors=[]
s=(ROOT/"SKILL.md").read_text(encoding="utf-8")
if not re.match(r"\A---\nname: [a-z0-9-]+\ndescription: .+\n---\n",s): errors.append("invalid frontmatter")
for phrase in [
    "FULL THESIS DEBUG","audit thesis berikut","Status: Error Not Found","NOT ASSESSABLE",
    "all 22 modules","Production hardening — v2.2.2 canonical execution contract",
    "Finding IDs are globally unique","Severity calibration","Health-score integrity",
    "Audit Integrity Check"]:
    if phrase not in s: errors.append(f"missing contract phrase: {phrase}")
for mid,name in MODULES:
    if mid not in s or name not in s: errors.append(f"missing canonical module registry entry: {mid} {name}")
for f in required:
    if not (ROOT/f).is_file(): errors.append("missing "+f)
schema=(ROOT/"references/output-schema.md").read_text(encoding="utf-8")
for mid,name in MODULES:
    if mid not in schema or name not in schema: errors.append(f"output schema missing module: {mid}")
for phrase in ["Status: FOUND | Error Not Found | NOT ASSESSABLE","Audit Integrity Check","Total unique findings","Health-score integrity"]:
    if phrase not in schema: errors.append(f"schema missing: {phrase}")
template=(ROOT/"templates/debug-report.md").read_text(encoding="utf-8")
for mid,name in MODULES:
    if mid not in template: errors.append(f"template missing module: {mid}")
for phrase in ["NOT ASSESSABLE","Audit Integrity Check","Score formula","Module Finding Reconciliation"]:
    if phrase not in template: errors.append(f"template missing: {phrase}")
rows=(ROOT/"examples/benchmark-manifest.csv").read_text(encoding="utf-8").splitlines()
if len(rows)<51: errors.append(f"benchmark has fewer than 50 cases: {len(rows)-1}")
if rows:
    header=rows[0]; ids=[r.split(',',1)[0] for r in rows[1:] if r.strip()]
    if len(ids)!=len(set(ids)): errors.append("benchmark contains duplicate case ids")
    if header!="id,category,title,expected_severity": errors.append("unexpected benchmark manifest header")
    for required_id in [f"AUTO-{i:03d}" for i in range(1,12)]:
        if required_id not in ids: errors.append(f"missing benchmark case: {required_id}")
if errors:
    print("FAIL")
    print("\n".join(errors)); sys.exit(1)
print("PASS")
print("required_files",len(required))
print("total_files",sum(1 for p in ROOT.rglob("*") if p.is_file()))
print("benchmark_cases",len(rows)-1)
print("canonical_modules",len(MODULES))
