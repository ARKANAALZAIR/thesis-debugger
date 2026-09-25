# THESIS DEBUG REPORT

Audit Mode: FULL THESIS DEBUG
Trigger: Broad thesis audit request
Execution: All supported modules (M01–M22)

## 1. Executive Summary

**Diagnostic state:** [brief assessment]

**Finding counts:** 🔴 Critical: [n] · 🟠 High: [n] · 🟡 Medium: [n] · 🔵 Low: [n] · ⚪ Info: [n]

## 2. Research Health Score

**Overall:** [score]/100 or `N/A` — diagnostic indicator, not a probability of acceptance.

**Score formula:** Fixed weights from `references/audit-integrity.md`; omit N/A dimensions and renormalize weights.
**Minimum aggregate rule:** Prefer `N/A` when fewer than four core dimensions are assessable.

| Dimension | Score | Confidence | Basis |
|---|---:|---|---|
| Research Logic | | | |
| Methodology | | | |
| Literature Review | | | |
| Evidence & Citation Integrity | | | |
| Data | | | |
| Consistency | | | |
| Analysis | | | |
| Conclusion Alignment | | | |

## 3. Finding Summary

List every unique finding count by severity. Counts must reconcile with the detailed finding objects.

## 4. Module Status Matrix

Every row below is mandatory and must appear exactly once.

```text
MODULE ID: M01
MODULE: Research structure & RQ/objective alignment
Execution: COMPLETE
Status: FOUND | Error Not Found | NOT ASSESSABLE
Coverage: FULL | PARTIAL | LIMITED
Key findings: [n]
Evidence: [location/evidence or NONE FOUND]
Verification needed: [text or NONE]
```

Repeat the same block for **M02 through M22**, using the canonical module registry in `references/output-schema.md`.

The final report must literally contain these 22 module blocks (one each, in this order):

### M01 — Research structure & RQ/objective alignment
[status block]

### M02 — Theory / hypothesis / model alignment
[status block]

### M03 — Methodology / research-question fit
[status block]

### M04 — Variable and definition drift
[status block]

### M05 — Measurement & operationalization
[status block]

### M06 — Sample / dataset / numeric consistency
[status block]

### M07 — Statistical interpretation
[status block]

### M08 — Logic / causality
[status block]

### M09 — Evidence / claim support
[status block]

### M10 — Internal consistency / contradictions
[status block]

### M11 — Scope / completeness
[status block]

### M12 — Results / discussion / conclusion alignment
[status block]

### M13 — Research dead ends / fragile dependencies
[status block]

### M14 — Change Impact Analysis baseline
[status block]

### M15 — Supervisor feedback translator
[status block]

### M16 — Literature Review Auditor
[status block]

### M17 — Reference & Citation Integrity
[status block]

### M18 — Plagiarism / Paraphrase Risk
[status block]

### M19 — Academic Authenticity / Provenance Risk
[status block]

### M20 — Research Decisions Ledger
[status block]

### M21 — Defense Risk Simulation
[status block]

### M22 — Prioritized Action Plan
[status block]

## 5. Detailed Findings

For every finding:

```text
Finding ID: TD-###
Primary Module: M##
Related Modules: [optional]
Type:
Status: CONFIRMED ERROR | LIKELY ISSUE | POTENTIAL ISSUE | SUGGESTION | INFO
Severity: CRITICAL | HIGH | MEDIUM | LOW | INFO
Confidence:
Location:
Problem:
Evidence:
Reasoning:
Impact:
Recommended Action:
Verification Needed:
```

## 6. Evidence Audit

| Claim | Evidence | Support Status | Risk | Location |
|---|---|---|---|---|
| | | | | |

## 7. Dependency Analysis

Show research chains, broken links, fragile dependencies, and high-sensitivity nodes.

## 8. Change Impact Baseline

If no explicit change was supplied, state:

`Baseline only — no explicit change supplied.`

Then show dependency-sensitive nodes and downstream review implications.

## 9. Literature Review Audit

Summarize synthesis, gap, contribution, coverage boundaries, and evidence balance.

## 10. Reference & Citation Integrity

Summarize citation↔reference matching, metadata consistency, and claim-source traceability.

## 11. Plagiarism / Paraphrase Risk

Distinguish internal self-overlap from external comparison. Never treat similarity as proof without sufficient evidence.

## 12. Academic Authenticity / Provenance Risk

Report observable signals and alternative explanations. Do not infer AI authorship from style alone.

## 13. Consistency Audit

| Item | Location A | Location B | Assessment | Action |
|---|---|---|---|---|
| | | | | |

## 14. Research Decisions Ledger

| Decision ID | Decision | Reason | Evidence | Affected components | Open questions |
|---|---|---|---|---|---|
| | | | | | |

## 15. Research Dead Ends / Fragile Dependencies

Identify research questions that may not be answerable with the stated design/evidence and fragile chains that could break downstream conclusions.

## 16. Supervisor Feedback Audit

If no supervisor feedback is supplied:

`Status: Error Not Found`  
`Coverage: LIMITED`  
`Verification needed: Supervisor feedback or revision notes required.`

Do not invent supervisor intent.

## 17. Defense Risks

Generate examiner-style questions tied to actual findings and fragile dependencies.

## 18. Prioritized Action Plan

Order actions by severity and dependency. Separate confirmed fixes from verification tasks and suggestions.

## 19. Verification / Coverage Limits

Explicitly list unavailable evidence and what each limitation prevents the audit from proving.

## 20. Final Debug State

Use exactly one:

- `CRITICAL ERRORS FOUND`
- `MATERIAL ERRORS FOUND`
- `NO CONCRETE ERROR FOUND IN AVAILABLE EVIDENCE`

## 21. Audit Integrity Check

```text
Audit Integrity Check
Modules Executed: 22/22
Modules Found: [n]
Modules Error Not Found: [n]
Modules Not Assessable: [n]
Unique Findings: [n]
Severity Reconciliation: PASS
Module Finding Reconciliation: PASS
Finding ID Reconciliation: PASS
Primary-Module Reconciliation: PASS
Severity Calibration: PASS
Health Score Auditability: PASS | N/A
```

### Final reconciliation gate

```text
[ ] M01–M22 all executed and shown exactly once
[ ] Every module has Status + Coverage + Key findings + Evidence + Verification
[ ] NOT ASSESSABLE is used when a core diagnostic input is absent
[ ] Error Not Found is not used as a substitute for missing core evidence
[ ] Every finding has one unique ID and one Primary Module
[ ] Related-module references resolve to existing findings
[ ] Duplicate root causes are not counted twice
[ ] Severity totals reconcile to unique findings
[ ] Module primary-finding totals reconcile to unique findings
[ ] CRITICAL/HIGH findings pass confidence/evidence calibration
[ ] Every score has a basis or N/A
[ ] Overall score formula is auditable or N/A
[ ] Change Impact baseline is present
[ ] Final Debug State is present
[ ] Audit Integrity Check is present and internally consistent
```
