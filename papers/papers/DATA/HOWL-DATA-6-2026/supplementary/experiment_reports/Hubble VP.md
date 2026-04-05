The experiment key in the JSON file is `experiment_hubble_vp_prediction_v0` but the filename is still `experiment_hubble_running_prediction_v0.json`. The runner loaded it (it searches all experiment JSON files by key), but the report command matches by the argument you pass.

Run:

```bash
./data6.py report experiment_hubble_vp_prediction_v0
```

That matches the key inside the JSON, which is what the result file is named after (`result_experiment_hubble_vp_prediction_v0_run002.json`).

Optionally rename the file to match: `experiment_hubble_vp_prediction_v0.json`.

---

The experiment ran correctly. 3 FAIL, 3 PASS, 4 INFO — exactly the expected negative result:

- **N_vp = 0.712** — less than one transit, VP step is too large (FAIL, as predicted)
- **VP step too large = True** (FAIL, expected — this IS the finding)
- **Monotonicity = False** (FAIL — H0LiCOW > SH0ES, known from the F1 strict null)
- **H₀(CMB predicted) matches Planck** at 0.0% miss (by construction)
- **F1 soft passes** (the inversion is within noise)

The 3 FAILs are the documented negative result: the α running VP step 1/(3π) does not work as a per-transit H₀ correction.

---

Let me check the result file for exact numbers.Now let me reconstruct the exact output numbers from the experiment run to write a precise report.

The experiment output is visible in the terminal dump. Let me extract the key numbers:

- N_vp = 0.71158
- r_vp = 0.893896704605403
- H₀(CMB predicted) = 67.4 (0.0% miss by construction)
- VP step too large = True
- Monotonicity = False
- F1 soft = True (pass)
- Best integer N miss = 40.53% (N_vp ≈ 0.71 vs nearest integer 1)
- Required 1-r at N=8 vs VP = 90.64% miss (massive mismatch)

---

# Hubble VP Step Prediction — Experiment Report

**Experiment:** `experiment_hubble_vp_prediction_v0`

**Run:** run002, April 6, 2026

**Program:** `program_hubble_running_v0` (Status: ACTIVE_INVESTIGATION)

**Category:** T — Hubble Running Prediction

**Result:** 3 PASS, 3 FAIL, 4 INFO. The VP step hypothesis fails quantitatively. N < 1 means the α running step size 1/(3π) is too large by ~13× to serve as a per-transit H₀ correction. Clear negative result — documented, not a bug.

---

## 1. THE HYPOTHESIS

The Hubble tension is the 5σ disagreement between local H₀ = 73.0 km/s/Mpc (SH0ES) and far H₀ = 67.4 km/s/Mpc (Planck). The running curve hypothesis proposes:

H₀(N) = H₀(0) × r^N

where N is the number of large-scale-structure boundary transits between observer and source, and r < 1 is a per-transit correction factor.

The VP step hypothesis goes further: it proposes that r = 1 − 1/(3π), the same vacuum polarization step size that governs α running through flavor thresholds in QED (PHYS-5, PHYS-6). If the structural parallel between α running and H₀ running is quantitative, the same step size should work.

---

## 2. THE COMPUTATION

**Step 1: Solve for N.** Given r = 1 − 1/(3π) = 0.89390 and the cumulative ratio H₀(Planck)/H₀(SH0ES) = 337/365 = 0.92329, solve:

N = ln(337/365) / ln(1 − 1/(3π)) = (−0.07981) / (−0.11226) = **0.7116**

**Step 2: Predict H₀(CMB).** H₀(CMB) = 73.0 × (0.89390)^0.7116 = 67.4. Matches Planck by construction — we solved for N to produce this match.

**Step 3: Intermediate scan.** Place all 5 H₀ measurements on the running curve by solving N_i = ln(H₀_i/H₀_local) / ln(r_vp) for each:

| Method | H₀ | Distance Class | Solved N |
|---|---|---|---|
| SH0ES | 73.0 | local | 0.000 |
| H0LiCOW | 73.3 | local-medium | −0.027 (negative — H₀ > local) |
| CCHP | 69.8 | medium | 0.406 |
| DES+BAO | 67.4 | high | 0.712 |
| Planck | 67.4 | maximum | 0.712 |

Monotonicity FAIL: H0LiCOW gives negative N (its H₀ is higher than SH0ES). The N values are not monotonically increasing.

**Step 4: Rational scan.** For integer N = 1 through 20, compute the required 1−r and compare to the VP step 1/(3π):

| N | 1−r required | VP ratio | Best fraction |
|---|---|---|---|
| 1 | 0.07671 | 0.723 | 1/13 (0.4%) |
| 2 | 0.03911 | 0.369 | 1/26 (1.4%) |
| 5 | 0.01596 | 0.150 | 1/63 (0.3%) |
| 8 | 0.01003 | 0.0946 | 1/100 (0.3%) |
| 10 | 0.00805 | 0.0759 | 1/124 (0.1%) |
| 20 | 0.00405 | 0.0381 | 1/247 (0.1%) |

The VP step 1/(3π) = 0.1061 is larger than the required 1−r at every integer N ≥ 1. At N = 1, the required 1−r is 0.077 — already 28% smaller than the VP step. At N = 10, the required 1−r is 0.008 — 13× smaller. The VP step overshoots at every scale.

---

## 3. RESULTS TABLE

| # | Check | Mode | Status | Detail |
|---|---|---|---|---|
| 1 | N from VP step (positive) | range [0.1, 100000] | PASS | 0.712 |
| 2 | H₀(CMB predicted) vs Planck | miss% | INFO | 0.0% (by construction) |
| 3 | H₀(CMB) within 2σ of Planck | range [0, 2.0] | PASS | 0.0σ |
| 4 | r_vp = 1 − 1/(3π) | miss% | INFO | 5.1 × 10⁻¹⁰% (verified) |
| 5 | N_vp > 1 (physical plausibility) | range [1.0, 100000] | **FAIL** | 0.712 < 1.0 |
| 6 | Intermediate N monotonic | bool | **FAIL** | H0LiCOW gives N < 0 |
| 7 | F1 soft monotonicity | bool | PASS | bands overlap |
| 8 | VP step too large (N < 1) | bool (expected: false) | **FAIL** | true — VP step too large |
| 9 | Best integer N miss | miss% | INFO | 40.5% (N_vp = 0.71 vs nearest int 1) |
| 10 | Required 1−r at N=8 vs VP | miss% | INFO | 90.6% miss (massive mismatch) |

**Summary:** 3 PASS, 3 FAIL, 4 INFO.

---

## 4. WHAT THE THREE FAILURES MEAN

**FAIL 1 — N_vp = 0.712 < 1.** The VP step 1/(3π) is so large that it reproduces the entire Hubble tension in 0.71 transits — less than one boundary crossing. This is unphysical. A per-transit correction that accomplishes its work in 0.71 transits is not a per-transit correction. The number N must be a positive integer ≥ 1 (you cross a whole number of boundaries). N = 0.71 means the step size is wrong.

**FAIL 2 — Monotonicity.** H0LiCOW (73.3) > SH0ES (73.0). This gives a negative solved N for H0LiCOW, breaking the monotonic-N requirement. This is the known F1 strict failure from the hubble_lib — the two local measurements are statistically indistinguishable (0.3 km/s/Mpc difference, within combined 2.1 uncertainties). They are the same distance class, not two distinct points.

**FAIL 3 — VP step too large = True.** This is the formal recording of FAIL 1 as a boolean. The VP step does not work as the Hubble per-transit correction. The structural parallel between α running and H₀ running breaks at the quantitative level.

---

## 5. WHAT THE THREE PASSES MEAN

**PASS 1 — N is positive.** The algebra works: ln(337/365)/ln(1−1/(3π)) is positive. The model produces a ratio < 1 from a step < 1. The structure is correct even though the magnitude is wrong.

