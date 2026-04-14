## Experiment Plan: Separating the Clock from the Reading

**Experiment key:** `experiment_clock_reading_decomposition_v0`

**Program:** `program_clock_reading_decomposition_v0`

**Purpose:** Test whether the Planck tick (K) and the reading depth (D) are experimentally separable components of what physics calls "time."

---

### THE DISTINCTION YOU'RE MAKING

Let me make sure I have this right, because this is the conceptual foundation.

**The reading (D)** is geometry. It is spatial. It is the structure of the soliton hierarchy. You can compute it at frozen time — no clock needed. Given the integers, the β coefficients, the boundary transformation laws, and the positions, you can predict what any measurement will return at any depth. Mercury's perihelion advance is a reading: the formula δω = 6πGM/(ac²(1−e²)) is a geometric property of the solar soliton's reading depth gradient. It doesn't need time. It needs curvature. The curvature exists in the hierarchy whether or not the clock is ticking.

PHYS-42 confirmed this. One derivation function scanned through the hierarchy — frozen, static, no temporal evolution — and predicted the reading at every depth. Mercury at 2.8 ppb. Solar redshift at 16 ppm. GPS at 0.35%. These are geometric facts about the hierarchy, computed from pool constants, matching historical measurements that were collected over decades. The measurements needed time (someone had to wait for Mercury to orbit). The predictions did not.

**The tick (K)** is the clock. It is temporal. It is what allows things to happen. The human jumps — that requires ticks. Each tick advances the state by one Planck step. The parabola unfolds over ticks. The human lands. Without ticks, nothing moves, nothing changes, nothing happens. The universe is a frozen geometry.

But here's the key: you could have predicted the entire parabola from the geometry alone. Given the initial velocity, the mass, and the reading depth gradient (g = GM/R²), the parabola is fully determined. The ticks didn't change the parabola's shape. They caused it to be traversed. The reading says what will happen. The tick makes it happen.

**Spacetime doesn't exist as a unified thing.** There is space (the soliton hierarchy, navigable by readings) and there is the clock (the Planck tick, monotonically incrementing). They are not woven together into a 4D manifold. They are separate. The Minkowski "metric" is actually two things: a spatial geometry (the hierarchy) and a clock rate (the tick). GR conflates them into g_μν because GR was built before anyone knew about soliton boundaries. The conflation works — PHYS-42 proved it works across 18 orders of magnitude — but it hides the seam.

The experiment looks for the seam.

---

### WHAT THE SEAM LOOKS LIKE

If K and D are truly separate, there should be measurable consequences:

**Consequence 1: Sector splitting.** The reading (D) depends on which force sector you're reading. The β coefficients differ between sectors (strong: −7, electromagnetic: 41/10, weak: −19/6). If the reading is a separate component from the tick, then different clock types — which read different sectors — should disagree at a level proportional to the β difference times the reading depth.

The tick is sector-blind. It ticks once for everything. The reading is sector-specific. It reads differently for different forces. A nuclear clock reads the strong sector. An optical clock reads the electromagnetic sector. If the reading contributes to what we call "time dilation," these two clocks disagree.

**Consequence 2: Static vs dynamic tests diverge at second order.** A static reading (Pound-Rebka: how much does the frequency shift over 22.5 m?) and a dynamic reading (muon dilation: how long does a moving particle live?) both agree with GR at first order. But if they're different components, they may differ at second order. The static test is pure D (geometry of the hierarchy). The dynamic test involves K (the tick must occur for the muon to decay and for it to move).

**Consequence 3: The frozen scan predicts everything the tick reveals.** If you give the derivation function the right inputs, it predicts Mercury, GPS, solar redshift, Planck units — all without any temporal evolution. The tick didn't add information. It added actuality. The experiment should test whether there are cases where the frozen scan fails — where the tick adds something the geometry cannot predict.

---

### THE EXPERIMENT STRUCTURE

One experiment JSON. Five derivation functions. One for each of the five tests from PHYS-43, corrected per the review.

#### Derivation 1: `sector_splitting_prediction_v0`

**What it computes:** The predicted fractional frequency ratio change between a nuclear clock (strong sector) and an optical clock (electromagnetic sector) at two gravitational potentials.

**The formula (corrected per errata E2, E3, A6):**

Use SM betas at laboratory scale, not CD-modified betas:

β₁_SM = 41/10 (electromagnetic sector, GUT-normalized)
β₃_SM = −7 (strong sector)

