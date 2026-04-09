# HOWL-PHYS-43-2026: PLAN

## Separating Clock from Reading: Five Tests That Decompose Time Dilation

---

### REGISTRY

**Paper:** HOWL-PHYS-43-2026
**Series Path:** PHYS-41 (reading depth thesis) → PHYS-42 (18 GR confirmations) → PHYS-43 (decomposition tests)
**Depends on:** PHYS-42 results (GR domain confirmed), PHYS-41 kill switches (now refined)
**Status:** Plan — awaiting agreement before writing

---

### I. THESIS

PHYS-42 confirmed that the GR dilation formula works across 18 orders of magnitude. But the formula is degenerate — it measures the sum of two potentially distinct contributions:

**Component T:** The tick count. A monotonic integer process. May be universal or local. The Planck time is the step size. Each tick may have geometric consequences on boundaries.

**Component R:** The reading depth. A spatial structure. Position within the nested soliton hierarchy. Computable in frozen time. Determines local values of physical constants through boundary transformation laws.

Standard GR says: there is only one component. Spacetime curvature couples universally to all physics. dτ/dt = √(1 − 2Φ/c²). Done.

RUM says: there may be two components. The observed dilation is T + R, and the five tests in this paper make different predictions depending on the T/R decomposition.

The paper does not claim to know the decomposition. It identifies five measurements where the decomposition matters, states what each measurement would show under three scenarios (pure T, pure R, mixed), and specifies the experimental sensitivity required to distinguish them.

---

### II. THE THREE SCENARIOS

**Scenario U (Universal tick, all dilation is R):**
One counter. Same tick everywhere. All observed dilation comes from reading depth — the spatial structure of boundaries changes the local readings of physical constants, which changes oscillation frequencies of clocks. The tick is the same everywhere but the readings differ.

Predictions: All clock types at the same potential agree exactly (equivalence principle holds perfectly). No pulsar timing trend with galactocentric radius beyond the known potential gradient. No α drift over cosmic time. Planck-scale discreteness exists but produces no dispersion (the lattice is in the readings, not in the ticks).

**Scenario L (Local ticks, all dilation is T):**
Many counters. Each location ticks at its own rate determined by local boundary structure. Readings are the same everywhere — physical constants do not depend on depth. The tick rate varies, and this is what clocks measure.

Predictions: All clock types at the same potential agree exactly (they all count local ticks). No sector dependence. But possible tick-rate gradients across large-scale structure that do not track the gravitational potential exactly, because the tick rate depends on the full boundary environment, not just the local Φ/c².

**Scenario M (Mixed — both T and R contribute):**
The tick may be universal or local, AND readings vary with depth. The observed dilation has contributions from both. The critical consequence: different clock types may disagree, because different clocks probe different reading sectors, and the reading contribution is sector-dependent while the tick contribution is universal.

Predictions: Nuclear and optical clocks at the same potential may disagree at a level set by the sector-dependent reading depth difference. Pulsar timing may show residuals. α may drift.

---

### III. THE FIVE TESTS

#### Test 1: Nuclear vs Optical Clock (Sector Decomposition)

**What:** Compare a thorium-229 nuclear clock and a strontium-87 optical lattice clock in the same gravitational potential, at the same location, over extended integration time.

**Why this decomposes T from R:** The tick contribution (T) is sector-blind — it affects all oscillation frequencies equally. The reading contribution (R) is sector-dependent — electromagnetic readings and strong-force readings may shift by different amounts across a gravitational boundary. If the two clocks agree beyond their combined measurement uncertainty, the reading contribution is either zero or sector-independent (indistinguishable from pure T). If they disagree, reading depth is sector-dependent and R ≠ 0.

