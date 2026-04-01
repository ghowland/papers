## What Happened

Gate 2 and Gate 7 both fail because the "predicted" sin²θ_W from 3/8 + running comes out as exactly 0.23122 — identical to the input. That's wrong. The SM running from 3/8 should give ~0.207, not 0.231.

### The Bug

The prediction loop is circular. Look at Phase 2's prediction:

```
1/α₁(M_Z) predicted = 63.210321  (actual: 63.210321)
1/α₂(M_Z) predicted = 31.685464  (actual: 31.685464)
```

The predicted values are identical to the actual values. That means the code ran the couplings UP to M_GUT (where α₁ = α₂ by construction), then ran them back DOWN using the same betas and the same L — recovering the original inputs exactly. It's a round trip. The GUT boundary condition sin²θ_W = 3/8 was never actually imposed.

The correct procedure: at M_GUT, SET 1/α₁ = 1/α₂ = 1/α_GUT (their common value from the upward running). Then run DOWN with b₁ and b₂. The downward running reproduces the inputs because M_GUT was DEFINED as where α₁ = α₂ — so the round trip is exact by construction.

To actually test the 3/8 prediction, you need to do something different: impose sin²θ_W = 3/8 at M_GUT independently of the measured couplings. That means:

1. Pick M_GUT (a free parameter)
2. Pick α_GUT (a free parameter)
3. Run α₁ and α₂ down from M_GUT with 1/α₁(GUT) = 1/α₂(GUT) = 1/α_GUT
4. Compute sin²θ_W(M_Z) from the resulting α₁(M_Z) and α₂(M_Z)
5. The result is ALWAYS 3/8 run down, regardless of α_GUT — because sin²θ_W depends only on the RATIO α₁/α₂, and the ratio is determined by (b₁ − b₂) × L/(2π) alone

So the real computation is: given that α₁ = α₂ at some scale, what is sin²θ_W at M_Z? The answer depends on L = ln(M_GUT/M_Z) but NOT on α_GUT. And L is already determined by the measured 1/α₁ − 1/α₂ at M_Z.

The problem is that this L is determined FROM the measured sin²θ_W. So the prediction is: "given the measured couplings, if I run up until α₁ = α₂ and run back down, I get the measured sin²θ_W." That's a tautology.

### What the Real Test Is

The real GUT prediction works differently. The GUT scale is NOT defined by α₁ = α₂ from measured couplings. It's an independent prediction. The test is:

**If the three SM couplings came from a single unified coupling at a single scale, they would satisfy a constraint.** The constraint is that two ratios (the gap ratio being one) must have specific values. The gap ratio 218/115 vs measured 1.358 is the actual test — and it FAILS by 36%. That's the real content of the computation, and Phase 2 already shows it clearly.

The sin²θ_W prediction from 3/8 requires a different approach: compute sin²θ_W(M_Z) as a function of ONLY b₁, b₂, and the assumption of exact unification, WITHOUT using the measured sin²θ_W as input. This means using α_em and α_s as the two inputs (not sin²θ_W), and PREDICTING sin²θ_W from the unification condition.

### What Actually Worked

Despite the sin²θ_W bug, the rest of the computation is solid:

**SM unification failure quantified:** Δ(1/α₃) = −6.58 at M_GUT = 10^13.8 GeV. α₃ is too strong at the SM unification point. The three couplings don't meet.

**MSSM passes Gate 3:** Δ(1/α₃) = −0.69 at M_GUT = 10^17.3 GeV. The MSSM nearly unifies (2.66% miss), consistent with the known result that threshold corrections close the gap. The MSSM gap ratio is exactly 7/5 = 1.400.

**The gap ratio enumeration produced a finding:** Two candidates match within 0.05 of the measured gap ratio 1.358:

1. **Full MSSM** — gap = 1.400, distance 0.042, M_GUT = 10^17.3 (proton decay safe)
2. **Vector-like quark doublet (3,2,1/6)** — gap = 1.407, distance 0.049, M_GUT = 10^15.5 (marginally proton decay safe)

