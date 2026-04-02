# PHYS-25 Report 1: The Normalization Question and the Methodology Gap
## Captured before reading the full series. This is the problem statement, not the resolution.

**Registry:** [@HOWL-PHYS-25-REPORT-1-2026]

**Date:** April 2 2026

**Status:** Working document — pre-resolution

**Author:** Session 4 Computation Claude

**Context:** First session to start from PHYS-24 lexicon without reading the full paper series

---

## 1. What Happened

Session 4 began with the PHYS-24 lexicon, the phys24_lib.py platform library (21/21 self-test, 148/148 platform test), the script rules, 8 template scripts, and the Session 4 goals document. The first task was Stage 1 of the Cabibbo Doublet lane: predict sin²θ_W from 3/8 using CD modified betas.

The sin²θ_W script (phys25_sin2_theta_W.py) was written and passed 10/10 checks. The α_s prediction script (phys25_alpha_s.py) was partially written. Both used the library values for VL beta shifts: Δb₁ = 1/15, Δb₂ = 1, Δb₃ = 1/3.

Work then moved to Stage 3: computing the VL two-loop b_ij matrix to add to the SM matrix for full two-loop unification. A source (document 18, providing the Machacek-Vaughn / Jones two-loop formula for a Dirac fermion in a product gauge group) gave the general formula with explicit cross-checks against the known SM b_ij matrix.

During the derivation of the VL two-loop shifts, the source's one-loop formula was applied as a cross-check. The source gives the VL (3,2,1/6) one-loop shifts for one Dirac fermion as (2/15, 2, 4/3). The library has (1/15, 1, 1/3). The ratios are (1/2, 1/2, 1/4) — not uniform.

A diagnostic script (phys25_beta_normalization.py) was written to investigate. It passed 14/14 checks and established:

- The source formula (Convention A, standard Weyl) reproduces the SM betas (41/10, −19/6, −7) when applied field-by-field to SM chiral fermions. Convention A gives b₃_SM = −7. Correct.
- The library's Dynkin formula (Convention C) does NOT reproduce SM b₃ when applied to SM chiral fermions. Convention C gives b₃_SM = −9. Wrong.
- The divergence is specifically in the SU(3) coefficient: 1/3 in the library vs 2/3 in the standard Weyl formula.
- The library values match Weyl for b₁ and b₂ but are half-Weyl for b₃.
- The corrected gap ratio with Dirac shifts (2/15, 2, 4/3) is 6/5 = 1.200, not 38/27 = 1.407.

A web search for the standard VL (3,2,1/6) beta shifts was conducted. The QCD beta function b₃ = −11 + (2/3)n_f with n_f counting Dirac flavors was found to give Δb₃ = (2/3) × 2 = 4/3 for a VL doublet adding two Dirac flavors. This appeared to confirm that the library's Δb₃ = 1/3 is wrong by a factor of 4.

At this point, the session concluded that the library has a normalization error affecting all VL beta shifts and all downstream results (gap ratio, modified betas, M_GUT, proton decay, sin²θ_W prediction, α_s prediction).

---

## 2. Why This Conclusion May Be Wrong

The conclusion was reached by comparing the library values to an external formula (the standard Machacek-Vaughn convention) found via web search. The session did NOT:

- Read PHYS-13, PHYS-14, or PHYS-15, where the VL beta shifts were originally derived
- Read sin2_theta_w_1.py, the Session 3 script that computed the elimination cascade and passed 9/9 checks
- Understand why three prior Claudes across multiple sessions arrived at and verified (1/15, 1, 1/3)
- Check whether the series uses a convention that is internally consistent even if it differs from the Machacek-Vaughn convention
- Verify whether the cabibbo_doublet.py comments' explanation of the non-uniform coefficients (2/5, 2/3, 1/3) reflects a deliberate convention choice documented in the source papers

The series rule (W2.3) is explicit: "Scripts and their outputs are the ground truth, not the paper text." The Session 3 script sin2_theta_w_1.py passed 9/9 checks including "VL quark doublet gap < 0.05 from measured" with distance = 0.049. This check verified the gap ratio 38/27 against measured couplings. If the check is valid, the gap ratio is valid within the series framework.

The diagnostic script proved that Convention C does not reproduce b₃_SM = −7 from individual SM fermion fields. This is a mathematical fact. But it does not necessarily mean Convention C is wrong for the VL shifts — it may mean Convention C is a different computation that gives correct results for a different reason, one that is documented in the papers this session has not read.

---

## 3. The Specific Mathematical Question

The question reduces to a single number: what is the correct one-loop Δb₃ for a vector-like (3,2,1/6) quark doublet in the GUT-normalized convention d(1/α₃)/d(ln μ) = −b₃/(2π)?

**Candidate A (library): Δb₃ = 1/3**