**Predictions by scenario:**
- Scenario U: Disagree possible. The reading depth for nuclear transitions (probing the strong force at ~1 fm) differs from the reading depth for electronic transitions (probing QED at ~0.1 nm). The disagreement magnitude depends on the transformation law difference between strong and electromagnetic sectors across the Earth's gravitational boundary. Order of magnitude estimate: the ratio of strong to electromagnetic coupling running rates is ~10, suggesting a sector splitting of order 10 × (Φ/c²) ~ 10 × 7 × 10⁻¹⁰ ~ 10⁻⁸. This is within reach of next-generation clock comparisons at 10⁻¹⁹ fractional frequency uncertainty.
- Scenario L: Agree exactly. The local tick rate is the same for all physics at one location. No sector dependence.
- Scenario M: Disagree at a level that separates the R contribution from noise. The disagreement magnitude directly measures the R component.

**Required sensitivity:** 10⁻¹⁹ fractional frequency or better. Current optical clocks achieve 10⁻¹⁸. Thorium-229 nuclear clock is under development at PTB, JILA, TU Wien. Expected 3-5 years to clock-quality interrogation.

**Kill condition for reading depth:** If nuclear and optical clocks agree to 10⁻¹⁹ at multiple gravitational potentials, the sector-dependent R contribution is below 10⁻¹⁹, which constrains it to < 0.1% of the total dilation at Earth's surface. Reading depth as a sector-dependent phenomenon would be effectively dead at laboratory scales.

**DATA-7 experiment:** `experiment_clock_sector_decomposition_v0`. Derivation computes the expected sector splitting from the ratio of β function coefficients (strong vs electromagnetic) times the local Φ/c². Comparison: predicted splitting vs measurement (when available). Currently: derivation produces the prediction, comparison stores it as INFO awaiting experimental data.

---

#### Test 2: Pulsar Timing vs Galactocentric Radius (Gradient Decomposition)

**What:** Analyze the ensemble of millisecond pulsars timed by NANOGrav, EPTA, PPTA, and IPTA as a function of their galactocentric radius. After subtracting the known galactic gravitational potential gradient (from the galactic mass model), look for residual timing trends that correlate with position in the galactic hierarchy.

**Why this decomposes T from R:** The gravitational potential gradient across the galaxy is well-modeled and produces a known dilation gradient. This is the standard GR prediction. Reading depth adds a possibility: the boundary structure of the galaxy (the toroidal DM distribution, the spiral arm density waves, the central bar) may produce additional reading depth gradients that do not follow the smooth 1/r potential. These would appear as residuals after subtracting the Newtonian + GR potential model.

**Predictions by scenario:**
- Scenario U: Residuals possible. If reading depth depends on boundary structure (not just potential), the galactic boundary geometry (torus, spiral, bar) imprints structure on the readings. Pulsars inside a spiral arm have different boundary nesting than pulsars between arms, even at the same galactocentric radius. This produces timing residuals that correlate with galactic structure, not with radius alone.
- Scenario L: Residuals possible but different pattern. If the tick rate depends on the full local boundary environment, pulsars in dense environments tick differently from pulsars in voids, but the pattern tracks local density, not sector-dependent readings.
- Scenario M: Residuals from both sources, potentially distinguishable by their spatial pattern (structure-correlated vs density-correlated).

**Required sensitivity:** NANOGrav 15-year dataset has timing residuals at the ~100 ns level for the best pulsars. The galactic potential gradient across the pulsar ensemble produces timing differences of order (ΔΦ/c²) × T_obs ~ 10⁻⁶ × (15 yr) ~ 500 μs. The residuals after model subtraction are at the 100 ns level, which is 0.02% of the signal. Additional structure at the 10 ns level (0.002% of signal) is the target.

**Kill condition:** If NANOGrav 25-year data shows no residual correlation with galactic structure (spiral arm membership, local density, boundary nesting level) at the 10 ns level, the boundary-structure component of reading depth is below the galactic noise floor. This does not kill reading depth entirely (it could still be present at smaller scales) but it kills the claim that galactic boundary structure affects readings.

**DATA-7 experiment:** `experiment_pulsar_gradient_v0`. Derivation computes the expected potential gradient across a sample of NANOGrav pulsars using the galactic mass model from the pool, predicts the GR timing gradient, and computes the residual pattern expected from boundary-structure reading depth. Inputs: pulsar positions, galactic mass model, DM amplification factor (22/13)π. Comparison: predicted gradient vs NANOGrav published timing model residuals (when available as public data).

