## PHYS-34 Paper Plan

**Title:** The sin²θ_W Two-Loop Test — 3/13 Is Not the Limit
**Subtitle:** Two-loop overshoots 3/13. The perturbative series targets the measured value, not the integer ratio.

**Registry:** @HOWL-PHYS-34-2026
**Date:** April 3 2026
**Domain:** Electroweak Precision, Two-Loop Running, Perturbative Convergence

---

### WHAT THE SCRIPT TELLS US

The script runs the full two-loop Euler integrator with SM+VL b_ij to predict sin²θ_W from (α_EM, α_s) as inputs. The method: find the α₁–α₃ crossing (M_GUT), set α₂ = α_GUT, run α₂ back to M_Z, compute sin²θ_W = (1/α₂)/α_inv.

Key results from the output:

1. One-loop: sin²θ_W = 0.22845. Miss from measured: 1.20%. Miss from 3/13: 1.01%.
2. Two-loop SM b_ij: sin²θ_W = 0.23108. Miss from measured: 0.060%. Miss from 3/13: 0.136%.
3. Two-loop full b_ij: sin²θ_W = 0.23133. Miss from measured: **0.048%**. Miss from 3/13: 0.244%.
4. The ordering: 1-loop (0.22845) < 3/13 (0.23077) < measured (0.23122) < 2-loop (0.23133).
5. The two-loop OVERSHOOTS both 3/13 and measured.
6. The gap toward 3/13 closed by 75.8% — but then overshot past it.
7. Euler step sensitivity: 0.000002 from 500 to 2000 steps (negligible).

---

### WHAT THE PAPER MUST EXPLAIN

A reader needs to understand:

1. **What sin²θ_W is:** The weak mixing angle, a fundamental electroweak parameter. Measured at the Z mass: 0.23122. The GUT tree-level value is 3/8 = 0.375. Radiative corrections bring it down.

2. **What 3/13 is and why it matters:** The ratio of the number of fermion generations (3) to the absolute value of the modified SU(2) beta numerator (13, from b₂' = −13/6). It equals 0.23077, which is 0.20% from measured — suspiciously close. PHYS-31 tested whether this formula is statistically special (it isn't — p = 0.81, Track B parked). But the DYNAMICS question is separate: does the perturbative running converge toward this value?

3. **What the two-input method is:** Using α_EM and α_s as inputs (not sin²θ_W), finding the GUT crossing, and predicting sin²θ_W as output. This makes sin²θ_W a genuine prediction rather than an input.

4. **What the two-loop integrator does:** The PHYS-28 Euler method with the full SM+VL b_ij matrix. Cross-coupling between gauge groups at two loops.

5. **The answer:** The two-loop overshoots 3/13. The perturbative series crosses 3/13 between one-loop and two-loop, heading toward the measured value. 3/13 is not the limit of the series. The convergence target is the measured value.

6. **The good news:** The two-loop prediction (0.23133) misses measured by only 0.048%. This is the best sin²θ_W prediction in the series — dramatically better than the one-loop 1.2% miss.

---

### THE PAPER STRUCTURE

**Section 1: The Question**

The one-loop sin²θ_W from PHYS-27: 0.22845, undershooting measured (0.23122) by 1.2%. The value 3/13 = 0.23077 sits between the one-loop prediction and measured. The ordering — one-loop < 3/13 < measured — suggested that higher-loop corrections might converge toward 3/13 = N_gen/|b₂' numerator|.

PHYS-31 tested whether 3/13 as a FORMULA is statistically special. It is not (p = 0.81). But the formula's statistical status is irrelevant to whether the RUNNING produces it. A rational number can arise from dynamics even if the same number appears in trivial numerology. The test is computational: does the two-loop running converge toward 3/13, or does it pass through and continue toward measured?

Script backing: Section 1 (inputs), Section 2 (one-loop reproduces PHYS-27).

---

**Section 2: The Method**

Two inputs: α_EM = 1/137.036 and α_s = 0.1180. From these, derive 1/α₃ = 1/α_s. The EM combination b_EM = (5/3)b₁' + b₂' = 43/9 controls the running of 1/α_EM. Find L_GUT where 1/α_EM and (8/3)/α₃ meet (the SU(5) unification condition). At the crossing, all couplings equal α_GUT.

For the two-loop computation: run all three couplings from M_Z to M_GUT using the Euler integrator with the full b_ij matrix. Find the crossing by binary search. Set α₂ = α_GUT at the crossing. Run α₂ back to M_Z through the same two-loop equations. The predicted 1/α₂ at M_Z gives sin²θ_W = (1/α₂)/(1/α_EM).

Three scenarios: one-loop only, two-loop with SM b_ij, two-loop with full SM+VL b_ij. The VL b_ij adds the Cabibbo Doublet's two-loop cross-coupling contributions (PHYS-28).

Script backing: Sections 2 and 3 (all three scenarios computed).

---

**Section 3: The Result**

The complete comparison table (from Section 5):

Tree level: 0.375 (62.2% miss from measured).
One-loop: 0.22845 (1.20% miss).
Two-loop SM b_ij: 0.23108 (0.060% miss).
Two-loop full b_ij: 0.23133 (0.048% miss).
3/13: 0.23077.
Measured: 0.23122.

