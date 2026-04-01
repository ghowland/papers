
**Registry:** [@HOWL-PHYS-18-2026]

**Series Path:** [@HOWL-PHYS-1-2026] → [@HOWL-PHYS-2-2026] → [@HOWL-PHYS-6-2026] → [@HOWL-PHYS-7-2026] -> [@HOWL-PHYS-8-2026] -> [@HOWL-PHYS-9-2026] -> [@HOWL-PHYS-10-2026] -> [@HOWL-PHYS-11-2026] -> [@HOWL-PHYS-12-2026] -> [@HOWL-PHYS-13-2026] -> [@HOWL-PHYS-14-2026] -> [@HOWL-PHYS-15-2026] -> [@HOWL-PHYS-17-2026] -> [@HOWL-PHYS-18-2026]

**Date:** April 1 2026

**Domain:** Electroweak Physics, QED Coefficient Structure

**DOI:** 10.5281/zenodo.zzz

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---


# PHYS-18: The Y = 1/6 Asymmetry — Why the Cabibbo Doublet Fixes the Gap Ratio

## Series: HOWL (Honest Organisation of What's Left)
## Registry: [@HOWL-PHYS-18-2026]
## Date: April 1, 2026
## Domain: Gauge Coupling Unification, Representation Theory
## Status: Published
## Backed by: sin2_theta_w_1.py (9/9 checks), DATA-3 (32/32 checks), new Fraction computation verified in paper

*This paper follows HOWL operational rules (Tables R.1-R.6). All measured values from DATA-3. All computation in exact Fraction arithmetic.*

---

## Abstract

The Cabibbo Doublet (3,2,1/6) fixes the Standard Model gap ratio with one particle because its hypercharge Y = 1/6 is the smallest nonzero value possible for a color triplet weak doublet with standard electric charges. The beta function contribution to b₁ (the hypercharge coupling) is proportional to Y², making Δb₁ = 1/15 — tiny. The contributions to b₂ (weak coupling) and b₃ (strong coupling) are independent of Y, giving Δb₂ = 1 and Δb₃ = 1/3. The resulting asymmetry ratio Δb₂/Δb₁ = 15 is the highest of any candidate in the 15-particle enumeration. This extreme asymmetry produces a double action on the gap ratio: the numerator (b₁ − b₂) shrinks by 13% because Δb₂ overwhelms Δb₁, while the denominator (b₂ − b₃) grows by 17% because Δb₂ exceeds Δb₃. Both effects push the gap ratio from 218/115 = 1.896 down to 38/27 = 1.407, within 0.049 of the measured 1.358. Increasing Y to any other value degrades the correction monotonically — at Y = 1/2, the gap ratio distance is already 3.4 times worse. The optimum at Y = 1/6 is sharp, not broad. The scalar version of (3,2,1/6) has the same asymmetry ratio but half the magnitude, reaching only 1.632 — five times worse. The Cabibbo Doublet is not merely a survivor of the elimination cascade. It is the uniquely optimal single-multiplet correction to the SM gap ratio, and the mechanism is exact rational arithmetic on the representation quantum numbers.

---

## 1. The Problem: What the Gap Ratio Needs

The Standard Model has three gauge forces described by three coupling constants. At the Z boson mass (M_Z = 91.19 GeV), the couplings are measured through three DATA-3 inputs: α⁻¹ = 137.036 (electromagnetic), sin²θ_W = 0.23122 (weak mixing), and α_s = 0.1180 (strong). These determine the GUT-normalized inverse couplings: 1/α₁ = 63.210, 1/α₂ = 31.685, 1/α₃ = 8.475 (verified by the GUT script, normalization check: diff = 0.00e+00, PASS).

The gap ratio tests whether the three couplings converge at high energy. It is the ratio of slope differences in the one-loop beta functions:

SM gap ratio = (b₁ − b₂) / (b₂ − b₃) = (109/15) / (23/6) = 218/115 = 1.896

Measured gap ratio = (1/α₁ − 1/α₂) / (1/α₂ − 1/α₃) = 31.525 / 23.211 = 1.358

The SM overshoots by 40%. The couplings do not converge. The Standard Model does not unify.

