# Thesis Debugger

> **Debug your research before your examiner does.**

Thesis Debugger is a Claude Agent Skill that audits academic research as a connected system rather than simply reviewing individual chapters. It looks for hidden logical, methodological, evidential, statistical, data, scope, and cross-document inconsistencies, with **Change Impact Analysis** as its signature workflow.

## What it detects

- Research-question/objective mismatch
- Theory/hypothesis/model mismatch
- Methodology/research-question mismatch
- Variable definition drift
- Sample and numeric inconsistencies
- Statistical interpretation problems
- Causal overclaims
- Unsupported or partially supported claims
- Internal contradictions across chapters/documents
- Scope inflation
- Results/conclusion mismatch
- Research dead ends
- Downstream effects of research changes
- Ambiguous supervisor feedback and its likely dependencies

## Why it exists

A thesis is not a collection of chapters. It is a connected research system. Changing one decision can affect hypotheses, variables, measurements, analyses, discussion, and conclusions. Thesis Debugger makes those dependencies explicit before the researcher edits downstream sections.

## Signature feature: Change Impact Analysis

Example request:

> I changed my methodology from OLS regression to SEM. What else needs to change?

The skill maps the change through the research dependency graph and reports what requires review, why it is affected, and how urgent the review is. It does not blindly rewrite the thesis.

## Example output

```text
# THESIS DEBUG REPORT

Research Health: 72/100 (diagnostic, not a probability of acceptance)

🔴 Critical: 3
🟠 High: 6
🟡 Medium: 11
🔵 Low: 8

## 🔴 CRITICAL #001
Type: METHODOLOGY_ERROR
Location: Chapter 3 → Research Design
Problem: The research question asks about causal effects while the stated design may only establish association.
Evidence: RQ2 asks “What is the effect of X on Y?”; Chapter 3 describes a cross-sectional survey.
Reasoning: The stated claim may exceed what the design can identify without additional assumptions/evidence.
Impact: Methodology, interpretation, discussion, conclusion.
Recommended Action: Clarify the intended estimand/claim and evaluate whether the design supports it.
```

## Installation

### Claude.ai

Anthropic currently documents custom skills as folders containing a `SKILL.md` plus optional bundled resources. To upload this skill in Claude.ai: zip the `thesis-debugger/` folder so it is the single top-level entry in the ZIP, then go to **Customize → Skills → + → Create skill → Upload a skill** and select the ZIP. The skill can then be enabled from your skills list. This requires the applicable Claude plan/features and code execution support.

### Claude Code

Claude Code discovers custom skills from the filesystem. For a personal skill, place the folder under `~/.claude/skills/`; for a project skill, place it under `.claude/skills/`. Keep `SKILL.md` at the skill directory root.

### API / other Agent Skills-compatible runtimes

Anthropic also supports custom Skills through the Skills API. The uploaded ZIP must contain the skill directory as its single top-level entry. Other Agent Skills-compatible runtimes may use their own registration mechanism; preserve the standard folder structure.

For current product details, see Anthropic's documentation: **Use skills in Claude**, **How to create custom skills**, and **Agent Skills**.

## Usage

Upload or make available one or more research artifacts, then ask naturally:

- `Debug my thesis.`
- `Find only critical errors.`
- `Check my methodology.`
- `Audit my claims and citations.`
- `Find contradictions across chapters.`
- `I changed variable X. What else needs to change?`
- `Prepare me for my thesis defense.`
- `Find research dead ends.`

Optional aliases include `/debug`, `/health`, `/impact`, `/contradictions`, `/evidence`, `/methodology`, `/data`, `/decisions`, `/feedback`, `/defense`, and `/full-audit`.

## Supported research materials

Designed to work with, when the environment can read them:

- PDF
- DOCX
- TXT
- Markdown
- CSV
- XLSX
- research notes
- questionnaires
- supervisor feedback
- university/project guidelines
- multiple documents together

The skill does not require a complete thesis. It reports which analyses are impossible when dependencies are missing.

## Reliability philosophy

Thesis Debugger is optimized for **high-signal debugging**, not maximum comment volume. A reliable finding must be grounded in evidence. Potential discrepancies are investigated before being promoted to errors.

The development targets are:

- Critical Error Recall ≥ 90%
- Finding Precision ≥ 85%
- False Positive Rate < 15%
- 100% of critical/high findings should have evidence locations when available

These are development targets, not guarantees.

## Academic integrity

The skill will not fabricate data, citations, sources, results, statistical significance, or supervisor instructions. If a user asks to “make a regression significant,” it should refuse the fabrication and help report or analyze the actual result transparently.

## Limitations

- It cannot guarantee thesis acceptance or replace an academic supervisor.
- It should not claim global novelty without sufficient literature evidence.
- Methodology-specific judgments may require a domain expert.
- A health score is heuristic, not a probability of passing.
- University-specific requirements should only be evaluated when the relevant policy/guideline is supplied.
- Statistical conclusions require sufficient data and context.

## Repository structure

```text
thesis-debugger/
├── SKILL.md
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── references/
│   ├── audit-framework.md
│   ├── error-taxonomy.md
│   ├── methodology-checks.md
│   ├── evidence-checks.md
│   ├── statistical-checks.md
│   ├── consistency-checks.md
│   ├── dependency-model.md
│   ├── severity-rubric.md
│   └── output-schema.md
├── templates/
│   ├── debug-report.md
│   ├── decision-log.md
│   └── action-plan.md
└── examples/
    ├── broken-thesis.md
    ├── expected-debug-report.md
    └── benchmark.md
```

## Roadmap

### v1.1
Improved evidence auditing.

### v1.2
Advanced statistical diagnostics.

### v1.3
More research-method templates.

### v2.0
Research Project Debugger for broader research and professional reports.

Potential future domains include grant proposals, business research, consulting reports, policy research, and technical reports. A future continuous research monitor could track changes, new risks, and resolved findings over time.

## License

MIT. See `LICENSE`.

## Ecosystem context

Anthropic's public Agent Skills repository describes skills as self-contained folders with `SKILL.md` plus optional bundled resources, and its skill-creator guidance recommends keeping the main skill focused and using reference files for progressive disclosure. Existing public academic skills tend to emphasize writing, literature/research workflows, or broader research agents; Thesis Debugger is intentionally narrower around connected-system debugging and change impact analysis.


## Validation

Run `python scripts/validate.py` to validate packaging and benchmark completeness. Static validation cannot prove model-level accuracy; evaluate the skill in Claude against the supplied benchmark and manually review findings.
