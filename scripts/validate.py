from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
EXPECTED='2.2.2'
MODULES=[('M01','Research structure & RQ/objective alignment'),('M02','Theory / hypothesis / model alignment'),('M03','Methodology / research-question fit'),('M04','Variable and definition drift'),('M05','Measurement & operationalization'),('M06','Sample / dataset / numeric consistency'),('M07','Statistical interpretation'),('M08','Logic / causality'),('M09','Evidence / claim support'),('M10','Internal consistency / contradictions'),('M11','Scope / completeness'),('M12','Results / discussion / conclusion alignment'),('M13','Research dead ends / fragile dependencies'),('M14','Change Impact Analysis baseline'),('M15','Supervisor feedback translator'),('M16','Literature Review Auditor'),('M17','Reference & Citation Integrity'),('M18','Plagiarism / Paraphrase Risk'),('M19','Academic Authenticity / Provenance Risk'),('M20','Research Decisions Ledger'),('M21','Defense Risk Simulation'),('M22','Prioritized Action Plan')]
errors=[]
for f in ['SKILL.md','README.md','LICENSE','CHANGELOG.md','CONTRIBUTING.md','QUALITY-GATES.md','VERSION','manifest.json','RELEASE-MANIFEST.json','references/output-schema.md','references/audit-integrity.md','templates/debug-report.md','scripts/validate.py']:
    if not (ROOT/f).is_file(): errors.append('missing '+f)
if (ROOT/'VERSION').read_text().strip()!=EXPECTED: errors.append('VERSION mismatch')
meta=json.loads((ROOT/'manifest.json').read_text())
if meta.get('version')!=EXPECTED: errors.append('manifest version mismatch')
sk=(ROOT/'SKILL.md').read_text(encoding='utf-8')
for q in ['Runtime render-conformance contract','Every module must emit exactly one block','External-artifact gate','Canonical finding ownership','Class: SYNTHESIS','COMPLETED | NOT ASSESSABLE | NOT APPLICABLE']:
    if q not in sk: errors.append('SKILL missing '+q)
# exact section order in canonical template
rep=(ROOT/'templates/debug-report.md').read_text(encoding='utf-8')
heads=re.findall(r'^## (\d+)\. (.+)$',rep,re.M)
expected_titles=['Executive Summary','Research Health Score','Finding Summary','Module Status Matrix','Detailed Findings','Evidence Audit','Dependency Analysis','Change Impact Baseline','Literature Review Audit','Reference & Citation Integrity','Plagiarism / Paraphrase Risk','Academic Authenticity / Provenance Risk','Consistency Audit','Research Decisions Ledger','Research Dead Ends / Fragile Dependencies','Supervisor Feedback Audit','Defense Risks','Prioritized Action Plan','Verification / Coverage Limits','Final Debug State','Audit Integrity Check']
expected=[(str(i),t) for i,t in enumerate(expected_titles,1)]
if heads[:21]!=expected: errors.append('template exact 21-section order mismatch')
# exact M01-M22 once and in order
ids=re.findall(r'^### (M\d{2}) — ',rep,re.M)
if ids!=[f'M{i:02d}' for i in range(1,23)]: errors.append('template M01-M22 order/count mismatch')
# finding schema exact order in SKILL
seq=['Finding ID: TD-###','Primary Module: M##','Related Modules: [optional]','Type:','Status: CONFIRMED ERROR | LIKELY ISSUE | POTENTIAL ISSUE | SUGGESTION | INFO','Severity: CRITICAL | HIGH | MEDIUM | LOW | INFO','Confidence:','Location:','Problem:','Evidence:','Reasoning:','Impact:','Recommended Action:','Verification Needed:']
fb=sk[sk.find('### E. Canonical finding ownership and reconciliation'):]; pos=-1
for q in seq:
 z=fb.find(q)
 if z<0: errors.append('finding field missing '+q)
 elif z<pos: errors.append('finding field out of order '+q)
 pos=z
# module names in output schema and template
os=(ROOT/'references/output-schema.md').read_text(encoding='utf-8')
for mid,name in MODULES:
 if mid not in os or name not in os: errors.append('output schema missing '+mid)
if 'Audit Integrity Check' not in rep or 'Final reconciliation gate' not in rep: errors.append('template integrity/reconciliation missing')
if '### v'+EXPECTED not in (ROOT/'README.md').read_text(encoding='utf-8'): errors.append('README current version missing')
if not (ROOT/'CHANGELOG.md').read_text().startswith('# Changelog\n\n## '+EXPECTED+' '): errors.append('CHANGELOG current release missing')
if errors:
 print('FAIL'); print('\n'.join(errors)); raise SystemExit(1)
print('PASS'); print('version',EXPECTED); print('render_contract PASS'); print('module_registry PASS'); print('finding_contract PASS'); print('status_contract PASS'); print('integrity_contract PASS')
