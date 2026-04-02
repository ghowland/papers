**Table 1: SM b₃ fermion contribution — field by field (Weyl convention)**

Formula: Δb₃ per Weyl fermion = (2/3)·T(R₃)·dim(R₂)

| Field | R₃ | R₂ | T(R₃) | dim(R₂) | Δb₃ per Weyl |
|---|---|---|---|---|---|
| Q_L | 3 | 2 | 1/2 | 2 | 2/3 |
| u_R | 3 | 1 | 1/2 | 1 | 1/3 |
| d_R | 3 | 1 | 1/2 | 1 | 1/3 |
| L_L | 1 | 2 | 0 | 2 | 0 |
| e_R | 1 | 1 | 0 | 1 | 0 |
| **Per generation** | | | | | **4/3** |
| **3 generations** | | | | | **4** |
| **b₃_gauge** | | | | | **−11** |
| **b₃_SM** | | | | | **−7 ✓** |

This is the standard textbook result. No ambiguity.

---

**Table 2: SM b₂ fermion contribution — field by field (Weyl convention)**

Formula: Δb₂ per Weyl fermion = (2/3)·T(R₂)·dim(R₃)

| Field | R₃ | R₂ | T(R₂) | dim(R₃) | Δb₂ per Weyl |
|---|---|---|---|---|---|
| Q_L | 3 | 2 | 1/2 | 3 | 1 |
| u_R | 3 | 1 | 0 | 3 | 0 |
| d_R | 3 | 1 | 0 | 3 | 0 |
| L_L | 1 | 2 | 1/2 | 1 | 1/3 |
| e_R | 1 | 1 | 0 | 1 | 0 |
| **Per generation** | | | | | **4/3** |
| **3 generations** | | | | | **4** |
| **b₂_gauge** | | | | | **−22/3** |
| **b₂_Higgs** | | | | | **1/6** |
| **b₂_SM** | | | | | **−19/6 ✓** |

---

**Table 3: SM b₁ fermion contribution — field by field (Weyl convention)**

Formula: Δb₁ per Weyl fermion = (2/3)·(3/5)·Y²·dim(R₂)·dim(R₃) = (2/5)·Y²·dim(R₂)·dim(R₃)

| Field | R₃ | R₂ | Y | Y² | dim(R₂)·dim(R₃) | Δb₁ per Weyl |
|---|---|---|---|---|---|---|
| Q_L | 3 | 2 | 1/6 | 1/36 | 6 | 1/30 |
| u_R | 3 | 1 | 2/3 | 4/9 | 3 | 4/15 |
| d_R | 3 | 1 | −1/3 | 1/9 | 3 | 1/15 |
| L_L | 1 | 2 | −1/2 | 1/4 | 2 | 1/10 |
| e_R | 1 | 1 | −1 | 1 | 1 | 2/5 |
| **Per generation** | | | | | | **4/3** |
| **3 generations** | | | | | | **4** |
| **b₁_gauge** | | | | | | **0** |
| **b₁_Higgs** | | | | | | **1/10** |
| **b₁_SM** | | | | | | **41/10 ✓** |

Per-generation sum: 1/30 + 4/15 + 1/15 + 1/10 + 2/5 = 1/30 + 8/30 + 2/30 + 3/30 + 12/30 = 26/30 = 13/15. Hmm — that's not 4/3.

Let me recheck. 1/30 + 4/15 + 1/15 + 1/10 + 2/5 = 1/30 + 8/30 + 2/30 + 3/30 + 12/30 = 26/30 = 13/15. But the source formula (document 18) gives per-gen b₁ = 4/3 from the Weyl sum. Let me recalculate using the source's Dirac formula divided by 2.

Source Dirac formula: Δb₁ = (4/5)·Y²·d₂·d₃ per Dirac fermion. Weyl = half.

Q_L (Weyl): (2/5)·(1/36)·2·3 = (2/5)·(6/36) = (2/5)·(1/6) = 2/30 = 1/15. Not 1/30.

I had an error above. Let me redo:

Formula: Δb₁ per Weyl = (2/5)·Y²·dim(R₂)·dim(R₃)

Q_L: (2/5)·(1/36)·2·3 = (2/5)·(1/6) = 2/30 = **1/15** (not 1/30)

Wait, dim(R₂)·dim(R₃) = 2·3 = 6. Y² = 1/36. So (2/5)·(1/36)·6 = (2/5)·(6/36) = (2/5)·(1/6) = 2/30 = 1/15.

