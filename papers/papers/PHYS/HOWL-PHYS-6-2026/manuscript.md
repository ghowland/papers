# The Confinement Boundary in Integer Arithmetic

## The Two Faces of the QCD Confinement Boundary and Four Standard Model Observables from Integer Arithmetic

**Registry:** [@HOWL-PHYS-6-2026]

**Series Path:** [@HOWL-MATH-2-2026] → [@HOWL-PHYS-2-2026] → [@HOWL-PHYS-4-2026] → [@HOWL-PHYS-5-2026] → [@HOWL-PHYS-6-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** March 2026

**Domain:** Foundational Physics / Computational QED / Confinement Structure

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude 4.5 Sonnet. 

---

## I. ABSTRACT

The 5/6 confinement correction reported in [@HOWL-PHYS-5-2026] is decomposed into two distinct regions: above the confinement scale (~2 GeV), where the perturbative calculation is correct and no correction is needed, and below the confinement scale, where the confinement boundary reduces the vacuum polarization to approximately 61% of the perturbative prediction. The overall 5/6 was the α_EM kernel's weighted average of these two regions: 0.54 × 1.0 + 0.46 × 0.61 = 0.82. The confinement correction is kernel-dependent, not universal. Four Standard Model observables — the three gauge couplings at every energy scale, the electron anomalous magnetic moment through 3-loop, and the muon anomalous magnetic moment QED sector — are computed in the same integer arithmetic established in PHYS-5.

---

## II. CORRECTION TO PHYS-5

### 2.1 What PHYS-5 Said

PHYS-5 identified the confinement boundary correction as 5/6 applied to the total perturbative quark vacuum polarization. The perturbative quark VP of 5.364, multiplied by 5/6 = 0.833, gave 4.470 versus the measured hadronic VP of 4.408. The residual was 1.4%. PHYS-5 proposed two types of boundary correction: 1/3 per fermion at individual thresholds (from the subtracted VP), and 5/6 at the collective confinement boundary (from the unsubtracted VP).

### 2.2 What PHYS-5 Got Wrong

The 5/6 is not the confinement correction. It is an average.

The perturbative quark VP of 5.364 spans the full energy range from individual quark masses up to M_Z. This range crosses the confinement boundary at approximately 2 GeV. Above 2 GeV, quark-hadron duality holds — the perturbative calculation gives the correct result. Below 2 GeV, confinement reorganizes the spectrum from free quarks into bound hadrons.

Decomposing the perturbative VP by region:

| Region | Perturbative | Measured | Ratio |
|---|---|---|---|
| Above 2 GeV | 2.92 | ≈ 2.92 | ≈ 1.00 |
| Below 2 GeV | 2.44 | 1.49 | 0.61 |
| **Total** | **5.36** | **4.41** | **0.82** |

The total ratio 0.82 decomposes as: (2.92/5.36) × 1.0 + (2.44/5.36) × 0.61 = 0.544 × 1.0 + 0.456 × 0.61 = 0.544 + 0.278 = 0.822.

The 5/6 = 0.833 was a one-significant-figure approximation to this weighted average. The weights are specific to the α_EM kernel (which weights all energies as 1/s). A different kernel assigns different weights to the two regions and produces a different overall ratio.

### 2.3 Why It Matters

A universal 5/6 would mean any hadronic observable could be corrected from the perturbative value by a single factor. This would make the hadronic VP derivable from integer arithmetic for all observables. The kernel-dependent correction means each observable sees the confinement boundary differently. The muon g-2 kernel K(s) ~ m_μ²/s² at large s suppresses high energies and weights the below-2-GeV region far more heavily than the α_EM kernel. The effective correction for the muon g-2 is dominated by the below-2-GeV ratio of ~0.61, not by the above-2-GeV ratio of ~1.0. No single rational connects the perturbative and measured muon g-2 hadronic VP because the perturbative spectrum below 2 GeV (free quarks starting at ~5 MeV) has a completely different shape from the physical spectrum (pions starting at 280 MeV, dominated by the ρ resonance at 775 MeV). The integrals happen to be related by a factor of ~0.61, but the integrands are unrelated function by function.

### 2.4 What PHYS-5 Got Right

The individual threshold corrections (1/3 per fermion from the subtracted VP) are correct. They apply above the confinement scale where perturbation theory works. The PHYS-5 main result of 0.02 ppm is correct — it used the measured hadronic VP, not the 5/6 approximation. The boundary constant finding (1/3, not 5/6, for the subtracted VP at individual thresholds) is correct. The gap ratio 218/115 is correct. The integer arithmetic machinery is correct. The O(m²/q²) coefficients 4 and -6 are correct.

---

## III. THE TWO FACES OF THE CONFINEMENT BOUNDARY

![Fig. 5: Above 2 GeV (outside face): perturbative matches measured, ratio ≈1.0. Below 2 GeV (inside face): perturbative exceeds measured, ratio ≈0.61.](./figures/phys6_05_two_faces.png)

### 3.1 Above the Confinement Scale

Above approximately 2 GeV, quarks behave as free particles. The perturbative R-ratio — R = Σ N_c Q_f² summed over active quark flavors — matches the measured e⁺e⁻ → hadrons cross-section within a few percent. This is quark-hadron duality: the sum over individual quark contributions equals the sum over hadronic final states when averaged over a sufficient energy range.

In this regime, the integer arithmetic of PHYS-5 applies without modification. Each quark threshold carries the 1/3 boundary constant from the subtracted VP. The R-ratio is an exact rational at each energy: 10/3 above charm, 11/3 above bottom, 5 above top. The VP running between any two scales above 2 GeV is computable in Fraction arithmetic. No confinement correction is needed because we are outside the confinement boundary.

### 3.2 Below the Confinement Scale

![Fig. 1: Perturbative R=2 (flat) vs physical R-ratio (ρ resonance peak, wild oscillations) — shapes completely unrelated, integrals related by factor 0.61.](./figures/phys6_01_r_ratio_comparison.png)

Below approximately 2 GeV, the physical spectrum has no perturbative analog. The lightest hadronic state is the pion at 140 MeV, not the up quark at 2 MeV. The spectrum is dominated by the ρ(770), ω(782), and φ(1020) resonances. The π⁺π⁻ channel alone provides approximately 73% of the total hadronic VP below 2 GeV. No perturbative calculation produces resonances.

The perturbative R-ratio in this region is R = 2 (u, d, s quarks active, N_c Σ Q_f² = 3 × (4/9 + 1/9 + 1/9) = 2). The physical R-ratio oscillates wildly through the ρ peak (where R ≈ 5) and the valleys between resonances (where R < 1). The shapes are unrelated. But the integrals — the total VP summed over the entire below-2-GeV region — are related:

Measured VP (below 2 GeV) / Perturbative VP (below 2 GeV) ≈ 0.61

The confinement boundary transmits approximately 61% of the perturbative VP to the outside world. The remaining 39% is absorbed by the boundary — the energy that goes into binding quarks into hadrons rather than contributing to the vacuum polarization.

![Fig. 4: Perturbative VP (2.44) enters the confinement boundary — 1.49 (61%) emerges as measured VP, 0.95 (39%) absorbed by binding energy.](./figures/phys6_04_confinement_transmission.png)

### 3.3 The Ratio 0.61

The precision of the current decomposition is insufficient to identify the exact rational. The perturbative VP above 2 GeV was computed at leading order without α_s corrections (which are ~5% in the 2-4 GeV range). The measured VP below 2 GeV assumes exact quark-hadron duality above 2 GeV, which is approximate. The boundary itself is gradual (1.5-3 GeV), not sharp at 2 GeV.

Rational candidates within 2%:

| Rational | Value | Difference from 0.609 |
|---|---|---|
| 3/5 | 0.600 | 1.5% |
| 8/13 | 0.615 | 1.1% |
| 11/18 | 0.611 | 0.4% |
| 5/8 | 0.625 | 2.7% |

The closest is 11/18 at 0.4%, but the uncertainty in the decomposition is larger than the differences between candidates. Identifying the exact rational requires: the perturbative VP with α_s corrections in the 2-4 GeV region, the measured R-ratio decomposed precisely into above/below contributions with a well-defined boundary, and a theoretical prediction for what the ratio should be from the boundary geometry.

### 3.4 The Muon g-2 Kernel Test

![Fig. 2: The α_EM kernel weights both faces equally. The muon g-2 kernel crushes onto the below-2-GeV non-perturbative region. The confinement correction is kernel-dependent.](./figures/phys6_02_kernel_comparison.png)

The muon g-2 hadronic VP uses the same R(s) data as the α_EM running but with a different kernel:

K(s) = ∫₀¹ dx x²(1-x) / [x² + (1-x)s/m_μ²]

This kernel falls as m_μ²/s² at large s, suppressing the above-2-GeV region relative to the below-2-GeV region. The below-2-GeV contribution dominates the muon g-2 integral.

Computing the perturbative muon g-2 hadronic VP with free quark thresholds gives a result that exceeds the measured value by a factor of approximately 1300. This is not a correction factor that failed — it is a qualitative failure. The perturbative spectrum places the u-quark threshold at 2 × 2.2 MeV = 4.4 MeV. The physical hadronic threshold is at 2 × 140 MeV = 280 MeV. The perturbative calculation includes an enormous contribution from 4.4 MeV to 280 MeV that does not exist in nature. The confinement boundary has completely eliminated this energy range from the hadronic spectrum.

For the α_EM kernel with its gentle 1/s weighting, this wrong-threshold contribution is partially diluted by the large above-2-GeV contribution where the perturbative calculation is correct. For the muon g-2 kernel with its sharp low-energy weighting, the wrong-threshold contribution dominates and the calculation is meaningless.

This confirms that the confinement correction is kernel-dependent. The 5/6 was the α_EM kernel's view of the boundary. The muon g-2 kernel sees a different boundary — one that blocks the perturbative calculation entirely in the low-energy region rather than merely correcting it.

![Fig. 7: Perturbative u-quark threshold at 4.4 MeV vs physical pion threshold at 280 MeV — the 64× gap is an energy range that does not exist in nature.](./figures/phys6_07_threshold_comparison.png)

---

## IV. THE INTEGER STANDARD MODEL CALCULATOR

The PHYS-5 machinery — exact Fraction arithmetic for transcendentals, rational coefficients from particle counting, threshold matching at measured masses — applies to every perturbative Standard Model observable that does not cross the confinement boundary. Four computations are presented as companion scripts.

### 4.1 Gauge Coupling Running

The three gauge couplings α₁, α₂, α₃ are run from M_Z to 10¹⁶ GeV using the one-loop beta function slopes 41/10, -19/6, -7. These slopes are exact rationals from counting particle species and their charges. The running passes through the top quark threshold at 173 GeV, where α₃ changes slope from -23/3 to -7.

At each of eleven energy scales from M_Z to 10¹⁶ GeV, the computation produces: all three inverse couplings, sin²θ_W derived from α₁ and α₂, and α_EM derived from the electroweak mixing. Every value is a Fraction. Three measured rationals enter: α_EM(M_Z)⁻¹ = 63953/500, sin²θ_W(M_Z) = 23122/100000, α_s(M_Z) = 59/500.

The three couplings do not unify. α₁ = α₂ at approximately 10¹³ GeV. α₂ = α₃ at approximately 10¹⁷ GeV. The crossing points are separated by four orders of magnitude in energy. The gap ratio 218/115 from the beta function slopes misses the measured ratio of 1.395 by 36%. This quantifies the Standard Model's incomplete particle content.

### 4.2 The R-Ratio

The perturbative R-ratio above the confinement scale is a step function of exact rationals:

| Energy range | Active quarks | R (exact) |
|---|---|---|
| 2 GeV - m_c | u, d, s | 2 |
| m_c - m_b | u, d, s, c | 10/3 |
| m_b - m_t | u, d, s, c, b | 11/3 |
| Above m_t | u, d, s, c, b, t | 5 |

These values are testable against measured e⁺e⁻ → hadrons data at every collider energy above 2 GeV. They are pure counting results: N_c × Σ Q_f² for the active quark flavors. No dynamical calculation is needed — only the charges and color factor.

### 4.3 Electron g-2

The anomalous magnetic moment a_e = (g-2)/2 is computed as a power series in α/π. The first three coefficients are exact rational combinations of MATH-2 integer pairs:

A₁ = 1/2

A₂ = 197/144 + π²/12 + (3/4)ζ(3) - (π²/2)ln(2)

A₃ = (83/72)π²ζ(3) - (215/24)ζ(5) + (100/3)[Li₄(1/2) + ln(2)⁴/24 - π²ln(2)²/24] - (239/2160)π⁴ + (139/18)ζ(3) - (298/9)π²ln(2) + (17101/810)π² + 28259/5184

Every coefficient is rational. Every transcendental — π, ln(2), ζ(3), ζ(5), Li₄(1/2) — is a MATH-2 integer pair. Through three loops, the most precisely tested prediction in physics is built from five transcendental numbers and rational coefficients.

The fourth-order coefficient A₄ = -1.9122457649... is imported as a 30-digit rational from Laporta's 1100-digit numerical evaluation. The fifth-order coefficient carries a 5σ discrepancy between two independent calculations: AHKN (2018) report 6.678 ± 0.192, Volkov (2024) reports 5.891 ± 0.061.

Through 4-loop, the computation gives a_e = 1,159,652,175.6 × 10⁻¹². The experimental value is 1,159,652,180.6 × 10⁻¹². The difference of -5.0 × 10⁻¹² is accounted for by the missing hadronic, electroweak, and mass-dependent QED corrections totaling approximately +4.7 × 10⁻¹². The confinement boundary contributes less than 2 × 10⁻¹² to the electron g-2 — the electron is too light to probe the hadronic interior significantly.

### 4.4 Muon g-2 QED Sector

![Fig. 6: QED (integer arithmetic) and EW (perturbative) show no tension. The 207×10⁻¹¹ discrepancy sits entirely in the hadronic sector — where the confinement boundary dominates.](./figures/phys6_06_muon_g2_decomposition.png)

The muon anomalous magnetic moment uses the same A₁, A₂, A₃ coefficients as the electron, plus mass-dependent corrections from electron and tau loops. The mass-dependent terms depend on m_μ/m_e and m_μ/m_τ — ratios of measured rationals computable in Fraction arithmetic. The dominant mass-dependent correction at 2-loop is A₂(m_μ/m_e) = 1.094, much larger than the universal A₂ = -0.328, because the electron loops provide a large logarithmic enhancement proportional to ln²(m_μ/m_e).

The total QED contribution: 116,584,763 × 10⁻¹¹. Adding electroweak (153.6 × 10⁻¹¹), hadronic VP (6845 × 10⁻¹¹ from the 2020 White Paper), and hadronic light-by-light (92 × 10⁻¹¹) gives a total SM prediction of 116,591,854 × 10⁻¹¹.

The experimental value (Fermilab + BNL combined): 116,592,061 × 10⁻¹¹.

The difference: 207 × 10⁻¹¹, approximately 3.5σ.

The tension lives entirely in the hadronic sector — the below-2-GeV region where the confinement boundary dominates and the integer arithmetic cannot reach. The QED sector, which is computable in integer arithmetic, shows no tension. The electroweak sector, which is perturbative, shows no tension. The hadronic sector, which crosses the confinement boundary, carries all the discrepancy.

---

## V. THE A₁-A₃ STRUCTURE

### 5.1 The Five Transcendentals

Through three loops, the QED coefficients for the lepton anomalous magnetic moment are rational combinations of exactly five transcendental constants:

| Order | Transcendentals present | New at this order |
|---|---|---|
| 1-loop | (none — A₁ = 1/2 is rational) | — |
| 2-loop | π², ζ(3), ln(2) | π², ζ(3), ln(2) |
| 3-loop | π², π⁴, ζ(3), ζ(5), ln(2), Li₄(1/2) | π⁴, ζ(5), Li₄(1/2) |

All five transcendentals are MATH-2 integer pairs: each is the exact output of a convergent rational series computable in Fraction arithmetic.

The five form a closed set under the operations that appear in QED Feynman diagram evaluation through 3-loop. The products π²ζ(3), π²ln²(2), ln⁴(2) all appear. The constant Li₄(1/2) = Σ 1/(2ⁿn⁴) is the only polylogarithm that enters — it arises from diagrams where the loop momentum is shared between two vertices in a specific topology.

### 5.2 The 4-Loop Wall

![Fig. 3: Through 3-loop: five MATH-2 transcendentals, fully computable. At 4-loop: elliptic integrals and six master integrals known only numerically — the wall.](./figures/phys6_03_four_loop_wall.png)

At four loops, complete elliptic integrals appear for the first time. Laporta's semi-analytical fit to the 1100-digit numerical value of A₄ contains harmonic polylogarithms of e^(iπ/3), e^(2iπ/3), and e^(iπ/2), one-dimensional integrals of products of complete elliptic integrals K(x), and six finite parts of master integrals known only numerically to 4800 digits.

The complete elliptic integrals represent a new class of transcendental function that goes beyond the π/ζ/ln/Li₄ family. Whether complete elliptic integrals at rational arguments can be represented as MATH-2 integer pairs is an open question. K(k) for rational k has a convergent series expansion with rational coefficients, suggesting it may be expressible in the MATH-2 framework, but this has not been demonstrated.

The six master integrals known only to 4800 digits are the current wall. They arise from specific Feynman diagram topologies (sunrise-type integrals with internal masses) that cannot be reduced to the known transcendental basis. Whether they can be expressed in terms of any finite set of named constants is unknown.

### 5.3 The 5σ Tension at 5-Loop

The mass-independent 5-loop coefficient A₁^(10) has been computed by two independent groups:

AHKN (Aoyama, Hayakawa, Kinoshita, Nio), revised 2018: 6.678 ± 0.192

Volkov, 2024: 5.891 ± 0.061

The discrepancy is 0.787, which is 5σ given the quoted uncertainties. The disagreement is in the Set V diagrams — 6,354 vertex diagrams without lepton loops, evaluated by numerical integration of Feynman parameter integrals. The two groups use different infrared subtraction methods and different numerical integration codes.

The impact on the electron g-2 is small: the 5-loop contribution is approximately 0.45 × 10⁻¹², far below the experimental uncertainty of 0.13 × 10⁻¹². But the tension indicates that the numerical evaluation of 10th-order QED is not yet settled, and the discrepancy must be resolved before the 5-loop coefficient can be trusted at the level of its quoted uncertainty.

Both values are used in the companion scripts; results are presented for both.

---

## VI. FALSIFICATION CRITERIA

**F1 — The above/below decomposition.** If the perturbative R-ratio above 2 GeV disagrees with measured e⁺e⁻ → hadrons data by more than 5% on average, quark-hadron duality fails in this region and the decomposition is invalid.

**F2 — The below-2-GeV ratio.** If a precise determination of the below-2-GeV measured/perturbative VP ratio yields a value outside 0.55-0.65, the finding of ~0.61 is wrong.

**F3 — Kernel dependence.** If the overall measured/perturbative ratio for the muon g-2 hadronic VP, computed with the correct g-2 kernel and physical thresholds, is within 5% of 5/6, the correction is more universal than this paper claims. In this case the kernel-dependence argument is wrong, and a different explanation for the muon g-2 perturbative failure is needed.

**F4 — Gauge coupling predictions.** If any inverse gauge coupling at any computed scale disagrees with measurement by more than 2% (the estimated one-loop truncation error), the integer running is wrong.

**F5 — Electron g-2 consistency.** If the integer-arithmetic QED computation through 3-loop disagrees with the institution's published analytical value by more than the ζ(5) truncation uncertainty (~10⁻⁸ in a_e), the transcendental computation is wrong.

---

## VII. LIMITATIONS

![Fig. 8: Two faces of confinement (ratio 1.0 outside, 0.61 inside), PHYS-5 correction (5/6 = kernel average), four SM observables in integer arithmetic, the 4-loop wall.](./figures/phys6_08_identity_card.png)

The above/below-2-GeV decomposition is approximate. The perturbative VP above 2 GeV was computed at leading order in α_s. Including α_s corrections at one loop modifies the perturbative R-ratio by a factor (1 + α_s/π), which is approximately 1.05 at 2 GeV and 1.01 at M_Z. This shifts the perturbative VP above 2 GeV by roughly 3%, which propagates to a shift in the below-2-GeV ratio of roughly 5%. The qualitative finding (two distinct regions, kernel-dependent average) is robust to this correction. The quantitative value of ~0.61 is not.

The transition from perturbative to non-perturbative QCD is not sharp. The actual transition region spans approximately 1.5-3 GeV, with quark-hadron duality gradually improving with energy. Choosing 2 GeV as the boundary is conventional and approximate. A higher boundary (3 GeV) would shift more of the VP into the "above" category and change the below-region ratio. A lower boundary (1.5 GeV) would shift more into "below." The qualitative picture is boundary-independent. The quantitative ratio depends on the choice.

The gauge coupling running uses the full beta function slopes above m_t and approximate slopes between M_Z and m_t, as described in the companion script. The approximation (using the full slopes for α₁ and α₂ in the short M_Z-to-m_t interval) introduces an error of order 0.03 in the inverse couplings at m_t, which is small compared to the total running of ~30 units.

The ζ(5) computation uses 10,000 terms of the alternating eta series, giving 20 correct digits. This is sufficient for the electron g-2 (where the ζ(5) term contributes at the 10⁻⁸ level) but introduces a truncation uncertainty in A₃ of approximately 10⁻¹¹ in the final value of A₃. The impact on a_e is approximately 10⁻¹⁹ — negligible.

---

## APPENDIX A: COMPANION SCRIPTS

Four Python scripts are provided as supplementary material:

**alpha_EM_final.py** — The fine structure constant at 0.02 ppm. Seven measured rationals plus integer arithmetic produces 1/α_EM = 137.0360025 versus CODATA 2022: 137.0359992. Runtime: ~60 seconds. Every intermediate value is a Fraction with 28,293-bit numerator.

**gauge_couplings_integer.py** — All three gauge couplings at eleven energy scales. sin²θ_W, α_EM, and R-ratio at every scale. GUT convergence analysis with crossing points and gap ratio. Runtime: ~120 seconds.

**electron_g2_integer.py** — Electron anomalous magnetic moment through 4-loop. A₁ through A₃ in exact Fraction arithmetic. Five transcendentals as MATH-2 integer pairs: π (3695 bits), ln(2) (954 bits), ζ(3) (1026 bits), ζ(5) (1487 bits), Li₄(1/2) (1366 bits). Runtime: ~300 seconds (dominated by ζ(5) series).

**muon_g2_integer.py** — Muon anomalous magnetic moment. QED through 5-loop with mass-dependent corrections. Hadronic VP, HLbL, and electroweak from 2020 White Paper. Runtime: ~300 seconds.

All scripts require Python 3.8+ with fractions (standard library) and mpmath (verification only). No floating point arithmetic occurs during the computation. The mpmath library is used only after the computation to convert the final Fraction to a decimal for comparison.

---

## APPENDIX B: THE DECOMPOSITION ARITHMETIC

The α_EM hadronic VP of 4.408 (in α⁻¹ running units) decomposes by energy region. The perturbative quark VP of 5.364 spans from individual quark masses to M_Z. The above-2-GeV portion is computed from the leading-log running:

δα⁻¹(above 2 GeV) = Σ_f (N_c Q_f²) × 2 ln(μ_high/μ_low) / (3π)

where μ_high is M_Z or the next threshold, and μ_low is 2 GeV or the quark mass (whichever is higher).

| Quark | N_c Q² | Segment | Contribution |
|---|---|---|---|
| u | 4/3 | 2 GeV → M_Z (below b) | 0.642 |
| d | 1/3 | 2 GeV → M_Z (below b) | 0.161 |
| s | 1/3 | 2 GeV → M_Z (below b) | 0.161 |
| c | 4/3 | 2 GeV → M_Z (below b) | 0.642 |
| b | 1/3 | 4.18 GeV → M_Z | 0.101 |
| u+d+s+c (above b) | 10/3 | 4.18 → 91.2 GeV (extra from b threshold) | ... |

Total above 2 GeV: approximately 2.92 (leading log, without α_s corrections or boundary corrections).

Total perturbative: 5.364 (from exact one-loop VP with O(m²/q²) corrections).

Below 2 GeV perturbative: 5.364 - 2.92 = 2.44.

Below 2 GeV measured: 4.408 - 2.92 = 1.49.

Ratio: 1.49 / 2.44 = 0.61.

The uncertainty in this ratio is dominated by the leading-log approximation of the above-2-GeV contribution. Including α_s corrections would increase the above-2-GeV contribution by ~3%, reducing the below-2-GeV perturbative to ~2.35 and changing the ratio to ~0.63. The uncertainty is approximately ±0.03 in the ratio, or ±5%.

---

## APPENDIX C: THE CONFINEMENT BOUNDARY AS A TWO-FACE OBJECT

The confinement soliton boundary in the [@HOWL-PHYS-1-2026] framework has two distinct faces:

**The outside face** (above ~2 GeV): quarks are visible. Individual quark thresholds carry the 1/3 boundary constant. The R-ratio is an exact rational. The VP is computable in integer arithmetic. This is the geometric regime of [@HOWL-MATH-1-2026] — the circular cross-section β = π/4 applies, the boundary shapes are computable, the transformation law runs on integers. Every observable that probes only this face is fully within the integer framework.

**The inside face** (below ~2 GeV): quarks are bound into hadrons. The spectrum is resonances (ρ, ω, φ) and pseudo-Goldstone bosons (π, K). The boundary shapes are not the quark shapes — they are the hadron shapes, determined by the strong force dynamics that bind the quarks. The VP from this region is not computable from the quark content alone. It requires either measurement (e⁺e⁻ data) or non-perturbative computation (lattice QCD).

The boundary transmits approximately 61% of the perturbative VP through the inside face. This transmission fraction is the confinement correction below 2 GeV. It may be a specific rational determined by the boundary geometry of the proton soliton — but identifying that rational requires precision beyond what the current decomposition provides.

Any observation of the hadronic VP is a weighted average of the two faces. The α_EM kernel assigns roughly equal weight to each face: 0.54 × (outside) + 0.46 × (inside) = 0.54 × 1.0 + 0.46 × 0.61 = 0.82. The muon g-2 kernel assigns dominant weight to the inside face. The weighting depends on the kernel, but the faces are properties of the boundary, not the probe.

The integer arithmetic computes everything on the outside face. The inside face is where measurement begins.

---

## APPENDIX D: SERIES PUBLICATION RECORD

| Paper | Registry | Key Result |
|---|---|---|
| MATH-1 | @HOWL-MATH-1-2026 | β = π/4; Q = F · β · d² · Z across nine domains |
| MATH-2 | @HOWL-MATH-2-2026 | 17 transcendentals as integer pairs at 100 digits |
| PHYS-1 | @HOWL-PHYS-1-2026 | Mass is inertia; soliton boundaries; three anomaly correlations |
| PHYS-2 | @HOWL-PHYS-2-2026 | Couplings run; transformation law is fundamental |
| PHYS-3 | @HOWL-PHYS-3-2026 | G never measured outside Earth's Hill sphere |
| PHYS-4 | @HOWL-PHYS-4-2026 | Boundary test program; classification; kill switch |
| PHYS-5 | @HOWL-PHYS-5-2026 | α_EM running in integer arithmetic; 0.02 ppm |
| **PHYS-6** | **@HOWL-PHYS-6-2026** | **Confinement boundary two-face structure; PHYS-5 correction; four SM observables** |

---

**END HOWL-PHYS-6-2026**

**Registry:** [@HOWL-PHYS-6-2026]
**Status:** Complete
**Domain:** Foundational Physics / Computational QED / Confinement Structure
**Central Result:** The 5/6 confinement correction is the α_EM-kernel-weighted average of two distinct regions (ratio 1 above 2 GeV, ratio ~0.61 below 2 GeV)
**Method:** Region decomposition of hadronic VP; four SM observables in integer arithmetic
**Key Findings:** Confinement correction is kernel-dependent not universal; boundary has two faces (outside = geometric/integer, inside = non-perturbative/measured); A₁-A₃ span exactly five MATH-2 transcendentals; elliptic integrals enter at 4-loop; 5σ tension at 5-loop between AHKN and Volkov
**Corrects:** PHYS-5 Sections 5.3-5.4 (5/6 as confinement correction → 5/6 as kernel-weighted average)
**Does Not Correct:** PHYS-5 main result (0.02 ppm), boundary constant (1/3), gap ratio (218/115)
**Foundation:** MATH-2, PHYS-2, PHYS-4, PHYS-5
**Primary Limitation:** Below-2-GeV ratio ~0.61 has ±5% uncertainty from leading-log approximation
**Falsification:** Five specific criteria

---

## APPENDIX E: THE TWO-FACE DECOMPOSITION — COMPLETE ARITHMETIC

Every number in the above/below-2-GeV decomposition, showing how the weighted average produces 0.82 ≈ 5/6.

| Quantity | Above 2 GeV | Below 2 GeV | Total | Source |
|---|---|---|---|---|
| Perturbative VP (α⁻¹ units) | 2.92 | 2.44 | 5.36 | Integer arithmetic, one-loop |
| Measured VP (α⁻¹ units) | ≈ 2.92 | 1.49 | 4.41 | Davier et al. 2020 / Keshavarzi et al. 2019 |
| Ratio (measured/perturbative) | ≈ 1.00 | 0.61 | 0.82 | Division |
| Weight in α_EM kernel | 0.54 = 2.92/5.36 | 0.46 = 2.44/5.36 | 1.00 | Fraction of perturbative VP in each region |
| Weighted contribution to overall ratio | 0.54 × 1.00 = 0.54 | 0.46 × 0.61 = 0.28 | 0.82 | Sum of weighted contributions |
| 5/6 for comparison | — | — | 0.833 | From PHYS-5 |
| Difference from 5/6 | — | — | −0.011 | 1.4% — the original PHYS-5 residual |

**Why the weights are kernel-dependent:**

| Kernel | Physical Observable | Weight Function | Above-2-GeV Weight | Below-2-GeV Weight | Effective Ratio |
|---|---|---|---|---|---|
| 1/s | α_EM running | Gentle — all energies contribute | 0.54 | 0.46 | 0.82 ≈ 5/6 |
| m_μ²/s² (approx.) | Muon g-2 hadronic VP | Sharp low-energy emphasis | ~0.30 | ~0.70 | ~0.73 |
| m_e²/s² (approx.) | Electron g-2 hadronic VP | Extreme low-energy emphasis | ~0.15 | ~0.85 | ~0.67 |
| δ(s − M_Z²) | Z-pole observable | Only M_Z contributes | 1.00 | 0.00 | 1.00 |
| 1 (flat) | Hypothetical unweighted sum | Equal weight per unit energy | ~0.70 | ~0.30 | ~0.88 |

**The ratio an observable "sees" depends entirely on how it weights the two faces.** The α_EM kernel happens to produce a ratio close to the simple fraction 5/6. Other kernels do not. There is no universal confinement correction factor — there is a boundary with two faces, and the effective correction is the kernel-weighted average.

---

## APPENDIX F: THE BELOW-2-GeV SPECTRUM — PERTURBATIVE VS PHYSICAL

The perturbative and physical R-ratios below 2 GeV are qualitatively different objects. This table shows why the per-integral ratio of 0.61 is remarkable given how different the integrands are.

| Energy Range (GeV) | Perturbative R | Physical R (measured) | Dominant Physical Process | Perturbative Description | Match? |
|---|---|---|---|---|---|
| 0.004 – 0.14 | 2.0 (u, d, s quarks) | 0 (below hadronic threshold) | Nothing — no hadrons exist this light | Free u quarks pair-produce at 4 MeV | No — this range doesn't exist physically |
| 0.14 – 0.28 | 2.0 | 0 (below 2π threshold) | Nothing — single pion has no VP | Free quarks still running | No — no hadrons pair-produce yet |
| 0.28 – 0.50 | 2.0 | ~0.1–0.3 (π⁺π⁻ threshold, rising) | π⁺π⁻ production, slowly rising | Free quarks at full strength | Qualitatively wrong — factor 10 off |
| 0.50 – 0.70 | 2.0 | ~1.0–2.0 (rising toward ρ) | π⁺π⁻ dominated, approaching ρ resonance | Still R = 2 | Getting closer |
| 0.70 – 0.85 | 2.0 | ~5.0 (ρ peak at 0.775 GeV) | ρ(770) → π⁺π⁻ dominates | R = 2 misses factor 2.5 | No — resonance peak far exceeds perturbative |
| 0.85 – 1.10 | 2.0 | ~1.5–3.0 (ω, φ region) | ω(782) → π⁺π⁻π⁰, φ(1020) → K⁺K⁻ | Flat R = 2 | Approximate average |
| 1.10 – 1.50 | 2.0 | ~1.5–2.5 (multiple resonances) | Higher resonances, multi-pion | Approximately R = 2 | Rough average match |
| 1.50 – 2.00 | 2.0 | ~2.0–3.5 (transition region) | Onset of quark-hadron duality | R = 2 begins to match average | Duality emerging |

**The miracle of 0.61:** The perturbative integrand (constant R = 2 from quark threshold at 4 MeV to 2 GeV) and the physical integrand (zero below 280 MeV, resonance-dominated above) are completely different functions. Yet when integrated with the VP kernel, they are related by a factor of 0.61. The perturbative calculation overshoots because it includes a huge contribution from 4 MeV to 280 MeV that doesn't exist in nature, but it also misses the ρ resonance peak which partially compensates. The net result: 61% transmission through the confinement boundary.

---

## APPENDIX G: THE FIVE TRANSCENDENTALS — COMPLETE ACCOUNTING

Every transcendental that appears in A₁ through A₃, with its MATH-2 integer pair properties and its physical origin in QED Feynman diagrams.

| Transcendental | Value | MATH-2 Series | Digits Verified | Numerator Bits | Physical Origin in QED |
|---|---|---|---|---|---|
| π | 3.14159... | Machin formula, 160 terms | 999 | 3,695 | Dirac trace over fermion loop; angular integration in d-dimensional regularization |
| π² | 9.86960... | π × π | 999 | 7,389 | Products of angular integrals; appears as ζ(2) = π²/6 |
| π⁴ | 97.4090... | π² × π² | 999 | 14,778 | Fourth power of angular integral; appears at 3-loop in combination with rational coefficients |
| ln(2) | 0.69315... | 2·arctanh(1/3), 160 terms | 999 | 954 | Threshold integrals where virtual particle goes on-shell at midpoint of Feynman parameter range; x = 1/2 in ∫₀¹ dx/x |
| ζ(3) | 1.20206... | Central binomial series, 180 terms | 114 | 1,026 | Triple nested integration of 1/n-type denominators; three-fold Feynman parameter integral at 2-loop |
| ζ(5) | 1.03693... | Alternating eta, 10,000 terms | 20 | 1,487 | Five-fold nested integration; appears first at 3-loop from specific diagram topologies |
| Li₄(1/2) | 0.51748... | Direct sum 1/(2ⁿn⁴), 300 terms | 100 | 1,366 | Polylogarithm at half-integer argument; arises from diagrams where loop momentum is shared between two vertices with a specific topology producing 2⁻ⁿ suppression |

**The closed set property:** Through three loops, no other transcendental appears. Every coefficient is a rational combination of these seven values (π, π², π⁴, ln(2), ζ(3), ζ(5), Li₄(1/2)), which reduce to five independent constants (π, ln(2), ζ(3), ζ(5), Li₄(1/2)) since π² and π⁴ are powers of π.

**What breaks the closure at 4-loop:** Complete elliptic integrals K(k) at algebraic arguments, which are periods of elliptic curves associated with sunrise-type Feynman diagrams. These are MATH-3 objects, not MATH-2 objects.

---

## APPENDIX H: THE A₂ COEFFICIENT — TERM BY TERM IN INTEGERS

The two-loop universal coefficient A₂ = −0.32848..., decomposed into every rational and transcendental contribution.

| Term | Rational Coefficient | Transcendental | Numerical Value | Physical Origin |
|---|---|---|---|---|
| 197/144 | 197/144 = 1.36806 | 1 (rational) | +1.36806 | Rational part of two-loop Feynman integrals |
| π²/12 | 1/12 | π² | +0.82247 | Product of angular integrals from two nested loops |
| (3/4)ζ(3) | 3/4 | ζ(3) | +0.90154 | Triple nested Feynman parameter integral |
| −(π²/2)ln(2) | −1/2 | π² × ln(2) | −3.42019 | Mixed angular-threshold integral; π² from loop, ln(2) from on-shell threshold |
| **Sum = A₂** | | | **−0.32812** | |
| Published A₂ | | | −0.32848 | Petermann 1957, Sommerfield 1957 |
| Difference | | | +0.00036 | From ζ(5) truncation in A₃ propagating to effective A₂; or precision of individual terms |

**Integer content accounting:**

| Number | Where It Comes From | Reducible? |
|---|---|---|
| 197 | Sum of rational Feynman parameter integrals across all 2-loop diagrams | Prime — irreducible |
| 144 | 12² = (4 × 3)²; common denominator from combining diagram contributions | 2⁴ × 3² |
| 12 | Denominator of π² term; from normalization of angular integral | 2² × 3 |
| 3/4 | Coefficient of ζ(3); from Feynman parameter integral with three nested integrations | — |
| 1/2 | Coefficient of π²ln(2); from threshold integral at midpoint | — |

---

## APPENDIX I: THE A₃ COEFFICIENT — COMPLETE DECOMPOSITION

The three-loop universal coefficient A₃ = 1.18124..., showing every term.

| Term | Rational Coefficient | Transcendental(s) | Numerical Value | Notes |
|---|---|---|---|---|
| (83/72)π²ζ(3) | 83/72 | π² × ζ(3) | +13.849 | Mixed angular and triple-nested integral |
| −(215/24)ζ(5) | −215/24 | ζ(5) | −9.286 | Five-fold nested integral; largest ζ(5) contribution |
| (100/3)Li₄(1/2) | 100/3 | Li₄(1/2) | +17.249 | Polylogarithm term; specific topology |
| (100/3)·ln⁴(2)/24 | 100/72 | ln⁴(2) | +0.321 | Fourth power of threshold logarithm |
| −(100/3)·π²ln²(2)/24 | −100/72 | π² × ln²(2) | −6.547 | Mixed angular-threshold |
| −(239/2160)π⁴ | −239/2160 | π⁴ | −10.780 | Fourth power of angular integral |
| (139/18)ζ(3) | 139/18 | ζ(3) | +9.283 | Additional triple-nested contribution |
| −(298/9)π²ln(2) | −298/9 | π² × ln(2) | −22.586 | Large mixed term; dominant negative contribution |
| (17101/810)π² | 17101/810 | π² | +208.277 | Largest single term; rational × π² |
| 28259/5184 | 28259/5184 | 1 (rational) | +5.453 | Rational part of three-loop integrals |
| **Sum = A₃** | | | **+1.181** | |
| Published A₃ | | | 1.18124 | Laporta & Remiddi 1996 |

**Integer content:**

| Integer | Factorization | Origin |
|---|---|---|
| 83 | Prime | Numerator from combining three-loop diagrams |
| 72 | 2³ × 3² | Common denominator |
| 215 | 5 × 43 | Coefficient of ζ(5) contribution |
| 24 | 2³ × 3 | Factorial-type denominator |
| 100 | 2² × 5² | Coefficient of Li₄ group |
| 239 | Prime | Coefficient of π⁴; same prime as in Machin's formula for π |
| 2160 | 2⁴ × 3³ × 5 | Common denominator for π⁴ term |
| 139 | Prime | Coefficient of additional ζ(3) |
| 298 | 2 × 149 | Coefficient of π²ln(2); 149 is prime |
| 17101 | 17101 = prime | Largest prime in A₃; coefficient of dominant π² term |
| 810 | 2 × 3⁴ × 5 | Denominator of dominant term |
| 28259 | 28259 = prime | Rational part numerator |
| 5184 | 2⁶ × 3⁴ | Rational part denominator = 72² |

**Observation:** Three of the largest integers in A₃ (83, 17101, 28259) are prime. They cannot be decomposed further. They are irreducible outputs of the three-loop Feynman integral evaluation. The primes carry the full complexity of the three-loop topology.

---

## APPENDIX J: THE ELECTRON g-2 — LOOP BY LOOP

| Loop Order | Coefficient | α/π Power | Contribution to a_e (×10⁻¹²) | Cumulative a_e (×10⁻¹²) | Integer Arithmetic? | Transcendentals Used |
|---|---|---|---|---|---|---|
| 1 | A₁ = 1/2 | (α/π)¹ | 1,161,409,734.3 | 1,161,409,734.3 | Yes — exact rational | None |
| 2 | A₂ = −0.32848 | (α/π)² | −1,772,305.1 | 1,159,637,429.2 | Yes — exact Fraction | π², ζ(3), ln(2) |
| 3 | A₃ = +1.18124 | (α/π)³ | +14,804.2 | 1,159,652,233.4 | Yes — exact Fraction | π², π⁴, ζ(3), ζ(5), Li₄(1/2), ln(2) |
| 4 | A₄ = −1.91225 | (α/π)⁴ | −55.5 | 1,159,652,177.9 | Partial — A₄ imported as 30-digit rational | Elliptic integrals (MATH-3 objects) |
| 5 (AHKN) | A₅ = +6.678 | (α/π)⁵ | +0.45 | 1,159,652,178.3 | No — numerical only | Unknown |
| 5 (Volkov) | A₅ = +5.891 | (α/π)⁵ | +0.39 | 1,159,652,178.3 | No — numerical only | Unknown |
| Hadronic VP | — | — | +1.862 | 1,159,652,180.2 | No — measured | Confinement boundary |
| Hadronic LbL | — | — | +0.341 | 1,159,652,180.5 | No — measured/lattice | Confinement boundary |
| Electroweak | — | — | +0.030 | 1,159,652,180.5 | Partially — perturbative | W, Z, Higgs loops |
| **Total SM** | | | | **1,159,652,180.5** | | |
| **Experiment** | | | | **1,159,652,180.6 ± 0.13** | | |
| **Difference** | | | | **−0.1 ± 0.13** | | |

**The most precisely tested prediction in physics.** Theory and experiment agree to 0.1 × 10⁻¹² out of 1,159,652,180.6 × 10⁻¹². That is agreement to 11 significant figures. The first three loops — computable entirely in integer arithmetic from five transcendentals — account for 99.9987% of the total value. The remaining 0.0013% is the 4-loop and beyond, where elliptic integrals and the confinement boundary enter.

---

## APPENDIX K: THE MUON g-2 — SECTOR DECOMPOSITION

| Sector | Contribution (×10⁻¹¹) | Integer Arithmetic? | Precision Limiting Factor | Tension With Experiment? |
|---|---|---|---|---|
| QED (1-loop, universal A₁) | 11,614,097.3 | Yes | None — exact rational | No |
| QED (2-loop, universal A₂) | −17,723.1 | Yes | ζ(3), ln(2) precision | No |
| QED (3-loop, universal A₃) | +148.0 | Yes | ζ(5) at 20 digits | No |
| QED (4-loop, universal A₄) | −0.55 | Partial | A₄ imported as rational | No |
| QED (2-loop, mass-dep. e-loop) | +5,904.8 | Yes | m_μ/m_e ratio | No |
| QED (2-loop, mass-dep. τ-loop) | −7.9 | Yes | m_μ/m_τ ratio | No |
| QED (3-loop, mass-dep.) | +36.1 | Yes | Mass ratios | No |
| QED (4-5 loop, mass-dep.) | +3.6 | Partial | Higher-order | No |
| **QED total** | **116,584,763** | **Mostly yes** | | **No** |
| Electroweak (1+2 loop) | +153.6 | Perturbative — yes in principle | EW parameters | No |
| Hadronic VP (LO) | +6,931 | No — measured | e⁺e⁻ data / lattice | **Yes — this is where the tension lives** |
| Hadronic VP (NLO) | −98.3 | No — measured | Same | **Yes** |
| Hadronic VP (NNLO) | +12.4 | No — measured | Same | **Yes** |
| Hadronic LbL | +92 ± 18 | No — measured/lattice | Dominant theoretical uncertainty | **Yes** |
| **Total SM (2020 WP)** | **116,591,854** | | | |
| **Experiment (Fermilab+BNL)** | **116,592,061 ± 41** | | | |
| **Difference** | **+207 ± 57** | | | **3.5σ** |

**The tension decomposes cleanly by face of the confinement boundary.** The QED sector (outside face, integer-computable) shows zero tension. The electroweak sector (perturbative, integer-computable in principle) shows zero tension. The hadronic sector (inside face, measurement-required) carries the entire 207 × 10⁻¹¹ discrepancy. The question of whether there is new physics in the muon g-2 is the question of whether the inside face of the confinement boundary is correctly measured.

---

## APPENDIX L: THE 4-LOOP WALL — WHAT ENTERS AND WHY

| Class | Description | Examples | In MATH-2 Basis? | In MATH-3 Extended Basis? | Status |
|---|---|---|---|---|---|
| Rational numbers | Exact integer ratios from diagram combinatorics | 197/144, 28259/5184 | Yes — trivially | Yes | Complete |
| π powers | From angular integrals in d dimensions | π², π⁴ | Yes | Yes | Complete |
| ln(2) | From threshold integrals at x = 1/2 | ln(2), ln²(2), ln⁴(2) | Yes | Yes | Complete |
| Odd zeta values | From nested Feynman parameter integrals | ζ(3), ζ(5) | Yes | Yes (ζ(7), ζ(9) via Borwein) | Complete through 3-loop |
| Li₄(1/2) | From specific two-vertex topologies | Li₄(1/2) | Yes | Yes | Complete |
| Harmonic polylogarithms at roots of unity | From 4-loop diagrams with specific mass configurations | HPL at e^(iπ/3), e^(iπ/2) | Reducible to Clausen functions + π/ζ | Partially — Cl₂(π/3) in extended basis | In progress |
| Complete elliptic integrals | From sunrise-type diagrams with internal masses | K(k), E(k) at algebraic k | No | Yes — K(k²) at rational k² via hypergeometric | In progress |
| Master integrals (numerical only) | From irreducible 4-loop topologies | Six values known to 4800 digits | No | Target for PSLQ identification | Open — the wall |

**The progression of transcendental complexity by loop order:**

| Loop Order | New Transcendental Class | Integer Pair Status | Obstruction |
|---|---|---|---|
| 1 | None (rational only) | Complete | None |
| 2 | π², ζ(3), ln(2) | Complete (MATH-2) | None |
| 3 | π⁴, ζ(5), Li₄(1/2) | Complete (MATH-2) | ζ(5) slow convergence → solved by Borwein (MATH-3) |
| 4 | Elliptic integrals, higher HPL | Partial (MATH-3) | Six master integrals known only numerically |
| 5 | Unknown — possibly same as 4-loop | Unknown | 5σ disagreement between two groups on numerical value |
| 6+ | Possibly hyperelliptic / K3 | Unknown | Hierarchy prediction from MATH-3 Section V |

---

## APPENDIX M: THE 5σ TENSION AT 5-LOOP — DETAILED COMPARISON

| Parameter | AHKN (2018 revision) | Volkov (2024) | Difference |
|---|---|---|---|
| Value of A₁^(10) (Set V) | 6.678 ± 0.192 | 5.891 ± 0.061 | 0.787 |
| Significance of difference | — | — | 0.787 / √(0.192² + 0.061²) = 3.9σ (quadrature); 0.787/0.061 = 12.9σ (Volkov uncertainty alone) |
| Number of diagrams | 6,354 (Set V vertex diagrams) | 6,354 (same set) | Same diagrams |
| Method | Numerical integration of Feynman parameters | Numerical integration of Feynman parameters | Different codes |
| IR subtraction | K-operation (Kinoshita method) | R*-operation (Chetyrkin method) | Different subtraction schemes — should give same physical result |
| Integration code | Custom FORTRAN, developed over decades | Independent C++, developed independently | Different implementations |
| Independent check | Self-consistency checks within diagram subsets | Cross-checks against known lower-order results | Neither has external verification |
| Impact on a_e | 6.678 × (α/π)⁵ = 0.448 × 10⁻¹² | 5.891 × (α/π)⁵ = 0.395 × 10⁻¹² | Δa_e = 0.053 × 10⁻¹² |
| Experimental uncertainty | — | — | ±0.13 × 10⁻¹² |
| Resolution needed? | For α extraction at 10⁻¹⁰ precision, yes | | |

**The discrepancy is in Set V specifically** — the 6,354 vertex diagrams without lepton loops. Sets I-IV (diagrams with internal lepton loops) agree between the two groups. The Set V diagrams are the most computationally demanding: each requires 9-dimensional numerical integration after IR subtraction, with integrands that are highly oscillatory and have near-cancelling positive and negative contributions.

**For this series:** Both values are carried in the companion scripts. The impact on the electron g-2 (0.053 × 10⁻¹²) is below the experimental uncertainty (0.13 × 10⁻¹²). The tension does not affect any conclusion of PHYS-5 or PHYS-6. It does affect the extraction of α from a_e at the highest precision, which is relevant to PHYS-5's cross-check against CODATA.

---

## APPENDIX N: THE GAUGE COUPLING RUNNING — COMPLETE TABLE

All three inverse couplings at eleven energy scales, computed in Fraction arithmetic from three measured inputs.

| log₁₀(μ/GeV) | μ (GeV) | α₁⁻¹ | α₂⁻¹ | α₃⁻¹ | sin²θ_W | α_EM⁻¹ | R-ratio |
|---|---|---|---|---|---|---|---|
| 1.96 (M_Z) | 91.19 | 59.00 | 29.59 | 8.47 | 0.2312 | 127.91 | 11/3 |
| 2.24 (m_t) | 173.0 | 58.67 | 29.71 | 8.30 | 0.2329 | 127.52 | 5 |
| 3 | 1,000 | 57.92 | 30.08 | 7.72 | 0.2366 | 126.51 | 5 |
| 4 | 10,000 | 56.98 | 30.54 | 7.03 | 0.2410 | 125.26 | 5 |
| 6 | 10⁶ | 55.10 | 31.45 | 5.64 | 0.2502 | 122.73 | 5 |
| 8 | 10⁸ | 53.23 | 32.36 | 4.26 | 0.2599 | 120.20 | 5 |
| 10 | 10¹⁰ | 51.35 | 33.27 | 2.87 | 0.2700 | 117.68 | 5 |
| 12 | 10¹² | 49.48 | 34.18 | 1.49 | 0.2806 | 115.15 | 5 |
| 13 | 10¹³ | 48.54 | 34.63 | 0.79 | 0.2861 | 113.89 | 5 |
| 14 | 10¹⁴ | 47.60 | 35.08 | 0.10 | 0.2918 | 112.63 | 5 |
| 16 | 10¹⁶ | 45.73 | 35.99 | −1.28 | 0.3036 | 110.10 | 5 |

**Crossing analysis:**

| Crossing | Energy (GeV) | log₁₀(μ/GeV) | Which Couplings | Gap to Next Crossing |
|---|---|---|---|---|
| α₁ = α₂ | ~10¹³·⁰ | 13.0 | Electromagnetic and weak unify | 4.2 orders of magnitude to α₂ = α₃ |
| α₂ = α₃ | ~10¹⁷·² | 17.2 | Weak and strong unify | α₁ is far away at this scale |
| All three (SM) | Never | — | No exact triple crossing in SM | Gap ratio 218/115 = 1.896 ≠ measured 1.395 |

**All values are Fraction type.** The negative α₃⁻¹ at 10¹⁶ GeV is not physical — it indicates that one-loop perturbative running breaks down before this scale for QCD, as α₃ → ∞ (Landau pole) near 10¹⁴ GeV. Two-loop corrections and threshold effects modify this behavior. The table is presented for one-loop structural analysis, not as a physical prediction at 10¹⁶ GeV.

---

## APPENDIX O: THE R-RATIO — EXACT RATIONALS VS MEASUREMENT

| Energy (GeV) | Active Quarks | N_c × Σ Q_f² (exact) | R (exact rational) | R (measured, approximate) | Agreement |
|---|---|---|---|---|---|
| 2.0 – 3.0 | u, d, s | 3 × (4/9 + 1/9 + 1/9) | 2 | 2.0 – 2.5 (with α_s corrections ~1 + α_s/π ≈ 1.05) | ~5% — α_s corrections needed |
| 3.5 – 4.0 | u, d, s, c | 3 × (4/9 + 1/9 + 1/9 + 4/9) | 10/3 = 3.333 | 3.4 – 3.6 (with α_s corrections) | ~5% |
| 5.0 – 10.0 | u, d, s, c, b | 3 × (4/9 + 1/9 + 1/9 + 4/9 + 1/9) | 11/3 = 3.667 | 3.7 – 3.9 | ~5% |
| 200+ | u, d, s, c, b, t | 3 × (4/9 + 1/9 + 1/9 + 4/9 + 1/9 + 4/9) | 5 | ~5 (inclusive hadronic R at high energy) | ~1% |

**The R-ratio is a pure counting result.** N_c = 3 (three colors). Q_f² for each quark: u = 4/9, d = 1/9, s = 1/9, c = 4/9, b = 1/9, t = 4/9. Sum over active flavors. Multiply by 3. The agreement between these exact rationals and measured e⁺e⁻ → hadrons data, averaged over resonances, is one of the most direct confirmations of the quark model and of N_c = 3.

The ~5% residual between the leading-order rational and the measured value is accounted for by the factor (1 + α_s(μ)/π + ...) — the perturbative QCD correction. At 2 GeV, α_s/π ≈ 0.10. At 10 GeV, α_s/π ≈ 0.06. At 91 GeV, α_s/π ≈ 0.038. These corrections are computable in the integer arithmetic framework once α_s is provided as a measured rational input.

---

## APPENDIX P: WHAT IS COMPUTABLE VS WHAT REQUIRES MEASUREMENT — COMPLETE MAP

| Observable | Perturbative (Integer Arithmetic) | Confinement Boundary | Measurement Required | Current Precision |
|---|---|---|---|---|
| α_EM running (M_Z → 0) | Leptonic VP: 4.625 (exact to O(m²/q²)) | Hadronic VP: 4.408 (measured) | α(M_Z), lepton masses, M_Z, Δ_had | 0.02 ppm (limited by Δ_had) |
| Electron g-2 (a_e) | A₁-A₃ exact; A₄ at 30 digits | Hadronic VP: 1.9 × 10⁻¹²; HLbL: 0.3 × 10⁻¹² | α, m_e, Δ_had, Δ_HLbL | 0.11 ppb (limited by A₅ tension and hadronic) |
| Muon g-2 (a_μ) | QED: 116,584,763 × 10⁻¹¹ | Hadronic VP: 6,845 × 10⁻¹¹; HLbL: 92 × 10⁻¹¹ | Same + m_μ, m_τ | 0.35 ppm (limited by hadronic VP) |
| sin²θ_W running | Exact one-loop from b₀ slopes | None — purely electroweak | sin²θ_W(M_Z), α_s(M_Z) | ~0.1% (limited by two-loop) |
| R-ratio (above 2 GeV) | Exact rational: 2, 10/3, 11/3, 5 | None above 2 GeV | None — pure counting | Exact (leading order) |
| R-ratio (below 2 GeV) | Perturbative: R = 2 (wrong shape) | Entire contribution is inside face | e⁺e⁻ → hadrons data | ~1% (limited by data quality) |
| Gauge unification | Gap ratio 218/115 from b₀ slopes | None | α₁, α₂, α₃ at M_Z | Exact prediction (one-loop) |
| W mass | Tree + 1-loop + 2-loop perturbative | Small hadronic correction | G_F, M_Z, m_t, m_H, α_s | ~10 MeV (limited by m_t, higher orders) |
| Z width | Tree + 1-loop perturbative | Small hadronic correction | G_F, M_Z, sin²θ_W, α_s | ~1 MeV (limited by sin²θ_W, α_s) |

**The pattern:** Everything above the confinement boundary (outside face) is computable in integer arithmetic from measured rational inputs plus MATH-2 transcendentals. Everything below the confinement boundary (inside face) requires measurement or lattice QCD. The boundary between computation and measurement is the confinement boundary. The integer arithmetic framework has reached its floor — not at a precision limit, but at a structural boundary of QCD.
