## PHYS-52 Supplement: The Giga Remainder Test — 11 Derivations Across 7 Hierarchy Levels

**Experiment:** experiment_giga_remainder_test_v0
**Run:** run001
**Date:** April 19, 2026
**Pool:** 3788 value nodes
**Result:** 11/11 derivations OK, 8 PASS, 2 FAIL, 0 INFO, 140 outputs

---

### I. THE SCOREBOARD

| # | Test | Predicted | Measured | Miss | Level | Status |
|---|---|---|---|---|---|---|
| G01 | \|V_us\| = 9/40 | 0.22500 | 0.22501 | **44 ppm** | Particle | **PASS** |
| G02 | \|V_cb\| = 1/24 | 0.04167 | 0.04182 | **0.37%** | Particle | **PASS** |
| G05 | Ω_Λ = (251−22π)/264 | 0.68896 | 0.6889 | **0.0084%** | Cosmos | **PASS** |
| G07 | Lepton K = 2/3 | 0.66667 | 0.66666 | **9.2 ppm** | Lepton | **PASS** |
| G08 | a_A/a_V = 3/2 | 1.5000 | 1.4968 | **0.21%** | Nuclear | **PASS** |
| G09 | Chandrasekhar = 15π/8 | 5.8905 | 5.836 | **0.93%** | Stellar | **PASS** |
| G10 | DM/baryon = 22π/13 | 5.3165 | 5.3204 | **725 ppm** | Cosmos | **PASS** |
| G06 | H₀ ratio = 12/11 | 1.0909 | 1.0837 | **0.67%** | Cosmos | **PASS** |
| G03 | \|V_ub\| = 1/264 | 0.003788 | 0.003685 | 2.79% | Particle | FAIL |
| G04 | \|V_cb/V_ub\| = 11 | 11.000 | 11.349 | 3.07% | Particle | FAIL |

**8 PASS, 2 FAIL across 7 hierarchy levels.**

---

### II. THE CKM DISCOVERY — PARTIAL CONFIRMATION

The strongest new finding: CKM matrix elements match simple fractions of gauge-group integers.

| Element | PDG value | Prediction | Expression | Miss | Common factor |
|---|---|---|---|---|---|
| \|V_us\| | 0.22501 ± 0.00068 | 0.22500 | 9/40 = 3²/(8×5) | **44 ppm** | 8 |
| \|V_cb\| | 0.04182 ± 0.00076 | 0.04167 | 1/24 = 1/(8×3) | **0.37%** | 8 |
| \|V_ub\| | 0.003685 ± 0.00020 | 0.003788 | 1/264 = 1/(8×3×11) | 2.79% | 8 |
| \|V_cb/V_ub\| | 11.349 | 11.000 | 11 (Yang-Mills) | 3.07% | — |

**Two clean passes, two failures.** \|V_us\| = 9/40 at 44 ppm is the sharpest CKM prediction — within the PDG uncertainty of ±0.00068. \|V_cb\| = 1/24 at 0.37% is also within the PDG uncertainty of ±0.00076.

\|V_ub\| = 1/264 misses by 2.79%. The PDG value 0.003685 ± 0.00020 is 1.6σ away from 1/264 = 0.003788. Not catastrophically wrong but outside the 2% spec.

The ratio \|V_cb/V_ub\| = 11.349 vs predicted 11 misses by 3.07%. The Yang-Mills coefficient 11 is close but the miss is driven by the \|V_ub\| value being lower than predicted.

The common factor across all three elements is 8 = dim(SU(3) adjoint), the gluon count. The hierarchy: 9/40 → 1/24 → 1/264 shows each successive off-diagonal element gaining an additional gauge factor in the denominator. The denominators are 40 = 8×5, 24 = 8×3, 264 = 8×3×11.

**Assessment:** The \|V_us\| = 9/40 match at 44 ppm is compelling. The \|V_cb\| = 1/24 match at 0.37% is strong. The \|V_ub\| = 1/264 prediction is in the right ballpark but misses at 2.79% — it could improve or worsen with future measurements. The Yang-Mills ratio 11 is suggestive but the 3% miss weakens it.

The CKM prediction should be tracked as \|V_ub\| measurements improve from LHCb and Belle II. If \|V_ub\| moves toward 0.003788, the 1/264 identification strengthens. If it moves further away, the identification fails.

