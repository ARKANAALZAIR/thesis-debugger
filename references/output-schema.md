# Output Schema

## Broad-audit report contract

When the user provides a thesis/research document and makes a broad audit request such as **“audit thesis berikut”**, generate a **FULL THESIS DEBUG** report automatically.

The report must be auditable for execution completeness, evidence boundaries, finding identity, severity, and score calculation.

```markdown
# THESIS DEBUG REPORT

Audit Mode: FULL THESIS DEBUG
Trigger: Broad thesis audit request
Execution: All supported modules (M01–M22)

## 1. Executive Summary
## 2. Research Health Score
## 3. Finding Summary
## 4. Module Status Matrix
## 5. Detailed Findings
## 6. Evidence Audit
## 7. Dependency Analysis
## 8. Change Impact Baseline
## 9. Literature Review Audit
## 10. Reference & Citation Integrity
## 11. Plagiarism / Paraphrase Risk
## 12. Academic Authenticity / Provenance Risk
## 13. Consistency Audit
## 14. Research Decisions Ledger
## 15. Research Dead Ends / Fragile Dependencies
## 16. Supervisor Feedback Audit
## 17. Defense Risks
## 18. Prioritized Action Plan
## 19. Verification / Coverage Limits
## 20. Final Debug State
## 21. Audit Integrity Check
```

## Canonical module status matrix

Class semantics:
- DIAG modules: M01–M13, M16–M19 → `FOUND` / `Error Not Found` / `NOT ASSESSABLE`.
- SYN modules: M14–M15, M20–M22 → `COMPLETED` / `NOT ASSESSABLE` / `NOT APPLICABLE`.
Never use `FOUND` or `Error Not Found` as a proxy for successful synthesis/control completion.

Every full audit must list these modules **exactly once and in order**:

| ID | Module |
|---|---|
| M01 | Research structure & RQ/objective alignment |
| M02 | Theory / hypothesis / model alignment |
| M03 | Methodology / research-question fit |
| M04 | Variable and definition drift |
| M05 | Measurement & operationalization |
| M06 | Sample / dataset / numeric consistency |
| M07 | Statistical interpretation |
| M08 | Logic / causality |
| M09 | Evidence / claim support |
| M10 | Internal consistency / contradictions |
| M11 | Scope / completeness |
| M12 | Results / discussion / conclusion alignment |
| M13 | Research dead ends / fragile dependencies |
| M14 | Change Impact Analysis baseline |
| M15 | Supervisor feedback translator |
| M16 | Literature Review Auditor |
| M17 | Reference & Citation Integrity |
| M18 | Plagiarism / Paraphrase Risk |
| M19 | Academic Authenticity / Provenance Risk |
| M20 | Research Decisions Ledger |
| M21 | Defense Risk Simulation |
| M22 | Prioritized Action Plan |

Each module must emit:

```text
MODULE ID: M01
MODULE: [canonical name]
Execution: COMPLETE
Status: FOUND | Error Not Found | NOT ASSESSABLE  # DIAG only
Coverage: FULL | PARTIAL | LIMITED
Key findings: [integer count of qualifying PRIMARY diagnostic findings owned by this module]
Observations: [integer count of PRIMARY INFO/SUGGESTION observations owned by this module]
Evidence: [locations/evidence or NONE FOUND]
Verification needed: [text or NONE]
```

## Status semantics

- `FOUND` = one or more concrete errors/issues were identified and are attributable to the module.
- `Error Not Found` = the module's core diagnostic question was materially assessable and no concrete error/issue was found in the available evidence.
- `NOT ASSESSABLE` = a required core input is absent, so the module cannot determine whether an error exists. This is not a clean bill of health.
- `Coverage: FULL` = core checks materially supported.
- `Coverage: PARTIAL` = core diagnostic can run but one or more sub-checks are blocked.
- `Coverage: LIMITED` = evidence is too sparse for a reliable core determination; normally pair with `NOT ASSESSABLE`.

Do not use `Error Not Found` as a substitute for missing core evidence.

## Canonical finding object

Every detailed finding must contain:

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

Every finding must have exactly one Primary Module. Related modules reuse the same Finding ID.

## Status–finding consistency