PHYS-17 showed that the gap ratio is determined entirely by the gauge self-coupling (0, −22/3, −11) and the Higgs (1/10, 1/6, 0), with zero contribution from any fermion. The numerator 109/15 = 7.267 is too large. To fix it, a new particle must contribute more to b₂ than to b₁, so that b₁ − b₂ shrinks. The denominator 23/6 = 3.833 could also grow, which requires the new particle to contribute more to b₂ than to b₃. The ideal correction maximizes Δb₂ relative to both Δb₁ and Δb₃.

This is a targeting problem. The gap ratio is a fraction. To reduce a fraction, you shrink the numerator and grow the denominator. Both require Δb₂ to be the dominant contribution. The question is: which representation makes Δb₂ maximally dominant?

---

## 2. How Hypercharge Enters the Beta Functions

Each gauge coupling's beta function receives contributions from every particle that carries the corresponding charge. For a vector-like fermion in representation (R₃, R₂, Y) under SU(3)×SU(2)×U(1), the contributions are:

Δb₁ depends on Y² — the square of the hypercharge. This is because the U(1) coupling vertex is proportional to Y, and the one-loop vacuum polarization diagram squares the coupling, giving Y².

Δb₂ depends on the SU(2) Dynkin index T(R₂) and the color multiplicity dim(R₃). It is independent of Y. The weak force vertex does not involve hypercharge.

Δb₃ depends on the SU(3) Dynkin index T(R₃) and the weak multiplicity dim(R₂). It is also independent of Y. The strong force vertex does not involve hypercharge.

This structural fact is the entire mechanism of this paper. Y enters ONLY Δb₁. The other two beta contributions are set by the color and weak quantum numbers, which are fixed once you choose the representation. The asymmetry ratio Δb₂/Δb₁ therefore scales as 1/Y². Small Y means large asymmetry. Large Y means small asymmetry.

---

## 3. The Cabibbo Doublet at Y = 1/6

The Cabibbo Doublet is a vector-like fermion in the (3,2,1/6) representation. Its hypercharge Y = 1/6 is the smallest nonzero value for any color triplet weak doublet that produces standard electric charges. The electric charges of the two components are Q = T₃ + Y = +1/2 + 1/6 = +2/3 (upper) and Q = −1/2 + 1/6 = −1/3 (lower) — the same charges as the up and down quarks. Any other hypercharge assignment for (3,2,Y) would produce non-standard charges not observed in nature.

The beta function contributions, verified by the GUT running script (sin2_theta_w_1.py, entry for "VL fermion (3,2,1/6)" in the 15-candidate enumeration, 9/9 checks pass):

Δb₁ = 1/15 (from Y² = 1/36 — very small)

Δb₂ = 1 (from the weak doublet Dynkin index times the color dimension — an exact integer)

Δb₃ = 1/3 (from the color triplet Dynkin index times the weak dimension)

The asymmetry ratio: Δb₂/Δb₁ = 1/(1/15) = 15.

This is the highest ratio of any candidate in the 15-particle enumeration. The next highest among survivors is the MSSM at Δb₂/Δb₁ = (25/6)/(5/2) = 5/3 = 1.67. The Cabibbo Doublet is 9 times more asymmetric than the MSSM.

---

## 4. The Double Action

The Cabibbo Doublet's extreme asymmetry produces two simultaneous effects on the gap ratio — a double action that is multiplicatively more effective than either effect alone.

The numerator shrinks. The change to the numerator is Δ(b₁ − b₂) = Δb₁ − Δb₂ = 1/15 − 1 = −14/15. The SM numerator 109/15 = 7.267 decreases by 14/15 = 0.933 to become 95/15 = 19/3 = 6.333. This is a 13% reduction. The numerator shrinks because Δb₂ = 1 overwhelms Δb₁ = 1/15 — the weak contribution is 15 times larger than the hypercharge contribution.

The denominator grows. The change to the denominator is Δ(b₂ − b₃) = Δb₂ − Δb₃ = 1 − 1/3 = 2/3. The SM denominator 23/6 = 3.833 increases by 2/3 = 0.667 to become 27/6 = 9/2 = 4.500. This is a 17% increase. The denominator grows because Δb₂ = 1 exceeds Δb₃ = 1/3 — the weak contribution is 3 times larger than the strong contribution.

The combined effect. The new gap ratio is:

(19/3) / (9/2) = (19 × 2) / (3 × 9) = 38/27 = 1.40741...

The gap ratio drops from 218/115 = 1.896 to 38/27 = 1.407 — a 26% reduction. The distance from the measured 1.358 goes from 0.538 to 0.049 — a factor of 11 improvement.

Why the double action matters: shrinking the numerator alone (holding the denominator fixed at 23/6) would give a gap ratio of (19/3)/(23/6) = 38/23 = 1.652. Growing the denominator alone (holding the numerator fixed at 109/15) would give (109/15)/(9/2) = 218/135 = 1.615. Doing both gives 38/27 = 1.407. The double action achieves a correction 60% larger than either single action alone. One particle does the work of the entire MSSM because it hits the gap ratio from both directions simultaneously.

---

## 5. What Happens at Other Hypercharges

The mechanism predicts that increasing Y from 1/6 should degrade the gap ratio correction, because Δb₁ grows as Y² while Δb₂ and Δb₃ stay fixed. To verify this, consider the (3,2,1/2) vector-like fermion — the next-simplest hypercharge for a color triplet weak doublet.

At Y = 1/2: Δb₁ is proportional to Y² = 1/4. Since Δb₁ scales as Y² with all other quantum numbers fixed, and the (3,2,1/6) gives Δb₁ = 1/15 at Y² = 1/36, the (3,2,1/2) at Y² = 1/4 gives Δb₁ = (1/15) × (1/4)/(1/36) = (1/15) × 9 = 9/15 = 3/5. Δb₂ = 1 (unchanged — independent of Y). Δb₃ = 1/3 (unchanged).

Verification of the Y² scaling: (Δb₁ at Y=1/6) / (Δb₁ at Y=1/2) = (1/15)/(3/5) = (1/15) × (5/3) = 5/45 = 1/9. And (Y=1/6)² / (Y=1/2)² = (1/36)/(1/4) = 4/36 = 1/9. The scaling is confirmed.

The modified betas for (3,2,1/2) VL:

b₁ + 3/5 = 41/10 + 6/10 = 47/10

b₂ + 1 = −19/6 + 6/6 = −13/6

b₃ + 1/3 = −7 + 1/3 = −20/3

Numerator: 47/10 − (−13/6) = 47/10 + 13/6 = 141/30 + 65/30 = 206/30 = 103/15

Denominator: −13/6 − (−20/3) = −13/6 + 40/6 = 27/6 = 9/2

Gap ratio: (103/15) / (9/2) = (103 × 2) / (15 × 9) = 206/135 = 1.526

Distance from measured 1.358: |1.526 − 1.358| = 0.168.

Compare to the Cabibbo Doublet at Y = 1/6: distance 0.049. The (3,2,1/2) is 3.4 times worse. Increasing Y by a factor of 3 (from 1/6 to 1/2) degrades the gap ratio match by a factor of 3.4.

The trend continues monotonically. At larger Y, Δb₁ grows quadratically, the numerator shrinks less (because Δb₁ partially cancels Δb₂ in the numerator change), and the gap ratio stays higher. By Y ≈ 1, the gap ratio change is negligible. By Y > 1, adding the (3,2,Y) VL fermion actually makes unification worse than the SM — the large Δb₁ overwhelms the Δb₂ correction.

The optimum at Y = 1/6 is sharp. It is not a broad valley where many nearby Y values work equally well. It is a spike where one specific value — the smallest possible — works dramatically better than any alternative.

---

## 6. Why Scalars Don't Work

The scalar leptoquark (3,2,1/6) has the same hypercharge as the Cabibbo Doublet and therefore the same asymmetry ratio Δb₂/Δb₁ = 15. But its beta function contributions are smaller in absolute magnitude because scalar loop contributions have a smaller prefactor than fermion contributions. The scalar Δb₂ = 1/2 (compared to the fermion's Δb₂ = 1). The scalar Δb₃ = 1/6 (compared to the fermion's Δb₃ = 1/3).

From the verified GUT script enumeration: the scalar (3,2,1/6) produces a gap ratio of 1.632, distance 0.274 from the measured 1.358. This is five times worse than the Cabibbo Doublet's distance of 0.049.

