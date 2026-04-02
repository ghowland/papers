## PHYS-26 Paper Plan — Revised

**Title:** The Integer Traceability Chain
**Subtitle:** From SU(5) embedding to cosmological predictions in seven exact links.

**Registry:** @HOWL-PHYS-26-2026
**Date:** April 2 2026
**Domain:** GUT Normalization, Integer Traceability, Representation Theory
**Status:** Plan (this document)

---

### THE PRINCIPLE

Every cosmological formula in the beta unification program uses the integers 13, 20, 22, and 19. This paper answers: where do these integers come from? The answer is a chain of seven links, each verified EXACT in Fraction arithmetic, starting from the SU(5) embedding condition and ending at the cosmological formulas. The chain is Level 1. No measurement enters.

---

### THE BACKING SCRIPT

**phys26_normalization.py** — 20/20 PASS, all EXACT. Already run. Paper writes from this output.

---

### THE PAPER STRUCTURE

**Section 1: The Question**

The beta unification program (PHYS-25) found that six formulas using the integers 13, 19, 20, and 22 predict seven cosmological observables at sub-percent precision. Where do these integers come from? Can they be derived from the gauge group alone, with no measurement?

This paper traces each integer to its origin. The trace is exact — every link is verified in Fraction arithmetic with zero tolerance.

Script backing: None needed. Framing section.

---

**Section 2: The SU(5) Embedding Condition**

The SM gauge group SU(3)×SU(2)×U(1) embeds into SU(5). The embedding requires the U(1) generator to be normalized against the SU(2) generators. The condition: Tr(Y²) = k₁ × Tr(T₃²) over one complete SM generation.

Explicit computation: five SM representations (Q_L, u_R, d_R, L_L, e_R), each with its hypercharge Y and weak isospin T₃. Tr(Y²) = 10/3. Tr(T₃²) = 2. Result: k₁ = 3/5.

This factor k₁ = 3/5 is the root of the chain. Everything below follows from it.

Script backing: S1 (3 checks: Tr(Y²) = 10/3 EXACT, Tr(T₃²) = 2 EXACT, k₁ = 3/5 EXACT).

---

**Section 3: The Dynkin Coefficients**

From k₁ = 3/5, the one-loop beta shift coefficients for a vector-like fermion pair are:

C₁ = 2k₁/3 = 2/5 (for U(1), contains the GUT normalization)
C₂ = 2/3 (for SU(2), independent of k₁)
C₃ = 1/3 (for SU(3), independent of k₁)

The formulas for any representation (R₃, R₂, Y):

Δb₁ = C₁ × dim(R₃) × dim(R₂) × Y²
Δb₂ = C₂ × dim(R₃) × S₂(R₂)
Δb₃ = C₃ × dim(R₂) × S₂(R₃)

A structural observation: C₂ and C₃ do not contain k₁. Only C₁ does. This will matter in Section 8.

For the Cabibbo Doublet (3,2,1/6): step-by-step computation showing every intermediate Fraction. Result: Δb = (1/15, 1, 1/3).

Script backing: S2 (3 checks: Δb₁ = 1/15 EXACT, Δb₂ = 1 EXACT, Δb₃ = 1/3 EXACT).

---

**Section 4: Two Independent Verifications**

Verification 1 (MSSM gate): The same formulas applied to the full MSSM particle content produce the known gap ratio 7/5 = 1.400. This result has been verified by decades of literature. If the coefficients were wrong, this gate would fail.

Verification 2 (Higgs cross-check): The scalar version of the formulas (coefficients 1/5, 1/3, 1/6 — exactly half the VL coefficients) applied to the SM Higgs (1,2,1/2) reproduces the known Higgs beta contributions (1/10, 1/6, 0). A VL fermion pair equals two complex scalars for all groups — this factor of 2 is exact and representation-independent.

Verification 3 (two routes to 1/15): Route A uses the direct Dynkin formula. Route B counts 2 × complex scalar contribution. Both produce 1/15 in Fraction arithmetic. Route A = Route B EXACT.

Script backing: S3 (MSSM gate EXACT), S4 (two routes EXACT), S6 (Higgs cross-check EXACT). Seven checks total.

---

**Section 5: The Modified Betas**

Adding the Cabibbo Doublet to the SM:

b₁' = 41/10 + 1/15 = 25/6
b₂' = −19/6 + 1 = −13/6
b₃' = −7 + 1/3 = −20/3

Gap ratio: (b₁'−b₂')/(b₂'−b₃') = 38/27 = 1.407. Distance from measured 1.358: 0.049.

