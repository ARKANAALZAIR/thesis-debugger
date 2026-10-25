# Quality Gates

## v2.2.8 result-trace gates

- The bundled fixture dataset is recomputed by the hash-pinned analysis script; user-supplied scripts are never invoked by the fixture evaluator.
- Reported value, sample count, exclusions, units, procedure, and tolerance are compared with the recomputed result.
- A deliberate numeric mismatch produces one canonical root-cause finding; duplicate module detections reuse it.
- Missing artifacts, blocked execution, and unsupported interpretation are not conflated with a numerical mismatch.
- A captured full report must be evaluated with `scripts/result_trace_eval.py --capture-report`; local fixture success alone does not establish target-runtime behavior.
- The target-runtime gate remains blocked until actual captures are available and pass.

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


## v2.2.7 Runtime Contract & Scoring Gates

- Full-audit status semantics distinguish diagnostic (`FOUND`, `Error Not Found`, `NOT ASSESSABLE`) from synthesis/action (`COMPLETED`, `NOT ASSESSABLE`, `NOT APPLICABLE`).
- Core missing evidence is never labeled as `Error Not Found`.
- All M01–M22 execute and appear exactly once.
- Unique finding/observation IDs, Primary Modules, severity totals, qualifying finding totals, and observation totals reconcile.
- CRITICAL/HIGH findings pass evidence-strength and alternative-explanation checks.
- Health-score dimensions have documented bases; the canonical audit-integrity reference is loaded before scoring; fixed weights and renormalization are used; insufficient evidence is N/A, not zero.
- Final `Audit Integrity Check` passes.
- `scripts/validate.py` passes.


### v2.2.7 status–finding integrity gate
- A diagnostic `FOUND` status requires a qualifying Primary Finding owned by that module.
- `SUGGESTION`/`INFO` alone cannot force `FOUND`.
- A blocked `POTENTIAL ISSUE` leaves the module `NOT ASSESSABLE`.
- `Error Not Found` requires zero qualifying Primary Findings; INFO/SUGGESTION observations may remain.


### v2.2.7 evidence-boundary + count-derived reconciliation gates
- M02 must be NOT ASSESSABLE when substantive theory/literature/model core evidence is absent from the supplied material.
- A module's Key findings and Observations counts must be derived from actual detailed Primary Module + Type + Severity fields, never manually estimated.
- A mismatch between reported and derived module counts is a hard integrity failure.
- INFO/SUGGESTION observations do not contribute to qualifying finding counts.

### Result trace and reproduction gates
- Material results are traced only as far as the supplied artifacts support.
- Reproduction is attempted only when inputs, dependencies, tools, permissions, and safe execution make it feasible.
- Result-level statuses are exactly `REPRODUCED`, `MISMATCH`, `NOT REPRODUCIBLE WITH SUPPLIED MATERIALS`, or `NOT ASSESSABLE`; they are not module statuses.
- `REPRODUCED` and `MISMATCH` require an execution or independent recalculation that actually completed.
- Rounding and documented non-determinism are considered before a mismatch is reported.
- A supported mismatch has one canonical finding owner and is deduplicated across M06/M07/M10 and related M09/M12 detections.
- Missing inputs or blocked execution are not proof of error or misconduct and do not become `Error Not Found`.
- The report contains a concise Result Traceability & Reproduction Audit matrix, with no invented empty rows.
- `scripts/reproducibility_contract_test.py` passes.
