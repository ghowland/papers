
# Video 6 Script: I Built a Test Suite for Physics and Everything Passed — 253 Comparisons

## Delivery Notes

This is your home turf. You're a software engineer explaining testing to a mixed audience. The emotional peak is the FAIL section — trust is built from the one failure that stays visible, not from the 252 passes. The terminal demos are the centerpiece: the audience watches real experiments produce real results with real failures left in.

---

## SECTION 1: Opening — The SWE Instinct (1 minute)

*[In frame, talking to camera. No slides.]*

### TECHNICAL VERSION

I'm a software engineer. When I build a system, I write tests. Not after the fact, not as validation for something I already believe — as part of the development process. The test defines the contract: this function, given these inputs, must produce this output within this tolerance. If it doesn't, the build fails.

Physics doesn't work this way. Physics publishes derivations and compares them to measurements in the text of papers. The comparison is qualitative — "in good agreement with experiment" — or quantitative but manual. There is no automated, reproducible, binary pass/fail testing of numerical predictions against published measurements.

I built one. 36 experiments. 253 comparisons. Automated. Reproducible. Binary. This video shows you the system and what it found.

### NON-TECHNICAL VERSION

I'm a software engineer. When I build something, I test it. That's not optional — it's how the job works. You write down what the answer should be before you compute it. You run the code. You check: did the answer match? Yes means PASS. No means FAIL. The computer decides, not a person.

Physics doesn't do this. Physicists derive predictions and compare them to measurements in papers. The comparison is usually a sentence — "our result is in good agreement with the data." That's a judgment call, not a test.

I built a test suite for physics. 36 experiments. 253 comparisons. The computer checks every number automatically and reports PASS or FAIL. Nobody told me to do this — physics doesn't work this way. But software does. And when I applied software testing to physics, something remarkable happened: almost everything passed.

### MERGE NOTES

This is your opening and it comes from your professional identity. "When I build something, I test it" is a sentence you've lived for 30 years. The contrast with physics — "in good agreement" vs binary PASS/FAIL — is an observation only an outsider would make. Deliver it as someone bringing engineering discipline to a field that lacks it.

---

## SECTION 2: What a Test Suite Is (2 minutes)

**SLIDE: talk6_01_test_cycle.png** — Show during three-step explanation

**SLIDE: talk6_02_test_vs_peer_review.png** — Show during comparison

*[Terminal demo: run one simple experiment]*

### TECHNICAL VERSION

A test suite is a collection of automated assertions. Each assertion specifies:
1. A computation to execute (the derivation function with its inputs)
2. An expected output (the measured or theoretically known value)
3. A comparison criterion (match mode: exact, miss_pct, digits, range, bool)
4. A pass/fail threshold (tolerance or exact equality)

The assertions are defined before execution. The computation runs without knowledge of the expected values. The comparison is performed programmatically. The result is binary: PASS (assertion satisfied) or FAIL (assertion violated).

Key properties: deterministic (same inputs always produce same outputs), reproducible (anyone with the code and data can run it), automated (no human judgment in the comparison step), comprehensive (every derived quantity is compared, not a cherry-picked subset).

The test suite does not validate theory. It checks numerical agreement between computed predictions and published measurements. A PASS means the number matches. It does not mean the theory is correct. A FAIL means the number doesn't match. It means something needs investigation.

### NON-TECHNICAL VERSION

For non-programmers: a test suite is a checklist that runs itself.

Step one: write down what the answer should be. Before you do any computation, you write: "alpha inverse should be 137.036 to 12 digits." "The weak mixing angle should be 0.23122." "Deuterium abundance should be 2.527 times 10 to the negative 5."

Step two: run the computation. The computer does the math. It doesn't know what you wrote in step one. It just computes.

Step three: compare. Did the computed answer match the expected answer? If yes: PASS. If no: FAIL. The computer decides. Not a committee. Not a peer reviewer. Not a person with opinions. A comparison operation.

The test doesn't care who wrote the code. It doesn't care what department you're in. It doesn't care whether the author has a PhD or a GED. It cares about one thing: does the number match?

*[Terminal]*

Let me show you. Here's one experiment running. Watch the output...