---

#### Test 3: Voyager Doppler at the Heliopause (Boundary Crossing)

**What:** Analyze the Doppler tracking data from Voyager 1 and Voyager 2 as they crossed the heliopause (~120 AU, 2012 and 2018 respectively). Look for anomalous frequency shifts that coincide with the boundary crossing — shifts that are not explained by the known deceleration, solar wind pressure, and thermal radiation pressure.

**Why this decomposes T from R:** The heliopause is a physical boundary — the transition from the solar wind (solar soliton interior) to the interstellar medium (galactic soliton interior). If reading depth changes across soliton boundaries, there should be a step change in the Doppler frequency as the spacecraft crosses from one boundary domain to another. Standard GR predicts no such step — the gravitational potential changes smoothly through the heliopause. The boundary is in the plasma, not in the metric.

**Predictions by scenario:**
- Scenario U: Step change possible. The reading depth at 120 AU in the solar soliton interior differs from the reading depth at 120 AU in the galactic soliton interior, because the boundary nesting level changes. The step magnitude depends on the heliospheric boundary transformation law. Order of magnitude: if the heliopause boundary contributes a reading shift of order (v_sw/c)² ~ (400 km/s / c)² ~ 10⁻⁶ × 10⁻⁶ ~ 10⁻¹², this would produce a Doppler shift of ~10⁻¹² (0.3 mm/s). This is near the limit of current Voyager tracking (~0.1 mm/s sensitivity at S-band).
- Scenario L: No step. The tick rate changes smoothly with the gravitational potential, which has no discontinuity at the heliopause.
- Scenario M: Step from R, smooth change from T. The step magnitude directly measures the R contribution from the heliospheric boundary.

**Required sensitivity:** 0.1 mm/s Doppler precision at S-band (2.3 GHz) over the heliopause crossing period (~months). The Voyager tracking data exists. The analysis is archival — no new observation required.

**Kill condition:** If Voyager Doppler data across the heliopause shows no anomalous step at the 0.1 mm/s level, the heliospheric boundary reading depth contribution is below detection. This does not kill reading depth at other boundaries (the heliosphere may be too weak a boundary) but it constrains the magnitude of boundary effects.

**Existing anomaly:** The Pioneer anomaly (anomalous sunward acceleration of ~8.7 × 10⁻¹⁰ m/s², later attributed to thermal radiation pressure) was initially consistent with a boundary-related effect. The thermal explanation (Turyshev et al. 2012) resolved the Pioneer case, but the analysis methodology developed for Pioneer can be applied to Voyager heliopause data.

**DATA-7 experiment:** `experiment_voyager_boundary_v0`. Derivation computes the expected smooth GR Doppler shift at 120 AU from GM_S/(r·c²), and the expected boundary step from the heliospheric reading depth model. Inputs: GM_S, heliopause distance, solar wind velocity (from pool). Comparison: predicted smooth + step vs Voyager published tracking residuals (archival data).

---

#### Test 4: G Scatter vs Laboratory Environment (Depth Variation)

**What:** Analyze the published compilation of Newton's constant G measurements (CODATA collection, ~15 experiments since 1982) as a function of the laboratory's gravitational environment — altitude, latitude, proximity to large mass concentrations (mountains, ocean trenches), local geological density.

**Why this decomposes T from R:** Newton's constant G appears in the reading depth formula: Φ/c² = GM/(Rc²). If G itself is a reading — a value that depends on position in the hierarchy — then measurements of G at slightly different reading depths would give slightly different values. The published G measurements disagree by up to 500 ppm, far exceeding individual uncertainties of 10-50 ppm. The standard explanation is underestimated systematics. The reading depth explanation is that G varies with depth.