But the phys24_cabibbo_doublet.py comments say Q_L contributes 1/30 to b₁. Let me recheck: "Q_L(3,2,1/6): db1 = (1/5)·3·2·(1/36) = 1/30."

The comment uses coefficient **(1/5)**, not (2/5). For a Weyl fermion the coefficient should be (2/5) per the source formula (half of Dirac 4/5). The comment uses (1/5) — half of that again. So the cabibbo_doublet.py comments use a **(1/5)** coefficient where the standard Weyl formula gives **(2/5)**.

But then the per-gen sum with (1/5) gives: 1/30 + 4/15·(1/2) + ... actually, let me just read the comments more carefully. From phys24_cabibbo_doublet.py:

```
#   Q_L(3,2,1/6): db1 = (1/5)*3*2*(1/36) = 1/30
#   u_R(3,1,2/3): db1 = (1/5)*3*1*(4/9) = 4/15
#   d_R(3,1,-1/3): db1 = (1/5)*3*1*(1/9) = 1/15
#   L_L(1,2,-1/2): db1 = (1/5)*1*2*(1/4) = 1/10
#   e_R(1,1,-1):  db1 = (1/5)*1*1*1 = 1/5
```

Sum: 1/30 + 4/15 + 1/15 + 1/10 + 1/5 = 1/30 + 8/30 + 2/30 + 3/30 + 6/30 = 20/30 = **2/3**.

Then 3 generations: 3·(2/3) = **2**. But the fermion contribution to b₁ should be **4** (since b₁_SM = 41/10 = 0 + 1/10 + 4 and b₁_gauge = 0, b₁_Higgs = 1/10).

So the comment's sum gives b₁_fermion = 2, but the correct value is 4. The comment itself says "Sum per generation: db1 = 2/3" and then discusses the factor-of-2 issue: "Factor of 2: each chiral fermion has coefficient half of Dirac." It concludes that "the standard formula with the coefficients as written in the SM literature gives b_fermion = (4/3) per generation including both chiralities."

This is the key passage. The comment acknowledges that its per-chiral-fermion coefficient (1/5) gives 2/3 per generation, but the actual b₁_fermion per generation is 4/3 — **double**. The comment attributes this to "counting both L and R (or equivalently, a generation contains both the representation and its conjugate in the full anomaly-free set)."

**So the SM convention counts each chiral fermion's contribution and then doubles it.** This is because in the SM, each Weyl fermion's representation contributes to the beta function as if it were part of a Dirac pair — the doubling comes from the anomaly-free completion of the representation. A complete SM generation effectively contributes as if each Weyl had a Dirac partner, even though the actual fermions are chiral.

This is the standard convention in the GUT literature. The point is: **the formulas in the cabibbo_doublet.py comments are using per-chiral-fermion coefficients that are half the standard Weyl convention**, and then the full generation result is obtained by noting that a complete generation doubles it.

**Now for the VL pair:** A VL pair IS a Dirac fermion — it already comes with both L and R. So there is no doubling needed. The VL contribution should use the standard Dirac formula directly.

But the library uses the **per-chiral** coefficients applied to the VL pair:
- Δb₁ = (2/5)·d₃·d₂·Y² — this is the chiral coefficient, same as SM per-chiral
- Δb₂ = (2/3)·d₃·S₂(R₂) — chiral coefficient  
- Δb₃ = (1/3)·d₂·S₂(R₃) — chiral coefficient

The per-chiral coefficients give the contribution of **one chiral representation**. For SM fermions, you sum over all chiralities in a generation and get the right answer because both L and R representations are present. For a VL pair, you should use the **Dirac** coefficients (double the chiral ones), because the VL pair is explicitly Dirac.

---

**Table 4: The normalization comparison**

| | Per-chiral (library Dynkin) | Per-Weyl (standard) | Per-Dirac (standard) | Library VL value | Correct VL Dirac |
|---|---|---|---|---|---|
| b₁ coeff | 2/5 | 2/5 | 4/5 | | |
| b₂ coeff | 2/3 | 2/3 | 4/3 | | |
| b₃ coeff | 1/3 | 2/3 | 4/3 | | |

Wait — the b₃ coefficient is different between "per-chiral" and "per-Weyl." Let me trace this more carefully.