Before reconciliation totals are accepted:

- `FOUND` requires at least one **Primary Finding** owned by that module.
- A qualifying diagnostic Primary Finding uses Type `CONFIRMED ERROR`, `LIKELY ISSUE`, or `POTENTIAL ISSUE` and Severity `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`.
- `SUGGESTION` and `INFO` cannot by themselves make a DIAG module `FOUND`.
- A blocked `POTENTIAL ISSUE` leaves the DIAG module `NOT ASSESSABLE`.
- A DIAG module marked `Error Not Found` must own zero **qualifying** Primary Findings; non-qualifying INFO/SUGGESTION observations may remain. Related-module references do not count.

## Reconciliation invariants

The final report must satisfy:

```text
Total unique finding/observation IDs = count(unique IDs)
Total unique finding/observation IDs = Critical + High + Medium + Low + Info
Total qualifying diagnostic findings = sum(Key findings for M01–M22)
Total observations = sum(Observations for M01–M22)
Every module Finding ID reference resolves to an existing finding
No underlying root cause is counted twice

**Count-source rule:** module `Key findings` and `Observations` values are derived from the detailed objects' actual `Primary Module`, `Type`, and `Severity` fields. They must never be manually estimated or copied from a narrative summary. If any module count does not equal the derived ledger count, `Module Finding Reconciliation` is `FAIL` until corrected.

**Evidence-boundary rule:** when a module's core diagnostic input is absent from the supplied material, use `NOT ASSESSABLE`. In particular, M02 requires substantive theory/literature/model evidence; a theory gap may be noted for verification, but cannot become a qualifying finding or `FOUND` without that core evidence.
```

## Severity calibration

Severity is a categorical risk label. It is not a measure of model quality and must not be derived mechanically from finding counts.

- CRITICAL: direct strong evidence + fundamental validity/dependency threat.
- HIGH: confirmed or strongly supported likely issue + material downstream impact.
- MEDIUM: bounded but meaningful concern or well-supported potential issue.
- LOW: localized traceability/clarity/minor consistency issue.
- SUGGESTION: non-qualifying improvement recommendation.
- INFO: observation with no required corrective action.

Low-confidence findings must not be promoted to CRITICAL/HIGH solely because a hypothetical impact would be large.

## Health-score integrity

Use the fixed weights and formula from `references/audit-integrity.md` when an overall score is reported. Only materially assessable dimensions enter the calculation; weights are renormalized. Missing evidence is `N/A`, never zero.

**Reference-loading prerequisite:** Before computing any numeric health score, the runtime must load `references/audit-integrity.md`. If that file is unavailable or not loaded, report `Overall: N/A` and do not substitute an unweighted or approximate score.

Every numeric dimension must include:

```text
Score: XX/100
Confidence: HIGH | MEDIUM | LOW
Basis: [short evidence-based basis]
```

Prefer `Overall: N/A` when fewer than four core dimensions are assessable.

## Change Impact baseline

M14 runs even when no explicit change is supplied. State:

`Baseline only — no explicit change supplied.`

Then identify high-sensitivity nodes and downstream review implications without inventing an `OLD → NEW` change.

## Audit Integrity Check

Every FULL THESIS DEBUG report must end with:

```text
Audit Integrity Check
Modules Executed: 22/22
Diagnostic Modules Found: N
Diagnostic Modules Error Not Found: N
Modules Not Assessable: N
Synthesis/Action Modules Completed: N
Modules Not Applicable: N
Unique Findings: N
Severity Reconciliation: PASS
Module Finding Reconciliation: PASS
Finding ID Reconciliation: PASS
Primary-Module Reconciliation: PASS
Severity Calibration: PASS
Health Score Auditability: PASS | N/A
```

Never claim `22/22` unless every module block is actually present.

## Verification / coverage limits

State missing source text, raw data, results/discussion, supervisor feedback, external comparison material, or other evidence boundaries that materially limit a module.

## Final debug state

Use exactly one:

- `CRITICAL ERRORS FOUND`
- `MATERIAL ERRORS FOUND`
- `NO CONCRETE ERROR FOUND IN AVAILABLE EVIDENCE`

Never claim the research is globally error-free.
