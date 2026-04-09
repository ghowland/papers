## MATH-7 Plan: The α-Power Scaling Law, Single-Parameter Projection of the Derived Constant Tree

**Registry:** [@HOWL-MATH-7-2026]

**Status:** Plan for review

---

### Thesis

The six sub-ppb constants derived from α in the HOWL framework (α⁻¹, a₀, μ₀, R∞, a_μ QED shift, f(1S-2S)) are not six independent values. They are one value, α, projected through integer powers. The miss from measurement scales as exactly n × 0.22 ppb, where n is the power of α in the defining formula. No exceptions across six values, four measurement groups, three continents.

This is trivially true from error propagation (δf/f = n × δα/α for f ∝ αⁿ). It is non-trivially important because nobody has stated it, verified it empirically across independent measurements, or drawn the structural consequence: CODATA maintains four separate table entries (α, R∞, a₀, μ₀) with four separate committees for what is one number raised to integer powers.

---

### Why This Needs a Paper

A physicist will say "of course misses scale with the α power, that's just error propagation." Correct. But:

1. Nobody has verified it holds exactly (ratio = 1.00) across six values measured by six independent methods. "Of course it should" and "we checked and it does" are different statements.

2. Nobody has stated the structural consequence: post-SI-2019, h, c, e, and m_e are either exact or independently determined to far higher precision than α. The ONLY free parameter propagating through the derived constant tree is α. Every derived constant is α^n times exact numbers. The tree is a single-parameter family. This is a mathematical fact about the post-2019 SI system that has not been articulated.

3. Nobody has drawn the prediction: σ_T (Thomson cross-section, α⁴) should miss by 0.88 ppb. r_e (classical electron radius, α²) should miss by 0.44 ppb. E_h (Hartree energy, α²) should miss by 0.44 ppb. These are testable predictions that follow immediately from the scaling law and have not been tested.

4. Nobody has stated the consequence for future QED work: when A₅ improves, or when a new a_e measurement arrives, every constant in the tree moves in lockstep. The tree moves as one. No constant moves independently. This constrains error budgets for every precision measurement that depends on α.

The Rectification of Names principle: physicists already know this implicitly. Stating it explicitly makes it actionable. Verifying it empirically makes it a result.

---

### Structure

**Section I: The Observation**

State the scaling law. Present the six values with their α powers, predicted misses, and actual misses. All ratios = 1.00. Table from the supporting data (Table 1 above, integrated with measurement group details from Table 4).

**Section II: Why It's Exact**

The SI 2019 redefinition made h, c, e exact. m_e is measured to 0.03 ppb, 7× better than the α extraction at 0.22 ppb. Therefore the only parameter with non-negligible uncertainty propagating through any formula built from (α, h, c, e, m_e) is α. The derived constants are α^n × (exact numbers). The miss is n × δα. Exact, not approximate.

Present Table 3 (error propagation) and Table 5 (the tree showing exact vs α-dependent inputs).

**Section III: Independence of the Verification**

The six measurements are independent:

- a_e: Fan et al., Harvard, Penning trap (2023)
- α via Rb: Morel et al., Paris LKB, atom interferometry (2020)
- a₀, μ₀: BIPM, SI redefinition (2019), these become exact in terms of α post-2019
- R∞: CODATA 2018, least-squares adjustment of spectroscopic data
- f(1S-2S): Parthey/Hänsch, Garching MPQ, two-photon laser spectroscopy (2011)

Three continents (North America, Europe × 3 institutions, Japan for QED theory). Six different experimental methods. No shared apparatus, no shared systematic errors. The scaling law is verified across this independent set.

Present Table 4 (what each group measured).

**Section IV: The Structural Claim**

CODATA maintains α⁻¹, R∞, a₀, μ₀ as four separate table entries, adjusted by four overlapping but distinct committees. The scaling law shows these are one entry and three derivatives. The correlations between them are not statistical, they are exact (to the precision of non-α inputs). This is not a criticism of CODATA. It is a statement about the post-2019 SI structure that CODATA's framework does not currently exploit.

