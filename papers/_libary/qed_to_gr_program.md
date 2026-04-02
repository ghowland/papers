## QED-to-GR Research Program: Technical Specification

**Registry:** [@HOWL-QED-GR-PROGRAM-2026]
**Date:** April 2 2026
**Status:** Staged for execution. No results claimed. All findings from the two exploratory scans are PROPOSED, not confirmed.
**Depends on:** phys24_lib.py (21/21, 148/148), qed_predicts_gr.py (10/10), qed_gr_scan_2.py (10/10)
**Location:** ./supplementary/qed_to_gr_program.md in PHYS-25

---

### 1. PROGRAM OBJECTIVE

Determine whether the Standard Model's integer structure — specifically the SU(2) beta coefficient b₂ and the QED vacuum polarization step size α/(3π) — quantitatively connects particle physics observables to cosmological observables through soliton boundary corrections.

The program produces one of three outcomes:

**Outcome A (confirmation):** The connections sharpen under additional computation (two-loop corrections, real galaxy survey data, three-parameter fits). The integers 19 and 13 appear in derivable formulas, not just numerical coincidences. The directional H₀ prediction is testable and specific.

**Outcome B (null):** The connections dissolve. Two-loop corrections move the Λ exponent away from 57. Galaxy surveys show no directional H₀ variation. The 13 pattern proves statistical. The scan constrains this parameter set. The framework remains open for different parameterizations.

**Outcome C (partial):** Some connections sharpen, others dissolve. The surviving connections define a narrower program for the next session.

All three outcomes are useful. A and C advance the program. B constrains the search space. None is a failure.

---

### 2. THE FIVE SIGNALS TO VERIFY OR FALSIFY

Each signal has a specific verification protocol and a specific falsification criterion.

#### Signal 1: VP Step Connection

**Claim:** The per-boundary H₀ correction at N=100 transits is approximately 1× α/(3π) = 0.000774.

**Current evidence:** (1−r)/[α/(3π)] = 1.045 at N=100. Miss: 4.5%.

**Verification protocol:**
1. Compute two-loop correction to α/(3π). The two-loop VP coefficient shifts the step size by a known amount (involves ζ(3) and π² terms from A₂). Recompute the ratio with the two-loop step.
2. Test N=100 against the H₀ data points using a proper chi² fit (not the crude grid from Scan 4). Use the five H₀ data points with their published uncertainties and correlation structure.
3. Compute the expected N for a line of sight to the CMB using real galaxy survey density. If the typical line of sight crosses ~100 major structures, the signal strengthens. If it crosses ~1000 or ~10, the N=100 calibration is wrong and the VP step match is coincidental.

**Falsification criterion:** If the real galaxy survey boundary count to the CMB is outside [30, 300], the VP step connection at k=1 fails. (It could reappear at a different k for a different N, but the specific N=100 / k=1 match is dead.)

**Script to write:** `phys25_vp_step_twoloop.py` — computes the two-loop VP step size in Fraction arithmetic using A₂ from the library, and recomputes the ratio.

**Data needed:** Galaxy survey boundary count estimates. These come from published galaxy number density (~0.1 per Mpc³) times line-of-sight distance to CMB (~14 Gpc). Rough estimate: ~1400 galaxies, but "major structures" (massive enough to produce significant correction) may be ~100-200. Published catalogs (SDSS, 2MASS) provide this.

---

#### Signal 2: Cosmological Constant from α^57

**Claim:** Λ_Planck ≈ α^(3×19), where 19 = |numerator of b₂_SM|.

**Current evidence:** α^57 = 10^−121.80 vs Λ = 10^−121.54. Miss: 0.26 decades.

