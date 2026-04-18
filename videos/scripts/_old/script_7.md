
# Video 7 Script: The Map Has Edges — What We Don't Know and Where the Boundaries Are

## Delivery Notes

This is the honesty video. After five videos of results, you're spending an entire episode on what doesn't work, what's uncertain, and what could kill the model. The energy is "engineer filing a bug report on their own system." Every section follows: here's the claim → here's the weakness → here's what would kill it. The audience should leave thinking "this person is more interested in being right than in being impressive."

---

## SECTION 1: Opening — Why This Video Exists (1 minute)

*[In frame, talking to camera. No slides.]*

### TECHNICAL VERSION

Six videos of results. 253 comparisons passing. Precision from ppb to ppm. The natural expectation is that this video continues the victory lap.

It doesn't. This video is the map's edges — the places where the derivation chains stop, where the approximations break down, where the statistics don't support the claims, and where specific future experiments could kill specific parts of the model.

A framework that only shows its strengths is a sales pitch. A framework that documents its weaknesses is a research program. The edges are where the next work happens. They're also where the kills would come from.

### NON-TECHNICAL VERSION

I've spent five videos showing you what works. This video is about what doesn't work. What we don't know. Where the model is weak. What could kill it.

If I only showed you the successes, you'd be right not to trust me. Every model has edges — places where the chain stops, where the approximation breaks, where the data isn't good enough. This video maps those edges.

The edges are the most valuable part of the map. They tell you where the next work is. They tell you where the kills would come from. And they tell you whether the person presenting the model cares more about being right or about looking impressive.

I care about being right. So let's talk about everything that's wrong.

### MERGE NOTES

Open by acknowledging the pattern — five videos of results, now a deliberate turn. "A framework that only shows its strengths is a sales pitch" is your thesis. Don't be performatively humble — be factual. This isn't self-deprecation. It's engineering documentation.

---

## SECTION 2: The Unification Gap — One-Loop Is Not Enough (3 minutes)

**SLIDE: talk7_01_unification_gap.png** — Show during one-loop limits

**SLIDE: talk7_02_loop_order_convergence.png** — Show during convergence discussion

### TECHNICAL VERSION

The entire framework operates at one-loop order in the renormalization group equations. The one-loop beta coefficients (b₁, b₂, b₃) are exact rational numbers, but the one-loop approximation itself is an approximation — it neglects two-loop, three-loop, and higher-order corrections to the running.

The two-loop beta coefficients are also exact rational numbers (computed from group theory), but they introduce cross-coupling between the three gauge groups. The correction to the unification scale M_GUT is of order α/(4π) ≈ 0.2% — small but potentially significant at the precision levels the framework claims.

Specific consequences:
- The proton mass prediction misses by 28.6%. This is a known one-loop artifact — the strong coupling α_s runs too fast at one-loop, giving too large a value at the confinement scale. Two-loop running reduces the miss significantly.
- The pion mass prediction misses by ~51%. Same origin.
- The precise location of the GUT scale M_GUT shifts by 0.2-0.5 orders of magnitude at two-loop.
- The gap ratio 38/27 is a one-loop result. At two-loop, small corrections of order Δ ~ 0.01-0.03 modify the ratio. Whether 38/27 remains meaningful at two-loop is an open question.

The two-loop implementation is pending work. The framework is designed to accommodate it — the value pool has `beta_twoloop_*` entries ready, and the derivation functions can be extended. But the computation has not been run.

This is the single largest systematic limitation of the framework: everything operates at the first order of a perturbative expansion that is known to have non-negligible higher-order corrections.

### NON-TECHNICAL VERSION

The entire model operates at the first level of approximation. Let me explain what that means.

When forces run — when they change strength with energy — the equation that describes the running has multiple terms. The first term is the one-loop contribution. It's exact — it comes from counting, and the count is right. The second term is the two-loop contribution. Also exact, also from counting. The third term, same.

The model uses only the first term. That's the one-loop approximation.

For most results, the first term dominates and the corrections are small — less than 1%. But for some results, the corrections matter.

The proton mass prediction misses by 28.6%. That's not a small miss. The reason: at one-loop, the strong force runs too fast, which means the confinement energy comes out too high. At two-loop, the running slows down and the prediction improves. This is a known fix — I just haven't implemented it yet.

The pion mass misses by about 51%. Same reason.

