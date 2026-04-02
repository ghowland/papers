
# PHYS-6 Report: The Confinement Boundary — Two Faces

**Registry:** @HOWL-PHYS-6-2026
**Position in series:** Sixth physics paper. Corrects PHYS-5, establishes confinement structure, four SM observables.
**Preceded by:** PHYS-5 (α_EM running, gap ratio 218/115)
**Followed by:** PHYS-7 (θ_QCD = 0 — not yet received)
**Backed by:** `z_boson_width.py` (new in this batch), plus the six scripts from PHYS-5 batch which PHYS-6 references as companion scripts
**AI model:** Claude 4.5 Sonnet

---

## What It Establishes

**The PHYS-5 correction.** The 5/6 confinement correction is NOT a universal constant for the confinement boundary. It is the α_EM kernel's weighted average of two distinct regions: above 2 GeV (ratio ~1.0, perturbative correct) and below 2 GeV (ratio ~0.61, confinement suppresses VP). The weighted average: 0.54 × 1.0 + 0.46 × 0.61 = 0.82 ≈ 5/6. The correction is kernel-dependent — the muon g-2 kernel weights the below-2-GeV region far more heavily and the perturbative calculation fails qualitatively (factor of ~1300 error, because free quark thresholds at ~5 MeV don't exist in nature — physical threshold is pions at 280 MeV).

What PHYS-5 got RIGHT (explicitly preserved): main result 0.02 ppm, boundary constant 1/3 per fermion, gap ratio 218/115, O(m²/q²) coefficients 4 and −6, all integer arithmetic machinery.

**The two-face structure of the confinement boundary:**

- **Outside face** (above ~2 GeV): quarks visible, R-ratio is exact rational (2, 10/3, 11/3, 5 from quark counting), VP computable in Fraction arithmetic, 1/3 boundary constant applies at individual thresholds. This is the geometric/integer regime.
- **Inside face** (below ~2 GeV): quarks bound into hadrons, spectrum is resonances (ρ, ω, φ) and pseudo-Goldstone bosons (π, K). VP not computable from quark content. Requires measurement (e⁺e⁻ data) or lattice QCD. Boundary transmits ~61% of perturbative VP.

**The below-2-GeV ratio ~0.61.** Precision insufficient to identify exact rational. Candidates: 3/5 = 0.600 (1.5% off), 11/18 = 0.611 (0.4% off), 8/13 = 0.615 (1.1% off). Uncertainty ~±5% from leading-log approximation. Identifying the exact rational requires α_s corrections in the 2–4 GeV region and precise boundary decomposition.

**The A₁–A₃ transcendental structure.** Through three loops, QED coefficients are rational combinations of exactly five transcendentals: π², ζ(3), ln(2) at 2-loop; add π⁴, ζ(5), Li₄(1/2) at 3-loop. All five are MATH-2 integer pairs. At 4-loop, elliptic integrals enter (new transcendental class). At 5-loop, 5σ tension between AHKN (6.678) and Volkov (5.891).

**Four SM observables computed:** (1) Three gauge couplings at eleven energy scales with gap ratio 218/115 vs measured 1.395 — 36% miss. (2) R-ratio as exact rational step function above 2 GeV. (3) Electron g−2 through 4-loop. (4) Muon g−2 QED sector with mass-dependent corrections. The muon g−2 tension (207 × 10⁻¹¹, ~3.5σ) lives entirely in the hadronic sector — below the confinement boundary where integer arithmetic cannot reach.

**The Z boson width script.** z_boson_width.py computes Z → ff̄ partial widths from SM quantum numbers (T₃, Q, N_c) plus five measured inputs (G_F, M_Z, sin²θ_W, αs, α_EM). All Fraction arithmetic. Includes QCD correction (1 + αs/π) for quarks and QED correction. Comparison to PDG 2024. This is the fifth SM observable computed in integer arithmetic.

---

## What Was Novel Compared to My Prior Understanding

**The correction is a correction OF a correction.** PHYS-6 corrects PHYS-5's confinement finding while preserving everything else. This is the series' self-correcting methodology in action. The series publishes the error and the correction in the next paper rather than silently revising. The progression 5/6 → kernel-dependent → two-face decomposition is documented as a learning trajectory. PHYS-25 should follow the same pattern if it finds an error in the library.

