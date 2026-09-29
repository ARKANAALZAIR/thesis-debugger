# Full-Audit Regression Contract — v2.2.6

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


## v2.2.6 evidence-boundary regression

If a theory/literature/model section is absent from the supplied audit material, M02 must be `NOT ASSESSABLE`, not `FOUND` from an inferred theory gap. A module with two qualifying primary findings must report `Key findings: 2`; the final integrity gate must derive and verify that count from the detailed finding objects.