And the big question: the gap ratio 38/27. That's the cornerstone number — the exact fraction that makes everything work. At one-loop, it's exactly 38/27. At two-loop, there are small corrections. Does 38/27 survive those corrections? I don't know yet. That's an open question and it's the most important open question in the framework.

This is the single largest systematic limitation: everything is computed at first order, and higher-order corrections are known to exist.

### MERGE NOTES

You understand this limitation clearly. "Known fix, haven't implemented it" is honest and concrete. The proton mass miss (28.6%) is a number you can cite — it's the worst result in the framework and you're leading with it. The open question about 38/27 at two-loop is genuinely uncertain, and you should say so. Don't promise it survives. Don't predict it fails. Say "I don't know yet."

---

## SECTION 3: The Statistical Problem — p = 0.81 (3 minutes)

**SLIDE: talk7_03_p081_blocked.png** — Show during statistical analysis

**SLIDE: talk7_04_random_integer_hits.png** — Show during random pair comparison

### TECHNICAL VERSION

The dark matter to baryon ratio prediction: DM/baryon = (22/13)π = 5.3165, compared to Planck measurement 5.3204 ± 0.0066. Miss: 725 ppm.

The statistical challenge: under the null hypothesis that the integers 22 and 13 are arbitrary (not derived from gauge theory), what is the probability that a random pair (a/b)π matches 5.320 as well or better?

The combinatoric analysis samples integer pairs (a, b) with a, b ∈ [1, 50] and computes |(a/b)π − 5.320|/5.320 for each. Result: approximately 81% of such pairs produce a match within 725 ppm of 5.320.

This means the (22/13)π match, taken in isolation, is not statistically significant. The probability that a random integer pair achieves comparable agreement is p = 0.81 — well above any conventional significance threshold.

The framework's response: the statistical control program has status = BLOCKING. The dark matter ratio claim cannot advance from "numerical match" to "derived prediction" until either:
1. Additional derivation chain evidence reduces the effective trial factor (e.g., the same 22 and 13 independently predict other observables)
2. An independent prediction from the same integers matches a different measurement
3. The combinatoric analysis is refined with physics-motivated constraints on (a, b)

The blocking is genuine — it affects how the result is presented in every paper and every video. The number is shown as a match, not as a confirmed derivation.

### NON-TECHNICAL VERSION

Now the statistical problem. This is the most uncomfortable section of the talk, and that's why it has to be here.

The dark matter ratio: 22 over 13 times pi equals 5.317. Planck measures 5.320. That's a match at 725 parts per million. Sounds impressive.

But here's the question: if I just picked two random integers and multiplied their ratio by pi, how often would I get a match that good?

The answer: 81% of the time.

Let me say that again. If you randomly pick integers from 1 to 50, form the ratio, multiply by pi, and compare to 5.320 — about 81% of random pairs match as well as 22/13 does.

That's devastating. It means the match, by itself, is not statistically significant. It might be a coincidence.

Now, 22 and 13 aren't random — they come from gauge theory. 22 is twice the Yang-Mills coefficient. 13 is the weak force beta numerator with the Cabibbo Doublet. There are physical reasons for those specific numbers. But the statistical test doesn't know that. It just asks: given the numerical value 5.320, how special is the match?

Not very. p = 0.81.

My system has a gate. The claim is blocked. The dark matter ratio is presented as a numerical match, not as a confirmed derivation. It stays blocked until either additional evidence reduces the trial factor, or an independent prediction from the same integers matches a different measurement.

I built a gate into my own pipeline that prevents me from fooling myself. The most exciting result in the entire framework is blocked by my own quality control.

### MERGE NOTES

This is the section where your credibility is forged. "81% of random pairs match as well" — deliver that as a body blow. Don't soften it. Don't immediately say "but the integers have physical meaning." Let the audience sit with the statistical problem before you acknowledge the physical reasoning. The gate — "my system blocks my own headline result" — should land as something the audience has never seen a researcher do.

---

## SECTION 4: The Confinement Wall — Where Perturbation Theory Stops (2 minutes)

**SLIDE: talk7_05_confinement_blank.png** — Show during non-perturbative discussion

**SLIDE: talk7_06_inside_the_wall.png** — Show during wall interior

### TECHNICAL VERSION

