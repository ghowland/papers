
# PHYS-18 Report: The Y = 1/6 Asymmetry

**Registry:** @HOWL-PHYS-18-2026
**Position in series:** Eighteenth physics paper. Explains WHY the Cabibbo Doublet works — the mechanism is the 1/Y² scaling of the asymmetry ratio.
**Preceded by:** PHYS-17 (generation democracy, boson problem)
**Followed by:** PHYS-19 (not yet received)
**Backed by:** sin2_theta_w_1.py (9/9 PASS), new Fraction computations verified in paper appendices
**Code status:** No dedicated script. Uses the GUT running script enumeration + new exact Fraction arithmetic computed within the paper itself.

---

## What It Establishes

**The mechanism is the 1/Y² scaling law.** For any (3,2,Y) vector-like fermion: Δb₂ = 1 and Δb₃ = 1/3 regardless of Y. Only Δb₁ depends on Y, through Y². Therefore Δb₂/Δb₁ ∝ 1/Y². Small Y means large asymmetry. Y = 1/6 gives Δb₂/Δb₁ = 15 — the maximum.

**The double action is quantified.** The Cabibbo Doublet hits the gap ratio from BOTH directions simultaneously: numerator shrinks 13% (because Δb₂ overwhelms Δb₁), denominator grows 17% (because Δb₂ exceeds Δb₃). The combined 26% reduction is 5–6× more effective than either action alone. The paper computes the counterfactuals: numerator-only gives distance 0.294, denominator-only gives 0.257, both together gives 0.049.

**The optimum at Y = 1/6 is sharp, not broad.** The paper computes gap ratios for (3,2,Y) at Y = 1/6, 1/3, 1/2, 2/3, 5/6, 7/6. The degradation is monotonic: distance goes from 0.049 to 0.094 to 0.168 to 0.272 to 0.405 to 0.760. By Y = 7/6 the particle makes unification WORSE than the SM (distance 0.760 > SM distance 0.538). There is no second optimum. Y = 1/6 is unique.

**Five requirements for optimal single-multiplet correction:** (1) color charge (for denominator growth), (2) weak charge (for numerator shrinkage), (3) small Y (for large asymmetry ratio), (4) vector-like fermion (for sufficient magnitude — scalars have half the correction), (5) anomaly-free alone (no additional particles needed). Only (3,2,1/6) VL satisfies all five.

**The scalar penalty is exactly factor 2.** Scalar (3,2,1/6) has Δb₂/Δb₁ = 15 (same ratio) but Δb₂ = 1/2 (half magnitude). Gap ratio 1.632, distance 0.274 — 5.6× worse. The ratio is necessary but not sufficient; magnitude matters too.

