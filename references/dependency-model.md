# Dependency Model

## Core graph

```text
Research Question
      ↓
Objective
      ↓
Theory / Gap
      ↓
Hypothesis / Proposition
      ↓
Variable / Construct
      ↓
Measurement
      ↓
Design / Sample / Data
      ↓
Analysis
      ↓
Result
      ↓
Discussion
      ↓
Conclusion
```

Additional links:

- Claim → Citation/Evidence
- Decision → Affected components
- Supervisor feedback → Target component → Downstream dependencies
- Guideline → Requirement → Affected section

## Impact traversal

For a changed node:

1. Find direct dependents.
2. Find second-order dependents.
3. Stop when the dependency is no longer material or evidence is absent.
4. Mark each node `REVIEW`, `LIKELY UPDATE`, or `NO DIRECT IMPACT`.
5. Explain the edge that creates the dependency.

## Impact levels

- CRITICAL — change may invalidate or materially alter downstream analysis/interpretation.
- HIGH — likely requires substantial revalidation or rewriting.
- MEDIUM — targeted review likely needed.
- LOW — wording/metadata or local adjustment likely.

## Example

Change: `H1 removed`

Potential path:

`H1 → X/Y relationship → model specification → results table → discussion → conclusion`

Do not claim that every downstream section must change. Verify whether each component actually references H1 or depends on its result.

## Change-impact output

```text
CHANGE
OLD → NEW

DIRECTLY AFFECTED
...

DOWNSTREAM IMPACT
...

REVIEW ORDER
1. ...
2. ...

NOT DIRECTLY AFFECTED
...

OPEN QUESTIONS
...
```