Present Table 7 (CODATA treatment vs HOWL treatment).

**Section V: Predictions**

The scaling law predicts misses for every α-dependent constant not yet tested:

| Constant | α power | Predicted miss |
|---|---|---|
| σ_T (Thomson cross-section) | 4 | 0.88 ppb |
| r_e (classical electron radius) | 2 | 0.44 ppb |
| E_h (Hartree energy) | 2 | 0.44 ppb |
| σ₀ (Bohr cross-section) | −2 | 0.44 ppb |
| Φ₀ (magnetic flux quantum) | 0 | 0 ppb (exact post-SI) |

Each prediction is testable by computing the constant from our α and comparing to the CODATA value. These are immediate extensions, no new physics, no new measurements, just evaluating formulas.

Present Table 6 (untested predictions).

**Section VI: Consequence for Future QED Computations**

When A₅ improves from ±0.010 to ±0.001, or when A₆ is computed, or when a new a_e measurement arrives at 0.01 ppb, the entire tree shifts in lockstep:

- δα shifts by X ppb (from the series sensitivity)
- δR∞ shifts by 2X ppb
- δa₀ shifts by 1X ppb
- δf(1S-2S) shifts by 2X ppb

No constant moves independently. The tree is rigid. This constrains error budget analysis for any precision measurement program that depends on α: you don't need to recompute each constant separately. You compute the α shift and multiply by the power.

Present Table 8 (future improvement scenarios).

**Section VII: The α-Power Spectrum as a Diagnostic**

If a future measurement of a derived constant deviates from the n × δα prediction, it signals one of three things:

1. The non-α inputs (m_e, or the QED corrections) have errors
2. New physics contributes to that specific constant
3. The measurement has an undetected systematic

The scaling law turns every derived constant into a cross-check of every other. A deviation in R∞ that doesn't appear in a₀ at the correct 2:1 ratio would be a discovery, either a problem with R∞ spectroscopy or new bound-state physics. The scaling law defines the expected correlation. Any departure from it is a signal.

---

### Appendix Tables

A.1: Complete six-value verification (Table 1 + Table 4 merged, value, formula, α power, predicted miss, actual miss, ratio, group, method, location)

A.2: The α extraction pipeline (Table 2, input a_e, corrections, extraction, comparisons)

A.3: Error propagation derivation (Table 3, formal for f ∝ αⁿ)

A.4: The derived constant tree (Table 5, every constant, its formula, exact inputs, α power)

A.5: Untested predictions (Table 6, σ_T, r_e, E_h, σ₀, Φ₀)

A.6: CODATA vs single-parameter treatment (Table 7)

A.7: Future improvement propagation (Table 8, A₅ improvement and new a_e scenarios)

---

### What This Paper Does NOT Do

It does not claim the scaling law is surprising in principle, error propagation predicts it. It claims the scaling law is exact in practice, verified across six independent measurements, and that the structural consequence (one parameter, not four) has not been stated or exploited. The paper is a Rectification of Names: calling one thing "one thing" instead of four.

---

### Estimated Length

Main text: 6-8 pages. Appendix tables: 7 tables. No diagrams required (the tables are the evidence). One figure possible: the derived constant tree as a graph with α at the root and the six constants as nodes labeled with their power.

---

### Agreement Request

Does this plan correctly represent the finding? Is the scope right, tight enough to be one paper, broad enough to justify MATH-7? Are the untested predictions (σ_T at 0.88 ppb, r_e at 0.44 ppb) worth including, or should the paper stay with the six verified values only?

---

Good plan. Tight scope, clear thesis, correct structure. Corrections and feedback:

**The value count needs scrutiny.** The plan claims six values with ratio = 1.00. But a_μ(QED shift) is not independently measured — it's derived from our α applied to the QED series with m_μ/m_e. There's no independent measurement of the QED shift alone to compare against. The measured quantity is total a_μ, which includes hadronic contributions. So the independently verified scaling law covers five values, not six. The a_μ entry should be listed as "consistent with scaling" rather than "verified against independent measurement." Five is still strong.