[PASS] [PASS] [PASS] [INFO] [PASS]

Five comparisons. Four passed. One is informational — it's reporting the miss without gating. The computer decided all of this in about two seconds.

### MERGE NOTES

You've written test suites your entire career. Explain it the way you'd explain testing to a new hire. The three-step process (write, run, compare) is so natural to you that you might rush it — don't. The non-technical audience needs to understand the concept before you show them the results. The terminal demo at the end of this section is just a taste — the big demos come later.

---

## SECTION 3: The Experiment System (3 minutes)

**SLIDE: talk6_03_experiment_json.png** — Show during JSON anatomy

**SLIDE: talk6_04_five_match_modes.png** — Show during match mode explanation

*[Terminal demo: list experiments, open one JSON, run one experiment with commentary]*

### TECHNICAL VERSION

Each experiment is a JSON specification with the following structure:

```
{
  "key": "experiment_bridge_bbn_v0",
  "description": "Big Bang nucleosynthesis from gauge integers",
  "derivations": ["derive_dm_baryon_ratio_v0", "derive_omega_b_v0", ...],
  "comparisons": [
    {"output": "result_dh_predicted_v0", "mode": "sigma", "expected": 2.527e-5, ...},
    ...
  ]
}
```

The runner is generic — it has no physics knowledge. It loads derivation functions by name, executes them in order, merges results into the pool, and evaluates comparisons. The physics is in the derivation functions and the value pool. The testing infrastructure is domain-agnostic.

Five match modes:
- **exact**: Fraction equality. For group theory outputs.
- **miss_pct**: |computed − expected|/expected × 10⁶ in ppm. Reports the miss.
- **digits**: counts matching significant figures.
- **range**: value falls within [lo, hi]. For order-of-magnitude sanity checks.
- **bool**: True/False structural checks.

The experiment is a contract: these inputs, these computations, these outputs, these checks. Everything declared before anything runs.

### NON-TECHNICAL VERSION

The system has 36 experiments. Let me show you what one looks like.

*[Terminal]*

Here's the list — 36 experiments, from QED alpha extraction to GR time dilation. Each one is a file that says: here are the inputs I need, here are the computations to run, here are the outputs I expect, and here are the checks.

Let me open one. This is the BBN experiment — Big Bang nucleosynthesis. It has a list of derivation functions to run in order. Then a list of comparisons — each one specifying what to check, how to check it, and what the expected value is.

The checking comes in five flavors:

"Exact" — the computed fraction must equal the expected fraction exactly. This is for things from group theory that are known perfectly.

"Miss percent" — how far off is the prediction from the measurement, in parts per million? This is for precision comparisons.

"Digits" — how many significant figures match? This is for things like alpha where we care about digit-by-digit agreement.

"Range" — is the value between these bounds? This is for sanity checks.

"Bool" — is this true or false? This is for structural checks, like "does the proton survive this decay mode."

The experiment file is a contract. It says what will happen before anything runs. No surprises. No post-hoc adjustments. The criteria are set in advance.

### MERGE NOTES

You designed this system. Walk through it as its architect. The JSON structure is familiar to any developer in the audience and demystifying to the non-developers. The five match modes are a design decision you made — explain why each exists with a concrete example. The "contract" framing is natural for you.

---

## SECTION 4: The Value Pool (3 minutes)

**SLIDE: talk6_05_value_pool.png** — Show during scale discussion

**SLIDE: talk6_06_value_node_anatomy.png** — Show during field walkthrough

*[Terminal demo: search pool, info on specific values]*

### TECHNICAL VERSION

The value pool contains 2,700+ nodes organized by namespace (coupling_, mass_, beta_, qed_, cosmo_, gr_, result_, etc.). Each node is a typed, sourced, versioned record with the following fields:

- **key**: unique identifier with version suffix (e.g., `coupling_alpha_em_inverse_v0`)
- **value**: stored as Fraction string (e.g., "137035999177/1000000000") or decimal string
- **value_type**: `exact_fraction` or `approximate`
- **unit**: physical units (e.g., "MeV", "dimensionless")
- **source**: provenance reference (e.g., "CODATA 2018", "PDG 2024", "group theory")
- **digits**: number of significant figures
- **tags**: searchable labels (e.g., ["alpha", "em", "measured"])
- **level**: classification (0=math, 1=group theory, 2=measured, 3=derived)
- **notes**: free-text description of physical meaning and context