The perturbative approach — expanding in powers of α_s — breaks down at the confinement scale Λ_QCD ≈ 200 MeV, where α_s approaches 1 and the expansion diverges. Below this scale, the strong coupling is non-perturbative and the framework's integer fraction machinery loses its precision.

Specific consequences:
- The proton mass cannot be derived from perturbative QCD. The 938 MeV comes from non-perturbative gluon field dynamics — lattice QCD is the only known method, and it's numerical, not analytic.
- The hadronic vacuum polarization contribution to muon g-2 — the quantity whose two computational methods disagree — involves integration over the non-perturbative regime.
- The pion mass, the nuclear reaction rates used in BBN, and any quantity involving hadron structure are limited by the confinement wall.

The framework inherits this limitation from the Standard Model. It is not a weakness specific to the soliton approach — it affects every framework in particle physics. But it bounds the precision achievable for any quantity that depends on the interior of the proton or other hadrons.

The boundary thickness work (PHYS-45) characterizes the wall mathematically: the confinement boundary has thickness 1/|b₃| = 1/7 in natural logarithmic units. This is a structural property of the boundary, but it doesn't provide a perturbative route through the wall.

### NON-TECHNICAL VERSION

There's a wall in the model. A hard wall. And it's not unique to this framework — every framework in physics hits it.

The strong force gets stronger as you go to lower energies. At the proton scale, it's approximately 1. When the force strength is 1, the approximation method — expanding in powers of the force strength — breaks down. You can't expand in powers of 1. The series doesn't converge.

Below this wall — inside the proton — the integer fraction machinery doesn't work. The proton mass of 938 MeV can't be derived from the methods I've been showing you. It comes from the non-perturbative gluon field — the circulation energy I described in Video 3. The only way to compute it from first principles is lattice QCD, which is a numerical simulation, not analytic integer arithmetic.

This affects the hadronic vacuum polarization — the piece that causes the disagreement in the muon anomaly. It affects pion masses. It affects nuclear reaction rates in BBN.

The framework inherits this wall from the Standard Model. I didn't create it and I can't fix it. It bounds what the model can compute at high precision.

I mapped the wall's properties — in a recent paper, I calculated the boundary thickness as 1/7 in natural units. I can describe the wall's structure. I can't see through it.

### MERGE NOTES

"I can describe the wall. I can't see through it" — a good closing line for this section. The confinement wall is a genuine limitation that every physicist knows about. You're not revealing a hidden weakness — you're documenting a known limitation that the framework inherits. The boundary thickness (1/7) is a result you're proud of — mention it, but acknowledge it doesn't solve the problem.

---

## SECTION 5: Gravity — The Disconnected Force (3 minutes)

**SLIDE: talk7_07_gravity_disconnected.png** — Show during gravity isolation

**SLIDE: talk7_08_g_scatter.png** — Show during G measurement scatter

### TECHNICAL VERSION

The framework derives 53 values from 13 inputs across 9 domains. The gravitational sector is structurally distinct from the other 8: gravity is not a gauge force in the Standard Model, Newton's constant G is not derived from the gauge group, and the gravitational results in the framework are largely interpretive — they use the reading/running reading vocabulary applied to GR but do not derive gravitational parameters from the same integer fraction chain.

Specific weaknesses:
- G is measured, not derived. The scatter in published G measurements (from different laboratories using different methods) spans approximately 500 ppm — an anomalously large spread for a fundamental constant. The framework offers an interpretation (different laboratories at different gravitational potentials see different effective G values) but no derivation.
- The GR comparison suite (18 comparisons) uses GR formulas with G as an input, not as a derived value. The integer fraction content of these comparisons comes from the geometric structure of GR (e.g., Shapiro delay parameter γ = 1 exact), not from the gauge group.
- The sector splitting prediction (ε ≈ 10⁻¹² between nuclear and optical clocks) is a proposal, not a computation. The magnitude 10⁻¹² is an order-of-magnitude estimate based on boundary thickness differences.

The gravity sector is the most speculative part of the framework. It's also the most falsifiable — the sector splitting prediction is specific enough to be tested by PTB/JILA thorium-229 clock experiments in 2028-2032.

### NON-TECHNICAL VERSION

Gravity is different from the other three forces. In the Standard Model, gravity isn't a gauge force. It doesn't come from the same SU(3) × SU(2) × U(1) symmetry group. And in this framework, it's also different — it's the least connected part.

