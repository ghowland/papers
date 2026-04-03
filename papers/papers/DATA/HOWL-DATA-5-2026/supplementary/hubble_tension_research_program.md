# Hubble Tension Running Curve Research Program

**Status:** Active investigation, blocked by effective transit count data gap

**Foundation:** phys24_hubble_lib.py (16/17, 1 physically meaningful FAIL)

**Connection:** Beta Unification Program Stage 1 (H₀ correction formula)

**Platform:** HOWL-PLATFORM-v1

**Rule:** Every claim backed by a script. Every unknown marked None. Every null result documented.

---

## The Thesis

The Hubble tension is not a binary discrepancy. It is an incomplete sampling of a continuous running curve H₀(N) = H₀(0) × r^N, where N is the effective boundary transit count and r is a per-transit correction factor. The five current H₀ measurements sample three independent distance classes on this curve. The curve cannot be fit because N is unknown for every measurement.

Two research paths converge on this thesis. Path A (empirical, this program) extracts the curve from data once N values are available. Path B (theoretical, from Beta Unification Stage 1) derives r = 1 − α²π²(20/13) from first principles. If both paths produce the same r, the running curve is established from both ends simultaneously.

---

## Stage 0: The N Problem

The entire program is blocked by one data gap: the effective boundary transit count N for each H₀ measurement method. Without N, the curve cannot be fit, r cannot be extracted empirically, and no prediction can be tested.

### Script 1: structure_catalog_N_estimates.py

**Purpose:** Extract effective boundary transit counts from published large-scale structure catalogs for each H₀ measurement line of sight.

**Method:**
- For SH0ES (Cepheid-calibrated SNe Ia): the typical distance is 20-40 Mpc. Use SDSS galaxy catalog to count galaxy clusters, filaments, and voids along representative lines of sight at this distance
- For H0LiCOW (lensing time delays): the specific lens systems are published (B1608+656, RXJ1131, HE0435, etc.). Use their known coordinates and redshifts to count structure along each specific line of sight
- For CCHP (TRGB): calibration galaxies are published. Count structure along those specific paths
- For DES+BAO: the effective distance is the BAO scale (~150 Mpc comoving). Count structure at that depth averaged over the survey footprint
- For Planck CMB: the effective distance is the last scattering surface (~13.8 Gly). Count total structure along a typical line of sight

**Data sources needed:**
- SDSS DR17 galaxy catalog (positions, redshifts, cluster memberships)
- 2dF Galaxy Redshift Survey (complementary sky coverage)
- Planck 2018 lensing convergence map (integrated mass along line of sight)
- Published void catalogs (Sutter et al. 2012, Hamaus et al. 2014)

**Output:** A table of (measurement_key, N_estimate, N_lo, N_hi) for each of the 5 H₀ measurements. These values populate the currently-None `effective_N` fields in phys24_hubble_lib.py.

**Libraries:** phys24_hubble_lib (measurement data, H0_MEASUREMENTS dict)

**Blocking status:** This script requires external data that may not be scriptable in pure Python. If the catalogs are too large for in-session processing, the alternative is to extract N estimates from published papers that count structures along specific lines of sight (Whitbourn & Shanks 2014, Keenan et al. 2013, Hoscheit & Barger 2018).

**Estimated size:** 100-150 lines if using published N estimates from literature. Much larger if processing raw catalogs.

### Script 2: literature_N_extraction.py

**Purpose:** Fallback for Script 1. Extract N estimates from published papers that characterize the local void, the local supercluster structure, and the large-scale matter distribution.

**Method:**
- The local universe has a known underdensity (the KBC void, Keenan et al. 2013) extending to ~300 Mpc
- Published counts of galaxy clusters within various radii: Abell catalog (richness class ≥ 1) gives ~50-100 clusters within 300 Mpc
- Published counts of voids: the SDSS void catalog (Sutter et al. 2012) gives ~100-200 voids within the survey volume
- Published filament counts: the Cosmic Web classification (Cautun et al. 2014) gives filament density per Mpc³
- From these: estimate N_SH0ES ~ 5-20, N_CCHP ~ 20-80, N_Planck ~ 1000-10000