Differential sector splitting for altitude difference Δh:

ΔΦ/c² = g × Δh / c²

ε_sector = κ × |β₃_SM − β₁_SM| × ΔΦ/c²

where |β₃ − β₁| = |−7 − 41/10| = |−111/10| = 111/10 = 11.1

For Δh = 1000 m:
ΔΦ/c² = 9.82 × 1000 / (299792458)² = 1.09 × 10⁻¹³

ε_sector(κ=1) = 11.1 × 1.09 × 10⁻¹³ = 1.21 × 10⁻¹²

The derivation outputs ε for several κ values (1, α_em, α_em², Φ/c²) so the comparison can store the prediction at each suppression level.

**Inputs from pool:**
- `beta_sm_u1_total_v0` = 41/10 (exact Fraction)
- `beta_sm_su3_total_v0` = −7 (exact Fraction)
- `result_g_surface_from_gm_v0` (from PHYS-42, approximate)
- `si_speed_of_light_v0` = 299792458 (exact)
- `coupling_alpha_em_inverse_v0` = 137035999177/1000000000 (exact Fraction)
- `result_earth_phi_over_c2_v0` (from PHYS-42)

**New values needed:**
- `test_clock_altitude_difference_v0` = 1000 m (reference altitude for prediction)
- `test_clock_sensitivity_target_v0` = 1e-18 (projected Sr-Th comparison sensitivity)

**Outputs:**
- `result_sector_beta_difference_v0` — the |β₃ − β₁| = 111/10
- `result_delta_phi_1000m_v0` — ΔΦ/c² for 1000 m
- `result_splitting_kappa_1_v0` — ε at κ = 1
- `result_splitting_kappa_alpha_v0` — ε at κ = α_em
- `result_splitting_kappa_alpha2_v0` — ε at κ = α²
- `result_splitting_kappa_phi_v0` — ε at κ = Φ/c²
- `result_splitting_detectable_kappa_1_v0` — bool: is κ=1 above sensitivity?
- `result_splitting_detectable_kappa_alpha_v0` — bool: is κ=α above sensitivity?
- `result_max_kappa_for_null_v0` — κ value below which the effect is undetectable

**Comparisons:**
1. |β₃ − β₁| = 111/10 (exact check — verifies SM betas read correctly)
2. ε(κ=1) > sensitivity target (bool — is the bold prediction detectable?)
3. ε(κ=α) > sensitivity target (bool — is the loop-suppressed prediction detectable?)
4. max detectable κ (range check — how much suppression can the experiment tolerate?)

---

#### Derivation 2: `static_vs_dynamic_classification_v0`

**What it computes:** For each of the 18 PHYS-42 tests, classify it as static-D (pure reading, no tick required), dynamic-K (tick required, geometry insufficient), or mixed.

This is a structural derivation — it doesn't compute new numbers. It reads the PHYS-42 outputs and tags each one.

**The classification logic:**

A test is static-D if the prediction formula uses only spatial quantities (positions, masses, radii, potentials) and the predicted value is a geometric property (angle, frequency ratio, dimensionless potential).

A test is dynamic-K if the prediction requires temporal evolution (lifetime, period decay, lightcurve stretch).

A test is mixed if the formula combines spatial geometry with a rate (GPS: gravitational shift is D, velocity shift involves K because velocity requires ticking).

**The classification (from the annotation A2):**

| Test | Type | Reason |
|---|---|---|
| Pound-Rebka | D | Frequency ratio from static potential gradient |
| GPS gravitational | D | Static potential difference between altitudes |
| GPS velocity | K | Velocity requires ticks; capacity allocation |
| GPS net | Mixed | Sum of D (gravitational) and K (velocity) |
| Gravity Probe A | D | Static potential difference |
| Solar redshift | D | Static potential at surface |
| Mercury perihelion | D | Geometric curvature (formula is static) |
| Muon dilation | K | Lifetime requires ticks; decay is temporal |
| Shapiro γ | D | Spatial curvature parameter |
| Hulse-Taylor | K | Period decay requires temporal evolution (GW emission) |
| SN Ia stretch | K | Cosmological expansion is temporal |
| Planck time | structural | Definition |
| Planck length | structural | Definition |
| c = l_P/t_P | structural | Identity |
| g surface | D | Static gradient |
| Earth Φ/c² | D | Static potential |
| Sun Φ/c² | D | Static potential |
| Earth r_s | D | Static radius |

