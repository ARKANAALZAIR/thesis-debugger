#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import re, sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md","README.md","LICENSE","CHANGELOG.md","CONTRIBUTING.md","QUALITY-GATES.md",
    "VERSION","manifest.json","RELEASE-MANIFEST.json","PRODUCTION-READINESS.md",
    "references/audit-framework.md","references/error-taxonomy.md","references/methodology-checks.md",
    "references/evidence-checks.md","references/literature-review-checks.md","references/citation-integrity-checks.md",
    "references/paraphrase-risk-checks.md","references/authenticity-checks.md","references/statistical-checks.md",
    "references/consistency-checks.md","references/dependency-model.md","references/severity-rubric.md",
    "references/output-schema.md","references/audit-integrity.md","references/reproducibility-checks.md",
    "templates/debug-report.md","templates/decision-log.md","templates/action-plan.md",
    "scripts/status_contract_test.py","scripts/report_reconciliation_test.py","scripts/spec_hygiene_test.py",
    "scripts/reproducibility_contract_test.py","scripts/result_trace_eval.py",
    "tests/fixtures/result-trace/analysis.py","tests/fixtures/result-trace/observations.csv",
    "tests/fixtures/result-trace/context.json","tests/fixtures/result-trace/reported-match.json",
    "tests/fixtures/result-trace/reported-mismatch.json",
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
if not re.match(r"\A---\nname: [a-z0-9-]+\ndescription: .+\n(?:version: .+\n)?---\n",s): errors.append("invalid frontmatter")
for phrase in [
    "FULL THESIS DEBUG","audit thesis berikut","Status: Error Not Found","NOT ASSESSABLE",
    "all 22 modules","Production hardening — v2.2.8 canonical execution contract","Observations:",
    "Finding/observation IDs are globally unique","Severity calibration","Health-score integrity",
    "Audit Integrity Check", "Class: DIAG", "Class: SYN", "Reference loading is mandatory",
    "Result Traceability & Reproduction Audit", "NOT REPRODUCIBLE WITH SUPPLIED MATERIALS"]:
    if phrase not in s: errors.append(f"missing contract phrase: {phrase}")
canonical_text = "\n".join([
    (ROOT/"SKILL.md").read_text(encoding="utf-8"),
    (ROOT/"references/audit-integrity.md").read_text(encoding="utf-8"),
    (ROOT/"references/output-schema.md").read_text(encoding="utf-8")
])
for phrase in [
    "Status–finding consistency gate",
    "FOUND` requires at least one **Primary Finding**",
    "SUGGESTION` and `INFO` cannot by themselves make a DIAG module `FOUND"
]:
    if phrase not in canonical_text: errors.append(f"missing cross-file contract phrase: {phrase}")
for mid,name in MODULES:
    if mid not in s or name not in s: errors.append(f"missing canonical module registry entry: {mid} {name}")
for f in required:
    if not (ROOT/f).is_file(): errors.append("missing "+f)

try:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    release = json.loads((ROOT / "RELEASE-MANIFEST.json").read_text(encoding="utf-8"))
    frontmatter = re.search(r"^version:\s*(\S+)\s*$", s, re.M)
    if not frontmatter or frontmatter.group(1) != version:
        errors.append("SKILL.md version does not match VERSION")
    if manifest.get("version") != version or release.get("version") != version:
        errors.append("manifest versions do not match VERSION")
    actual_hash = hashlib.sha256((ROOT / "SKILL.md").read_bytes()).hexdigest()
    if release.get("skill_sha256") != actual_hash:
        errors.append("RELEASE-MANIFEST skill_sha256 does not match SKILL.md")
    if manifest.get("capture_evaluator") != "python scripts/result_trace_eval.py --capture-report REPORT.md":
        errors.append("manifest does not identify the captured-report evaluator")
except (OSError, json.JSONDecodeError) as exc:
    errors.append("release metadata is invalid: " + str(exc))

try:
    from result_trace_eval import TRUSTED_ANALYSIS_SHA256
    actual_analysis_hash = hashlib.sha256((ROOT / "tests/fixtures/result-trace/analysis.py").read_bytes()).hexdigest()
    if actual_analysis_hash != TRUSTED_ANALYSIS_SHA256:
        errors.append("pinned fixture analysis hash does not match analysis.py")
    for filename in ("context.json", "reported-match.json", "reported-mismatch.json"):
        json.loads((ROOT / "tests/fixtures/result-trace" / filename).read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError, ImportError) as exc:
    errors.append("result-trace fixture is invalid: " + str(exc))
schema=(ROOT/"references/output-schema.md").read_text(encoding="utf-8")
for mid,name in MODULES:
    if mid not in schema or name not in schema: errors.append(f"output schema missing module: {mid}")
for phrase in ["Status: FOUND | Error Not Found | NOT ASSESSABLE", "COMPLETED", "Audit Integrity Check", "Total unique finding/observation IDs", "Health-score integrity"]:
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
    for required_id in [*(f"AUTO-{i:03d}" for i in range(1,12)), *(f"RT-{i:03d}" for i in range(1,8))]:
        if required_id not in ids: errors.append(f"missing benchmark case: {required_id}")
if errors:
    print("FAIL")
    print("\n".join(errors)); sys.exit(1)
print("PASS")
print("required_files",len(required))
print("total_files",sum(1 for p in ROOT.rglob("*") if p.is_file()))
print("benchmark_cases",len(rows)-1)
print("canonical_modules",len(MODULES))
