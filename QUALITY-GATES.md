# Quality Gates

Run `python scripts/validate.py` before every release.

Model-level evaluation must separately measure:
- critical/high recall
- finding precision
- false-positive rate
- traceability coverage
- change-impact coverage
- incomplete-input behavior
- integrity refusal behavior
- literature-review coverage/gap precision
- citation-reference linkage accuracy
- source-support accuracy
- paraphrase-risk precision with supplied source text
- authenticity-risk false-positive rate and calibration

A static pass validates packaging only; it does not prove the model is correct or error-free.


For the automatic full-audit contract, also validate:
- broad prompt activation without a module checklist;
- all 22 module status blocks present;
- no silent module omission;
- `Error Not Found` semantics;
- limited-evidence disclosure;
- finding-count reconciliation;
- baseline change-impact scan even without an explicit change.


## v2.2.6 Runtime Contract & Scoring Gates

- Full-audit status semantics distinguish diagnostic (`FOUND`, `Error Not Found`, `NOT ASSESSABLE`) from synthesis/action (`COMPLETED`, `NOT ASSESSABLE`, `NOT APPLICABLE`).
- Core missing evidence is never labeled as `Error Not Found`.
- All M01–M22 execute and appear exactly once.
- Unique finding/observation IDs, Primary Modules, severity totals, qualifying finding totals, and observation totals reconcile.
- CRITICAL/HIGH findings pass evidence-strength and alternative-explanation checks.
- Health-score dimensions have documented bases; the canonical audit-integrity reference is loaded before scoring; fixed weights and renormalization are used; insufficient evidence is N/A, not zero.
- Final `Audit Integrity Check` passes.
- `scripts/validate.py` passes.


### v2.2.6 status–finding integrity gate
- A diagnostic `FOUND` status requires a qualifying Primary Finding owned by that module.
- `SUGGESTION`/`INFO` alone cannot force `FOUND`.
- A blocked `POTENTIAL ISSUE` leaves the module `NOT ASSESSABLE`.
- `Error Not Found` requires zero qualifying Primary Findings; INFO/SUGGESTION observations may remain.


### v2.2.6 evidence-boundary + count-derived reconciliation gates
- M02 must be NOT ASSESSABLE when substantive theory/literature/model core evidence is absent from the supplied material.
- A module's Key findings and Observations counts must be derived from actual detailed Primary Module + Type + Severity fields, never manually estimated.
- A mismatch between reported and derived module counts is a hard integrity failure.
- INFO/SUGGESTION observations do not contribute to qualifying finding counts.