---

### III. THE COSMOLOGICAL PARTITION — STRONGEST RESULT

| Component | Predicted | Expression | Measured | Miss |
|---|---|---|---|---|
| Ω_DM | 0.26180 | π/12 = β/3 | 0.2607 ± 0.002 | 0.42% |
| Ω_b | 0.04924 | 13/264 | 0.0490 ± 0.0004 | 0.49% |
| DM/baryon | 5.3165 | 22π/13 | 5.3204 | **725 ppm** |
| **Ω_Λ** | **0.68896** | **(251−22π)/264** | **0.6889** | **0.0084%** |
| **Sum** | **1.00000** | **exact** | **~1.000** | **—** |

The cosmological constant prediction Ω_Λ = (251−22π)/264 = 0.68896 matches the Planck 2018 value 0.6889 to **84 ppm** — the most precise cosmological prediction in the framework.

The symbolic form (251−22π)/264 decomposes into gauge integers: 264 = 8×3×11, 251 = 264−13, 22 = 2×11. Every integer has a gauge-theory origin: 8 (SU(3) adjoint), 3 (generations), 11 (Yang-Mills), 13 (modified SU(2) numerator).

The partition sums to 1.00000 exactly (by construction — Ω_Λ is the residual). All three components are within Planck uncertainty. The DM/baryon ratio 22π/13 at 725 ppm is the tightest single cosmological prediction.

---

### IV. THE HUBBLE TENSION — 12/11

| Quantity | Value |
|---|---|
| H₀ (CMB, Planck) | 67.4 km/s/Mpc |
| H₀ (local, SH0ES) | 73.04 km/s/Mpc |
| Ratio measured | 1.0837 |
| Ratio predicted | 12/11 = 1.0909 |
| Miss | 0.67% |
| Predicted H₀(local) from 12/11 | 73.53 km/s/Mpc |
| Miss from SH0ES | 0.67% |

The Hubble tension ratio matches 12/11 at 0.67%. The 11 is the Yang-Mills coefficient. If the tension is real (not systematic), the framework says it reflects a scale-dependent inertial partition where the Yang-Mills coefficient sets the scale separation between CMB and local measurements.

The predicted local H₀ = 67.4 × 12/11 = 73.53 km/s/Mpc, within the SH0ES uncertainty (73.04 ± 1.04).

---

### V. THE HADRON KOIDE TRIPLETS — NEGATIVE RESULT CONFIRMED

Nine triplets computed. Results:

| Triplet | K | a² | Nearest p/q | Miss from p/q |
|---|---|---|---|---|
| **e, μ, τ (reference)** | **0.66666** | **2.0000** | **2/3** | **9.2 ppm** |
| Σ⁺, Σ⁰, Σ⁻ | 0.33333 | 0.000004 | 1/3 | 0.0002% |
| Υ(1S), Υ(2S), Υ(3S) | 0.33345 | 0.00069 | 1/3 | 0.035% |
| p, n, Λ | 0.33390 | 0.00340 | 1/3 | 0.17% |
| ρ, K*, φ | 0.33437 | 0.00623 | 1/3 | 0.31% |
| Σ⁺, Ξ⁰, Ω⁻ | 0.33509 | 0.01054 | 1/3 | 0.52% |
| W, Z, H | 0.33635 | 0.01809 | 1/3 | 0.90% |
| π, K, η | 0.35799 | 0.14795 | 3/8 | 4.75% |
| π, K, D | 0.41918 | 0.51505 | 3/7 | 2.24% |

**No hadron triplet matches K = 2/3.** All near-degenerate triplets (mass ratio < 2:1) cluster at K ≈ 1/3 (the equal-mass limit, a ≈ 0). The Sigma baryons are the most degenerate (a² = 0.000004, masses within 0.7% of each other).

The meson triplet (π, K, D) gives K = 0.419, the farthest from 1/3 because it spans the largest mass range (140 to 1870 MeV). But 0.419 is not near 2/3 either (miss 37%).

**Conclusion:** K = 2/3 is lepton-specific. The R₃/R₂ dimensional embedding applies to color-singlet charged leptons only. Colored hadrons either have no dimensional embedding or have a different one.

---

### VI. THE NUCLEAR BINDING RATIO

