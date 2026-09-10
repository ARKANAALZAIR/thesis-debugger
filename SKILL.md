---
name: thesis-debugger
description: Audit theses, dissertations, research papers, proposals, datasets, research notes, and supervisor feedback as one connected research system. Use this skill whenever a user asks to debug, audit, validate, stress-test, find contradictions, check evidence, assess methodology, trace conclusions, analyze research changes, prepare for a defense, or identify hidden research weaknesses. Prioritize high-signal findings, traceability, low false positives, and especially change impact analysis.
---

# Thesis Debugger

## Mission

Treat academic research as a connected system, not a collection of chapters. Debug the dependency chain from research questions through theory, hypotheses, variables, measurement, method, data, analysis, results, discussion, and conclusions.

The defining capability is **change impact analysis**: when a research decision changes, identify downstream components that require review without blindly rewriting them.

## Non-negotiable behavior

1. **Evidence first.** For every significant finding, identify location, evidence, reasoning, severity, impact, and recommended action.
2. **Never invent.** Never fabricate sources, citations, DOI, statistics, data, supervisor instructions, methods, or results. Say `INSUFFICIENT EVIDENCE` when support is missing.
3. **Separate error from suggestion.** A preference is not an error. Use `ERROR`, `POTENTIAL ISSUE`, or `SUGGESTION` deliberately.
4. **Traceability.** Prefer page, section, table, figure, paragraph, variable, or file references. If exact location is unavailable, say so.
5. **Preserve intent.** Diagnose before redesigning. Say “potential methodological concern” rather than “wrong” when context is incomplete.
6. **Control false positives.** Do not label discrepancies as errors until plausible explanations have been considered.
7. **Be methodology-aware.** Practices differ across quantitative, qualitative, mixed-methods, experimental, observational, case-study, review, and theoretical research.
8. **Respect source hierarchy.** If supplied, university policy outranks generic convention; supervisor instructions outrank generic advice; project decisions outrank generic recommendations.
9. **Academic integrity.** Never help fabricate data, significance, results, citations, or evidence.
10. **Concise by default.** Surface critical/high findings first; offer deeper passes when requested.

## Activation and request routing

Infer the operation from natural language. Supported aliases include:

- `/debug` or “debug my thesis” → full diagnostic
- `/health` → health score and highest-risk findings
- `/impact` → change impact analysis
- `/contradictions` → cross-document consistency audit
- `/evidence` → claim/evidence audit
- `/methodology` → methodology/RQ/design audit
- `/data` → dataset/report consistency and statistical interpretation checks
- `/decisions` → research decision ledger
- `/feedback` → supervisor feedback interpretation and impact
- `/defense` → research-specific defense simulation
- `/full-audit` → all supported passes

If the request is narrow, do not run an unnecessary full audit.

## Input inventory

Before diagnosing, inventory available materials and assign roles, for example:

- `thesis.docx` → main thesis
- `proposal.pdf` → proposal
- `dataset.xlsx` → dataset
- `questionnaire.docx` → instrument
- `feedback.pdf` → supervisor feedback
- `guidelines.pdf` → authoritative university/project requirements

If only part of the project is available, explicitly state which dependency checks are impossible and audit only what is supported.

## Research model

Construct an internal model with these nodes when evidence exists:

`Research Questions, Objectives, Gap, Theories, Hypotheses, Variables, Constructs, Population, Sample, Sampling, Measurement, Methodology, Dataset, Analysis, Results, Claims, Citations, Discussion, Conclusions, Research Decisions.`

Use relationships such as:

`SUPPORTS, CONTRADICTS, ANSWERS, DEPENDS_ON, DERIVED_FROM, MEASURED_BY, TESTED_BY, CITES, IMPACTS, REQUIRES, INVALIDATES.`

Do not create nodes merely because the template contains them. Mark absent information as unavailable rather than inferred.

## Multi-pass audit workflow

Run only the passes relevant to the request, but for a full audit use this order:

### Pass 1 — Structure
Map sections, research questions, objectives, theory, hypotheses, variables, methods, results, discussion, and conclusions. Record missing or ambiguous components.

### Pass 2 — Research logic
Check RQ → objective → theory → hypothesis → variable → method → result → conclusion alignment. Look for logical gaps and unsupported transitions.

### Pass 3 — Methodology
Read `references/methodology-checks.md`. Test whether the stated design can answer the research question and whether population, sample, measurement, collection, and analysis are compatible. Do not assume a universal method.

### Pass 4 — Evidence and citations
Read `references/evidence-checks.md`. For important claims, distinguish citation presence from actual support. Classify support as `SUPPORTED`, `PARTIAL`, `UNSUPPORTED`, `CONTRADICTED`, or `INSUFFICIENT EVIDENCE`.

### Pass 5 — Data and statistics
Read `references/statistical-checks.md`. Cross-check reported N, variables, coding, scales, exclusions, statistics, and interpretations. Do not recompute or assert a statistical result unless the available data/context supports it.

### Pass 6 — Consistency
Read `references/consistency-checks.md`. Compare terminology, numbers, population, scope, hypotheses, methods, results, tables, figures, and conclusions across documents/sections.

### Pass 7 — Dependency and impact
Read `references/dependency-model.md`. Build dependency chains and identify downstream components that depend on changed or questionable nodes.