**Verification protocol:**
1. Account for the Λ prefactor. Λ_Planck = 2.888 × 10^−122, not 10^−122. The log₁₀(2.888) = 0.461 shifts the target from −122 to −121.539. This is already included in the scan. The remaining miss is 0.260 decades.
2. Compute two-loop b₂. The two-loop correction to b₂_SM is known analytically (involves the SM particle content at two loops). If the effective b₂ at two loops shifts from −19/6 to −19.X/6, the exponent shifts from 57 to 3 × 19.X. Check whether this closes the 0.26-decade gap.
3. Test the alternative: (α/(3π))^39 = 10^−121.33, miss 0.206 decades. This uses b₂_mod = −13/6. Check whether two-loop correction to b₂_mod closes THIS gap instead. The VL doublet version may be more accurate than the SM version.
4. Test the exact formula: Λ = α^(3 × |b₂_num|) × (prefactor). Compute what prefactor is needed to make the formula exact, and check whether it is a recognizable rational or transcendental.

**Falsification criterion:** If two-loop corrections move the effective exponent more than 3 units away from 57 (i.e., outside [54, 60]), the connection between Λ and b₂ is broken. If the needed prefactor is not a simple expression, the formula is numerology rather than structure.

**Script to write:** `phys25_lambda_from_b2.py` — computes Λ from α^(3 × b₂_num) at one-loop and two-loop, with explicit prefactor extraction.

**Data needed:** Two-loop SM beta coefficients (published, e.g., Machacek-Vaughn 1983-84). The two-loop b₂ for the SM is b₂^(2) = 136/3 (from the SM with one Higgs doublet). This shifts the effective running but the exact impact on the exponent 57 requires computation.

---

#### Signal 3: Dark Matter Ratio = (22/13)π

**Claim:** DM/baryon ≈ (22/13)π = 5.3165. Measured: 5.3204. Miss: 0.07%.

**Verification protocol:**
1. Check the measurement uncertainty. Planck 2018 gives Ω_DM = 0.2607 ± 0.0025 and Ω_b = 0.0490 ± 0.0003. The ratio DM/baryon = 5.320 ± 0.065 (propagated). The miss 0.004 is well within the 1σ uncertainty of 0.065. The hit is consistent but not constraining.
2. Test whether (22/13)π can be derived from the gauge structure. 22 = 2 × 11. 11 is the Yang-Mills universal integer (from the gauge self-coupling −11C₂/3). 13 = |b₂_mod numerator|. π enters through R₂ = π/4 (circular geometry). If DM/baryon = (2 × 11)/(|b₂_mod_num|) × π, this is a formula involving only gauge integers and circular geometry. Check whether this formula has a physical derivation from the soliton boundary picture.
3. Test with updated DM measurements. Planck 2020, ACT, SPT-3G may have updated Ω_DM and Ω_b values. Check whether the ratio has moved toward or away from (22/13)π.
4. Statistical control test. Generate 1000 random rationals p/q × π with p,q in [1, 25] and check what fraction of them land within 0.07% of any target in [4, 7]. If the expected hit rate is >10%, the match is not significant. If <1%, it is.

**Falsification criterion:** If the statistical control shows >5% expected hit rate, the match is not significant. If updated measurements move DM/baryon away from (22/13)π by >2σ, the match is dead.

**Script to write:** `phys25_dm_ratio_test.py` — statistical control (random rational × π scan) plus updated measurement comparison.

**Data needed:** Latest Planck/ACT/SPT Ω_DM and Ω_b values with uncertainties.

---

#### Signal 4: Product Form (1−r) = α²π²(20/13)

**Claim:** The per-boundary H₀ correction at N=100 is α²π² × (20/13) = 0.000809. Target: 0.000809. Miss: 0.08%.

**Verification protocol:**
1. Check what α²π² IS physically. α² = the two-loop coupling factor. π² = 32R₄ = the 4D geometric content. The product α²π² = α² × 32R₄ is the two-loop correction with 4D geometry. The coefficient 20/13 involves both 13 (b₂_mod) and 20 (= b₃_mod × 3 since b₃_mod = −20/3). Check: 20/13 = |b₃_mod × 3| / |b₂_mod_num|. This would mean the per-boundary correction involves the RATIO of SU(3) to SU(2) modified beta coefficients.
2. Verify the 20/13 interpretation. b₃_mod = −20/3. So |b₃_mod| × 3 = 20. And |b₂_mod_num| = 13. So 20/13 = (3|b₃_mod|) / |b₂_mod_num|. Check whether this algebraic relationship holds exactly in Fraction arithmetic.
3. Statistical control. Same as Signal 3: how many α^a × π^b × (p/q) expressions with small a, b, p, q land within 0.1% of the target? The scan tested 4 × 5 × 20 × 20 = 8000 combinations and found ~6 within 0.5%. Expected from random: ~40 (0.5% of 8000). The scan found FEWER than random, not more. The specific hit at 0.08% is the closest, but the overall hit rate is below random expectation.