The pool serves as both input database and output repository. Experiments read inputs from the pool and write results back. The provenance chain is traceable: any result can be traced through its derivation function to its input values to their original sources.

### NON-TECHNICAL VERSION

Everything lives in the value pool. 2,700 values. Every constant, every measurement, every intermediate result, every final prediction.

*[Terminal]*

Let me search for something. "Alpha" — here are all the values related to alpha. The fine structure constant, its inverse, the QED coefficients that depend on it.

Let me look at one in detail. Here's alpha inverse. The key: coupling_alpha_em_inverse_v0. The value: 137,035,999,177 over 1,000,000,000 — that's a fraction, not a decimal. The type: exact_fraction. The source: CODATA 2018. Digits: 12. Tags: alpha, em, measured. Level: 2, meaning it's a measured value.

Every field tells you something. The key identifies it uniquely. The value stores the number. The type tells you whether it's exact or approximate. The source tells you where it came from. The digits tell you how many are meaningful. The tags let you search for it. The level tells you whether it's pure math, group theory, measurement, or derived.

Nothing is anonymous. Nothing is untyped. Nothing is unsourced. If you pick any value in this pool, you can trace it back to its origin — a measurement, a paper, a theorem.

*[Terminal]*

Here's a more interesting one: the hadronic vacuum polarization delta. Value: 220,393 over 50,000. Type: exact_fraction. But look — there's also an uncertainty field: plus or minus 0.010. And the notes say: "this value is at the confinement wall, limited by non-perturbative QCD." The system is telling you its own limitations.

### MERGE NOTES

You built this database. Walk through it as a database architect. The search and info commands are your tools. The "system telling you its own limitations" moment with the hadronic VP delta is a great detail — the system's notes field explicitly flags where it's weakest. Show this to the audience.

---

## SECTION 5: Live Demonstration — Five Experiments (5 minutes)

**SLIDE: talk6_07_five_experiments.png** — Show after all five have run

**SLIDE: talk6_08_terminal_output.png** — Show during terminal output explanation

*[Terminal demo: run five experiments back to back — this is the centerpiece]*

### TECHNICAL VERSION

Five experiments demonstrating the breadth of the test suite:

1. **experiment_qed_alpha_extraction_v0**: Newton inversion of the 5-loop QED series. Residual 10⁻²⁰⁴. α⁻¹ = 137.035999207. 15-digit series recovery. 12-digit CODATA match. All PASS.

2. **experiment_electroweak_anatomy_v0**: Pure gauge structure. Gap = 2 (exact Fraction match). Yang-Mills coefficient = −11/3 (exact). Gauge hierarchy verified. All PASS.

3. **experiment_bridge_bbn_v0**: Full cosmological chain. DM/baryon at 725 ppm. D/H at 0.12σ. He-4 at 0.94σ. Flatness sum = 1.0000 (exact). 11 PASS, 2 INFO.

4. **experiment_proton_decay_v0**: M_GUT = 10¹⁵·⁵ GeV. Proton lifetime > Super-K bound. Both PASS.

5. **experiment_gr_time_dilation_v0**: 18 comparisons across 60 orders of magnitude. Mercury at 2.8 ppm. GPS at 0.35%. Shapiro delay γ = 1 exact. GPA at 2.47%: FAIL.

Total: 42 comparisons. 41 PASS. 1 FAIL. The FAIL is right there in the output.

### NON-TECHNICAL VERSION

Now let me just run them. Five experiments, back to back. Watch the results.

*[Terminal]*

**Experiment one: QED alpha extraction.**

This is the precision showcase from Video 1. The Newton inversion converges... residual 10 to the negative 204... alpha inverse: 137.035999207... 15 digits recovered from the series... PASS. PASS. PASS. Everything matches.

**Experiment two: electroweak anatomy.**