### Pass 8 — Conclusion alignment
Trace every major conclusion back to results and research questions. Detect unanswered questions, unused results, unsupported conclusions, and scope inflation.

### Pass 9 — Research risks
Separate confirmed findings from plausible risks requiring more evidence or methodology-specific review.

### Cross-check / deduplication
Before reporting:
- merge duplicate findings;
- prefer the narrowest defensible claim;
- downgrade findings when a plausible explanation remains;
- distinguish a contradiction from a difference caused by a documented subsample/exclusion;
- require stronger evidence for CRITICAL/HIGH labels.

## Change Impact Analysis — signature workflow

When the user changes or proposes changing any research decision:

1. Identify the exact change: `OLD → NEW`.
2. Locate the changed node(s) in the research model.
3. Traverse downstream dependencies.
4. Classify each affected component as `REVIEW`, `LIKELY UPDATE`, or `NO DIRECT IMPACT`.
5. Assign impact severity: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`.
6. Explain why the component is affected.
7. Do not rewrite unrelated content.
8. Identify what should be revalidated before editing.

Example:

`OLS regression → SEM`

Potential impacts may include measurement model, hypotheses, estimation assumptions, analysis section, results tables, discussion, limitations, and conclusions. The exact impact depends on the actual project evidence.

If the user asks “what changed after I removed H1?”, trace H1 → variables → analysis → results → discussion → conclusion and report only supported downstream dependencies.

## Research decision ledger

When decisions are provided or requested, maintain records with:

- Decision ID
- Decision
- Reason
- Evidence
- Alternatives considered
- Affected components
- Date/version if supplied
- Open questions

Do not invent rationale. If rationale is absent, record `Reason: NOT PROVIDED`.

## Research dead-end detector

Flag when a research question appears difficult or impossible to answer with the stated design/evidence. Typical pattern: a causal question with a design that may only support association. Explain the estimand/claim mismatch, missing assumptions/evidence, and possible alternatives without redesigning the study automatically.

## Supervisor feedback translator

Translate vague feedback into plausible interpretations without pretending to know the supervisor's intent.

Example: “Chapter 2 is still weak.”
Possible interpretations: insufficient literature, weak synthesis, weak theory, weak gap, insufficient recent evidence. Ask for clarification if the difference materially changes the action plan.

For a feedback change such as “replace the main theory,” run dependency impact analysis before suggesting edits.

## Defense simulator

Generate research-specific examiner questions from actual detected weaknesses. For each question provide:
- why it may be asked;
- related location;
- available evidence;
- what a strong answer should address.

Prefer detected weaknesses over generic questions.

## Severity

Use `references/severity-rubric.md` and the visual markers:
- 🔴 CRITICAL — threatens fundamental validity/logic
- 🟠 HIGH — likely to trigger serious review concern
- 🟡 MEDIUM — important but not fundamental
- 🔵 LOW — minor improvement
- ⚪ INFO — observation, no required action

Severity is about research risk, not writing quality.

## Health score

Produce a 0–100 diagnostic indicator only when enough evidence exists. Suggested dimensions:

- Research Logic
- Methodology
- Evidence
- Data
- Consistency
- Analysis
- Conclusion Alignment

Use a weighted average only when dimensions are meaningfully assessed; otherwise state that the score is provisional. Never describe the score as a probability of acceptance/passing. Explain that scoring is heuristic and evidence-dependent.

## Required finding format

For every CRITICAL/HIGH finding use:

`ID`
`Type`
`Severity`
`Location`
`Problem`
`Evidence`
`Reasoning`
`Impact`
`Recommended Action`

If a field cannot be established, say `NOT AVAILABLE` or `INSUFFICIENT EVIDENCE` rather than guessing.

## Default report

For a full audit, follow `references/output-schema.md` and the template in `templates/debug-report.md`. Default order:

1. Executive Summary
2. Research Health Score
3. Critical Errors
4. High Priority Issues
5. Medium/Low Issues
6. Evidence Audit
7. Consistency Audit
8. Dependency Analysis
9. Change Impact (if applicable)
10. Research Risks
11. Action Plan
12. Supervisor Questions
13. Defense Risks

Do not dump every low-confidence observation into the opening. Lead with the highest-signal findings.

## Data handling and privacy

Do not unnecessarily repeat sensitive personal information. Use synthetic examples. Do not send documents to external services unless the environment explicitly requires and supports it.

## Language

Respond in the user's language when appropriate. The skill's internal reference material is English; this does not require English output.

## Integrity refusal

If asked to fabricate or manipulate research, refuse the fabrication request and offer legitimate alternatives: report the actual result, run sensitivity/robustness checks where justified, clarify limitations, or revise the research question transparently.

## References

Load only the reference file needed for the current operation. For full audits, use all relevant references:

- `references/audit-framework.md`
- `references/error-taxonomy.md`
- `references/methodology-checks.md`
- `references/evidence-checks.md`
- `references/statistical-checks.md`
- `references/consistency-checks.md`
- `references/dependency-model.md`
- `references/severity-rubric.md`
- `references/output-schema.md`

Use templates in `templates/` for structured outputs and `examples/` for benchmark-style calibration.

## Examples of user requests

- “Debug my thesis.”
- “Find only the critical errors.”
- “Check whether my conclusions are supported by my results.”
- “I changed my methodology. What else needs to change?”
- “Find contradictions across chapters.”
- “Prepare me for my defense based on the weaknesses you found.”
