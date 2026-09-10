# Consistency Checks

## Compare these dimensions

### Numeric
- sample size
- dates
- coefficients
- p-values
- percentages
- table totals

### Semantic
- variable names
- construct definitions
- population labels
- research question wording
- hypothesis direction
- method names

### Logical
- hypothesis vs result
- result vs discussion
- discussion vs conclusion
- RQ vs conclusion

### Scope
- geography
- population
- period
- institution/context
- sample type

## Numeric discrepancy protocol

If Chapter 3 says `N=300` and Chapter 4 says `N=287`:

1. search for exclusions/missingness/subsamples;
2. check table notes;
3. check model-specific N;
4. if explained, do not flag;
5. if plausible but undocumented, flag `TRACEABILITY_ERROR` or `POTENTIAL CONSISTENCY ISSUE`;
6. if impossible/unexplained, escalate to `CONSISTENCY_ERROR`.

## Terminology protocol

Do not treat synonyms as different variables automatically. Compare operational definition, indicators, scale, role, and conceptual meaning.

## Contradiction protocol

A contradiction requires mutually incompatible statements about the same object under the same scope/time/context. A difference is not necessarily a contradiction.
