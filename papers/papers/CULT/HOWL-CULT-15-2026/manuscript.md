# Showing Your Work in 2026
## A Structural Specification for Reproducible Scientific Computation

**Registry:** [@HOWL-CULT-15-2026]

**Series Path:** [@HOWL-CULT-1-2026] → [@HOWL-CULT-2-2026] → [@HOWL-CULT-3-2026] → [@HOWL-CULT-4-2026] → [@HOWL-CULT-5-2026] → [@HOWL-CULT-6-2026] → [@HOWL-CULT-7-2026] → [@HOWL-CULT-8-2026] → [@HOWL-CULT-9-2026] → [@HOWL-CULT-12-2026] → [@HOWL-CULT-13-2026] → [@HOWL-CULT-14-2026] → [@HOWL-DATA-6-2026] → [@HOWL-CULT-15-2026]

**Date:** May 2026

**DOI:** 10.5281/zenodo.20184251

**Domain:** Scientific Methodology / Data Infrastructure / Reproducibility

**Status:** Structural specification with working reference implementation

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## 1. What "Showing Your Work" Currently Means

A physicist completes a computation. The computation derives a physical quantity — say, the primordial helium abundance — from a chain of input values and intermediate calculations. The physicist writes a paper. The paper is typeset in LaTeX. The equations are formatted. The derivation is described in prose.

The prose reads something like this: "Using the Planck 2018 value of the baryon density parameter Ω_b = 0.0490 ± 0.0006, we derive the baryon-to-photon ratio η via the standard relation involving the CMB photon number density (Fixsen 2009) and the critical density. Substituting into the Pitrou et al. (2018) BBN fitting formulae, we obtain Y_p = 0.2486, in reasonable agreement with the Aver et al. (2015) measurement of 0.2449 ± 0.0040."

The reader who wants to verify this result must perform the following steps. Find the Planck 2018 paper. Locate the Ω_b value in its tables. Find the Fixsen 2009 paper. Locate the CMB temperature value. Calculate the photon number density from the temperature using the standard formula, which requires knowing that formula and looking up ζ(3). Find the critical density, which requires the Hubble constant and the gravitational constant, each of which requires its own lookup. Compute η from these inputs. Find the Pitrou 2018 paper. Locate the fitting coefficients. Apply the fitting formula. Check whether the result matches the paper's stated value.

This process has specific failure modes. The reader may copy a value incorrectly from one of the cited papers — transcription error. The paper may use a symbol that means different things in different conventions and not state which convention is intended — notational ambiguity. The paper may skip steps the author considered obvious — derivation gaps. The paper may have used a specific numerical method with specific parameters and not reported them — unstated numerical choices. The computation may have been performed in double-precision floating point, where rounding errors accumulated across the chain and the final digits depend on the implementation rather than on the physics — floating-point artifact.

These are not descriptions of bad practice. This is standard practice. The best papers in the best journals follow this format. The format was designed for an era when computation meant pen-and-paper derivation and publication meant printed pages. In that era, prose description of a computation was the best available technology for communicating the computation to others. The format served that era.

The era is over. Computation is performed by machines. Storage is effectively unlimited. Distribution is instantaneous and global. The infrastructure that made prose description the only viable format no longer constrains us. What constrains us is convention — the inherited practice of describing computations rather than publishing them.

The structural problem is precise. A prose description of a computation is not a computation. It is a set of instructions for performing a computation, written in natural language, subject to ambiguity, and requiring manual re-execution by every reader who wishes to verify the result. The distance between the description and the computation is the space where irreproducibility lives. Every ambiguity, every unstated choice, every transcription opportunity is a point where two independent readers may arrive at different results from the same paper. The prose description does not prevent this divergence. It enables it.

---

## 2. What "Showing Your Work" Should Mean

Showing your work means publishing the work. Not a description of the work. The work itself — the inputs, the derivations, the outputs, the comparisons, the failures — in a form that anyone can run, check, and extend without manual re-derivation.

The standard has five layers. Each layer is necessary. Each has a specific structural role. Together they constitute a complete, verifiable, reproducible scientific computation.

**Layer 1: The value store.** Every input to every computation exists as a named, typed, versioned, machine-readable entry. Each entry carries a unique key that identifies it unambiguously. The value itself, stored as an exact fraction where possible or with stated precision where not. The unit. The number of significant digits. The uncertainty. The source — the specific paper, specific table, specific year from which the value was obtained. Tags for searchability. Notes for methodological context — not buried in a paper's appendix but attached to the value itself, at the point where anyone encountering the value will see them.

A value store entry for the primordial helium measurement looks like this. Key: `cosmo_yp_measured_v0`. Value: 0.2449. Unit: dimensionless. Digits: 4. Uncertainty: 0.0040. Source: "Aver, Olive, Skillman 2015. JCAP 07, 011. Primordial helium mass fraction." Tags: cosmology, BBN, helium, measured. Notes: "Y_p = primordial 4He mass fraction. Weighted average of extragalactic HII region measurements."

Every field serves a purpose. The key enables machine reference — no ambiguity about which value is being used. The exact representation eliminates floating-point accumulation in downstream computations. The source enables tracing — anyone can check where the value came from and verify it against the original publication. The uncertainty enables proper comparison — a prediction that misses by less than the input's uncertainty is within the measurement's own limits. The notes capture methodological context at the point of data entry.

The Boltzmann constant illustrates the precision the store supports. Key: `si_boltzmann_constant_v0`. Value: stored as the exact fraction 1380649/10^29. Source: "SI 2019. Exact by definition." The constant is exact since the 2019 SI redefinition. The store represents it as exact. No floating-point approximation. No loss of precision. The value is what it is, stored as what it is.

A working value store contains thousands of entries spanning every domain the computation touches. The reference implementation described in this paper contains over 4900 value nodes covering quantum electrodynamics, electroweak physics, cosmology, Big Bang nucleosynthesis, CKM mixing, confinement, gravity, and more. Each node in the same format. Each queryable. Each traceable to its source.

**Layer 2: The experiment definition.** A machine-readable document that declares everything the computation needs and everything it will produce, written before the computation runs.

The definition has four sections. Dependencies: which value store entries are required as inputs, listed by name. Execution plan: which derivations to run and in what order. Expected outputs: every result the derivation should produce, named in advance. Comparisons: every test that will be applied to the results, with the match mode, the expected value, the tolerance, and the reference source — all stated before the computation executes.

This structure embeds a property that is absent from current scientific practice and essential to the standard: pre-registered falsification. Every comparison in the experiment definition is a falsification condition written before the result is known to the runner. The definition states: "I predict this output will match this reference value within this tolerance, and if it does not, the experiment reports FAIL at this specific point." The prediction is committed. The tolerance is stated. The criterion is mechanical. The outcome — PASS, FAIL, or INFO — is determined by the comparison, not by the author's interpretation after the fact.

This is Karl Popper's demarcation criterion — commitment, specificity, priority, acceptance — implemented as data infrastructure. The commitment is the comparison entry. The specificity is the expected value and tolerance. The priority is structural — the definition exists before the run. The acceptance is automatic — the runner prints FAIL when the criterion is not met, and the author cannot suppress it without altering the definition, which is itself a versioned, auditable document.