Newton's gravitational constant G is measured, not derived. I don't have a chain from gauge integers to G. I have an interpretation — the soliton vocabulary applied to general relativity — but not a derivation.

And the measurements of G are strange. Different laboratories get different values. The scatter is about 500 parts per million — much larger than the measurement uncertainties. For a fundamental constant, that's bizarre. My framework offers an interpretation: maybe different labs at different gravitational potentials see different effective G values. But that's speculation, not computation.

The 18 GR comparisons in the test suite use Einstein's equations with G as an input. They test the geometric structure of general relativity — the Shapiro delay parameter equals exactly 1, Mercury's perihelion matches to 2.8 ppm. But the integers in these results come from the geometry of spacetime, not from the gauge group.

And the sector splitting prediction — the idea that nuclear and optical clocks might show different gravitational time dilation — is an order-of-magnitude estimate. It's specific enough to test, but it's not a precision computation like the QED chain.

The gravity sector is the most speculative part of the model. I say that openly. It's also the most falsifiable — one experiment in the next decade either confirms or kills it.

### MERGE NOTES

"The gravity sector is the most speculative part" — say this directly. The G scatter observation is interesting but speculative, and you should frame it that way. The key honesty: "I have an interpretation but not a derivation." The sector splitting prediction being testable is the upside — say "most speculative, most falsifiable" together.

---

## SECTION 6: The Hubble Tension — Reading Differences or Systematic Errors? (2 minutes)

**SLIDE: talk7_09_hubble_tension.png** — Show during tension description

**SLIDE: talk7_10_four_confidence_levels.png** — Show during confidence ranking

### TECHNICAL VERSION

The Hubble tension: the local measurement of H₀ (Cepheid-calibrated Type Ia supernovae, Riess et al.) gives 73.0 ± 1.0 km/s/Mpc. The CMB-inferred value (Planck ΛCDM fit) gives 67.4 ± 0.5 km/s/Mpc. The tension is 4-6σ depending on the analysis.

The framework offers an interpretation: the two measurements probe different soliton boundaries. The local measurement uses objects within the galactic and cluster boundary hierarchy. The CMB measurement uses the cosmic microwave background at the outermost boundary. Different boundaries can give different readings of the same underlying expansion rate.

This interpretation is not computed. There is no derivation that predicts H₀(local) = 73 and H₀(CMB) = 67.4 from soliton boundary properties. The interpretation is qualitative, not quantitative.

The framework classifies its results by confidence level:
1. **Computed and tested** (highest): QED chain, electroweak sector, BBN chain. Specific predictions matched against measurement.
2. **Computed but statistically uncertain**: DM/baryon ratio (p = 0.81).
3. **Interpreted but not computed**: Hubble tension, G scatter.
4. **Speculative**: sector splitting prediction, toroidal dark matter interpretation.

The Hubble tension sits at level 3. The interpretation is consistent with the framework but doesn't constitute evidence for it.

### NON-TECHNICAL VERSION

The Hubble tension is one of the biggest open problems in cosmology. Two ways of measuring the expansion rate of the universe give different answers. Local measurements say 73. The cosmic microwave background says 67.4. The disagreement is between 4 and 6 standard deviations — significant.

The framework offers an interpretation: the two measurements are looking at different boundaries. The local measurement uses objects inside the galaxy and nearby clusters. The CMB measurement uses the oldest light in the universe — the outermost boundary. Different boundaries, different readings. That's the soliton principle.

But I haven't computed this. There's no derivation that predicts 73 from one boundary and 67.4 from another. The interpretation is qualitative — it says why they might differ, not how much they differ.

Let me rank the confidence levels in the framework:

Level one, highest: QED chain, electroweak sector, BBN chain. These are computed, tested, matched. This is the solid ground.

Level two: the dark matter ratio. Computed but statistically uncertain — p = 0.81.

Level three: the Hubble tension, the G scatter. Interpreted but not computed. Consistent with the framework but not evidence for it.

Level four: sector splitting, toroidal dark matter. Speculative. Testable but not yet tested.

The Hubble tension is level three. I don't claim it as a result. I claim it as a question worth investigating.

### MERGE NOTES

The four-level confidence ranking is your own system and you can present it clearly. "I don't claim it as a result, I claim it as a question" — that's precisely the right framing. The audience should see you voluntarily reducing the scope of your claims. Each level has concrete examples they've seen in previous videos.

