# Audit Framework

## Purpose

Audit a research project as a connected system. The audit should maximize reliable findings per comment, not raw finding count.

## Workflow

1. Inventory documents and authority levels.
2. Extract explicit research entities and claims.
3. Build the research model.
4. Build dependency links only when supported.
5. Run relevant diagnostic passes.
6. Cross-check apparent contradictions.
7. Classify confidence and severity.
8. Deduplicate.
9. Generate an action plan in dependency order.
10. Offer deeper analysis on request.

## Authority hierarchy

When available:

1. University/project guideline
2. Explicit supervisor instruction
3. Project-specific decision
4. Stated methodology protocol
5. General academic convention

A generic convention should not silently override a project-specific requirement.

## Finding confidence

Use these internal confidence states:

- CONFIRMED — direct evidence establishes the inconsistency/error.
- LIKELY — evidence strongly indicates a problem, but context may remain.
- POTENTIAL — plausible concern requiring verification.
- SUGGESTION — improvement that is not an error.

Only CONFIRMED or well-supported LIKELY findings should normally be CRITICAL/HIGH.

## Full audit sequence

### 1. Structure

Map research questions, objectives, theory, hypotheses, variables, methods, results, discussion, and conclusions.

### 2. Logic

Check whether each major component has a defensible predecessor and successor.

### 3. Methodology

Check fit between question, design, sampling, measurement, collection, and analysis.

### 4. Evidence

Check whether important claims are supported by the cited evidence and whether claim strength exceeds evidence strength.

### 5. Data/statistics

Check reported N, variable definitions, coding, exclusions, statistics, and interpretation.

### 6. Consistency

Check across chapters/documents rather than only within sections.

### 7. Dependencies

Trace important changes and weak nodes downstream.

### 8. Conclusion alignment

Trace conclusions back to results and questions.

### 9. Literature review

Audit review scope, search/selection transparency when supplied, synthesis, competing evidence, gap logic, source quality, and literature-to-RQ/hypothesis/contribution alignment.

### 10. Citation integrity

Audit reference/citation linkage and bibliographic consistency separately from substantive claim support.

### 11. Paraphrase/plagiarism risk

Use source-text comparison when available. Report risk, not misconduct verdicts, unless evidence genuinely supports a stronger conclusion.

### 12. Academic authenticity

Assess provenance and observable writing-pattern anomalies as review signals. Never use stylistic fluency as proof of AI authorship.

### 13. Risks

List plausible concerns that cannot yet be confirmed.

## False-positive controls

Before labeling a discrepancy an error, ask:

- Could this be a different analytical sample?
- Is an exclusion criterion documented elsewhere?
- Is the term an intentional construct distinction?
- Is the difference due to a robustness or sensitivity analysis?
- Is the method valid for the stated design under a named assumption?
- Is the apparent contradiction resolved by scope or time period?

If yes and the thesis explains it, do not report an error. If the explanation is plausible but not documented, report a potential traceability issue rather than a contradiction. If the core diagnostic input is absent, use `NOT ASSESSABLE` rather than `Error Not Found`.


## Broad-audit automation contract

A broad request like “audit thesis berikut” is a FULL THESIS DEBUG request. The system must expand the request internally to all supported modules without requiring the user to specify them.

The audit is incomplete until every module has an explicit status. If no concrete error is found in a module, report `Status: Error Not Found`; if inputs are missing, also report the coverage limitation and verification requirement.

Before finalizing, validate: (1) all 22 modules appear exactly once, (2) no module is silently skipped, (3) finding counts reconcile with the visible findings, and (4) `Error Not Found` is not used as a substitute for missing evidence.


## Final hardening rule

The final report is a data-reconciliation problem as well as a reasoning problem. The model must count unique finding IDs, assign one owner per finding, validate module-state semantics, calibrate severity to evidence, and make every health-score number traceable to a documented basis.
