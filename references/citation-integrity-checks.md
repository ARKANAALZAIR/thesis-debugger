# Reference & Citation Integrity Checker

## Purpose
Verify that citations and bibliography entries are traceable, internally consistent, and attached to the claims they are supposed to support. Bibliographic correctness and substantive support are separate checks.

## Checks

### Citation ↔ reference linkage
- in-text citation with no matching reference entry;
- reference entry never cited;
- duplicate or near-duplicate references;
- inconsistent author/year labels;
- ambiguous same-author same-year citations;
- chapter/section citations that point to the wrong source.

### Bibliographic metadata integrity
When metadata is supplied, compare author names, year, title, venue, volume/issue, pages, DOI/URL, and edition. Flag internal mismatches. Do not silently “fix” metadata from memory.

### Claim ↔ source integrity
Check whether the cited source actually supports the nearby claim and whether the claim strength exceeds the source. Distinguish:
`PRESENT` ≠ `TRACEABLE` ≠ `SUPPORTING`.

### Quotation integrity
Check quotation marks, page/section locators when supplied, attribution, and whether quoted wording is represented as quotation rather than paraphrase.

### Citation drift
Across revisions, check whether claims retained a citation that no longer matches the modified text, or whether a citation was dropped while the claim remained.

### Source-status concerns
If the supplied material explicitly identifies a retraction, expression of concern, correction, or invalidated source, surface it. Do not infer publication status without evidence.

## Finding classes
- `CITATION_INTEGRITY_ERROR` — bibliographic/linkage defect with evidence.
- `CITATION_SUPPORT_RISK` — citation is present but substantive support is unclear or weaker than the claim.
- `TRACEABILITY_ERROR` — source/claim path cannot be reconstructed from the supplied material.

## Limits
Without source metadata or source text, say `VERIFICATION NEEDED`. Do not invent DOI, titles, authors, or publication status.
