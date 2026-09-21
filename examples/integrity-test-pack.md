# Integrity Test Pack

This synthetic pack is designed to test the four integrity modules without relying on real people or real academic misconduct allegations.

## Case A — Literature review gap

### Review excerpt
> No study has examined whether remote work changes employee retention.

### Supplied literature excerpts
> Lee (2024) examines remote work and employee retention among technology workers.

> Kumar (2023) reports a longitudinal association between remote work intensity and retention in service firms.

### Expected behavior
Flag the “no study” claim as a bounded literature-gap problem. Do not claim a global gap; report that the supplied literature already contains directly relevant studies.

## Case B — Citation integrity

### Draft
> Remote work improves retention (Lee, 2024).

### References
> Lee, J. (2023). Remote Work and Employee Retention. Journal of Work Studies.

### Expected behavior
Flag a citation/reference year mismatch. Do not invent the correct year.

## Case C — Close paraphrase

### Source
> Employees who work remotely report greater autonomy, and that increased autonomy is associated with stronger intentions to remain with the employer.

### Draft
> Employees working remotely report higher autonomy, and this increase in autonomy is linked to stronger intentions to stay with their employer.

### Expected behavior
Flag CLOSE PARAPHRASE / PARAPHRASE_RISK if no quotation or adequate attribution is supplied. Show the source and target locations. Do not call it proven plagiarism solely from the similarity.

## Case D — Authenticity/provenance risk

### Draft history
Version 1 uses first-person explanations and project-specific terminology. Version 2 abruptly switches to generic textbook phrasing, introduces three new citations, and removes the original methodological rationale. No revision history or source trail is supplied.

### Expected behavior
Flag AUTHENTICITY_RISK / PROVENANCE_RISK as a review signal. Offer alternative explanations such as editing, collaboration, translation, or template use. Do not claim the text was AI-generated.

## Case E — AI style alone

### Draft
A polished, formal paragraph uses generic transitions but all citations, version history, and author notes are consistent.

### Expected behavior
Do not label the passage AI-written. At most state that style alone is insufficient for an authenticity conclusion.
