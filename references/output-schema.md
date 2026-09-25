# Output Schema

## Broad-audit report contract

When the user provides a thesis/research document and makes a broad audit request such as “audit thesis berikut”, generate a **FULL THESIS DEBUG** report.

The top of the report should contain:

```markdown
# THESIS DEBUG REPORT

Audit Mode: FULL THESIS DEBUG
Trigger: Broad thesis audit request
Execution: All supported modules

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
```

## Module Status Matrix

Every full audit must list these modules exactly once:

1. Research structure & RQ/objective alignment
2. Theory / hypothesis / model alignment
3. Methodology / research-question fit
4. Variable and definition drift
5. Measurement & operationalization
6. Sample / dataset / numeric consistency
7. Statistical interpretation
8. Logic / causality
9. Evidence / claim support
10. Internal consistency / contradictions
11. Scope / completeness
12. Results / discussion / conclusion alignment
13. Research dead ends / fragile dependencies
14. Change Impact Analysis baseline
15. Supervisor feedback translator
16. Literature Review Auditor
17. Reference & Citation Integrity
18. Plagiarism / Paraphrase Risk
19. Academic Authenticity / Provenance Risk
20. Research Decisions Ledger
21. Defense Risk Simulation
22. Prioritized Action Plan

For each module use:

```text
MODULE: [name]
Status: FOUND | Error Not Found
Coverage: FULL | PARTIAL | LIMITED
Key findings: [count or concise statement]
Evidence: [locations/evidence or NONE FOUND]
Verification needed: [text or NONE]
```

### Status semantics

- `FOUND` = one or more concrete errors/issues were identified.
- `Error Not Found` = the module was executed and no concrete error was found in the available evidence.
- `Coverage: LIMITED` or `PARTIAL` must be used when missing inputs reduce what can be verified. `Error Not Found` never means “the thesis is proven error-free.”

## Finding object

```text
ID:
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

## Module-to-finding coverage

The final report must make it possible to trace each finding back to one of the 22 modules and to a source location when available.

## Detailed findings

Show CRITICAL/HIGH findings in full. Show MEDIUM/LOW/INFO findings in concise form unless needed for traceability.

## Integrity-specific finding fields

For `PARAPHRASE_RISK` / plagiarism-review findings:

```text
Overlap Type:
Source Location:
Target Location:
Matched Evidence:
Attribution Status:
Confidence:
Verification Needed:
```

For `AUTHENTICITY_RISK` / `PROVENANCE_RISK` findings:

```text
Observed Signal:
Location:
Alternative Explanations:
Corroborating Evidence:
Confidence:
Human Verification:
```

## Change Impact baseline

Even when no explicit `OLD → NEW` change is supplied, report the most dependency-sensitive nodes and what would likely need review if they changed. If a real change is supplied, include `OLD → NEW`, downstream traversal, affected components, severity, and validation gates.

## Final debug state

Use one of:

- `CRITICAL ERRORS FOUND`
- `MATERIAL ERRORS FOUND`
- `NO CONCRETE ERROR FOUND IN AVAILABLE EVIDENCE`

Never claim the research is globally error-free.
