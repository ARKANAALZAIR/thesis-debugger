# Audit Integrity & Reconciliation Rules

## Purpose

This reference defines the final self-check performed at the end of every FULL THESIS DEBUG run. It is designed to prevent four common failures: mislabeling missing evidence as "Error Not Found", duplicate findings, unsupported severity escalation, and opaque health scores.

## 1. Module-state semantics

Use status taxonomy by module class:

**Diagnostic modules (M01–M13, M16–M19):**
- `FOUND` — at least one concrete error/issue is supported by the evidence available to the module.
- `Error Not Found` — the module can materially evaluate its diagnostic question with the available evidence and finds no concrete error/issue within that scope.
- `NOT ASSESSABLE` — a required core input is absent, so the module cannot determine whether an error exists. Absence of evidence is not a negative finding.

**Synthesis/action modules (M14–M15, M20–M22):**
- `COMPLETED` — the synthesis/control task completed from available evidence.
- `NOT ASSESSABLE` — a required core input prevents completion.
- `NOT APPLICABLE` — the synthesis/control task does not materially apply.

Coverage is separate from status:

- `FULL` — the module's core checks are materially supported.
- `PARTIAL` — some meaningful checks can run, but one or more sub-checks are blocked.
- `LIMITED` — only a small portion of the module can be tested.

Typical diagnostic mapping:

| Evidence state | Status | Coverage |
|---|---|---|
| Core evidence present; concrete issue found | FOUND | FULL/PARTIAL |
| Core evidence present; no concrete issue found | Error Not Found | FULL/PARTIAL |
| Core evidence absent; core diagnostic cannot be answered | NOT ASSESSABLE | LIMITED |
| Core evidence partly present; no concrete issue in tested scope | Error Not Found | PARTIAL |

Do not use `Error Not Found` merely because the diagnostic module was called. Do not use `COMPLETED` on a diagnostic module or `FOUND` / `Error Not Found` on a synthesis/action module.

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

## 2.1 Status–finding consistency gate

Before the final reconciliation totals are accepted, validate every DIAG module against its **Primary Findings** and the module's evidence boundary:

- `FOUND` requires materially assessable core evidence **and** at least one qualifying Primary Finding owned by that module.
- A qualifying Primary Finding must be Type `CONFIRMED ERROR`, `LIKELY ISSUE`, or `POTENTIAL ISSUE` with Severity `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`.
- `SUGGESTION` and `INFO` are non-qualifying observations; they cannot by themselves produce `FOUND`.
- A `POTENTIAL ISSUE` or `LIKELY ISSUE` that cannot be resolved because core evidence is missing must leave the module `NOT ASSESSABLE`; it may remain only as a verification observation.
- `Error Not Found` requires materially assessable core evidence and zero qualifying Primary Findings, but may carry non-qualifying INFO/SUGGESTION observations.
- A finding/observation appearing only under `Related Modules` does not count as Primary ownership.

### Core-evidence boundary rule

Absence from a supplied excerpt, synopsis, or partial package is not evidence that the underlying thesis lacks the component. When the supplied material is insufficient to answer a module's core diagnostic question, use `NOT ASSESSABLE`.

**M02-specific rule:** substantive theory, literature, conceptual-model, or equivalent theoretical-basis material is core evidence for theory/hypothesis/model alignment. If none is supplied, M02 must be `NOT ASSESSABLE`; a suspected theory gap may be logged as a non-qualifying verification observation but cannot create `FOUND`.

## 3. Severity calibration

Severity combines **impact** and **evidence strength**. A severe hypothetical impact does not justify a severe label when evidence is weak.

- `CRITICAL` → fundamental validity/dependency threat with direct, strong evidence; normally `CONFIRMED ERROR`.
- `HIGH` → material research risk supported by `CONFIRMED ERROR` or strong `LIKELY ISSUE` evidence.
- `MEDIUM` → meaningful but bounded problem, or a well-supported potential issue with limited downstream effect.
- `LOW` → localized traceability, clarity, or minor consistency issue.
- `INFO` → observation without required corrective action.
- `SUGGESTION` / `INFO` are observations, not qualifying diagnostic findings.

Before using CRITICAL/HIGH, run the alternative-explanation test. If a plausible, project-consistent explanation remains unresolved, downgrade to a lower-confidence status or request verification rather than overstating certainty.

## 4. Health-score auditability

The health score is diagnostic, not a probability of passing or acceptance.

Use the following fixed dimension weights when all dimensions are present. **This reference must be loaded before calculating any numeric Health Score.**

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

If this reference has not been loaded, report `Overall: N/A` rather than approximating. If fewer than four core dimensions are assessable, prefer `Overall: N/A` rather than an unstable aggregate.

## 5. Final reconciliation gate

### 5.1 Count-derived ledger (mandatory)

The report must derive module counts from the detailed finding/observation objects, not from manually typed summaries. For every module, calculate:

```text
Key findings = count(Primary Module == module AND Type in {CONFIRMED ERROR, LIKELY ISSUE, POTENTIAL ISSUE} AND Severity in {CRITICAL, HIGH, MEDIUM, LOW})
Observations = count(Primary Module == module AND Type in {INFO, SUGGESTION})
```

Then assert exact equality with the module status block. Any mismatch is a reconciliation failure and must be repaired before `PASS` is allowed.

Before returning the report, verify:

```text
[ ] M01–M22 present exactly once and in canonical order
[ ] Every module has the correct Class and role-specific status taxonomy
[ ] Every module has Execution: COMPLETE
[ ] Every module has Class, role-appropriate Status, Coverage, Key findings, Observations, Evidence, Verification needed
[ ] NOT ASSESSABLE is used when a core diagnostic input is absent
[ ] Error Not Found is not used as a substitute for missing core evidence
[ ] Every finding ID is unique
[ ] Every finding has exactly one Primary Module
[ ] Every DIAG `FOUND` module owns at least one qualifying Primary Finding
[ ] No DIAG `FOUND` module is supported only by SUGGESTION/INFO
[ ] Any blocked DIAG POTENTIAL ISSUE leaves the module NOT ASSESSABLE
[ ] Every DIAG `Error Not Found` module owns zero qualifying Primary Findings; INFO/SUGGESTION observations may remain
[ ] Related-module references point to existing findings
[ ] Severity totals equal the unique finding list
[ ] Key-finding totals + observation totals reconcile to the unique ID totals
[ ] No orphan/phantom finding IDs exist
[ ] No duplicate root cause is counted twice
[ ] CRITICAL/HIGH severity has sufficient confidence/evidence
[ ] Every health-score dimension has a basis or N/A
[ ] Overall score formula is auditable or the score is N/A
[ ] M14 baseline is present even without OLD → NEW input
[ ] Final debug state is present
```