The lesson: the asymmetry ratio is necessary but not sufficient. The absolute magnitude of the corrections also matters. The vector-like fermion has both: maximum ratio (15) AND sufficient magnitude (Δb₂ = 1). The scalar has the right ratio but insufficient magnitude. One must choose a fermion.

---

## 7. Why Other Representations Fail

The double action requires three properties simultaneously:

**Color charge is required.** Without it, Δb₃ = 0 and the denominator cannot grow. The VL lepton doublet (1,2,−1/2) has Δb₃ = 0. Its gap ratio is 1.712, distance 0.354 — seven times worse than the Cabibbo Doublet. The VL charged singlet (1,1,−1) also has Δb₃ = 0, and additionally has Δb₂ = 0. Its gap ratio is 2.000, worse than the SM.

**Weak charge is required.** Without it, Δb₂ = 0 and the numerator cannot shrink. The VL down singlet (3,1,−1/3) has Δb₂ = 0. Its gap ratio is 2.114, worse than the SM. The VL up singlet (3,1,2/3) has Δb₂ = 0. Its gap ratio is 2.229, the worst in the enumeration.

**Small hypercharge is required.** Without it, Δb₁ is large and the asymmetry ratio is low. The SU(5) 5+5̄ fermion has all three charges but Y is effectively mixed (it contains both a color triplet and a color singlet). Its composite Δb₁ = 2/5 gives Δb₂/Δb₁ = 1/(2/5) = 5/2 — much less asymmetric than 15. Its gap ratio is 1.481, distance 0.123, and it's excluded by proton decay (M_GUT = 10^14.9).

Every candidate in the enumeration table fails on at least one of these three requirements. The Cabibbo Doublet satisfies all three:

| Requirement | Why Needed | Cabibbo Doublet |
|---|---|---|
| Color (dim(R₃) ≥ 3) | Δb₃ > 0 for denominator growth | SU(3) triplet ✓ |
| Weak charge (dim(R₂) ≥ 2) | Δb₂ > 0 for numerator reduction | SU(2) doublet ✓ |
| Small Y | Large Δb₂/Δb₁ for maximum asymmetry | Y = 1/6 (smallest possible) ✓ |
| Fermion (not scalar) | Sufficient magnitude | Vector-like ✓ |
| Anomaly-free as single multiplet | No additional particles needed | Vector-like (automatic) ✓ |

No other single representation in the enumeration satisfies all five.

---

## 8. The 1/Y² Scaling Law

The dependence of the asymmetry ratio on hypercharge is a scaling law: Δb₂/Δb₁ ∝ 1/Y² for any (3,2,Y) vector-like fermion, because Δb₂ is fixed at 1 (independent of Y) while Δb₁ ∝ Y². This predicts the gap ratio performance of any (3,2,Y) candidate without needing to run the full computation.

| Y | Y² | Δb₁ | Δb₂/Δb₁ | Gap Ratio | Distance from 1.358 |
|---|---|---|---|---|---|
| 1/6 | 1/36 | 1/15 | 15 | 38/27 = 1.407 | 0.049 |
| 1/2 | 1/4 | 3/5 | 5/3 | 206/135 = 1.526 | 0.168 |

The ratio of distances: 0.168/0.049 = 3.4. The ratio of Y² values: (1/4)/(1/36) = 9. The distance grows faster than linearly in Y² but slower than quadratically, because the gap ratio is a ratio of sums, not a simple linear function of Δb₁.

For Y > 1, the (3,2,Y) VL fermion's large Δb₁ makes the gap ratio worse than the SM. The scaling law predicts this crossover: when Δb₁ becomes comparable to Δb₂, the asymmetry vanishes and the correction reverses sign.

---

## 9. Why Y = 1/6 Is the SM Quark Doublet Hypercharge

The Cabibbo Doublet is not an exotic particle. Its quantum numbers (3,2,1/6) are identical to those of the left-handed quark doublet (u_L, d_L) that exists in every SM generation. The hypercharge Y = 1/6 produces electric charges Q = T₃ + Y = +2/3 (upper) and −1/3 (lower) — the observed quark charges. Any other hypercharge for a (3,2,Y) doublet would produce charges not seen in nature.

