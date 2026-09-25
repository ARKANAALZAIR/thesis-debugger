# Synthetic Benchmark Suite

Purpose: evaluate recall, precision, traceability, and false-positive control. All cases are synthetic.

## Broken cases — expected to produce findings

### B01 — RQ/Objectives mismatch
**Input:** RQ2 asks “How does X affect Y?” Objective 2 says “Describe the prevalence of X.”
**Expected:** ALIGNMENT_ERROR, MEDIUM/HIGH depending on centrality. Explain causal/associational mismatch.
**Do not flag:** Mere wording differences that preserve the same target.

### B02 — Hypothesis/model mismatch
**Input:** H2 predicts moderation by Z, but the model contains only X and Y and no interaction/stratification logic is documented.
**Expected:** DEPENDENCY_ERROR or ALIGNMENT_ERROR, HIGH if H2 is central.

### B03 — Methodology mismatch
**Input:** RQ asks for a causal effect; design is cross-sectional observational; no identification strategy/assumptions supplied.
**Expected:** METHODOLOGY_ERROR/CAUSALITY_ERROR, HIGH or CRITICAL depending on centrality.

### B04 — Variable inconsistency
**Input:** Chapter 2 defines “financial literacy” with a 10-item scale; Chapter 3 uses “financial knowledge” as a single test score with no explanation.
**Expected:** DEFINITION_ERROR, HIGH if the hypothesis concerns the former construct.

### B05 — Sample inconsistency
**Input:** Methods N=500; regression table N=461; no missing/exclusion note.
**Expected:** POTENTIAL then CONSISTENCY_ERROR if no explanation is available; HIGH when material.
**Do not flag:** If table note clearly says 39 observations were excluded for documented missingness.

### B06 — Statistical interpretation
**Input:** p=.42; text says “statistically significant positive effect.”
**Expected:** STATISTICAL_ERROR, HIGH.

### B07 — Causal overclaim
**Input:** r=.72 from a correlational study; conclusion says “X causes Y.”
**Expected:** CAUSALITY_ERROR, HIGH.

### B08 — Unsupported claim
**Input:** “AI adoption always increases productivity,” citation is present but supplied source only reports a small association in one industry.
**Expected:** EVIDENCE_ERROR/SCOPE_ERROR, HIGH.

### B09 — Conclusion/result mismatch
**Input:** Results show H1 not supported; conclusion says H1 was confirmed.
**Expected:** LOGIC_ERROR/CONSISTENCY_ERROR, CRITICAL or HIGH.

### B10 — Scope inflation
**Input:** Sample = 200 students at one university; conclusion says “all university students in Indonesia.”
**Expected:** SCOPE_ERROR, HIGH/MEDIUM depending on claims.

### B11 — Dependency removal
**Input:** H3 is removed from the model but the discussion and conclusion still interpret H3.
**Expected:** DEPENDENCY_ERROR, HIGH.

### B12 — Research dead end
**Input:** RQ asks “What is the causal effect?”; design is descriptive cross-sectional survey with no causal identification logic.
**Expected:** Research dead-end risk, METHODOLOGY_ERROR/CAUSALITY_ERROR.

### B13 — Evidence contradiction
**Input:** Source summary says intervention had no detectable effect; thesis claims the source proves a positive effect.
**Expected:** EVIDENCE_ERROR, HIGH.

### B14 — Method terminology contradiction
**Input:** Methods says “random sampling”; appendix says participants were recruited through convenience posting and self-selection.
**Expected:** METHODOLOGY_ERROR/CONSISTENCY_ERROR, HIGH.

### B15 — Numerical table contradiction
**Input:** Table total is 240; text says total sample is 260; no subgroup explanation.
**Expected:** CONSISTENCY_ERROR, MEDIUM/HIGH.

## Mostly-correct cases — should avoid false positives

### G01 — Explained different N
**Input:** Survey collected N=300; regression N=287. Table note documents 13 observations excluded for missing outcome values.
**Expected:** No error. Optionally INFO/traceability observation.

### G02 — Construct synonym with operational continuity
**Input:** Chapter 1 uses “digital adoption”; Chapter 3 says “digital adoption (technology usage intensity)” and explicitly defines the measurement as a validated usage-intensity scale.
**Expected:** No definition error if the construct identity and measurement are clearly maintained.

