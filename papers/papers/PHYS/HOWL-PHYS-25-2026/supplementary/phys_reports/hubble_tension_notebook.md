## Hubble Tension as Running Curve — Working Notebook

**Status:** Active investigation, not parked
**Origin:** Session 4 conversation, April 2 2026
**Context:** Arose during PHYS-5 reading, from the observation that H₀ measurements at different distances may trace a continuous running curve rather than a binary tension

---

### 1. THE THESIS

The Hubble tension is not a discrepancy between two measurements. It is an incomplete sampling of a continuous running curve.

Every H₀ measurement at a different effective distance (equivalently, different boundary transit count N) samples a different point on the curve H₀(N). The curve is parameterized by boundary transit count N. The per-transit correction factor is an exact rational. Three or more measured points overdetermine the rational, enabling prediction at any distance.

This reframes the problem from "which H₀ is correct?" to "what is the transformation law H₀(N)?"

---

### 2. SERIES FOUNDATION

The thesis connects existing series results that have not been assembled:

| Series result | Paper | Connection to H₀ curve |
|---|---|---|
| Soliton boundaries produce different readings at different depths | PHYS-1 | Each distance probes a different boundary depth |
| The transformation law is more fundamental than any single value | PHYS-2 | The H₀ running curve is the fundamental object, not 67.4 or 73.0 |
| Reproducibility within one depth ≠ universality across depths | PHYS-3 | Local H₀ measurements cluster because they sample similar depths |
| Per-transit correction must be ~0.9992 to ~0.99992 depending on N | PHYS-4 | Magnitude constraint on the per-transit rational |
| VP running through discrete boundaries matches CODATA to 0.02 ppm | PHYS-5 | Computational template — exact rational running through discrete boundaries |
| H₀ running would be Subgroup B (monotonic accumulation) | PHYS-11 | Classification predicts monotonic curve, not periodic |
| Step size for α running is 1/(3π) = 1/(12R₂), an exact Fraction | PHYS-5/11 | H₀ step size may have analogous exact rational form involving R₂ |

---

### 3. THE DATA

Available H₀ measurements sorted by effective boundary transit count (from PHYS-1 Appendix E and PHYS-4 Appendix G):

| Method | H₀ (km/s/Mpc) | Uncertainty | Effective N (relative) | Distance class |
|---|---|---|---|---|
| SH0ES (Type Ia SNe) | 73.0 | ±1.0 | Low | Local galaxies |
| H0LiCOW (lensing time delays) | 73.3 | ±1.8 | Low-medium | Through lens galaxy |
| CCHP (TRGB) | 69.8 | ±1.7 | Medium | Different calibration chain |
| DES + BAO + BBN | 67.4 | ±1.2 | High | Cosmological scale |
| Planck CMB | 67.4 | ±0.5 | Maximum | Full observable universe |

Qualitative observation: monotonic decrease with increasing N. The intermediate values (69.8, 73.3) fall between the endpoints, consistent with a continuous curve rather than a step function.

---

### 4. THE NEW MOVE

The series identified the per-transit correction as a missing theoretical piece (PHYS-4 Section IX.3). The thesis inverts the approach:

**Series approach (top-down):** Derive the per-transit correction from boundary geometry → predict the curve → compare to data.

**Curve thesis approach (bottom-up):** Fit a rational running curve to the measured H₀ values → extract the per-transit correction empirically → look for its integer origin in the boundary geometry.

The bottom-up approach requires:

1. An estimate of effective N for each measurement method (from published large-scale structure catalogs)
2. A functional form for H₀(N) — the simplest candidate is H₀(N) = H₀(0) · r^N where r is the per-transit rational correction factor
3. At least three (N, H₀) pairs to overdetermine the two-parameter fit (H₀(0) and r)

If the fit produces r as a recognizable exact rational (with integer content traceable to R₂, β, or the VP integral constants), the curve is established. If r is irrational or does not relate to known series constants, the curve thesis is not supported.

---

### 5. STRUCTURAL PARALLELS

The α running and the proposed H₀ running share structural features:

| Feature | α running (established) | H₀ running (proposed) |
|---|---|---|
| Variable | Probe energy | Effective distance / boundary count N |
| Discrete boundaries | Flavor thresholds (quark masses) | Soliton boundaries (galaxy clusters, filaments, voids) |
| Direction | α increases with energy (screening weakens) | H₀ decreases with N (cumulative correction reduces apparent value) |
| Per-boundary correction | 1/(3π) = 1/(12R₂) per unit charge² | Unknown — to be extracted |
| Subgroup (PHYS-11) | B (monotonic accumulation) | B (monotonic accumulation, predicted) |
| Exact arithmetic | Fraction, verified to 0.02 ppm | Fraction, to be verified |
| Known from counting | Beta slopes from particle species | Per-transit correction from boundary geometry (unknown) |

Key difference: for α, the per-threshold correction is derived from group theory counting (Dynkin indices, charge assignments). For H₀, the per-transit correction has no known derivation from first principles. The curve thesis proposes extracting it empirically first, then deriving.

---

### 6. MAGNITUDE CONSTRAINT

From PHYS-4 Appendix G:

The cumulative factor is 67.4/73.0 = 0.923. If H₀(N) = H₀(0) · r^N:

| Effective N | Required r | 1 − r | Character |
|---|---|---|---|
| 10 | 0.9920 | 0.0080 | ~1/125 |
| 100 | 0.99920 | 0.00080 | ~1/1250 |
| 1000 | 0.999920 | 0.000080 | ~1/12500 |
| 10000 | 0.9999920 | 0.0000080 | ~1/125000 |

The pattern: 1 − r ≈ 0.080/N. The 0.080 ≈ ln(73.0/67.4) = ln(1.083) = 0.0798.

If N is known (from structure catalogs), r is determined. If r is a recognizable fraction, the curve is established.

Note the factor 0.080 ≈ 1/(12.5). Compare to the VP running step size 1/(3π) ≈ 1/9.42 ≈ 0.106. The H₀ per-transit correction is smaller than the VP step size by a factor of ~1.3. This may or may not be significant — the comparison requires N to be known.

---

### 7. FALSIFICATION

**F1.** If intermediate H₀ measurements (TRGB, lensing, BAO) do not fall on a smooth monotonic curve when plotted against estimated N, the running curve thesis is not supported.

**F2.** If the best-fit r is not a recognizable exact rational — if it has no integer structure traceable to R₂, β, or VP integral constants — the curve exists but has no connection to the series framework.

**F3.** If the curve fit requires more than two parameters (H₀(0) and r), the simple exponential running model is insufficient. A more complex functional form may apply, or the thesis may be wrong.

**F4.** If improved measurements at intermediate distances converge to one of the endpoint values rather than maintaining distinct intermediate values, the curve collapses to a step function and the running interpretation is not supported.

**F5.** If the Hubble tension resolves through identification of a systematic error in either CMB or local measurements, the running curve is unnecessary.

---

### 8. WHAT THIS NOTEBOOK NEEDS NEXT

1. Published estimates of effective boundary count N for each H₀ measurement method (from SDSS, 2dF, Planck lensing maps).
2. A concrete fit: does H₀(N) = H₀(0) · r^N with r rational reproduce the five data points above?
3. If the fit works: what is r as an exact Fraction? Does it decompose into known series constants?
4. If the fit works: prediction for H₀ at specific intermediate distances not yet measured, stated before the measurement is performed.
5. Check whether any subsequent PHYS papers (6–24) address intermediate H₀ values or the running curve idea.

---

### 9. SERIES POSITION

This thesis was not stated in any paper read so far (PHYS-1 through PHYS-5, PHYS-11, MATH-1 through MATH-6). The series has all the pieces but assembled them as "binary tension with boundary transit correlation" (PHYS-1) and "per-transit correction is the missing theoretical piece" (PHYS-4). The reframing — continuous running curve extractable empirically from intermediate measurements — is new in this session.

If the curve thesis holds, it would be the H₀ analog of PHYS-5's α running: a transformation law in exact rational arithmetic connecting readings at different boundary depths. The paper that develops this would connect PHYS-1 (boundary catalog), PHYS-2 (transformation law priority), PHYS-4 (per-transit constraint), PHYS-5 (computational template), and PHYS-11 (Subgroup B classification).

---

**End of working notebook. Status: active. Updated: Session 4, April 2 2026.**