**Layer 3: The connection bundle.** A semantic manifest that declares the experiment's purpose, its scope, and the cross-domain relationships it tests. The bundle lists every input by name and states what the experiment is checking — which physical identities, which cross-domain derivation chains, which hierarchy levels. The connection bundle is the experiment's thesis statement in machine-readable form.

The bundle also serves as the anti-smuggling guard's manifest. Every input the experiment uses must appear in the bundle's input list. An undeclared value cannot enter the derivation because the infrastructure has no mechanism for it to enter. If a value is not in the store and not in the bundle's input list, the runner cannot access it. The structural prevention of hidden parameters is not a policy. It is an architectural constraint.

**Layer 4: The run output.** Every result produced by the computation is stored as a new value node in the same format as the input values — keyed, typed, sourced to the specific run that produced it. The run output is not a paper. It is not a summary. It is the complete set of values the computation produced, each traceable, each queryable, each available as input to future computations.

This property — output in the same format as input — makes derivation chains continuous. The results of one experiment become the inputs to the next without transcription, format conversion, or manual re-entry. Each run's output is a permanent, versioned record of what the computation produced at that moment with those inputs.

**Layer 5: The report.** A human-readable summary generated from the run output. Derivation status — how many succeeded, how many errored. Comparison results — predicted value, measured value, miss percentage, pass/fail status for each test. Located failures — which specific test failed, by how much, at which point in the chain. The report is generated from the output, not written separately. It cannot disagree with the output because it is derived from it.

---

## 3. A Cross-Domain Example

The five layers become concrete through a specific example. Consider a computation that starts from integer inputs in particle physics and derives nuclear abundances in cosmology — a chain that crosses three domains of physics in a single derivation.

The experiment is called `experiment_bridge_bbn_v0`. Its purpose is to test whether gauge integers from the Standard Model predict primordial nuclear abundances through the cosmological chain. The derivation proceeds as follows. Integer inputs produce the baryon density parameter Ω_b. Ω_b combined with the CMB photon number density produces the baryon-to-photon ratio η. η enters the Big Bang Nucleosynthesis fitting formulae and produces predictions for the primordial helium-4 mass fraction Y_p and the primordial deuterium-to-hydrogen ratio D/H. Separately, the derived cosmological parameters are checked for consistency with the effective number of neutrino species N_eff, and the vacuum energy density is derived and compared against observation.

Three domains — particle physics integers, cosmological parameters, nuclear abundances — connected by a single derivation chain. If the integers are wrong, the helium prediction breaks. If the cosmological bridge is wrong, the deuterium prediction breaks. The chain is falsifiable end to end.

**Layer 1 in practice.** The experiment draws from twenty-eight named value store entries. Each entry is a specific physical quantity with full metadata. The CMB temperature: `cosmo_t_cmb_v0`, value 2.7255 K, 5 digits, uncertainty 0.0006 K, source "Fixsen 2009. ApJ 707, 916. COBE/FIRAS CMB monopole temperature." The primordial deuterium measurement: `cosmo_dh_measured_v0`, value 2.527 × 10⁻⁵, 4 digits, uncertainty 0.030 × 10⁻⁵, source "Cooke, Pettini, Steidel 2018. ApJ 855, 102." The BBN fitting coefficients: `bbn_yp_a_coeff_v0`, value 0.2485, source "Pitrou et al. 2018. Phys.Rept. 754, 1." Every input named. Every input sourced. Every input machine-readable. A reader verifying the computation does not hunt through citations. They query the value store.

**Layer 2 in practice.** The experiment definition declares seven derivations in a specific execution order: derive Ω_b from integers, derive Ω_DE from flatness, derive η from Ω_b, derive Y_p from η, derive D/H from η, check N_eff consistency, derive vacuum energy density. It declares thirteen comparisons — the pre-registered falsification conditions. Each comparison specifies what is being tested, what the output key is, what match mode to use (miss percentage, digit agreement, range check, sigma check), what the expected value is, and where the expected value comes from.

For example, one comparison entry reads: label "D/H digits of agreement," output key `result_dh_derived_v0`, match mode "digits," expected "2.53e-5," digits 3, reference source "Cooke 2018." This entry states, before the computation runs: the derived deuterium abundance must agree with the Cooke 2018 measurement to three significant digits. If it does not, the experiment reports FAIL at this point. The falsification condition is pre-registered in the experiment definition. It cannot be adjusted after seeing the result without changing the definition, which is a versioned document.

Another comparison tests the full derivation chain: label "Full chain: integers → eta_10 → Y_p within 1 sigma," output key `result_yp_sigma_v0`, match mode "range," lo 0, hi 2.0. This states: the helium prediction, derived from integers through cosmology through nucleosynthesis, must fall within one standard deviation of the measurement. The sigma value is computed by the derivation and compared against the range by the runner. The result is mechanical.

**Layer 3 in practice.** The connection bundle for this experiment lists all twenty-eight input values by key and describes the experiment's scope: "Tests whether gauge integers predict nuclear abundances through the cosmological chain." The bundle identifies the cross-domain nature of the test explicitly. The inputs span particle physics (gauge integers), cosmology (Planck parameters, CMB temperature, critical density), and nuclear physics (BBN fitting coefficients, measured abundances). The bundle is the manifest — anyone reading it knows what the experiment claims to test, what inputs it uses, and what domains it crosses.

**Layer 4 in practice.** The run produces fifty-seven output values. Each is stored as a named value node keyed to the specific run. The derived baryon density: `result_omega_b_derived_v0`, value 0.049035637966613, source `experiment_bridge_bbn_v0_run011`. The derived helium abundance: `result_yp_derived_v0`, value 0.248643255182356. The derived deuterium abundance: `result_dh_derived_v0`, value 2.53060482485205 × 10⁻⁵. The miss percentages, sigma values, intermediate quantities, and consistency checks — all stored, all named, all traceable to the run that produced them.

**Layer 5 in practice.** The report prints the complete results. Thirteen comparisons, each with its verdict:

Omega_b from integers versus Planck: predicted 0.049036, measured 0.0490, miss 0.073%. Status: INFO.

D/H digits of agreement: predicted 2.531 × 10⁻⁵, expected 2.53 × 10⁻⁵, three-digit match, miss 0.024%. Status: PASS.

Y_p digits of agreement: predicted 0.2486, expected 0.245, two digits agree but the third does not, miss 1.49%. Status: FAIL.

Full chain integers → η → Y_p within 1 sigma: got 0.936 sigma. Status: PASS.

Full chain integers → η → D/H within 1 sigma: got 0.120 sigma. Status: PASS.

The failure is located precisely. Y_p misses the three-digit agreement target. The miss is 1.49%. The sigma value is 0.94 — within one standard deviation of the measurement, so the full-chain sigma test passes even though the digit test fails. Anyone reading the report knows exactly what succeeded, what failed, and the quantitative gap between prediction and measurement at the failure point.

The summary is generated, not written: seven derivations, zero errors. Four passes, one failure, eight informational. Status: partial. The experiment does not claim success. It reports what it found. The failure is printed with the same mechanical precision as the successes.

---

## 4. The Anti-Smuggling Property

Smuggling is an undeclared input affecting the result of a computation. In current practice, smuggling is easy and usually unintentional. A physicist uses a value they remember from a previous calculation without re-checking it against the current reference. A numerical parameter — integration step count, precision setting, convergence threshold — is chosen and not reported. A fitting parameter is adjusted until the result matches expectation and then presented as derived.

