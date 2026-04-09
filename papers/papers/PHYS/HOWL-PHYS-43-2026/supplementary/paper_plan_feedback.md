## Review of PHYS-43 Plan

### What's Right

The decomposition idea is the strongest conceptual move since the one-loop degeneracy proof (MATH-9). PHYS-41 said "time dilation IS reading depth." PHYS-42 confirmed the formula works everywhere. PHYS-43 asks: "but what if the formula hides two components?" This is the correct next question. It takes the tautology (reading depth = GR) and looks for the seam where they could come apart.

The five tests are well-chosen. Each probes a different aspect of the decomposition. The nuclear clock test is the crown jewel — it's the only laboratory-scale test that could produce a result distinguishable from standard GR within a decade. The other four are archival or statistical, which means they can be attempted now without waiting for new hardware.

The three-scenario structure (U, L, M) is clean and covers the logical space. The decomposition matrix (Section IV) is the paper's most useful table — it tells a reader exactly what each test constrains and why the five tests together are more powerful than any one alone.

The kill conditions are specific and falsifiable. Each names a measurement, a threshold, and a consequence. This is the standard the series has maintained since the first kill switches.

### What Needs Work

**The T/R decomposition is underdefined.** The plan says Component T is "a monotonic integer process" and Component R is "a spatial structure." But it doesn't give a formula for how they combine. Is the observed dilation T × R? T + R? f(T, R)? Without a combining law, the "decomposition" is a verbal framework, not a computational one. The paper needs an equation, even if it's parameterized:

dτ/dt = √(1 − 2Φ/c²) × [1 + ε_sector × δΦ_sector/c²]

where ε_sector is the sector-dependent reading depth correction and δΦ_sector is the deviation from the universal potential for a given force sector. This makes the prediction concrete: Test 1 measures ε_sector. If ε = 0, reading depth is sector-blind. If ε ≠ 0, it's sector-dependent.

Without this formula, the derivation functions have nothing to compute. The plan lists five derivation functions but doesn't give the formulas they implement. The `clock_sector_splitting_v0` function needs an equation relating the β coefficient ratio to the sector splitting. What is that equation? The plan says "the ratio of strong to electromagnetic coupling running rates is ~10, suggesting a sector splitting of order 10 × (Φ/c²) ~ 10⁻⁸." That's a dimensional argument, not a derivation. The paper needs the actual formula or it's hand-waving.

**Scenario U is internally inconsistent as stated.** The plan says Scenario U is "Universal tick, all dilation is R" and predicts "possible disagreement" between nuclear and optical clocks. But then it also says the disagreement depends on "the transformation law difference between strong and electromagnetic sectors across the Earth's gravitational boundary." This implicitly assumes the reading depth IS sector-dependent — which is the defining feature of Scenario M, not Scenario U. 

The issue: if all dilation is R (reading depth), and R is sector-dependent, then calling it "universal tick" is misleading. The tick is universal but the readings aren't. This is Scenario M with the T component set to zero. The plan needs to either rename Scenario U to something that captures "universal tick, sector-dependent readings" or split it into U-blind (readings sector-independent) and U-sector (readings sector-dependent). The current naming conflates universality of the tick with universality of the reading.

Suggested fix: four scenarios, not three.

| Scenario | Tick | Readings | Nuclear vs optical |
|---|---|---|---|
| GR (standard) | One coordinate | Universal coupling | Exact agreement |
| U-blind | Universal tick | Sector-independent R | Exact agreement |
| U-sector | Universal tick | Sector-dependent R | Disagreement from R |
| L-local | Local tick rates | No R dependence | Exact agreement |

This makes the prediction space cleaner. GR and U-blind are experimentally indistinguishable (both predict exact agreement). U-sector is the only scenario that predicts nuclear/optical disagreement. L-local predicts agreement but through a different mechanism (local ticks, not universal coupling). The nuclear clock test distinguishes U-sector from everything else.

**Test 2 (pulsar gradient) needs sharper predictions.** The plan says NANOGrav residuals could show "structure-correlated vs density-correlated patterns." This is vague. What specific correlation coefficient or statistic would distinguish them? The plan needs to specify: compute the Pearson correlation between timing residual and (a) galactocentric radius, (b) local DM column density, (c) spiral arm membership flag, (d) distance from galactic plane. If (c) is significant and (a) is not, that's structure-dependent R. If (a) is significant and (c) is not, that's smooth potential (standard GR). The plan should state these specific tests.

