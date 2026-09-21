# Academic Authenticity / AI-Generated Writing Risk

## Purpose
Assess whether there are observable **authenticity/provenance risks** that warrant human review. This is not a reliable standalone AI detector and must not be presented as proof of AI authorship.

## Observable signals

### Provenance signals
- unexplained authorship or editing-history gaps;
- sudden changes in terminology or technical depth between sections;
- references that do not match the cited text;
- claims or citations that appear after-the-fact or cannot be traced;
- version-to-version changes with no stated reason when such versions are supplied.

### Writing-pattern signals
- unusually repetitive generic structure;
- templated transitions that recur without research-specific content;
- generic claims standing in for evidence;
- sudden voice/register shifts inconsistent with nearby author-written material.

These are weak signals individually. They may also arise from editing, translation, co-authorship, supervisor revisions, institutional templates, or legitimate use of writing tools.

## Do not use as proof
Never infer AI authorship solely from:
- fluent English;
- grammar quality;
- formal vocabulary;
- coherent structure;
- “AI-like” tone;
- detector scores from another tool without validation context.

## Verification ladder
1. Compare against earlier drafts or author-provided writing samples when available.
2. Check claims/citations against sources.
3. Review revision history or document provenance where available.
4. Ask the author to explain key methodological/content decisions.
5. Treat external AI-detector outputs as one uncertain signal, not a verdict.

## Output
For each concern report: observed signal, location, alternative explanations, confidence, corroborating evidence, and recommended human verification. Use `AUTHENTICITY_RISK` or `PROVENANCE_RISK`, not a claim of “AI-written” unless explicit provenance evidence exists.
