# Thesis Debugger

> **Debug your research before your examiner does.**

Thesis Debugger is a Claude Agent Skill that audits academic research as a connected research system rather than simply reviewing individual chapters. It traces the chain from research questions and literature through theory, hypotheses, variables, methodology, data, analysis, evidence, discussion, and conclusions, with **Change Impact Analysis** as its signature workflow.

## What it detects

- Research-question/objective mismatch
- Theory/hypothesis/model mismatch
- Methodology/research-question mismatch
- Variable and definition drift
- Measurement and operationalization problems
- Sample, dataset, and numeric inconsistencies
- Statistical interpretation problems
- Causal overclaims and logic jumps
- Unsupported or partially supported claims
- Internal contradictions across chapters/documents
- Scope inflation and completeness gaps
- Results/discussion/conclusion mismatch
- Research dead ends and fragile dependencies
- Downstream effects of research changes
- Ambiguous supervisor feedback and its likely dependencies
- Literature-review synthesis, coverage, gap, and contribution risks
- Reference/citation integrity and claim-source traceability
- Plagiarism/paraphrase risk when comparison text is supplied
- Academic-authenticity/provenance risk signals (not a definitive AI detector)

## Why it exists

A thesis is not a collection of chapters. It is a connected research system:

`RESEARCH QUESTION → THEORY → HYPOTHESIS → VARIABLES → MEASUREMENT → METHOD → DATA → ANALYSIS → RESULTS → DISCUSSION → CONCLUSION`

A weak link can propagate into downstream sections. Changing one research decision can therefore require changes elsewhere. Thesis Debugger makes those dependencies explicit before the researcher edits downstream sections.

The goal is not to maximize the number of comments. The goal is to identify **material, evidence-grounded research problems** and show what they affect.

## Signature feature: Change Impact Analysis

Example request:

> I changed my methodology from OLS regression to SEM. What else needs to change?

The skill maps the change through the research dependency graph and reports:

- what is directly affected
- what is likely to require an update
- what has no direct dependency
- why the dependency exists
- what should be revalidated before the change is considered complete

It does not blindly rewrite the thesis.

## Example output

The following is illustrative only; it uses hypothetical research inputs and demonstrates categorical diagnosis rather than an arbitrary overall acceptance probability.

```text
# THESIS DEBUG REPORT

Research State: CONTESTED
Decision State: FRAGILE
Confidence: MODERATE

🔴 Critical: 2
🟠 High: 4
🟡 Medium: 5
🔵 Low: 2

## 🔴 CRITICAL #001
Type: METHODOLOGY_ERROR
Location: Chapter 3 → Research Design
Problem: The research question asks about a causal effect while the stated design may only establish association.
Evidence: RQ2 asks “What is the effect of X on Y?”; Chapter 3 describes a cross-sectional survey.
Reasoning: The stated claim may exceed what the design can identify without additional assumptions or evidence.
Impact: Methodology, interpretation, discussion, conclusion.
Recommended Action: Clarify the intended estimand/claim and evaluate whether the design supports it.

## 🟠 HIGH #002
Type: ALIGNMENT_ERROR
Location: Chapter 5 → Conclusion
Problem: The conclusion makes a stronger claim than the reported results establish.
Evidence: The results report an association, while the conclusion uses causal language.
Reasoning: The inferential strength of the conclusion exceeds the evidence described in the results.
Impact: Conclusion validity and research claims.
Recommended Action: Reconcile the conclusion with the actual analysis and evidence.
```


### One-line full audit

Attach the thesis and simply write:

> **audit thesis berikut**

That short request automatically activates **FULL THESIS DEBUG** and runs all supported audit modules. The user does not need to list features or type a long prompt. Every module is shown in the final report. When a module finds no concrete error in the available evidence, its status is explicitly shown as **`Error Not Found`**. Missing evidence is disclosed separately as limited coverage.

## Installation

### Claude.ai