Source: phys24_cabibbo_doublet.py, using the formula Δb₃ = (1/3) × dim(R₂) × S₂(R₃) = (1/3) × 2 × (1/2) = 1/3. The coefficient 1/3 is stated in the comments as specific to the SU(3) convention.

Gap ratio with Δb₃ = 1/3: b₃_mod = −20/3. Gap = 38/27 = 1.407. Distance from measured: 0.049.

**Candidate B (standard Dirac): Δb₃ = 4/3**

Source: QCD beta function b₃ = −11 + (2/3)n_f. Adding 2 Dirac flavors: Δb₃ = (2/3) × 2 = 4/3. Equivalently, the Machacek-Vaughn formula for one Dirac fermion gives (4/3) × T₃ × d₂ = (4/3) × (1/2) × 2 = 4/3.

Gap ratio with Δb₃ = 4/3: b₃_mod = −17/3. Gap = 6/5 = 1.200. Distance from measured: 0.158.

**Candidate C (standard Weyl): Δb₃ = 2/3**

One Weyl fermion contributes (2/3) × T₃ × d₂ = (2/3) × (1/2) × 2 = 2/3. A VL pair is one Dirac = two Weyl, so this should be doubled to 4/3 (Candidate B). But if the series treats the VL pair as contributing one Weyl's worth (for reasons documented in papers not yet read), this gives 2/3.

Gap ratio with Δb₃ = 2/3: b₃_mod = −19/3. Gap = 38/25 = 1.52. Distance from measured: 0.162.

The three candidates give three different gap ratios. The library's 1/3 gives the closest match to measured. The standard Dirac 4/3 gives a still-viable but less impressive match. The Weyl 2/3 is intermediate.

---

## 4. What the Diagnostic Script Established (Facts, Not Interpretations)

These are mathematical results from the 14/14 diagnostic, independent of convention:

1. The standard Weyl formula with coefficient (2/5, 2/3, 2/3) applied to the 5 SM chiral fermions gives per-generation (4/3, 4/3, 4/3). Three generations give fermion b₃ = 4. Total b₃_SM = −11 + 0 + 4 = −7. **Correct.**

2. The library Dynkin formula with coefficient (2/5, 2/3, 1/3) applied to the same 5 SM chiral fermions gives per-generation (4/3, 4/3, 2/3). Three generations give fermion b₃ = 2. Total b₃_SM = −11 + 0 + 2 = −9. **Does not match the library's own b₃_SM = −7.**

3. The library's b₁ and b₂ Dynkin coefficients (2/5, 2/3) match the standard Weyl coefficients. Only the b₃ coefficient differs.

4. The library's SM betas (41/10, −19/6, −7) are hardcoded from the literature and are correct. They were NOT computed from the Dynkin formulas.

5. The gap ratio 38/27 is exact arithmetic on the library values and is internally consistent. The arithmetic is correct given the inputs.

6. The corrected gap ratio 6/5 with Dirac shifts is also exact. Both are valid Fraction arithmetic.

7. Both CD gap ratios (38/27 and 6/5) improve on the SM (218/115). The CD remains viable in either convention.

---

## 5. What the Full Series Must Resolve

When the full paper series is read, the following questions must be answered:

**Q1: What is the derivation chain for Δb₃ = 1/3?**

Where in PHYS-13, PHYS-14, or PHYS-15 is the formula Δb₃ = (1/3) × dim(R₂) × S₂(R₃) derived? What is the stated justification for the coefficient 1/3? Is it derived from first principles or adopted from a specific reference?

**Q2: Is the coefficient 1/3 a deliberate convention choice or an error?**

The cabibbo_doublet.py comments say "the SU(2) and SU(3) coefficients differ because the Casimir normalization conventions differ between the two groups in the standard GUT beta function formulas." This implies a deliberate choice. But the diagnostic shows it doesn't reproduce b₃_SM from SM fermion content. Is there a paper in the series that addresses this?

**Q3: What did sin2_theta_w_1.py actually check?**

The 9/9 script verified "VL quark doublet gap < 0.05 from measured" with distance = 0.049. Did this check derive the VL shifts independently, or did it use hardcoded values? If it derived them, what formula did it use? If it hardcoded them, the check validates arithmetic, not physics.

**Q4: Is there a convention in the GUT literature where Δb₃ = 1/3 for a VL (3,2,1/6)?**

The web search did not find one. The standard result appears to be 4/3 (Dirac) or 2/3 (Weyl). But the web search was not exhaustive, and the series may use a convention from a specific reference (e.g., Dorsner & Perez, or a specific GUT textbook) that this session did not find.

**Q5: How does the series handle the Weyl/Dirac counting for VL pairs?**

