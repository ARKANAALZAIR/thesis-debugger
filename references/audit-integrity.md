# Audit Integrity & Reconciliation Rules

## Purpose

This reference defines the final self-check performed at the end of every FULL THESIS DEBUG run. It is designed to prevent four common failures: mislabeling missing evidence as "Error Not Found", duplicate findings, unsupported severity escalation, and opaque health scores.

## 1. Module-state semantics

Use exactly one module status:

- `FOUND` — at least one concrete error/issue is supported by the evidence available to the module.
- `Error Not Found` — the module can materially evaluate its diagnostic question with the available evidence and finds no concrete error/issue within that scope.
- `NOT ASSESSABLE` — a required core input is absent, so the module cannot determine whether an error exists. Absence of evidence is not a negative finding.

Coverage is separate from status:

- `FULL` — the module's core checks are materially supported.
- `PARTIAL` — some meaningful checks can run, but one or more sub-checks are blocked.
- `LIMITED` — only a small portion of the module can be tested.

Typical mapping:

| Evidence state | Status | Coverage |
|---|---|---|
| Core evidence present; concrete issue found | FOUND | FULL/PARTIAL |
| Core evidence present; no concrete issue found | Error Not Found | FULL/PARTIAL |
| Core evidence absent; core diagnostic cannot be answered | NOT ASSESSABLE | LIMITED |
| Core evidence partly present; no concrete issue in tested scope | Error Not Found | PARTIAL |

Do not use `Error Not Found` merely because the module was called.

## 2. Finding ownership and deduplication

Each unique underlying issue has exactly one `Finding ID` and one `Primary Module`.

When multiple modules detect the same root cause, deduplicate when these three conditions substantially match:

1. same underlying defect or unresolved decision;
2. same evidence/location or dependency node;
3. materially the same corrective action.

Use `Related Modules` for the other detections.

### Ownership precedence for common overlaps

Prefer the module closest to the root cause:

- definition/construct drift → `M04`
- measurement/operationalization → `M05`
- numeric/sample inconsistency → `M06`
- causality/claim-strength mismatch → `M08`
- substantive evidence support → `M09`
- cross-location contradiction → `M10`
- citation↔reference linkage → `M17`
- plagiarism/paraphrase comparison → `M18`
- provenance/authenticity signal → `M19`

This precedence is a default, not a license to hide materially different problems. If two findings have different roots or actions, keep them separate.

## 3. Severity calibration

Severity combines **impact** and **evidence strength**. A severe hypothetical impact does not justify a severe label when evidence is weak.

- `CRITICAL` → fundamental validity/dependency threat with direct, strong evidence; normally `CONFIRMED ERROR`.
- `HIGH` → material research risk supported by `CONFIRMED ERROR` or strong `LIKELY ISSUE` evidence.
- `MEDIUM` → meaningful but bounded problem, or a well-supported potential issue with limited downstream effect.
- `LOW` → localized traceability, clarity, or minor consistency issue.
- `INFO` → observation without required corrective action.

Before using CRITICAL/HIGH, run the alternative-explanation test. If a plausible, project-consistent explanation remains unresolved, downgrade to a lower-confidence status or request verification rather than overstating certainty.

## 4. Health-score auditability

The health score is diagnostic, not a probability of passing or acceptance.

Use the following fixed dimension weights when all dimensions are present:

| Dimension | Weight |
|---|---:|
| Research Logic | 0.20 |
| Methodology | 0.15 |
| Literature Review | 0.10 |
| Evidence & Citation Integrity | 0.15 |
| Data | 0.10 |
| Consistency | 0.10 |
| Analysis | 0.10 |
| Conclusion Alignment | 0.10 |

Only **assessable** dimensions enter the calculation. Renormalize the weights across the dimensions that have numeric scores. Any dimension that is not materially assessable is `N/A`, not zero.

Formula:

`Overall = round(sum(weight_i × score_i) / sum(weight_i for assessable i))`

Every scored dimension must include a short basis. Do not reverse-engineer scores from finding counts. The score should summarize documented diagnostic judgments; it must not manufacture precision when evidence is weak.

If fewer than four core dimensions are assessable, prefer `Overall: N/A` rather than an unstable aggregate.

## 5. Final reconciliation gate

Before returning the report, verify:

```text
[ ] M01–M22 present exactly once and in canonical order
[ ] Every module has Execution: COMPLETE
[ ] Every module has Status, Coverage, Key findings, Evidence, Verification needed
[ ] NOT ASSESSABLE is used when a core diagnostic input is absent
[ ] Error Not Found is not used as a substitute for missing core evidence
[ ] Every finding ID is unique
[ ] Every finding has exactly one Primary Module
[ ] Related-module references point to existing findings
[ ] Severity totals equal the unique finding list
[ ] Module primary-finding totals equal the unique finding list
[ ] No orphan/phantom finding IDs exist
[ ] No duplicate root cause is counted twice
[ ] CRITICAL/HIGH severity has sufficient confidence/evidence
[ ] Every health-score dimension has a basis or N/A
[ ] Overall score formula is auditable or the score is N/A
[ ] M14 baseline is present even without OLD → NEW input
[ ] Final debug state is present
```