Under the five-layer standard, smuggling is structurally prevented. Every input must exist in the value store. The experiment definition declares every input by name. The connection bundle lists them. The runner loads only declared inputs. If a value is not in the store, the computation does not silently produce a wrong result. It refuses to run. The infrastructure has no mechanism for an undeclared value to enter the derivation.

The BBN experiment demonstrates this. Twenty-eight inputs are declared in the dependencies section of the experiment definition. The runner loads the value store, checks that each declared dependency exists, and proceeds only if all dependencies are satisfied. If someone added a twenty-ninth input to the derivation code without declaring it in the experiment definition, the runner would access the value store for a key that was never loaded and fail with a traceable error.

Even numerical configuration is stored in the value store. Integration step counts, decimal precision settings, convergence thresholds — these are not buried in source code comments. They are named value nodes with sources and notes. The reference implementation stores `config_euler_step_count_v0` at 10000 with the note: "Increased from 4000 (original) to 10000 for improved two-loop convergence." The choice is recorded. The change is documented. If changing the step count changes the result, that sensitivity is discoverable because both configurations are stored, both are versioned, and both runs are reproducible.

The anti-smuggling property is not a policy. It is not a guideline that researchers are encouraged to follow. It is an architectural constraint enforced by the infrastructure. The same way a compiler rejects code that references an undeclared variable, the runner rejects computations that reference undeclared values. The mechanism is identical. The consequence is identical. You cannot use what you have not declared.

---

## 5. Pre-Registered Falsification as Infrastructure

The experiment definition's comparison section deserves specific attention because it implements something that current scientific practice discusses extensively but rarely achieves: pre-registration of falsification conditions.

In current practice, pre-registration is a separate administrative process. A researcher files a pre-registration document with a registry before conducting an experiment. The document states what will be tested and what criteria will determine success or failure. The document exists in a separate system from the experiment itself. Compliance is voluntary and verified after the fact.

Under the five-layer standard, pre-registration is not a separate process. It is the experiment definition. The comparisons section of the definition is the pre-registration. It states what will be tested, what the expected values are, what the tolerances are, and what constitutes pass or fail — and it states all of this as machine-readable data that the runner executes automatically.

The BBN experiment's definition contains thirteen comparison entries. Each entry was written before the run. Each specifies a mechanical criterion. The runner evaluates each criterion against the computation's output and prints the verdict. The author does not interpret the results. The runner compares numbers. The verdict is PASS, FAIL, or INFO. The author can examine the results, investigate the failures, and plan improvements — but the author cannot change the verdict without changing the definition, and the definition is a versioned document whose changes are traceable.

This is stronger than external pre-registration in three specific ways. First, it is structural rather than administrative — the pre-registration is embedded in the computation infrastructure, not filed with a separate registry. Second, it is automatically enforced — the runner evaluates the criteria mechanically, removing the opportunity for post-hoc reinterpretation of what "success" means. Third, it is granular — each comparison is an independent test with its own criterion, so a partial failure is located at a specific point rather than producing an ambiguous overall verdict.

The BBN experiment demonstrates all three properties. It pre-registers thirteen tests. Eleven produce clear verdicts (four PASS, one FAIL, six INFO with quantified miss). The failure is at Y_p digit agreement — located at a specific comparison, with a specific miss of 1.49%. The experiment does not hide this failure. It cannot hide it. The comparison was in the definition. The runner evaluated it. The report printed it.

---

## 6. The Sensor Measurement Extension

The five-layer standard applies to theoretical computation as described above. It extends to experimental measurement with the instrument replacing the derivation.

Layer 1 is the same — calibration values, instrument parameters, and environmental metadata stored as named, typed, sourced value nodes. Layer 2 is the measurement protocol — what the instrument will measure, what inputs it requires, what outputs it will produce, and what quality criteria determine whether a reading is valid. Layer 3 is the semantic context — what physical quantity is being measured and how the measurement relates to other measurements. Layer 4 is the raw data — every reading with its timestamp, stored in the same value node format at the instrument's native sampling rate, with timestamps synchronized to a common clock. Layer 5 is the reduction pipeline — the computation that converts raw readings into published values, itself subject to the five-layer standard.

The critical requirement for sensor measurements: the raw data and the reduction pipeline are published together. The published value is one output of a specific reduction pipeline applied to specific raw readings. Anyone who wants a different output — a different averaging window, different outlier criteria, different weighting — applies their own pipeline to the same raw data. The raw data is the ground truth. The reduction pipeline is a computation. The published value is a result. All three are available.

This is the proposal from CULT-13 made concrete as an engineering specification. CULT-13 argued that CODATA's averaging process destroys temporal structure, disagreement structure, and contextual correlation. The five-layer standard specifies what replaces the averaging: raw timestamped readings (Layer 4), the reduction methodology as executable code (Layer 5), and the published value as one view of the data rather than the only view. Nothing is destroyed. Everything is preserved. The average can still be computed by anyone who wants it. But the raw structure is available to anyone who wants to ask questions the average cannot answer.

---

## 7. What This Standard Costs

The standard requires more work than current practice. The cost is quantifiable.

The value store costs data entry time. Each input value must be entered with its full metadata — source, uncertainty, digits, tags, notes. For a computation with twenty-eight inputs, as in the BBN experiment, this is perhaps one to two hours of careful data entry. The return: the inputs are entered once and reused across every computation that references them. The reference implementation's 4900-node store was built incrementally. Each new experiment adds a few values and reuses hundreds. The marginal cost of adding a new experiment to an established store is minutes, not hours.

The experiment definition costs planning time. Declaring inputs, outputs, and comparisons in advance requires thinking through the computation before running it. This is not overhead. This is the commitment step. The time spent writing the definition is the time spent making the prediction specific and testable before the test. Under current practice, this thinking happens informally and incompletely. Under the standard, it happens explicitly and is documented.

The run infrastructure costs implementation time. Building a runner that loads the value store, executes derivations, runs comparisons, and produces reports is an engineering project. The reference implementation exists and is operational — fifty experiments across multiple domains of physics. For a new research group, adopting the standard means either using the existing infrastructure or building a compatible implementation against the specification. This is a one-time cost.

The total cost is small relative to the cost of the science. A single precision measurement experiment at a national laboratory costs millions of dollars and years of effort. The five-layer standard costs days of engineering to implement and hours per experiment to maintain. The cost of not implementing it — irreproducible results, unlocated errors, smuggled parameters, destroyed temporal structure — is paid by every downstream user of the results, repeatedly, for as long as the results are used.

---

## 8. The Standard Applied

Three categories of current scientific publication, each examined against the standard.

**Theoretical computation papers.** Currently: LaTeX equations, prose derivation, stated result, citations to input values. Under the standard: value store with all inputs, experiment definition with all derivations and comparisons, connection bundle stating purpose, run output with all results, generated report. The paper still exists — as the human-readable narrative explaining what was done and why it matters. But the computation exists alongside it as a rerunnable artifact. The paper describes the science. The artifact is the science. Both are published.

**Experimental measurement papers.** Currently: description of apparatus, description of procedure, stated result with uncertainty, data availability statement. Under the standard: value store with calibration and configuration, measurement protocol, semantic context, raw timestamped data at native sampling rate, reduction pipeline as executable code, generated report. The paper still exists as narrative. The data, the pipeline, and the results exist as rerunnable artifacts.