**Output:** Same as Script 1 — populate the N fields with literature-based estimates and uncertainty ranges.

**Libraries:** phys24_hubble_lib

**Key constraint:** The total ratio H₀_far/H₀_local = 337/365 is fixed. Once N_Planck is estimated, r is determined: r = (337/365)^(1/N_Planck). Then N for intermediate measurements follows from their H₀ values: N_CCHP = ln(H₀_local/H₀_CCHP) / ln(1/r).

---

## Stage 1: Curve Fitting

Once N estimates exist (even rough ones), the curve can be fit.

### Script 3: hubble_curve_fit.py

**Purpose:** Fit H₀(N) = H₀(0) × r^N to the five measurements using estimated N values.

**Method:**
- Import phys24_hubble_lib (measurements, fitting functions)
- Use N estimates from Scripts 1-2
- Call fit_running_curve() from the Hubble library
- Report: H₀(0), r, χ²/dof, residuals for each measurement
- Compare empirical r to theoretical r_theory = 1 − α²π²(20/13) from beta unification
- If they agree to 0.1%: the empirical and theoretical paths converge

**Libraries:** phys24_lib, phys24_hubble_lib

**Key check:** χ²/dof < 2.0 for the two-parameter fit. The example fit in the current library gives χ²/dof = 6.98 with guessed N values — this should drop dramatically with real N estimates.

**Pass condition:** The fit produces r within the range implied by the magnitude constraint table in phys24_hubble_lib.py.

### Script 4: hubble_N_sensitivity.py

**Purpose:** Map how the fit quality depends on the N assignments.

**Method:**
- Hold N_SH0ES = 0 (definition: local, no transits)
- Hold N_Planck at the estimated value (e.g., 5000)
- Scan N_CCHP from 10 to 500 in steps of 10
- For each N_CCHP: fit the curve, record χ²/dof
- Find the optimal N_CCHP that minimizes χ²/dof
- Repeat for N_H0LiCOW and N_DES

**Output:** Three curves of χ²/dof vs N for the three intermediate measurements. The minima determine the best-fit N values. If the minima are sharp, N is well-determined by the data. If flat, N is poorly constrained.

**Libraries:** phys24_lib, phys24_hubble_lib

**Key finding expected:** N_CCHP should be intermediate between N_SH0ES and N_Planck, consistent with CCHP's medium distance class.

### Script 5: hubble_r_extraction.py

**Purpose:** Extract r empirically from the best-fit curve and test its integer content.

**Method:**
- From Script 3: best-fit r value
- Compute 1−r
- Call test_F2_rational_r() from phys24_hubble_lib to check if 1−r is a recognizable fraction
- Also test: is 1−r close to α²π²(20/13) from the beta unification program?
- If yes: the H₀ running curve has the same origin as the beta unification formula
- If no: the running exists but has a different mechanism

**Libraries:** phys24_lib, phys24_hubble_lib

**Connection to Beta Unification:** The theoretical prediction is (1−r) = α²π²(20/13) = 0.0008086. If the empirical extraction gives (1−r) within 1% of this value, the two research programs converge. This would be the strongest finding: a formula derived from gauge group integers that matches an empirically extracted correction factor.

---

## Stage 2: Falsification Tests

### Script 6: hubble_falsification_full.py

**Purpose:** Run all four falsification tests from the notebook with the best available data.

**Method:**
- F1 strict: raw monotonicity (currently FAILS — known, documented)
- F1 soft: monotonicity within uncertainties (currently PASSES)
- F2: is the best-fit r a recognizable rational? (requires N from Stage 0)
- F3: is χ²/dof acceptable for the two-parameter model? (requires N from Stage 0)
- F4: do intermediate values remain distinct from endpoints? (currently PASSES)
- F5: has the tension been resolved by systematic error identification? (check literature)

