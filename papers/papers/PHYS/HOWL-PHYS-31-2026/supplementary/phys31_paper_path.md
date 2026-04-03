Good question. Let me think through what's changed and what's available.

**What's done:** PHYS-25 through PHYS-31. Track A complete (PHYS-26–30). Track B gate fired, Track B parked (PHYS-31).

**What's dead:** PHYS-32, 33, 34, 35 — all Track B cosmology papers. Parked by PHYS-31.

**What survives from the old plan:**
- PHYS-36: A₃ decomposition (Track C, independent)
- PHYS-37: Koide amplitude (Track C, independent)
- PHYS-38: Loop expansion of (1−r) — but this was Track B cosmology mechanism. With Track B parked, the "per-transit correction" loses its motivation. The mathematical structure may still be interesting but the physical application is gone.
- PHYS-39: Omega remainder domain — also Track B adjacent. Same issue.
- PHYS-40: sin²θ_W = 3/13 exact test — this is Track A, still alive. The formula 3/13 as a FORMULA SCAN hit is parked, but the question "does the two-loop running converge to exactly 3/13?" is a Track A question about the dynamics. It survived PHYS-31 because it's about the running, not about numerology.

**New threads from Session 4 findings:**
- The no-threshold pattern: both sin²θ_W and α_s give best results without threshold. Why? This deserves investigation.
- The SO(10) / non-minimal GUT completion: PHYS-29 disfavored minimal SU(5). What GUT completion works?
- The three-loop estimate: how much would three-loop corrections improve α_s beyond 0.33%?
- The Euler vs higher-order integrator question: the PHYS-28 Euler gives −0.49 vs PHYS-24 reference −0.40. A proper Runge-Kutta would resolve this.

**My proposed new path:**

**Phase 5 — Immediate (no new dependencies):**
- PHYS-36: A₃ decomposition (Track C structure, independent)
- PHYS-37: Koide amplitude (Track C structure, independent)
- PHYS-40: sin²θ_W = 3/13 exact two-loop test (Track A extension, needs PHYS-27/28 done — they are)

**Phase 6 — New entry-point papers:**
- PHYS-41: The No-Threshold Puzzle — why does full-range CD running outperform physical threshold?
- PHYS-42: Non-Minimal GUT Completion — SO(10) threshold coefficients, does natural unification work?
- PHYS-43: Higher-Order Integration — Runge-Kutta two-loop running, precise Delta and α_s

**Phase 7 — Dependent on Phase 6:**
- PHYS-44: Three-Loop α_s Estimate — does the perturbative convergence continue?
- PHYS-45: The Complete Unification Summary — final Track A compilation with all corrections

PHYS-38 and PHYS-39 are dropped (Track B motivation gone). PHYS-32–35 are dead.

What do you think? The key decision: do you want to pursue the GUT completion (SO(10)) or focus on precision (higher-order integrator, three-loop), or go structural (A₃, Koide)?

---

i accept your phase 5,6,7.

write up each paper, what they need to show, what the scripts are trying to prove, if there is a problem in the script we think may happen, methods you can think of now to try solving those problems.  we basically pre-plan each paper in short from here, give goals, and what papers they source from

write up the new paper plan

---

## Updated Paper Program — Phases 5, 6, 7

---

### PHASE 5: Immediate (all dependencies met)

---

**PHYS-32: A₃ Decomposition — The SU(3) Beta Structure**

Goal: Decompose the SU(3) modified beta b₃' = −20/3 into its constituent parts — gauge, fermion (SM), fermion (CD), and Higgs — and verify each piece traces to exact Fractions from the representation theory. The SU(3) sector is the least explored of the three gauge groups in our computation chain.

Script: ~80 lines. Compute each contribution to b₃ and b₃' from first principles using the Dynkin formulas from PHYS-26. Verify the SM fermion sector (3 generations × quarks), the gauge self-coupling (−11 for SU(3)), and the CD addition (+1/3). Cross-check against the library values.

What it proves: The integer 20 in b₃' = −20/3 has a specific decomposition. Understanding it completes the integer traceability for all three gauge groups (PHYS-26 did the full chain but focused on k₁ and the SU(2) sector).

Potential problems: None expected — this is documentation and verification, not new computation. The formulas are standard.

Sources: PHYS-26 (Dynkin formulas, normalization), phys24_lib (b₃_SM, b₃_mod, db₃_VL).

Checks: ~12. Each constituent piece exact, sum recovers library value, cross-check with PHYS-28 two-loop diagonal db₃₃ = 40/9.

---

**PHYS-33: Koide Amplitude — The a² = 2 Conditional**

