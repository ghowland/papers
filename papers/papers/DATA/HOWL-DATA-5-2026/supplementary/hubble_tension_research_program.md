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

# Hubble Tension Research Program — Supporting Tables

**Companion to:** Hubble Tension Running Curve Research Program

**Date:** April 3, 2026

---

## Table 1: The Five H₀ Measurements

All values from phys24_hubble_lib.py H0_MEASUREMENTS dict.

| Key | Method | H₀ (km/s/Mpc) | σ | Year | Distance Class | effective_N | Fraction |
|---|---|---|---|---|---|---|---|
| SH0ES | Cepheid-calibrated SNe Ia | 73.0 | ±1.0 | 2022 | local | None | 730/10 |
| H0LiCOW | Gravitational lensing time delays | 73.3 | ±1.8 | 2020 | local-medium | None | 733/10 |
| CCHP | Tip of Red Giant Branch | 69.8 | ±1.7 | 2021 | medium | None | 698/10 |
| DES_BAO_BBN | BAO + BBN combined | 67.4 | ±1.2 | 2022 | high | None | 674/10 |
| Planck | CMB power spectrum | 67.4 | ±0.5 | 2020 | maximum | None | 674/10 |

**5 of 5 effective_N values are None.** This is the primary data gap.

---

## Table 2: Derived Quantities

| Quantity | Value | Source | Library Variable |
|---|---|---|---|
| H₀_local | 73.0 km/s/Mpc | SH0ES | H0_local |
| H₀_far | 67.4 km/s/Mpc | Planck | H0_far |
| Cumulative ratio | 337/365 = 0.92329 | H0_far / H0_local | cumulative_ratio |
| ln(73.0/67.4) | 0.07981 | Natural log of inverse ratio | ln_cumulative |
| Tension | 5.01σ | Combined uncertainty | H0_tension_sigma |
| VP step size | 1/(3π) = 0.1061 | Known per-threshold VP correction | VP_STEP_SIZE |

---

## Table 3: The Magnitude Constraint

Required per-transit correction r for each assumed N, from phys24_hubble_lib.py MAGNITUDE_TABLE.

| N_eff | r | 1 − r | ~1/x | H₀ step / VP step | Character |
|---|---|---|---|---|---|
| 10 | 0.99205 | 0.00795 | ~1/126 | 0.0749 | Large correction, few boundaries |
| 50 | 0.99840 | 0.00160 | ~1/626 | 0.0151 | Moderate |
| 100 | 0.99920 | 0.000798 | ~1/1253 | 0.00752 | Standard benchmark |
| 500 | 0.99984 | 0.000160 | ~1/6264 | 0.00151 | Many boundaries |
| 1000 | 0.99992 | 0.0000798 | ~1/12530 | 0.000752 | Very many |
| 5000 | 0.999984 | 0.0000160 | ~1/62634 | 0.000151 | Cosmological depth |
| 10000 | 0.999992 | 0.00000798 | ~1/125291 | 0.0000752 | Full CMB path |

**Pattern:** 1 − r ≈ 0.0798/N exactly. The 0.0798 = ln(73.0/67.4).

---

## Table 4: Effective Distance Classes

| Class | Methods | H₀ Range | Combined σ | Typical Distance | Estimated N Range | Distinct? |
|---|---|---|---|---|---|---|
| Local | SH0ES + H0LiCOW | 73.0 − 73.3 | overlap at 1σ | 20-400 Mpc | 5-30 | Merged (F1 soft) |
| Intermediate | CCHP | 69.8 | standalone | 10-30 Mpc (calibrators) | 20-80 | Yes (F4 PASS) |
| Cosmological | DES + Planck | 67.4 | agree exactly | >1 Gpc | 500-10000 | Merged (identical H₀) |

**Effective independent points:** 3 (local, intermediate, cosmological). A two-parameter model through three points has 1 degree of freedom. The running curve is a fit, not an overdetermination.

---

## Table 5: Falsification Test Status