### G03 — Negative result handled correctly
**Input:** H1 predicts positive effect; coefficient is negative and significant; discussion explicitly states H1 is not supported and interprets the negative direction cautiously.
**Expected:** No sign error. Possibly INFO observation.

### G04 — Association language matches design
**Input:** Cross-sectional survey; RQ asks whether X is associated with Y; results and conclusion use “associated with,” not “causes.”
**Expected:** No causality error.

### G05 — Subsample analysis
**Input:** Main sample N=500; subgroup analysis N=180; section heading and table note clearly identify the subgroup.
**Expected:** No sample inconsistency.

### G06 — Mixed methods explicitly integrated
**Input:** Survey addresses prevalence; interviews explain mechanisms; methods explain sequencing and integration; conclusion distinguishes quantitative and qualitative contributions.
**Expected:** No methodology mismatch merely because two methods are used.

### G07 — Qualitative study
**Input:** RQ asks how participants experience X; study uses purposive sampling, interviews, thematic analysis, and evidence excerpts.
**Expected:** Do not flag absence of regression or power analysis.

### G08 — Causal design with assumptions stated
**Input:** Experimental assignment, treatment/control groups, outcome measurement, and analysis are documented; conclusion uses causal language tied to the randomized design.
**Expected:** No automatic causality error.

### G09 — University guideline differs from generic convention
**Input:** Supplied university guideline requires a specific chapter order; thesis follows it even though another generic template differs.
**Expected:** Treat supplied guideline as authoritative project-specific standard.

### G10 — Partial document
**Input:** Only Chapter 1 is available. It contains RQs and objectives but no methodology/results.
**Expected:** Perform supported structure/alignment checks; explicitly state that downstream dependency analysis is unavailable. Do not invent findings about missing chapters.


## Integrity and literature cases — expected behavior

### B16 — Literature gap overclaim
**Input:** Review claims “no studies have examined X,” but supplied literature includes two directly relevant studies on X in the same population and period.
**Expected:** LITERATURE_REVIEW_ERROR / SCOPE_ERROR, HIGH or MEDIUM depending on contribution centrality.
**Do not flag:** If the claim is explicitly narrowed to a different context and the cited studies are outside that scope.

### B17 — Weak literature synthesis
**Input:** Ten studies are summarized one-by-one; the review never compares methods, findings, contradictions, or unresolved issues, yet claims a strong theoretical gap.
**Expected:** LITERATURE_REVIEW_ERROR, MEDIUM/HIGH.

### B18 — Citation-reference mismatch
**Input:** Text cites “Smith, 2024,” but bibliography has no Smith 2024 entry; another entry uses the same author/year label for a different paper.
**Expected:** CITATION_INTEGRITY_ERROR, HIGH when the citation supports a central claim.

### B19 — Citation present but unsupported
**Input:** Citation is correctly formatted and linked to a source, but the supplied source only reports correlation while the thesis states the source proves causality.
**Expected:** CITATION_SUPPORT_RISK / EVIDENCE_ERROR / CAUSALITY_ERROR, HIGH.

### B20 — Close paraphrase
**Input:** Supplied source passage and target draft preserve distinctive wording and sentence structure with minor synonym swaps and no quotation/clear attribution.
**Expected:** PARAPHRASE_RISK, HIGH when evidence is direct; include both locations and minimum matched evidence.

### B21 — Unattributed quotation
**Input:** Distinctive source wording appears in draft without quotation marks, despite a citation.
**Expected:** PARAPHRASE_RISK or CITATION_INTEGRITY_ERROR, HIGH depending on extent.

### B22 — Authenticity risk from provenance + voice shift
**Input:** Supplied drafts show an unexplained abrupt change in terminology/style, several citations cannot be traced, and authorship/provenance is undocumented.
**Expected:** AUTHENTICITY_RISK / PROVENANCE_RISK, MEDIUM/HIGH with explicit alternative explanations and human verification steps.

### B23 — AI style alone is not proof
**Input:** Writing is polished, formal, and generic but all sources and revision history supplied are consistent.
**Expected:** No AI-authorship finding. At most INFO about provenance if the user requested it and evidence is genuinely incomplete.

## Mostly-correct integrity cases

### G11 — Literature scope is explicitly bounded
**Input:** Review says “Within Indonesian public universities from 2021–2025, five studies were identified” and provides a documented search strategy plus inclusion criteria.
**Expected:** Do not flag “not exhaustive globally.”