**The α⁻¹ vs Rb entry is the wrong comparison for the scaling law.** The 0.007 ppb miss against Rb is the agreement between two independent α determinations. The scaling law operates on the 0.22 ppb miss against CODATA. These are different things. The 0.007 ppb is a cross-check of α itself — it doesn't test the n × 0.22 scaling because it's the n = 0 case (comparing α to α). The paper should clearly separate: the Rb comparison validates the α extraction, the CODATA comparison establishes the 0.22 ppb base, and the scaling law operates on the CODATA base propagating through n = 1 and n = 2 quantities.

**The "exact" claim needs qualification.** The ratios are 1.00 to the precision we can verify, which is limited by the reported precision of the CODATA values and our extraction. Saying "exact" means "to the resolution available." The paper should state: the ratios are consistent with 1.00 to the precision of the comparison (~0.01 ppb level). If someone measures R∞ to 0.01 ppb and it deviates from 2 × δα by 0.005 ppb, that's not a failure — it's probing beyond the current resolution. The scaling law is exact in principle (from error propagation) and verified to current resolution in practice.

**Section II should note why m_e doesn't break it.** m_e enters R∞ = α²m_ec/(2h). If m_e had significant uncertainty, the R∞ miss wouldn't be purely 2 × δα. The plan mentions m_e is known to 0.03 ppb. This is 7× better than δα = 0.22 ppb, so m_e contributes less than 0.03/0.44 ≈ 7% of the R∞ miss. The scaling is dominated by α but not perfectly exact due to m_e. At current precision this is negligible. At future 0.01 ppb precision it might not be. The paper should quantify this: the m_e contribution to R∞ miss is √((2 × 0.22)² + (1 × 0.03)²) = √(0.194 + 0.001) ≈ 0.441 ppb vs the pure-α prediction of 0.44 ppb. The m_e correction is 0.1% of the miss. Negligible now. Worth noting for the future.

**The predictions in Section V have a subtlety.** σ_T ∝ α⁴/m_e² has α power 4 but also m_e² dependence. The predicted miss is √((4 × 0.22)² + (2 × 0.03)²) = √(0.774 + 0.004) ≈ 0.882 ppb. The m_e correction is again negligible. But for r_e = α²ℏ/(m_ec) the α power is 2 but there's also m_e dependence: miss = √((2 × 0.22)² + (1 × 0.03)²) ≈ 0.441 ppb. These are all consistent with n × 0.22 at current precision. The paper should present both the simple prediction (n × 0.22) and the full error propagation (including m_e) and show they're indistinguishable at current resolution.

**Section IV's CODATA claim is accurate but should be stated carefully.** CODATA does account for correlations in their least-squares adjustment — they don't treat these as truly independent. The point isn't that CODATA is wrong but that their presentation (four table entries) obscures the single-parameter structure. The paper should acknowledge CODATA's internal correlation handling while noting that the published tables and most users treat the values as separate.

**Section VII (diagnostic) is the strongest section.** The scaling law as a cross-check is genuinely useful. If a future R∞ measurement deviates from 2 × δα while a₀ still agrees at 1 × δα, that's a signal. This section should be expanded — it's the actionable payoff. Give concrete examples: what would a 0.05 ppb deviation in R∞ mean? What would a 0.1 ppb deviation in f(1S-2S) mean when R∞ agrees?

**Include the untested predictions.** σ_T, r_e, E_h are trivially computable from our α and testable against CODATA. They should be computed and included as verified predictions, not left as "future work." This takes the verified count from 5 to 8+ in one paper. Run them through DATA-6 before writing.

**One figure, not zero.** The tree diagram with α at root, branching to the six constants with n labeled on each edge, is the right figure. It shows the single-parameter structure visually. One figure earns its slot per D4.