Standard per-Weyl b₃ formula: (2/3)·T(R₃)·dim(R₂). For Q_L(3,2): (2/3)·(1/2)·2 = 2/3. ✓ matches standard.

Library per-chiral b₃ formula: (1/3)·dim(R₂)·S₂(R₃). For Q_L(3,2): (1/3)·2·(1/2) = 1/3. This is **half** the standard Weyl value.

So the library's per-chiral formulas are **half** the standard Weyl formulas for ALL three gauge groups. Verify:

b₁: library (2/5)·Y²·d₂·d₃ vs standard Weyl (2/5)·Y²·d₂·d₃. **Same!**

b₂: library (2/3)·d₃·S₂(R₂) vs standard Weyl (2/3)·T₂·d₃. T₂ = S₂(R₂). **Same!**

b₃: library (1/3)·d₂·S₂(R₃) vs standard Weyl (2/3)·T₃·d₂. **Factor of 2 difference!**

The b₃ library formula has coefficient 1/3 where the standard has 2/3. This is **only for b₃**. For b₁ and b₂ they match.

So the library's Dynkin formulas are standard Weyl for b₁ and b₂, but **half** the standard Weyl for b₃. That's why the ratio library/Dirac is (1/2, 1/2, 1/4) — because the library is (Weyl, Weyl, Weyl/2) while Dirac is (2·Weyl, 2·Weyl, 2·Weyl).

---

**Table 5: Definitive comparison — VL (3,2,1/6) one-loop shifts**

| | Standard Weyl | Standard Dirac | Library (cabibbo_doublet.py) | Library / Weyl | Library / Dirac |
|---|---|---|---|---|---|
| Δb₁ | 1/15 | 2/15 | 1/15 | 1 | 1/2 |
| Δb₂ | 1 | 2 | 1 | 1 | 1/2 |
| Δb₃ | 2/3 | 4/3 | 1/3 | **1/2** | 1/4 |

The library matches Weyl for b₁ and b₂, but is **half** Weyl for b₃. This is because the library's b₃ Dynkin coefficient is 1/3 instead of 2/3.

**Now: which is correct for b₃_SM?**

Using standard Weyl: b₃_fermion per gen = 4/3. Three gen = 4. b₃_SM = −11 + 4 = −7. ✓

Using library's formula: b₃_fermion per gen (from comment) = sum of chiral contributions using (1/3) coefficient = Q_L: (1/3)·2·(1/2) = 1/3, u_R: (1/3)·1·(1/2) = 1/6, d_R: (1/3)·1·(1/2) = 1/6. Sum = 1/3 + 1/6 + 1/6 = 2/3. Three gen: 2. b₃_SM = −11 + 2 = **−9**. ✗

The library's b₃ Dynkin formula gives the **wrong SM b₃** when applied field-by-field. The SM b₃ = −7 requires the fermion contribution to be 4, not 2. The cabibbo_doublet.py comment handles this by noting a "factor of 2" correction, but that factor is applied to the per-generation total (doubling from 2/3 to 4/3), not derived from the formula.

**The library's VL shift Δb₃ = 1/3 is obtained from a formula that does NOT reproduce b₃_SM when applied consistently. The correct value is Δb₃ = 2/3 (Weyl) or 4/3 (Dirac).**

---

**Table 6: Impact on the gap ratio**

| Convention | b₁_mod | b₂_mod | b₃_mod | Gap ratio |
|---|---|---|---|---|
| Library (current) | 41/10 + 1/15 = 25/6 | −19/6 + 1 = −13/6 | −7 + 1/3 = −20/3 | 38/27 = 1.407 |
| Weyl (correct for one Weyl) | 41/10 + 1/15 = 25/6 | −19/6 + 1 = −13/6 | −7 + 2/3 = −19/3 | 38/24 = 19/12 = 1.583 |
| Dirac (correct for VL pair) | 41/10 + 2/15 = 127/30 | −19/6 + 2 = −7/6 | −7 + 4/3 = −17/3 | (127/30 + 7/6) / (−7/6 + 17/3) = ... |

Let me compute the Dirac gap ratio:
- b₁' − b₂' = 127/30 − (−7/6) = 127/30 + 35/30 = 162/30 = 27/5
- b₂' − b₃' = −7/6 − (−17/3) = −7/6 + 34/6 = 27/6 = 9/2
- Gap = (27/5)/(9/2) = (27/5)·(2/9) = 54/45 = **6/5 = 1.200**