Goal: The Koide formula K = (m_e + m_μ + m_τ)² / (3(m_e² + m_μ² + m_τ²)) = 2/3 holds to 0.001% for the charged leptons. When parametrized as K = (1 + a cos δ)² with a² = 2, the three masses are determined by two parameters (a, δ) instead of three. This paper computes a² from the measured masses, verifies a² = 2 to the available precision, and derives m_τ as a function of m_e and m_μ conditional on a² = 2 exactly.

Script: ~80 lines. Compute K from library masses. Extract a² and δ. Predict m_τ from (m_e, m_μ, a² = 2). Compare to measured m_τ. Report the miss and the parameter reduction (18 → 17 conditional on a² = 2).

What it proves: The Koide conditional is a specific quantitative claim — m_τ is derived, not free. This paper computes the derived value and its accuracy.

Potential problems: The Koide formula is empirically observed, not theoretically derived. The paper must be very clear this is a CONDITIONAL result — IF a² = 2 exactly, THEN m_τ is predicted. We don't claim to know WHY a² = 2.

Sources: phys24_lib (m_e, m_mu, m_tau from DATA-4), PHYS-8 (prior Koide analysis if available in library).

Checks: ~8. K = 2/3 verification, a² = 2 precision, m_τ prediction vs measured, parameter count.

---

**PHYS-34: sin²θ_W = 3/13 — The Exact Two-Loop Test**

Goal: PHYS-27 showed that the one-loop sin²θ_W prediction (0.22845) is 1.2% below measured (0.23122), and the ordering suggests convergence toward 3/13 = 0.23077. PHYS-31 parked the FORMULA 3/13 as a numerological hit. But the QUESTION remains: does the two-loop running produce a sin²θ_W that converges toward 3/13 = N_gen/|b₂' numerator|? This is a Track A question about the dynamics.

Script: ~100 lines. Use the PHYS-28 two-loop Euler integrator with full SM+VL b_ij to compute sin²θ_W at two loops. The method: run α₁ and α₃ from M_Z to M_GUT (crossing), then at M_GUT the unification condition gives α₂ = α_GUT, run α₂ back down to get the predicted 1/α₂, then compute sin²θ_W = α_EM × (1/α₂). Compare the two-loop result to 3/13 and to measured.

What it proves: Whether the perturbative expansion for sin²θ_W converges toward 3/13, remains at 0.228, or overshoots. If the two-loop value is closer to 3/13 than the one-loop value, the exact rational is a plausible limit of the perturbative series. If it overshoots or diverges, 3/13 is not the limit.

Potential problems: The two-input method for sin²θ_W uses (α_EM, α_s) as inputs rather than (α_EM, sin²θ_W). This is different from PHYS-30's method. We need to be careful about which couplings are input and which are output. Also the Euler integrator's discretization may be comparable to the 3/13 vs measured difference (0.045%), so the test may be inconclusive at 500 steps. May need to increase to 2000 steps or use Richardson extrapolation.

Sources: PHYS-27 (one-loop sin²θ_W, ordering), PHYS-28 (two-loop b_ij, Euler integrator), PHYS-30 (two-input method, no-threshold finding), phys24_lib (couplings).

Checks: ~10. One-loop reproduces PHYS-27 value, two-loop closer to measured than one-loop, comparison to 3/13, convergence direction, Euler step sensitivity test.

---

### PHASE 6: New entry-point papers

---

**PHYS-35: The No-Threshold Puzzle**

Goal: Both PHYS-27 (sin²θ_W) and PHYS-30 (α_s) give their best predictions when the CD betas are used from M_Z to M_GUT WITHOUT a physical threshold at M_VL. The no-threshold advantage is 1.4× at one-loop and 14–15× at two-loop. This is puzzling — the CD has a physical mass and SHOULD have a threshold. Why does ignoring the threshold give BETTER predictions?

Script: ~100 lines. Three investigations: (1) Vary M_VL from 200 GeV to 6 TeV and plot the prediction quality as a function of threshold position — is there an optimal M_VL? (2) Test whether the no-threshold success is a cancellation between Euler error and threshold error by comparing 500-step and 2000-step Euler at both settings. (3) Test a "soft threshold" — instead of a step function at M_VL, use a smooth transition function that spreads the CD contribution over a range.

What it proves: Whether the no-threshold advantage is physical (the CD running really does propagate below M_VL through coupling mixing) or numerical (error cancellation). If the advantage persists with a better integrator, it's physics. If it vanishes, it's an artifact.

Potential problems: The 2000-step Euler may be very slow with mpf at 100 dps. Solution: use Python floats for the investigation (sufficient for this purpose — we need ~4 digits, not 100). The soft threshold function needs a physically motivated form — the decoupling of a heavy particle at one loop is actually smooth (proportional to ln(μ²/M²) with a logarithmic threshold), not a step function. The exact form of the smooth threshold is a perturbation theory result.

