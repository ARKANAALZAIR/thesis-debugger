---
name: thesis-debugger
description: Audit theses, dissertations, research papers, proposals, datasets, research notes, and supervisor feedback as one connected research system. Use this skill for research debugging, literature review auditing, citation/reference integrity, paraphrase or plagiarism-risk review, academic-authenticity risk review, methodology/evidence checks, contradiction tracing, research-change impact analysis, and defense preparation. Prioritize evidence, traceability, low false positives, and change impact. Never claim plagiarism or AI authorship from style alone.
version: 2.2.6
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
10. **Integrity limits.** Treat plagiarism/paraphrase and AI-authorship review as risk assessment unless matching source text or stronger provenance evidence is actually supplied. Never state that a text was definitely AI-written or definitely plagiarized from style alone.
11. **Simple-prompt full-audit behavior.** When a thesis/research document is supplied and the user asks broadly to “audit”, “debug”, “review”, “check”, or equivalent without naming a narrower module, run the **FULL THESIS DEBUG** workflow automatically. Do not require a long prompt, a slash command, or a module checklist.
12. **All modules must be shown.** In FULL THESIS DEBUG, every supported module executes and every module appears in the final report, even when no issue is found.
13. **Role-specific module-state semantics.** Diagnostic modules use exactly `FOUND`, `Error Not Found`, or `NOT ASSESSABLE`. Synthesis/action modules use exactly `COMPLETED`, `NOT ASSESSABLE`, or `NOT APPLICABLE`. Do not mix these taxonomies.
14. **Coverage transparency.** Coverage is reported separately as `FULL`, `PARTIAL`, or `LIMITED`. Do not use `Error Not Found` as a substitute for missing core evidence, and never imply the research is globally error-free.
15. **Reference loading is mandatory.** Before executing any module or formula, read every bundled reference explicitly cited by the selected workflow, including the canonical output and audit-integrity contracts. If a required reference cannot be loaded, do not silently approximate or invent its rule.
16. **No prompt burden.** Never tell the user to restate all desired audit modules when the request is a broad thesis audit; the skill itself expands the request into the full workflow.

## Activation and request routing

### Default behavior: broad thesis-audit requests automatically become FULL THESIS DEBUG

When the user supplies a thesis, proposal, dissertation, research paper, or equivalent research package and uses a broad request such as:

- “audit thesis berikut”
- “audit skripsi ini”
- “debug thesis ini”
- “cek thesis saya”
- “review skripsi berikut”
- “audit this thesis”

run the **FULL THESIS DEBUG** workflow automatically. The user must not need to type `/full-audit` or repeat the feature list.

The activation rule is:

```text
RESEARCH DOCUMENT SUPPLIED
        +
BROAD AUDIT / DEBUG / REVIEW / CHECK REQUEST
        ↓
AUTOMATIC FULL THESIS DEBUG
        ↓
RUN ALL SUPPORTED MODULES
        ↓
DISPLAY ALL MODULES
```

Do not ask a clarification question solely to determine which audit modules to run. If the document is readable, begin the audit.

### Supported explicit aliases

Users may still request narrower workflows when they explicitly name one, for example:

- `/health` → health score and highest-risk findings
- `/impact` → change impact analysis
- `/contradictions` → cross-document consistency audit
- `/evidence` → claim/evidence audit
- `/literature` → literature review audit
- `/citations` → reference and citation integrity audit
- `/integrity` → plagiarism/paraphrase risk + academic authenticity review
- `/authenticity` → academic-authenticity risk review only
- `/methodology` → methodology/RQ/design audit
- `/data` → dataset/report consistency and statistical interpretation checks
- `/decisions` → research decision ledger
- `/feedback` → supervisor feedback interpretation and impact
- `/defense` → research-specific defense simulation
- `/full-audit` → all supported passes

When a user explicitly requests a narrow module, obey the narrower request. When the request is broad, default to FULL THESIS DEBUG.

## Input inventory

Before diagnosing, inventory available materials and assign roles, for example:

- `thesis.docx` → main thesis
- `proposal.pdf` → proposal
- `dataset.xlsx` → dataset
- `questionnaire.docx` → instrument
- `feedback.pdf` → supervisor feedback
- `guidelines.pdf` → authoritative university/project requirements
- `source-paper.pdf` / `source-text.txt` → comparison source for citation or paraphrase review
- `references.bib` / `references.docx` → bibliography/reference list
- `draft-v1.docx` / `draft-v2.docx` → version pair for citation drift, self-overlap, or authenticity/provenance review

If only part of the project is available, explicitly state which dependency checks are impossible and audit only what is supported.

## Research model

Construct an internal model with these nodes when evidence exists:

`Research Questions, Objectives, Gap, Literature Sources, Literature Themes, Theories, Hypotheses, Variables, Constructs, Population, Sample, Sampling, Measurement, Methodology, Dataset, Analysis, Results, Claims, Citations, References, Paraphrases, Quotations, Discussion, Conclusions, Research Decisions.`

Use relationships such as:

`SUPPORTS, CONTRADICTS, ANSWERS, DEPENDS_ON, DERIVED_FROM, MEASURED_BY, TESTED_BY, CITES, IMPACTS, REQUIRES, INVALIDATES.`

Do not create nodes merely because the template contains them. Mark absent information as unavailable rather than inferred.

## FULL THESIS DEBUG — always-on workflow

For every broad thesis audit, run the following modules in one complete pass. Do not stop after finding the first error. Continue until every module has been evaluated.

### Module 1 — Research structure and RQ/objective alignment
Map research questions, objectives, scope, contribution, chapter structure, and core research entities. Check research-question/objective mismatch.

### Module 2 — Theory / hypothesis / model alignment
Check theory → construct → hypothesis/model → test alignment. Flag unsupported theory-to-hypothesis jumps, model mismatches, and unused constructs.

**Evidence boundary rule:** A material theory/literature/model section is core evidence for M02. If that core evidence is not present in the supplied material, M02 **MUST** be `NOT ASSESSABLE`; do not promote a suspected theory gap to a qualifying finding merely because H1 appears under-justified. You may record a verification observation (for example, “theory basis not visible in supplied material”) with `Verification needed`, but that observation cannot make M02 `FOUND`.

### Module 3 — Methodology / research-question fit
Test whether the stated research design, population, sampling, data collection, and analysis can answer each research question. Do not impose universal methods.

### Module 4 — Variable and definition drift
Track each key variable/construct across chapters, instruments, tables, figures, analysis, and conclusions. Detect changes in meaning, label, unit, coding, or scope.

### Module 5 — Measurement and operationalization
Check construct definitions, indicators, instruments, scales, units, operational definitions, reliability/validity evidence where relevant, and alignment between conceptual and measured variables.

### Module 6 — Sample, dataset, and numeric consistency
Cross-check N, sample counts, exclusions, treatment/group counts, totals, units, dates, reported values, tables, figures, appendices, and any supplied dataset.

### Module 7 — Statistical interpretation
Read `references/statistical-checks.md`. Audit model/test fit, assumptions where material, interpretation of p-values/effect sizes/intervals, multiple testing claims, table arithmetic when supported, and whether conclusions overstate the analysis.

### Module 8 — Logic and causality
Detect invalid inference chains, circular reasoning, causal overclaims, temporal leaps, confounding claims, and unsupported transitions.

### Module 9 — Evidence and claim support
Read `references/evidence-checks.md`. For material claims, distinguish citation presence from substantive support. Classify support as `SUPPORTED`, `PARTIAL`, `UNSUPPORTED`, `CONTRADICTED`, or `INSUFFICIENT EVIDENCE`.

### Module 10 — Internal consistency and contradictions
Read `references/consistency-checks.md`. Compare terminology, numbers, variables, hypotheses, samples, methods, results, tables, figures, scope, and conclusions across chapters/documents.

### Module 11 — Scope and completeness
Check whether the thesis claims more than its design/evidence can support, whether required reasoning links are missing, and whether key components are present for the stated research goal. Missing information is not automatically an error.

### Module 12 — Results / discussion / conclusion alignment
Trace each major result into discussion and conclusion, and each conclusion back to results and research questions. Detect unanswered RQs, unused results, unsupported conclusions, and scope inflation.

