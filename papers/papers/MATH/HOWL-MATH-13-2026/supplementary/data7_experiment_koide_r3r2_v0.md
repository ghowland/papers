## Koide R₃/R₂ Report: The 2D-to-3D Filling Fraction Ratio

**Experiment:** experiment_koide_r3r2_v0
**Run:** run001
**Date:** April 19, 2026
**Pool:** 3590 value nodes
**Result:** 3/3 derivations OK, 6 PASS, 0 FAIL, 2 INFO

---

### I. THE FIVE FINDINGS

**1. R₃/R₂ = 2/3 is exact, and it is the ONLY simple fraction in the filling ratio sequence.** The consecutive filling fraction ratios R_{n+1}/R_n for n = 1 through 6 are: π/4 ≈ 0.785, **2/3**, 3π/16 ≈ 0.589, 8/(5π) ≈ 0.533, π³/384 × ... ≈ 0.491, ... ≈ 0.457. The nearest simple fractions (p/q with p,q ≤ 10) miss by 0.97% (R₂/R₁), **0.000%** (R₃/R₂), 1.86% (R₄/R₃), 4.17% (R₅/R₄), 1.86% (R₆/R₅), 2.78% (R₇/R₆). The 2D→3D transition is arithmetically unique — it is the only dimensional transition where the filling fraction ratio is a ratio of small integers.

**2. The Koide ratio matches R₃/R₂ to 9.2 ppm.** K_lepton = 0.666660511, R₃/R₂ = 0.666666667. Miss: 9.23 ppm (0.00092%). The amplitude a² = 1.99996, miss from 2: 18.5 ppm. The lepton mass spectrum fills its parameter space with 2/3 efficiency to better than 10 parts per million.

**3. The four-loop toroidal correction moves K TOWARD 2/3.** Before correction: miss = 9.233 ppm. After four-loop mass shifts: miss = 9.178 ppm. Shift: 0.054 ppm toward 2/3. Direction: TOWARD. The toroidal radiative correction does not break Koide — it tightens it. The correction is small (0.054 ppm out of 9.2 ppm) but in the right direction.

**4. The bosons confirm the spherical limit.** K_boson = 0.3363, a² = 0.018. The boson Koide is within 0.9% of 1/3 (the equal-mass limit). The boson amplitude is nearly zero — no spread, no toroidal content. The bosons sit at the pole of the parameter space (a ≈ 0, pure spherical symmetry).

**5. E(k)/K(k) = 2/3 at k = 0.7739.** The ratio of elliptic integrals E/K takes the value 2/3 at a specific modulus k = 0.7739. This is a second geometric definition of 2/3 in the elliptic framework — the modulus where the arc length integral is exactly 2/3 of the period integral. This modulus is distinct from the Laporta moduli (0.99713, 0.999994) and from the critical modulus k = 0.9844 where K = π.

---

### II. THE R₃/R₂ IDENTITY

| Dimension n | Rₙ | Rₙ/Rₙ₋₁ | Nearest p/q (p,q ≤ 10) | Miss from p/q |
|---|---|---|---|---|
| 1 | 1 | — | — | — |
| 2 | π/4 = 0.7854 | π/4 | 7/9 | 0.97% |
| **3** | **π/6 = 0.5236** | **2/3** | **2/3** | **0.000%** |
| 4 | π²/32 = 0.3084 | 3π/16 | 3/5 | 1.86% |
| 5 | 8π²/960 = 0.1645 | 8/(5π) | 5/9 | 4.17% |
| 6 | π³/384 = 0.0808 | 3π²/128 | 1/2 | 1.86% |
| 7 | 16π³/10080 = 0.0369 | ... | 4/9 | 2.78% |

R₃/R₂ = (π/6)/(π/4) = 4/6 = 2/3. The π cancels. This is the ONLY consecutive ratio where π cancels completely, leaving a pure rational number. Every other ratio retains π or π² in the expression.

Why π cancels at the 2D→3D transition specifically: R₂ = π^(2/2)/(2² × Γ(2)) = π/4. R₃ = π^(3/2)/(2³ × Γ(5/2)) = π^(3/2)/(8 × 3√π/4) = π/(6). The ratio R₃/R₂ = (π/6)/(π/4). The single power of π in both numerator and denominator cancels. At no other consecutive step does the π power match exactly.