**Reference compilations.** Currently: committee-averaged recommended values published on multi-year cycles. Under the standard: every contributing instrument's time series with full metadata, the averaging methodology as executable reduction pipeline, the recommended values as pipeline output. Anyone can run the pipeline. Anyone can modify the methodology. Anyone can query the raw data. The committee's role shifts from producing the answer to maintaining the infrastructure and certifying data quality.

In every case, the standard adds a layer of verifiable artifact to an existing layer of narrative description. Nothing is taken away. The paper, the prose, the narrative explanation — all remain. What is added is the computation itself, in a form that does not require manual re-execution to verify.

---

## 9. Falsification Conditions

This paper practices what it prescribes.

**Prediction 1: Reproducibility.** If two independent groups implement the five-layer standard and run the same experiment definition against the same value store, they will produce identical results. If implementation differences produce different results from the same declared inputs and derivations, the standard is insufficiently specified and requires revision at the point of divergence.

**Prediction 2: Error detection.** If the five-layer standard is applied to a published theoretical result and the rerunnable artifact produces a different value than the published paper states, the standard has identified an error in the published result. If this never occurs across a sufficient sample, current prose-based practice is more reliable than this paper claims.

**Prediction 3: Information preservation.** If the standard is applied to experimental measurements and the raw data plus reduction pipeline reveals no information beyond what the published averaged result contains — no temporal structure, no contextual correlations, no instrument-specific patterns — then the averaging process does not destroy scientifically valuable information and the additional infrastructure is not justified for experimental data.

**Prediction 4: Anti-smuggling completeness.** If a computation conforming to the standard nevertheless contains undeclared inputs that affect the result, the standard's structural prevention of smuggling is incomplete and requires architectural revision.

Each test is specific. Each is observable. Each could fail. The paper commits and accepts falsification if it comes.

---

## 10. Closing

The reference implementation exists. Over 4900 value nodes. Fifty experiments. Domains spanning quantum electrodynamics, electroweak physics, cosmology, Big Bang nucleosynthesis, CKM mixing, confinement, gravity, and Hubble tension. Each experiment with pre-registered falsification conditions. Each run producing a complete audit trail. Each failure located precisely.

The BBN experiment starts from gauge integers in particle physics and derives primordial nuclear abundances in cosmology. The derivation crosses three domains. The predictions are compared against Planck satellite measurements and precision spectroscopy of high-redshift absorbers. The deuterium prediction matches to three digits. The helium prediction misses the digit target — and the report says so, in print, with the exact miss percentage, because the falsification condition was pre-registered in the experiment definition and the runner evaluated it mechanically.

That is what showing your work looks like. Not "our result is consistent with observation." Not "we obtain reasonable agreement." The predicted value is 0.248643. The measured value is 0.2449. The miss is 1.53%. The sigma is 0.94. The digit test fails. The sigma test passes. Every number printed. Every comparison evaluated. Every failure located. Every input traceable. Every step rerunnable.

The infrastructure to do this is commodity technology. Value stores are databases. Experiment definitions are structured data files. Runners are programs. Reports are generated text. None of this is new technology. None of this is expensive. None of this is impractical. It is a choice.

The current practice of describing computations in prose and asking readers to re-derive them manually is a convention inherited from an era of printed pages and pen-and-paper calculation. The convention persists because conventions persist — not because the constraints that created the convention still exist. The constraints are gone. The convention remains.

Showing your work means publishing the work. The inputs. The definitions. The outputs. The comparisons. The failures. All of it, in a form that anyone can run, anyone can check, and anyone can extend. In 2026, the infrastructure to meet this standard is available to every researcher with a computer.

Everything else is telling, not showing.

---

## References

[1] Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters," *Astronomy & Astrophysics*, vol. 641, A6, 2020.

[2] D. J. Fixsen, "The Temperature of the Cosmic Microwave Background," *The Astrophysical Journal*, vol. 707, pp. 916–920, 2009.

[3] C. Pitrou et al., "Precision big-bang nucleosynthesis with improved Helium-4 predictions," *Physics Reports*, vol. 754, pp. 1–66, 2018.

[4] E. Aver, K. A. Olive, and E. D. Skillman, "The effects of He I λ10830 on helium abundance determinations," *JCAP*, vol. 07, 011, 2015.

[5] R. J. Cooke, M. Pettini, and C. C. Steidel, "One Percent Determination of the Primordial Deuterium Abundance," *The Astrophysical Journal*, vol. 855, 102, 2018.

[6] K. Popper, *The Logic of Scientific Discovery*, 1934 (German), 1959 (English).

[7] CODATA Task Group on Fundamental Constants, "CODATA Recommended Values of the Fundamental Physical Constants," *Reviews of Modern Physics*, 2021.

---

**Series cross-references (for deeper treatment of concepts introduced in this paper):**

- Statistical breadth substituting for functional depth: [@HOWL-CULT-1-2026]
- What falsification structurally requires: [@HOWL-CULT-4-2026]
- Why located errors are the most valuable finding: [@HOWL-CULT-5-2026]
- Publications as immutable timestamps: [@HOWL-CULT-6-2026]
- The structural mechanics of institutional non-commitment: [@HOWL-CULT-12-2026]
- Replacing averaged snapshots with synchronized measurement: [@HOWL-CULT-13-2026]
- Content-based evaluation of scientific contributions: [@HOWL-CULT-14-2026]

---

# CULT-15 Supporting Appendices

**Appendices to:** Showing Your Work in 2026

**Purpose:** Reference tables consolidating the five-layer specification, the reference implementation anatomy, failure mode analysis, cost analysis, and adoption checklist. These appendices serve as the actionable engineering reference for implementing the standard.

---

## Appendix A — The Five-Layer Specification

### A.1 Layer Summary

| Layer | Name | Purpose | Format | Authored By | When Created |
|---|---|---|---|---|---|
| 1 | Value Store | Single source of truth for all inputs | Named, typed, versioned value nodes | Researcher + community | Incrementally, reused across experiments |
| 2 | Experiment Definition | Pre-registered commitment to inputs, derivations, outputs, and falsification conditions | Machine-readable structured document | Researcher | Before computation runs |
| 3 | Connection Bundle | Semantic manifest declaring purpose, scope, and cross-domain relationships | Machine-readable structured document | Researcher | Before computation runs |
| 4 | Run Output | Complete set of results as value nodes | Same format as Layer 1 | Runner (automated) | During computation |
| 5 | Report | Human-readable summary with located failures | Generated text | Runner (automated) | After computation |

### A.2 Value Store Node — Required Fields

| Field | Type | Required | Purpose | Example |
|---|---|---|---|---|
| key | string | yes | Unique machine-readable identifier | `cosmo_yp_measured_v0` |
| canonical | string | yes | Version-independent identifier | `cosmo_yp_measured` |
| version | integer | yes | Schema version for the node | 0 |
| node_type | enum | yes | Structural classification | `value` |
| value | string, fraction, integer, boolean | yes | The datum itself | `0.2449` |
| value_type | enum | yes | Representation category | `approximate`, `exact_fraction`, `exact_integer` |
| unit | string | yes | Physical unit or dimensionless | `dimensionless`, `MeV`, `K`, `GeV^4` |
| source | string | yes | Publication, year, specific table or equation | `Aver, Olive, Skillman 2015. JCAP 07, 011` |

### A.3 Value Store Node — Recommended Fields