### Module 13 — Research dead ends and fragile dependencies
Read `references/dependency-model.md`. Identify weak or broken nodes that can invalidate downstream analysis, and research questions that appear difficult/impossible to answer with the stated evidence/design.

### Module 14 — Change Impact Analysis baseline
Always run a baseline dependency scan, even when the user did not specify a change. Identify high-dependency nodes and components that would likely require review if a material research decision changes. If an explicit `OLD → NEW` change exists, run the full downstream impact traversal.

### Module 15 — Supervisor feedback translator
Search all supplied materials for supervisor/advisor comments or instructions. Translate vague feedback into plausible interpretations and trace likely dependencies. If no feedback is supplied, still show the module and state that no feedback was available for diagnosis.

### Module 16 — Literature Review Auditor
Read `references/literature-review-checks.md`. Audit synthesis, coverage, gap logic, contribution, competing findings, source relevance/quality, chronology when material, search/selection transparency when supplied, and duplicate/overlapping arguments.

### Module 17 — Reference & Citation Integrity
Read `references/citation-integrity-checks.md`. Audit citation↔reference linkage, uncited references, missing reference entries, duplicate references, metadata inconsistencies, quotation attribution, citation drift, and claim-source traceability. Never invent bibliographic metadata.

### Module 18 — Plagiarism / Paraphrase Risk
Read `references/paraphrase-risk-checks.md`. Always check for internal self-overlap and compare external source text when supplied. Use `RISK` / `REVIEW NEEDED` unless evidence supports a stronger conclusion.

### Module 19 — Academic Authenticity / Provenance Risk
Read `references/authenticity-checks.md`. Audit observable provenance and writing-pattern anomalies, citation anomalies, terminology shifts, revision/provenance gaps, and supplied authorship statements. Never infer AI authorship from style alone.

### Module 20 — Research decisions ledger
Extract explicit research decisions, assumptions, and methodological choices. Record decision, reason/evidence when supplied, affected components, and open questions. Do not invent rationale.

### Module 21 — Defense risk simulation
Generate examiner-style questions from actual detected weaknesses, fragile dependencies, unsupported claims, or unresolved methodological choices. Tie every defense risk to evidence from the thesis.

### Module 22 — Prioritized action plan
Order actions by dependency and severity. Separate confirmed errors from verification tasks, potential concerns, and suggestions.

## Production hardening — v2.2.6 canonical execution contract

The following rules are mandatory for every **FULL THESIS DEBUG** run. They harden execution completeness, module-state semantics, deduplication, severity calibration, health-score transparency, and final reconciliation.

### A. Full-audit execution is non-short-circuiting

- Once a broad audit request is detected, execute **all 22 modules** in the canonical registry below before composing the final report.
- Do not stop early because a CRITICAL/HIGH finding has already been found.
- Do not ask the user which modules they want.
- Do not replace a module with “covered above.” Each module gets its own status block.
- A module may reuse evidence discovered by another module, but it still executes its own diagnostic question.

### B. Canonical 22-module registry

Use these IDs, names, and classes exactly:

| ID | Class | Canonical module name |
|---|---|---|
| M01 | DIAG | Research structure & RQ/objective alignment |
| M02 | DIAG | Theory / hypothesis / model alignment |
| M03 | DIAG | Methodology / research-question fit |
| M04 | DIAG | Variable and definition drift |
| M05 | DIAG | Measurement & operationalization |
| M06 | DIAG | Sample / dataset / numeric consistency |
| M07 | DIAG | Statistical interpretation |
| M08 | DIAG | Logic / causality |
| M09 | DIAG | Evidence / claim support |
| M10 | DIAG | Internal consistency / contradictions |
| M11 | DIAG | Scope / completeness |
| M12 | DIAG | Results / discussion / conclusion alignment |
| M13 | DIAG | Research dead ends / fragile dependencies |
| M14 | SYN | Change Impact Analysis baseline |
| M15 | SYN | Supervisor feedback translator |
| M16 | DIAG | Literature Review Auditor |
| M17 | DIAG | Reference & Citation Integrity |
| M18 | DIAG | Plagiarism / Paraphrase Risk |
| M19 | DIAG | Academic Authenticity / Provenance Risk |
| M20 | SYN | Research Decisions Ledger |
| M21 | SYN | Defense Risk Simulation |
| M22 | SYN | Prioritized Action Plan |