Anthropic documents custom Skills as folders containing a `SKILL.md` plus optional bundled resources. To upload this skill in Claude.ai, zip the `thesis-debugger/` folder so it is the single top-level entry in the ZIP, then use the applicable **Customize → Skills → Create/Upload** flow in your Claude account.

### Claude Code

Claude Code discovers custom skills from the filesystem. For a personal skill, place the folder under `~/.claude/skills/`; for a project skill, place it under `.claude/skills/`. Keep `SKILL.md` at the skill directory root.

### API / other Agent Skills-compatible runtimes

For Skills-compatible runtimes, preserve the standard skill directory structure and keep `SKILL.md` at the directory root. Follow the host platform's current registration/upload mechanism.

## Usage

Upload or make available the research artifacts relevant to the audit, then ask naturally. A broad request automatically expands into the complete workflow:

- `audit thesis berikut`
- `Debug my thesis.`
- `Find only critical errors.`
- `Check my methodology.`
- `Audit my claims and citations.`
- `Audit my literature review for gaps and weak synthesis.`
- `Check reference/citation integrity.`
- `Compare this draft with these sources for paraphrase risk.`
- `Check academic-authenticity risks without deciding whether AI wrote it.`
- `Find contradictions across chapters.`
- `I changed variable X. What else needs to change?`
- `Prepare me for my thesis defense.`
- `Find research dead ends.`

The skill also supports narrower workflows through internal routing, including evidence, literature, citation integrity, methodology, data/statistics, consistency, change impact, supervisor feedback, defense, and academic-integrity analysis.

## Supported research materials

Designed to work with, when the environment can read them:

- Theses and dissertations
- Research papers and manuscripts
- Research proposals
- PDF, DOCX, TXT, and Markdown documents
- CSV/XLSX datasets and research tables
- Research notes
- Questionnaires and instruments
- Reference lists and citation exports
- Supervisor/advisor feedback
- University or project guidelines
- Multiple documents and versions together
- Supplied source text for plagiarism/paraphrase comparison

The skill does not require a complete thesis. It reports which analyses are blocked by missing, ambiguous, or unverified inputs rather than silently filling the gaps.

## Reliability philosophy

Thesis Debugger is optimized for **high-signal research auditing**, not maximum comment volume. A finding should be grounded in available evidence and tied to a material consequence.

The system is designed to:

- distinguish observation from inference and recommendation
- distinguish confirmed errors from likely/potential issues
- avoid treating missing information as an error
- preserve stable finding IDs across iterative audits
- trace critical/high findings to locations when available
- search for contradictory evidence and alternative explanations
- separate research-system dependencies from superficial text similarity
- downgrade severity when evidence is indirect
- require verification paths for consequential findings
- avoid fabricating citations, data, results, significance, or provenance

Development targets include:

- Critical/High Error Recall ≥ 90%
- Finding Precision ≥ 85%
- False Positive Rate < 15%
- 100% of critical/high findings should have evidence locations when available

These are development targets, not guarantees. Static repository validation is a packaging check, not proof of model-level accuracy. Real evaluation should include adversarial cases, mostly-correct cases, and human review.

## Research integrity

The skill includes four integrity-focused modules:

**Literature Review Auditor:** evaluates synthesis, competing findings, source relevance/quality, gap logic, contribution alignment, and coverage claims when a defensible search/selection record is available.

**Reference & Citation Integrity Checker:** checks citation↔reference linkage, duplicates, metadata consistency, quotation attribution, citation drift, and whether supplied sources support cited claims. Bibliographic correctness and substantive support are assessed separately.

**Plagiarism / Paraphrase Risk Detection:** compares supplied source and target text for exact overlap, near-exact overlap, close paraphrase, patchwriting, unattributed quotation, and self-overlap. It reports review risk rather than treating similarity alone as proof of misconduct.

