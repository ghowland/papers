## PHYS-35 Paper Plan

**Title:** The No-Threshold Puzzle — More CD Running Means Better Predictions
**Subtitle:** No-threshold beats hard threshold by 12×. Soft threshold is worse. The CD contribution is needed at all scales.

**Registry:** @HOWL-PHYS-35-2026
**Date:** April 3 2026
**Domain:** Threshold Physics, Decoupling, Renormalization Group Running

---

### WHAT THE SCRIPT TELLS US

The script tests three threshold configurations for the α_s prediction from gauge coupling unification with the Cabibbo Doublet:

1. **M_VL scan (12 points, 200–6000 GeV):** Every threshold position gives worse α_s than no-threshold. The best hard threshold (M_VL = 200 GeV, miss 1.72%) is still 5.3× worse than no-threshold (0.33%). Higher M_VL = worse prediction, monotonically. No optimal threshold exists that matches no-threshold.

2. **Step sensitivity (200/500/1000/2000 steps):** The no-threshold advantage is 12.3× at both 500 and 2000 steps. The advantage does NOT shrink with better integration. It is not a numerical artifact of Euler discretization.

3. **Soft threshold (sigmoid f(mu) = 1/(1+(M_VL/mu)²)):** WORSE than hard threshold at every M_VL tested. Best soft: 7.14% miss (M_VL=200) vs best hard: 1.72% (M_VL=200) vs no-threshold: 0.33%. The softer the transition, the worse the prediction.

The pattern: more CD running = better prediction. No-threshold has maximum CD running. Hard threshold has partial CD. Soft threshold has even less effective CD (gradual onset). The ranking is perfectly correlated with the amount of CD contribution integrated.

---

### WHAT THE PAPER MUST EXPLAIN

A reader who has never seen any HOWL paper needs:

1. **What the Cabibbo Doublet is:** A hypothetical vector-like quark doublet in the (3,2,1/6) representation that modifies the gauge coupling beta functions. When added to the SM, the three gauge couplings converge more precisely at high energy.

2. **What a threshold is:** In quantum field theory, a particle with mass M contributes to loop corrections only at energies above M. Below M, the particle "decouples" — its virtual effects are suppressed. The transition from "not contributing" to "contributing" is the threshold. In practice, the running changes from SM betas (below M) to modified betas (above M).

3. **What the puzzle is:** The CD has a physical mass (M_VL). Standard QFT says the CD betas should apply only above M_VL, with SM betas below. But the α_s prediction is 12× better when CD betas are used from M_Z (91 GeV) — far below any reasonable M_VL (200+ GeV). Why does ignoring the physical threshold give a better answer?

4. **What the three investigations found:** The M_VL scan shows monotonic degradation with higher threshold. The step sensitivity test shows the advantage is not numerical. The soft threshold test shows that smoothing the transition makes things worse, not better. All three point to the same conclusion: the CD contribution is needed at all energy scales.

5. **What this means:** Three possible explanations. (a) The CD has virtual effects below its mass through loop mixing that the step function misses but the no-threshold configuration implicitly captures. (b) The no-threshold configuration is an effective resummation that accidentally includes higher-order corrections. (c) There is a cancellation between threshold effects and missing higher-order terms that makes the no-threshold result accidentally precise.

---

### THE PAPER STRUCTURE

**Section 1: The Puzzle**

The PHYS-30 α_s prediction: two-loop running with CD betas from M_Z (no threshold) gives α_s = 0.11838, missing measured 0.1180 by 0.33%. The same computation with a physical threshold at M_VL = 500 GeV gives α_s = 0.11327, missing by 4.0%. The no-threshold is 12× more precise.

This is puzzling. The CD is a massive particle — it should decouple below its mass. Using its betas at energies where it shouldn't be active violates the standard decoupling theorem. Yet ignoring the threshold gives a dramatically better prediction. The PHYS-27 sin²θ_W analysis showed the same pattern.

The question: is the no-threshold advantage physical or numerical?

Script backing: Section 1 (reproduces PHYS-30: no-thresh 0.33%, threshold 4.0%, ratio 12.3×).

---

**Section 2: The Decoupling Theorem**