**Libraries:** phys24_hubble_lib (all test functions)

**Output:** A falsification status report for each test, with the data that drives each result.

### Script 7: hubble_new_measurements.py

**Purpose:** Incorporate H₀ measurements published after the initial five.

**Method:**
- Search for: DESI 2024 H₀, ACT DR6 H₀, SPT-3G H₀, JWST TRGB H₀
- For each new measurement: add to H0_MEASUREMENTS dict (following structural upgrade protocol — new keys, never remove old ones)
- Re-run all falsification tests with the expanded dataset
- Does the new measurement fall on the running curve? Above it? Below it?

**Libraries:** phys24_hubble_lib

**Key question:** Does JWST's TRGB measurement (Freedman et al. 2024) give an H₀ value intermediate between SH0ES and Planck? If so, it provides a fourth distance class and strengthens the running curve. If it agrees with Planck, the running curve loses an intermediate point.

**Structural upgrade:** New measurements are added as new entries in H0_MEASUREMENTS. Old entries are never modified.

```python
# Example upgrade
H0_MEASUREMENTS["JWST_TRGB"] = {
    "H0": Fraction(698, 10),          # placeholder
    "uncertainty": Fraction(13, 10),
    "year": 2024,
    "source": "Freedman et al. 2024",
    "distance_class": "medium",
    "effective_N": None,
    "effective_N_estimate": "medium",
    "method": "JWST TRGB calibration",
}
```

---

## Stage 3: The VP Derivation Path

This stage connects to Beta Unification Program Stage 1. The scripts are shared between the two programs.

### Script 8: vp_at_soliton_boundary.py (= Beta Unification Script 2)

**Purpose:** Derive (1−r) from the vacuum polarization change at a soliton boundary.

**Method:**
- The VP integral gives the electromagnetic coupling's change across a boundary
- At a cosmological soliton boundary (galaxy cluster wall, filament crossing), the vacuum polarization changes because the matter density changes
- The VP change involves the SU(2) and SU(3) gauge content of the matter at the boundary
- Compute: ΔVP = α² × (geometric factor) × (gauge content factor)
- Check: does the geometric factor give π²? Does the gauge content factor give 20/13?

**Libraries:** phys24_lib, data_4_derivation_lib

**If it works:** r is derived. The Hubble running curve has a mechanism. Write the paper.

### Script 9: photon_boundary_redshift.py

**Purpose:** Compute the frequency shift of a photon crossing a region of changing vacuum polarization.

**Method:**
- A photon traveling through a region where α_eff changes experiences a frequency shift
- The shift is δν/ν = −δα/α (from the coupling-dependence of photon energy in medium)
- At a soliton boundary: δα = α² × (VP change from boundary)
- If δα involves the SU(3)/SU(2) ratio 20/13, the photon redshift per boundary is α²π²(20/13)
- This IS (1−r) — the Hubble running correction
- Compute: frequency shift for a specific boundary model (Navarro-Frenk-White density profile)

**Libraries:** phys24_lib, data_4_derivation_lib, phys24_boundary_map_lib

**Key connection to boundary map:** The boundary map library documents what changes at each boundary. For cosmological boundaries, the relevant change is the matter density — which determines the local VP integral. The boundary map infrastructure (traversal functions, coupling values at each boundary) provides the computational framework.

### Script 10: cumulative_redshift.py

**Purpose:** Accumulate the per-boundary redshift across N boundaries and compare to the observed H₀ tension.

**Method:**
- Start with H₀(local) = 73.04 km/s/Mpc
- At each boundary: H₀(N+1) = H₀(N) × r
- After N boundaries: H₀(N) = H₀(0) × r^N
- If r = 1 − α²π²(20/13) and N = 100: H₀(100) = 73.04 × 0.99919^100 = 67.364
- Compare to Planck: 67.36. Miss: 0.007%
- This is the full end-to-end derivation: gauge group → VP change → photon shift → cumulative redshift → H₀(CMB)