### C. Canonical module registry classes

| Class | Modules | Status taxonomy |
|---|---|---|
| DIAG | M01–M13, M16–M19 | `FOUND` / `Error Not Found` / `NOT ASSESSABLE` |
| SYN | M14–M15, M20–M22 | `COMPLETED` / `NOT ASSESSABLE` / `NOT APPLICABLE` |

Synthesis/action modules may reference diagnostic findings but must not relabel completion as `FOUND` or `Error Not Found`.

### D. Canonical module result block

Every module must emit exactly one block, in M01→M22 order:

```text
MODULE ID: M01
MODULE: Research structure & RQ/objective alignment
Class: DIAG
Execution: COMPLETE
Status: FOUND | Error Not Found | NOT ASSESSABLE
Coverage: FULL | PARTIAL | LIMITED
Key findings: [integer count of qualifying PRIMARY findings owned by this module]
Observations: [integer count of non-qualifying INFO/SUGGESTION PRIMARY observations]
Evidence: [locations/evidence or NONE FOUND]
Verification needed: [text or NONE]
```

For synthesis/action modules, replace `Status:` with the role-appropriate taxonomy:

```text
Class: SYN
Status: COMPLETED | NOT ASSESSABLE | NOT APPLICABLE
```

### E. Exact status decision rule

For DIAG modules:
```text
Can the module materially answer its core diagnostic question from the supplied evidence?
├─ NO → Status: NOT ASSESSABLE
│       Coverage: LIMITED
│       Verification needed: identify the missing core input
└─ YES
   ├─ Concrete error/issue found → Status: FOUND
   └─ No concrete error/issue found → Status: Error Not Found
```

For SYN modules:
```text
Can the synthesis/control task be completed from available evidence?
├─ NO, missing core input → Status: NOT ASSESSABLE
├─ Task does not materially apply → Status: NOT APPLICABLE
└─ Otherwise → Status: COMPLETED
```

`PARTIAL` coverage may be used with `FOUND`, `Error Not Found`, or `COMPLETED` when the core task runs but some sub-checks are blocked.

Important:
- Suggestions and INFO observations alone do not force `FOUND`.
- Missing evidence is not a finding.
- `NOT ASSESSABLE` does not mean “the module is clean”; it means the evidence boundary prevents a determination.
- `Error Not Found` does not mean the research is globally error-free.

### F. Canonical finding ownership and reconciliation

Every finding in the detailed findings section must have:

```text
Finding ID: TD-###
Primary Module: M##
Related Modules: [optional]
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

Rules:
1. Finding/observation IDs are globally unique within the report.
2. Every finding/observation has exactly one Primary Module.
3. Related modules must reuse the same ID and never create another global count.
4. A diagnostic **finding** is a qualifying Type: `CONFIRMED ERROR`, `LIKELY ISSUE`, or `POTENTIAL ISSUE` with Severity `CRITICAL|HIGH|MEDIUM|LOW`.
5. `SUGGESTION` and `INFO` are **observations**, not qualifying diagnostic findings. They may be attached to a Primary Module for traceability.
6. `Key findings` counts qualifying diagnostic Primary Findings only. `Observations` counts Primary INFO/SUGGESTION observations.
7. Global severity totals are computed from all canonical finding/observation objects.
8. `sum(M01…M22 Key findings) = number of qualifying diagnostic findings`.
9. `sum(M01…M22 Observations) = number of INFO/SUGGESTION observations`.
10. `Critical + High + Medium + Low + Info = Total unique finding/observation IDs`.
11. Deduplicate only when root cause, evidence/location, and corrective action materially match. Different roots/actions remain separate.
12. When overlap occurs, prefer the root-cause module as Primary Module. See `references/audit-integrity.md`.
13. Before finalizing, verify there are no orphan IDs, phantom module references, or duplicate root causes.


### F.1 Status–finding consistency gate

Reconcile each DIAG module against its **Primary Findings**, not against `Related Modules` references. The gate is evidence-gated and count-derived; the model must not hand-wave a status or count.

```text
DIAG + FOUND
→ core diagnostic evidence is materially assessable
→ owns ≥1 qualifying Primary Finding
→ each qualifying Primary Finding is CONFIRMED ERROR / LIKELY ISSUE / POTENTIAL ISSUE
→ each qualifying Primary Finding has CRITICAL/HIGH/MEDIUM/LOW severity