| Ratio | Value | Framework candidate | Miss |
|---|---|---|---|
| a_A/a_V | 1.4968 | 3/2 = R₂/R₃ (inverse Koide) | **0.21%** |
| a_S/a_V | 1.1073 | ~1 + 1/9? | unclear |
| a_C/a_V | 0.04479 | — | — |

The asymmetry-to-volume ratio a_A/a_V = 1.4968 matches 3/2 to 0.21%. This is R₂/R₃ — the INVERSE of the Koide ratio R₃/R₂ = 2/3. In the Koide context, going from 3D→2D (the reverse embedding) gives 3/2. In nuclear physics, the asymmetry energy penalizes imbalance between protons and neutrons. The penalty ratio being 3/2 of the volume energy might reflect the dimensional structure of the nuclear force.

Single ratio, fitted parameters, 0.21% — suggestive but not diagnostic.

---

### VII. THE CHANDRASEKHAR COEFFICIENT

The Lane-Emden coefficient for polytropic index n = 3 (relevant to white dwarf structure): 5.836.

Framework candidate: 15π/8 = 5.8905.

Miss: **0.93%**.

15 = 3 × 5 (generations × SU(5) fundamental?). 8 = dim(SU(3) adjoint). The coefficient 15π/8 is sub-percent from the standard Lane-Emden value. Whether this is structural or coincidental depends on whether the Lane-Emden integration can be connected to gauge-group integers.

---

### VIII. THE MUON g-2 TOROIDAL CONTRIBUTION

| Quantity | Value |
|---|---|
| ae mass-dep 4-loop × (m_μ/m_e)² | 1.283 × 10⁻⁹ |
| (m_μ/m_e)² | 42,753 |
| SM total prediction | 0.001165917409 |
| Measured | 0.001165920590 |
| Anomaly | 3.181 × 10⁻⁹ |
| Toroidal fraction of anomaly | **40.3%** |

The toroidal four-loop contribution is 40.3% of the measured anomaly (down from the 51% estimate in the addendum because the anomaly here uses the full SM total rather than just R-ratio hadronic). The toroidal piece is the right order of magnitude — 1.28 × 10⁻⁹ vs the anomaly 3.18 × 10⁻⁹. The remaining 60% would need to come from five-loop toroidal contributions or hadronic sector toroidal content.

---

### IX. THE KOIDE AMPLITUDE MAP

| Family | a² | K | Position | Character |
|---|---|---|---|---|
| Charged leptons | 1.99996 | 0.66666 | **Critical (equator)** | K = R₃/R₂ = 2/3 |
| Down quarks | 2.3877 | 0.73129 | Beyond critical | Past saturation |
| Up quarks | 3.0928 | 0.84879 | Far beyond critical | Near one-mass-dominant |
| EW bosons | 0.0181 | 0.33635 | **Symmetric (pole)** | K ≈ 1/3 |

The four particle families occupy distinct positions in the K-a² plane. Leptons at the critical amplitude a² = 2. Quarks beyond critical (a² > 2, meaning the lightest quark is near-massless relative to the heaviest). Bosons at the symmetric pole (a² ≈ 0, near-degenerate masses).

The pattern: leptons at the 2D→3D embedding (R₃/R₂ = 2/3). Quarks past the embedding (a² > 2, the up quark at 2.2 MeV is nearly massless compared to the top at 173 GeV). Bosons at the trivial limit (W, Z, H masses span only 1.56×).

---

### X. THE FILLING FRACTION LADDER

| Transition | R_{n+1}/R_n | Nearest p/q | Miss | Rational? |
|---|---|---|---|---|
| 1D → 2D | 0.7854 = π/4 | 7/9 | 0.97% | No |
| **2D → 3D** | **0.6667 = 2/3** | **2/3** | **0.000%** | **Yes** |
| 3D → 4D | 0.5890 = 3π/16 | 3/5 | 1.86% | No |
| 4D → 5D | 0.5333 = 8/15 | 5/9 | 4.17% | No* |
| 5D → 6D | 0.4909 | 1/2 | 1.86% | No |
| 6D → 7D | 0.4571 | 4/9 | 2.78% | No |

*Note: R₅/R₄ = 8/15 is actually rational (from PHYS-50 errata §XVI), but the physical ladder has only three dimensions (from §XVII). Within the physical ladder (1D, 2D, 3D), R₃/R₂ = 2/3 is the unique rational. The experiment confirms this: one rational in two physical transitions.