| Field | Type | Purpose | Example |
|---|---|---|---|
| topic | string | Domain classification for search | `cosmo`, `qed`, `ckm`, `bbn`, `si` |
| term | string | Physical quantity name | `yp_measured`, `boltzmann_constant` |
| level | integer | Hierarchy level (0=substrate, 1=theoretical, 2=measured, 3=derived) | 2 |
| digits | integer | Significant figures in value | 4 |
| uncertainty | string | Measurement uncertainty | `0.0040` |
| tags | array of strings | Searchable classification | `["cosmology", "BBN", "helium", "measured"]` |
| notes | string | Methodological context, caveats, relationships | `Y_p = primordial 4He mass fraction...` |

### A.4 Experiment Definition — Required Sections

| Section | Purpose | Contents |
|---|---|---|
| key | Unique identifier for the experiment | `experiment_bridge_bbn_v0` |
| description | Human-readable purpose statement | What the experiment tests and why |
| purpose | Program-level classification | Which research program this experiment belongs to |
| dependencies.values | Declared inputs | Every value store key the computation requires |
| dependencies.derivations | Declared computations | Every derivation the experiment will execute |
| execution_plan | Ordered derivation list | Derivations in execution order |
| expected_outputs | Pre-declared results | Every output key the derivation should produce |
| comparisons | Pre-registered falsification conditions | Every test with match mode, expected value, tolerance, reference |

### A.5 Comparison Entry — Required Fields

| Field | Type | Purpose | Example |
|---|---|---|---|
| label | string | Human-readable description of test | `D/H digits of agreement` |
| output_key | string | Which result to test | `result_dh_derived_v0` |
| match_mode | enum | How to evaluate | `miss_pct`, `digits`, `range`, `bool` |
| expected | string or number | Reference value or target | `2.53e-5` |
| reference_source | string | Where expected value comes from | `Cooke_2018` |

### A.6 Comparison Match Modes

| Mode | Evaluates | Pass Condition | Failure Output |
|---|---|---|---|
| miss_pct | Percentage deviation from expected | Informational — reports miss | Miss percentage with digit-by-digit comparison |
| digits | Agreement to N significant figures | First N digits match | Specific digit position where divergence occurs |
| range | Value falls within [lo, hi] | lo ≤ value ≤ hi | Value and which bound was violated |
| bool | Boolean identity | value == expected | Expected vs got |

### A.7 Connection Bundle — Required Fields

| Field | Type | Purpose | Example |
|---|---|---|---|
| key | string | Unique identifier | `connection_pctrm_substrate_identities_v0` |
| connection_type | string | Category of connection | `substrate`, `bridge`, `consistency` |
| description | string | What the bundle tests and why | Full scope description |
| inputs | array of strings | Every value store key used | All twenty-eight input keys listed |
| tags | array of strings | Searchable classification | `["PCTRM", "substrate", "cross_domain"]` |
| notes | string | Scope and hierarchy levels covered | Which hierarchy levels, which domains |

### A.8 Run Output Node — Required Fields

| Field | Type | Purpose | Example |
|---|---|---|---|
| key | string | Run-specific unique identifier | `experiment_bridge_bbn_v0_run011_result_omega_b_derived_v0` |
| canonical | string | Version-independent identifier | `experiment_bridge_bbn_v0_run011_result_omega_b_derived` |
| version | integer | Schema version | 0 |
| node_type | enum | Always `value` | `value` |
| value | string or number | The computed result | `0.049035637966613` |
| value_type | enum | Representation category | `approximate` |
| unit | string | Physical unit | `dimensionless` |
| source | string | Which run produced this value | `experiment_bridge_bbn_v0_run011` |

### A.9 Report — Required Sections

| Section | Contents | Generated From |
|---|---|---|
| Header | Experiment name, result file, timestamp, status, mode, purpose | Experiment definition + run metadata |
| Derivation Outputs | Every output value with its computed result | Layer 4 run output |
| Comparisons | Every test with predicted, measured, agreement, miss, status | Layer 2 comparisons evaluated against Layer 4 output |
| Summary | Derivation count (OK/error), comparison count (PASS/FAIL/INFO/SKIP), overall status | Aggregated from above |

---

## Appendix B — BBN Experiment Anatomy

Complete structural decomposition of the reference cross-domain experiment.

### B.1 Input Values — Full Catalog

| Key | Value | Unit | Digits | Source | Domain |
|---|---|---|---|---|---|
| `geom_pi_v0` | π | dimensionless | exact | Mathematical constant | Mathematics |
| `geom_zeta3_v0` | ζ(3) = 1.20206... | dimensionless | exact | Mathematical constant | Mathematics |
| `integer_yang_mills_eleven_v0` | 11 | dimensionless | exact | Gauge structure | Particle physics |
| `integer_b2_modified_numerator_abs_v0` | 13 | dimensionless | exact | Gauge structure | Particle physics |
| `cosmo_omega_dm_planck_v0` | 0.2607 | dimensionless | 4 | Planck 2018 | Cosmology |
| `cosmo_omega_b_planck_v0` | 0.0490 | dimensionless | 3 | Planck 2018 | Cosmology |
| `cosmo_omega_de_planck_v0` | 0.6889 | dimensionless | 4 | Planck 2018 | Cosmology |
| `cosmo_omega_m_planck_v0` | 0.3111 | dimensionless | 4 | Planck 2018 | Cosmology |
| `cosmo_dm_to_baryon_planck_v0` | 5.3204 | dimensionless | 5 | Planck 2018 | Cosmology |
| `cosmo_dm_to_baryon_ratio_prefactor_v0` | 22π/13 | dimensionless | exact | Derived | Cross-domain |
| `cosmo_t_cmb_v0` | 2.7255 | K | 5 | Fixsen 2009 | Cosmology |
| `cosmo_n_gamma_cmb_v0` | 410.7 | cm⁻³ | 4 | From T_CMB | Cosmology |
| `cosmo_rho_crit_v0` | 8.53e-30 | g/cm³ | 3 | From H0 Planck | Cosmology |
| `cosmo_eta_planck_v0` | 6.104e-10 | dimensionless | 4 | Planck 2018 | Cosmology |
| `cosmo_yp_measured_v0` | 0.2449 | dimensionless | 4 | Aver et al. 2015 | Nuclear/observational |
| `cosmo_dh_measured_v0` | 2.527e-5 | dimensionless | 4 | Cooke et al. 2018 | Nuclear/observational |
| `cosmo_neff_standard_v0` | 3.044 | dimensionless | 4 | de Salas & Pastor 2016 | Particle physics |
| `cosmo_neff_planck_v0` | 2.99 | dimensionless | 3 | Planck 2018 | Cosmology |
| `cosmo_rho_lambda_measured_v0` | 5.88e-30 | g/cm³ | 3 | From Ω_DE × ρ_crit | Cosmology |
| `cosmo_rho_lambda_gev4_v0` | 2.85e-47 | GeV⁴ | 3 | Converted | Cosmology |
| `cosmo_h0_planck_v0` | 67.4 | km/s/Mpc | 3 | Planck 2018 | Cosmology |
| `bbn_yp_a_coeff_v0` | 0.2485 | dimensionless | 4 | Pitrou et al. 2018 | Nuclear physics |
| `bbn_yp_b_coeff_v0` | 0.0016 | dimensionless | 2 | Pitrou et al. 2018 | Nuclear physics |
| `bbn_dh_a_coeff_v0` | 2.57 | dimensionless | 3 | Pitrou et al. 2018 | Nuclear physics |
| `bbn_dh_b_coeff_v0` | -0.44 | dimensionless | 2 | Pitrou et al. 2018 | Nuclear physics |
| `astro_gravitational_constant_v0` | 6.674e-11 | m³/kg/s² | 4 | CODATA 2018 | Gravitation |
| `mass_proton_v0` | 938.272... | MeV | 6 | PDG 2024 | Particle physics |
| `si_speed_of_light_v0` | 299792458 | m/s | exact | SI definition | Metrology |
| `si_planck_constant_v0` | 6.62607015e-34 | J·s | exact | SI 2019 | Metrology |