This checks the structural properties of force unification. The pure gauge gap — the ratio that should be exactly 2 — is it exactly 2? Let's see... PASS. Exact Fraction match. The Yang-Mills coefficient — should be exactly negative 11/3 — PASS. Exact.

**Experiment three: the BBN bridge.**

The full cosmological chain. This is the big one — from gauge integers to deuterium. Dark matter ratio... baryon density... baryon-to-photon ratio... deuterium... helium...

D/H: PASS, 0.12 sigma. He-4: PASS, 0.94 sigma. Flatness residual: exactly 1.0. INFO on lithium — factor of 3, the known lithium problem. 11 PASS, 2 INFO. Nothing fails.

**Experiment four: proton decay.**

The GUT scale mass — is it high enough that protons don't decay too fast? M_GUT at 10 to the 15.5... survives the Super-Kamiokande bound... PASS. PASS.

**Experiment five: GR time dilation.**

18 comparisons spanning from a 22-meter tower to cosmological distances. Mercury perihelion: 2.8 parts per million. PASS. Solar redshift: 16 ppm. PASS. GPS: 0.35 percent. PASS. Shapiro delay: gamma equals 1, exact. PASS.

And... Gravity Probe A: 2.47 percent. FAIL.

There it is. In red. In the same output as everything else. Same font size. Not hidden. Not in a footnote. Right there.

42 comparisons. 41 passed. 1 failed.

### MERGE NOTES

This is the emotional centerpiece of the video. Run the experiments live. Let the output scroll. Point at each result as it appears. The audience should feel the rhythm: PASS, PASS, PASS, PASS... and then FAIL. The FAIL landing is the moment trust is built. Don't rush past it. Point at it. Say "there it is." Let the audience see that you leave failures visible.

Practice this demo multiple times. Know exactly which experiments to run, in which order, and which lines to highlight. The five experiments should take about 5 minutes with commentary.

---

## SECTION 6: The FAIL — Why It Matters (3 minutes)

**SLIDE: talk6_09_gpa_fail.png** — Show during anatomy

**SLIDE: talk6_10_pass_fail_ratio.png** — Show during ratio discussion

### TECHNICAL VERSION

The Gravity Probe A comparison: predicted fractional frequency shift Δf/f = GM/(Rc²) with R = R_Earth + 10,000 km = 4.252 × 10⁻¹⁰. Measured (Vessot & Levine, 1980): (4.36 ± 0.03) × 10⁻¹⁰. Miss: 2.47%. Gate: < 1%. Result: FAIL.

Three possible explanations, none confirmed:
1. The reference altitude (10,000 km) is a round number. The actual rocket trajectory was suborbital — the effective altitude was lower than the apogee, and the comparison should use a trajectory-integrated average, not the peak altitude.
2. The 1976 reference paper's value may have been rounded differently than the original measurement report.
3. There may be a genuine systematic issue with the derivation at this level of approximation.

The diagnosis is published alongside the failure. The failure is not hidden, not explained away, not moved to supplementary material. It appears in the same report as the 41 passes, in the same format.

The ratio — 252:1 — is not the point. The point is that the 1 exists. A system that only shows successes is a marketing document, not a test suite.

### NON-TECHNICAL VERSION

The GPA comparison fails. Let me tell you exactly what happened.

The derivation uses the standard gravitational redshift formula. It predicts a frequency shift of 4.252 times 10 to the negative 10. The measurement, from a 1980 suborbital rocket experiment, is 4.36 times 10 to the negative 10. That's a 2.47% miss. The tolerance was set at 1%. It's outside the gate. FAIL.

Why might it fail? Three possibilities. First: I used 10,000 km as the altitude — a round number. The actual rocket was suborbital — it went up and came back down. The effective altitude was lower than the peak. A proper trajectory integration would give a different number.

Second: the reference value might be rounded differently in the paper I used versus the original measurement report.

Third: there might be a genuine problem I haven't identified.

I don't know which. The system doesn't know which. It just says FAIL and leaves the investigation for later.

Here's what matters: the FAIL is in the output. Same format as the passes. Same font size. Not hidden. Not in a footnote. Not explained away as "within expected approximation error." It says FAIL and I show it to you.

252 pass. 1 fails. The ratio isn't the point. The point is that the 1 is there. If I hid the red, why would you trust the green?