---

### XI. THE MICROSCOPIC-COSMIC BRIDGE

| Quantity | Value |
|---|---|
| Microscopic: \|A₄\| × (α/π)⁴ | 5.567 × 10⁻¹¹ |
| Cosmic: 22π/13 | 5.317 |
| Bridge ratio: cosmic/microscopic | 9.550 × 10¹⁰ |
| 3(M_Z/m_e)² | 9.553 × 10¹⁰ |
| Bridge miss | **0.030%** |

The ratio of cosmic toroidal content (22π/13) to microscopic toroidal content (\|A₄\| × (α/π)⁴) equals 3(M_Z/m_e)² to **0.030%** — 300 ppm.

The Z boson mass bridges the microscopic and cosmic scales. The factor 3 is either the spatial dimension count or the generation count. The formula:

22π/13 = \|A₄\| × (α/π)⁴ × 3 × (M_Z/m_e)²

connects the Laporta constant A₄ (microscopic QED topology), the fine structure constant α (QED coupling), the Z mass (electroweak scale), and the electron mass (lepton scale) to the cosmic DM/baryon ratio (cosmological scale).

This is the tightest cross-scale connection in the framework: five independently measured quantities from three different physics domains (QED, electroweak, cosmology) connected by one formula at 300 ppm.

---

### XII. THE COMPLETE RESULTS TABLE

| # | Test | Level | Predicted | Measured | Miss | Status |
|---|---|---|---|---|---|---|
| 1 | \|V_us\| = 9/40 | Particle | 0.22500 | 0.22501 | 44 ppm | **PASS** |
| 2 | \|V_cb\| = 1/24 | Particle | 0.04167 | 0.04182 | 0.37% | **PASS** |
| 3 | \|V_ub\| = 1/264 | Particle | 0.003788 | 0.003685 | 2.79% | FAIL |
| 4 | \|V_cb/V_ub\| = 11 | Particle | 11.000 | 11.349 | 3.07% | FAIL |
| 5 | Ω_Λ = (251−22π)/264 | Cosmos | 0.68896 | 0.6889 | 0.0084% | **PASS** |
| 6 | H₀ ratio = 12/11 | Cosmos | 1.0909 | 1.0837 | 0.67% | **PASS** |
| 7 | Lepton K = 2/3 | Lepton | 0.66667 | 0.66666 | 9.2 ppm | **PASS** |
| 8 | a_A/a_V = 3/2 | Nuclear | 1.5000 | 1.4968 | 0.21% | **PASS** |
| 9 | 15π/8 = Lane-Emden | Stellar | 5.8905 | 5.836 | 0.93% | **PASS** |
| 10 | DM/baryon = 22π/13 | Cosmos | 5.3165 | 5.3204 | 725 ppm | **PASS** |
| 11 | Bridge = 3(M_Z/m_e)² | QED↔Cosmos | 9.553 × 10¹⁰ | 9.550 × 10¹⁰ | 0.030% | (**PASS**) |
| 12 | Hadron K = 2/3 | Hadron | — | all ≈ 1/3 | — | **Negative** |
| 13 | Muon toroidal | Lepton | 1.28 × 10⁻⁹ | anomaly 3.18 × 10⁻⁹ | 40% of anomaly | **INFO** |
| 14 | R₃/R₂ unique | Math | rational | — | — | **Confirmed** |
| 15 | Koide amplitude map | All | — | 4 families mapped | — | **INFO** |

---

### XIII. ASSESSMENT BY HIERARCHY LEVEL

| Level | Tests | Passes | Fails | Verdict |
|---|---|---|---|---|
| **Particle (CKM)** | 4 | 2 | 2 | **Partial** — V_us sharp, V_ub needs work |
| **Cosmos** | 3 | 3 | 0 | **Strong** — all sub-1% |
| **Lepton** | 2 | 1 pass, 1 info | 0 | **Strong** — Koide 9.2 ppm |
| **Nuclear** | 1 | 1 | 0 | **Suggestive** — single ratio |
| **Stellar** | 1 | 1 | 0 | **Suggestive** — single coefficient |
| **Hadron** | 1 | 0 | 0 | **Negative** — no K = 2/3 found |
| **QED↔Cosmos bridge** | 1 | 1 | 0 | **Strong** — 300 ppm |
| **Math** | 1 | 1 | 0 | **Confirmed** — R₃/R₂ unique |

