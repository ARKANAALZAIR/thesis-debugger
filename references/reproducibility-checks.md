# Reproducibility & Result Trace Audit

## Purpose and boundary

Audit whether material reported results can be traced to, and where the supplied artifacts and execution environment permit, reproduced from the research inputs. This is a provenance and verification workflow, not a thesis rewrite and not a presumption that every project must be reproducible from a thesis document alone.

Inspect the materials actually supplied. Do not claim that code ran, a statistic was independently recalculated, or an output was verified unless that action occurred. A blocked or incomplete reproduction is not evidence that a result is false, that the method is invalid, or that misconduct occurred.

## Workflow

### Local fixture and capture evaluation

`scripts/reproducibility_contract_test.py` executes only the bundled `tests/fixtures/result-trace/analysis.py` whose hash is pinned in `scripts/result_trace_eval.py`. The runner uses a temporary copy, isolated Python mode, a short timeout, and process resource limits. It calculates the comparison from `observations.csv`; user-supplied research scripts are never passed to this runner.

Use `python scripts/result_trace_eval.py --capture-report REPORT.md` to check a saved full-report response against the independent fixture result. This local check does not authenticate where the capture came from or prove general target-runtime behavior. Without a real runtime capture, the target-runtime gate remains blocked.

### 1. Select material results

Prioritize results that materially support the main research question, hypothesis, contribution, or conclusion. Include a table, figure, or statistical statement only when its reported result is identifiable and material. Do not manufacture result IDs or add empty matrix rows.

### 2. Trace the available chain

For each selected result, trace as far as the supplied material allows:

`source dataset/input → cleaning/transformation/exclusions → analysis script/notebook/formula/documented method → intermediate/output artifact → thesis table/figure/statistical statement → discussion/claim → conclusion`

For each link, record its actual artifact and location, or identify it as missing, ambiguous, or inconsistent. Distinguish an artifact that was not supplied from one that was inspected and found not to contain the expected link. Check whether the thesis result points to the same sample, variable definitions, transformations, exclusions, model, and output as the supplied analysis.

### 3. Decide whether execution is safe and feasible

Reproduction is optional and proportional. Attempt it only when the relevant inputs, code, required dependencies, execution tools, and permissions are available.

Before running supplied code:

- inspect the code and relevant configuration for destructive writes, network access, credential access, unrelated filesystem access, or other unsafe behavior;
- understand the command and its working directory, and do not run code blindly;
- do not modify raw research data; use read-only inputs and a separate output location when execution is justified;
- do not install dependencies or make environment changes without authorization;
- stop and report the specific blocker if code is unsafe, permission is absent, execution is unavailable, or a required dependency cannot be obtained.

Record the exact input artifacts, command/procedure, environment or dependency versions that were actually known, and whether execution completed. Never substitute a newly written implementation for missing author-supplied analysis while describing it as reproduction of the supplied code. An independent calculation from supplied data may be reported as such, distinct from executing the author's script.

### 4. Compare reported and reproduced results

Compare the dimensions relevant to the result, not only its headline value:

- sample size, groups, exclusions, missing-data handling, and analysis population;
- transformations, variable coding, units, formula/model/test, and assumptions;
- coefficients or estimates, standard errors, test statistics, degrees of freedom, p-values, intervals, and effect sizes;
- table/figure values, totals, labels, and the corresponding thesis narrative;
- rounding and display precision.

Use the thesis's stated precision and a justified, predeclared numerical tolerance where needed. A difference explained by ordinary rounding is not a mismatch. Consider documented random seeds, stochastic algorithms, platform/library differences, floating-point behavior, and other legitimate non-determinism. Compare within an explicitly justified range or tolerance where possible. If variation cannot be bounded or the comparison basis is unclear, state that limitation rather than calling it a mismatch.

## Result-level status contract

Each material result included in the matrix receives exactly one of these labels. These labels describe a result-level reproduction assessment and are separate from the canonical module status taxonomy (`FOUND`, `Error Not Found`, `NOT ASSESSABLE`, `COMPLETED`, or `NOT APPLICABLE`).

| Result status | Definition |
|---|---|
| `REPRODUCED` | The relevant supplied procedure was executed or the result was independently recalculated from supplied inputs, and the compared result agrees within justified precision/tolerance, including any documented non-determinism. State which of those actions occurred. |
| `MISMATCH` | A feasible reproduction or independent recalculation actually completed, and a material difference remains after checking sample, transformations, exclusions, model, rounding, and legitimate environment variation. |
| `NOT REPRODUCIBLE WITH SUPPLIED MATERIALS` | A meaningful reproduction attempt is blocked by missing or incomplete required artifacts/inputs, an unavailable dependency/tool, absent permission, or a justified safety restriction. Name the exact blocker and any links that remain traceable. This does not imply error or misconduct. |
| `NOT ASSESSABLE` | The reported result or its scope/meaning cannot be identified well enough from the supplied material to define a meaningful trace or comparison. Explain what is ambiguous or absent. Do not use this label merely because a reproduction attempt is blocked; use `NOT REPRODUCIBLE WITH SUPPLIED MATERIALS` in that case. |

Do not label a result `REPRODUCED` merely because its narrative is internally consistent or because code appears plausible. Do not label it `MISMATCH` based only on a missing artifact, an unexplained difference in display rounding, or an unexamined alternative analysis sample.

## Findings, ownership, and interpretation

A missing provenance link or blocked reproduction is a coverage limitation, not automatically a canonical error finding. Report it in the matrix and verification limits. Do not turn missing evidence into `Error Not Found`, a false claim of verification, or an accusation.

When an actual, supported material mismatch is found:

1. Create or link one canonical finding with the existing finding schema: unique ID, one Primary Module, related modules as applicable, evidence and locations, severity, impact, and corrective/verification action.
2. Prefer root-cause ownership under `references/audit-integrity.md`: use M06 for a data/sample/numeric root cause, M07 for a statistical calculation or interpretation root cause, and M10 for an unresolved cross-location contradiction when neither is more primary. M09 and M12 may be related when claim support or downstream result/conclusion alignment is affected.
3. Reuse an existing finding ID when the evidence, root cause, and corrective action are materially the same. Do not create a second finding for the same mismatch simply because another module or the trace matrix also reports it.
4. Separate a reproduction failure from a distinct methodological defect or unsupported interpretation. A reproducible statistic can still have an unsupported interpretation; assess that under the existing statistical, evidence, and logic workflows.
5. Calibrate severity to evidence and downstream impact. Do not escalate a limitation or unresolved alternative explanation to a confirmed error.

## Report matrix

Include a concise **Result Traceability & Reproduction Audit** subsection in a full report. Use one row per selected material result, with only evidence-supported entries:

| Result/claim ID | Thesis location | Source data/artifact | Script/formula/method | Reported result | Reproduced result | Discrepancy | Result status | Limitations | Downstream impact |
|---|---|---|---|---|---|---|---|---|---|

Identify artifacts and locations precisely. For absent or unclear links, use concise labels such as `NOT SUPPLIED`, `NOT IDENTIFIED`, or `NOT ASSESSABLE` and explain the blocker in limitations. For a blocked attempt, reproduced result is `NOT RUN` plus the exact reason; do not imply execution. If nothing material can be selected from the supplied material, state that explicitly instead of rendering an empty or invented row.

The report's verification/coverage section must summarize the evidence boundary and distinguish results actually reproduced, mismatches actually observed, blocked attempts, and results not assessable. State that the feature evaluates only supplied materials and does not certify the complete research project.
