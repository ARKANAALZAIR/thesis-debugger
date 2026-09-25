# Severity Rubric

Severity is based on research risk, evidence strength, and downstream impact.

## 🔴 CRITICAL

Use when the finding may threaten a fundamental research claim, validity, or dependency chain and evidence is strong enough to justify escalation.

Examples:
- core RQ cannot be answered by stated design;
- fabricated/contradictory data would invalidate a key result;
- conclusion directly contradicts a decisive result without explanation;
- a required dependency is broken across the central model.

## 🟠 HIGH

Likely to trigger serious supervisor/reviewer concern but may be repairable without invalidating the whole study.

Examples:
- material unsupported claim;
- major variable-definition drift;
- repeated causal overclaim;
- unexplained major sample discrepancy.

## 🟡 MEDIUM

Important issue with limited or localized consequences.

## 🔵 LOW

Minor issue or local clarity/traceability problem.

## ⚪ INFO

Useful observation with no required action.

## Confidence interaction

Do not promote a low-confidence finding to CRITICAL merely because the hypothetical impact is large. A high-impact uncertainty should be reported as a potential risk until evidence improves.


## Final hardening rules

Severity must not be inferred from hypothetical impact alone.

Before assigning CRITICAL or HIGH, verify:

1. The evidence is direct enough for the stated confidence.
2. A plausible project-specific alternative explanation has been checked.
3. The issue is an error/risk rather than a preference or generic recommendation.
4. The claimed downstream impact is actually connected by a supported dependency.

A low-confidence issue with a potentially large impact should remain a potential/verification item until the evidence strengthens.
