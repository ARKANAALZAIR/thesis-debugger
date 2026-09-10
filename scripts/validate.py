#!/usr/bin/env python3
from pathlib import Path
import re, sys, zipfile

ROOT = Path(__file__).resolve().parents[1]
required = ["SKILL.md","README.md","LICENSE","CHANGELOG.md","CONTRIBUTING.md",
"references/audit-framework.md","references/error-taxonomy.md","references/methodology-checks.md",
"references/evidence-checks.md","references/statistical-checks.md","references/consistency-checks.md",
"references/dependency-model.md","references/severity-rubric.md","references/output-schema.md",
"templates/debug-report.md","templates/decision-log.md","templates/action-plan.md",
"examples/benchmark.md","examples/benchmark-manifest.csv"]
errors=[]
s=(ROOT/"SKILL.md").read_text(encoding="utf-8")
if not re.match(r"\A---\nname: [a-z0-9-]+\ndescription: .+\n---\n",s): errors.append("invalid frontmatter")
m=re.search(r"^description: (.+)$",s,re.M)
if m and len(m.group(1))>1024: errors.append("description too long")
for f in required:
    if not (ROOT/f).is_file(): errors.append("missing "+f)
rows=(ROOT/"examples/benchmark-manifest.csv").read_text(encoding="utf-8").splitlines()
if len(rows)<21: errors.append("benchmark has fewer than 20 cases")
if errors:
    print("FAIL")
    print("\n".join(errors)); sys.exit(1)
print("PASS")
print("required_files",len(required))
print("benchmark_cases",len(rows)-1)