**Falsification criterion:** If the 20/13 = (3|b₃_mod|)/|b₂_mod_num| identity does NOT hold exactly, the connection to beta coefficients is broken and the hit is numerical coincidence. If the identity holds, the connection is algebraic and warrants derivation.

**Script to write:** `phys25_product_form_verify.py` — tests the 20/13 identity against beta coefficients, performs statistical control.

**Data needed:** None beyond the library. All beta coefficients are in phys24_lib.py.

---

#### Signal 5: The 19/13 = 57/39 Exact Identity

**Claim:** The ratio of the SM and VL cosmological constant exponents equals the ratio of b₂ numerators. 57/39 = 19/13 = |b₂_SM_num|/|b₂_mod_num|. EXACT.

**Current evidence:** Verified exact in Fraction arithmetic. 10/10 PASS.

**Verification protocol:**
1. This identity is algebraic, not numerical. It does not need statistical testing. It needs PHYSICAL INTERPRETATION. Why does the exponent of the cosmological constant scale as 3 × |b₂_num|? What physical mechanism makes Λ proportional to α raised to a power determined by the SU(2) beta function?
2. Test the formula at two loops. If the two-loop effective b₂ is (−19 + δ)/6, the exponent becomes 3 × (19 − δ). Compute δ from the known two-loop coefficient and check whether the shifted exponent gives a better or worse match to Λ.
3. Test the formula for other gauge groups. If Λ ∝ α^(3 × |b₂_num|), does the same structure hold with b₁ or b₃? Compute α^(3 × |b₁_num|) = α^(3 × 41) = α^123. This gives 10^−262.8 — far below Λ. Compute α^(3 × |b₃_num|) = α^(3 × 7) = α^21. This gives 10^−44.9 — far above Λ. Only b₂ (the SU(2) coefficient) gives the right order of magnitude. This is a non-trivial selection: of the three gauge groups, only SU(2) produces an exponent in the right range.

**Falsification criterion:** If the two-loop shift moves the exponent outside [54, 60] for the SM or outside [36, 42] for the VL version, the quantitative connection to Λ is broken. The algebraic identity 57/39 = 19/13 remains true regardless — it is an algebraic fact. What can be falsified is the INTERPRETATION that these exponents have physical meaning for the cosmological constant.

**Script to write:** `phys25_b2_exponent_test.py` — tests all three gauge groups, two-loop shifts, prefactor extraction.

**Data needed:** Two-loop SM beta coefficients (published).

---

### 3. INFRASTRUCTURE REQUIREMENTS

#### 3.1 Library Extensions

The following values should be added to phys24_lib.py (or its successor) before executing the program:

| Variable | Value | Type | Purpose |
|---|---|---|---|
| H0_local | Fraction(7304, 100) | Measured | H₀ SH0ES (km/s/Mpc) |
| H0_CMB | Fraction(6736, 100) | Measured | H₀ Planck (km/s/Mpc) |
| Omega_DM | Fraction(2607, 10000) | Measured | Planck 2018 |
| Omega_b | Fraction(490, 10000) | Measured | Planck 2018 |
| G_Newton | Fraction(667430, 10**16) | Measured | m³ kg⁻¹ s⁻² |
| Lambda_obs | Fraction(11056, 10**56) | Measured | m⁻² |
| b2_SM_2loop | TBD | Derived | Two-loop SU(2) beta coefficient |

These are currently defined locally in the scan scripts. For the program proper, they belong in the library with DATA-4 entry numbers and cross-checks.

