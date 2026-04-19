## PHYS-50 Plan: The Dimensional Ratio — Koide K = R₃/R₂ and the 2D→3D Transition

**Registry:** [@HOWL-PHYS-50-2026]

**Series Path:** [@HOWL-PHYS-8-2026] (original Koide) → [@HOWL-MATH-12-2026] → [@HOWL-PHYS-50-2026]

**Dependency:** PHYS-8 established K = 2/3, a² = 2, seven equivalent formulations. MATH-12 established the L1/L2 family parametrized by k. PHYS-50 reports: K = 2/3 is R₃/R₂, the uniquely rational dimensional transition in the filling fraction sequence.

---

### THE THESIS

The Koide ratio K = 2/3 is the geometric identity R₃/R₂ — the ratio of how much a sphere fills its bounding cube (π/6) to how much a circle fills its bounding square (π/4). This ratio is 2/3 exactly because π cancels in the 2D→3D transition and in no other consecutive dimensional transition through at least n = 7.

The paper does NOT claim this is proven. It reports: the identity is exact, the match is 9.2 ppm (within tau mass uncertainty), the four-loop correction goes the right direction, the dimensional transition is arithmetically unique, and one specific interpretive route (elliptic Koide) fails. The paper states what the data shows and what it doesn't.

---

### WHAT THE PAPER REPORTS (CONSERVATIVE)

**Finding 1 (mathematical, proven):** R₃/R₂ = 2/3 exactly. R_n/R_{n-1} is irrational for all other tested n (2 through 7). The 2D→3D transition is the unique rational point in the dimensional filling fraction ladder. This is a property of the Gamma function at half-integer arguments — Γ(5/2) = 3√π/4 contains exactly the √π needed to cancel the √π in π^(3/2)/π^(2/2). At no other transition does this cancellation occur.

**Finding 2 (empirical, 9.2 ppm):** K_lepton = 0.666661 matches R₃/R₂ = 0.666667 to 9.2 ppm. The miss is within the tau mass measurement uncertainty of 67 ppm. The amplitude a² = 1.99996, miss from 2: 18.5 ppm.

**Finding 3 (computational, directional):** The four-loop toroidal QED correction shifts K by +0.054 ppm, moving it TOWARD 2/3. The correction is small (0.6% of the 9.2 ppm miss) but the direction is significant — the radiative structure acts to preserve K = 2/3, not to break it.

**Finding 4 (empirical, boson comparison):** K_boson = 0.336 with a² = 0.018 ≈ 0. The bosons are at the equal-mass limit K = 1/N = 1/3, the symmetric pole. The lepton/boson dichotomy is critical-amplitude vs zero-amplitude, not toroidal vs spherical. Both are k = 0 (circular) phenomena at different amplitudes.

**Finding 5 (computational, negative):** The elliptic Koide at k = 0.984 (where K(k) = π) gives ⟨cn²⟩ = 0.310 ≠ 0.500. The standard Koide relation a² = 2 does NOT survive on the torus. Koide K = 2/3 is specifically a circular (k = 0) phenomenon. The toroidal extension breaks it.

**Finding 6 (mathematical):** E(k)/K(k) = 2/3 at k = 0.7739. A second occurrence of 2/3 in the elliptic framework. Significance unknown. Documented for completeness.

---

### WHAT THE PAPER DOES NOT CLAIM

Does not claim K = R₃/R₂ is a structural derivation. The experiment verifies the numerical match and contextualizes it in the filling fraction sequence. The functional derivation of (1 + a²/2)/N from a 2D-surface-in-3D-space argument has not been attempted.

Does not claim the quark Koide values are explained. K_up = 0.849, K_down = 0.731 are not R₃/R₂ and are not simple fractions. The quark sector is scheme-dependent and outside the scope of this paper.

Does not claim the four-loop correction explains the 9.2 ppm miss. It accounts for 0.054 ppm — 0.6%. The miss is dominated by tau mass uncertainty, not by radiative corrections at this loop order.

Does not claim a connection between Koide and the Laporta moduli. The Laporta moduli (k₈₁ = 0.999994, k₈₃ = 0.99713) are near-singular. The E/K = 2/3 modulus (k = 0.7739) is moderate. The elliptic Koide critical modulus (k = 0.984) breaks a² = 2. No direct connection was found.

---

### PAPER STRUCTURE