### MERGE NOTES

"If I hid the red, why would you trust the green" is the line of the entire video. Deliver it looking at the camera. The three hypotheses for the GPA failure are honest — you've investigated and you don't know the answer. Say that. "I don't know which" is more credible than any explanation. The ratio observation — "252:1, the ratio isn't the point" — reframes what the audience should take away.

---

## SECTION 7: The Kill Switches (3 minutes)

**SLIDE: talk6_11_kill_switch_anatomy.png** — Show during kill switch display

**SLIDE: talk6_12_statistical_block.png** — Show during p=0.81 discussion

### TECHNICAL VERSION

Every active research program in the framework carries an explicit `kill_switches` array — an ordered list of conditions that, if satisfied by future data, would terminate the program.

Example — `program_beta_unification_v0`:
- Kill 1: `coincidence_probability` — if p > 0.1 for the observed integer matches under a random-pair null model. Source: combinatoric analysis. Status: BLOCKING at p = 0.81.
- Kill 2: `cmb_s4_omega` — if CMB-S4 or LiteBIRD data moves Ω_DM away from 44/169. Source: CMB-S4 (2027+).
- Kill 3: `lhc_no_cd` — if LHC Run 3 + HL-LHC excludes the CD at all masses up to 6 TeV. Source: ATLAS/CMS (2025-2035).

Each kill switch names a specific condition, a specific threshold, and a specific data source with an approximate timeline. These are not vague — they are pre-registered falsification criteria.

The statistical control node deserves emphasis: the framework's own combinatoric analysis shows p = 0.81 for the (22/13)π match to the dark matter ratio. Random integer pairs (a/b)π achieve comparable or better matches to 5.320 about 81% of the time. The system blocks the claim from advancing until this p-value is resolved — either through additional derivation chain evidence that reduces the effective trial factor, or through an independent prediction that the same integers produce.

This is a self-imposed gate against confirmation bias. The most exciting headline result in the framework — the dark matter ratio from gauge integers — is explicitly blocked by the framework's own quality control.

### NON-TECHNICAL VERSION

Every active research program has kill switches — pre-defined conditions that would kill the program if they're met.

Let me show you what one looks like.

The beta unification program — the one that produces the dark matter ratio and the weak mixing angle — has three kill switches.

Kill switch one: the statistical test. If random integers can do as well as 22/13, the match might be coincidence. The threshold: p must be below 0.1. The current value: p = 0.81. Status: BLOCKING.

Let me say that again. My own system, my own statistical test, says the headline result — the one I'm most excited about — might be a coincidence. And the system won't let me advance the claim until the statistics are resolved.

Kill switch two: if a better satellite — CMB-S4, launching in the next few years — measures the dark matter density and it moves away from our predicted value, the program dies.

Kill switch three: if the LHC searches the entire mass range and doesn't find the Cabibbo Doublet, the unification part of the program dies.

Named conditions. Named experiments. Named thresholds. Not vague. Not movable. If the condition is met, the program dies. I wrote these kill switches into my own system. Nobody required it. Nobody asked for it. Software engineers build kill conditions into their systems because that's how you prevent bad code from shipping. I applied the same principle to physics claims.

### MERGE NOTES

The kill switches are your engineering discipline applied to physics. "I wrote these into my own system, nobody required it" — that's a software engineer's instinct and you can explain it naturally. The p = 0.81 blocking is the most powerful honesty moment in the series. "My own system blocks my own headline result" — deliver that slowly. Let it land. The audience has never seen a researcher build self-blocking quality gates into their own work.

---

## SECTION 8: The Killed Paths (2 minutes)

**SLIDE: talk6_13_graveyard.png** — Show during dead ends list

**SLIDE: talk6_14_program_status_map.png** — Show during status overview

### TECHNICAL VERSION

Six research programs have been terminated with documented cause of death:

1. SM unification without CD: gap ratio 218/115, miss 39.6% from measurement. Status: KILLED.
2. PSLQ search for compact relations: 82/82 null. Status: KILLED.
3. Koide phase adjustment: identity proof shows the phase parameter is not adjustable. Status: KILLED.
4. Fermion gap fix: generation democracy forces the correction to zero. Status: KILLED.
5. Lambda one-eighth: radiative corrections have the wrong sign. Status: KILLED.
6. Hubble VP prediction: N_VP = 0.71 < 1, insufficient for a full VP step. Status: KILLED.

Each killed program remains in the documentation with its kill date, kill reason, and the evidence that triggered the kill. The killed programs are not deleted — they serve as documented dead ends that prevent future investigators from repeating the same work.

Current status: 6 ACTIVE, 6 KILLED, 1 BLOCKED. The balanced ratio — equal numbers of active and killed programs — indicates that the kill discipline is genuine, not performative.

### NON-TECHNICAL VERSION

The system also records what didn't work. Not as failed attempts swept under the rug — as documented dead ends with cause of death.

Six programs have been killed.

SM unification without the Cabibbo Doublet — killed because the gap ratio 218/115 misses by 40%.

The PSLQ search for shortcuts between transcendental constants — killed because 82 out of 82 tests found nothing.

Koide phase adjustment — killed because a mathematical proof shows it can't work.

Fermion gap fix — killed because a symmetry argument zeroes out the correction.

Lambda one-eighth — killed because the corrections go the wrong direction.

Hubble VP prediction — killed because the step size is too small.

Six killed. Six active. One blocked. Equal numbers. That ratio tells you something: I kill as many ideas as I keep. The dead ends are as valuable as the successes because they save the next person from trying the same thing.

The institution doesn't do this. Dead research programs are quietly abandoned. The funding dries up, the students graduate, the professor moves on. Nobody publishes "we tried this and it's dead, here's why." This system does.

### MERGE NOTES

"I kill as many ideas as I keep" is a strong line. The six-killed-six-active parity is a number you can cite. Each kill has a one-line cause of death you can state. The institutional contrast — "nobody publishes 'we tried this and it's dead'" — is an observation that builds credibility.

---

## SECTION 9: The Provenance Chain (2 minutes)

**SLIDE: talk6_15_provenance_chain.png** — Show during trace-back

**SLIDE: talk6_16_version_control.png** — Show during update comparison

*[Terminal demo: trace a result back to its source]*

### TECHNICAL VERSION

Any result in the framework can be traced backward through five links:

1. **Result**: e.g., `result_sin2_predicted_v0 = 0.231223`
2. **Derivation**: `sin2_from_one_loop_crossing_v0` — the function that produced it
3. **Inputs**: `coupling_alpha_em_inverse_v0`, `beta_modified_u1_total_v0`, etc. — the pool values it consumed
4. **Sources**: CODATA 2018 (for α_em), group theory (for beta coefficients)
5. **Measurements**: Parker et al. 2018 / Morel et al. 2020 (for the Rb recoil determination of α)

This is a chain of custody from prediction back to measurement. If a measurement improves — for example, if CODATA 2024 revises α_em — you update one JSON node in the pool and rerun all experiments. Every downstream result updates automatically. The test suite reports which comparisons changed status.

Compare to the standard workflow: a measurement improves → manually identify every paper that used the old value → manually recompute each downstream result → publish corrections → wait for peer review. This process takes months and is error-prone. The automated pipeline takes 30 seconds and is exact.

### NON-TECHNICAL VERSION

Pick any result in the system and I can trace it back to where it came from.

*[Terminal]*

Here's the weak mixing angle prediction: 0.231223. Where did it come from? From this derivation function. What did that function use as inputs? Alpha inverse from the pool, the modified beta coefficients from the pool. Where did those come from? Alpha from CODATA 2018, betas from group theory.

Five links. Prediction → derivation → inputs → sources → original measurements.

Every number has a return address. Every derivation is a chain of custody.

And here's the practical payoff. When a measurement improves — say CODATA publishes a better alpha — I change one number in one file. Then I rerun all 36 experiments. Every downstream result that depends on alpha updates automatically. In 30 seconds, I know which comparisons still pass and which changed.

In standard physics: someone publishes a better alpha. Every paper that used the old alpha needs to be manually updated. Every downstream calculation recomputed by hand. Corrections published. Peer review waited for. Months of work, error-prone at every step.