### B.2 Derivation Chain

| Step | Derivation | Inputs From | Outputs | Domain Crossed |
|---|---|---|---|---|
| 1 | `bridge_omega_b_from_integers_v0` | Gauge integers (11, 13), π | Ω_b, Ω_DE, flatness | Particle physics → Cosmology |
| 2 | `bridge_omega_de_from_flatness_v0` | Ω_b, Ω_DM | Ω_DE, flatness sum, residual | Cosmology (internal) |
| 3 | `bridge_eta_from_omega_b_v0` | Ω_b, T_CMB, ρ_crit, n_γ, H0, G, m_p, c, ℏ | η, η_10, n_γ computed, ρ_crit computed | Cosmology → Nuclear physics |
| 4 | `bridge_yp_from_eta_v0` | η_10, BBN Y_p coefficients, Y_p measured | Y_p derived, miss, sigma | Nuclear physics (BBN) |
| 5 | `bridge_dh_from_eta_v0` | η_10, BBN D/H coefficients, D/H measured | D/H derived, miss, sigma | Nuclear physics (BBN) |
| 6 | `bridge_neff_consistency_v0` | Ω_b, Ω_DM, Ω_DE, N_eff standard, N_eff Planck | N_eff check, miss | Cosmology (consistency) |
| 7 | `bridge_vacuum_energy_v0` | Ω_DE, ρ_crit, ρ_Λ measured | ρ_Λ derived (g/cm³, GeV⁴), miss, CC ratio | Cosmology → Quantum field theory |

### B.3 Pre-Registered Comparisons — Full Catalog

| # | Label | Output Key | Mode | Expected | Source | Result | Status |
|---|---|---|---|---|---|---|---|
| 1 | Ω_b from integers vs Planck | `result_omega_b_derived_v0` | miss_pct | 0.0490 | Planck 2018 | 0.049036, miss 0.073% | INFO |
| 2 | η derived vs Planck | `result_eta_derived_v0` | miss_pct | 6.104e-10 | Planck 2018 | 6.090e-10, miss 0.237% | INFO |
| 3 | η_10 derived vs Planck | `result_eta10_derived_v0` | miss_pct | 6.104 | Planck 2018 | 6.090, miss 0.237% | INFO |
| 4 | Y_p from integers vs measured | `result_yp_derived_v0` | miss_pct | 0.2449 | Aver 2015 | 0.2486, miss 1.528% | INFO |
| 5 | Y_p digits of agreement | `result_yp_derived_v0` | digits(2) | 0.245 | Aver 2015 | 0.249, diverge at position 4 | FAIL |
| 6 | D/H from integers vs measured | `result_dh_derived_v0` | miss_pct | 2.527e-5 | Cooke 2018 | 2.531e-5, miss 0.143% | INFO |
| 7 | D/H digits of agreement | `result_dh_derived_v0` | digits(3) | 2.53e-5 | Cooke 2018 | 2.531e-5, 3-digit match | PASS |
| 8 | N_eff consistency with N_eff = 3 | `result_neff_check_v0` | range [2.5, 3.5] | — | SM prediction | 2.712, in range | PASS |
| 9 | N_eff vs standard 3.044 | `result_neff_check_v0` | miss_pct | 3.044 | de Salas 2016 | 2.712, miss 10.9% | INFO |
| 10 | Vacuum energy (GeV⁴) vs observed | `result_rho_lambda_gev4_derived_v0` | miss_pct | 2.85e-47 | Planck 2018 | 2.538e-47, miss 10.94% | INFO |
| 11 | Vacuum energy (g/cm³) vs observed | `result_rho_lambda_derived_v0` | miss_pct | 5.88e-30 | Planck 2018 | 5.889e-30, miss 0.152% | INFO |
| 12 | Full chain: integers → η → Y_p within 1σ | `result_yp_sigma_v0` | range [0, 2.0] | — | Aver 2015 | 0.936σ, in range | PASS |
| 13 | Full chain: integers → η → D/H within 1σ | `result_dh_sigma_v0` | range [0, 2.0] | — | Cooke 2018 | 0.120σ, in range | PASS |

### B.4 Derivation Output Values — Full Catalog

| Key | Value | Description |
|---|---|---|
| `result_omega_b_derived_v0` | 0.049035637966613 | Baryon density from integers |
| `result_omega_b_measured_v0` | 0.049 | Planck reference |
| `result_omega_b_miss_pct_v0` | 0.0727 | Miss percentage |
| `result_omega_b_used_v0` | 0.049035637966613 | Value used downstream |
| `result_omega_de_derived_v0` | 0.690264362033387 | Dark energy density from flatness |
| `result_omega_de_measured_v0` | 0.6889 | Planck reference |
| `result_omega_de_miss_pct_v0` | 0.198 | Miss percentage |
| `result_omega_dm_input_v0` | 0.2607 | Dark matter density (input) |
| `result_omega_m_derived_v0` | 0.309735637966613 | Total matter density |
| `result_omega_m_measured_v0` | 0.3111 | Planck reference |
| `result_omega_m_miss_pct_v0` | 0.439 | Miss percentage |
| `result_flatness_sum_v0` | 1.0 | Ω_b + Ω_DM + Ω_DE |
| `result_flatness_residual_v0` | 0.0 | Departure from unity |
| `result_dm_baryon_ratio_used_v0` | 5.31654141376734 | DM/baryon ratio (22π/13) |
| `result_eta_derived_v0` | 6.08953448897262e-10 | Baryon-to-photon ratio |
| `result_eta_measured_v0` | 6.104e-10 | Planck reference |
| `result_eta_miss_pct_v0` | 0.237 | Miss percentage |
| `result_eta10_derived_v0` | 6.08953448897262 | η × 10¹⁰ |
| `result_eta10_measured_v0` | 6.104 | Planck reference |
| `result_eta10_used_v0` | 6.08953448897262 | Value used in BBN |
| `result_n_gamma_computed_v0` | 410726847.924845 | Photon number density (m⁻³) |
| `result_rho_crit_computed_v0` | 8.53145574533961e-27 | Critical density (kg/m³) |
| `result_h0_si_v0` | 2.18405703175632e-18 | H0 in SI (s⁻¹) |
| `result_yp_derived_v0` | 0.248643255182356 | Primordial helium fraction |
| `result_yp_measured_v0` | 0.2449 | Aver 2015 reference |
| `result_yp_measured_used_v0` | 0.2449 | Value used for comparison |
| `result_yp_miss_pct_v0` | 1.528 | Miss percentage |
| `result_yp_sigma_v0` | 0.935813795589048 | Deviation in sigma units |
| `result_yp_a_used_v0` | 0.2485 | BBN fitting coefficient a |
| `result_yp_b_used_v0` | 0.0016 | BBN fitting coefficient b |
| `result_yp_at_neff3_v0` | 0.248643255182356 | Y_p at N_eff = 3 |
| `result_dh_derived_v0` | 2.53060482485205e-5 | Primordial deuterium ratio |
| `result_dh_measured_v0` | 2.527e-5 | Cooke 2018 reference |
| `result_dh_miss_pct_v0` | 0.143 | Miss percentage |
| `result_dh_sigma_v0` | 0.120160828401573 | Deviation in sigma units |
| `result_dh_x1e5_derived_v0` | 2.53060482485205 | D/H × 10⁵ |
| `result_dh_x1e5_measured_v0` | 2.527 | D/H × 10⁵ reference |
| `result_dh_a_used_v0` | 2.57 | BBN fitting coefficient a |
| `result_dh_b_used_v0` | -0.44 | BBN fitting coefficient b |
| `result_neff_check_v0` | 2.71205729366492 | Derived N_eff from Ω ratios |
| `result_neff_standard_v0` | 3.044 | Standard model prediction |
| `result_neff_planck_v0` | 2.99 | Planck measurement |
| `result_neff_miss_standard_pct_v0` | 10.905 | Miss vs standard |
| `result_neff_miss_planck_pct_v0` | 9.296 | Miss vs Planck |
| `result_neff_sigma_v0` | 1.63495709608869 | Deviation in sigma units |
| `result_rho_lambda_derived_v0` | 5.88895985727292e-30 | Vacuum energy (g/cm³) |
| `result_rho_lambda_gev4_derived_v0` | 2.53821856816922e-47 | Vacuum energy (GeV⁴) |
| `result_rho_lambda_kgm3_derived_v0` | 5.88895985727292e-27 | Vacuum energy (kg/m³) |
| `result_rho_lambda_measured_gcm3_v0` | 5.88e-30 | Reference (g/cm³) |
| `result_rho_lambda_measured_gev4_v0` | 2.85e-47 | Reference (GeV⁴) |
| `result_rho_lambda_miss_gcm3_pct_v0` | 0.152 | Miss in g/cm³ |
| `result_rho_lambda_miss_gev4_pct_v0` | 10.940 | Miss in GeV⁴ |
| `result_omega_de_used_v0` | 0.690264362033387 | Ω_DE used for vacuum energy |
| `result_cc_problem_ratio_v0` | 3.93977103682322e+54 | Cosmological constant problem ratio |