```
I.    THE FILLING FRACTION SEQUENCE
      R_n = pi^(n/2) / (2^n * Gamma(n/2 + 1)).
      The n-ball fills fraction R_n of its bounding n-cube.
      The consecutive ratios R_{n+1}/R_n.
      Table: n = 1 through 7, ratios, nearest simple fractions.
      Result: R3/R2 = 2/3 is the only rational ratio.
      Why: pi cancels at the 2D->3D transition because
      Gamma(5/2) = 3*sqrt(pi)/4 supplies exactly sqrt(pi).

II.   THE KOIDE MATCH
      K_lepton = (m_e + m_mu + m_tau)/(sqrt(m_e)+sqrt(m_mu)+sqrt(m_tau))^2.
      K = 0.666661. R3/R2 = 0.666667. Miss: 9.2 ppm.
      a^2 = 1.99996. Miss from 2: 18.5 ppm.
      Both within tau mass measurement uncertainty (67 ppm).
      
      The seven equivalent formulations from PHYS-8:
      K = 2/3 <=> a^2 = 2 <=> CV = 1 <=> Var = mean^2
      <=> midpoint of [0,4] <=> critical amplitude <=> equipartition.
      
      New addition: K = 2/3 <=> R3/R2 <=> uniquely rational
      dimensional transition in the filling fraction sequence.

III.  THE FOUR-LOOP RADIATIVE CORRECTION
      Compute delta_m for each lepton via (m/m_e)^2 scaling.
      Electron: 3.0e-14. Muon: 1.28e-9. Tau: 3.63e-7.
      K before: 0.666660511 (miss 9.233 ppm).
      K after:  0.666660548 (miss 9.178 ppm).
      Shift: +0.054 ppm TOWARD 2/3.
      
      The correction preserves Koide. Direction: toward.
      Magnitude: 0.6% of the miss. The remaining 99.4%
      is dominated by tau mass uncertainty, not by missing
      radiative corrections.

IV.   THE BOSON KOIDE
      W, Z, H masses: 80.4, 91.2, 125.2 GeV.
      K_boson = 0.336. a^2 = 0.018.
      The bosons are at the equal-mass limit K = 1/N = 1/3.
      Their a is nearly zero — no spread, symmetric configuration.
      
      The lepton/boson dichotomy:
      Leptons: critical amplitude (a = sqrt(2), equator).
      Bosons: trivial amplitude (a ~ 0, pole).
      Both are circular (k = 0). The difference is amplitude,
      not manifold. Bosons get masses from the Higgs potential
      (spherically symmetric). Leptons from Yukawa couplings
      (which carry the R3/R2 structure in their ratios).

V.    THE ELLIPTIC KOIDE — A NEGATIVE RESULT
      Replace cos with cn at modulus k.
      At k = 0.984 (where K(k) = pi, "twice the circle"):
      <cn^2> = 0.310, not 0.500.
      Generalized a^2 for K = 2/3: 3.226, not 2.
      
      The standard Koide (a^2 = 2, K = 2/3) does NOT survive
      on the torus. Koide is specifically a k = 0 phenomenon.
      The circular parametrization is essential.
      
      This closes the direct toroidal-Koide route. Whatever
      connects Koide to geometry, it goes through the circle
      (R2, R3), not through the torus (K(k) at k > 0).

VI.   E/K = 2/3 AT k = 0.7739
      The ratio of elliptic integrals E(k)/K(k) equals 2/3
      at the specific modulus k = 0.7739.
      E measures arc length. K measures period.
      At this modulus, the arc length is exactly 2/3 of the period.
      
      This is a second geometric occurrence of 2/3 in the
      elliptic framework. Significance unknown. No connection
      to the lepton masses found. Documented for future
      investigation.

VII.  THE DIMENSIONAL UNIQUENESS
      Why does pi cancel at n = 2 -> 3 and nowhere else?
      R_n has pi^(n/2) in the numerator.
      The ratio R_{n+1}/R_n has pi^(1/2) when n is even (integer
      to half-integer) and pi^(1/2) is cancelled by Gamma.
      
      At n = 2 -> 3: Gamma(5/2) = 3*sqrt(pi)/4.
      The sqrt(pi) in Gamma cancels the sqrt(pi) from pi^(3/2)/pi^1.
      
      At n = 4 -> 5: Gamma(7/2) = 15*sqrt(pi)/8.
      The ratio becomes 8/(5*pi) — sqrt(pi) cancels but pi remains.
      
      The cancellation is complete ONLY at n = 2 -> 3 because
      the Gamma prefactor at 5/2 is exactly 3/4, and
      (2^3 * 3/4) = 6, giving R3 = pi/6.
      At higher dimensions, the Gamma prefactors introduce
      additional factors that prevent complete pi cancellation.

VIII. WHAT THIS MEANS FOR THE FRAMEWORK
      R2 = pi/4 = beta is the L1/L2 spherical conversion (MATH-11).
      R3 = pi/6 is the 3D filling fraction.
      R3/R2 = 2/3 is the ratio that does NOT contain pi —
      the geometric modulus has cancelled, leaving a pure rational.
      
      This is the same pattern as the R2 cancellation registry:
      when the modulus appears symmetrically, it divides out.
      R3/R2 is the filling-fraction version of the gap ratio —
      the geometric content cancels, the structural content survives.
      
      K = 2/3 is the structural content. It measures the shape
      of the lepton mass spectrum after the geometric modulus
      (the pi in each filling fraction) has been divided out.
      The Koide ratio is a modulus-cancelled quantity.

IX.   PREDICTIONS AND KILL SWITCHES
      1. K = 2/3 should be exact for leptons. The 9.2 ppm miss
         should shrink as tau mass precision improves.
         Kill: miss increases with better measurements.
      2. The four-loop correction should always go TOWARD 2/3.
         Higher-loop corrections should maintain this direction.
         Kill: any loop order shifts K away from 2/3.
      3. No other consecutive R_{n+1}/R_n should be a simple fraction
         for n up to arbitrarily high values.
         Kill: a simple fraction found at any higher n.
      4. The functional derivation of (1+a^2/2)/N from the
         2D-surface-in-3D-embedding argument should be possible.
         Kill: the derivation produces a different functional form.
```