#### 3.2 External Data

| Data source | What we need | Where to get it | Format |
|---|---|---|---|
| Galaxy number density | N per Mpc³ as function of distance | SDSS DR17, 2MASS | Published tables |
| Galaxy morphology catalog | Fraction sphere vs disk vs irregular | Galaxy Zoo, SDSS | Published classification |
| Updated Ω_DM, Ω_b | Latest values with uncertainties | Planck 2020, ACT DR6 | Published papers |
| Two-loop SM betas | b_i^(2) exact rationals | Machacek-Vaughn 1983-84 | Published formulas |
| Void catalog | Void positions and sizes | SDSS void catalog | Published tables |

None of this data needs to be collected. All is published and available.

#### 3.3 Scripts to Write

| Script | What it computes | Signals tested | Priority |
|---|---|---|---|
| phys25_vp_step_twoloop.py | Two-loop VP step, recompute ratio | Signal 1 | HIGH |
| phys25_lambda_from_b2.py | Λ from α^(3×b₂_num) at 1 and 2 loop | Signal 2, 5 | HIGH |
| phys25_dm_ratio_test.py | Statistical control on (22/13)π | Signal 3 | MEDIUM |
| phys25_product_form_verify.py | 20/13 identity vs beta coefficients | Signal 4 | MEDIUM |
| phys25_b2_exponent_test.py | All three gauge groups, two-loop | Signal 5 | HIGH |
| phys25_galaxy_boundary_count.py | Estimate N per line of sight | Signal 1 | HIGH |
| phys25_directional_h0.py | Predict H₀(θ,φ) from mock census | Signal 1 | LOW |
| phys25_three_param_fit.py | Fit r_sphere, r_torus, r_void | Signals 1,3 | LOW |

Priority HIGH means: execute before writing any paper. The program cannot proceed without these results. Priority MEDIUM means: execute if HIGH scripts produce non-null results. Priority LOW means: execute if MEDIUM scripts produce non-null results.

---

### 4. DECISION TREE

```
START
  │
  ├─ Run phys25_lambda_from_b2.py
  │   ├─ Two-loop exponent in [54, 60]? 
  │   │   ├─ YES → Signal 2 survives. Continue.
  │   │   └─ NO → Signal 2 dead. Check if Signal 5 identity 
  │   │           still has physical meaning without Λ connection.
  │   │
  │   └─ Prefactor is recognizable rational/transcendental?
  │       ├─ YES → Formula candidate. Attempt derivation.
  │       └─ NO → Numerology. Park Signal 2.
  │
  ├─ Run phys25_vp_step_twoloop.py
  │   ├─ Two-loop ratio still within 10% of integer k?
  │   │   ├─ YES → Signal 1 survives. Proceed to boundary count.
  │   │   └─ NO → Signal 1 dead at this parameterization.
  │   │           Try alternative: (1-r) = alpha^2*pi^2*(20/13).
  │   │
  │   └─ Run phys25_galaxy_boundary_count.py
  │       ├─ Estimated N in [30, 300]?
  │       │   ├─ YES → VP step + boundary count consistent.
  │       │   │         Signal 1 survives. Write directional prediction.
  │       │   └─ NO → N and k don't match. Signal 1 dead.
  │
  ├─ Run phys25_product_form_verify.py
  │   ├─ 20/13 = (3|b3_mod|)/|b2_mod_num| EXACT?
  │   │   ├─ YES → Algebraic connection to beta coefficients.
  │   │   │         Signal 4 upgrades from numerical to structural.
  │   │   └─ NO → 20/13 is coincidental. Signal 4 dead.
  │   │
  │   └─ Statistical control: hit rate for random p/q?
  │       ├─ <1% → Match is significant.
  │       └─ >5% → Match is expected from random. Park Signal 4.
  │
  ├─ Run phys25_dm_ratio_test.py
  │   ├─ Statistical control: hit rate for random (p/q)*pi?
  │   │   ├─ <1% → (22/13)π is significant.
  │   │   └─ >5% → Expected from random. Signal 3 dead.
  │   │
  │   └─ Updated measurements closer to (22/13)π?
  │       ├─ YES → Signal 3 strengthens.
  │       └─ NO → Signal 3 weakens or dead.
  │
  └─ ASSESS
      ├─ 0 signals survive → Outcome B (null). Document constraints.
      │   Framework open for different parameterizations.
      │
      ├─ 1-2 signals survive → Outcome C (partial). 
      │   Narrow program to surviving signals.
      │   Write results paper on what survived and what didn't.
      │
      └─ 3+ signals survive → Outcome A (confirmation path).
          Write the QED-to-GR connection paper.
          The surviving signals define the specific formulas.
          Testable predictions go to experimentalists.
```