**Predictions by scenario:**
- Scenario U: G scatter correlates with reading depth. Laboratories at higher altitude (shallower depth) measure slightly different G from laboratories at lower altitude (deeper depth). The correlation is with Φ/c², which varies by ~10⁻⁹ across typical laboratory altitude differences. If G changes proportionally to Φ/c², the variation would be G × 10⁻⁹ ~ 10⁻⁹ G, which is ~0.7 ppb — far below the 500 ppm scatter. Reading depth alone cannot explain the G scatter. But if G has a stronger boundary dependence (e.g., depends on the local soliton boundary nesting level rather than just the smooth potential), the variation could be larger.
- Scenario L: G scatter does not correlate with gravitational environment. Local tick rates differ but G is a universal constant. Scatter is from systematics.
- Scenario M: Partial correlation. The R component produces an environment-dependent term. The T component does not. The correlation strength measures R/T.

**Required analysis:** Regression of published G values against laboratory gravitational potential, altitude, latitude, local crustal density. The data exists. The analysis is statistical — no new measurement required. The challenge is that G measurements use different techniques (torsion balance, beam balance, cold atom, servo-controlled) with different systematic profiles. A positive correlation would need to survive correction for technique-dependent systematics.

**Kill condition:** If no correlation between G values and laboratory gravitational environment survives technique-dependent correction, reading depth variation of G is below the 500 ppm scatter level. G scatter is then fully attributable to experimental systematics.

**DATA-7 experiment:** `experiment_g_scatter_v0`. Derivation computes the expected G variation across laboratory locations from the reading depth model. Inputs: laboratory coordinates (from published papers), local gravitational potential model, crustal density model. Comparison: predicted variation vs observed scatter. Currently: derivation can compute the potential at each lab location, comparison stores it as INFO.

---

#### Test 5: Cosmological α Drift (Tick Geometry)

**What:** Compare the fine structure constant α measured at cosmological distances (quasar absorption spectra at z = 1-4, corresponding to 7-12 billion years ago) with the local laboratory value.

**Why this decomposes T from R:** If each Planck tick has a geometric effect on boundaries — expanding or deforming the soliton hierarchy slightly — then accumulated ticks produce a drift in reading depth structure over cosmic time. Physical constants measured at earlier epochs (fewer accumulated ticks) would differ from current values. This is a pure test of the geometric tick hypothesis (Component T with geometric consequences). Reading depth without geometric tick effects (pure Scenario U with no boundary drift) predicts no α change.

**Predictions by scenario:**
- Scenario U (no geometric tick): No α drift. Reading depth is a spatial structure determined by boundary geometry. The geometry does not change with tick count. Constants are the same at all epochs.
- Scenario U (with geometric tick): α drifts. Each tick deforms boundaries by a small amount. Over ΔN ticks (corresponding to Δt cosmic time), the accumulated deformation shifts α. The drift rate dα/dt depends on the geometric effect per tick, which is unknown. The constraint from quasar spectra (Δα/α < 10⁻⁶ at z ~ 2) requires the per-tick drift to be < 10⁻⁶ / (10⁶¹ ticks from z=2 to now) = 10⁻⁶⁷ per tick. This is an extraordinarily small number but is not zero.
- Scenario L: α drifts if local tick rates were different in the past (e.g., if the cosmic expansion changes the local tick rate). The drift pattern depends on the expansion history, which is well-measured.
- Scenario M: α drifts from the geometric tick effect. The drift rate directly measures the geometric deformation per tick.

**Required sensitivity:** Current best constraints: Webb et al. (Keck+VLT) report possible spatial dipole in Δα/α at the 10⁻⁶ level. Murphy et al. (ESPRESSO/VLT) constrain Δα/α < 10⁻⁶ at z ~ 1. Next-generation spectrographs (ANDES on ELT, expected 2030s) aim for 10⁻⁸.

**Kill condition:** If ANDES measures Δα/α = 0 at 10⁻⁸ across z = 1-5, the geometric tick effect is below 10⁻⁸/(10⁶¹ ticks) = 10⁻⁶⁹ per tick. This does not prove geometric tick effects are zero, but it pushes them below any foreseeable observational consequence. The geometric tick hypothesis becomes unfalsifiable at that point and should be shelved.