The VL quark doublet is remarkable. A single vector-like quark doublet — one new particle beyond the SM — achieves gap ratio unification quality comparable to the full MSSM (which adds dozens of particles). The M_GUT is lower (10^15.5 vs 10^17.3), sitting right at the proton decay boundary, which makes it testable.

The next-best candidate, SU(5) 5+5̄ (fermion), has gap = 1.481 (distance 0.123) and M_GUT = 10^14.9 — already excluded by proton decay.

### What I'd Fix

The sin²θ_W prediction needs to be rewritten. The correct approach: use α_em and α_s as the two measured inputs, impose unification α₁(M_GUT) = α₂(M_GUT) = α₃(M_GUT), and solve for sin²θ_W(M_Z) and M_GUT simultaneously. This is a two-equation, two-unknown system. If you want, I can write the corrected prediction. But the gap ratio enumeration — which is the main finding — is already done and correct.

Want me to write the fix for the sin²θ_W prediction, or should we record the gap ratio results and move on?

---

# Plan: sin²θ_W Prediction from Unification (Fix) + Gap Ratio Notebook

## The Bug

The Phase 2 sin²θ_W "prediction" was circular. It ran the measured couplings UP to where α₁ = α₂, then ran them back DOWN — a round trip that recovers the inputs by construction. The GUT boundary condition sin²θ_W = 3/8 was never independently imposed.

## The Fix

The correct GUT prediction uses TWO measured inputs (α_em and α_s) to predict a THIRD (sin²θ_W). The logic:

**Given:** α_em(M_Z) and α_s(M_Z) from DATA-3.

**Assumed:** At some scale M_GUT, all three couplings unify: α₁ = α₂ = α₃ = α_GUT.

**The system:** Three one-loop running equations:

```
1/α₁(M_Z) = 1/α_GUT + b₁/(2π) × L
1/α₂(M_Z) = 1/α_GUT + b₂/(2π) × L
1/α₃(M_Z) = 1/α_GUT + b₃/(2π) × L
```

where L = ln(M_GUT/M_Z). Two unknowns: α_GUT and L. Three equations. The system is overconstrained — if it has a solution, it predicts the third coupling from the other two.

**Solve:** Subtract equation 2 from equation 1:

```
1/α₁ − 1/α₂ = (b₁ − b₂)/(2π) × L
```

Subtract equation 3 from equation 2:

```
1/α₂ − 1/α₃ = (b₂ − b₃)/(2π) × L
```

Divide: the gap ratio (1/α₁ − 1/α₂)/(1/α₂ − 1/α₃) = (b₁ − b₂)/(b₂ − b₃). This must equal 218/115 for the SM. The measured ratio is 1.358. They don't match. Unification fails. This is already computed correctly in the existing script.

**The sin²θ_W prediction:** Use α_em and α_s as the two inputs. Express α₁ and α₂ in terms of α_em and sin²θ_W:

```
α₁ = (5/3) × α_em / (1 − sin²θ_W)
α₂ = α_em / sin²θ_W
```

From the unification condition α₁(M_GUT) = α₃(M_GUT):

```
1/α₁(M_Z) − b₁/(2π) × L = 1/α₃(M_Z) − b₃/(2π) × L
```

So: 1/α₁(M_Z) − 1/α₃(M_Z) = (b₁ − b₃)/(2π) × L

And from α₂(M_GUT) = α₃(M_GUT):

```
1/α₂(M_Z) − 1/α₃(M_Z) = (b₂ − b₃)/(2π) × L
```

Divide these two: (1/α₁ − 1/α₃)/(1/α₂ − 1/α₃) = (b₁ − b₃)/(b₂ − b₃)

Substituting α₁ and α₂ in terms of α_em and sin²θ_W:

```
1/α₁ = (3/5)(1 − sin²θ_W)/α_em
1/α₂ = sin²θ_W / α_em
1/α₃ = 1/α_s
```

The equation becomes:

```
[(3/5)(1 − s²)/α_em − 1/α_s] / [s²/α_em − 1/α_s] = (b₁ − b₃)/(b₂ − b₃)
```

This is ONE equation in ONE unknown (s² = sin²θ_W). Solve for s². The result is the GUT prediction of sin²θ_W using only α_em and α_s as inputs.