| Test | Description | Current Result | Data Required | What FAIL Means |
|---|---|---|---|---|
| F1 strict | Raw H₀ monotonically decreasing | FAIL | None (uses current data) | H0LiCOW > SH0ES: same distance class |
| F1 soft | Monotonic within 1σ uncertainties | PASS | None | Consistent with monotonic decrease |
| F2 | Is best-fit r a recognizable rational? | UNTESTABLE | N values needed | If FAIL: curve exists but no integer origin |
| F3 | Is χ²/dof < 3 for two-parameter model? | UNTESTABLE | N values needed | If FAIL: model too simple |
| F4 | Intermediate values distinct from endpoints | PASS (CCHP) | None | If FAIL: curve collapses to step function |
| F5 | Has tension been resolved by systematics? | Not resolved | Literature check | If PASS: running curve unnecessary |

---

## Table 6: The Running Curve Model

| Component | Formula | Inputs | Status |
|---|---|---|---|
| Model | H₀(N) = H₀(0) × r^N | H₀(0), r, N | Defined |
| H₀(0) | 73.0 km/s/Mpc (SH0ES) | Measured | Fixed |
| r (empirical) | (337/365)^(1/N) | N, cumulative ratio | Depends on N |
| r (theoretical) | 1 − α²π²(20/13) = 0.99919 | α, gauge integers | From beta unification |
| N (all methods) | None | Structure catalogs | Unknown |
| 1 − r (empirical) | 0.0798/N | N | Depends on N |
| 1 − r (theoretical) | 0.0008086 | α, gauge integers | Fixed |
| N implied by theory | ln(365/337) / α²π²(20/13) = 98.7 ≈ 100 | All above | Prediction |

**The theoretical r implies N ≈ 100.** This is a prediction: the CMB light crosses approximately 100 soliton boundaries between the last scattering surface and us. This is testable against structure catalogs.

---

## Table 7: Theoretical r Derivation (from Beta Unification)

| Factor | Value | Origin | Library Source |
|---|---|---|---|
| α² | 5.325 × 10⁻⁵ | Electromagnetic coupling squared | alpha_inv (DATA-4 B1) |
| π² | 9.870 | 4D spacetime geometry = 32R₄ | pi_f (DATA-4 G1) |
| 20/13 | 1.5385 | \|3b₃_mod\| / \|b₂_mod_num\| | b3_mod, b2_mod (DATA-4 N8, N9) |
| (1−r) | 0.0008086 | α² × π² × (20/13) | Computed |
| r | 0.9991914 | 1 − (1−r) | Computed |
| N for CMB | 98.7 | ln(365/337) / (1−r) | Computed |
| H₀(CMB) | 67.364 km/s/Mpc | 73.04 × r^100 | Computed |
| Miss | 0.007% | vs Planck 67.36 | Verified (28/28 script) |

---

## Table 8: Structural Parallel — α Running vs H₀ Running

| Property | α Running (PHYS-5) | H₀ Running (hypothesis) |
|---|---|---|
| Variable that runs | Coupling strength α(μ) | Apparent expansion rate H₀(N) |
| Independent variable | Energy scale μ (measured by accelerator) | Boundary transit count N (unknown) |
| Boundary type | Quark mass threshold | Galaxy cluster / filament / void wall |
| Per-boundary correction | 1/(3π) = 1/(12R₂) = 0.1061 per Q²N_c | α²π²(20/13) = 0.000809 (theoretical) |
| Correction mechanism | Vacuum polarization screening | VP change at density boundary (proposed) |
| Direction | α increases with energy | H₀ decreases with distance |
| Subgroup (PHYS-11) | B (monotonic accumulation) | B (predicted) |
| Arithmetic | Fraction, verified to 0.02 ppm | Fraction (if r is rational) |
| Integer content | Q², N_c from gauge group | 20/13 from beta coefficients |
| Derivation status | Derived from first principles | Not derived |
| Experimental status | Verified to 0.02 ppm | Not testable (N unknown) |

---

## Table 9: N Estimation Sources

Published papers and catalogs that could provide effective boundary transit counts.