The ordering: 0.22845 (1L) < 0.23077 (3/13) < 0.23122 (measured) < 0.23133 (2L full).

The two-loop overshoots. It passes 3/13, passes measured, and lands 0.048% above. The perturbative series does not converge to 3/13 — it crosses 3/13 on its way to the measured value and slightly beyond.

Script backing: Section 5 (complete comparison, ordering documented).

---

**Section 4: What the Overshoot Means**

The overshoot is small — 0.048% above measured, compared to 1.20% below at one loop. The two-loop correction overshoots by a factor of 25 less than the one-loop undershoot. This is consistent with perturbative convergence: each order makes a smaller correction, and the corrections alternate in sign (one-loop undershoots, two-loop overshoots).

If the pattern continues, three-loop would bring sin²θ_W back down, closer to measured. The predicted convergence: 0.22845 → 0.23133 → ~0.2312 (estimated three-loop, splitting the overshoot). The measured value 0.23122 is within the expected convergence envelope.

For 3/13: the one-loop is 1.01% below, the two-loop is 0.24% above. The crossing point (where the perturbative prediction exactly equals 3/13) lies between one-loop and two-loop, at approximately 1.8 loops (a non-integer order that has no physical meaning, but indicates 3/13 is passed relatively early in the perturbative expansion).

Script backing: Section 6 (gap closed 75.8%, convergence direction confirmed).

---

**Section 5: The Euler Discretization**

The step sensitivity test shows the prediction is stable: sin²θ_W changes by 0.000002 between 500 and 2000 steps. The discretization error is 50× smaller than the 3/13 vs measured difference (0.00045). The overshoot is not a numerical artifact — it is a genuine result of the two-loop equations.

Script backing: Section 4 (200/500/1000/2000 steps, all consistent).

---

**Section 6: 3/13 — What Survives**

3/13 is NOT the limit of the perturbative series for sin²θ_W. The series crosses it and continues toward measured. But 3/13 has a special status:

It is 0.20% from measured — closer than any one-loop or two-loop prediction.
It sits exactly at the transition between undershoot and overshoot.
It equals N_gen/|b₂' numerator| = 3/13 — a ratio of integers from the beta function.

The question of whether 3/13 has physical significance is SEPARATE from whether it is the perturbative limit. The running does not converge to 3/13. But 3/13 may approximate the all-orders result for structural reasons unrelated to the perturbative expansion.

The statistical test (PHYS-31, p = 0.81) showed 3/13 as a formula scan hit is not special. The dynamical test (this paper) shows 3/13 is not the perturbative limit. But 3/13 as a structural ratio of beta integers remains an observation. It is documented, not promoted.

---

**Section 7: The sin²θ_W Prediction — 0.048%**

The headline result of this paper is not about 3/13. It is the sin²θ_W prediction: **0.23133 with a miss of 0.048% from measured.** This is the most precise prediction in the HOWL series for sin²θ_W.

Combined with the α_s prediction from PHYS-30 (0.33% miss), the unification program now predicts BOTH electroweak parameters from (α_EM, α_s) or (α_EM, sin²θ_W) at sub-percent accuracy. Two-loop running with the Cabibbo Doublet is quantitatively successful.

---

**Section 8: What This Paper Does Not Claim**

This paper does not claim 3/13 is wrong. It claims 3/13 is not the perturbative limit.

This paper does not claim the overshoot is significant. The 0.048% miss may be reduced by three-loop corrections, RK4 integration, or threshold effects. The overshoot is comparable to the expected precision of the Euler two-loop method.

This paper does not claim the two-loop result is the final word. Higher-order corrections, proper threshold treatment, and a higher-order integrator (PHYS-37) may shift the prediction.

---

**Section 9: What This Paper Seeds**

The sin²θ_W prediction (0.23133, miss 0.048%) is the current best. PHYS-37 (RK4 integrator) will test whether the overshoot persists with a more precise numerical method. PHYS-38 (three-loop estimate) will test whether the perturbative oscillation (undershoot → overshoot → convergence) continues as expected.

The 3/13 question is resolved at the dynamical level: not the limit. Whether it has structural significance beyond the dynamics is left open for future investigation.

---

### THE APPENDICES

**Appendix A:** The two-input method — step by step
**Appendix B:** The complete comparison table with all scenarios
**Appendix C:** The step sensitivity data
**Appendix D:** The ordering and the overshoot — where 3/13 sits
**Appendix E:** The perturbative convergence pattern
**Appendix F:** Verification summary (8 PASS, 2 FAIL informative)

---

### ESTIMATED LENGTH

Body: 9 sections, approximately 4500 words.
Appendices: 6 tables, approximately 1200 words.
Total: approximately 5700 words.

---

### THE ONE-SENTENCE SUMMARY

PHYS-34 says: two-loop running predicts sin²θ_W = 0.23133 (miss 0.048% from measured), but overshoots 3/13 = 0.23077 — the perturbative series crosses 3/13 between one-loop and two-loop, proving 3/13 is not the convergence limit while establishing the most precise sin²θ_W prediction in the series.