---

## SECTION 7: Mass Hierarchy and the Koide Relation (2 minutes)

**SLIDE: talk7_11_mass_hierarchy.png** — Show during mass scale discussion

**SLIDE: talk7_12_koide_conditional.png** — Show during Koide status

### TECHNICAL VERSION

The charged lepton masses (m_e = 0.511 MeV, m_μ = 105.7 MeV, m_τ = 1776.9 MeV) satisfy the Koide relation: (m_e + m_μ + m_τ)/(√m_e + √m_μ + √m_τ)² = 2/3 to 62 ppm. This is an empirical observation with no standard derivation.

The framework's status:
- The Koide relation is reproduced (it uses the measured masses, which satisfy the relation by construction).
- The framework proposes that the Koide relation arises from a structural property of the soliton boundary hierarchy — specifically, that the three lepton generations are three modes of the same vortex pattern, and the mass ratio encodes the mode structure.
- However, no derivation exists that predicts the three masses from the framework's inputs. The masses are inputs, not outputs.

The mass hierarchy problem — why m_t/m_e ≈ 338,000 — is not addressed. The framework has no mechanism to derive quark or lepton masses from gauge integers. The masses enter as measured inputs. The Koide relation and the generation structure are acknowledged as patterns without derived explanations.

The Koide phase adjustment (attempting to modify the relation to predict masses) was tried and killed — the identity proof shows the phase parameter is algebraically constrained and cannot serve as a free parameter.

### NON-TECHNICAL VERSION

Why is the electron so light and the top quark so heavy? The top quark weighs 338,000 times more than the electron. Why?

I don't know. The framework doesn't answer this.

The masses of the particles are inputs to the model, not outputs. I don't derive them from integers. I use the measured values. This is a major gap.

There's a beautiful pattern — the Koide relation — that connects the three charged lepton masses. The electron, the muon, and the tau satisfy a formula to 62 parts per million. That's suspiciously precise for a relation nobody has derived.

The framework reproduces this relation, but only because it uses the measured masses as inputs. Reproducing it isn't the same as predicting it. I tried to modify the relation to predict the masses — that path was killed. The math proves it can't be done the way I attempted.

The mass hierarchy is an open problem. It's an open problem for everyone, not just for me. But it's still a gap in the map.

### MERGE NOTES

"I don't know" is a powerful sentence. Use it. The Koide relation at 62 ppm is genuinely interesting and you can cite the number. The killed path (Koide phase adjustment) is documented honesty. "It's an open problem for everyone, not just for me" — this contextualizes the gap without excusing it.

---

## SECTION 8: The Lithium Problem and Inherited Failures (2 minutes)

**SLIDE: talk7_13_lithium_problem.png** — Show during lithium discussion

**SLIDE: talk7_14_four_elements.png** — Show during BBN element comparison

### TECHNICAL VERSION

The primordial lithium-7 abundance: the framework predicts Li-7/H = 4.74 × 10⁻¹⁰. The observed value (Spite plateau) is 1.60 × 10⁻¹⁰. Overproduction factor: 2.96×.

This is the cosmological lithium problem, a 40-year-old unsolved discrepancy present in every BBN calculation using standard nuclear reaction rates. Proposed explanations include: modified Be-7(n,p) reaction rates, in-situ stellar lithium depletion, non-equilibrium photon spectra during BBN, and beyond-Standard-Model physics during the nucleosynthesis epoch. None is universally accepted.

The framework inherits this problem because it uses the same Wagoner-Kawano BBN reaction network with the same nuclear cross-sections. Getting the same wrong answer for lithium as every other BBN calculation confirms that the chain is doing correct nuclear physics — the error (if it is in the nuclear rates) is in the rates, not in the framework.

Similarly: the muon g-2 tension is inherited, not generated. The proton radius puzzle (if it persists) would be inherited. Any discrepancy that exists in the Standard Model's predictions also exists in this framework, because this framework uses the Standard Model's equations.

Inherited failures are informative: they confirm the chain is computing correctly, even when the underlying physics has known issues.

### NON-TECHNICAL VERSION

Lithium. The one element the Big Bang math gets wrong.

The framework predicts 4.74 parts per ten billion of lithium-7. The measurement: 1.60. Off by a factor of 3. That's not a small miss.