DIAG + Error Not Found
→ core diagnostic evidence is materially assessable
→ owns 0 qualifying Primary Findings
→ may carry non-qualifying INFO/SUGGESTION observations for traceability

DIAG + NOT ASSESSABLE
→ names the missing or insufficient core evidence
→ any blocked POTENTIAL/LIKELY issue is treated as a verification observation, not a qualifying finding
```

**Mandatory evidence-boundary rule:** Absence from the supplied excerpt/package is not evidence that the underlying thesis lacks the component. A diagnostic module may claim a concrete absence only when the supplied artifact is sufficiently complete for that module's core question. Otherwise use `NOT ASSESSABLE`.

**M02 hard gate:** If no theory, literature, conceptual model, or other substantive theoretical basis is present in the supplied material, M02 cannot be `FOUND`; it must be `NOT ASSESSABLE`.

A module mentioned only as a Related Module does not become `FOUND`.

### F.2 Count-derived reconciliation algorithm

Do not manually estimate module counts. After the detailed finding/observation list is finalized, construct an internal ledger from the actual IDs and `Primary Module` fields:

```text
qualifying_primary[module] = count(
  object.PrimaryModule == module
  AND object.Type in {CONFIRMED ERROR, LIKELY ISSUE, POTENTIAL ISSUE}
  AND object.Severity in {CRITICAL, HIGH, MEDIUM, LOW}
)

observation_primary[module] = count(
  object.PrimaryModule == module
  AND object.Type in {INFO, SUGGESTION}
)
```

Then require, for every module:

```text
reported Key findings == qualifying_primary[module]
reported Observations == observation_primary[module]
````

If any count differs, the final integrity gate is `FAIL` and the report must be repaired before return. Never declare reconciliation PASS from manually typed totals.

For DIAG status:

```text
FOUND              ↔ qualifying_primary[module] >= 1 AND core evidence assessable
Error Not Found    ↔ qualifying_primary[module] == 0 AND core evidence assessable
NOT ASSESSABLE     ↔ core evidence not assessable
```

The same ledger must be used to compute global qualifying-finding and observation totals.

### G. Severity calibration

Severity must reflect both impact and evidence strength.

- `CRITICAL` normally requires `CONFIRMED ERROR` plus fundamental validity/dependency impact.
- `HIGH` requires `CONFIRMED ERROR` or a strongly supported `LIKELY ISSUE` with material downstream impact.
- Do not promote low-confidence findings because their hypothetical impact is large.
- Run an alternative-explanation check before CRITICAL/HIGH classification.
- Preferences, generic advice, and style concerns are not automatically errors.

### H. Health-score integrity

Auditability rule: every score is traceable to evidence; no score is inferred from finding counts.

Use the fixed diagnostic weights and formula in `references/audit-integrity.md` when an overall score is reported. Every scored dimension must include a basis. `N/A` is required for dimensions that are not materially assessable; missing evidence must never be silently converted to zero. If fewer than four core dimensions are assessable, prefer `Overall: N/A`.

### I. Change Impact baseline

M14 runs even when no explicit change is supplied. Report the highest-sensitivity nodes and downstream review implications, but do not invent an `OLD → NEW` change. Use `Baseline only — no explicit change supplied.` when appropriate.

### J. Final reconciliation gate

Final Audit Integrity Check must be explicitly rendered as `Audit Integrity Check` in the report.

Before final output, repair any inconsistency until all of these are true:

