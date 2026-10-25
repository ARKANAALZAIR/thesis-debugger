# Statistical Checks

## Principle

Separate four layers:

1. Statistical fact
2. Interpretation
3. Theoretical implication
4. Causal/normative claim

A valid statistic does not automatically validate the next layer.

## Basic checks

When values are available, cross-check:

- N
- subgroup N
- coefficients and signs
- p-values / intervals when reported
- test statistic and degrees of freedom when available
- model labels
- table text vs narrative text
- variable direction/coding
- significance wording

## Common traps

### Non-significant result described as significant
Example: `p = .31` followed by “significant effect.”

### Sign reversal
Hypothesis says positive; coefficient is negative. This may be a substantive finding, not an error. Check whether the discussion and conclusion acknowledge it.

### Correlation presented as causation
Flag `CAUSALITY_ERROR` unless the design/identification supports the causal claim.

### Statistical significance treated as practical importance
A significant estimate does not by itself establish substantive importance.

### Multiple samples
Different N values are not automatically inconsistent. Search for exclusions, missing data, subgroup models, or robustness samples before escalating.

## No-data rule

Do not perform or claim statistical calculations unless the necessary values/data and context are actually available.

## Reproduction and result comparison

For a material reported result, follow `references/reproducibility-checks.md`. Compare only after an actual execution of inspected supplied code or an independent calculation from supplied inputs. Record the inputs and procedure used. Compare sample size, exclusions, transformations, model/test, estimates, standard errors, p-values, intervals, effect sizes, and table or figure contents when applicable.

Check rounding at the thesis's reported precision and consider documented random seeds, stochastic methods, floating-point behavior, platform/library variation, and other justified non-determinism before labeling a mismatch. A reproducible statistic does not establish that the method is appropriate or the interpretation supported; assess those separately.

Missing data, code, dependencies, execution tools, or permission is a reproduction limitation, not proof of error. State the exact blocker and use the result-level statuses in the reproducibility reference. Keep those labels separate from the diagnostic module status.