**Libraries:** phys24_lib, phys24_hubble_lib, data_4_derivation_lib

**Pass condition:** Derived H₀(CMB) within 0.1% of 67.36 km/s/Mpc using only α, gauge group integers, and an estimated N.

---

## Stage 4: Structure-Dependent Predictions

Once the model is calibrated (r known, N estimated), it makes predictions for specific lines of sight.

### Script 11: directional_H0_predictions.py

**Purpose:** Predict H₀ in specific sky directions based on known large-scale structure.

**Method:**
- The matter distribution is anisotropic: the local universe has known overdensities (Shapley Supercluster, Great Attractor) and underdensities (KBC void, Dipole Repeller)
- Lines of sight through overdense regions cross more boundaries (higher N) → lower apparent H₀
- Lines of sight through underdense regions cross fewer boundaries (lower N) → higher apparent H₀
- Using published structure maps: estimate N(direction) for 10-20 sky directions
- Predict H₀(direction) for each
- Compare to directional H₀ measurements (if available)

**Libraries:** phys24_hubble_lib (running model)

**Key prediction:** The model predicts H₀ should be ANISOTROPIC. Lines of sight through the Shapley Supercluster should give lower H₀ than lines of sight through the KBC void. This is a testable prediction that distinguishes the running curve from a simple systematic error (which would be isotropic).

**Connection to existing data:** Migkas et al. 2020 reported evidence for H₀ anisotropy in X-ray cluster data. Their dipole direction and amplitude would be a direct test of the running curve prediction.

### Script 12: redshift_dependence.py

**Purpose:** Predict the H₀ value as a continuous function of source redshift z.

**Method:**
- Convert redshift z to effective distance in Mpc (using standard cosmology)
- Convert distance to estimated boundary transit count N(z)
- Predict H₀(z) = H₀(0) × r^(N(z))
- Plot H₀ vs z from z = 0 (local) to z = 1100 (CMB)
- The curve should be smooth and monotonically decreasing
- Mark where each measurement sits on the curve

**Libraries:** phys24_lib, phys24_hubble_lib, data_5_diagram_lib (for plotting)

**Key shape:** The curve should be concave (faster decrease at low z where boundaries are sparser, slower decrease at high z where boundaries are denser). This is because the boundary density increases with distance (more structure to cross). The shape is a testable prediction — different from a linear H₀(z) which would imply constant boundary density.

### Script 13: intermediate_distance_prediction.py

**Purpose:** Make a SPECIFIC prediction for H₀ at a distance not yet measured with high precision.

**Method:**
- Choose a distance class between CCHP (medium) and DES (high): z ~ 0.3-0.5
- Estimate N at this distance from structure catalogs
- Predict H₀ at this distance from the calibrated curve
- State the prediction BEFORE any measurement at this distance is published
- This is the gold standard: a pre-registered prediction that can be confirmed or falsified

**Libraries:** phys24_hubble_lib

**Example prediction format:**

```
PREDICTION (pre-registered):
  At effective distance z ~ 0.4 (N ~ 200 estimated):
  H0 = 73.04 × (1 − 0.000809)^200 = 62.1 ± 1.5 km/s/Mpc
  
  If measured H0 at z ~ 0.4 falls within [60.6, 63.6]: consistent
  If outside: running curve excluded at this N estimate
  
  Date: [date of prediction]
  Measurement not yet available: [reference]
```

---

## Stage 5: Cross-Validation

### Script 14: alpha_running_parallel.py

**Purpose:** Verify that the VP running template from PHYS-5 is consistent with the H₀ running model.