**PASS 2 — H₀(CMB) within 2σ.** By construction — we solved for N to match. This is not a test of the model; it verifies the algebra.

**PASS 3 — F1 soft monotonicity.** The H0LiCOW inversion is within 1σ uncertainties. The raw data is consistent with monotonic decrease even though it doesn't prove it.

---

## 6. THE MAGNITUDE PROBLEM

The core finding is a scale mismatch:

| Quantity | Value | What it means |
|---|---|---|
| VP step: 1/(3π) | 0.1061 | 10.6% correction per transit |
| Hubble tension: ln(73/67.4) | 0.0798 | 7.7% total correction needed |
| Required 1−r at N=1 | 0.0767 | 7.7% per transit if only one crossing |
| Required 1−r at N=10 | 0.00805 | 0.8% per transit if ten crossings |
| Ratio: VP / required(N=10) | 13.2× | VP step is 13× too large at N=10 |

The VP step 1/(3π) is the per-flavor-threshold correction for α running. It equals 1/(12R₂) where R₂ = π/4. In α running, this step applies at each quark mass threshold — there are 5 thresholds between m_e and M_Z, producing a total running of ~7%. The step size is matched to the number of thresholds.

For H₀ running, the total correction is also ~7.7% (from 73.0 to 67.4). But the number of boundary crossings N is unknown. If N = 1, the per-transit correction is 7.7% — close to the VP step but not equal (0.077 vs 0.106, off by 38%). If N = 10, the per-transit correction is 0.8% — an order of magnitude smaller than the VP step. The VP step doesn't match at any plausible N.

---

## 7. WHAT SURVIVES

The qualitative structure survives:

- H₀ measurements decrease with distance (within uncertainties)
- The running curve model H₀(N) = H₀(0) × r^N fits the data for appropriate r
- The cumulative ratio 337/365 is an exact Fraction from the measured values
- The three-distance-class picture (local ~73, intermediate ~70, far ~67.4) is monotonic

What does NOT survive: the specific VP step size 1/(3π) as the per-transit correction. The α running and H₀ running share mathematical structure (both are monotonic reductions through boundary crossings) but NOT magnitude. Different physics, different step sizes.

---

## 8. WHAT THE EXPERIMENT RULES OUT

This experiment rules out one specific quantitative claim: that the per-transit H₀ correction equals the per-threshold α correction 1/(3π). It does NOT rule out:

- The running curve model itself (which works for any r)
- A different per-transit step (e.g., 1−r ≈ 1/126 at N = 10, or 1/1253 at N = 100)
- A connection between gauge integers and H₀ running through a different mechanism
- The qualitative structural parallel between α running and H₀ running

---

## 9. COMPARISON TO HUBBLE_LIB SELF-TEST

The experiment confirms all findings from the phys24_hubble_lib self-test:

| Test | hubble_lib | This experiment |
|---|---|---|
| F1 strict monotonicity | FAIL (H0LiCOW > SH0ES) | FAIL (same) |
| F1 soft monotonicity | PASS (bands overlap) | PASS (same) |
| VP step < required at N=10 | PASS (0.008 < 0.106) | Confirmed |
| All effective_N are None | PASS (5 unknowns) | N/A (we solved N from r) |
| Tension > 4σ | PASS (5.01σ) | Confirmed from pool values |

The experiment adds: the formal computation that N_vp = 0.71 < 1, the intermediate scan showing H0LiCOW gives negative N, and the rational scan showing no simple fraction matches the VP step at any integer N.

---

## 10. DERIVATION OUTPUTS

**hubble_solve_n_from_vp_v0** (18 outputs):

| Key | Value |
|---|---|
| result_n_vp_v0 | 0.71158 |
| result_r_vp_v0 | 0.893896704605 |
| result_one_minus_r_vp_v0 | 0.106103295395 |
| result_vp_step_too_large_v0 | True |
| result_cum_ratio_v0 | 0.923287671233 |
| result_r_at_n1_v0 | 0.923288 |
| result_r_at_n5_v0 | 0.984039 |
| result_r_at_n8_v0 | 0.989969 |
| result_r_at_n10_v0 | 0.991953 |
| result_r_at_n20_v0 | 0.995964 |
| result_r_at_n50_v0 | 0.998403 |

