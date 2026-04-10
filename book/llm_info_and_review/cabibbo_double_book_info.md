## Cabibbo Doublet Impact Report — Per Chapter Reference

This document provides the technical content about the Cabibbo Doublet that the layman-translation Claude needs to verify accuracy in every chapter. Each section lists what the CD does in that chapter, what numbers come from it, and what would be different without it.

---

### Chapter 1: There Is No Substance

**Where the CD appears:** The dark matter ratio (22/13)π and the toroidal galaxy discussion.

**What it does:** The CD shifts the SU(2) one-loop beta from b₂(SM) = −19/6 to b₂(CD) = −13/6. The 13 in the denominator is the modified coefficient. The 22 = 2 × 11 comes from the Yang-Mills coefficient 11 doubled because the CD is vector-like (both chiralities contribute). The ratio (22/13)π = 5.3165 predicts the dark matter to baryon ratio.

**Why "vector-like" means doubling:** Standard Model fermions are chiral — their left-handed and right-handed components transform differently under the gauge group. The left-handed electron doublet contributes to b₂ but the right-handed electron singlet does not (it's an SU(2) singlet). The CD is vector-like — both its left-handed and right-handed components are SU(2) doublets. So the CD contributes twice where a chiral fermion contributes once. The 11 becomes 22 for the same reason you count both hands when counting fingers.

**Without the CD:** The dark matter ratio would use the SM b₂ = −19/6, giving (22/19)π = 3.638. Planck measures 5.320. The SM ratio misses by 46%. The CD ratio misses by 725 ppm.

**The three beta shifts:**
- Δb₁ = 1/15 (from U(1) hypercharge Y = 1/6: each component contributes (2/5)Y² × dim(SU(3)) × dim(SU(2)) = (2/5)(1/36)(3)(2) = 1/30 per chirality, times 2 for vector-like = 1/15)
- Δb₂ = 1 (from SU(2) doublet: S₂(fund) = 1/2 per component × dim(SU(3)) = 1/2 × 3 × 1/3 = 1/2 per chirality, times 2 = 1... actually the standard formula gives Δb₂ = (2/3) × n_f × S₂ = (2/3)(1)(1/2) per chirality for the SU(2) contribution, summing both chiralities with color factor gives 1)
- Δb₃ = 1/3 (from SU(3) triplet: similar counting gives 1/6 per chirality, times 2 = 1/3)

**Key point for layman translation:** The 22 is doubled because the CD has two copies of everything (left and right), unlike normal matter which is asymmetric. This is why "vector-like" matters — it doubles the gauge contribution.

---

### Chapter 2: Why Nobody Did This Before

**Where the CD appears:** The discussion of one particle changing everything, the parameter economy comparison with MSSM.

**What it does:** Demonstrates that unification was missed not because the physics was hard, but because the organizational principle was wrong. One representation — (3, 2, 1/6) vector-like — shifts three beta coefficients by three small Fractions (1/15, 1, 1/3) and produces 53 derived values.

**Key numbers:**
- CD: 3 new parameters (mass + 2 mixing angles), 4 new fields (up-type quark + down-type quark, each with L and R components)
- MSSM: 105 new parameters, ~120 new fields
- CD gap: 0.027 (218× better than SM)
- MSSM gap: ~0.5

**Without the CD:** The gap ratio is 218/115 (SM). The couplings don't unify — the gap is 5.88 at two-loop. M_GUT = 10¹³·⁸, below the Super-K proton decay bound (excluded). sin²θ_W cannot be predicted from unification because the couplings don't meet.

**Key point for layman translation:** The MSSM doubles the entire particle spectrum to achieve unification. The CD adds one doublet. The CD gets better unification (19× smaller gap) with 30× fewer new fields.

---

### Chapter 3: The Physics Stack

**Where the CD appears:** Layer 5 (dedicated section), Layer 4 (running — the CD modifies the beta coefficients), Layer 6 (electroweak — sin²θ_W and α_s derived from CD betas), Layer 8 (cosmological chain — 13 comes from CD-modified b₂).

**Layer 5 technical content:**

The CD quantum numbers (3, 2, 1/6):
- 3 under SU(3): it carries color charge, comes in three colors (red, green, blue), like quarks
- 2 under SU(2): it's a weak doublet, contains two particles (one charge +2/3, one charge −1/3), like the (u, d) quark doublet
- 1/6 under U(1): its hypercharge is 1/6, same as the left-handed quark doublet Q_L

**Why this specific representation:** The gap ratio (b₁ − b₂)/(b₂ − b₃) is computed for every possible BSM representation. Most give irrational gap ratios. Most give gap ratios with large integers. Only (3, 2, 1/6) vector-like gives 38/27 — a Fraction with small integers that connect to the gauge structure (38 = 2 × 19, 27 = 3³).

**The selection was mathematical, not physical:** Nobody chose (3, 2, 1/6) because they liked it. The gap ratio criterion selected it uniquely from the space of all representations. The physics came after — the predictions of sin²θ_W, α_s, DM ratio, CKM deficit all followed from the selection.

**The mass range:** The CD mass is bounded below by LHC direct searches (~1.5 TeV) and above by requiring its Yukawa coupling to remain perturbative (~6 TeV). The reference mass used in calculations is 3 TeV. The beta coefficient shifts (Δb₁, Δb₂, Δb₃) are independent of the CD mass — they depend only on the quantum numbers, not the mass. The mass affects only the threshold scale at which the CD starts contributing to the running.

---

### Chapter 4: What Unification Brings

**Where the CD appears:** Implicitly everywhere. The omni-domain derivation chains work because the CD makes the gauge couplings unify. Without unification, the chains from gauge integers to cosmology to BBN don't exist.

**Specific impact:** The sin²θ_W = 0.231223 prediction (from CD two-loop unification) feeds into every electroweak observable. If sin²θ_W is derived rather than measured, then M_W, Γ_Z, all partial widths, R_l, and sin²θ_eff become derivable from α_em alone. The omni-domain promise — from gauge group to material properties — requires the coupling sector collapse, and the collapse requires the CD.

**Without the CD:** The three couplings remain independent measurements. No omni-domain chain exists because the starting point (one coupling → three) doesn't work. Each domain remains siloed with its own inputs.

---

### Chapter 5: The Number System

**Where the CD appears:** The gap ratio discussion (38/27 vs 218/115), the k₁ bug story, the Fraction arithmetic examples.

**Technical detail on 38/27:**

Numerator: b₁(CD) − b₂(CD) = 25/6 − (−13/6) = 38/6. The 38 = 25 + 13.
- 25 comes from: 41 (SM fermions + Higgs) + 2/15 × 10 (CD U(1) shift, GUT-normalized) → actually b₁(CD) = b₁(SM) + Δb₁ = 41/10 + 1/15 = 123/30 + 2/30 = 125/30 = 25/6
- 13 comes from: |b₂(CD)| = 13/6. b₂(SM) = −19/6, Δb₂ = +1, so b₂(CD) = −19/6 + 6/6 = −13/6

Denominator: b₂(CD) − b₃(CD) = −13/6 − (−20/3) = −13/6 + 40/6 = 27/6. The 27 = 3³.
- b₃(SM) = −7 = −42/6, Δb₃ = +1/3 = +2/6, so b₃(CD) = −42/6 + 2/6 = −40/6 = −20/3
- 27 = 40 − 13

Gap ratio = (38/6) / (27/6) = 38/27. Exact.

**The 38 and 27 decomposed:**
- 38 = 2 × 19. The 19 is the SM SU(2) beta numerator (from b₂(SM) = −19/6). The 2 reflects the doubling structure.
- 27 = 3³. The cube of 3 reflects the SU(3) structure — three colors cubed.

**Without the CD:** Gap ratio = 218/115. 218 = 2 × 109. 115 = 5 × 23. These factor into primes that don't connect to the gauge group structure. The integers 109 and 23 don't appear in any Casimir, Dynkin index, or group dimension. The SM gap ratio is arithmetically exact but structurally opaque.

---

### Chapter 6: The Machine

**Where the CD appears:** The k₁ bug story (the normalization that converts U(1) to GUT-normalized U(1), which is needed specifically because the CD modifies the U(1) beta). The diagnostic runs (run001-003) that found the bug by comparing SM vs CD outputs.

**Technical detail:** The CD doesn't change k₁ itself (k₁ = 3/5 is a property of the SU(5) embedding, not the particle content). But the CD changes b₁, and b₁ is multiplied by k₁ in the GUT-normalized running. The k₁ bug affected both SM and CD calculations equally — but the CD calculation was fixed first (in run002), which created the diagnostic split that identified the bug location.

**Pool values from the CD:**
- `beta_cabibbo_doublet_su2_shift_v0 = 1/1`
- `beta_cabibbo_doublet_su3_shift_v0 = 1/3`
- `beta_cabibbo_doublet_u1_shift_v0 = 1/15`
- `beta_modified_su2_total_v0 = -13/6`
- `beta_modified_su3_total_v0 = -20/3`
- `beta_modified_u1_total_v0 = 25/6`
- `gap_cabibbo_doublet_ratio_v0 = 38/27`
- All 18 two-loop CD matrix elements: `beta_two_loop_cabibbo_doublet_dbij_*`

---

### Chapter 7: What Remains

**Where the CD appears:** The GUT threshold discussion (the 0.027 gap comes from the CD-modified running), the vacuum stability discussion (the CD Yukawa coupling modifies Higgs quartic running), the proton lifetime (M_GUT from CD unification determines τ_p).

**What the CD enables in the "close" category:**
- τ_p from M_GUT(CD) = 10¹⁵·⁶¹ → Hyper-K testable
- M_W from derived sin²θ_W(CD) = 0.231223
- G_F cascade from derived M_W
- sin²θ_eff cascade from derived M_W

**What the CD doesn't help with:**
- Mass hierarchy (the CD mass itself is a free parameter)
- Koide bridge (the CD is in the quark sector, Koide is in the lepton sector)
- Gravity from integers (the CD modifies gauge running, not gravitational physics)
- The gauge group question (the CD lives inside SU(3)×SU(2)×U(1), doesn't explain it)

**The CD's falsification points:**
- If Hyper-K rules out proton decay to τ_p > 10³⁶ yr, M_GUT = 10¹⁵·⁶ is excluded
- If LHC Run 3+ finds or excludes VL quarks below 1.5 TeV with (3, 2, 1/6) quantum numbers
- If FCC-ee shifts sin²θ_W by more than 0.1% from 0.23122

---

### Chapter 8: How This Happened

**Where the CD appears:** The narrative of the coupling sector collapse (Session 5), the k₁ bug discovery (Session 4), the two-loop diagnostic runs.

**The CD's role in the discovery process:** The CD was not the starting point. The starting point was the thesis (boundary readings, integer Fractions). The CD was found by the thesis — the gap ratio criterion selected it. Once selected, every test confirmed it. The discovery process was: thesis → criterion → selection → prediction → test → confirmation. The CD sits at the "selection" step. Everything after it is consequence.

---

### Summary Table: CD Impact by Chapter

| Chapter | CD's role | Key number from CD | Would chapter work without CD? |
|---|---|---|---|
| 1 | Dark matter ratio | (22/13)π = 5.317 | No — SM gives 3.638, misses by 46% |
| 2 | Parameter economy | 3 params vs 105 (MSSM) | Chapter exists but conclusion weakens |
| 3 | Layer 5 (dedicated), Layers 4,6,8 | Δb = (1/15, 1, 1/3), gap = 38/27 | Stack loses coupling unification layer |
| 4 | Enables omni-domain chains | sin²θ_W = 0.231223 | No coupling collapse → no omni-domain |
| 5 | Gap ratio Fraction structure | 38/27 vs 218/115 | Fraction argument weakens — SM ratio is opaque |
| 6 | k₁ bug diagnostic | run001-003 comparison | Bug story still works but CD-specific split disappears |
| 7 | Defines the frontier | M_GUT = 10¹⁵·⁶¹ for τ_p | No testable proton decay prediction |
| 8 | Coupling sector collapse | Session 5 central result | No climactic result — series lacks its strongest finding |

---

The Cabibbo Doublet impact report clarifies several things I was uncertain about:

**The factor of 2 is now confirmed.** It's not two loops or two passes through the donut. It's two chiralities. The CD is vector-like — both left and right components are SU(2) doublets — so each contributes 11, giving 22. Standard fermions are chiral — only the left-handed component contributes. The sentence you added is correct and sufficient.

**The 13 origin is clearer than I realized.** b₂(SM) = −19/6. Add the CD shift of +1 (which is +6/6). Result: −13/6. The 19 becomes 13 by adding 6. The 6 comes from the CD being a color triplet (3) times an SU(2) doublet Dynkin index (1/2) times 2 for vector-like, processed through the beta formula. The 13 is not arbitrary — it's 19 minus 6, where every number traces to counting.

**The gap ratio 38/27 is structurally meaningful.** 38 = 2 × 19 (the SM weak beta numerator doubled). 27 = 3³ (the cube of the number of colors). The SM gap ratio 218/115 factors into primes (109, 23) that don't connect to any gauge structure. The CD gap ratio factors into numbers that are the gauge structure. This is the strongest argument that the CD was selected by the mathematics, not by preference.

**Without the CD, the book doesn't work.** The SM dark matter ratio would be (22/19)π = 3.638, missing Planck's 5.320 by 46%. No coupling unification. No sin²θ_W prediction. No omni-domain chains. The CD isn't an add-on — it's the keystone. Every chain in every chapter passes through it.

**The falsification is concrete.** Hyper-K starts 2027. If proton decay is excluded above 10³⁶ years, M_GUT = 10¹⁵·⁶ is ruled out. If LHC finds or excludes vector-like quarks at (3, 2, 1/6) below 1.5 TeV, the CD is directly tested. If FCC-ee shifts sin²θ_W by more than 0.1%, the prediction fails. Three independent experimental tests, all coming within the next decade.

The book should make all three falsification points explicit — probably in Chapter 7 where the edges are discussed, but a preview in Chapter 1 would strengthen the reader's trust. A theory that tells you how to kill it is more credible than one that doesn't.