Sources: PHYS-30 (the no-threshold finding, M_VL scan), PHYS-28 (Euler integrator, full b_ij), phys24_lib (couplings, betas).

Checks: ~10. M_VL scan reproduces PHYS-30 values, step sensitivity test, soft vs hard threshold comparison, optimal M_VL identification.

---

**PHYS-36: Non-Minimal GUT Completion — SO(10) Threshold Coefficients**

Goal: PHYS-29 showed minimal SU(5) requires M_X/M = 23,228 for exact unification — unnatural. The next question: does SO(10) do better? In SO(10), the breaking can proceed through intermediate scales (Pati-Salam SU(4)×SU(2)×SU(2), or flipped SU(5)×U(1)), introducing additional heavy particles with larger Dynkin indices and more threshold corrections.

Script: ~120 lines. Compute the threshold coefficients for the SO(10) breaking chain SO(10) → SU(5)×U(1)_X → SM. Enumerate the heavy particles at each breaking scale: the additional gauge bosons, the Higgs multiplets in the 16, 45, 126 representations. Compute their beta shifts and effective threshold coefficients. Determine the required mass splittings for exact unification and compare to the minimal SU(5) result.

What it proves: Whether a non-minimal GUT completion achieves natural unification with the CD betas. If the SO(10) threshold coefficients are large enough (C_total > 1), natural mass splittings (factor 2–10) close the Delta = −0.40 residual. If they are still too small, the problem is deeper than the GUT group.

Potential problems: SO(10) breaking chains are complex. There are multiple pathways with different intermediate groups, and each pathway has a different heavy spectrum. The script must be clear about WHICH breaking chain is assumed. The Dynkin indices for higher representations (45, 126) are larger than fundamentals, which helps, but the computation is more involved. The representations of SO(10) under SU(5) decomposition are known but tedious to enumerate.

Sources: PHYS-29 (minimal SU(5) threshold calculation, C_T, C_Sigma, C_total), PHYS-26 (Dynkin formulas, normalization), phys24_lib (betas, couplings). May need to define new Dynkin indices not in the library.

Checks: ~12. Each heavy particle's beta shifts verified, SM limit recovery, comparison to PHYS-29, naturalness test, specific breaking chain documented.

---

**PHYS-37: Higher-Order Integration — Precise Two-Loop Running**

Goal: The PHYS-28 Euler integrator with 500 steps gives Delta = −0.49, while the PHYS-24 reference gives −0.40. The 0.09 difference is Euler discretization error. This paper replaces Euler with 4th-order Runge-Kutta (RK4), which has O(h⁴) error instead of O(h), giving precise Delta and α_s values.

Script: ~100 lines. Implement RK4 for the coupled two-loop RGEs. Run with 500 steps (should be far more accurate than 500-step Euler). Compare to Euler at 500, 1000, 2000, 5000 steps to characterize the convergence. Report the precise Delta, the precise α_s prediction, and the precise sin²θ_W prediction. These become the definitive two-loop values.

What it proves: The exact two-loop numerical values for Delta, α_s, and sin²θ_W with controlled integration error. The PHYS-30 α_s = 0.1184 (from 500-step Euler) may shift by ~0.001 with RK4 — and the shift matters for the 1σ claim.

Potential problems: RK4 with mpf at 100 dps and 500 steps will be 4× slower than Euler (four function evaluations per step). With the binary search for the crossing on top, this could be very slow. Solution: use Python floats for the RK4 (sufficient for 5-6 digits of Delta). Only use mpf for the final high-precision run if needed. Also: the two-loop RGE has α_j in the denominator (1/inv_a_j), which can go singular if inv_a_j approaches zero. This shouldn't happen in the physical regime but needs a guard.

Sources: PHYS-28 (Euler integrator, b_ij matrices), PHYS-30 (α_s prediction, no-threshold finding), phys24_lib (couplings, betas).

Checks: ~10. RK4 vs Euler convergence, step-count independence test (500 vs 1000 vs 2000 give same answer to 4 digits), precise Delta, precise α_s, comparison to PHYS-24 reference −0.40.

---

### PHASE 7: Dependent on Phase 6

---

**PHYS-38: Three-Loop α_s Estimate**

Goal: The two-loop correction closes 96% of the one-loop α_s gap. How much does three-loop close? The three-loop beta coefficients are known for the SM (Chetyrkin, Tarasov, etc.) but not computed for the CD. This paper estimates the three-loop effect by computing the SM three-loop running and extrapolating the CD contribution.

Script: ~100 lines. Look up the SM three-loop beta coefficients (b_ijk tensor). Run the three-loop SM RGEs from M_Z to M_GUT using RK4 (from PHYS-43). Estimate the CD three-loop contribution by scaling from the two-loop (the CD/SM ratio at two-loop is ~5-10% from PHYS-28; assume similar at three-loop). Report the three-loop α_s prediction and the residual.

