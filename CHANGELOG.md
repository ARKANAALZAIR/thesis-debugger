# Changelog

## 2.2.2 — Final production hardening

- Enforced exact 21-section broad-audit rendering and M01–M22 module order.
- Made the canonical finding schema mandatory for every finding severity.
- Hardened final self-checks against status/class drift, duplicate IDs, orphan references, and score/reconciliation inconsistencies.

## 2.2.1 — Repository baseline


- Added a canonical M01–M22 module registry with deterministic names and IDs.
- Enforced non-short-circuit execution for broad thesis audits.
- Added `Execution: COMPLETE` to every module status block.
- Added canonical finding ownership via `Primary Module` and unique finding IDs.
- Added severity and module-count reconciliation rules to prevent inconsistent totals.
- Clarified `FOUND` vs `Error Not Found` semantics and coverage boundaries.
- Made the Change Impact baseline explicitly mandatory even without an `OLD → NEW` change.
- Added health-score integrity rules so missing evidence is not silently scored as zero.
- Expanded validation to check the canonical module registry, output schema, template, and regression contract.
- Added two activation/regression benchmark cases for count reconciliation and all-module completeness.

## 2.2.0 — Automatic Full-Audit Activation

- Broad requests such as `audit thesis berikut` now automatically trigger FULL THESIS DEBUG.
- Removed the need for users to enumerate audit modules or type a long prompt for the standard thesis audit.
- Added a 22-module full-audit contract covering logic, methodology, evidence, consistency, literature, citation integrity, paraphrase risk, academic authenticity, change impact, feedback, decisions, defense, and action planning.
- Every full audit now shows an explicit status for every module.
- Added `Status: Error Not Found` for modules that complete without finding a concrete error in the available evidence.
- Added explicit coverage/verification fields so `Error Not Found` is not mistaken for proof that the thesis is globally error-free.
- Added a baseline Change Impact scan even when no explicit `OLD → NEW` change is supplied.
- Added an auto-trigger benchmark case for the short prompt workflow.


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