**Existing anomaly:** The Webb et al. spatial dipole in Δα/α, if confirmed, would be inconsistent with all three scenarios as stated — none of them predict a spatial dipole. A dipole would require additional structure (e.g., the universe has a preferred direction, which would be extraordinary). The ESPRESSO results do not confirm the dipole. The status is unresolved.

**DATA-7 experiment:** `experiment_alpha_drift_v0`. Derivation computes the expected α drift per unit redshift from the geometric tick model, using the expansion history (H(z) from Planck cosmology in the pool) and a parameterized geometric deformation rate. Inputs: H₀, Ω_m, Ω_DE, Planck time, parameterized drift rate. Comparison: predicted drift vs published quasar absorption constraints. Currently: the drift rate parameter is unknown, so the derivation computes the constraint on the parameter from existing data.

---

### IV. THE DECOMPOSITION MATRIX

| Test | Probes | U predicts | L predicts | M predicts | Timeline |
|---|---|---|---|---|---|
| 1. Nuclear vs optical clock | R sector dependence | possible disagreement | exact agreement | disagreement = R | 3-5 yr |
| 2. Pulsar gradient | R boundary structure | structure residuals | density residuals | both patterns | archival + 5 yr |
| 3. Voyager heliopause | R boundary step | Doppler step | no step | step = R | archival now |
| 4. G scatter | R depth variation | correlation | no correlation | partial correlation | archival now |
| 5. α drift | T geometric effect | no drift (or drift) | possible drift | drift = T geometry | 5-10 yr |

The five tests are complementary. Tests 1, 3, 4 primarily probe the R component (reading depth structure). Test 5 primarily probes the T component (tick geometry). Test 2 probes both. No single test fully decomposes T from R, but the combination constrains the decomposition from multiple directions.

---

### V. DERIVATIONS NEEDED

Five new derivation functions, one per test. All read from pool. No hardcoded constants.

| Derivation | Inputs from pool | New values needed | Key output |
|---|---|---|---|
| `clock_sector_splitting_v0` | α_em, α_s, β coefficients (both sectors), Φ_earth/c² | sector coupling ratio | `result_sector_splitting_predicted_v0` |
| `pulsar_gradient_model_v0` | galactic mass model, DM amplification, pulsar positions | galactic mass model params, pulsar catalog | `result_gradient_residual_pattern_v0` |
| `voyager_boundary_step_v0` | GM_S, heliopause distance, v_sw | heliosphere boundary params | `result_boundary_step_doppler_v0` |
| `g_scatter_prediction_v0` | G, lab positions, local potentials | laboratory coordinate catalog | `result_g_variation_predicted_v0` |
| `alpha_drift_constraint_v0` | H₀, Ω_m, Ω_DE, t_P, current α | cosmological parameters (already in pool) | `result_drift_rate_constraint_v0` |

New values files needed:

| File | Contents | Count |
|---|---|---|
| `values_heliosphere_v0.json` | heliopause distance, solar wind velocity, heliosheath thickness | ~5 nodes |
| `values_galactic_model_v0.json` | galactic mass model parameters, bulge/disk/halo masses, scale lengths | ~10 nodes |
| `values_g_measurements_v0.json` | published G values with lab coordinates and techniques | ~15 nodes |
| `values_alpha_drift_v0.json` | quasar Δα/α constraints at various z, ESPRESSO limits | ~5 nodes |

---

### VI. PAPER STRUCTURE