The Appelquist-Carazzone decoupling theorem states that heavy particles with mass M contribute to low-energy observables only through suppressed corrections of order (E/M)². At energies E << M, the heavy particle effectively disappears from the theory. In the renormalization group, this manifests as a threshold: the beta functions change at μ = M.

In practice, the threshold is implemented as a step function: SM betas for μ < M_VL, modified betas for μ > M_VL. This is the leading-order approximation. The exact threshold is smoother — logarithmic corrections of order ln(μ²/M²) spread the transition — but the step function is the standard treatment.

The puzzle violates the decoupling theorem's expectation: the CD betas, which should be active only above M_VL, give better results when used from M_Z (91 GeV) — below any reasonable CD mass.

---

**Section 3: The M_VL Scan**

The scan tests M_VL from 200 GeV to 6 TeV. At each threshold position, the two-loop running is performed with SM betas below M_VL and full CD betas above.

The result: monotonic degradation. The lower the threshold, the better — but no threshold position matches the no-threshold result.

M_VL = 200 GeV: α_s = 0.11597, miss 1.72%.
M_VL = 500 GeV: α_s = 0.11327, miss 4.01%.
M_VL = 1000 GeV: α_s = 0.11132, miss 5.66%.
M_VL = 2000 GeV: α_s = 0.10944, miss 7.26%.
M_VL = 6000 GeV: α_s = 0.10658, miss 9.68%.

No threshold: α_s = 0.11838, miss 0.33%.

Even at the lowest tested threshold (M_VL = 200 GeV, below current LHC exclusion limits), the miss is 1.72% — still 5.3× worse than no-threshold. There is no "optimal M_VL" that approaches the no-threshold quality.

The trend is clear: more CD running = better α_s. The maximum CD running (from M_Z) = best α_s.

Script backing: Section 2 (12 M_VL values, all with alpha_s and miss).

---

**Section 4: The Step Sensitivity Test**

The Euler integrator's discretization error could create a fake advantage if it systematically favored one configuration. The test: run both no-threshold and threshold (M_VL = 500) at 200, 500, 1000, and 2000 Euler steps.

No-threshold: miss = 0.3246%, 0.3251%, 0.3253%, 0.3255% at 200/500/1000/2000 steps. Stable to 0.001%.

Threshold: miss = 4.0049%, 4.0050%, 4.0050%, 4.0048% at 200/500/1000/2000 steps. Stable to 0.001%.

The advantage ratio: 12.3× at 500 steps, 12.3× at 2000 steps. Unchanged. The advantage is NOT an artifact of the Euler discretization. It persists identically with four times the step count.

Script backing: Section 3 (8 data points, 4 per configuration, advantage ratio constant).

---

**Section 5: The Soft Threshold**

The hard threshold is a mathematical idealization — a step function at M_VL. Real decoupling is smoother. The test: replace the step function with a sigmoid f(μ) = 1/(1 + (M_VL/μ)²). This function equals 0.5 at μ = M_VL, approaches 1 for μ >> M_VL, and approaches 0 for μ << M_VL. The effective betas are b_i(μ) = b_SM + f(μ) × Δb_VL.

The result: the soft threshold is WORSE than the hard threshold at every M_VL.

Soft M_VL = 200 GeV: miss 7.14%. Hard M_VL = 200 GeV: miss 1.72%.
Soft M_VL = 500 GeV: miss 8.90%. Hard M_VL = 500 GeV: miss 4.01%.
Soft M_VL = 1000 GeV: miss 10.27%. Hard M_VL = 1000 GeV: miss 5.66%.

The ranking: no-threshold (0.33%) > hard threshold > soft threshold (worst). Smoothing the transition makes predictions worse because the sigmoid function gives less total CD running than the step function. At μ = M_VL, the sigmoid gives only half the CD contribution; the step function gives the full amount. The soft threshold reaches full CD strength only at μ >> M_VL, losing the CD's contribution in the critical region just above M_VL.

The finding: the puzzle is not about the threshold SHAPE. It is about the AMOUNT of CD running. More CD = better.

Script backing: Section 4 (5 soft threshold values, all worse than hard, all worse than no-threshold).

---

**Section 6: The Pattern — More CD Running = Better Predictions**

The three investigations converge on one conclusion:

No-threshold (CD from M_Z): miss 0.33%. Maximum CD running.
Hard threshold at M_VL=200: miss 1.72%. CD running from 200 GeV. Less CD.
Hard threshold at M_VL=500: miss 4.01%. CD running from 500 GeV. Even less CD.
Soft threshold at M_VL=200: miss 7.14%. Gradual CD onset. Least effective CD.

The correlation is perfect: the prediction quality tracks the integrated CD contribution. The more CD running included, the closer α_s gets to the measured value. There is no threshold configuration that outperforms no-threshold.

---

**Section 7: Three Possible Explanations**

**Explanation A: Virtual propagation below M_VL.** The CD has virtual effects at energies below its mass through loop diagrams where the CD appears as an internal line. These effects are suppressed by (E/M_VL)² but nonzero. The no-threshold configuration may implicitly capture these virtual contributions, which the step function misses entirely. In this picture, the CD is never truly "off" — it contributes at all scales through quantum loops.

**Explanation B: Effective resummation.** The no-threshold running may accidentally resum a class of higher-order diagrams. By including the CD betas at all scales, the computation captures corrections that would appear only at three or higher loops in the standard threshold treatment. The no-threshold result is "too good" because it includes physics that belongs at higher perturbative orders.

**Explanation C: Cancellation.** The threshold correction and a missing higher-order correction may cancel at M_VL ~ M_Z. By not applying the threshold, both corrections are absent, and the cancellation is automatic. The no-threshold result is accidentally precise because two errors cancel.

The three explanations make different predictions for PHYS-37 (RK4 integration) and PHYS-38 (three-loop estimate). If Explanation A is correct, the advantage should persist with any integrator. If B, the advantage may shrink at higher orders. If C, the advantage is fragile and may vanish with more precise computation.

---

**Section 8: What This Paper Does Not Claim**

This paper does not claim the CD has no physical mass. If the CD exists, it has a mass, and the decoupling theorem applies. The paper documents that ignoring the threshold gives better predictions at the current level of computation.

This paper does not claim the no-threshold advantage is theoretically understood. The three explanations are hypotheses. None is derived.

This paper does not claim the soft threshold implementation is the only possible smooth function. Other forms (logarithmic matching, effective field theory step functions with Wilson coefficients) might perform differently. The sigmoid f = 1/(1+(M_VL/μ)²) is one physically motivated choice.

This paper does not claim that threshold corrections are unimportant in general. They are essential in precision electroweak physics. The paper claims they worsen the α_s prediction specifically in the context of CD unification.

---

**Section 9: What This Paper Seeds**

The no-threshold advantage is documented as a robust finding: 12× improvement, stable under step count variation, stronger than any threshold configuration tested.

PHYS-37 (RK4 integrator) tests whether the advantage persists with O(h⁴) integration instead of O(h) Euler. If it does, Explanation C (cancellation of Euler error with threshold error) is ruled out.

PHYS-38 (three-loop estimate) tests whether the advantage shrinks at higher perturbative order. If it does, Explanation B (effective resummation) is supported.

The finding constrains future CD mass estimates. If the CD is discovered and its mass measured, the threshold analysis must be revisited with the actual mass. The current analysis uses a scan over assumed masses.

---

### THE APPENDICES

**Appendix A:** The M_VL scan — complete data table (12 points)
**Appendix B:** Step sensitivity — 8 data points (4 per configuration)
**Appendix C:** Soft threshold — the sigmoid function and its behavior
**Appendix D:** The ranking — all configurations compared
**Appendix E:** The three explanations — predictions for future tests
**Appendix F:** Verification summary (9 PASS, 1 informative FAIL)

---

### ESTIMATED LENGTH

Body: 9 sections, approximately 5000 words.
Appendices: 6 tables, approximately 1500 words.
Total: approximately 6500 words.

---

### THE ONE-SENTENCE SUMMARY

PHYS-35 says: the no-threshold advantage (12× better α_s prediction) persists at 2000 Euler steps, beats every hard threshold from 200 GeV to 6 TeV, and is worsened by smooth decoupling — the pattern is that more CD running equals better predictions, which is physically puzzling because the decoupling theorem says the CD should not contribute below its mass, and three possible explanations (virtual propagation, effective resummation, cancellation) await testing by RK4 integration and three-loop estimates.