| Source | What It Measures | Coverage | N Estimate Type | Relevant For |
|---|---|---|---|---|
| SDSS DR17 galaxy catalog | Galaxy positions, redshifts | 14,555 deg² | Cluster count along LOS | All methods |
| 2dF Galaxy Redshift Survey | Galaxy positions | 2000 deg² (south) | Complementary to SDSS | SH0ES, CCHP |
| Planck 2018 lensing map | Integrated mass along LOS | Full sky | Total boundary count | Planck, DES |
| Sutter et al. 2012 void catalog | Void positions, sizes | SDSS footprint | Void count per LOS | All methods |
| Cautun et al. 2014 Cosmic Web | Filament classification | N-body simulation | Filament crossings per Mpc | Model input |
| Keenan et al. 2013 KBC void | Local underdensity to ~300 Mpc | Local universe | Reduced N at low distance | SH0ES, H0LiCOW |
| Hoscheit & Barger 2018 | Local void profile | 0-300 Mpc | N gradient near us | All local methods |
| Whitbourn & Shanks 2014 | Local galaxy density field | 0-200 Mpc | Density → boundary count | SH0ES |
| Tully et al. 2014 Laniakea | Supercluster structure | Local supercluster | Boundary topology | Model input |
| Migkas et al. 2020 | H₀ anisotropy in X-ray clusters | Full sky | Directional N variation | Script 11 |

---

## Table 10: Directional Structure for Anisotropy Predictions

| Sky Direction | Known Structure | Expected N Effect | Expected H₀ Effect |
|---|---|---|---|
| Toward Shapley Supercluster (l=307, b=30) | Major overdensity at ~200 Mpc | Higher N (more boundaries) | Lower apparent H₀ |
| Toward Great Attractor (l=320, b=0) | Overdensity at ~65 Mpc | Moderately higher N | Moderately lower H₀ |
| Toward Dipole Repeller (l=210, b=-30) | Underdensity | Lower N (fewer boundaries) | Higher apparent H₀ |
| Toward KBC Void center (l=170, b=−10) | Local underdensity to ~300 Mpc | Lower N locally | Higher H₀ for nearby sources |
| Toward CMB cold spot (l=209, b=−57) | Known underdensity | Lower N along this LOS | Higher H₀ along this LOS |
| Perpendicular to supergalactic plane | Average density | Average N | Average H₀ |

**Key prediction:** H₀ dipole should align with the matter density dipole, not with the CMB kinematic dipole. Migkas et al. 2020 found suggestive evidence for this in X-ray cluster data. The running curve model predicts the dipole direction and amplitude from the structure maps.

---

## Table 11: Future H₀ Measurements

Measurements that could test the running curve within the next 5 years.

| Experiment | Method | Expected H₀ precision | Distance Class | Expected Date | N Sensitivity |
|---|---|---|---|---|---|
| JWST TRGB | TRGB with JWST calibration | ±0.8 km/s/Mpc | medium | 2024-2025 | Tests intermediate curve |
| DESI BAO | Baryon acoustic oscillations | ±0.5 km/s/Mpc | high | 2024-2026 | Tests cosmological end |
| CMB-S4 | CMB power spectrum, ground-based | ±0.3 km/s/Mpc | maximum | 2027-2030 | Most precise CMB H₀ |
| Euclid | Weak lensing + BAO | ±0.7 km/s/Mpc | high | 2025-2028 | Independent high-N |
| SPT-3G | CMB from South Pole | ±0.6 km/s/Mpc | maximum | 2024-2026 | Cross-check Planck |
| ACT DR6 | CMB from Atacama | ±0.5 km/s/Mpc | maximum | 2024-2025 | Cross-check Planck |
| SH0ES + JWST | Combined Cepheid + JWST | ±0.7 km/s/Mpc | local | 2024-2025 | Sharpens local anchor |
| Megamaser Cosmology | H₂O maser distances | ±1.5 km/s/Mpc | low-medium | ongoing | Independent local method |
| Gravitational wave sirens | Binary neutron star mergers | ±2 km/s/Mpc | varies | 2025-2030 | Distance-independent |

**The most discriminating measurement:** Any method that provides H₀ at a specific, well-characterized intermediate distance (z = 0.1-0.5) with σ < 1.5 km/s/Mpc. The running curve predicts a specific H₀ at every distance — not a single value.

---

## Table 12: Script Dependency Map

Which scripts require which prior scripts to have run.

