# The F1 Strict Null: What the Monotonicity Failure Means

**Library:** phys24_hubble_lib.py

**Test:** F1 strict — raw H0 monotonically decreasing with distance

**Result:** FAIL

**Date:** April 3, 2026

---

## 1. The Observation

The five H₀ measurements, ordered by increasing effective distance:

| Rank | Method | H₀ (km/s/Mpc) | Uncertainty | Distance Class |
|---|---|---|---|---|
| 1 | SH0ES | 73.0 | ±1.0 | local |
| 2 | H0LiCOW | 73.3 | ±1.8 | local-medium |
| 3 | CCHP | 69.8 | ±1.7 | medium |
| 4 | DES+BAO+BBN | 67.4 | ±1.2 | high |
| 5 | Planck | 67.4 | ±0.5 | maximum |

The F1 strict test checks whether each value is less than or equal to the one before it. It fails at the first pair: H0LiCOW (73.3) > SH0ES (73.0). The sequence is not monotonically decreasing.

The F1 soft test checks whether this violation survives within 1-sigma uncertainties. SH0ES has 73.0 ± 1.0, so its upper bound is 74.0. H0LiCOW has 73.3 ± 1.8, so its lower bound is 71.5. The bands overlap by 2.5 km/s/Mpc. The soft test passes — the violation is within measurement noise.

---

## 2. What the FAIL Does NOT Mean

The FAIL does not mean the running curve hypothesis is dead. Here is why.

The running curve hypothesis says: H₀(N) = H₀(0) × r^N, where N is the effective boundary transit count. For this curve to be monotonically decreasing, every measurement at higher N must give a lower H₀. But the test assumes the ordering SH0ES → H0LiCOW → CCHP → DES → Planck corresponds to strictly increasing N. That assumption is the weak link, not the data.

SH0ES measures H₀ using Cepheid-calibrated Type Ia supernovae in local galaxies (distances ~20-40 Mpc). H0LiCOW measures H₀ using gravitational lensing time delays through a lens galaxy (distances ~hundreds of Mpc to the source, but the light passes through ONE specific foreground galaxy). The effective boundary transit count for H0LiCOW depends on the specific line of sight — it could be lower, equal to, or higher than SH0ES depending on the large-scale structure along that particular path.

The 0.3 km/s/Mpc difference (73.3 vs 73.0) is 0.4% — well within the combined 2.1 km/s/Mpc uncertainty. These two measurements are statistically indistinguishable. Assigning them to different distance classes with a strict ordering is the error, not the data.

---

## 3. What the FAIL DOES Mean

The FAIL tells us three concrete things.

**First:** SH0ES and H0LiCOW are in the same distance class. They should not be treated as distinct points on a running curve. They are two measurements of the same effective quantity — H₀ at low boundary transit count — made with different methods. Their agreement (73.0 vs 73.3, 0.4% apart) is a consistency check, not two points on a curve.

**Second:** the running curve hypothesis has at most three independent distance classes in the current data, not five:

| Class | Methods | H₀ range | Status |
|---|---|---|---|
| Local (low N) | SH0ES + H0LiCOW | 73.0 - 73.3 | Two methods agree |
| Intermediate (medium N) | CCHP | 69.8 | Single method |
| Cosmological (high N) | DES + Planck | 67.4 | Two methods agree |

Three classes, three H₀ values, strictly decreasing: 73.2 (average of local) > 69.8 > 67.4. A two-parameter model (H₀(0) and r) through three points has one degree of freedom. This is a fit, not an overdetermination. The curve thesis requires at least four independent distance classes to be testable.

**Third:** the effective boundary transit count N is the primary unknown, not r. The magnitude constraint table shows that r is fully determined once N is known. The question is not "what is r?" but "what is N for each measurement method?" This requires published large-scale structure catalogs along the specific lines of sight used by each measurement team. Without N, the curve cannot be fit.

---

## 4. What the Two Tests Together Mean

| Test | Result | Interpretation |
|---|---|---|
| F1 strict | FAIL | Raw ordering has a 0.3 km/s/Mpc inversion at rank 1-2 |
| F1 soft | PASS | The inversion is within 1-sigma measurement noise |

Together: the data is consistent with monotonic decrease but does not prove it. The inversion at rank 1-2 is noise, not signal. The real structure is three distance classes with strictly decreasing H₀.

