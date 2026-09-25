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