But here's the thing: every model in cosmology gets lithium wrong by the same factor. This has been a known problem for 40 years. Nobody has solved it. The leading theories are that some nuclear reaction rate is wrong, or that stars have destroyed the primordial lithium. Nobody knows for sure.

My framework gets the same wrong answer because it uses the same nuclear physics equations. I didn't generate this problem — I inherited it. Getting the same wrong answer as everyone else, for the same reasons, is actually what correct physics looks like.

The same principle applies to the muon g-2 tension. My framework gets the same answer as the standard calculation, including the same unresolved dispute about how to compute the hadronic contribution. I inherit the tension. That's what a correct calculation does — it reproduces the known results, including the known problems.

Inherited failures confirm the chain is working. The bug is upstream, in the nuclear rates or the hadronic calculation, not in the framework.

### MERGE NOTES

"Getting the same wrong answer as everyone else is what correct physics looks like" — you've used this line before and it's effective. The lithium factor of 3 is dramatic. The principle of inherited failures is something any engineer understands: if you correctly implement a specification with a known bug, your output also has the bug.

---

## SECTION 9: Theta QCD and the Strong CP Problem (2 minutes)

**SLIDE: talk7_15_theta_qcd.png** — Show during strong CP discussion

**SLIDE: talk7_16_cd_search_window.png** — Show during experimental outlook

### TECHNICAL VERSION

The strong CP parameter θ_QCD measures the degree of CP violation in the strong interaction. Experimentally, θ < 10⁻¹⁰ (from the neutron electric dipole moment upper bound). The theoretical expectation — without fine-tuning — is θ ~ O(1). The discrepancy is the strong CP problem.

The framework has no derivation of θ = 0 or θ ≈ 0. The strong CP problem is not addressed. Standard proposed solutions (the Peccei-Quinn mechanism with an axion, Nelson-Barr type models) are not incorporated.

This is a known gap. If the Cabibbo Doublet is vector-like (as specified), it does not introduce additional CP-violating phases beyond those already in the CKM matrix. But this doesn't explain why θ is small — it merely doesn't make the problem worse.

The strong CP problem is listed as an open question in the framework's research program, not as a solved or addressed problem.

### NON-TECHNICAL VERSION

There's a famous puzzle called the strong CP problem. The strong force has a parameter — theta QCD — that controls how much the force violates a certain symmetry. Experimentally, this parameter is less than 10 to the negative 10. Essentially zero. But there's no theoretical reason for it to be zero. Naturally, it should be of order 1.

Why is it so small? I don't know. The framework doesn't answer this question. The standard proposed answer — the axion — is not part of the framework.

The Cabibbo Doublet doesn't make this problem worse. Being vector-like means it doesn't introduce new symmetry violations. But "doesn't make it worse" is not "solves it."

The strong CP problem is an open question. I list it as open, not addressed.

### MERGE NOTES

Brief section. "I don't know" again. The key distinction: "doesn't make it worse is not the same as solves it." You're mapping the edges honestly. Not every open problem in physics needs to be solved by your framework for the framework to be useful.

---

## SECTION 10: The Cabibbo Doublet — What If It's Not There? (3 minutes)

**SLIDE: talk7_17_cd_dependency_map.png** — Show during dependency chain

**SLIDE: talk7_18_complete_map.png** — Show during full model overview

### TECHNICAL VERSION

The Cabibbo Doublet is the single BSM particle predicted by the framework. If it doesn't exist, the consequences propagate through every chain that depends on the modified beta coefficients:

Directly killed: gap ratio = 38/27, sin²θ_W prediction (12 ppm), DM/baryon = (22/13)π (725 ppm), CKM first-row deficit explanation, proton decay prediction, modified running to the unification scale.

Survives: QED chain (depends on α_em, not on CD betas), Koide relation (uses measured masses), GR comparisons (uses G and GR equations, not gauge integers), BBN nuclear physics (uses measured η₁₀, not derived η₁₀ — though the derived η₁₀ from the DM ratio would be killed), mathematical results (Q335, PSLQ null, boundary thickness calculations).

The framework is designed to be modular. The QED chain's 15-digit match doesn't depend on the Cabibbo Doublet. The boundary thickness paper (PHYS-45) doesn't depend on it. The test suite methodology doesn't depend on it.