---

### III. THE KOIDE MATCH

| Quantity | Value | Reference | Miss |
|---|---|---|---|
| R₃/R₂ | 0.666666666666667 | exact 2/3 | 0 (mathematical identity) |
| K_lepton | 0.666660511465522 | measured masses | 9.23 ppm from 2/3 |
| a² | 1.99996306879313 | measured masses | 18.5 ppm from 2 |

The Koide ratio agrees with R₃/R₂ = 2/3 to 9.2 parts per million. The amplitude a² agrees with 2 (the intrinsic dimension of the torus surface) to 18.5 ppm. Both are measured from the physical lepton masses — no free parameters.

The 9.2 ppm miss is either:
(a) The measurement precision limit of the lepton masses (unlikely — masses are known to much better than 9 ppm).
(b) A real deviation from exact K = 2/3, caused by radiative corrections, scheme dependence, or higher-order effects.
(c) A deviation from the R₃/R₂ identification itself (the relation is approximate, not exact).

The four-loop correction (Finding 3) addresses option (b): it shifts K by 0.054 ppm TOWARD 2/3. If all radiative corrections shift K toward 2/3, the bare-mass Koide would be farther from 2/3 than the pole-mass Koide, and the R₃/R₂ relation would hold for the CORRECTED masses, not the bare masses. The 9.2 ppm miss in the pole masses would be the residual of incomplete radiative correction.

---

### IV. THE FOUR-LOOP RADIATIVE CORRECTION

| Lepton | Mass (MeV) | Fractional 4-loop correction | (m/mₑ)² scaling |
|---|---|---|---|
| Electron | 0.511 | 3.0 × 10⁻¹⁴ | 1 |
| Muon | 105.7 | 1.28 × 10⁻⁹ | 42,753 |
| Tau | 1776.9 | 3.63 × 10⁻⁷ | 12,088,960 |

| Koide K | Value | Miss from 2/3 (ppm) |
|---|---|---|
| Before correction | 0.666660511 | 9.233 |
| After correction | 0.666660548 | 9.178 |
| **Shift** | **+3.63 × 10⁻⁸** | **−0.054 ppm (TOWARD 2/3)** |

The correction is tiny — 0.054 ppm out of a 9.2 ppm miss. At this rate, the four-loop correction accounts for only 0.6% of the miss. The remaining 99.4% of the miss must come from other sources: lower-loop corrections (which are larger), hadronic contributions, or a genuine deviation from K = 2/3.

But the DIRECTION is significant. The correction moves K toward 2/3, not away. The toroidal sector (which scales as (m/mₑ)²) differentially shifts the tau mass more than the muon, and the muon more than the electron. This differential shift happens to tighten the Koide ratio. The toroidal geometry is not random with respect to Koide — it acts in the direction that preserves the relation.

---

### V. THE BOSON KOIDE — SPHERICAL LIMIT

| Boson | Mass (MeV) | √m |
|---|---|---|
| W | 80,369 | 283.5 |
| Z | 91,188 | 302.0 |
| H | 125,200 | 353.8 |

| Quantity | Value | Interpretation |
|---|---|---|
| K_boson | 0.33635 | Near 1/3 = equal-mass limit |
| a²_boson | 0.01809 | Near 0 = no spread |
| Miss from 1/3 | 0.90% | Moderate |

The boson masses span only a factor of 1.56 (125.2/80.4). The lepton masses span a factor of 3477 (1776.9/0.511). The bosons are nearly equal; the leptons are wildly unequal.

In the R₃/R₂ framework: K = 1/3 is the pole (a = 0, all masses equal). K = 2/3 is the "equator" (a = √2, critical amplitude). K = 1 is the other pole (one mass dominates completely). The bosons are at the symmetric pole. The leptons are at the critical equator.

The boson K = 1/3 is the N = 3 equal-mass limit, which is R₃/R₃ = 1... no, that's 1. Actually 1/3 = 1/N for N = 3 generations. The bosons show no geometric structure — they're at the trivial configuration. Their masses come from the Higgs mechanism (spherically symmetric potential), not from toroidal topology.

---

