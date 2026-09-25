# Auto-Trigger Full Audit Contract

## User input

**Attachment:** `thesis.pdf`

**Prompt:**

> audit thesis berikut

## Required behavior

The skill must automatically enter **FULL THESIS DEBUG** mode. The user must not have to type `/full-audit` or enumerate modules.

The final report must include all 22 module status blocks, even when a module has no finding. A module with no concrete error uses:

`Status: Error Not Found`

If evidence is unavailable for that module, the report must also state the coverage limitation instead of implying global certainty.

The audit should still perform useful internal checks where possible. For example, the plagiarism/paraphrase module should check internal self-overlap even when no external comparison source is supplied.

## Acceptance checks

- Full-audit mode triggered from the short prompt.
- All modules executed.
- All modules shown in the report.
- No long prompt required.
- No module silently skipped.
- Finding counts reconcile.
- Missing evidence is disclosed.