Also: the NANOGrav collaboration has published their own analyses of spatial correlations in timing residuals (the Hellings-Downs curve for the gravitational wave background). The plan needs to address how to separate a reading depth gradient from the already-detected stochastic gravitational wave background. These are different signals but they both produce spatially correlated timing residuals.

**Test 3 (Voyager) is the weakest test.** The estimated boundary step is 10⁻¹² (0.3 mm/s Doppler), and the Voyager tracking sensitivity is ~0.1 mm/s. This is a factor of 3 margin — barely detectable even if the effect exists. More importantly, the heliopause crossing produced a wealth of plasma physics signatures (energetic particle flux changes, magnetic field rotation, plasma density jump) that dominate the Doppler signal. Extracting a 0.3 mm/s step from a dataset contaminated by plasma effects at the 1-10 mm/s level is extremely challenging.

The plan acknowledges this ("near the limit of current Voyager tracking") but doesn't address the systematic contamination. Suggestion: downgrade this from a standalone test to a "if Tests 1-2 show positive results, look here for confirmation" supporting check. It shouldn't carry the same weight as the nuclear clock test.

**Test 4 (G scatter) has a serious confound.** The plan proposes regressing published G values against laboratory gravitational potential. But the G measurements use radically different techniques (torsion balance, beam balance, atom interferometry, servo-controlled pendulum). The technique-dependent systematics are much larger than any plausible reading depth effect. A correlation between G and altitude could easily be a correlation between G and "which country's metrology lab uses which technique" — European labs at one altitude, US labs at another, Chinese labs at a third.

The plan says "a positive correlation would need to survive correction for technique-dependent systematics" but doesn't specify how to do this correction with only ~15 data points and ~5 technique categories. With 15 points and 5 technique dummies, you have 10 degrees of freedom for the environmental regression. This is marginal statistics at best.

Suggestion: frame this test honestly. The G scatter is a known puzzle. The reading depth interpretation offers one possible explanation. But the test is underpowered with existing data. The honest statement is: "if future G measurements are performed at deliberately varied gravitational potentials using the same technique, this test becomes decisive. With existing heterogeneous data, it is suggestive at best."

**Test 5 (α drift) is mostly existing physics.** Varying fundamental constants is a well-established research program (Uzan 2011, Martins 2017). The connection to "geometric tick effects" is novel but thin. The plan says each Planck tick might deform boundaries by a tiny amount, accumulated over cosmic time. But the per-tick deformation is constrained to < 10⁻⁶⁷ per tick — a number so small it has no physical content. The test is really "does α vary?" which is an existing question with existing experiments. The reading depth framing adds the interpretation but not the measurement program.

Suggestion: keep the test but frame it as "what existing α variation constraints tell us about the geometric tick hypothesis" rather than proposing new observations. The ANDES spectrograph is already planned regardless of this paper. The paper's contribution is interpreting existing and future constraints through the T/R decomposition lens.

**The paper has no derivations that produce testable numbers.** The plan lists five derivation functions but four of them produce predictions that depend on unknown parameters (sector coupling ratio, boundary transformation law, geometric deformation rate). Only Test 1 has a concrete dimensional estimate (sector splitting ~ 10 × Φ/c² ~ 10⁻⁸). The other four are "compute the constraint on an unknown parameter from existing data."

