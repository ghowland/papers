
You're right — let me check what's actually in this conversation right now.Good — I can see the PHYS-5 paper is document 11, and the scripts are documents 12–17 in this conversation. Let me now process the paper and all six scripts together.

---

# PHYS-5 Report: The Running of α_EM in Integer Arithmetic

**Registry:** @HOWL-PHYS-5-2026
**Position in series:** Fifth physics paper. First quantitative computation.
**Preceded by:** PHYS-4 (boundary test program)
**Followed by:** PHYS-6 (confinement boundary — two faces)
**Backed by:** `alpha_EM_final.py` (core), `alpha_em_complete.py` (complete with quarks + gap ratio), `gauge_coupling_2.py` (three couplings running), `electron_g2_2.py`, `muon_g2_2.py`, `m_w_prediction.py`
**AI model:** Claude Opus 4.6

---

## What It Establishes

The first quantitative computation in the series. The QED running of α_EM from M_Z to atomic scale, computed entirely in Fraction arithmetic:

**Central result: 1/α_EM = 137.0360025 vs CODATA 2022 137.0359992 — error 0.02 ppm.** Seven measured rationals enter (α_EM⁻¹(M_Z), three lepton masses, M_Z, hadronic VP, top VP). All transcendentals (π, ln) are integer pairs from MATH-2 at 160-term precision. Every intermediate value is a Python Fraction. No float created during computation. The result is a ratio of two integers with ~28,000-bit numerator.

**The boundary constant correction.** The unsubtracted VP constant is −5/3. Using half of this (5/6 per fermion) gives 0.24% error. The SUBTRACTED VP constant is −2/3 (subtraction removes exactly 1). Using half of this (1/3 per fermion) gives 6.5 ppm error — a 350× improvement. The correction traces through a chain of single-digit integers from the Feynman parameter integral: ∫₀¹ x(1−x)·ln(x) dx = −5/36 where 5 = 3² − 2².

**The O(m²/q²) corrections.** Coefficients +4 and −6, exact integers from the VP expansion. Including these moves the error from 6.5 ppm to 0.02 ppm. The τ lepton dominates the correction (largest mass ratio to M_Z).

**The confinement finding.** Perturbative quark VP = 5.364. Measured hadronic VP = 4.408. Ratio = 0.822. Compare to 5/6 = 0.833. Residual: 1.4%. The same 5/6 from the Feynman parameter integral, but applied to the collective confinement boundary rather than individual thresholds. Three interpretations offered (geometric, universal, coincidence). Explicitly unresolved.

**The gap ratio 218/115.** First appearance of this critical quantity. SM one-loop beta slopes 41/10, −19/6, −7. The gap ratio (b₁−b₂)/(b₂−b₃) = (109/15)/(23/6) = 218/115 = 1.896. Measured ratio at M_Z: 1.395. Miss: 36%. "The 36% is the quantitative measure of the Standard Model's incomplete particle content."

**The progression table.** Error decreases by four orders of magnitude across six stages, each from adding boundary structure — thresholds, boundary shape, boundary fine structure, measurement precision. No free parameters tuned. No loop corrections beyond one-loop added.

---

## What Was Novel Compared to My Prior Understanding

**The gap ratio originates HERE.** I had been treating 218/115 as a known quantity throughout the session. PHYS-5 is where it first appears. It is a PURE INTEGER PREDICTION — no measured value enters, no transcendental appears. The 218 and 115 come entirely from counting particle species and their charges. The 36% miss is the quantitative target: any BSM extension must modify the beta slopes to bring the predicted gap ratio to 1.395.

This is the foundation for everything in the unification lane. The Cabibbo Doublet modifies the beta slopes from (41/10, −19/6, −7) to (41/10 + Δb₁, −19/6 + Δb₂, −7 + Δb₃). The modified gap ratio becomes the test. The VL beta shifts (Δb₁, Δb₂, Δb₃) determine whether the modified ratio matches 1.395. This is WHY getting the beta shifts right matters — they determine the gap ratio, which is the primary confrontation with measurement.

**The SM betas are hardcoded from counting, not from Dynkin indices.** Section VII gives the three slopes as "exact rationals from particle counting" without reference to Dynkin indices. The script `gauge_coupling_2.py` hardcodes them:

```
b0_1 = Fraction(41, 10)
b0_2 = Fraction(-19, 6)
b0_3_6f = Fraction(-7, 1)
b0_3_5f = Fraction(-23, 3)
```