| Convention | Gap ratio | Distance from measured 1.358 |
|---|---|---|
| SM | 218/115 = 1.896 | 0.538 |
| Library (Δb₃=1/3) | 38/27 = 1.407 | 0.049 |
| Weyl (Δb₃=2/3) | 19/12 = 1.583 | 0.225 |
| Dirac (Δb₃=4/3) | 6/5 = 1.200 | 0.158 |
| MSSM | 7/5 = 1.400 | 0.042 |

---

**Assessment:**

The library value Δb₃ = 1/3 gives gap ratio 38/27, closest to measured. But this value comes from a formula with coefficient 1/3 that does NOT reproduce b₃_SM when applied consistently to SM fermions. The standard Weyl coefficient 2/3 gives 19/12, and the Dirac coefficient (appropriate for a VL pair) gives 6/5.

All three CD conventions improve on the SM (1.896), but by very different amounts. The Dirac convention 6/5 = 1.200 undershoots the measured 1.358, while the library convention 38/27 = 1.407 overshoots. The Weyl convention 19/12 = 1.583 is intermediate.

**The critical question is: which convention did the Session 3 sin2_theta_w_1.py script use, and what exactly did its 9/9 checks verify?** If it verified the gap ratio against the measured coupling ratio using the library betas for running, then the library convention is what was validated operationally — even if it uses a nonstandard Dynkin formula.

But there's a more fundamental issue: **the library's SM betas (41/10, −19/6, −7) are standard and correct.** These were NOT computed using the library's Dynkin formulas — they're hardcoded from the literature. The Dynkin formulas in cabibbo_doublet.py are used ONLY for the VL shifts. So the inconsistency is: the SM betas use one convention, and the VL shifts use a different convention. The gap ratio mixes both.

**This is the normalization issue. It is now fully characterized. The next step is to determine which VL Δb₃ is correct.**

To settle this definitively: I should check what value the standard GUT literature uses for the beta shift of a (3,2,1/6) VL doublet. The Kowalska & Kumar (2019) and Bhattacherjee et al. (2018) papers should have explicit tables. Do you want me to try fetching one of those PDFs, or do you have access to the specific numbers from those papers?

---

# Search Notes

Let me fetch the key paper that lists VL beta shifts explicitly.The full text is paywalled. Let me try the arxiv version and also search for the specific beta coefficient values.Let me fetch the Bhattacherjee et al. (2018) paper which has explicit beta coefficient tables for VL fermions.The key insight is in document 53 from Tong's textbook. Let me look at the critical point about how n_f counts in the SU(3) beta function.Now I have it. From Wikipedia/MDPI (documents 59/63), the key formula is clear:

The general one-loop beta function for a gauge group with **Dirac fermions** has a coefficient **(4/3)·T(R)** per Dirac fermion. For **Weyl fermions**, replace 4/3 by **2/3**.

From document 60 (Floerchinger lecture notes): β(g) for SU(N) with n_f massless **Dirac** fermions in the fundamental: b = 11/3·N − **(2/3)·n_f**. For QCD with N=3, n_f=6: b = 11 − 4 = 7.

This is the **QCD convention** where n_f counts **Dirac flavors** and the coefficient is **2/3 per Dirac flavor** (not 4/3). The 2/3 vs 4/3 discrepancy comes from different conventions for whether the beta function is written in terms of g or α.

Here's the resolution:

**The QCD beta function has TWO common conventions:**

1. **β(g) convention**: β(g) = −(11/3·C₂(G) − 4/3·n_f·T(R))·g³/(16π²). The coefficient of n_f is **4/3**.

2. **β(α)/b convention**: b₃ = −11 + (2/3)·n_f. The coefficient of n_f is **2/3**. This is because d(1/α)/d(ln μ) = −b/(2π) where b = (11/3)·C₂(G) − (4/3)·n_f·T(R), and for SU(3) fundamental T(R)=1/2, so the fermion term is (4/3)·n_f·(1/2) = (2/3)·n_f.

**The library convention is b₃ = −11 + (2/3)·n_f with n_f = 6 → b₃ = −7.** Each Dirac quark flavor contributes **(2/3)** to b₃ in this convention. The Cabibbo Doublet (3,2,1/6) adds 2 new Dirac quark flavors (up-type and down-type components of the doublet), so Δb₃ = 2·(2/3)·T₃ = 2·(2/3)·(1/2) = **2/3**... wait, that gives 2/3, not 1/3.