**hubble_predict_h0_cmb_v0** (10 outputs):

| Key | Value |
|---|---|
| result_h0_cmb_predicted_v0 | 67.4 |
| result_h0_cmb_miss_pct_v0 | ~0.0% |
| result_h0_cmb_sigma_v0 | ~0.0 |
| result_best_integer_n_v0 | 1 |
| result_best_integer_n_miss_pct_v0 | 40.53% |

**hubble_intermediate_scan_v0** (8 outputs):

| Key | Value |
|---|---|
| result_n_shoes_v0 | 0.000 |
| result_n_h0licow_v0 | −0.027 |
| result_n_cchp_v0 | 0.406 |
| result_n_des_v0 | 0.712 |
| result_n_planck_v0 | 0.712 |
| result_n_monotonic_v0 | False |
| result_f1_soft_v0 | True |

---

## 11. VALUE NODE ADDED

One new value node: `cosmo_h0_cumulative_ratio_v0` = Fraction(337, 365) in `values_hubble_running_v0.json`.

---

## 12. REGISTRY ADDITIONS

Four new derivations added to DERIVATION_MORE_INDEX_V0 under Category T:

```python
    # T: Hubble running prediction
    "hubble_solve_n_from_vp_v0": hubble_solve_n_from_vp_v0,
    "hubble_predict_h0_cmb_v0": hubble_predict_h0_cmb_v0,
    "hubble_intermediate_scan_v0": hubble_intermediate_scan_v0,
    "hubble_rational_scan_v0": hubble_rational_scan_v0,
```

---

## 13. FALSIFICATION UPDATE

The experiment tested one specific falsifiable prediction of the VP step hypothesis. The prediction failed (N < 1). This does NOT kill the program_hubble_running — it kills one branch of the hypothesis. The program status remains ACTIVE_INVESTIGATION with the VP step branch marked as FAILED.

Updated kill switch status:

| Kill Switch | Condition | Status |
|---|---|---|
| KS1: VP step as per-transit r | N_vp must be ≥ 1 | **KILLED** — N_vp = 0.71 |
| KS2: Monotonic H₀ with distance | All N_i must be ≥ 0, increasing | **SOFT PASS** — F1 soft passes, strict fails |

---

## 14. FORWARD PATH

The VP step branch is dead. The open questions are:

1. **What IS the per-transit step?** At N = 10: 1−r ≈ 1/126. At N = 100: 1−r ≈ 1/1253. Is either of these a recognizable rational from gauge theory? The rational scan shows 1/126 ≈ best match at N ≈ 10. Is 126 a gauge-theory number? (It's 2 × 63 = 2 × 7 × 9. Not obviously from SU(3) × SU(2) × U(1).)

2. **What is N for each measurement method?** This requires published large-scale-structure catalogs along the specific lines of sight. The SDSS filament catalog or Planck lensing maps could provide boundary transit estimates. This is external data, not computation.

3. **Is the running curve model the right functional form?** H₀(N) = H₀(0) × r^N assumes exponential decay. Linear, power-law, or step-function models could also fit three data points. Without more intermediate measurements, the functional form is underdetermined.

---

**END OF REPORT**

**Experiment:** `experiment_hubble_vp_prediction_v0`, run002

**Status:** 3 PASS, 3 FAIL, 4 INFO

**Central Finding:** The VP step 1/(3π) from α running does NOT work as the per-transit H₀ correction. N_vp = 0.71 < 1 — the step is too large by ~13× at N = 10. The structural parallel between α running and H₀ running is qualitative, not quantitative. Different physics, different step sizes.

**What it proves:** The VP step hypothesis is falsified. The Hubble running model itself survives with r as a free parameter.

**What it does NOT prove:** That H₀ doesn't run. Only that it doesn't run with the specific step size from QED vacuum polarization.

---

