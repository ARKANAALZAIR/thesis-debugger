# Contributing

Thank you for improving Thesis Debugger.

## Good contributions

Prioritize additions that improve reliability, traceability, and low false-positive debugging:

- Synthetic benchmark cases
- New error types with clear boundaries
- Methodology-specific checks with stated assumptions
- Evidence and claim-support edge cases
- Cross-document consistency cases
- Change-impact dependency cases
- Documentation improvements

## Adding a benchmark

Each case should include:

1. Synthetic input
2. Expected findings
3. Expected severity
4. Evidence location
5. Reasoning
6. What should *not* be flagged

False-positive controls are as important as positive examples.

## Pull requests

Keep changes focused. Avoid adding speculative abstractions or unrelated files. If behavior changes, add or update a benchmark case.

## Integrity rule

Do not add fabricated academic sources, real-person private information, or examples that encourage research fraud. Synthetic examples are preferred.