The comments explain: "n_g=3 generations, n_H=1 Higgs doublet: b0_1 = (4/3)*n_g + (1/10)*n_H = 41/10." These are the standard SM formulas from particle counting. The VL shifts, which MODIFY these betas, must be derived from the same type of counting applied to the (3,2,1/6) representation. But the SM betas themselves don't use the Dynkin index notation — they use the standard counting rules.

**The 5/6 vs 1/3 distinction.** Section III traces this carefully: 5/6 is the per-fermion constant from the UNSUBTRACTED VP, used incorrectly in the early stages (0.24% error). 1/3 is the per-fermion constant from the SUBTRACTED VP, the correct one (6.5 ppm). Then in Section V, 5/6 reappears for the COLLECTIVE confinement boundary. The distinction is structural: individual thresholds use the subtracted version (1/3), collective boundaries use the unsubtracted version (5/6). This is PHYS-6's territory.

**The six companion scripts.** These are the first scripts in the series to compute physics results:

- `alpha_EM_final.py`: Core computation. Leptonic VP only. 0.02 ppm result.
- `alpha_em_complete.py`: Adds perturbative quarks, confinement finding, gap ratio.
- `gauge_coupling_2.py`: Runs all three SM couplings from M_Z to 10¹⁶ GeV. GUT convergence analysis. Gap ratio from measured couplings.
- `electron_g2_2.py`: Electron g−2 through 5-loop. A₁ through A₃ in exact integer arithmetic.
- `muon_g2_2.py`: Muon g−2 with mass-dependent corrections. White Paper comparison.
- `m_w_prediction.py`: W boson mass from Sirlin relation with 1-loop corrections.

ALL of these use the same infrastructure: Fraction arithmetic, Machin π, arctanh series for ln, MATH-2 integer pairs. All hardcode the SM betas as exact Fractions. None uses the Dynkin index formalism from phys24_lib.py to derive the betas — they take the betas as known results from particle counting.

---

## What Misled Me

**The scripts don't use the library.** These six scripts are standalone — they don't import phys24_lib.py. They compute π, ln, and VP functions from scratch each time. The library comes later in the series (PHYS-13+ presumably). This means the VL beta shifts in phys24_lib.py were NOT derived in PHYS-5. They come from later papers. The derivation chain runs: PHYS-5 establishes SM betas → later papers extend to BSM → phys24_lib.py stores the results. I need PHYS-13/15 to find the extension step.

**The gap ratio measured value.** PHYS-5 says the measured ratio at M_Z is 1.395. The PHYS-24 lexicon says 1.358. The PHYS-6 report (from my earlier reading) also cited 1.395. This discrepancy likely reflects different input values for sin²θ_W and αs. The exact value matters because it's the TARGET the VL extension must hit. I need to track which input values each paper uses.

**The beta slope formula in `gauge_coupling_2.py`.** The comment explicitly states the counting:
- b0_1 = (4/3)·n_g + (1/10)·n_H = 41/10
- b0_2 = (4/3)·n_g − 22/3 + (1/6)·n_H = −19/6
- b0_3(6f) = (2/3)·6 − 11 = −7

The fermion contribution per generation to b₃ is (2/3) per quark flavor. Six quark flavors × 2/3 = 4. Gauge contribution −11. Total: 4 − 11 = −7. For five flavors: (2/3)·5 = 10/3. Gauge −11. Total: 10/3 − 11 = −23/3.

The (2/3) per quark flavor for SU(3) — this is the coefficient I need to trace. In the standard Weyl convention, each Dirac quark (= 2 Weyl fermions) contributes (2/3)·T(R) to the one-loop beta. For the fundamental of SU(3), T(R) = 1/2. So per Dirac quark: (2/3)·(1/2) = 1/3. But the script says (2/3)·6 − 11 = −7, meaning each quark contributes 2/3, not 1/3. This means the (2/3) ALREADY includes the factor of 2 for Dirac (two Weyl spinors). So: per Weyl fermion, T(R) = 1/2, contribution = 1/3. Per Dirac fermion = 2 Weyl, contribution = 2/3.

The library's Dynkin coefficient for (3,2,1/6) under SU(3) is 1/3 for the VL doublet. If this is per DIRAC fermion, it should be 2/3 (matching the SM counting above). If it's per WEYL fermion, 1/3 is correct but needs to be doubled for Dirac. This is EXACTLY the normalization question. PHYS-5 has now given me the SM convention: **2/3 per quark flavor for SU(3)**, which is per Dirac fermion including both Weyl components.

