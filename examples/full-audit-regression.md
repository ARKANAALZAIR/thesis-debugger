# Full-Audit Regression Contract — v2.2.2

Use a readable thesis and the short prompt:

> audit thesis berikut

The run passes only if:

1. FULL THESIS DEBUG is triggered automatically.
2. M01–M22 execute without short-circuiting.
3. M01–M22 each appear exactly once.
4. Every module has `Execution: COMPLETE` plus Status, Coverage, Key findings, Evidence, Verification needed.
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