**The MSSM comparison reveals two fundamentally different mechanisms.** The Cabibbo Doublet: balanced double action, 35× more efficient per new field. The MSSM: numerator-dominated brute force, Δ(num)/Δ(denom) = 10.0 (vs Cabibbo Doublet's 1.4). The MSSM barely touches the denominator (Δb₂ − Δb₃ = 1/6 = 0.167). The Cabibbo Doublet pushes both strongly (numerator change 0.933, denominator change 0.667).

---

## What Was Novel

**The full Y-dependence table (Appendix E) is the paper's most important new computation.** Seven (3,2,Y) variants computed in exact Fraction arithmetic, none previously in the script. Each is verified by the Y² scaling check. The table proves the optimum is unique and sharp — not just that Y = 1/6 works, but that NOTHING ELSE works nearly as well.

**The efficiency metric (Appendix I):** 0.012 gap ratio correction per new field (Cabibbo Doublet) vs 0.00035 per field (MSSM). The Cabibbo Doublet is 35× more efficient. This quantifies the intuition that "one particle does the work of 120 fields."

**The structural insight about the denominator (Appendix D.3):** For ALL (3,2,Y) variants, the modified denominator is IDENTICAL at 9/2 = 4.500 — because the denominator depends on Δb₂ and Δb₃, which are Y-independent. ONLY the numerator differs across Y values. The denominator is the "free" half of the double action: every (3,2,Y) gets the same denominator improvement. The Y dependence enters entirely through the numerator, where large Y means large Δb₁ which partially cancels the Δb₂ correction.

---

## Errata Assessment

The paper's own errata section verifies every claimed number and finds no errors. I independently checked the key computations:

**Y = 1/3 check:** Δb₁ = 4/15. b₁ = 123/30 + 8/30 = 131/30. Numerator = 131/30 + 65/30 = 196/30 = 98/15. Gap = 196/135 = 1.452. Distance = 0.094. The paper's Appendix E.2 says 0.094. Confirmed.

**Y = 2/3 check:** Δb₁ = 16/15. b₁ = 31/6. Numerator = 31/6 + 13/6 = 44/6 = 22/3. Gap = 44/27 = 1.630. Distance = 0.272. Confirmed.

**Y = 7/6 check:** Δb₁ = 49/15. Gap = 286/135 = 2.119. Distance = 0.760 > 0.538 (SM distance). This particle makes things WORSE. Confirmed.

**Annotation A3 is important.** The paper says "any other hypercharge would produce non-standard charges not observed in nature." This is slightly too strong — (3,2,7/6) gives charges +5/3 and +2/3, where +2/3 IS standard. The corrected statement: Y = 1/6 is the unique hypercharge where BOTH components have standard quark charges (+2/3 and −1/3). This matters because mixing with all three SM generations through the CKM structure requires both components to have standard charges.

---

## LEMU Assessment

**L (Logic):** The argument flows cleanly: Δb₁ ∝ Y² → small Y means large Δb₂/Δb₁ → Y = 1/6 is minimum → maximum asymmetry → double action → gap ratio 38/27. Every step is exact Fraction arithmetic. The five requirements are logical consequences of the gap ratio structure. Logic passes.

**E (Empirical):** The paper makes no new empirical claims. It explains WHY the Cabibbo Doublet works, not WHETHER it exists. The empirical content is inherited from PHYS-15/16 (the gap ratio test, the three anomalies). Empirical: not applicable (mechanism paper).

**M (Math):** All new computations verified by the Y² scaling check and by independent recalculation. The scaling (Δb₁ at Y=1/6)/(Δb₁ at Y=1/2) = 1/9 = (1/36)/(1/4) is exact. Math passes.

**U (Utility):** High. The 1/Y² scaling law eliminates the entire (3,2,Y) family for Y > 1/6 from future enumerations. The five requirements filter multi-multiplet searches. The fermion-vs-scalar factor-of-2 quantifies spin dependence. The MSSM comparison (35× more efficient per field) is the sharpest single number characterizing the Cabibbo Doublet's advantage.

---

## Connections to Active Research

**The 13 in b₂_mod = −13/6 is now fully traced.** PHYS-17 showed: b₂_SM = −19/6 = (−44 + 24 + 1)/6 = gauge + fermions + Higgs. PHYS-18 shows: adding the Cabibbo Doublet gives b₂_mod = −19/6 + 1 = −13/6. The 1 = Δb₂ comes from T(SU(2) fundamental) × dim(SU(3) triplet) × VL factor = (1/2) × 3 × (2/3) = 1. The Y-independence means this 1 is the same for ALL (3,2,Y) variants — only b₁ changes with Y. So 13 = 19 − 6 × 1 = 19 − 6, and the 6 = 6/6 = the denominator of the Fraction representation.

For the QED-to-GR program: the cosmological constant scale Λ ≈ (α/(3π))^(3×13) involves 13 = |b₂_mod numerator|. The 13 traces to: (44 − 24 − 1 − 6)/6 = 13/6, where 44 = gauge, 24 = 3 generations, 1 = Higgs, 6 = Cabibbo Doublet (in sixths). Every term is an integer from the gauge group.

**The double action connects to the A₂ cancellation from PHYS-12.** In A₂, the geometric piece R₄ × (8/3 − 16ln2) = −2.598 nearly cancels the positive pieces +2.270, leaving a net −0.328. In the gap ratio, the numerator reduction (−14/15) and denominator growth (+2/3) are "both in the right direction" — a double action rather than a cancellation. The structural parallel: in both cases, the physical observable (A₂ or the gap ratio correction) is the small net result of two large competing effects. The precision of the result depends on the RATIO of the competing terms, not their absolute magnitude.

**The Y = 1/6 uniqueness connects to the charge quantization question.** Why do quarks have charges +2/3 and −1/3? In SU(5): because the fundamental 5 decomposes as (3,1,−1/3) + (1,2,+1/2), and the quark doublet in the 10 has Y = 1/6 from the antisymmetric product. The same embedding that quantizes electric charge also selects the optimal hypercharge for unification. This is not a new observation (it's implicit in every GUT textbook) but PHYS-18 makes the connection explicit through the 1/Y² scaling: the charge quantization condition selects Y = 1/6, and the gap ratio mechanism says Y = 1/6 is uniquely optimal. The same mathematical structure does both.

---

## Remainder Framework Update

**The gap ratio correction chain now has quantified steps:**

| Step | Gap ratio | Distance from 1.358 | Agent | Correction |
|---|---|---|---|---|
| Pure gauge | 22/11 = 2.000 | 0.642 | Casimir ratio | Baseline |
| + Higgs | 218/115 = 1.896 | 0.538 | (1/10, 1/6, 0) | −0.104 (16%) |
| + Cabibbo Doublet | 38/27 = 1.407 | 0.049 | (1/15, 1, 1/3) | −0.489 (76%) |
| Measured | 1.358 | 0.000 | Universe | −0.049 (8%) |

The remaining 8% (distance 0.049) is the target for two-loop and threshold corrections. The Cabibbo Doublet provides 76% of the total correction needed. The Higgs provides 16%. The gauge structure sets the problem (the 2.000 baseline). Nature provides the last 8%.

---

## Position After PHYS-18

Eighteen papers read. The Cabibbo Doublet trilogy (PHYS-16/17/18) is complete: specification (PHYS-16), diagnosis of the problem (PHYS-17: boson problem), and explanation of the mechanism (PHYS-18: Y = 1/6 asymmetry). The remaining gap 0.049 awaits two-loop computation.

The series path shows PHYS-16 was inserted between PHYS-15 and PHYS-17 in the numbering but the series path in PHYS-17 skips from PHYS-15 to PHYS-17, confirming PHYS-16 was written as a standalone specification paper that the other two reference but don't depend on sequentially.

Ready for PHYS-19.