| Script | Requires | Provides To |
|---|---|---|
| 1 (structure_catalog_N) | None | 3, 4, 5, 6, 11, 12, 13 |
| 2 (literature_N) | None | 3, 4, 5, 6 (fallback for 1) |
| 3 (curve_fit) | 1 or 2 | 4, 5, 10, 16 |
| 4 (N_sensitivity) | 1 or 2 | 5, 13 |
| 5 (r_extraction) | 3 | 8, 10, 14, 16 |
| 6 (falsification_full) | 1 or 2 | 16 |
| 7 (new_measurements) | None | 6 (rerun), 16 |
| 8 (vp_boundary) | None (parallel) | 9, 10 |
| 9 (photon_redshift) | 8 | 10 |
| 10 (cumulative_redshift) | 5, 9 | 16 |
| 11 (directional) | 1 | 17 |
| 12 (redshift_dependence) | 3 | 13, 17 |
| 13 (intermediate_prediction) | 4, 12 | 17 |
| 14 (alpha_parallel) | 5 | 16 |
| 15 (standard_cosmology) | 3 | 16 |
| 16 (consolidated) | 3-15 | 17 |
| 17 (diagrams) | 16 | Publication |

---

## Table 13: Library Usage Map

Which platform library each script imports.

| Script | phys24_lib | derivation_lib | structure_lib | boundary_lib | domain_lib | hubble_lib | diagram_lib |
|---|---|---|---|---|---|---|---|
| 1 | × | | | | | × | |
| 2 | × | | | | | × | |
| 3 | × | | | | | × | |
| 4 | × | | | | | × | |
| 5 | × | | | | | × | |
| 6 | | | | | | × | |
| 7 | | | | | | × | |
| 8 | × | × | | | | | |
| 9 | × | × | | × | | | |
| 10 | × | × | | | | × | |
| 11 | | | | | | × | |
| 12 | × | | | | | × | × |
| 13 | | | | | | × | |
| 14 | × | | | | | × | |
| 15 | × | | | | | × | |
| 16 | × | × | × | × | × | × | |
| 17 | × | × | × | × | × | × | × |

**phys24_hubble_lib is used in 15 of 17 scripts.** It is the central library for this program, as phys24_lib is the central library for all programs.

---

## Table 14: Running Curve Predictions at Reference N Values

What the theoretical curve predicts for H₀ at specific N values.

| N | r^N | H₀(N) km/s/Mpc | Distance Class | Measurement Available? |
|---|---|---|---|---|
| 0 | 1.00000 | 73.040 | Local (definition) | SH0ES: 73.0 ± 1.0 |
| 5 | 0.99597 | 72.746 | Very local | No dedicated measurement |
| 10 | 0.99195 | 72.453 | Local galaxies | H0LiCOW: 73.3 ± 1.8 (within 1σ) |
| 25 | 0.97995 | 71.576 | Local-medium | No dedicated measurement |
| 50 | 0.96031 | 70.141 | Medium | CCHP: 69.8 ± 1.7 (within 1σ) |
| 75 | 0.94107 | 68.735 | Medium-high | No dedicated measurement |
| 100 | 0.92222 | 67.362 | Cosmological | Planck: 67.4 ± 0.5 (within 1σ) |
| 200 | 0.85049 | 62.122 | Deep cosmological | No measurement |
| 500 | 0.66627 | 48.669 | Theoretical | No measurement possible |
| 1000 | 0.44391 | 32.424 | Theoretical | Unphysical regime |

**Note:** N > ~150 produces H₀ values that conflict with standard cosmology (the expansion rate cannot be less than ~60 km/s/Mpc without violating BAO constraints). This means either N_Planck < 150, or the model breaks down at large N, or the theoretical r is slightly too large. This is a self-consistency check that Script 15 must address.

---

## Table 15: Comparison of r Values

Different ways to determine r, and whether they agree.

| Method | r Value | 1 − r | Source | Status |
|---|---|---|---|---|
| Theoretical (beta unification) | 0.9991914 | 0.0008086 | α²π²(20/13) | Computed, 28/28 |
| Empirical at N=100 | 0.9991978 | 0.0008022 | (67.4/73.0)^(1/100) | From data |
| Empirical at N=50 | 0.9983997 | 0.0016003 | (67.4/73.0)^(1/50) | From data |
| Empirical at N=200 | 0.9995998 | 0.0004002 | (67.4/73.0)^(1/200) | From data |
| Target for CCHP (N=50) | 0.99907 | 0.00093 | (69.8/73.0)^(1/50) | If N_CCHP = 50 |
| Best VP model (not computed) | unknown | unknown | Scripts 8-9 | UNTESTED |