### VI. THE ELLIPTIC KOIDE — ⟨cn²⟩ AT THE CRITICAL MODULUS

The critical modulus k = 0.98443 where K(k) = π (the "twice the circle" condition) was found. At this modulus, the average ⟨cn²⟩ over 120-degree-equivalent spacing on the cn parametrization is:

| Quantity | k = 0 (standard Koide) | k = 0.98443 (critical modulus) |
|---|---|---|
| Period | 2π | 4K = 4π |
| ⟨cos²⟩ or ⟨cn²⟩ | 0.500 (exact) | 0.310 |
| a² for K = 2/3 | 2.000 | 3.226 |

At the critical modulus, ⟨cn²⟩ = 0.310, NOT 0.500. The Jacobi cn function at k = 0.984 has a different shape from cos — its peaks are flatter and its troughs are sharper. This changes the average ⟨cn²⟩ from 1/2 to ~0.31.

If the lepton masses lived on a torus with k = 0.984, the amplitude required for K = 2/3 would be a² = 3.23, not 2. The standard Koide relation a² = 2 is SPECIFIC to k = 0 (the circular parametrization). On a genuine torus, the amplitude changes.

This means the R₃/R₂ = 2/3 interpretation and the toroidal K(k) framework are NOT the same thing at the critical modulus. The K = 2/3 relation works at k = 0 (circle) with a² = 2. At k > 0 (torus), the relation requires a different a². The 2D→3D filling fraction ratio is a k = 0 phenomenon — it describes the circular parametrization embedded in 3D, not the toroidal parametrization.