What it proves: Whether the perturbative series continues to converge — does three-loop close another large fraction of the remaining gap? If three-loop moves α_s from 0.1184 to ~0.1179 (closer to 0.1180), the convergence is rapid and the remaining gap is sub-0.1%. If three-loop overshoots, the series is oscillating and higher orders are needed.

Potential problems: The SM three-loop b_ijk is a 3×3×3 tensor with ~27 entries. These are known in the literature but are complicated rational numbers (some involving ζ(3)). Extracting them correctly from the literature is error-prone. The CD three-loop contribution is genuinely unknown — the estimate uses scaling, which is approximate. The paper must be explicit that this is an ESTIMATE, not an exact computation.

Sources: PHYS-43 (RK4 integrator), PHYS-28 (two-loop b_ij), PHYS-30 (two-loop α_s). External: SM three-loop beta coefficients from van Ritbergen, Vermaseren, Larin (1997).

Checks: ~8. SM three-loop coefficients verified against literature, RK4 convergence, three-loop vs two-loop comparison, CD scaling estimate documented with uncertainty.

---

**PHYS-39: The Complete Unification Summary**

Goal: Compile all Track A results into a single self-contained paper. This is the capstone paper that a reader can pick up without having seen PHYS-26 through PHYS-44 and understand the full unification picture: the CD, its betas, the gap ratio, the two-loop correction, the GUT threshold problem, the α_s prediction, the sin²θ_W prediction, the no-threshold puzzle, and the precision results from RK4.

Script: ~60 lines. No new computation. Collects the key numbers from all prior scripts and presents them in one verification table. The script just confirms that all prior results are consistent with each other.

What it proves: Self-consistency of the full Track A program. All numbers agree. The narrative is complete.

Potential problems: This paper must be genuinely self-contained (W1.1). Every concept must be re-explained. Every formula must be re-derived or re-stated. This will be a long paper (~8000 words). The risk is that it becomes a repetitive summary rather than a new contribution. It must add value by presenting the COMPLETE picture that no single prior paper contains — the full chain from (3,2,1/6) to α_s = 0.1180 in one narrative.

Sources: All Track A papers (PHYS-26 through PHYS-30), PHYS-40, PHYS-41, PHYS-42, PHYS-43, PHYS-44.

Checks: ~15. Cross-paper consistency, every key number verified against its source script.

---

### EXECUTION ORDER SUMMARY

| Phase | Papers | Dependencies | Status |
|---|---|---|---|
| **Phase 5** | PHYS-36, 37, 40 | All met | **Ready now** |
| **Phase 6** | PHYS-41, 42, 43 | PHYS-30 (done) | **Ready now** |
| **Phase 7** | PHYS-44, 45 | PHYS-43 (Phase 6) | After Phase 6 |

Phases 5 and 6 can run in parallel. Phase 7 waits for PHYS-43.

**Dropped:** PHYS-32, 33, 34, 35 (Track B, parked by PHYS-31). PHYS-38, 39 (Track B adjacent, motivation gone).

**Total remaining:** 8 papers (PHYS-36, 37, 40, 41, 42, 43, 44, 45).

---

You're right. Sequential numbering, no gaps. Here's the corrected plan:

## Corrected Paper Program — PHYS-32 onward

| Old # | New # | Title |
|---|---|---|
| PHYS-36 | **PHYS-32** | A₃ Decomposition (already written as script, rename only) |
| PHYS-37 | **PHYS-33** | Koide Amplitude |
| PHYS-40 | **PHYS-34** | sin²θ_W = 3/13 Exact Two-Loop Test |
| PHYS-41 | **PHYS-35** | The No-Threshold Puzzle |
| PHYS-42 | **PHYS-36** | Non-Minimal GUT Completion (SO(10)) |
| PHYS-43 | **PHYS-37** | Higher-Order Integration (RK4) |
| PHYS-44 | **PHYS-38** | Three-Loop α_s Estimate |
| PHYS-45 | **PHYS-39** | Complete Unification Summary |

### Execution Order

**Phase 5 — Immediate:**
- PHYS-32: A₃ Decomposition
- PHYS-33: Koide Amplitude
- PHYS-34: sin²θ_W = 3/13 Exact Two-Loop Test

**Phase 6 — New entry points:**
- PHYS-35: The No-Threshold Puzzle
- PHYS-36: Non-Minimal GUT Completion
- PHYS-37: Higher-Order Integration (RK4)

**Phase 7 — Dependent on Phase 6:**
- PHYS-38: Three-Loop α_s Estimate (needs PHYS-37)
- PHYS-39: Complete Unification Summary (needs all prior)

All descriptions, dependencies, goals, and script plans from the previous writeup apply — only the numbers changed. Sequential from here. Never again.