**AI-Generated Writing / Academic Authenticity Check:** reviews observable provenance and writing-pattern signals such as abrupt voice shifts, unverifiable citations, generic templating, and version-history gaps. It does not claim that style alone can reliably determine whether AI wrote a passage.

The skill will not fabricate data, citations, sources, results, statistical significance, or supervisor instructions.

## Academic integrity safeguards

If a user asks the skill to fabricate or manipulate research, such as:

- inventing data
- manufacturing citations
- changing results to become significant
- hiding contradictory findings
- falsely attributing a quotation
- creating a fake supervisor instruction

the skill should refuse the fabrication and help analyze or report the actual research transparently.

## Limitations

- It cannot guarantee thesis acceptance or replace an academic supervisor.
- It should not claim global novelty without sufficient literature evidence.
- Methodology-specific judgments may require a domain expert.
- Literature-review coverage cannot be claimed exhaustive without a defensible search/selection record.
- Plagiarism/paraphrase review is risk-based unless source text is available for comparison; similarity is not proof of misconduct.
- Academic-authenticity review is not a reliable standalone AI detector; style alone cannot establish AI authorship.
- A health score, when used, is heuristic and not a probability of passing.
- University-specific requirements should only be evaluated when the relevant policy/guideline is supplied.
- Statistical conclusions require sufficient data and context.
- Dataset or source verification may be limited by what the execution environment can actually access.

## Repository structure

```text
thesis-debugger/
├── SKILL.md
├── README.md
├── references/
│   ├── audit-framework.md
│   ├── error-taxonomy.md
│   ├── methodology-checks.md
│   ├── evidence-checks.md
│   ├── literature-review-checks.md
│   ├── citation-integrity-checks.md
│   ├── paraphrase-risk-checks.md
│   ├── authenticity-checks.md
│   ├── statistical-checks.md
│   ├── consistency-checks.md
│   ├── dependency-model.md
│   ├── severity-rubric.md
│   └── output-schema.md
├── templates/
│   ├── debug-report.md
│   ├── decision-log.md
│   └── action-plan.md
├── examples/
│   ├── broken-thesis.md
│   ├── integrity-test-pack.md
│   ├── expected-debug-report.md
│   ├── benchmark.md
│   └── benchmark-manifest.csv
├── scripts/
│   └── validate.py
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── QUALITY-GATES.md
```

## Roadmap

### v2.1.0

- Literature Review Auditor
- Reference & Citation Integrity Checker
- Plagiarism / Paraphrase Risk Detection
- Academic Authenticity / AI-Generated Writing Risk review
- Integrity-specific finding types and verification requirements
- Expanded synthetic benchmark coverage
- Stronger false-positive controls for integrity modules

### v1.0.0

- Production-oriented research-system debugging workflow
- Research model and dependency graph
- Multi-pass diagnostic workflow
- Change Impact Analysis
- Evidence-first and false-positive controls
- Methodology, evidence, statistical, consistency, scope, and causality diagnostics
- Research decision ledger
- Research dead-end detection
- Supervisor feedback translation and impact analysis
- Defense simulator
- Severity taxonomy and heuristic research health score
- Incomplete-document handling and academic-integrity safeguards

### Future

- Expanded domain-specific benchmark suites
- More automated dependency and version-diff reporting
- Additional statistical and methodological edge cases
- Broader evaluation tooling for false positives and critical/high finding recall
- Research-project monitoring across evolving document versions

## License

Released under the MIT License. See `LICENSE`.

## Ecosystem context

Thesis Debugger is one component of a broader **Debugger Series**: tools built around the idea that many bad outcomes come from errors in the reasoning process before the final answer, research conclusion, or decision.

Financial Debugger applies the same philosophy to financial decisions. Thesis Debugger applies it to connected academic research systems.

## Validation

Run:

```bash
python scripts/validate.py
```

before release. Static validation checks repository integrity and test coverage; it does not prove that the model will make every research judgment correctly.