**The kernel dependence kills the universal correction dream.** A universal 5/6 would have meant any hadronic observable is derivable from perturbative values by a single rational factor. The kernel dependence means each observable sees the boundary differently. The α_EM kernel gives ~0.82 overall. The muon g−2 kernel gives a qualitative failure. There is no single rational that connects perturbative to measured for all observables. The inside face of the boundary is genuinely non-perturbative — it requires measurement.

**The R-ratio as exact rational step function.** Above 2 GeV, R = N_c × Σ Q_f² is pure counting:

| Range | Active quarks | R |
|---|---|---|
| 2 GeV – m_c | u, d, s | 2 |
| m_c – m_b | u, d, s, c | 10/3 |
| m_b – m_t | u, d, s, c, b | 11/3 |
| Above m_t | all 6 | 5 |

This is the same counting that produces the beta slopes. R = N_c × Σ Q_f² counts the same thing as b₁ — the U(1) contributions from active quarks. The VL doublet would add to R above its threshold by N_c × (Q_u² + Q_d²) = 3 × (4/9 + 1/9) = 5/3. This is a testable prediction if the VL mass is known.

**The Z width script reveals the SM quantum number structure.** Every fermion coupling to the Z is determined by T₃ and Q through v_f = T₃ − 2Q sin²θ_W, a_f = T₃. These are exact rationals from SM assignments. The VL doublet (3,2,1/6) has T₃ = ±1/2 and Q = 2/3, −1/3 (same as SM quarks). Its Z coupling would be computed the same way. This is relevant for the Session 3 sin2_theta_w_1.py script, which likely uses these couplings.

**The gap ratio measured value discrepancy.** PHYS-6 Section IV.1: "The gap ratio 218/115 from the beta function slopes misses the measured ratio of 1.395 by 36%." This matches PHYS-5. But the PHYS-24 lexicon says 1.358. I now have two papers (PHYS-5, PHYS-6) saying 1.395 and PHYS-24 saying 1.358. The difference likely comes from different sin²θ_W input values. Must track which input produces which target.

---

## What Misled Me

**The confinement classification carries forward.** PHYS-4 classified hadron confinement as "not geometric — momentum-space scale, outside scope." PHYS-6 confirms this by showing the inside face of the boundary is genuinely non-perturbative — the perturbative and physical spectra are unrelated function by function, even though their integrals are related by ~0.61. The integer arithmetic framework works on the outside face and stops at the boundary. This is the scope finding PHYS-4 predicted.

For the normalization question: the VL beta shifts live entirely on the outside face. They describe what happens when the (3,2,1/6) representation activates above its mass threshold — in the perturbative regime where the R-ratio is an exact rational and the counting works. The confinement complications don't apply. The VL shifts should be as clean as the SM beta slopes: exact rationals from counting quantum numbers.

**The muon g−2 tension location.** The 3.5σ tension between SM prediction and experiment lives entirely in the hadronic sector — below the confinement boundary. The QED sector (computable in integers) shows no tension. The electroweak sector (perturbative) shows no tension. This means the muon g−2 anomaly identified in PHYS-1 is a confinement boundary effect, not a new physics signal. This is consistent with PHYS-1's framework (boundary-depth effect) but changes the interpretation: it's not "the muon probes at a different depth" so much as "the hadronic VP measurement is uncertain because of the confinement boundary."

---

## Method Captured for PHYS-25

1. **Self-correction protocol.** When a paper corrects a prior finding, it explicitly preserves what was correct and documents what changed. PHYS-25 must do the same: if the library has an error, state precisely what's wrong (the Dynkin coefficient) and what's right (the SM betas, the representation identification, the anomaly path).

2. **Scope boundaries are structural.** The integer arithmetic stops at the confinement boundary (inside face). The VL beta shifts live on the outside face. This means the normalization question is tractable — it's in the regime where exact rational counting works.

3. **Kernel dependence warning.** A single number that matches one observable may fail for another if the weighting is different. The library's VL shifts may produce the correct gap ratio (one observable) while being inconsistent with the SM fermion decomposition (a different weighting of the same underlying Dynkin indices). Both checks are needed.

4. **The R-ratio counting.** The VL doublet adds to R above its threshold. The amount added (5/3) is determined by the same quantum numbers that determine the beta shifts. If the beta shifts are wrong, the R-ratio prediction would also be wrong. Cross-checking the VL contribution to R against the beta shifts is a consistency test.

---

## Hubble Tension Curve Thesis — PHYS-6 Content