---

### 5. TIMELINE AND ORDERING

**Phase 1 (immediate, this session if time permits):**
- phys25_lambda_from_b2.py — the Λ exponent test is the highest-information-content computation. If 57 is wrong at two loops, half the program collapses immediately. If it's right, the entire program is energized.
- phys25_product_form_verify.py — the 20/13 identity check is pure algebra on library values. Takes 10 minutes. Immediately upgrades or kills Signal 4.

**Phase 2 (next session):**
- phys25_vp_step_twoloop.py — requires encoding the two-loop VP coefficient, which involves A₂ from the library.
- phys25_galaxy_boundary_count.py — requires looking up published galaxy density numbers.
- phys25_dm_ratio_test.py — requires the statistical control scan.

**Phase 3 (after Phase 2 results):**
- phys25_b2_exponent_test.py — comprehensive test of all gauge groups.
- phys25_directional_h0.py — directional predictions from mock or real census.
- phys25_three_param_fit.py — calibrated fit with void anti-corrections.

**Phase 4 (if Outcome A):**
- Paper: "The SU(2) Beta Coefficient and the Cosmological Constant" or similar.
- Testable predictions document for experimentalists.
- Integration with the series' existing PHYS-25 (normalization question) paper.

---

### 6. WHAT THIS PROGRAM IS NOT

This program is NOT a claim that QED produces GR. It is a search for quantitative connections between QED integers and GR observables through the soliton boundary mechanism. The connections may be coincidental, approximate, or exact. The program determines which.

This program does NOT replace the PHYS-25 normalization paper. The convention discrepancy (VL beta shifts, 2× vs 4× scalar) is a separate finding with its own resolution path. The QED-to-GR program USES the VL beta shifts but does not depend on the convention question — it uses the library values (1/15, 1, 1/3) which are supported by the gap ratio test regardless of which scalar convention produced them.

This program does NOT claim to solve the cosmological constant problem, the dark matter problem, or the Hubble tension. It claims to TEST whether these problems are connected to the SM gauge structure through specific, computable, falsifiable formulas. The formulas are stated. The tests are specified. The outcomes are enumerated.

A null result at any stage constrains THIS parameterization. It does not constrain the soliton boundary framework (which may operate through different formulas) or the HOWL series (which stands on its established results in particle physics regardless of the cosmological extension).

---

### 7. THE CRITICAL UNKNOWN

The single most important unknown in the entire program is the PHYSICAL MECHANISM by which a soliton boundary crossing produces a correction of order α/(3π) to the effective H₀. In QED, the VP correction arises from virtual pair production in the photon propagator. In the cosmological context, the analog would be: light passing through a galaxy's gravitational field interacts with the galaxy's electromagnetic structure (its plasma, magnetic fields, charged particle content) in a way that shifts the effective propagation by one VP step.

If this mechanism can be derived from first principles (the galaxy's electromagnetic content produces a VP-like correction to photon propagation), the entire program has a physical foundation. If the mechanism cannot be identified, the numerical matches remain unexplained coincidences regardless of how precise they are.

The mechanism question is PHYSICS, not computation. It requires a theoretical argument, not a scan. The scans identify WHAT the numbers are. The mechanism explains WHY.

---

**End of technical specification. This document is the operational plan for the QED-to-GR research program. It is staged, not executed. All outcomes (A, B, C) are acceptable. The program advances by computing, not by assuming.**