This is a significant departure from the HOWL methodology. Every previous paper produces numbers that can be checked against measurement. PHYS-43 produces predictions that are parameterized — they say "if the parameter is X, the observation would be Y." This is legitimate physics (it's how BSM phenomenology works) but it's weaker than "we predict 42.98 arcsec/century and the measurement is 42.9799."

The paper should be honest about this distinction. It's a roadmap paper, not a results paper. The derivations constrain parameter space, they don't predict observables.

### Structural Suggestions

**Lead with Test 1.** The nuclear clock test is the one that matters. It's the only test with a concrete prediction (sector splitting ~ 10⁻⁸), a specific experimental timeline (3-5 years), and a clean kill condition. The other four tests are supporting evidence. The paper should make this hierarchy clear: Test 1 is the decisive test, Tests 2-5 are complementary constraints.

**Drop the "Component T / Component R" naming.** It's confusing because T looks like it stands for "time" and R for something else, but both are aspects of time. Suggest: "tick component" (universal clock rate) and "depth component" (position-dependent reading). Or just use the scenario labels (U-blind, U-sector, L-local) consistently.

**Add a Section 0: What PHYS-42 Established.** The paper assumes the reader knows the GR mega-experiment results. A one-page summary of PHYS-42 (18 tests, 7 PASS, 1 FAIL, Mercury at 2.8 ppb, reading depth = GR confirmed) sets the stage. The decomposition question only makes sense if you first establish that the sum (T+R) is confirmed.

**The connection to β coefficients in Test 1 needs to be worked out explicitly.** The plan says the sector splitting depends on "the ratio of β function coefficients (strong vs electromagnetic) times the local Φ/c²." This is the most important formula in the paper. It connects the GR domain (Φ/c²) to the GUT domain (β coefficients) through the reading depth interpretation. If this formula works — if the sector splitting is literally β_s/β_em × Φ/c² — then it's the first quantitative prediction that connects gravity to gauge physics through integers. This is potentially more important than the GR mega-experiment. The plan buries it in a bullet point. It should be the paper's central equation.

---

## Supporting Tables

### Table S.1: The Four Scenarios (Revised from Three)

| Scenario | Tick | Reading depth | Clock sector dependence | Pulsar residuals | G scatter | α drift | Distinguishing test |
|---|---|---|---|---|---|---|---|
| GR (standard) | One coordinate, universal coupling | Not a separate component | All clocks agree | No structure residuals | No environmental correlation | Possible (unrelated mechanism) | None needed — default |
| U-blind | Universal Planck counter | Exists but sector-independent | All clocks agree | No structure residuals (smooth Φ) | No environmental correlation | No drift | Indistinguishable from GR at current precision |
| U-sector | Universal Planck counter | Sector-dependent (β-weighted) | Nuclear ≠ optical by ε × Φ/c² | Structure-correlated residuals | Possible correlation | No drift (R is static) | Test 1: nuclear vs optical clock |
| L-local | Local tick rates vary with boundary environment | Not a separate component | All clocks agree (same local tick) | Density-correlated residuals | Possible (technique confound) | Possible (tick rate changes with expansion) | Test 2: residual pattern (structure vs density) |

### Table S.2: Sector Splitting Estimate for Test 1

| Quantity | Value | Source | Role in prediction |
|---|---|---|---|
| Φ/c² at Earth surface | 6.961 × 10⁻¹⁰ | PHYS-42 derivation | Base gravitational reading depth |
| β₃ (SU(3), CD-modified) | −20/3 = −6.667 | Pool: beta_modified_su3_total_v0 | Strong force running rate |
| β₁ (U(1), CD-modified) | 25/6 = 4.167 | Pool: beta_modified_u1_total_v0 | EM force running rate (GUT normalized) |
| Ratio β₃/β₁ | (−20/3)/(25/6) = −8/5 = −1.6 | Exact from pool Fractions | Sector coupling ratio |
| |β₃/β₁| | 8/5 = 1.6 | Exact | Sector asymmetry factor |
| ε_sector (dimensional estimate) | |β₃/β₁| × Φ/c² ~ 1.1 × 10⁻⁹ | This paper | Predicted sector splitting |
| Required clock sensitivity | 10⁻¹⁹ fractional frequency | PTB/JILA projections | 10× below ε_sector — detectable |

The critical observation: the sector splitting ε ~ 10⁻⁹ is three orders of magnitude above the projected clock comparison sensitivity of 10⁻¹⁸ to 10⁻¹⁹. If the β-ratio formula is correct, the effect is detectable with planned hardware. If the formula overcounts by a factor of 100 (e.g., the correct formula involves β² not β), the effect is still at 10⁻¹¹, two orders above detection. Only if the formula overcounts by > 10⁵ is the effect undetectable.

This is why Test 1 is decisive: the predicted magnitude is large enough that non-detection at planned sensitivity would kill sector-dependent reading depth definitively.

### Table S.3: Existing Data for Each Test

| Test | Data source | Status | Access | Key limitation |
|---|---|---|---|---|
| 1. Nuclear vs optical | Th-229 nuclear clock (PTB, JILA, TU Wien) | Under development | Not yet available | Clock not yet operational at required precision |
| 2. Pulsar gradient | NANOGrav 15-year dataset (Agazie et al. 2023) | Published | Public (zenodo) | GW background signal already detected — must separate |
| 3. Voyager heliopause | NASA DSN tracking data, Voyager 1 (2012) + Voyager 2 (2018) | Archived | Request from PDS | Plasma contamination at boundary crossing |
| 4. G scatter | CODATA G compilation (Mohr et al. 2016) + individual papers | Published | Literature | Only ~15 measurements, 5 technique categories |
| 5. α drift | ESPRESSO/VLT (Murphy et al. 2022), Keck+VLT (Webb et al. 2011) | Published | Literature + ESO archive | Webb dipole unresolved, ESPRESSO limited z range |

### Table S.4: Timeline — When Each Test Could Produce a Result

| Test | Earliest result | Decisive result | What triggers decision |
|---|---|---|---|
| 1. Nuclear vs optical | 2028-2029 (first clock comparison) | 2030-2032 (10⁻¹⁹ sensitivity) | Th-229 clock operational at PTB or JILA |
| 2. Pulsar gradient | 2026 (reanalysis of existing data) | 2030 (NANOGrav 25-year) | Sufficient pulsar count for structure correlation |
| 3. Voyager heliopause | 2026 (archival analysis) | 2026 (data already exists) | Someone does the analysis |
| 4. G scatter | 2026 (regression on existing data) | 2030+ (same-technique G at varied altitudes) | New G measurement campaign at varied potentials |
| 5. α drift | 2026 (ESPRESSO constraints published) | 2035+ (ANDES on ELT) | ANDES first light and quasar survey |

### Table S.5: Kill Switch Refinement

| Kill switch | Previous (PHYS-41/42) | Refined (PHYS-43) | What changes |
|---|---|---|---|
| Nuclear vs optical agree | "Nuclear clock vs optical clock comparison shows disagreement beyond GR" — binary | "Nuclear and optical clocks agree to 10⁻¹⁹ at ≥ 2 gravitational potentials" — quantified threshold | Adds precision requirement and multi-potential condition |
| NANOGrav no gradient | "No correlation with galactocentric radius" — vague | "No timing residual correlation with spiral arm membership at 10 ns level in NANOGrav 25-year data" — specific statistic | Distinguishes structure correlation from density correlation |
| G scatter no pattern | "G measurements show no lab environment correlation" — vague | "Regression of G vs laboratory Φ/c² shows |r| < 0.3 after technique correction with ≥ 20 measurements" — specific statistic | Adds sample size requirement and technique correction |
| Voyager no step | "No reading depth anomaly at heliopause" — vague | "Voyager 1+2 Doppler residuals at heliopause show no step > 0.1 mm/s after plasma correction" — specific threshold | Adds plasma correction requirement |
| α drift zero | Not previously specified | "ANDES measures |Δα/α| < 10⁻⁸ at z = 1-5 with no spatial dipole" — specific | New kill switch for geometric tick hypothesis |

### Table S.6: What Each Test Kills (If Null)

| Test | Null result | What it kills | What survives |
|---|---|---|---|
| 1. Nuclear = optical at 10⁻¹⁹ | Sector-dependent R below 10⁻¹⁹ | U-sector scenario at Earth gravity | U-blind, L-local, GR standard. Reading depth may still exist but is sector-blind |
| 2. No structure residuals at 10 ns | Boundary structure R below galactic noise | Galactic-scale boundary effects | Local boundary effects (heliosphere, Hill sphere). Smooth R survives |
| 3. No Voyager step at 0.1 mm/s | Heliosphere boundary R below 10⁻¹² | Heliospheric boundary reading step | Other boundaries (stronger). Heliosphere may be too weak |
| 4. No G correlation at |r| < 0.3 | G as reading below 500 ppm | G varies with reading depth at detectable level | G may still be a reading but variation is below current scatter |
| 5. |Δα/α| < 10⁻⁸ at z = 1-5 | Geometric tick deformation above 10⁻⁶⁹/tick | Tick has geometric effect on boundaries | Geometric effect exists but is astronomically small — effectively unfalsifiable, should be shelved |

### Table S.7: What Each Test Confirms (If Positive)

| Test | Positive result | What it confirms | Immediate consequence |
|---|---|---|---|
| 1. Nuclear ≠ optical beyond GR | R is sector-dependent | Reading depth is NOT just a name change — it's new physics | Nobel-class discovery. Equivalence principle violation. Entire framework validated as physical, not interpretive |
| 2. Structure-correlated residuals | R has boundary structure | Galactic soliton boundaries affect clock rates | DM distribution affects timing. Connection to toroidal DM model |
| 3. Voyager Doppler step at heliopause | R changes across soliton boundaries | Heliosphere is a reading depth boundary | First measurement of a soliton boundary reading step |
| 4. G correlates with lab environment | G is a reading, not a constant | Newton's "constant" is position-dependent | Metrology revolution. G measurements need environmental correction |
| 5. α drifts with z | Tick has geometric consequences | Each Planck step deforms boundary structure | Fundamental cosmological discovery. Constants evolve |

### Table S.8: The Formula Gap — What PHYS-43 Needs to Derive

| Formula needed | Current status | What's missing | Priority |
|---|---|---|---|
| ε_sector = f(β_i, Φ/c²) | Dimensional estimate: |β₃/β₁| × Φ/c² | Rigorous derivation from the boundary transformation law | CRITICAL — this is the paper's central prediction |
| Boundary step ΔΦ at heliopause | Order estimate: (v_sw/c)² ~ 10⁻¹² | Soliton boundary matching condition | LOW — Voyager test is weak |
| G variation δG/G = g(Φ/c²) | Not derived | Relationship between G and reading depth | MEDIUM — needed for Test 4 regression |
| α drift rate dα/dN | Constrained to < 10⁻⁶⁷/tick | Geometric deformation model | LOW — unfalsifiable at this magnitude |
| Pulsar timing gradient ΔT/T = h(r, structure) | Not derived | Galactic boundary reading depth model | MEDIUM — needed for Test 2 predictions |

The CRITICAL gap is the sector splitting formula. Without it, Test 1 has a dimensional estimate but not a derivation. With it, Test 1 has a concrete prediction from pool constants (β coefficients × Φ/c²) that can be checked against future clock data. This formula connects the GUT domain (β coefficients from the Cabibbo Doublet) to the GR domain (Φ/c² from the mega-experiment) through the reading depth interpretation. If the formula works, it's the first quantitative prediction linking gravity to gauge physics through the soliton boundary structure.

### Table S.9: Comparison to Existing Equivalence Principle Tests

| Test | What it tests | Current best | PHYS-43 adds |
|---|---|---|---|
| Lunar Laser Ranging (Nordtvedt) | Gravitational self-energy falls same as matter | η = (−0.8 ± 1.3) × 10⁻¹³ | Nothing — different aspect of EP |
| MICROSCOPE (Touboul 2022) | WEP: Be vs Ti free fall | η = (−1.5 ± 2.8) × 10⁻¹⁵ | Nothing — tests WEP, not clock rates |
| Atom interferometry (Asenbaum 2020) | Rb-87 vs Rb-85 redshift | Δf/f < 10⁻¹² | Similar concept but same force sector |
| Optical clock comparison (Bothwell 2022) | Sr vs Sr at different heights | Δf/f at 10⁻¹⁸ | Same force sector — doesn't test sector dependence |
| **PHYS-43 Test 1** | **Nuclear vs optical at same potential** | **Not yet performed** | **First cross-sector clock comparison for EP** |

The key distinction: all existing equivalence principle tests compare objects of the same type (same force sector) at different gravitational potentials. PHYS-43 Test 1 compares objects of different types (different force sectors) at the same potential. This is a qualitatively different test. If the equivalence principle is exact, all clock types agree. If reading depth is sector-dependent, they disagree. No existing test probes this.

### Table S.10: Connection to Existing HOWL Pool

| PHYS-43 quantity | Pool source | Key | How it enters |
|---|---|---|---|
| Φ/c² at Earth surface | PHYS-42 derivation output | result_earth_phi_over_c2_v0 | Base potential for Test 1 splitting |
| β₃ (CD-modified) | Pool value | beta_modified_su3_total_v0 | Strong sector running rate for sector ratio |
| β₁ (CD-modified) | Pool value | beta_modified_u1_total_v0 | EM sector running rate for sector ratio |
| β₂ (CD-modified) | Pool value | beta_modified_su2_total_v0 | Weak sector (not in Test 1 but available) |
| GM_S | Pool value | gr_gm_sun_v0 | Heliopause potential for Test 3 |
| G | Pool value | gr_newton_g_v0 | Base for Test 4 regression |
| H₀, Ω_m, Ω_DE | Pool values | cosmo_* | Expansion history for Test 5 |
| α_em | Pool value | coupling_alpha_em_inverse_v0 | Current α for drift comparison |
| Planck time | PHYS-42 derivation | result_planck_time_from_constants_v0 | Tick step size for geometric deformation rate |

The paper draws from 3 pool domains: GR (PHYS-42 outputs), GUT (β coefficients), and cosmology (expansion parameters). This is the first paper that explicitly uses outputs from the GR domain as inputs to a new prediction, closing the loop between the gravitational hierarchy and the integer structure.