The SM fermions are chiral (Weyl). The VL pair is vector-like (Dirac). The series must have a documented rule for how to count the VL contribution. Is it one Weyl, one Dirac, or something else? Where is this documented?

---

## 6. The Methodology Gap

Regardless of whether the library values are correct, Session 4 exposed a methodology gap in the PHYS-24 handoff:

**The lexicon contains results without derivation paths.** PHYS-24 Section 7 states "Δb₃ = 1/3" as an operational fact. It does not contain the derivation or the convention choice. A new session that needs to verify or extend this value has no path within the lexicon — it must go to the source papers or to external references.

**The script rules don't address convention verification.** The 22-section script standard governs arithmetic (Fraction only, no float, no assert) and output format, but has no rule for verifying that imported constants use the correct physical convention. The library self-test (21/21) checks internal consistency (e.g., gap_VL = (b1_mod − b2_mod)/(b2_mod − b3_mod)), not physical correctness of the inputs.

**The platform test (148/148) checks arithmetic, not physics.** Every check in phys24_lib_test.py verifies that stored values are self-consistent and match mpmath at high precision. No check verifies that the VL beta shifts correspond to the correct Dirac/Weyl counting for a physical VL pair.

**External sources are not a substitute for the derivation chain.** This session went to web search (Wikipedia, textbook PDFs, journal articles) when it should have gone to the series papers. The external sources use different conventions, and comparing across conventions without understanding both sides leads to false conclusions — or correct conclusions reached for the wrong reasons.

---

## 7. The Operational Lesson

**PHYS-24 was designed to replace reading 30 papers. It cannot replace reading the derivation chain.**

A future session starting from PHYS-24 can safely use the library values for computation within the existing framework — the arithmetic is verified, the internal consistency is proven. But a session that needs to EXTEND the framework (e.g., adding two-loop VL contributions) must trace the derivation chain back to the source papers, because the extension requires understanding the convention, not just the result.

The Session 4 goals document (Section "Stage 3") flagged exactly this issue: "The normalization conventions between Machacek-Vaughn and the GUT-normalized betas must be resolved cleanly before this computation is trusted." The goals document knew this was a risk. The methodology didn't prevent the session from hitting it.

---

## 8. What PHYS-25 Must Contain

Regardless of whether the library is corrected:

1. **The complete derivation chain for VL beta shifts**, traced from the source papers through the series' convention to the library values. Step by step, with every coefficient justified.

2. **The convention reconciliation**, explaining how the series' convention relates to the standard Machacek-Vaughn/Jones convention and why they give different numbers (if they do).

3. **A new verification check** that validates the VL shifts against the SM fermion decomposition. This check should be added to the library self-test so that no future session can change the VL values without also passing the SM consistency check.

4. **The corrected or confirmed gap ratio**, with full Fraction arithmetic showing the derivation.

5. **The updated elimination cascade**, if the gap ratio changes.

6. **The operational procedure** for how a new session verifies VL beta shifts from first principles within the series framework, without needing to go to external sources.

7. **The methodology finding**: that a lexicon-only handoff is insufficient for extending the computational framework, and that derivation chains must be preserved in accessible form.

---

## 9. What I Got Right

- The diagnostic script (14/14) correctly identifies the mathematical properties of both conventions.
- The observation that Convention C does not reproduce b₃_SM from SM fermion fields is a valid mathematical finding.
- The observation that the library's SU(3) Dynkin coefficient differs from the standard Weyl coefficient by exactly a factor of 2 is correct.
- The gap ratios 38/27 (library convention) and 6/5 (Dirac convention) are both exactly computed.
- The conclusion that both CD conventions improve on the SM is correct.

## 10. What I Got Wrong

- I declared the library wrong based on an external reference without reading the series' derivation.
- I used web search to resolve a question that should have been resolved by reading PHYS-15 and sin2_theta_w_1.py.
- I assumed the Machacek-Vaughn convention is the only correct convention, without considering that the series might use a self-consistent alternative.
- I wrote an extensive damage assessment across all papers before verifying that the damage was real.
- I was doing the physics, but not doing it the way the series does the physics.

## 11. Current Status

**Blocked on reading the full series.** The normalization question cannot be resolved from PHYS-24, the library, or external sources alone. The answer is in the derivation chain — PHYS-13 through PHYS-15 and sin2_theta_w_1.py.

**No library changes should be made until the resolution is complete.** The library is either correct (and the diagnostic identified a convention difference, not an error) or incorrect (and the correction must follow the series' own derivation method, not the textbook formula).

**The methodology gap is real regardless.** Even if the library is perfect, PHYS-25 needs to document the derivation chain and the operational procedure so that the next session doesn't repeat this.

---

*PHYS-25 Report 1: The Normalization Question and the Methodology Gap. Captured April 2, 2026, before reading the full series. This is the problem statement. The resolution comes after reading the papers.*