### G12 — Correct citation but weak source not overstated
**Input:** Source reports association and thesis says “associated with.”
**Expected:** No citation-support or causality error.

### G13 — Proper quotation
**Input:** Exact source wording is in quotation marks with citation and page/section locator.
**Expected:** No paraphrase-risk finding.

### G14 — Legitimate self-reuse disclosed
**Input:** Thesis reuses a methods description from the author's prior proposal, with disclosure and supervisor/institution context supplied.
**Expected:** No automatic plagiarism finding; optionally INFO about policy verification.

### G15 — Style shift has an alternative explanation
**Input:** One chapter is more formal because it was edited by a supervisor; revision notes document the edit.
**Expected:** No authenticity finding from style alone.

### G16 — Citation list is incomplete because sources are still being added
**Input:** Draft explicitly marked as early-stage and user asks whether citation integrity can be completed.
**Expected:** Report incomplete verification, not a fabricated citation error.


## AUTO-001 — Broad prompt must trigger full audit

Input: a readable thesis plus the short prompt `audit thesis berikut`.

Expected behavior:
- automatically run FULL THESIS DEBUG;
- execute all supported modules;
- display every module status;
- use `Error Not Found` when a module finds no concrete error in available evidence;
- separately disclose limited coverage when a module needs unavailable source/data/feedback;
- do not ask the user to provide a long prompt or module checklist.

## AUTO-002 — Finding count reconciliation

Input: a thesis that triggers the same underlying issue in multiple modules.
Expected behavior:
- deduplicate the underlying issue into one unique Finding ID;
- assign one Primary Module;
- optionally list other modules under Related Modules;
- severity totals and module primary-finding counts must reconcile to the number of unique Finding IDs.

## AUTO-003 — All-module status completeness

Input: a thesis with several real errors, incomplete chapters, and no supervisor feedback.
Expected behavior:
- execute M01–M22 without short-circuiting;
- display all 22 status blocks exactly once;
- use `Error Not Found` when no concrete error is found;
- disclose `PARTIAL` or `LIMITED` coverage when evidence is missing;
- never replace a module with “covered above.”



## Final hardening regression cases

### AUTO-004 — Missing core evidence is NOT ASSESSABLE
**Input:** Proposal contains a method plan but no dataset/results. Statistical interpretation cannot inspect actual estimates.
**Expected:** M07 is `NOT ASSESSABLE` when its core diagnostic is blocked; it is not `Error Not Found`. Other M07-adjacent checks may be reported elsewhere with their own evidence.

### AUTO-005 — Partial module can still find an error
**Input:** Method section is present, result tables are missing, and the method claims a test that cannot answer the stated RQ.
**Expected:** Relevant methodology module is `FOUND` with `Coverage: PARTIAL`; missing results do not erase the confirmed method mismatch.

### AUTO-006 — Error Not Found requires usable evidence
**Input:** No supervisor feedback file is supplied.
**Expected:** M15 is `NOT ASSESSABLE`, not `Error Not Found`.

### AUTO-007 — Severity calibration
**Input:** A possible inconsistency has a plausible project-specific explanation that the document does not resolve.
**Expected:** Do not force CRITICAL/HIGH; use LIKELY/POTENTIAL plus verification or a lower severity consistent with evidence.

### AUTO-008 — Finding ownership deduplication
**Input:** M04 and M10 flag the same variable-definition mismatch and recommend the same correction.
**Expected:** One Finding ID, one Primary Module (M04 by default), M10 listed as Related Module, one global count.

### AUTO-009 — Health score transparency
**Input:** Data and conclusions are unavailable, while six other dimensions are assessable.
**Expected:** Data and Conclusion Alignment are N/A, remaining dimension weights are renormalized using the fixed formula, and every scored dimension has a basis.

### AUTO-010 — No arbitrary score from finding counts
**Input:** Two critical findings and four medium findings are detected.
**Expected:** Do not derive the health score from those counts; score dimensions from documented diagnostic bases only.

### AUTO-011 — Audit integrity gate
**Input:** A draft report references TD-007 in M10 but TD-007 does not exist in Detailed Findings.
**Expected:** Audit Integrity Check fails; the report must be repaired before being returned.