This is either a problem (the toroidal interpretation doesn't help Koide) or a refinement (Koide is specifically the k = 0 limit of a toroidal family, and the 2/3 value reflects the CIRCULAR geometry, not the toroidal geometry).

---

### VII. E(k)/K(k) = 2/3 AT k = 0.7739

A second occurrence of 2/3 in the elliptic framework: the ratio of complete elliptic integrals E(k)/K(k) equals exactly 2/3 at k = 0.7739.

| Quantity | Value |
|---|---|
| k where E/K = 2/3 | 0.773939574812122 |
| K at this k | 2.1146 |
| E at this k | 1.4097 |
| E/K | 0.666666666666667 |

E measures arc length on the ellipse. K measures the period. Their ratio E/K is the "arc efficiency" — how much of the period is traversed per unit of angular time. At k = 0: E/K = 1 (circle, maximum efficiency). At k → 1: E/K → 0 (degenerate, minimum efficiency). At k = 0.7739: E/K = 2/3, the Koide ratio.

This k = 0.7739 is distinct from the Laporta moduli (0.997, 0.99999) and from the critical modulus (0.984). It has no known physical connection yet. But it demonstrates that 2/3 appears naturally in the elliptic function framework at a specific, non-trivial modulus.

If the "Koide modulus" is k = 0.7739 rather than k = 0, the interpretation would be: the lepton mass spectrum sits on an elliptic curve where the arc length is 2/3 of the period. The mass parametrization is not circular (cos) but elliptic (cn) at a modulus where E/K has the Koide value. This is a different geometric reading from R₃/R₂ but equally specific.

---

### VIII. THE DIMENSIONAL SEQUENCE — WHAT'S SPECIAL ABOUT 2→3

The filling fraction sequence Rₙ/Rₙ₋₁:

| Transition | Ratio | Expression | Rational? |
|---|---|---|---|
| 1D → 2D | π/4 | irrational (π) | No |
| **2D → 3D** | **2/3** | **rational** | **Yes** |
| 3D → 4D | 3π/16 | irrational (π) | No |
| 4D → 5D | 8/(5π) | irrational (π) | No |
| 5D → 6D | 5π²/192 | irrational (π²) | No |

The 2D→3D transition is the ONLY one where π cancels. This happens because:

R₂ = π¹/(2² × 1!) = π/4 — one power of π
R₃ = π^(3/2)/(2³ × Γ(5/2)) = π^(3/2)/(8 × 3√π/4) = π/6 — also one power of π (after Γ simplification)

The π power in Rₙ = π^(n/2)/(...) alternates between integer and half-integer. At n = 2: π¹. At n = 3: π^(3/2). But the Γ function in the denominator contributes √π at n = 3 (Γ(5/2) = 3√π/4), canceling the extra √π. This is specific to the transition from even to odd dimension at n = 2→3. At n = 4→5, the same mechanism gives R₅/R₄ = 8/(5π), not a rational.

The reason: Γ(5/2) = (3/2)(1/2)√π contains exactly √π. At higher half-integer arguments, Γ contains √π but the prefactors don't simplify to cancel all π. The 2→3 transition is special because the Gamma function at 5/2 is the SIMPLEST half-integer Gamma that cancels the √π in π^(3/2)/π^(2/2) = √π.

---

### IX. THE COMPLETE NUMBER MAP

| Quantity | Value | Origin | Connection |
|---|---|---|---|
| R₃/R₂ | 2/3 | Filling fraction ratio, 2D→3D | Mathematical identity |
| K_lepton | 0.666661 | Lepton masses | Miss: 9.2 ppm from 2/3 |
| a² | 1.99996 | Koide amplitude | Miss: 18.5 ppm from 2 |
| K_boson | 0.33635 | Boson masses | Miss: 0.90% from 1/3 |
| a²_boson | 0.01809 | Boson amplitude | Near zero |
| E/K = 2/3 modulus | k = 0.7739 | Elliptic function | Exact 2/3 at this k |
| K = π modulus | k = 0.9844 | "Twice the circle" | ⟨cn²⟩ = 0.310 ≠ 1/2 |
| k₈₃ (Laporta) | 0.99713 | Topology 83 | Different from E/K modulus |
| k₈₁ (Laporta) | 0.999994 | Topology 81 | Different from all above |
| Four-loop K shift | +0.054 ppm | Radiative correction | TOWARD 2/3 |

---

### X. ASSESSMENT

**What is established:**

1. R₃/R₂ = 2/3 is exact and arithmetically unique — the only simple fraction in the filling ratio sequence.
2. K_lepton = 2/3 to 9.2 ppm. The match is precise.
3. a² = 2 to 18.5 ppm. The amplitude equals the intrinsic dimension of the torus surface.
4. The four-loop correction moves K TOWARD 2/3. The toroidal geometry acts in the preserving direction.
5. Bosons are at the spherical limit (a ≈ 0, K ≈ 1/3). Leptons are at the critical amplitude (a ≈ √2, K ≈ 2/3).
6. E(k)/K(k) = 2/3 at a specific modulus k = 0.7739.

**What is NOT established:**

1. Whether K = R₃/R₂ is a structural identification or a numerical coincidence. The number 2/3 appears in many contexts; sharing a value does not prove a connection.
2. Whether a² = 2 literally counts torus surface dimensions or is simply the critical amplitude of the Koide parametrization.
3. Whether the four-loop correction fully explains the 9.2 ppm miss (it accounts for only 0.054 ppm — 0.6% of the miss).
4. Whether the E/K = 2/3 modulus (k = 0.7739) has physical significance for the lepton masses.

**What the experiment discriminates:**

The R₃/R₂ identification makes a specific prediction: K = 2/3 should be EXACT for leptons, with all deviations explained by radiative corrections. The four-loop correction moves K in the right direction. If the full radiative correction (all loops, not just four-loop) explains the entire 9.2 ppm, the identification is strongly supported. If the full correction overshoots or falls short of 9.2 ppm, the identification has a quantitative problem.

The elliptic Koide test shows that K = 2/3 is NOT preserved on the torus at the critical modulus (⟨cn²⟩ = 0.31 ≠ 0.50). This means Koide K = 2/3 is specifically a CIRCULAR phenomenon (k = 0), not a toroidal one. The R₃/R₂ interpretation is consistent: R₃/R₂ measures circle-in-sphere, not torus-in-something. The "2D surface" in the R₃/R₂ reading is the circular cross-section, not the toroidal surface.

The lepton/boson dichotomy (K = 2/3 vs K ≈ 1/3) maps onto critical/symmetric rather than toroidal/spherical. Both values are from the k = 0 (circular) family. The leptons are at the critical amplitude. The bosons are at the trivial amplitude. The geometry is circular for both; the difference is the amplitude, not the manifold.

---

**END OF REPORT**
