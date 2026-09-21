# Plagiarism / Paraphrase Risk Detection

## Purpose
Identify passages that may require source-attribution or originality review. This module is a **risk detector**, not a legal or disciplinary plagiarism adjudicator.

## Evidence ladder

### EXACT
Substantial word-for-word overlap between a supplied source passage and target passage. Report the matched locations and whether quotation/attribution is present.

### NEAR-EXACT
Minor word substitutions, reordered phrases, or surface edits preserve most wording/structure.

### CLOSE PARAPHRASE
The target preserves distinctive source ideas, sentence structure, ordering, or uncommon phrasing with insufficient attribution/independent synthesis.

### PATCHWRITING
Target mixes source wording with light substitutions or copied fragments instead of independent paraphrase.

### UNATTRIBUTED QUOTATION
Distinctive source wording appears without clear quotation/attribution.

### SELF-OVERLAP
The author's own supplied documents reuse substantial text across thesis, paper, proposal, or earlier draft. This is not automatically misconduct; it may be legitimate reuse, but should be checked against venue/institution rules.

## Required controls
- Compare supplied text against actual supplied source text when possible.
- Quote only the minimum evidence necessary.
- Separate “same wording” from “same idea.”
- Consider common technical phrases and field-standard terminology before escalating.
- Consider whether quotation marks, citation, and page/section attribution are present.

## Output status
Use `RISK`, `REVIEW NEEDED`, or `SUPPORTED CONCERN`. Use `CONFIRMED MISCONDUCT` only when the evidence and task context genuinely establish it; do not infer intent.

## Limits
If no source corpus or comparison text is supplied, do not claim a document is plagiarism-free or plagiarized. A similarity-style signal alone does not establish misconduct.