**Method:**
- The VP running gives Δα/α = (α/3π) × ΣQ²N_c × ln(μ/m_f) per flavor threshold
- The VP step size is 1/(3π) = 1/(12R₂) = 0.1061
- The H₀ running gives ΔH₀/H₀ = (1−r) = α²π²(20/13) = 0.000809 per boundary
- The ratio: H₀ step / VP step = 0.000809 / 0.1061 = 0.00763
- This ratio should have integer content: 0.00763 ≈ α × (some integer combination)
- Check: α × π × (20/13) = 0.00730 × 3.14159 × 1.538 = 0.0353 — too large
- Check: α² × π × (20/13) = 5.33×10⁻⁵ × 3.14159 × 1.538 = 0.000257 — too small
- The ratio does NOT obviously simplify. This may indicate the two running mechanisms are structurally similar but not derived from each other.

**Libraries:** phys24_lib, phys24_hubble_lib

**Honest assessment:** The VP running is about electromagnetic coupling change with energy. The H₀ running is about photon frequency change with distance. They may share the same mathematical framework (exponential running through discrete boundaries) without sharing the same mechanism. The structural parallel in phys24_hubble_lib.py documents this correctly.

### Script 15: consistency_with_standard_cosmology.py

**Purpose:** Check whether the running curve model is consistent with standard ΛCDM cosmology, or whether it requires modifications.

**Method:**
- In ΛCDM: H₀ is a constant. The Hubble parameter H(z) varies with redshift due to matter and dark energy density evolution, not due to running
- The running curve says: the MEASURED H₀ varies because light crossing boundaries accumulates a systematic correction. The PHYSICAL H₀ is still constant
- Test: is the running curve a systematic correction to the measurement, or a modification to the physics?
- Compute: if the correction is systematic (affects apparent H₀ but not real expansion), does the corrected H₀ = 73.04 km/s/Mpc everywhere produce a consistent cosmology?
- Check BAO scale: does the corrected H₀ give the right sound horizon?
- Check CMB power spectrum: does the corrected H₀ give the right peak positions?

**Libraries:** phys24_lib, phys24_hubble_lib

**Key distinction:** The running curve model does NOT modify ΛCDM. It adds a systematic correction to the H₀ measurement that depends on the line-of-sight boundary count. The universe expands at H₀ = 73.04 km/s/Mpc everywhere. The CMB measurement sees 67.36 because the CMB photons crossed ~100-5000 boundaries on the way here. This is a measurement correction, not new physics.

If this interpretation is correct, the "Hubble tension" is not a tension at all — it is a VP-like systematic that was never corrected for because no one knew soliton boundaries affected photon frequency.

---

## Stage 6: Integration and Publication

### Script 16: hubble_consolidated.py

**Purpose:** The reference script. Computes everything, reports everything, with full provenance.

**Method:**
- Import all libraries
- Compute the running curve with best available N estimates
- Run all falsification tests
- Compare empirical r to theoretical r
- Produce the consolidated prediction table
- Report all unknowns as None or estimated with ranges
- Log provenance for every value

**Libraries:** All platform libraries

### Script 17: hubble_diagrams.py (expanded)

**Purpose:** Expand the existing 8-figure Hubble diagram set to 16-24 figures covering all findings.

**Additional figures beyond the existing 8:**
- Directional H₀ predictions on a sky map
- H₀(z) continuous curve with measurement overlay
- χ²/dof vs N_CCHP from the sensitivity scan
- VP step vs H₀ step structural comparison
- Theoretical r vs empirical r comparison (from beta unification)
- Falsification boundary diagram for each formula
- The KBC void and its effect on local H₀
- Set A vs Set B baryon formula chains propagated through H₀

**Libraries:** data_5_diagram_lib, phys24_hubble_lib, all platform libraries

---

## Kill Switches