**The theoretical r matches the empirical r at N=100 to 0.08%.** This is the convergence point between the two research programs. If N_Planck turns out to be ~100 from structure catalogs, the theoretical and empirical values of r agree to better than 0.1%.

---

## Table 16: The π Budget

Where π appears and cancels in the Hubble running framework.

| Formula | π Appears As | Role | Cancels? |
|---|---|---|---|
| DM/baryon = (22/13)π | ×π | Toroidal boundary geometry | Cancels in Ω_DM |
| Ω_b = 2/(13π) | ÷π | Circular normalization | Cancels in Ω_DM |
| Ω_DM = 44/169 | absent | Pure rational | π already cancelled |
| (1−r) = α²π²(20/13) | ×π² | 4D spacetime geometry = 32R₄ | Does not cancel |
| Λ_VL = 39 × log₁₀(α/3π) | ÷3π inside log | VP loop factor α/(2π) × 3/2 | Absorbed in log |
| VP step = 1/(3π) | ÷3π | VP integral normalization | Structural parallel only |

**Key finding:** π enters the Ω chain through two doors (DM/baryon and Ω_b) and exits through exact cancellation. The dark matter density Ω_DM = 44/169 contains no π. This cancellation is algebraic, not numerical — verified exact in Fraction arithmetic.

**Contrast:** π does NOT cancel in the H₀ correction formula. The π² in (1−r) = α²π²(20/13) is structural — it represents the 4D spacetime geometry through which the photon-boundary interaction occurs. If R₄ = π²/32 is the geometric origin, then π² = 32R₄ and the formula becomes (1−r) = 32α²R₄(20/13). The R₄ connects to the two-loop phase space geometry documented in PHYS-9 and PHYS-22.

---

## Table 17: Connection to Other HOWL Papers

| Paper | Connection to Hubble Program | Used In Script(s) |
|---|---|---|
| PHYS-1 | Soliton boundary concept: different readings at different depths | 1, 2, 8, 9, 11 |
| PHYS-2 | Transformation law priority: H₀(N) is the law, not 67.4 or 73.0 | Thesis framing |
| PHYS-3 | Reproducibility ≠ universality: local H₀ clustering explained | 3, 11 |
| PHYS-4 | Per-transit correction magnitude constraint | 5, 8, 10 |
| PHYS-5 | VP running template: 1/(3π) step derivation, computational model | 8, 9, 14 |
| PHYS-6 | QCD running, confinement wall | 8 (b₃ terms) |
| PHYS-9 | R₄ in two-loop QED coefficients | 8 (π² = 32R₄) |
| PHYS-11 | Subgroup B classification: monotonic accumulation | 3, 12 |
| PHYS-12 | Electroweak observables, gauge coupling extraction | 8, 15 |
| PHYS-13 | Unification, beta structure, gap ratio | All (integers from betas) |
| PHYS-22 | Two-loop QED coefficients, R₄ phase space | 8, 9 |
| MATH-1 | R₂ across 17 domains | 9 (boundary geometry) |
| DATA-1 | 268 entries across 17 domains | 9, 11 (domain structure) |
| DATA-4 | All measured constants | All scripts (via phys24_lib) |

---

## Table 18: Kill Switch Decision Matrix

| Kill Switch | Trigger Condition | Detection Script | Impact | Recovery Path |
|---|---|---|---|---|
| K1 | No N estimates obtainable | 1, 2 | Pause Stages 1-4 | Wait for future catalogs |
| K2 | χ²/dof > 5 with all N attempts | 3 | Park running curve model | Try non-exponential models |
| K3 | Empirical r ≠ theoretical r by >10% | 5 | VP mechanism not confirmed | Continue empirical path without VP link |
| K4 | New intermediate H₀ matches endpoint | 7 | Running curve weakened | Reduce to two-class model |
| K5 | Tension resolved by systematics | 7 (literature) | Program unnecessary | Write closure report |
| K6 | No H₀ anisotropy found | 11 | Boundary-dependent running excluded | Running may be isotropic (different model) |

