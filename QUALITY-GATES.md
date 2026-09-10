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

A static pass validates packaging only; it does not prove the model is correct or error-free.