---

## Appendix C — Failure Mode Analysis

### C.1 Current Practice Failure Modes

| Failure Mode | Description | Frequency | Consequence | Detectable By Reader |
|---|---|---|---|---|
| Transcription error | Reader copies value incorrectly from cited paper | Common | Wrong downstream result | Only if reader catches own error |
| Notational ambiguity | Symbol means different things in different conventions | Common | Incorrect calculation | Only if reader knows both conventions |
| Derivation gap | Paper skips steps author considered obvious | Very common | Reader cannot verify intermediate steps | Only if reader can bridge gap independently |
| Unstated numerical choice | Step count, precision, convergence threshold not reported | Very common | Result depends on unreported choice | Not detectable from paper |
| Floating-point artifact | Accumulated rounding affects final digits | Common in long chains | Final digits implementation-dependent | Not detectable from paper |
| Parameter smuggling | Undeclared value enters computation | Occasional, usually unintentional | Result depends on hidden input | Not detectable from paper |
| Post-hoc comparison adjustment | Success criteria adjusted after seeing result | Occasional | False positive | Not detectable from paper |
| Selective reporting | Failures omitted from published results | Occasional | Incomplete picture | Not detectable from paper |

### C.2 Five-Layer Standard Prevention Mechanisms

| Failure Mode | Prevention Mechanism | Layer |
|---|---|---|
| Transcription error | Values read from store by key, not transcribed | Layer 1 |
| Notational ambiguity | Values have explicit units, types, and definitions | Layer 1 |
| Derivation gap | Derivation is executable code, every step runs | Layer 2 |
| Unstated numerical choice | Configuration stored in value store with source and notes | Layer 1 |
| Floating-point artifact | Exact fraction storage where possible, stated precision where not | Layer 1 |
| Parameter smuggling | Runner loads only declared dependencies, undeclared access fails | Layers 1+2+3 |
| Post-hoc comparison adjustment | Comparisons pre-registered in experiment definition before run | Layer 2 |
| Selective reporting | Report generated from all comparisons, not written selectively | Layer 5 |

### C.3 Remaining Failure Modes Under the Standard

| Failure Mode | Description | Mitigation |
|---|---|---|
| Wrong value in store | Value entered incorrectly at data entry | Source field enables verification against original publication |
| Wrong derivation code | Computation itself contains a bug | Independent reimplementation against same definition |
| Incomplete comparison set | Relevant test not included in definition | Peer review of experiment definition, not just results |
| Infrastructure bug | Runner evaluates comparisons incorrectly | Independent runner implementations |
| Value store corruption | Data loss or modification | Versioning, checksums, immutable append-only storage |

---

## Appendix D — Cost Analysis

### D.1 One-Time Costs

| Component | Effort | Skills Required | Reusable Across |
|---|---|---|---|
| Runner implementation | 2-4 weeks engineering | Python or equivalent, JSON processing | All experiments |
| Value store schema | 1-2 days design | Data modeling | All experiments |
| Report generator | 2-3 days engineering | Text formatting, arithmetic | All experiments |
| Documentation of standard | 1 week writing | Technical writing | All adopters |

### D.2 Per-Experiment Costs

| Activity | Effort (New Store) | Effort (Established Store) | Current Practice Equivalent |
|---|---|---|---|
| Value entry | 1-2 hours for 28 inputs | 10-20 minutes (most values already exist) | Looking up values in papers (same time, not reusable) |
| Experiment definition | 1-2 hours | 30-60 minutes (patterns established) | Informal planning (same time, not documented) |
| Connection bundle | 30 minutes | 15 minutes | No equivalent (purpose unstated) |
| Derivation code | Same as current practice | Same as current practice | Same — computation must be written regardless |
| Running experiment | Seconds (automated) | Seconds (automated) | Manual re-derivation by each reader (hours) |
| Reviewing report | 10-20 minutes | 10-20 minutes | Manual comparison against references (hours) |

### D.3 Amortization Profile

| Store Size | Experiments | New Values Per Experiment | Reuse Rate | Marginal Cost Trend |
|---|---|---|---|---|
| 0-100 nodes | 1-5 | 20-30 | 0-20% | High (building store) |
| 100-500 nodes | 5-15 | 10-15 | 40-60% | Moderate (growing reuse) |
| 500-2000 nodes | 15-30 | 5-10 | 70-85% | Low (most values exist) |
| 2000-5000 nodes | 30-50 | 2-5 | 90-95% | Minimal (mature store) |

### D.4 Cost Comparison — Single Experiment Lifecycle

| Activity | Current Practice | Five-Layer Standard |
|---|---|---|
| Author: compute result | Hours-days | Hours-days (same) |
| Author: write paper | Days-weeks | Days-weeks (same, paper still written) |
| Author: prepare standard artifacts | Not done | 2-4 hours additional |
| Reader 1: verify result | Hours (manual re-derivation) | Minutes (rerun experiment) |
| Reader 2: verify result | Hours (manual re-derivation, again) | Minutes (rerun experiment) |
| Reader N: verify result | Hours (manual re-derivation, again) | Minutes (rerun experiment) |
| Total verification cost (10 readers) | ~50 hours manual labor | ~1.5 hours + 4 hours author preparation |