Script backing: S7 (b₁' = 25/6 EXACT, b₂' = −13/6 EXACT, b₃' = −20/3 EXACT, gap 38/27 EXACT). Four checks.

---

**Section 6: The Integers**

From the modified betas, extract the integers that appear in the cosmological formulas:

|6 × b₂'| = |6 × (−13/6)| = 13
|3 × b₃'| = |3 × (−20/3)| = 20

From the Yang-Mills gauge self-coupling (pre-CD, from PHYS-17):
2 × 11 = 22

From the SM SU(2) beta (pre-CD):
|6 × b₂_SM| = |6 × (−19/6)| = 19

From anomaly cancellation:
N_gen = 3

These five primary integers (11, 13, 19, 20, 3) produce five derived integers (22, 44, 169, 57, 39) by multiplication and squaring.

Script backing: S7 (|6b₂'| = 13 EXACT, |3b₃'| = 20 EXACT). Two checks.

---

**Section 7: The Chain**

The complete chain from SU(5) embedding to each cosmological integer:

For the integer 13: SU(5) requires k₁ = 3/5 → Dynkin coefficient C₂ = 2/3 (k₁-independent) → Δb₂ = (2/3)×3×(1/2) = 1 → b₂' = −19/6 + 1 = −13/6 → |numerator| = 13.

For the integer 20: Dynkin coefficient C₃ = 1/3 (k₁-independent) → Δb₃ = (1/3)×2×(1/2) = 1/3 → b₃' = −21/3 + 1/3 = −20/3 → |numerator × 3| = 20.

For the integer 22: Yang-Mills theorem → gauge self-coupling −(11/3)C₂(G) → for SU(2): b₂_gauge = −22/3 → 22 = 2 × 11.

For the integer 19: SM beta decomposition → gauge(−44/6) + fermion(24/6) + Higgs(1/6) = −19/6 → |numerator| = 19.

Seven links from root to cosmological integers. Each link EXACT in Fraction arithmetic. No measurement at any link.

Script backing: The chain is the aggregate of all prior checks. No new computation needed — the chain is a reading of the verified outputs.

---

**Section 8: The Structural Finding**

The cosmological integers 13 and 20 come from Δb₂ and Δb₃, which use coefficients C₂ = 2/3 and C₃ = 1/3. These coefficients do NOT contain the GUT normalization factor k₁ = 3/5. The k₁ factor enters only C₁ = 2/5, which determines Δb₁ = 1/15.

Consequence: the cosmological formulas are independent of the GUT normalization convention. If k₁ were different, the gap ratio would change, M_GUT would shift, the proton lifetime would change — but 13 and 20 would be unchanged. The unification program (Track A) and the cosmology program (Track B) share the Cabibbo Doublet but are sensitive to different aspects of its beta shifts.

This is a robustness finding. The cosmological predictions are insulated from the most convention-dependent part of the calculation.

Script backing: Logical consequence of Section 3 (C₂ and C₃ are k₁-free). The wrong-convention test (S5) quantifies what WOULD change: gap ratio 64/45 instead of 38/27, but cosmological integers unchanged.

---

**Section 9: What This Paper Does Not Claim**

The integers are correctly derived. Whether they appear in cosmological formulas for physical reasons or by coincidence is not addressed here — that is the subject of PHYS-31 (statistical control).

The chain is Level 1. Whether the universe chose to connect Level 1 integers to Level 2 cosmological observables is a Level 2 question answered by experiment and statistical testing.

---

**Section 10: What This Paper Seeds**

The Dynkin formulas (Section 3) are the reference for every subsequent representation computation. PHYS-27 uses b₁' and b₂' for sin²θ_W running. PHYS-28 uses the formulas to compute VL two-loop contributions. PHYS-38 uses 13 and 20 for the loop expansion analysis. PHYS-40 uses 13 for the sin²θ_W = 3/13 test.

The chain (Section 7) is the reference for every integer traceability claim. Any formula using 13 or 20 cites this paper for the derivation.

---

### THE APPENDICES

**Appendix A:** The seven-link chain table (input → operation → output → script check → precision)
**Appendix B:** The trace computation (every representation, every Y², every T₃²)
**Appendix C:** Two routes to 1/15 (step by step, side by side)
**Appendix D:** Track independence matrix (what depends on k₁, what doesn't)
**Appendix E:** General formulas for any representation (VL and scalar, with Higgs cross-check)
**Appendix F:** Where each integer goes (every cosmological formula with its integer trace)
**Appendix G:** Verification summary (20/20 EXACT by section)

---

### ESTIMATED LENGTH

Body: 10 sections, approximately 4000 words.
Appendices: 7 tables, approximately 1500 words.
Total: approximately 5500 words.