If the CD is excluded by the LHC at all masses up to 6 TeV, or if Hyper-Kamiokande sees no proton decay at the predicted rate: the kill switch fires, the unification program dies, and the framework loses its most dramatic claims. What remains is an engineering methodology (fraction arithmetic, automated testing, cross-domain derivation chains) and the domain-specific results that don't require the CD.

### NON-TECHNICAL VERSION

The biggest question: what if the Cabibbo Doublet doesn't exist?

The CD is the one new particle the model predicts. Everything that depends on the modified running rates — the gap ratio 38/27, the weak mixing angle at 12 ppm, the dark matter ratio at 725 ppm, the CKM deficit explanation — all of it depends on the CD being real.

If the LHC searches the full mass range and finds nothing, the kill switch fires. The unification program dies.

But not everything dies.

The QED chain — alpha extracted to 12 digits, hydrogen frequency to 11 digits — doesn't use the CD. It depends on the measured electron magnetic moment and the QED series. That chain survives.

The GR comparisons — Mercury at 2.8 ppm, GPS at 0.35% — don't use the CD. They use Einstein's equations. Those survive.

The methodology — fraction arithmetic, automated testing, the value pool, the kill switches — is independent of any specific particle. That survives.

The framework is modular by design. If the CD is killed, I lose the most exciting claims. What remains is an engineering methodology and the results that don't require the CD. The framework shrinks but doesn't collapse.

### MERGE NOTES

"The framework shrinks but doesn't collapse" is a precise and honest statement. The dependency map slide shows exactly what dies and what survives — point to both zones. You designed the modularity deliberately, and you can explain why. "If I lose the most exciting claims" — acknowledge the cost of being wrong.

---

## SECTION 11: The Kill Switch Coverage (2 minutes)

**SLIDE: talk7_19_kill_switch_coverage.png** — Show during coverage overview

**SLIDE: talk7_20_trust_from_failures.png** — Hold as closing reference

### TECHNICAL VERSION

Complete kill switch coverage across active programs:

1. **Beta unification**: killed by p > 0.1 sustained (BLOCKING at p = 0.81), CMB-S4 Ω_DM deviation, LHC CD exclusion.
2. **Toroidal DM**: killed by direct dark matter particle detection, NFW profile confirmation at high precision, toroidal morphology refuted by JWST deep field surveys.
3. **Reading depth / sector splitting**: killed by nuclear vs optical clock null at ≥2 gravitational potentials (PTB/JILA, 2028-2032).
4. **Hubble running**: killed by Hubble tension resolved as systematic error in SH0ES or Planck.
5. **G running**: killed by G scatter shown to correlate with laboratory systematics rather than gravitational environment.
6. **Confinement boundary**: killed by lattice QCD calculation matching PHYS-45 thickness prediction.

Every program has at least one kill condition with a named experiment and an approximate timeline. No program is unfalsifiable. The framework as a whole cannot be killed by a single experiment (modularity), but every individual claim can be killed by a specific test.

### NON-TECHNICAL VERSION

Every active program in the framework has at least one kill switch.

The unification program: killed if the LHC excludes the CD at all masses, or if CMB-S4 moves the dark matter density away from our prediction.

The dark matter interpretation: killed if someone detects dark matter particles directly. If dark matter is particles, it's not circulation energy.

The reading depth interpretation: killed if nuclear and optical clocks show the same time dilation. One experiment, 2028-2032.

The Hubble interpretation: killed if the tension turns out to be a systematic error in one of the measurement teams.

The G scatter interpretation: killed if the scatter turns out to correlate with lab equipment rather than gravitational environment.

Every claim has a kill condition. Every kill condition names an experiment. No claim is unfalsifiable.

The framework as a whole can't be killed by one experiment — that's the modularity. But every individual piece can be killed by a specific test. That's how science should work.

### MERGE NOTES

Run through the kill switches quickly — the audience has seen the concept in Video 6. The new content is the completeness: every program covered, every experiment named. "Every claim has a kill condition" and "no claim is unfalsifiable" are statements you can make with authority because you built the system to ensure them.

---

## SECTION 12: Close (1 minute)

*[In frame, talking to camera.]*

### TECHNICAL VERSION

The map has edges. The one-loop approximation limits mass predictions. The statistical control blocks the headline result. The confinement wall bounds non-perturbative quantities. Gravity is interpretive, not derived. The mass hierarchy is unexplained. The strong CP problem is unaddressed.

Every edge is documented. Every limitation is published. Every kill switch is named.

