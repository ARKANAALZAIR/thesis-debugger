# Changelog

## 2.2.0 — Automatic Full-Audit Activation

- Broad requests such as `audit thesis berikut` now automatically trigger FULL THESIS DEBUG.
- Removed the need for users to enumerate audit modules or type a long prompt for the standard thesis audit.
- Added a 22-module full-audit contract covering logic, methodology, evidence, consistency, literature, citation integrity, paraphrase risk, academic authenticity, change impact, feedback, decisions, defense, and action planning.
- Every full audit now shows an explicit status for every module.
- Added `Status: Error Not Found` for modules that complete without finding a concrete error in the available evidence.
- Added explicit coverage/verification fields so `Error Not Found` is not mistaken for proof that the thesis is globally error-free.
- Added a baseline Change Impact scan even when no explicit `OLD → NEW` change is supplied.
- Added an auto-trigger benchmark case for the short prompt workflow.

# Changelog

## 2.1.0 — Research Integrity & Literature Audit Expansion

- Added Literature Review Auditor for scope, synthesis, evidence balance, gap logic, and literature-to-research alignment.
- Added Reference & Citation Integrity Checker for citation↔reference linkage, metadata consistency, citation drift, quotation attribution, and claim-source traceability.
- Added Plagiarism / Paraphrase Risk Detection with exact, near-exact, close-paraphrase, patchwriting, quotation, and self-overlap checks.
- Added Academic Authenticity / AI-Generated Writing Risk review based on provenance and observable signals; explicitly avoids treating style as proof of AI authorship.
- Added integrity-specific finding types and output fields.
- Expanded the benchmark suite to 39 synthetic cases covering literature, citation integrity, paraphrase risk, and authenticity-risk behavior.
- Added false-positive controls and verification requirements for the new integrity modules.


## 1.0.0 — Initial release

- Added production-oriented `thesis-debugger` Claude Skill.
- Added research-system model and dependency graph.
- Added nine-pass diagnostic workflow.
- Added change impact analysis as the signature feature.
- Added evidence-first and false-positive controls.
- Added methodology, evidence, statistical, consistency, and scope diagnostics.
- Added research decision ledger.
- Added research dead-end detection.
- Added supervisor feedback translation and impact analysis.
- Added defense simulator workflow.
- Added severity taxonomy and heuristic health score.
- Added incomplete-document handling and academic-integrity safeguards.
- Added the original synthetic benchmark suite.