```text
[ ] FULL THESIS DEBUG triggered from broad request
[ ] M01–M22 executed and displayed exactly once
[ ] Every module has the correct Class and role-specific Status taxonomy
[ ] Every module has Execution: COMPLETE
[ ] Every module has Status + Coverage + Key findings + Observations + Evidence + Verification
[ ] NOT ASSESSABLE is used for missing core evidence
[ ] Error Not Found is not used as a substitute for missing core evidence
[ ] Synthesis/action modules use COMPLETED / NOT ASSESSABLE / NOT APPLICABLE
[ ] Every finding has one unique ID and one Primary Module
[ ] Related-module references are valid
[ ] Every DIAG `FOUND` module owns at least one qualifying Primary Finding
[ ] Every DIAG `FOUND` module has materially assessable core evidence
[ ] M02 is `NOT ASSESSABLE` whenever theory/literature/model core evidence is absent from the supplied material
[ ] No DIAG `FOUND` module is supported only by `SUGGESTION` or `INFO`
[ ] Any DIAG `POTENTIAL ISSUE` blocked by missing core evidence leaves the module `NOT ASSESSABLE`
[ ] Any DIAG `Error Not Found` module owns zero qualifying Primary Findings; INFO/SUGGESTION observations may remain
[ ] No duplicate underlying root cause is counted twice
[ ] Severity totals reconcile to unique finding/observation IDs
[ ] Module primary-finding totals are derived from actual Primary Module + Type + Severity fields
[ ] Every module `Key findings` count exactly matches the derived qualifying-primary ledger
[ ] Every module `Observations` count exactly matches the derived observation-primary ledger
[ ] CRITICAL/HIGH classifications pass confidence/evidence calibration
[ ] Every health-score dimension has a basis or N/A
[ ] Canonical health-score reference was loaded before calculating any score
[ ] Overall score uses the fixed weighted renormalized formula or is N/A
[ ] Change Impact baseline is present
[ ] Final debug state is present
```

If any gate fails, repair the report before returning it.

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
- Literature Review
- Evidence & Citation Integrity
- Data
- Consistency
- Analysis
- Conclusion Alignment

Use the fixed dimension weights and renormalized formula in `references/audit-integrity.md`. Never score missing evidence as zero. Never describe the score as a probability of acceptance/passing. Every scored dimension needs a short basis.

## Academic integrity finding rules

For plagiarism/paraphrase-risk findings, include:
- source/target locations when both are available;
- overlap type (EXACT, NEAR-EXACT, CLOSE PARAPHRASE, PATCHWRITING, UNATTRIBUTED QUOTATION, SELF-OVERLAP);
- matched excerpt(s) only as needed;
- confidence and missing verification;
- a clear statement that risk is not proof of misconduct unless evidence is sufficient.

For AI/authenticity findings, include:
- observable signal;
- provenance/evidence available;
- alternative explanations (editing, translation, co-authorship, template use);
- confidence;
- what additional evidence would verify the concern.

Do not recommend punitive action from stylistic signals alone.

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

For a broad thesis audit, always follow `references/output-schema.md` and `templates/debug-report.md`. The report must include the executive summary, health score, finding summary, the **full 22-module status matrix**, all detailed findings, coverage limits, change-impact baseline, and final debug state.

Before returning the report, the v2.2.6 reconciliation gate in `references/audit-integrity.md` must pass: all M01–M22 appear exactly once, module/severity totals reconcile to unique finding IDs, missing core evidence is classified as `NOT ASSESSABLE`, and health-score bases are auditable.

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
- `references/literature-review-checks.md`
- `references/citation-integrity-checks.md`
- `references/paraphrase-risk-checks.md`
- `references/authenticity-checks.md`

Use templates in `templates/` for structured outputs and `examples/` for benchmark-style calibration. Load the new integrity references only when the request involves literature, citations, paraphrase/plagiarism risk, or authenticity.

## Examples of user requests

- “Debug my thesis.”
- “Audit my literature review for gaps and weak synthesis.”
- “Check that every citation has a matching reference and that the cited source supports the claim.”
- “Look for plagiarism/paraphrase risk between my draft and these source excerpts.”
- “Check this chapter for academic-authenticity risks without claiming whether AI wrote it.”
- “Find only the critical errors.”
- “Check whether my conclusions are supported by my results.”
- “I changed my methodology. What else needs to change?”
- “Find contradictions across chapters.”
- “Prepare me for my defense based on the weaknesses you found.”