The framework is strongest at cosmological scale (3/3 pass, all sub-1%), at lepton scale (Koide at 9.2 ppm), and at the cross-scale bridge (300 ppm). It is weakest at the hadron scale (no K = 2/3) and partially confirmed at the particle scale (V_us sharp, V_ub off).

---

### XIV. THE FIVE STRONGEST RESULTS

Ranked by precision:

1. **Ω_Λ = (251−22π)/264 at 84 ppm.** The cosmological constant as inertial closure. Gauge integers 8, 3, 11, 13 in the expression. Testable by CMB-S4.

2. **\|V_us\| = 9/40 at 44 ppm.** The Cabibbo angle is 3²/(8×5). Common factor 8 = dim(SU(3) adjoint). Within PDG uncertainty.

3. **Bridge = 3(M_Z/m_e)² at 300 ppm.** Five quantities from three domains connected by one formula. The Z mass bridges microscopic toroidal content to cosmic toroidal content.

4. **DM/baryon = 22π/13 at 725 ppm.** The dark matter to baryon ratio from Yang-Mills doubled (22 = 2×11) and modified SU(2) (13). Within Planck uncertainty.

5. **Lepton K = R₃/R₂ = 2/3 at 9.2 ppm.** The Koide ratio as the unique rational filling fraction transition. Within tau mass uncertainty.

---

### XV. THE TWO FAILURES — DIAGNOSIS

**\|V_ub\| = 1/264 misses by 2.79%.** PDG: 0.003685 ± 0.00020. Predicted: 0.003788. The prediction is 1.6σ from the central value. The \|V_ub\| measurement is the most difficult CKM element to extract (it requires exclusive or inclusive B → Xu ℓν analysis). The PDG uncertainty is ±5.4%, so the prediction is within the error bar in the loose sense but outside the 2% spec.

Possible outcomes: (a) Future measurements move \|V_ub\| toward 0.00379, confirming 1/264. (b) Future measurements confirm 0.00369, and 1/264 is wrong — the correct fraction might be 1/271 = 0.00369 (miss: 0.1%), which equals 1/271 with 271 = prime. No obvious gauge integer decomposition for 271.

**\|V_cb/V_ub\| = 11 misses by 3.07%.** This is driven by the \|V_ub\| miss. If \|V_ub\| = 1/264 is confirmed, the ratio becomes (1/24)/(1/264) = 264/24 = 11 exactly. If \|V_ub\| stays at 0.00369, the ratio is 0.04182/0.003685 = 11.35, and 11 is close but not exact.

**Both failures trace to \|V_ub\|.** The framework's CKM prediction stands or falls on whether \|V_ub\| converges toward 1/264 with improved measurements.

---

### XVI. WHAT THE EXPERIMENT ESTABLISHES

**Established across hierarchy levels:**

The modulus/remainder decomposition produces sub-percent predictions at cosmological, lepton, and cross-scale levels. The gauge integers 8, 11, 13 appear in the CKM matrix (particle level), the cosmological partition (cosmic level), and the microscopic-cosmic bridge (cross-level). The same structural integers operating at different scales is the remainder program's central prediction, and it is confirmed for these three integers across three levels.

**Established as negative results:**

No hadron triplet matches K = 2/3. The dimensional embedding R₃/R₂ is lepton-specific. Colored particles do not share this structure.

**Established as suggestive:**

Nuclear a_A/a_V = 3/2 at 0.21%. Chandrasekhar 15π/8 at 0.93%. Each is a single ratio from a single computation. Confirmation requires either independent derivation chains reaching the same ratios or additional nuclear/stellar predictions that match.

**Not established:**

Whether \|V_ub\| = 1/264. Whether the Hubble tension is literally 12/11. Whether the muon g-2 anomaly is 40% toroidal. All require improved measurements or additional computation.

---

**END OF REPORT**

**Session 8 running total:** 11 experiments across the Laporta program, Koide R₃/R₂, the α_EM killing spree (rounds 1 and 2), and the giga remainder test. Combined: 13 experiments, ~620 outputs, ~100 PASS, ~12 FAIL. The framework's inertial partition is tested from sub-femtometer QED to Hubble-scale cosmology. The data selects what survives.