**Outputs:**
- `result_count_static_d_v0` — number of D-type tests
- `result_count_dynamic_k_v0` — number of K-type tests
- `result_count_mixed_v0` — number of mixed tests
- `result_count_structural_v0` — number of structural identities
- `result_d_tests_all_pass_v0` — bool: did all D-type tests pass in PHYS-42?
- `result_k_tests_all_pass_v0` — bool: did all K-type tests pass in PHYS-42?
- `result_classification_consistent_v0` — bool: does the D/K split introduce any inconsistency?

**Comparisons:**
1. D-type test count (range [7, 12] — sanity check)
2. K-type test count (range [2, 5])
3. All D tests passed (bool = true)
4. All K tests passed (bool = true)
5. Classification consistent (bool = true)

The point: if all D tests pass and all K tests pass independently, the two components both work. If one category systematically has larger misses than the other, there's a tension between the components.

---

#### Derivation 3: `frozen_scan_completeness_v0`

**What it computes:** For each PHYS-42 test classified as dynamic-K, check whether the frozen scan (static geometry alone) can reproduce the prediction. If it can, the K component added actuality but not information. If it cannot, the K component carries information that the frozen scan misses.

**The logic:**

Mercury perihelion: the formula δω = 6πGM/(ac²(1−e²)) is static geometry. The orbit precesses, which takes time, but the precession rate is fully determined by the frozen curvature. K adds actuality (the orbit is traversed) but not information (the rate is predicted from D alone). Score: D-complete.