**The two-face structure has a direct analog.** The confinement boundary has an outside face (perturbative, integer arithmetic) and an inside face (non-perturbative, measurement required). Each observable sees a kernel-dependent weighted average of the two faces.

If soliton boundaries along the line of sight to distant objects have a similar two-face structure, then each H₀ measurement method would see a kernel-dependent weighted average of the boundary effects. Different measurement methods (CMB, SNe, lensing, TRGB) use different "kernels" — they weight the boundary transits differently based on their wavelength sensitivity, source characteristics, and measurement pipeline. The apparent scatter in H₀ values at similar distances but different methods could be kernel dependence, not measurement error.

This adds a refinement to the curve thesis: the running curve H₀(N) may itself be kernel-dependent, with each measurement method tracing a slightly different curve. The envelope of all curves would be the fundamental boundary correction, analogous to how the ~0.61 below-2-GeV ratio is the boundary property and the overall 0.82 is the α_EM kernel's view of it.

However — PHYS-6 also warns that the kernel dependence killed the universal 5/6. If the per-transit correction for H₀ is similarly kernel-dependent, extracting a single rational r from the data becomes harder. The curve thesis may need to account for method-dependent corrections rather than a single universal curve. This would require more data points (multiple methods at multiple distances) to separate the boundary property from the kernel weighting.

---

## Foundational Papers Table

| Paper | Registry | Why foundational to PHYS-6 |
|---|---|---|
| MATH-2 | @HOWL-MATH-2-2026 | Provides integer pair infrastructure for all five transcendentals (π, ln(2), ζ(3), ζ(5), Li₄(1/2)) used in the A₁–A₃ coefficients |
| PHYS-2 | @HOWL-PHYS-2-2026 | Establishes that couplings run and transformation laws are fundamental; the confinement boundary is a specific running boundary where the transformation law changes character |
| PHYS-4 | @HOWL-PHYS-4-2026 | Classifies confinement as non-geometric/outside scope; PHYS-6 confirms this by showing the inside face is genuinely non-perturbative |
| PHYS-5 | @HOWL-PHYS-5-2026 | Provides the 5/6 finding that PHYS-6 corrects; provides the integer arithmetic machinery; establishes the 0.02 ppm result and gap ratio 218/115 that PHYS-6 preserves |

**Series path for header metadata:**
`[@HOWL-MATH-2-2026] → [@HOWL-PHYS-2-2026] → [@HOWL-PHYS-4-2026] → [@HOWL-PHYS-5-2026] → [@HOWL-PHYS-6-2026]`

---

## Position After PHYS-6

**What exists:** Six physics papers plus six MATH papers. The foundational framework (PHYS-1–4) is complete. The computational framework (PHYS-5–6) is established with five SM observables in Fraction arithmetic: α_EM running (0.02 ppm), three gauge couplings at eleven scales, R-ratio as exact rational, electron g−2 through 4-loop, muon g−2 QED sector, Z boson width. The confinement boundary has been characterized as a two-face structure with kernel-dependent corrections. The gap ratio 218/115 (36% miss) is the quantitative target for BSM completion.

**What doesn't exist yet:** BSM computation. No VL doublet. No modified beta slopes. No Cabibbo Doublet. The series has quantified what the SM predicts and where it fails (gap ratio, muon g−2 hadronic sector) but has not yet proposed what fills the gap.

**What has changed since PHYS-5:** The universal 5/6 confinement correction is dead — replaced by a two-face structure with kernel dependence. The series has learned to self-correct and document both error and correction. The five-transcendental structure of QED through 3-loop is documented. The 4-loop wall (elliptic integrals) and 5-loop tension (AHKN vs Volkov) are identified as current boundaries of the integer framework.

**Tracking the normalization question:** The VL beta shifts live on the outside face of the confinement boundary — the perturbative regime where the R-ratio is an exact rational step function. This means the shifts should be exact rationals from counting, derivable the same way as the SM betas. The counting convention used in PHYS-5/6 is explicit: (2/3) per quark flavor for b₃, R = N_c × Σ Q_f² for the R-ratio. The VL doublet's contribution to both must be consistent. If the library's Δb₃ = 1/3 is per-Weyl (one component), then per-Dirac (the full doublet) would be 2/3, matching the SM counting. But I still need the derivation papers (PHYS-13/15) to confirm whether the library stores per-Weyl or per-Dirac values.