This is version control for physics.

### MERGE NOTES

"Version control for physics" — you invented this framing and it's perfect. The trace-back demo is something you can do live. The contrast between "30 seconds, automatic" and "months, manual, error-prone" is SRE versus legacy operations. You live this contrast daily.

---

## SECTION 10: The Comparison to Peer Review (2 minutes)

**SLIDE: talk6_19_complete_system.png** — Show during system architecture

**SLIDE: talk6_20_physics_vs_software.png** — Show during practice comparison

### TECHNICAL VERSION

Peer review and automated testing are complementary quality control mechanisms that operate on different dimensions:

| Dimension | Peer Review | Test Suite |
|---|---|---|
| What it checks | Narrative coherence, methodological validity | Numerical agreement with measurement |
| Who evaluates | 2-3 domain experts | A comparison function |
| Time to result | 3-6 months | 2-30 seconds |
| Reproducibility | Low (different reviewers give different opinions) | Perfect (deterministic computation) |
| Coverage | Selected claims in the paper | Every derived quantity |
| Bias sensitivity | High (author reputation, institutional affiliation) | Zero (doesn't know the author) |
| Failure visibility | Low (rejections not published, failures buried) | Perfect (FAIL in same report as PASS) |

The test suite does not replace peer review. It replaces the assumption that social evaluation is equivalent to numerical verification. A paper that passes peer review may contain numerical errors that reviewers didn't check. A computation that passes the test suite may be theoretically flawed in ways the tests don't capture. Both are necessary. Neither is sufficient.

### NON-TECHNICAL VERSION

Let me compare the two quality control systems.

The institution's system: peer review. You submit a paper. You wait 3 to 6 months. Two or three people read it and give their opinion. The opinion is subjective — it depends on who the reviewers are, what they know, what they think of you. The result is accept or reject.

My system: a test suite. You write the comparison. You run it. 253 numbers checked in 2 seconds. Binary result: PASS or FAIL. The computer doesn't know who wrote the code. It doesn't know what department you're in. It doesn't care.

Peer review checks the story. The test suite checks the numbers. Peer review takes months. The test suite takes seconds. Peer review depends on who reviews. The test suite depends on whether the number matches.

Both have value. Peer review catches conceptual errors, logical gaps, methodological flaws that no numerical test would find. The test suite catches numerical errors that no reviewer would compute by hand.

But only one of them can be automated, reproduced by anyone, and run at the speed of computation. And only one of them publishes FAIL alongside PASS in the same report.

The test suite doesn't replace understanding. It replaces the pretense that a social process is the same as numerical verification.

### MERGE NOTES

"The test suite doesn't replace understanding" — say this first to prevent misunderstanding. You're not attacking peer review. You're supplementing it. The 10-row comparison slide does the heavy lifting. The key insight: "only one publishes FAIL alongside PASS." You've experienced the contrast between social and automated quality control in your SRE career — bring that experience.

---

## SECTION 11: Close (1 minute)

**SLIDE: talk6_20_physics_vs_software.png** — Hold as closing reference

*[In frame, talking to camera.]*

### TECHNICAL VERSION

36 experiments. 253 comparisons. 252 PASS. 1 FAIL. Both visible.

Kill switches on every active program. Documented dead ends for every killed program. A statistical blocking gate on the headline result.

Every value typed, every source documented, every chain traceable from prediction to original measurement. The system doesn't tell you the results are good — it shows you the results and the references and the gaps, and you decide.

This is what physics looks like when a software engineer builds it.

### NON-TECHNICAL VERSION

36 experiments. 253 comparisons. 252 pass. 1 fail. Both published.

Kill switches on every program. Dead ends documented. The headline result blocked by my own statistical test.

Every value typed. Every source documented. Every chain traceable from prediction back to original measurement.

The system doesn't tell you the results are good. It shows you the results and you decide.

This is what physics looks like when a software engineer builds it. You can run every experiment yourself — the code is on GitHub, the value pool is public. If you find an error, it's a real error, not a matter of opinion.

Next week: the map has edges. What we don't know, where the boundaries are, and what kills the model.

Links in the pinned comment. Check the numbers.

### MERGE NOTES

"This is what physics looks like when a software engineer builds it" — that's the thesis of your entire project, not just this video. Let it land. "If you find an error, it's a real error, not a matter of opinion" — that's an invitation and a challenge. End on "check the numbers."

---

## TERMINAL DEMO NOTES

This is the most terminal-heavy video alongside Video 5. Seven demos:

**Demo 1 (Section 2):** Run one simple experiment to show the output format. 30 seconds.

**Demo 2 (Section 3):** List all 36 experiments. Open one JSON briefly. Run one experiment with line-by-line commentary. 90 seconds.

**Demo 3 (Section 4):** Search the pool. Info on alpha inverse. Info on hadronic VP delta (showing uncertainty and notes). 90 seconds.

**Demo 4 (Section 5):** THE CENTERPIECE. Run five experiments back-to-back. QED, EW, BBN, proton decay, GR. Comment on each output as it scrolls. Point at the FAIL. 5 minutes.

**Demo 5 (Section 7):** Show kill switch entries in the pool/programs. Show the statistical control node. 60 seconds.

**Demo 6 (Section 8):** Show killed program entries. 30 seconds.

**Demo 7 (Section 9):** Trace a result back to its source — show the derivation, inputs, and sources. 60 seconds.

Total demo time: ~10 minutes. In a 30-minute video, that's 33% terminal time. Practice the five-experiment centerpiece until you can do it smoothly with commentary.

---

## PACING GUIDE

| Section | Duration | Energy | Key Moment |
|---|---|---|---|
| Opening | 1 min | Professional | "When I build something, I test it" |
| What a test suite is | 2 min | Teaching | "Does the number match?" |
| Experiment system | 3 min | Architectural | "The experiment is a contract" |
| Value pool | 3 min | Database tour | "Nothing anonymous, nothing unsourced" |
| Five experiments | 5 min | Demonstration crescendo | "FAIL. There it is." |
| The FAIL | 3 min | Honest, slow | "If I hid the red, why trust the green" |
| Kill switches | 3 min | Principled | "My own system blocks my own claim" |
| Killed paths | 2 min | Matter-of-fact | "I kill as many ideas as I keep" |
| Provenance | 2 min | Engineering pride | "Version control for physics" |
| vs Peer review | 2 min | Balanced | "Both necessary, neither sufficient" |
| Close | 1 min | Direct | "You can run every experiment yourself" |

Total: ~27 minutes. The five-experiment demo can expand to 8 minutes or contract to 4 depending on pace.

---

## SLIDE SEQUENCE

| Slide | Filename | When to show |
|---|---|---|
| 1 | talk6_01_test_cycle.png | "write, run, compare" |
| 2 | talk6_02_test_vs_peer_review.png | "two quality systems" |
| 3 | talk6_03_experiment_json.png | "inside the experiment file" |
| 4 | talk6_04_five_match_modes.png | "five ways to check" |
| 5 | talk6_05_value_pool.png | "2700+ values" |
| 6 | talk6_06_value_node_anatomy.png | "every field" |
| 7 | talk6_07_five_experiments.png | "after all five have run" |
| 8 | talk6_08_terminal_output.png | "raw output" |
| 9 | talk6_09_gpa_fail.png | "the one that failed" |
| 10 | talk6_10_pass_fail_ratio.png | "252:1, the 1 is the point" |
| 11 | talk6_11_kill_switch_anatomy.png | "named conditions" |
| 12 | talk6_12_statistical_block.png | "p = 0.81, BLOCKING" |
| 13 | talk6_13_graveyard.png | "six documented dead ends" |
| 14 | talk6_14_program_status_map.png | "6 alive, 6 killed, 1 blocked" |
| 15 | talk6_15_provenance_chain.png | "chain of custody" |
| 16 | talk6_16_version_control.png | "swap one node, rerun" |
| 17 | talk6_17_253_domain_map.png | "9 domains, mostly green" |
| 18 | talk6_18_precision_staircase_sorted.png | "ppb to percent" |
| 19 | talk6_19_complete_system.png | "the complete architecture" |
| 20 | talk6_20_physics_vs_software.png | "closing comparison — hold" |