Muon dilation: τ_lab = γ × τ_rest. The Lorentz factor γ depends on velocity v/c. Velocity is a spatial quantity (dx/ds in the geometry). The rest lifetime τ_rest is a temporal quantity — it depends on how many ticks the muon survives. The frozen scan can compute γ (it's geometric). It cannot compute τ_rest (that requires knowing the decay rate, which is a temporal process). But τ_rest is a measured input, not a prediction. The prediction (τ_lab = γ × τ_rest) uses one geometric quantity (γ) and one measured temporal quantity (τ_rest). Score: D-complete given τ_rest as input.

Hulse-Taylor: Pdot (period decay rate) comes from the quadrupole radiation formula, which depends on masses, orbital parameters, and the gravitational wave emission rate. The emission rate is temporal — energy leaves the system over time. But the formula for Pdot is algebraic: it depends on masses and orbital elements, all spatial. The temporal aspect is that the system evolves (the orbit shrinks), but the instantaneous Pdot is computable from the frozen geometry. Score: D-complete for instantaneous Pdot; the cumulative period change requires K.

SN Ia stretch: (1+z) is cosmological redshift, which depends on the scale factor ratio between emission and observation epochs. The scale factor changes with time (cosmic expansion). This is genuinely temporal — you cannot compute the stretch from a single frozen snapshot. You need two snapshots at different tick counts. Score: K-required.

GPS velocity: v²/(2c²) requires knowing the velocity, which is dx/dt — rate of position change per tick. In the frozen scan, there is no dt, so there is no velocity. Score: K-required for the velocity component.

**Outputs:**
- `result_d_complete_count_v0` — number of K-type tests where frozen scan suffices
- `result_k_required_count_v0` — number of tests where ticking adds essential information
- `result_frozen_scan_coverage_v0` — fraction of all 18 tests that the frozen scan covers
- `result_k_required_list_v0` — string listing the K-required tests

**Comparisons:**
1. Frozen scan coverage > 0.6 (range — the frozen scan should cover most tests)
2. K-required count (range [2, 5] — some tests genuinely need ticking)
3. D-complete count + K-required count + structural = 18 (exact — accounts for all tests)

---

#### Derivation 4: `reading_hierarchy_scan_v0`

**What it computes:** The reading at every level of the soliton hierarchy, from Planck to cosmological, computed purely from spatial inputs. No temporal quantities. This is the frozen scan itself — demonstrating that reading depth is computable without time.

**The scan:** For each level, compute Φ/c² = GM/(Rc²) using spatial quantities only. The mass M and radius R are spatial properties of the soliton at that level. The speed of light c is l_P/t_P (the ratio of spatial to temporal resolution, which is itself a structural identity).

| Level | M source | R source | Φ/c² |
|---|---|---|---|
| Earth surface | GM_E | R_E | ~7e-10 |
| GPS orbit | GM_E | r_gps | ~1.7e-10 |
| Sun surface | GM_S | R_S | ~2.1e-6 |
| Mercury orbit | GM_S | a_mercury | ~2.6e-8 |
| Neutron star | GM_NS (estimated) | R_NS | ~0.15-0.35 |
| Planck | (definition) | l_P | 1 (horizon) |

Each of these is a frozen-time computation. No tick is involved. The derivation scans through the hierarchy and produces the reading depth profile.

**Then:** compare each frozen-scan reading to the corresponding PHYS-42 measurement. If the frozen scan reproduces the measurement, the reading is sufficient. If it doesn't, the tick contributed something beyond geometry.

**Inputs from pool:**
- All `gr_*` values from PHYS-42
- PHYS-42 experiment results (the `result_*` outputs)

**Outputs:**
- `result_hierarchy_depth_earth_v0` — Φ/c² at Earth (frozen scan)
- `result_hierarchy_depth_sun_v0` — Φ/c² at Sun
- `result_hierarchy_depth_mercury_v0` — Φ/c² at Mercury orbit
- `result_hierarchy_depth_gps_v0` — Φ/c² at GPS
- `result_hierarchy_depth_ns_v0` — Φ/c² at neutron star
- `result_hierarchy_matches_phys42_v0` — bool: do all frozen-scan values match PHYS-42?
- `result_frozen_scan_max_miss_v0` — worst miss between frozen scan and PHYS-42

**Comparisons:**
1. Earth Φ/c² matches PHYS-42 (miss_pct, expected ~0)
2. Sun Φ/c² matches PHYS-42 (miss_pct, expected ~0)
3. All frozen-scan readings match PHYS-42 (bool = true)
4. Maximum miss < 0.01% (range — the frozen scan should be exact, any miss is a computational consistency check)

---

#### Derivation 5: `tick_observable_unique_v0`

**What it computes:** For each K-required test (from derivation 3), compute what the tick adds that the frozen scan cannot. This isolates the unique contribution of K.

**For SN Ia stretch:** The frozen scan gives the reading depth at z = 1 and at z = 0 separately, but cannot give the stretch factor (1+z) because the stretch requires comparing two different tick counts (two different epochs). The tick's contribution is: the ratio of scale factors between epochs. This is the expansion history H(z), which is a K-quantity (rate of change of geometry per tick).

The derivation computes: H₀ from pool, then the lookback tick count ΔN = Δt/t_P between z = 0 and z = 1.

**For GPS velocity:** The frozen scan gives the potential at GPS altitude (D component). The velocity requires ticks (K component). The derivation computes: the K contribution to GPS net shift = −v²/(2c²) × 86400 = −7.21 μs/day. This is the part that cannot be computed from a frozen snapshot.

**For muon dilation:** The frozen scan gives γ from the spatial trajectory. The rest lifetime τ_rest is a K-quantity — how many ticks the muon survives internally. The derivation computes: τ_rest in Planck ticks = 2.197 × 10⁻⁶ / 5.391 × 10⁻⁴⁴ = 4.08 × 10³⁷ ticks. This is the muon's internal tick budget. The dilated lifetime = γ × tick budget (in Planck ticks).

**Outputs:**
- `result_sn1a_tick_count_v0` — number of Planck ticks from z=1 to z=0
- `result_gps_k_component_us_v0` — velocity contribution to GPS shift (μs/day)
- `result_gps_d_component_us_v0` — gravitational contribution to GPS shift (μs/day)
- `result_gps_k_fraction_v0` — K/(D+K) fraction of total GPS shift
- `result_muon_tick_budget_v0` — τ_rest in Planck ticks
- `result_muon_tick_budget_log10_v0` — log₁₀ of above
- `result_k_adds_information_v0` — bool: does K contribute beyond D?

**Comparisons:**
1. GPS K fraction (range [0.1, 0.3] — velocity is ~18% of total GPS shift)
2. GPS D+K total matches PHYS-42 (miss_pct against 38.50 μs/day)
3. Muon tick budget in range (range [10³⁶, 10³⁸] — order-of-magnitude check)
4. K adds information (bool = true — it must, because velocity and lifetime require ticking)

---

### EXPERIMENT JSON STRUCTURE

```
experiment_clock_reading_decomposition_v0
  ├── derivation 1: sector_splitting_prediction_v0
  │     4 comparisons (exact, bool×2, range)
  ├── derivation 2: static_vs_dynamic_classification_v0
  │     5 comparisons (range×2, bool×3)
  ├── derivation 3: frozen_scan_completeness_v0
  │     3 comparisons (range×2, exact)
  ├── derivation 4: reading_hierarchy_scan_v0
  │     4 comparisons (miss_pct×2, bool, range)
  └── derivation 5: tick_observable_unique_v0
        4 comparisons (range×2, miss_pct, bool)
Total: 5 derivations, 20 comparisons
```

---

### NEW VALUE NODES NEEDED

| Key | Value | Unit | Source | Purpose |
|---|---|---|---|---|
| `test_clock_altitude_difference_v0` | 1000 | m | reference | Altitude for splitting prediction |
| `test_clock_sensitivity_target_v0` | 1e-18 | dimensionless | PTB/JILA projection | Detection threshold |
| `gr_ns_typical_mass_solar_v0` | 7/5 | M_sun | Ozel 2016 | Already in pool from the GR values |
| `gr_ns_typical_radius_m_v0` | 10000 | m | NICER 2019 | Already in pool |

Most inputs are already in the pool from PHYS-42. The experiment primarily reads existing values and PHYS-42 outputs. Only 2 genuinely new nodes needed.

---

### WHAT EACH DERIVATION PROVES

**Derivation 1** answers: if D is sector-dependent, how large is the effect? It gives the number that Test 1 (nuclear vs optical clock) will measure or constrain. This is the experiment's central prediction.

**Derivation 2** answers: which of the 18 PHYS-42 tests are pure-D (frozen geometry) and which require K (ticking)? This classifies the existing evidence into the two components.

**Derivation 3** answers: for the K-required tests, could the frozen scan have predicted them anyway? This tests whether K adds information or just actuality. If every K-required test can be predicted from spatial geometry plus measured temporal inputs, then K adds actuality but the readings carry all the information.

**Derivation 4** answers: does the frozen scan (pure D, no ticking) reproduce the reading at every level of the hierarchy? This is the positive case for D — demonstrating that reading depth IS geometry.

**Derivation 5** answers: what specifically does K contribute that D cannot? It isolates the K-unique observables: velocity, lifetime, expansion history. These are the things that require ticking. The universe needs a clock for them. The clock is K.

Together: the five derivations establish that D and K are conceptually separable, computationally separable, and (via derivation 1) potentially experimentally separable. The sector splitting prediction is the seam.

---

### WHAT THE EXPERIMENT DOES NOT DO

Does not perform the nuclear clock comparison (hardware not ready). Does not analyze pulsar timing data (archival analysis, separate experiment). Does not analyze Voyager data. Does not regress G measurements. Does not measure α drift.

It computes predictions and classifications. It prepares the framework for when the experimental data arrives. When the thorium clock comparison is published (2028-2032), the comparison in derivation 1 will be updated from INFO to PASS/FAIL.

---

### CONNECTION TO EXISTING POOL

The experiment reads from:
- PHYS-42 outputs (all `result_*` values from `gr_reading_depth_mega_v0`)
- SM beta coefficients (`beta_sm_*`)
- Coupling constants (`coupling_alpha_em_inverse_v0`)
- SI constants (`si_speed_of_light_v0`)
- GR values (`gr_*` from the time dilation mega-experiment)
- Cosmological values (`cosmo_*` for the SN Ia tick count)
- Planck units (`gr_planck_time_v0`, `gr_planck_length_v0`)

No values from the CD-modified beta set are used (per erratum A6: use SM betas at laboratory scale).

---

### EXPECTED RESULTS

All 20 comparisons should PASS. The experiment is computational, not observational. It classifies, predicts, and checks internal consistency. The one prediction that awaits experimental data (sector splitting) is stored as INFO.

The interesting outputs are:
- The sector splitting at κ = 1: ~1.2 × 10⁻¹² (6 orders above detection)
- The sector splitting at κ = α: ~8.8 × 10⁻¹⁵ (3 orders above detection)
- The D/K classification: ~9 D-type, ~3 K-type, ~3 mixed, ~3 structural
- The frozen scan coverage: ~80% of tests predicted from geometry alone
- The GPS K fraction: ~18% (velocity is 18% of the total GPS shift)
- The muon tick budget: ~4 × 10³⁷ Planck ticks

---

Ready for review. Should I proceed to writing the experiment JSON and derivation functions, or do you want to adjust the scope?
