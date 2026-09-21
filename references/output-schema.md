# Output Schema

## Full report

```markdown
# THESIS DEBUG REPORT

## 1. Executive Summary

## 2. Research Health Score
Overall: NN/100 (diagnostic only)

| Dimension | Score | Confidence |
|---|---:|---|
| Research Logic | | |
| Methodology | | |
| Literature Review | | |
| Evidence & Citation Integrity | | |
| Data | | |
| Consistency | | |
| Analysis | | |
| Conclusion Alignment | | |

## 3. Critical Errors

## 4. High Priority Issues

## 5. Medium / Low Issues

## 6. Literature Review Audit

## 7. Evidence Audit

## 8. Reference & Citation Integrity

## 9. Plagiarism / Paraphrase Risk

## 10. Academic Authenticity Risk

## 11. Consistency Audit

## 12. Dependency Analysis

## 13. Change Impact

## 14. Research Risks

## 15. Action Plan

## 16. Supervisor Questions

## 17. Defense Risks
```

## Finding object

```text
ID:
Type:
Severity:
Confidence:
Location:
Problem:
Evidence:
Reasoning:
Impact:
Recommended Action:
```

## Minimal output

For “only critical errors,” output only CRITICAL findings plus a short count of other findings. Do not hide material caveats.


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