A model that maps its own edges is more trustworthy than a model that claims to have none. The edges are where the next work happens. They're also where the kills would come from, and I've told you exactly where to aim.

### NON-TECHNICAL VERSION

The map has edges.

The one-loop approximation limits mass predictions. The p = 0.81 problem blocks the dark matter claim. The confinement wall stops the fraction chain. Gravity is interpretive, not derived. The mass hierarchy is unsolved. The strong CP problem is open.

Every edge is documented. Every limitation is published. Every kill switch is named.

I've told you what works. I've told you what doesn't. I've told you what could kill each part. A framework that maps its own edges is more trustworthy than one that pretends it has none.

The edges are where the next work happens. They're also where the kills would come from. And I've told you exactly where to aim.

Next week: human plus AI — how this framework was actually built, and what honest AI disclosure looks like.

Links in the pinned comment. Check the numbers.

### MERGE NOTES

End on "I've told you exactly where to aim." That's the most powerful line in the video — it's an invitation to falsify. It communicates complete confidence that the results are either right or worth killing. Don't soften it. Let it land.

---

## TERMINAL DEMO NOTES

Light on demos — this is mostly talking to camera with slides:

**Demo 1 (Section 3):** Show the p = 0.81 calculation or the statistical control node. 45 seconds.

**Demo 2 (Section 10):** Show the dependency map or the CD-dependent values in the pool. 45 seconds.

Total demo time: ~90 seconds. This video is 95% talking to camera and slides.

---

## PACING GUIDE

| Section | Duration | Energy | Key Moment |
|---|---|---|---|
| Opening | 1 min | Direct | "Everything that's wrong" |
| One-loop limit | 3 min | Technical | "Does 38/27 survive at two-loop?" |
| p = 0.81 | 3 min | Uncomfortable | "81% of random pairs match as well" |
| Confinement wall | 2 min | Honest | "I can describe the wall, can't see through it" |
| Gravity | 3 min | Candid | "Interpretive, not derived" |
| Hubble tension | 2 min | Careful | "Level three: interpreted, not computed" |
| Mass hierarchy | 2 min | Brief | "I don't know" |
| Lithium | 2 min | Contextualized | "Same wrong answer as everyone" |
| Theta QCD | 2 min | Brief | "Doesn't make it worse ≠ solves it" |
| CD not there | 3 min | Structural | "Shrinks but doesn't collapse" |
| Kill coverage | 2 min | Conclusive | "Every claim has a kill condition" |
| Close | 1 min | Direct | "Where to aim" |

Total: ~26 minutes.

---

## SLIDE SEQUENCE

| Slide | Filename | When to show |
|---|---|---|
| 1 | talk7_01_unification_gap.png | "one-loop limits" |
| 2 | talk7_02_loop_order_convergence.png | "two-loop corrections" |
| 3 | talk7_03_p081_blocked.png | "p = 0.81, BLOCKING" |
| 4 | talk7_04_random_integer_hits.png | "81% of random pairs" |
| 5 | talk7_05_confinement_blank.png | "where perturbation stops" |
| 6 | talk7_06_inside_the_wall.png | "non-perturbative zone" |
| 7 | talk7_07_gravity_disconnected.png | "gravity isn't derived" |
| 8 | talk7_08_g_scatter.png | "G measurement scatter" |
| 9 | talk7_09_hubble_tension.png | "73 vs 67.4" |
| 10 | talk7_10_four_confidence_levels.png | "computed, uncertain, interpreted, speculative" |
| 11 | talk7_11_mass_hierarchy.png | "338,000× mass ratio" |
| 12 | talk7_12_koide_conditional.png | "62 ppm but not derived" |
| 13 | talk7_13_lithium_problem.png | "factor of 3, everyone gets it wrong" |
| 14 | talk7_14_four_elements.png | "three green, one red" |
| 15 | talk7_15_theta_qcd.png | "less than 10⁻¹⁰, no explanation" |
| 16 | talk7_16_cd_search_window.png | "LHC search range" |
| 17 | talk7_17_cd_dependency_map.png | "what dies, what survives" |
| 18 | talk7_18_complete_map.png | "the full model with edges marked" |
| 19 | talk7_19_kill_switch_coverage.png | "every program covered" |
| 20 | talk7_20_trust_from_failures.png | "closing frame — hold" |