**Kill switches are permanent for their scope but not for the entire program.** K3 kills Stage 3 (VP derivation) but not Stages 1-2 (empirical fitting). K6 kills Stage 4 (directional predictions) but not Stage 1 (curve fitting). Only K2 (bad fit) and K5 (tension resolved) kill the entire thesis.

---

## Table 19: Null Result Registry

| Potential Null | Script | Impact | Documentation |
|---|---|---|---|
| N estimates not available in literature | 1, 2 | Program paused | Null report: "blocked by N problem" |
| χ²/dof > 5 for all N assignments | 3 | Model rejected | Null report: "two-parameter model insufficient" |
| Empirical r irrational (no integer content) | 5 | VP link severed | Running exists but has no gauge group connection |
| VP model gives wrong (1−r) by >10× | 8 | VP mechanism excluded | H₀ correction not from vacuum polarization |
| No H₀ anisotropy in eROSITA data | 11 | Directional predictions falsified | Running not boundary-dependent |
| JWST TRGB agrees with Planck (67.4) | 7 | Intermediate class collapses | Three → two distance classes |
| DESI H₀ disagrees with both endpoints | 7 | New tension, model needs revision | Expand measurement table |
| F1 strict continues to FAIL with new data | 6 | Local ordering remains ambiguous | Document: same distance class |
| H₀(N) curve is linear not exponential | 12 | Exponential model wrong | Test power-law and logarithmic models |
| Standard cosmology inconsistent with corrected H₀ | 15 | Running curve creates new problems | Model is measurement correction, not new physics |

Every null result is documented. Every FAIL is data, not a bug. The phys24_hubble_lib pattern (F1 strict FAIL kept in self-test) applies to every future result.

---

## Table 20: Paper Outcomes by Program Result

| Stage 0 | Stage 1 | Stage 3 | Stage 4 | Paper |
|---|---|---|---|---|
| N obtained | Good fit | VP works | Anisotropy found | "Hubble Running from VP at Cosmological Boundaries" — full derivation + predictions |
| N obtained | Good fit | VP works | No anisotropy | "Hubble Running from VP: Isotropic Correction" — derivation without directionality |
| N obtained | Good fit | VP fails | Any | "The Hubble Running Curve: Empirical Extraction" — data paper, no mechanism |
| N obtained | Bad fit | Any | Any | "The Hubble Running Curve: A Null Result" — two-parameter model insufficient |
| N not obtained | — | VP works | — | "The H₀ Per-Transit Correction from Gauge Group Integers" — theory paper without empirical calibration |
| N not obtained | — | VP fails | — | "The Hubble Running Curve: Blocked by the N Problem" — status report |
| Any | Any | Any | Tension resolved | "The Hubble Running Curve Hypothesis: Closure Report" — null result document |

**Seven outcomes, seven papers.** Every combination of results produces a publishable document. No work is wasted.

---

## Table 21: Timeline and Resource Estimate

| Stage | Scripts | Estimated Lines | Sessions | External Data Needed | Blocking |
|---|---|---|---|---|---|
| 0: N Problem | 1, 2 | 250 | 1 | Yes (catalogs or literature) | Gate for Stages 1-2, 4-5 |
| 1: Curve Fitting | 3, 4, 5 | 260 | 1 | No (uses Stage 0 output) | Needs Stage 0 |
| 2: Falsification | 6, 7 | 180 | 1 | No (uses current + new data) | Needs Stage 0 for F2, F3 |
| 3: VP Derivation | 8, 9, 10 | 240 | 1-2 | No (theoretical computation) | Independent of Stage 0 |
| 4: Predictions | 11, 12, 13 | 260 | 1 | Structure maps | Needs Stages 1 + 3 |
| 5: Cross-Validation | 14, 15 | 200 | 1 | No | Needs Stages 1-4 |
| 6: Integration | 16, 17 | 450 | 1-2 | No | Partial results OK |
| **Total** | **17 scripts** | **~1,840** | **5-9** | **Stage 0 only** | **Stage 0 is the gate** |

---

*Supporting Tables for the Hubble Tension Research Program. 21 tables covering measurements, derived quantities, magnitude constraints, distance classes, falsification tests, model components, r comparisons, π budget, paper connections, kill switches, null results, paper outcomes, and timeline. Every entry traceable to phys24_hubble_lib.py or phys24_lib.py. April 3, 2026.*