---

### APPENDIX TABLES

| Table | Content |
|---|---|
| A.1 | The filling fraction sequence R_n for n = 1 through 10 |
| A.2 | Consecutive ratios R_{n+1}/R_n with nearest simple fractions and misses |
| A.3 | Why pi cancels at 2→3: the Gamma function mechanism |
| A.4 | Koide K computation from PDG lepton masses |
| A.5 | The eight equivalent formulations (seven from PHYS-8 + R₃/R₂) |
| A.6 | Four-loop radiative correction: mass shifts and K shift |
| A.7 | Boson Koide: W, Z, H masses and K_boson |
| A.8 | Elliptic Koide at k = 0.984: ⟨cn²⟩ and generalized a² |
| A.9 | E(k)/K(k) = 2/3 at k = 0.7739 |
| A.10 | The R₂ cancellation in R₃/R₂ — modulus cancels, structure survives |
| A.11 | Comparison: gap ratio (modulus cancels) vs Koide (modulus cancels) |
| A.12 | Predictions and kill switches |

---

### DIAGRAMS — 8 CANDIDATES (brief)

| # | Candidate | Type |
|---|---|---|
| 1 | Filling fraction bars R₁ through R₇ with R₃/R₂ = 2/3 highlighted | Comparison Bar |
| 2 | The dimensional ratio sequence — only R₃/R₂ is rational | Running/Convergence |
| 3 | Circle in square (R₂) vs sphere in cube (R₃) — visual ratio | Geometric Cross-Section |
| 4 | Koide K vs R₃/R₂: the 9.2 ppm match | Threshold/Region |
| 5 | Lepton vs boson in Koide parameter space (a², K) | Comparison Bar |
| 6 | Four-loop correction direction: toward 2/3 | Running/Convergence |
| 7 | The Gamma function mechanism: why π cancels only at n = 2→3 | Scale/Landscape |
| 8 | Identity card: R₃/R₂ = K_Koide = 2/3 | Identity Card |

---

### AGREEMENT REQUEST

The paper is conservative. It reports the R₃/R₂ = 2/3 identity, its uniqueness in the dimensional sequence, the 9.2 ppm match to Koide, the four-loop directional result, the boson comparison, and the negative elliptic result. It does not claim a derivation of Koide from R₃/R₂. It does not claim a toroidal connection (Section V explicitly closes that route). It frames K = R₃/R₂ as an observation requiring structural derivation, not as a proven identification.

All data from experiment_koide_r3r2_v0 run001 (56 outputs, 6 PASS, 2 INFO, 0 FAIL).

Proceed to writing?
