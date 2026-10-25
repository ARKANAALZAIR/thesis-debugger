# Full-Audit Regression Contract — v2.2.7

Use a readable thesis and the short prompt:

> audit thesis berikut

The run passes only if:

1. FULL THESIS DEBUG is triggered automatically.
2. M01–M22 execute without short-circuiting.
3. M01–M22 each appear exactly once.
4. Every module has `Execution: COMPLETE` plus Status, Coverage, Key findings, Observations, Evidence, Verification needed.
5. A module with adequate core evidence and no error uses `Error Not Found`.
6. A module with missing core diagnostic input uses `NOT ASSESSABLE`, not `Error Not Found`.
7. A partially assessable module can still be `FOUND` when a supported concrete issue exists.
8. Every concrete finding has one unique Finding ID and one Primary Module.
9. Duplicate root causes across modules are deduplicated.
10. Severity totals and module primary-finding totals reconcile.
11. CRITICAL/HIGH findings are not justified by low confidence alone.
12. Health-score dimensions have a basis or N/A, and the overall formula is auditable.
13. M14 includes a baseline dependency scan even without an explicit change.
14. The final Audit Integrity Check is internally consistent.
15. The final debug state is present.

## Runtime regression — status/schema parity

M14/M15/M20/M21/M22 are synthesis/action modules and must use `COMPLETED`, `NOT ASSESSABLE`, or `NOT APPLICABLE`; diagnostic modules must use `FOUND`, `Error Not Found`, or `NOT ASSESSABLE`. A runtime report using `COMPLETED` on M01–M13 or `FOUND` on M20–M22 fails this regression.

## Runtime regression — health-score prerequisite

If `references/audit-integrity.md` is not loaded, the runtime must not emit a numeric Overall Health Score. It must report `Overall: N/A` and identify the missing prerequisite.


## 12. Status–finding consistency regression

### CASE-SF-001 — Suggestion alone cannot produce FOUND
- Diagnostic module has one Primary Finding.
- Finding Type = `SUGGESTION`, Severity = `LOW`.
- Expected: `Error Not Found` when the core diagnostic question is materially assessed and no concrete error exists.
- A runtime report using `FOUND` fails this regression.

### CASE-SF-002 — Potential issue blocked by missing core evidence
- Diagnostic module has a `POTENTIAL ISSUE`, but required evidence to determine whether the issue is real is absent.
- Expected: `NOT ASSESSABLE`.
- The potential item may remain as a verification observation but cannot make the module `FOUND`.

### CASE-SF-003 — Related finding is not primary ownership
- A finding lists a module only under `Related Modules`.
- Expected: the module does not become `FOUND` merely because it is referenced.

### CASE-SF-004 — FOUND requires qualifying primary finding
- Diagnostic module status = `FOUND`.
- Expected: at least one Primary Finding owned by that module with Type `CONFIRMED ERROR`, `LIKELY ISSUE`, or `POTENTIAL ISSUE` and Severity `CRITICAL/HIGH/MEDIUM/LOW`.
- Otherwise the integrity gate must fail and require repair.


## Evidence-boundary regression

If a theory/literature/model section is absent from the supplied audit material, M02 must be `NOT ASSESSABLE`, not `FOUND` from an inferred theory gap. A module with two qualifying primary findings must report `Key findings: 2`; the final integrity gate must derive and verify that count from the detailed finding objects.

## Reproducibility & Result Trace Audit regression

The result-level statuses `REPRODUCED`, `MISMATCH`, `NOT REPRODUCIBLE WITH SUPPLIED MATERIALS`, and `NOT ASSESSABLE` are not module statuses. The report includes a concise result trace matrix for material results only, and never invents empty rows. A blocked or incomplete reproduction states the specific limitation and is not proof of error or misconduct.

| Case | Supplied evidence and action | Expected result-level behavior |
|---|---|---|
| RT-001 | Supplied synthetic dataset and inspected calculation procedure reproduce a reported mean | `REPRODUCED`; record the data and procedure actually used |
| RT-002 | A completed calculation differs materially from the reported table after sample, transformations, rounding, and alternatives are checked | `MISMATCH`; link one canonical finding with evidence, impact, and verification action |
| RT-003 | Raw data or analysis script required for the identified result is not supplied | `NOT REPRODUCIBLE WITH SUPPLIED MATERIALS`; name the missing artifact and do not call the result false |
| RT-004 | Required dependency is unavailable or inspected execution is blocked | `NOT REPRODUCIBLE WITH SUPPLIED MATERIALS`; report `NOT RUN` and the precise blocker |
| RT-005 | Difference is explained by reported precision or documented stochastic/platform variation | `REPRODUCED` when agreement is within a justified tolerance/range; explain the harmless variation |
| RT-006 | Statistic is recalculated but its causal or theoretical interpretation exceeds the evidence | Result is `REPRODUCED`; assess unsupported interpretation separately under the existing module/findings contract |
| RT-007 | One reproduced mismatch is detected by M06 and M10, with materially identical root cause and corrective action | Reuse one finding ID and one Primary Module; other modules are related, not duplicate findings |

If a result cannot be identified or its scope cannot be determined from supplied material, use `NOT ASSESSABLE`, not `NOT REPRODUCIBLE WITH SUPPLIED MATERIALS`. Missing evidence must not become `Error Not Found`.