| ID | Condition | Action | What Dies |
|---|---|---|---|
| K1 | No published N estimates findable in literature | Program paused (not killed) until data available | Stages 1-4 paused |
| K2 | Best-fit χ²/dof > 5.0 with any reasonable N assignment | Running curve model insufficient. Park thesis. | Stages 3-5 |
| K3 | Empirical r differs from α²π²(20/13) by more than 10% | VP mechanism not confirmed. Continue empirical path only. | Stage 3 only |
| K4 | New measurement at intermediate distance agrees with endpoint (not curve) | Running curve collapses to step function. F4 fails. | Thesis weakened |
| K5 | Hubble tension resolved by identified systematic error | Running curve unnecessary. Write closure report. | Entire program |
| K6 | H₀ anisotropy NOT found in direction-dependent measurements | Isotropic tension rules out boundary-dependent running. | Stages 4-5 |

---

## Falsification Targets

| Observable | Model Prediction | Current Data | Excluded at 2σ if | Key Experiment |
|---|---|---|---|---|
| H₀(z=0.4) | ~68-70 (N-dependent) | Not measured at this z | Outside prediction ± 2 km/s/Mpc | DESI, Euclid |
| H₀ anisotropy | Dipole aligned with LSS | Migkas et al. 2020: some evidence | No dipole found in expanded sample | eROSITA, CMB-S4 |
| H₀ monotonicity | Decreasing with distance | 5 points, marginally consistent | New intermediate measurement above local | JWST, HST |
| 1−r value | 0.0008086 (from beta unification) | Not directly measurable | Empirical r differs by >10% | This program |
| N dependence | H₀(N) = H₀(0)×r^N exactly | Not testable yet | Curve shape is not exponential | Multiple z measurements |

---

## Connection to Beta Unification Program

| This Program | Beta Unification Program | Shared Element |
|---|---|---|
| Extracts r empirically from H₀ data | Derives r = 1 − α²π²(20/13) from gauge integers | The value of r |
| Needs N from structure catalogs | Does not need N (uses N = 100 as reference) | N = 100 benchmark |
| Tests running curve shape | Tests formula precision | H₀(CMB) prediction |
| Scripts 8-10 (VP derivation) | Scripts 2-4 (VP derivation) | Identical scripts |
| Falsification via future H₀ measurements | Falsification via future Ω measurements | Independent tests |

If both programs succeed: the Hubble tension is a VP running effect with (1−r) derived from the gauge group, calibrated against structure catalogs, and verified by independent measurements at multiple distances. The tension becomes a measurement of the large-scale structure boundary count.

---

## Script Inventory

| # | Script Name | Stage | Lines (est) | Libraries | Blocking? |
|---|---|---|---|---|---|
| 1 | structure_catalog_N_estimates.py | 0 | 150 | hubble_lib | YES — unlocks all |
| 2 | literature_N_extraction.py | 0 | 100 | hubble_lib | Fallback for Script 1 |
| 3 | hubble_curve_fit.py | 1 | 80 | phys24_lib, hubble_lib | No |
| 4 | hubble_N_sensitivity.py | 1 | 100 | phys24_lib, hubble_lib | No |
| 5 | hubble_r_extraction.py | 1 | 80 | phys24_lib, hubble_lib | No |
| 6 | hubble_falsification_full.py | 2 | 100 | hubble_lib | No |
| 7 | hubble_new_measurements.py | 2 | 80 | hubble_lib | No |
| 8 | vp_at_soliton_boundary.py | 3 | 100 | phys24_lib, derivation_lib | No |
| 9 | photon_boundary_redshift.py | 3 | 80 | phys24_lib, derivation_lib, boundary_lib | No |
| 10 | cumulative_redshift.py | 3 | 60 | phys24_lib, hubble_lib, derivation_lib | No |
| 11 | directional_H0_predictions.py | 4 | 120 | hubble_lib | No |
| 12 | redshift_dependence.py | 4 | 80 | phys24_lib, hubble_lib, diagram_lib | No |
| 13 | intermediate_distance_prediction.py | 4 | 60 | hubble_lib | No |
| 14 | alpha_running_parallel.py | 5 | 80 | phys24_lib, hubble_lib | No |
| 15 | consistency_with_standard_cosmology.py | 5 | 120 | phys24_lib, hubble_lib | No |
| 16 | hubble_consolidated.py | 6 | 150 | all libraries | No |
| 17 | hubble_diagrams.py (expanded) | 6 | 300 | all libraries + diagram_lib | No |