```
I.    THE DECOMPOSITION
      - PHYS-42 confirmed the sum. This paper decomposes it.
      - Component T (tick count) vs Component R (reading depth)
      - Three scenarios: U, L, M

II.   THE COUNTING MACHINE
      - Time as Planck tick integer count
      - Universal vs local vs geometric
      - Arrow of time as property of counting
      - Not a metaphor: the Planck time exists

III.  THE FROZEN SCAN
      - Reading depth as spatial structure
      - Computable without time evolution
      - Sector dependence: strong vs electromagnetic readings
      - Boundary transformation laws

IV.   TEST 1: NUCLEAR VS OPTICAL CLOCK
      - The one test that could make reading depth real
      - Sector splitting prediction from β coefficient ratios
      - Required sensitivity and timeline

V.    TEST 2: PULSAR TIMING GRADIENT
      - Galactic boundary structure in the timing residuals
      - What NANOGrav should look for
      - Structure-correlated vs density-correlated patterns

VI.   TEST 3: VOYAGER AT THE HELIOPAUSE
      - Boundary crossing Doppler step
      - Archival data, analysis methodology
      - Connection to Pioneer anomaly resolution

VII.  TEST 4: G SCATTER
      - Is the 500 ppm scatter environmental?
      - Regression against gravitational potential
      - The challenge of technique-dependent systematics

VIII. TEST 5: COSMOLOGICAL α DRIFT
      - The geometric tick hypothesis
      - Constraint from quasar absorption spectra
      - ANDES projection

IX.   THE DECOMPOSITION MATRIX
      - What each test tells us about T vs R
      - How the five tests combine
      - The resolution timeline: 2026-2036

X.    KILL CONDITIONS
      - Five specific conditions that kill specific claims
      - None kills the entire framework
      - Each constrains the T/R decomposition
```

---

### VII. DIAGRAMS

8 figures minimum per paper spec:

1. **The T/R decomposition diagram.** Two axes: tick count (vertical, labeled N) and reading depth (horizontal, labeled Φ/c²). GR dilation as a diagonal through the T-R plane. The five tests as projections onto each axis.

2. **Sector splitting prediction.** Two clock oscillation frequencies as a function of gravitational potential. Divergence between nuclear and optical curves at the predicted splitting level.

3. **Pulsar timing gradient map.** Schematic galaxy face-on with pulsar positions, known potential gradient (smooth), and predicted boundary structure residual (correlated with spiral arms).

4. **Voyager heliopause crossing.** Doppler frequency vs distance. Smooth GR curve with superimposed step at 120 AU.

5. **G scatter vs laboratory potential.** Published G values plotted against laboratory Φ/c², with regression line and confidence band.

6. **α drift vs redshift.** Δα/α measurements at various z from quasar spectra, with drift model curves for different geometric tick rates.

7. **The soliton hierarchy with T and R labeled.** Nested boundaries (Planck → quark → nucleon → atom → planet → star → galaxy → universe) with R as the radial coordinate and T as tick arrows at each level.

8. **The decomposition decision tree.** Flowchart: Test 1 result → if disagree: R is sector-dependent → Test 2 result → if structure residuals: R has boundary structure → etc. Each branch labels which component is constrained and what follows.

---

### VIII. CONNECTION TO PROGRAMS

**Updates to program_gr_reading_depth_v0:**
- Kill switch 1 (nuclear vs optical clock) is now Test 1 of PHYS-43
- Kill switch 2 (NANOGrav gradient) is now Test 2 of PHYS-43
- Kill switch 4 (G scatter) is now Test 4 of PHYS-43
- Kill switch 5 (Voyager Doppler) is now Test 3 of PHYS-43

**New program entry:** `program_clock_reading_decomposition_v0`
- Thesis: Observed time dilation has two components (tick count T, reading depth R) that can be experimentally separated
- Kill switches: nuclear/optical agreement at 10⁻¹⁹ kills sector-dependent R; NANOGrav no structure kills boundary R; ANDES Δα/α = 0 at 10⁻⁸ kills geometric T
- Connections: program_gr_reading_depth (shares tests 1-4), program_beta_unification (β coefficients determine sector splitting in Test 1)

---

### IX. WHAT THIS PAPER DOES NOT DO

- Does not claim to know the T/R decomposition
- Does not perform any of the five tests (experimental data awaited)
- Does not add to the integer chain prediction count
- Does not compute new derived values from existing pool data
- Does not modify any existing experiment results

What it does: lays out the experimental program that would resolve the deepest open question in the RUM framework. States predictions under each scenario. Specifies sensitivities. Sets kill conditions. Provides the roadmap for the next decade of tests.

---

**Agreement needed before writing:** Is this the right scope? Should any tests be dropped or added? Is the three-scenario structure (U, L, M) the right decomposition, or is it missing a fourth option? Should the derivations be written in this session or deferred to Session 8?