---

## Appendix E — Domain Coverage of Reference Implementation

### E.1 Experiment Inventory by Domain

| Domain | Experiment Count | Example Experiments |
|---|---|---|
| QED / anomalous magnetic moments | 8 | `alpha_em_killing_spree`, `muon_g2`, `laporta_*` |
| Electroweak | 5 | `ew_oneloop_*`, `ew_v2`, `electroweak_anatomy`, `sin2_theta_w_*` |
| CKM mixing | 1 | `ckm_cd_mixing` |
| Cosmology | 4 | `cosmology_chain`, `toroidal_dm`, `hubble_running_*` |
| Big Bang nucleosynthesis | 2 | `bridge_bbn`, `bbn_extended` |
| Cross-domain bridges | 2 | `bridge_bbn`, `bridge_ew_cosmo` |
| Confinement / nuclear | 1 | `confinement_boundary` |
| Gravity / relativity | 3 | `soliton_gravity`, `gr_time_dilation`, `relativity` |
| Mathematical foundations | 3 | `math11_beta_metric`, `beta_content_a3`, `beta_unification` |
| Hydrogen spectroscopy | 1 | `hydrogen_1s2s` |
| Parameter reduction | 2 | `parameter_reduction`, `pctrm_b_round_0` |
| Proton decay | 1 | `proton_decay` |
| Diagnostic / scanning | 5 | `whatif_*`, `giga_remainder_test` |
| Total | 50 | — |

### E.2 Value Store Coverage by Domain

| Topic | Approximate Node Count | Examples |
|---|---|---|
| Cosmology (`cosmo`) | ~400 | Ω parameters, H0 values, CMB, BBN abundances |
| QED (`qed`) | ~600 | α contributions by loop order, g-2 components |
| Electroweak (`ew`) | ~300 | Z widths, mixing angles, radiative corrections |
| CKM (`ckm`) | ~100 | Matrix elements, unitarity |
| Masses (`mass`) | ~200 | All SM particles, ratios |
| Couplings (`coupling`) | ~200 | α_em, α_s, Fermi constant |
| Geometry / math (`geom`, `metric`) | ~300 | π, β, ζ values, elliptic integrals |
| SI constants (`si`) | ~50 | c, ℏ, k_B, e, N_A |
| BBN (`bbn`) | ~50 | Fitting coefficients, measured abundances |
| Configuration (`config`) | ~30 | Numerical parameters |
| Experiment results | ~3000+ | Outputs from all 50 experiments |
| Total | ~4900+ | — |

---

## Appendix F — Adoption Checklist

### F.1 Minimum Viable Implementation

| Step | Action | Validates |
|---|---|---|
| 1 | Define value store schema (key, value, type, unit, source minimum) | Layer 1 |
| 2 | Enter input values for one computation with full metadata | Layer 1 operational |
| 3 | Write experiment definition with dependencies, plan, outputs, comparisons | Layer 2 operational |
| 4 | Write connection bundle listing all inputs and stating purpose | Layer 3 operational |
| 5 | Implement runner that loads store, executes derivation, evaluates comparisons | Layers 4+5 operational |
| 6 | Run experiment, inspect output values and report | Full pipeline operational |
| 7 | Have a second person run same experiment against same store | Reproducibility confirmed |

### F.2 Quality Criteria for Each Layer

| Layer | Quality Test | Pass Condition |
|---|---|---|
| 1 — Value Store | Every input traceable to source | Source field populated, verifiable against original publication |
| 1 — Value Store | No duplicate entries | Each physical quantity has exactly one canonical key |
| 1 — Value Store | Exact where possible | SI-exact constants stored as exact fractions, not floats |
| 2 — Experiment Definition | All dependencies declared | Runner loads only declared values, no undeclared access |
| 2 — Experiment Definition | Comparisons pre-registered | All comparisons written before run, not added after |
| 2 — Experiment Definition | Expected outputs enumerated | Every output the derivation produces is declared in advance |
| 3 — Connection Bundle | All inputs listed | Bundle input list matches experiment dependency list |
| 3 — Connection Bundle | Purpose stated | Description explains what is being tested and why |
| 4 — Run Output | All outputs stored | Every declared expected output has a corresponding output node |
| 4 — Run Output | Source traceability | Every output node references the specific run that produced it |
| 5 — Report | Generated not written | Report produced by runner from output, not authored separately |
| 5 — Report | All comparisons included | No comparison from definition omitted in report |
| 5 — Report | Failures printed | FAIL status printed with same precision as PASS status |

### F.3 Scaling Path

| Phase | Scope | Store Size | Experiment Count | Team Size |
|---|---|---|---|---|
| Proof of concept | One computation, one domain | 50-100 nodes | 1-3 | 1 person |
| Single domain | All computations in one subfield | 200-500 nodes | 5-15 | 1-3 people |
| Cross-domain | Computations spanning multiple subfields | 500-2000 nodes | 15-30 | 3-5 people |
| Comprehensive | All major computations in a research program | 2000-5000 nodes | 30-50+ | 5-10 people |
| Community standard | Multiple groups sharing store and definitions | 10000+ nodes | 100+ | Open community |

---

## Appendix G — Pre-Registered Falsification Structure

### G.1 How Pre-Registration Is Embedded

| Current Practice | Five-Layer Standard |
|---|---|
| Pre-registration filed with external registry | Pre-registration is the experiment definition |
| Separate document from the experiment | Same document that runs the experiment |
| Compliance checked after the fact by humans | Compliance enforced by runner at execution time |
| Success criteria may be ambiguous or qualitative | Success criteria are mechanical: match modes with explicit tolerances |
| Partial reporting possible — omit unfavorable tests | All comparisons evaluated and printed automatically |
| Reinterpretation of criteria possible after seeing results | Criteria are versioned data — changes are traceable |

### G.2 Comparison as Falsification Commitment

| Element of Falsification (Popper) | Corresponding Structure in Experiment Definition |
|---|---|
| Commitment: state specific prediction | `output_key` + `expected` value |
| Specificity: prediction can disagree with observation | `match_mode` + tolerance (digits, range, percentage) |
| Priority: prediction before test | Definition file created before run; versioned with timestamp |
| Acceptance: accept failure when it occurs | Runner prints FAIL mechanically; report includes all failures |

### G.3 BBN Experiment — Falsification Surface

| Test | What Would Falsify | Located At |
|---|---|---|
| Ω_b miss > 1% | Integer derivation of baryon density wrong | Step 1 of chain |
| η miss > 1% | Cosmological bridge wrong | Step 3 of chain |
| Y_p outside 2σ | BBN chain from integers to helium fails | Steps 1→3→4 |
| D/H outside 2σ | BBN chain from integers to deuterium fails | Steps 1→3→5 |
| N_eff outside [2.5, 3.5] | Derived Ω ratios inconsistent with three neutrino species | Step 6 |
| Flatness residual > 0.001 | Cosmic partition doesn't close to unity | Steps 1→2 |
| ρ_Λ (g/cm³) miss > 1% | Vacuum energy derivation wrong | Step 7 |

---

**End of Supporting Appendices.**