This is the correct state for an active investigation with limited data. The hypothesis survives but is not confirmed. The falsification test did its job — it identified the weakest point in the data ordering and showed that it is not a hard violation.

---

## 5. What Would Change the Assessment

**Upgrade to FAIL (hypothesis weakened):** A future measurement at an unambiguously intermediate distance (100-500 Mpc, well-determined line of sight) that gives H₀ > 73 km/s/Mpc. This would be a genuine non-monotonic value that cannot be explained by distance class overlap.

**Upgrade to PASS (hypothesis strengthened):** Multiple measurements at different well-characterized distances that all fall on a smooth curve when plotted against estimated N. The curve would need to pass through 73.2 at low N, 69.8 at medium N, and 67.4 at high N, with intermediate values falling on the same curve.

**Kill (hypothesis dead):** Discovery of a systematic error in either the local or cosmological measurement chain that resolves the Hubble tension without any distance-dependent running. If the tension disappears, the running curve is unnecessary.

**Unlock (hypothesis testable):** Published estimates of effective boundary transit count N for each measurement method, derived from SDSS, 2dF, or Planck lensing maps of large-scale structure along the specific lines of sight. This is the blocking dependency. Without N, the curve fit is illustrative only.

---

## 6. The Data Gap

The self-test output shows:

```
UNKNOWN QUANTITIES (None values)
  SH0ES: effective_N = None
  H0LiCOW: effective_N = None
  CCHP: effective_N = None
  DES_BAO_BBN: effective_N = None
  Planck: effective_N = None

  5 of 5 measurements have unknown effective N.
  This is the primary data gap blocking the analysis.
```

Every effective_N is None. This is the honest state of the library. The running curve model H₀(N) = H₀(0) × r^N has two parameters (H₀(0) and r) and five data points, but zero of those data points have a known N coordinate. The model is underdetermined in its independent variable.

The example fit uses guessed N values [0, 5, 50, 500, 5000] and produces chi²/dof = 6.98 — a poor fit, confirming the guesses are wrong. Different N assignments would give different r values and different chi² values. Without real N values, the fit is meaningless.

The per-transit correction r is not independently unknown — it is fully determined by N through the constraint r^N = 67.4/73.0 = 337/365. Knowing N for any one measurement (other than the endpoints) would determine r and enable prediction at all other distances. This is a one-parameter problem disguised as a two-parameter problem.

---

## 7. The Structural Parallel

The alpha running computation in PHYS-5 faces none of these ambiguities because the independent variable (energy scale μ) is directly measured at every point. The effective boundary transit count for alpha running is known exactly — it is the number of quark flavor thresholds between the two energy scales. The per-threshold correction 1/(3π) = 1/(12R₂) is derived from group theory.

The Hubble running hypothesis has the same mathematical structure but none of the same certainty in the independent variable. Energy scales are measured by accelerators. Boundary transit counts for cosmological light paths are estimated from galaxy surveys with large systematic uncertainties.

This asymmetry is the fundamental difference between the two cases:

| Property | α running | H₀ running (hypothesis) |
|---|---|---|
| Independent variable known? | Yes (energy μ from accelerator) | No (N from structure catalogs, not measured) |
| Per-boundary correction derived? | Yes (Dynkin indices, group theory) | No (unknown) |
| Data points | Continuous (any μ above confinement) | 3-5 discrete distance classes |
| Model tested to | 0.02 ppm (PHYS-5) | Not tested (no N values) |

The hypothesis borrows the structure of alpha running but cannot borrow its certainty until N is known.

---

## 8. Recommendation

Keep the F1 strict FAIL in the self-test. Do not relax it. It is informative.

The FAIL tells every future session: "the raw data ordering has an inversion at rank 1-2, SH0ES and H0LiCOW are in the same distance class, and the running curve hypothesis has three effective data points, not five."

The soft PASS tells them: "the inversion is within noise and the data is consistent with monotonic decrease."

Both facts together give the correct picture: a hypothesis that survives its first contact with data but is not yet testable due to the N gap.

The next step is not more modeling. It is data: published estimates of effective boundary transit count for at least one intermediate measurement method (CCHP is the best candidate because its distance class is most distinct from both endpoints). With one N value, r is determined and the curve makes predictions at every other distance.

---

*F1 Strict Null Report. 1 FAIL out of 17 checks. The FAIL is data, not a bug. The hypothesis survives within uncertainties but cannot be tested until effective boundary transit counts are known. April 3, 2026.*