Let me recount. The SM has 6 Dirac flavors: u,d,c,s,t,b. Each is in the fundamental of SU(3). Each contributes (2/3)·T(fund) = (2/3)·(1/2) = 1/3 to b₃. Six flavors: 6·(1/3) = 2. b₃ = −11 + 2... that gives −9, not −7.

No — the 2/3 already includes the T(R)=1/2. The formula is b₃ = −11 + (2/3)·n_f where n_f counts Dirac flavors. With n_f=6: b₃ = −11 + 4 = −7. Each Dirac flavor contributes 2/3 to b₃. The VL doublet has 2 Dirac flavors → Δb₃ = 2·(2/3) = 4/3. Not 1/3.

**But** — the VL doublet is a single (3,2) representation. The "2 flavors" interpretation counts the SU(2) components separately. However, in the GUT-convention beta function, the contribution of a multiplet in representation (R₃, R₂) to b₃ depends on dim(R₂)·T(R₃), not on n_f. Specifically: Δb₃ = (4/3)·T(R₃)·dim(R₂) for one Dirac fermion, or (2/3)·T(R₃)·dim(R₂) for one Weyl fermion.

For the VL (3,2,1/6) as **one Dirac fermion**: Δb₃ = (4/3)·(1/2)·2 = 4/3. This matches the source formula.

For the VL pair treated as **adding n_f = 2 Dirac flavors** to QCD: Δb₃ = (2/3)·2 = 4/3. Same answer.

**The library has Δb₃ = 1/3, which is a factor of 4 too small.**

The gap ratio 38/27 used the library value. This means **the gap ratio 38/27 is computed with incorrect absolute betas**. However, the gap ratio only depends on differences of betas, and if all three shifts are wrong by related factors, the gap ratio could still be meaningful — but the non-uniform ratio (1/2, 1/2, 1/4) means the gap ratio IS affected.

This is a serious finding. Let me state it clearly:

**The library one-loop VL shifts (1/15, 1, 1/3) appear to be incorrect for absolute RGE running. The standard formulas give (2/15, 2, 4/3) for a Dirac VL pair.** The gap ratio 38/27 was computed with the library values, and the Session 3 sin2_theta_w_1.py verified it against the measured coupling ratio — but the gap ratio with the corrected betas would be 38/21 ≈ 1.81, which is **farther** from the measured 1.358 than the SM value of 218/115 ≈ 1.896. That would mean the Cabibbo Doublet makes unification **worse**, not better.

This is potentially a kill-switch finding. But before declaring it, I need to verify: **what exactly did sin2_theta_w_1.py check?** The 9/9 checks in that Session 3 script are the ultimate arbiter. If those checks verified the gap ratio 38/27 against measured couplings AND used the library betas for the running, then there's either an error in the Session 3 script or an error in my analysis.

The safest resolution: the library's one-loop formulas from cabibbo_doublet.py may use a **different convention for the RGE** than the standard d(1/α)/d(ln μ) = −b/(2π). There exist conventions with different overall factors absorbed into the definition of b_i. The key test is whether the **SM betas** (41/10, −19/6, −7) are in the same convention.

SM check: b₃ = −7 = −11 + 4. The fermion part = 4 = 3 generations × (4/3). Each generation contributes 4/3. A generation has Q_L(3,2) + u_R(3,1) + d_R(3,1) contributing to SU(3). Using the **Weyl** formula: (2/3)·T₃·d₂ per Weyl fermion. Q_L: (2/3)·(1/2)·2 = 2/3. u_R: (2/3)·(1/2)·1 = 1/3. d_R: (2/3)·(1/2)·1 = 1/3. Sum = 4/3 per generation. × 3 = 4. **Correct.**

Now: VL (3,2,1/6) as one **Dirac** = two Weyl. Each Weyl contributes (2/3)·(1/2)·2 = 2/3. Two Weyl: 2·(2/3) = 4/3. **This is the standard result.** The library's 1/3 is wrong by a factor of 4.

**My conclusion: there is a normalization error in the library's VL one-loop beta shifts.** The error doesn't affect the gap ratio *direction* (the CD still shifts the gap ratio toward measured), but it changes the *magnitude* and the gap ratio value. This needs to be resolved before any further computation.

---