**Total estimated lines:** ~1,920 across 17 scripts.

---

## Papers This Program Would Produce

**If N estimates obtained and curve fits well (χ²/dof < 2):**
- PHYS-XX: "The Hubble Running Curve: H₀ as a Function of Boundary Transit Count" — empirical extraction of r, curve shape, and predictions for unmeasured distances. No VP derivation needed — pure data.

**If VP derivation succeeds (Stage 3):**
- PHYS-XX: "Hubble Running from Vacuum Polarization at Cosmological Boundaries" — derives (1−r) from first principles, predicts H₀(CMB) from α and gauge group integers. Joint paper with Beta Unification Program.

**If directional predictions confirmed:**
- PHYS-XX: "Anisotropic Hubble Constant from Large-Scale Structure Boundary Counts" — predicts and tests H₀ variation with sky direction. Most directly testable finding.

**If the tension is resolved by systematics (K5):**
- DISC-XX: "The Hubble Running Curve Hypothesis: A Closure Report" — documents the thesis, the data gap, and the resolution. Honest null result.

**If N estimates cannot be obtained (K1):**
- DISC-XX: "The Hubble Running Curve: Blocked by the N Problem" — documents the thesis, the available falsification tests, and the data gap. Status: parked until structure catalog processing is feasible.

Every outcome produces a paper. No work is wasted.

---

## Null Result Registry

| Potential Null | Script | What It Would Mean | Status |
|---|---|---|---|
| No published N estimates exist | 1, 2 | Program blocked. Park until catalogs available. | UNTESTED |
| χ²/dof > 5 with best N estimates | 3 | Two-parameter model insufficient. Need more complex running. | UNTESTED |
| Empirical r ≠ α²π²(20/13) by >10% | 5 | VP mechanism not responsible. Running may have different origin. | UNTESTED |
| No H₀ anisotropy found | 11 | Boundary-dependent running ruled out. Tension is isotropic. | UNTESTED |
| F1 strict FAIL at 73.3 > 73.0 | — | SH0ES and H0LiCOW are same distance class. Known, documented. | KNOWN |
| JWST TRGB agrees with Planck | 7 | Intermediate distance class collapses. Three → two classes. | UNTESTED |
| New α measurement shifts predictions | — | All formulas using α would shift. Sensitivity script needed. | UNTESTED |

Every null result gets documented. The F1 strict FAIL is already documented in the null report and stays in the library. Future nulls follow the same pattern.

---

## Timeline

| Stage | Scripts | Sessions | Blocking Dependencies |
|---|---|---|---|
| 0: N problem | 1, 2 | 1 | None (run first, may require external data) |
| 1: Curve fitting | 3, 4, 5 | 1 | Stage 0 (need N estimates) |
| 2: Falsification | 6, 7 | 1 | Stage 0 (F2, F3 need N) |
| 3: VP derivation | 8, 9, 10 | 1-2 | Stage 0 pass, parallel with Beta Unification |
| 4: Predictions | 11, 12, 13 | 1 | Stages 1-3 (need calibrated curve) |
| 5: Cross-validation | 14, 15 | 1 | Stages 1-4 (need full model) |
| 6: Integration | 16, 17 | 1-2 | Stages 1-5 (partial results OK) |
| **Total** | **17 scripts** | **5-9 sessions** | **Stage 0 is the gate** |

---

*Hubble Tension Running Curve Research Program. 17 scripts, 6 stages, 6 kill switches. Stage 0 (the N problem) is the gate. Connected to Beta Unification via shared VP derivation scripts. Every outcome produces a paper. The F1 strict FAIL is data, not a bug. April 3, 2026.*

---