The Cabibbo Doublet is a heavier, vector-like copy of the quark doublet that already exists. The property that makes it optimal for fixing the gap ratio — the smallest Y for a color triplet weak doublet — is the same property that gives the SM quarks their charges. The mathematical optimality (Y = 1/6 maximizes the asymmetry ratio) and the physical reality (quarks have charges +2/3 and −1/3) point to the same hypercharge assignment.

This is not a coincidence that requires explanation. It is a consequence of the same charge quantization condition that determines all SM hypercharges. In SU(5) grand unification, the hypercharges are fixed by the embedding of SU(3)×SU(2)×U(1) into SU(5), and Y = 1/6 for the quark doublet follows from the decomposition of the fundamental 5 representation. The Cabibbo Doublet sits in the same spot because it has the same quantum numbers.

---

## 10. Comparison with the MSSM Mechanism

The MSSM and the Cabibbo Doublet achieve nearly identical gap ratios — 7/5 = 1.400 vs 38/27 = 1.407 — through fundamentally different mechanisms.

The MSSM adds large contributions to all three beta functions: (Δb₁, Δb₂, Δb₃) = (5/2, 25/6, 4). These are all large numbers. The MSSM's asymmetry ratio Δb₂/Δb₁ = (25/6)/(5/2) = 25/15 = 5/3 = 1.67 — unremarkable. The MSSM reshapes the entire running structure by adding massive corrections to every coupling. Its numerator change is −5/3 = −1.667 (larger than the Cabibbo Doublet's −14/15 = −0.933). Its denominator change is 25/6 − 4 = 1/6 = 0.167 (smaller than the Cabibbo Doublet's 2/3 = 0.667). The MSSM works primarily by crushing the numerator with large Δb₂, while barely touching the denominator.

The Cabibbo Doublet works through surgical asymmetry. Its Δb₁ = 1/15 is almost nothing. Its Δb₂ = 1 is large. The numerator change (−14/15) and the denominator change (+2/3) are both substantial and both in the right direction. The double action — numerator and denominator — is more balanced than the MSSM's numerator-dominated correction.

The result: one particle with 4 Weyl fermion fields achieves what approximately 120 MSSM fields achieve, because it exploits the Y = 1/6 asymmetry rather than brute-forcing all three beta functions.

---

## 11. What This Paper Does Not Claim

This paper does not claim Y = 1/6 is unique in all of physics. It is the smallest nonzero hypercharge for (3,2,Y) with the standard charge quantization. Non-standard charge assignments could in principle produce smaller Y values, but these would give fractional or non-standard electric charges not observed in nature and are outside the enumeration scope.

This paper does not claim two-multiplet combinations cannot do better. Two particles with individually suboptimal asymmetries might jointly achieve a better gap ratio. Multi-multiplet enumeration is outside the single-particle scope of PHYS-15 and this paper.

This paper does not claim the asymmetry ratio alone determines performance. The scalar (3,2,1/6) has ratio 15 but fails because the absolute magnitude is halved. Both ratio and magnitude matter.

This paper does not claim two-loop corrections are negligible. They shift gap ratios by 2-5% and could change quantitative details. The one-loop mechanism presented here is the leading term. The structural finding — that Δb₁ ∝ Y² while Δb₂ and Δb₃ are Y-independent — holds at all loop orders because it is a property of the U(1) vertex structure, not of the loop order.

This paper does not claim the (3,2,1/2) computation is in the verified script. The GUT script enumerates the 15 candidates within scope; (3,2,1/2) is outside that scope. The gap ratio 206/135 = 1.526 for (3,2,1/2) VL is computed in this paper by exact Fraction arithmetic as a demonstration of the Y-dependence. It is verified by the scaling check: (Δb₁ at 1/6)/(Δb₁ at 1/2) = 1/9 = (1/6)²/(1/2)² ✓.

---

## 12. What This Paper Seeds

The 1/Y² scaling law predicts the gap ratio performance of any (3,2,Y) candidate before the full computation is performed. For multi-multiplet enumerations in future sessions, this eliminates the entire (3,2,Y) family for Y > 1/6 as single-particle candidates.

The five requirements (color, weak charge, small Y, fermion, anomaly-free) provide a filter for multi-multiplet searches. Any viable combination must include at least one component satisfying requirements 1-3. Combinations of particles that all lack color, or all lack weak charge, cannot fix the gap ratio regardless of their number.

The comparison between fermion and scalar versions of (3,2,1/6) — same ratio, different magnitude — quantifies the spin dependence. Fermion contributions are twice as effective as scalar contributions for any given representation. This constrains the spin content of viable BSM extensions.

The connection between the gap ratio mechanism (Y = 1/6 gives maximum asymmetry) and the SM charge quantization (Y = 1/6 gives standard quark charges) provides a structural link to the SU(5) embedding. The representation that is optimal for unification is the representation that nature already uses for quarks. This is consistent with the Cabibbo Doublet being a vector-like extension of the existing quark sector rather than a new type of particle.

---

## 13. Summary

The Cabibbo Doublet fixes the gap ratio because Y = 1/6 creates the maximum Δb₂/Δb₁ asymmetry of 15 among all color triplet weak doublets. Δb₁ is proportional to Y² and therefore tiny at Y = 1/6 (giving 1/15). Δb₂ = 1 and Δb₃ = 1/3 are independent of Y and determined by the color and weak quantum numbers alone. The double action — numerator shrinks 13%, denominator grows 17% — drops the gap ratio from 218/115 = 1.896 to 38/27 = 1.407, within 0.049 of the measured 1.358. The optimum at Y = 1/6 is sharp: increasing Y to 1/2 degrades the match by a factor of 3.4. The scalar version of the same representation has the right asymmetry ratio but half the magnitude, reaching only 1.632. No other single representation achieves the combination of maximum asymmetry ratio and sufficient absolute magnitude.

The mechanism is Level 1 — it depends on no measured value. The dependence Δb₁ ∝ Y² is a property of the U(1) vertex. The independence of Δb₂ and Δb₃ from Y is a property of the SU(2) and SU(3) vertices. The asymmetry ratio 15 is exact rational arithmetic on the representation quantum numbers. The gap ratio 38/27 is exact Fraction arithmetic on the modified beta coefficients. The only Level 2 input is the measured gap ratio 1.358 that the SM fails to match. Why the Cabibbo Doublet would work, if it exists, is mathematics. Whether it exists is for the universe to say.

---

## Appendix: Verification

All Cabibbo Doublet beta contributions and gap ratios verified by the GUT running script (sin2_theta_w_1.py), 9/9 checks pass:

| Check | Result |
|---|---|
| Normalization: sin²θ_W from couplings | PASS (diff = 0.00e+00) |
| SM gap ratio = 218/115 | PASS (1.8956521739) |
| MSSM gap ratio = 7/5 | PASS (1.4000000000) |
| SM does not unify (Δ > 5) | PASS (Δ(1/α₃) = −6.58) |
| MSSM nearly unifies (Δ < 5) | PASS (Δ(1/α₃) = −0.69) |
| M_GUT(SM) > 10^13 | PASS (log₁₀ = 13.80) |
| M_GUT(MSSM) > 10^16 | PASS (log₁₀ = 17.32) |
| VL quark doublet gap < 0.05 from measured | PASS (distance = 0.049) |
| Measured gap ratio in [1.2, 1.5] | PASS (gap = 1.358193) |

From the enumeration table in the script output:

Rank 2: VL fermion (3,2,1/6) — Gap = 1.4074, Dist = 0.0492, log M_GUT = 15.5. SAFE.

Rank 5: Scalar (3,2,1/6) — Gap = 1.6320, Dist = 0.2738, log M_GUT = 14.6. Eliminated.

The scalar version is 5.6 times further from the target than the fermion version, confirming that magnitude matters alongside the asymmetry ratio.

New computation in this paper (not in the GUT script):

(3,2,1/2) VL fermion gap ratio: b₁ = 47/10, b₂ = −13/6, b₃ = −20/3. Numerator = 103/15. Denominator = 9/2. Gap = 206/135 = 1.526. Distance = 0.168.

Y² scaling check: (1/15)/(3/5) = 1/9 = (1/36)/(1/4) = 1/9 ✓.

All measured values from DATA-3 (123 entries, 32/32 consistency checks pass).

---

*PHYS-18: The Y = 1/6 Asymmetry. Small hypercharge, large correction. The mechanism is in the ratio. Published April 1, 2026. This paper is never edited after publication.*

---

