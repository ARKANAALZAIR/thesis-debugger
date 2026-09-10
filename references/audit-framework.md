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

### 9. Risks

List plausible concerns that cannot yet be confirmed.

## False-positive controls

Before labeling a discrepancy an error, ask:

- Could this be a different analytical sample?
- Is an exclusion criterion documented elsewhere?
- Is the term an intentional construct distinction?
- Is the difference due to a robustness or sensitivity analysis?
- Is the method valid for the stated design under a named assumption?
- Is the apparent contradiction resolved by scope or time period?

If yes and the thesis explains it, do not report an error. If the explanation is plausible but not documented, report a potential traceability issue rather than a contradiction.