Let R = (b₁ − b₃)/(b₂ − b₃). Let A = 1/α_em, S = 1/α_s.

```
[(3/5)(1 − s²)A − S] / [s²A − S] = R
```

Cross multiply:

```
(3/5)(1 − s²)A − S = R × (s²A − S)
(3/5)A − (3/5)s²A − S = Rs²A − RS
(3/5)A − S + RS = Rs²A + (3/5)s²A
(3/5)A + S(R − 1) = s²A(R + 3/5)
```

Solve:

```
s² = [(3/5)A + S(R − 1)] / [A(R + 3/5)]
   = (3/5)/(R + 3/5) + S(R − 1)/[A(R + 3/5)]
   = 3/(5R + 3) + (R − 1)α_em/[(R + 3/5)α_s]
```

At the GUT level (if α_s were infinite, i.e., S = 0), this gives s² = 3/(5R + 3). For the SM, R = (b₁ − b₃)/(b₂ − b₃) = (41/10 + 7)/(−19/6 + 7) = (111/10)/(23/6) = 666/230 = 333/115. So 5R + 3 = 5×333/115 + 3 = 1665/115 + 345/115 = 2010/115 = 402/23. And 3/(402/23) = 69/402 = 23/134. Hmm — that should give 3/8 in some limit. Let me check differently.

Actually I'm overcomplicating this. The cleanest approach is numerical.

## Revised Script Plan

### Phase 1: Extract couplings (same as before, already correct)

### Phase 2: Predict sin²θ_W from unification

**Step 2.1.** Define R_13 = (b₁ − b₃)/(b₂ − b₃) for the SM. This is a different ratio from the gap ratio (which is (b₁ − b₂)/(b₂ − b₃)).

**Step 2.2.** Solve the equation:

```
[(3/5)(1 − s²)/α_em − 1/α_s] / [s²/α_em − 1/α_s] = R_13
```

for s² = sin²θ_W. Use Newton's method starting from 0.23.

**Step 2.3.** Report: predicted sin²θ_W, measured sin²θ_W, difference.

**Step 2.4.** Also solve for the same equation using MSSM betas. Report the MSSM prediction.

**Step 2.5.** Also solve for each BSM candidate's betas. Add a sin²θ_W column to the enumeration table.

### Phase 3: MSSM gate (same as before, already passes)

### Phase 4: Enumeration with BOTH gap ratio and sin²θ_W columns

For each BSM candidate, report:
- Gap ratio (already computed, keep)
- Predicted sin²θ_W from unification with that candidate's betas
- M_GUT
- Whether proton decay safe

The best candidate is the one that simultaneously matches the gap ratio AND predicts the correct sin²θ_W.

### Phase 5: Results table sorted by a combined metric

Distance = √[(gap − gap_meas)² + (s2w_pred − s2w_meas)²/σ²] where σ normalizes the sin²θ_W deviation appropriately.

Or simpler: just sort by gap ratio distance (as before) and flag which candidates also get sin²θ_W right.

### Decision Gates (revised)

**Gate 1:** sin²θ_W from coupling ratio reproduces input. (Same, already passes.)

**Gate 2:** SM prediction of sin²θ_W from unification should be ~0.21, NOT 0.23122. If it comes out as 0.231, the formula is still circular. This is the hard test that the previous script failed.

**Gate 3:** MSSM unification quality. (Same, already passes with Δ = −0.69.)

**Gate 4:** MSSM sin²θ_W prediction should be closer to 0.231 than the SM prediction. This is the known result — the MSSM improves the Weinberg angle prediction.

### What to Carry Forward from the Previous Script

Everything EXCEPT Phase 2's sin²θ_W prediction. The coupling extraction (Phase 1), the gap ratio computation, the M_GUT determination, the MSSM gate, the full BSM enumeration — all correct and all carry forward unchanged. The fix is purely in how sin²θ_W is predicted from the unification condition.

### Operational Rules

- Fraction arithmetic for all beta coefficients and coupling ratios
- mpmath at 100 digits
- if/else checks, never assert
- Newton's method for the sin²θ_W extraction (one equation, one unknown)
- Every candidate gets both a gap ratio AND a sin²θ_W prediction