---

## Method Captured for PHYS-25

1. **The SM convention is explicit.** PHYS-5 and gauge_coupling_2.py use (2/3) per quark flavor for b₃. This is the Dirac convention. Per Weyl fermion it would be (1/3). The VL beta shifts in the library must be checked against this convention.

2. **The gap ratio is the primary observable.** 218/115 vs measured 1.395 (or 1.358). The VL shifts modify the numerator and denominator. The modified ratio is the test. PHYS-25 must trace: what gap ratio does the library produce, and does it match the measured value?

3. **Scripts are standalone.** They don't import the library. They hardcode SM betas. The library's Dynkin formalism is a later addition. The derivation chain for the VL shifts is in later papers, not in PHYS-5.

4. **Integer arithmetic verified.** Every intermediate is Fraction. Result has ~28,000-bit numerator. mpmath used only for verification at the end. This is the computational standard all subsequent scripts must meet.

5. **The confinement boundary is the measurement floor.** The hadronic VP uncertainty (±73 ppm) dominates the error budget. The integer arithmetic has reached the measurement floor. This explains PHYS-4's classification: confinement is outside scope (non-geometric, momentum-space).

---

## Foundational Papers Table

| Paper | Registry | Why foundational to PHYS-5 |
|---|---|---|
| MATH-1 | @HOWL-MATH-1-2026 | Provides β = π/4, the geometric invariant that the boundary constant 1/3 relates to through the VP integral |
| MATH-2 | @HOWL-MATH-2-2026 | Provides the integer pair infrastructure (π, ln as rational series at 160 terms) that makes exact Fraction arithmetic possible |
| PHYS-1 | @HOWL-PHYS-1-2026 | Provides the soliton boundary concept — the VP cloud, flavor thresholds, confinement boundary as boundary crossings |
| PHYS-3 | @HOWL-PHYS-3-2026 | Provides the running coupling comparison that PHYS-5 quantifies (α documented, αs documented, G undocumented) |
| PHYS-4 | @HOWL-PHYS-4-2026 | Provides the calibration-first principle — PHYS-5 IS Test 0 of the boundary test program, the calibration case the framework must pass |

**Series path for header metadata:**
`[@HOWL-PHYS-1-2026] → [@HOWL-MATH-1-2026] → [@HOWL-MATH-2-2026] → [@HOWL-PHYS-3-2026] → [@HOWL-PHYS-4-2026] → [@HOWL-PHYS-5-2026]`

---

## Position After PHYS-5

**What exists:** Five physics papers plus six MATH papers. The foundational framework is complete (PHYS-1 through PHYS-4). The first quantitative computation achieves 0.02 ppm for α_EM running. Six standalone scripts compute SM observables in Fraction arithmetic: α running, three gauge couplings, electron g−2 through 5-loop, muon g−2 with mass-dependent corrections, W boson mass. The gap ratio 218/115 has been computed and the 36% miss documented. The confinement finding (5/6 correction at 1.4%) is documented but unresolved.

**What doesn't exist yet:** Any BSM computation. No VL doublet. No modified beta slopes. No Cabibbo Doublet. No Dynkin index formalism. The gap ratio miss has been quantified but no candidate particle has been proposed to close it. The unification lane opens after PHYS-5 — the quantitative question is: what particle content changes 218/115 to hit 1.395?

**What has changed since PHYS-4:** The series has made the transition from conceptual (PHYS-1–4) to computational (PHYS-5). The computational infrastructure is established: Fraction arithmetic, MATH-2 integer pairs, standalone scripts, 100-digit verification. The gap ratio target is set. The SM betas are established with an explicit convention: (2/3) per quark flavor for SU(3), which is the Dirac counting.

**Tracking the normalization question:** PHYS-5 provides a critical anchor. The SM beta convention is (2/3) per quark flavor for b₃, where each quark flavor is a Dirac fermion. The library's Dynkin coefficient for the VL doublet under SU(3) is 1/3. If this is the Weyl contribution (one component of a Dirac fermion), it must be doubled to get the Dirac contribution 2/3, matching the SM convention. If the library already accounts for Dirac counting internally (multiplying by 2 somewhere in the beta formula), then 1/3 is the Dynkin index and the factor of 2 is applied elsewhere. The resolution requires reading phys24_lib.py's beta shift formula AND the derivation papers (PHYS-13/15). The SM anchor point is now clear: b₃ = (2/3)·n_f − 11.
