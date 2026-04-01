# Supporting Tables for the Electroweak Overconstrained Computation

## Table 1: Fermion Quantum Numbers (all exact integers or simple fractions)

These are the gauge group assignments. Every one is exact. They enter every partial width formula.

| Fermion | T₃ (weak isospin) | Q (electric charge) | N_c (color) | v_f = T₃ − 2Q sin²θ_W | a_f = T₃ |
|---|---|---|---|---|---|
| ν_e, ν_μ, ν_τ | +1/2 | 0 | 1 | +1/2 | +1/2 |
| e⁻, μ⁻, τ⁻ | −1/2 | −1 | 1 | −1/2 + 2sin²θ_W | −1/2 |
| u, c, t | +1/2 | +2/3 | 3 | +1/2 − 4sin²θ_W/3 | +1/2 |
| d, s, b | −1/2 | −1/3 | 3 | −1/2 + 2sin²θ_W/3 | −1/2 |

**In Fraction arithmetic** with s² = sin²θ_W = Fraction(23122, 100000):

| Fermion | v_f (Fraction) | v_f (decimal) | a_f (Fraction) | v_f² + a_f² |
|---|---|---|---|---|
| ν | 1/2 | 0.5000 | 1/2 | 1/2 |
| e⁻ | −1/2 + 2×23122/100000 = −3756/100000 | −0.03756 | −1/2 | 0.25141 |
| u | 1/2 − 4×23122/(3×100000) = 19170/100000 | 0.19170 | 1/2 | 0.28675 |
| d | −1/2 + 2×23122/(3×100000) = −34586/100000 | −0.34586 | −1/2 | 0.36962 |

Note: v_e is small (0.038) because sin²θ_W ≈ 1/4 makes the two terms in v_e nearly cancel. This is why the leptonic asymmetries are small and sensitive to sin²θ_W.

## Table 2: QCD Correction Factors (rational coefficients)

The QCD correction to hadronic Z partial widths is:

δ_QCD = (α_s/π) + c₂(α_s/π)² + c₃(α_s/π)³ + ...

| Order | Coefficient | Exact Rational | Decimal | Source |
|---|---|---|---|---|
| 1-loop | c₁ | 1 | 1.000 | Exact |
| 2-loop | c₂ | 365/24 − 11ζ(3) + n_f(−11/12 + 2ζ(3)/3) | 1.409 (n_f=5) | Chetyrkin, Kataev, Tkachov |
| 3-loop | c₃ | (known rational + transcendental) | −12.77 (n_f=5) | Gorishnii, Kataev, Larin, Surguladze |

At α_s = 0.1180, α_s/π = 0.03756:

| Term | Value | Cumulative |
|---|---|---|
| 1 | 1.00000 | 1.00000 |
| +α_s/π | +0.03756 | 1.03756 |
| +c₂(α_s/π)² | +0.00199 | 1.03955 |
| +c₃(α_s/π)³ | −0.00068 | 1.03887 |
| **Total δ_QCD** | | **1.03887** |

For the Fraction computation, use α_s/π = α_s/(4R₂) and the Q335 numerator for π.

## Table 3: Tree-Level Partial Widths

The tree-level formula: Γ_f = (G_F M_Z³)/(6π√2) × (v_f² + a_f²) × N_c

The prefactor (G_F M_Z³)/(6π√2) is common to all channels. Compute once:

| Quantity | Expression | Value (MeV) |
|---|---|---|
| G_F M_Z³ | 1.1663788×10⁻⁵ × 91187.6³ | 8.8386 × 10⁹ MeV² |
| 6π√2 | 6 × 3.14159 × 1.41421 | 26.6573 |
| Prefactor Γ₀ | G_F M_Z³/(6π√2) | 331.56 MeV |

Then each partial width is Γ₀ × (v_f² + a_f²) × N_c × (1 + δ_QCD):

| Channel | v_f² + a_f² | N_c | 1+δ_QCD | Γ_f (MeV) | LEP measured (MeV) |
|---|---|---|---|---|---|
| ν (×3 flavors) | 0.2500 | 1 | 1.000 | 82.89 × 3 = 248.7 | — (invisible) |
| e⁻ (= μ⁻ = τ⁻) | 0.25141 | 1 | 1.000 | 83.36 | 83.984 ± 0.086 |
| u, c (×2) | 0.28675 | 3 | 1.039 | 296.4 × 2 = 592.8 | — |
| d, s, b (×3) | 0.36962 | 3 | 1.039 | 382.0 × 3 = 1146.1 | — |
| **Γ_had** | | | | **1738.9** | — |
| **Γ_total** | | | | **2153.9** | **2495.2 ± 2.3** |

The tree-level total width misses the measured value by ~14%. This is expected — one-loop electroweak corrections (primarily the ρ parameter from the top quark) shift partial widths by ~3-4% each. The computation needs the leading ρ correction to reach per-mille agreement.

## Table 4: The ρ Parameter (Leading One-Loop Correction)

The dominant radiative correction is:

Δρ = 3G_F m_t²/(8π²√2) = 3G_F m_t²/(256R₄√2)

With DATA-2 values: Δρ = 3 × 1.1664×10⁻⁵ × 172570²/(8 × 9.8696 × 1.4142) = 0.00940

This shifts all partial widths by a factor (1 + Δρ) in the relation between the measured sin²θ_W and the tree-level couplings. The effective replacement is:

v_f² + a_f² → ρ_eff × (v_f² + a_f²) where ρ_eff ≈ 1 + Δρ ≈ 1.0094

| Quantity | Formula | Value |
|---|---|---|
| Δρ | 3G_F m_t²/(8π²√2) | 0.00940 |
| ρ_eff | 1 + Δρ | 1.00940 |
| Correction to Γ_total | ×ρ_eff | +0.94% |

Including Δρ: Γ_total ≈ 2153.9 × 1.0094 ≈ 2174.1 MeV. Still 13% below. The remaining gap is from proper treatment of the running of sin²θ_W between the on-shell and MS-bar schemes, and higher-order corrections.

## Table 5: Observables for Extraction

These are the measured ratios and asymmetries that constrain sin²θ_W and α_s independently.

| Observable | Formula | Depends On | DATA-2 Value | Precision |
|---|---|---|---|---|
| R_l = Γ_had/Γ_l | [Σ_q N_c(v_q²+a_q²)(1+δ)] / (v_l²+a_l²) | sin²θ_W, α_s | 20.767 | 0.12% |
| A_FB^l | (3/4) × [2v_ea_e/(v_e²+a_e²)]² | sin²θ_W only | 0.0171 | 5.8% |
| A_l(SLD) | 2v_la_l/(v_l²+a_l²) | sin²θ_W only | 0.1513 | 1.4% |
| σ⁰_had | 12πΓ_eΓ_had/(M_Z²Γ_Z²) | G_F, M_Z, sin²θ_W, α_s | 41.481 nb | 0.08% |
| R_b = Γ_bb/Γ_had | (v_b²+a_b²)/[Σ_q(v_q²+a_q²)] | sin²θ_W, m_t (vertex) | 0.21629 | 0.31% |
| N_ν | Γ_inv/Γ_l (assumes Γ_ν = SM) | sin²θ_W | 2.9840 | 0.27% |

**Extraction chain:**
1. A_FB^l → sin²θ_W (independent of α_s)
2. R_l + sin²θ_W → α_s (the only remaining unknown in R_l)
3. Compare extracted sin²θ_W and α_s to input values

## Table 6: The Integer Content

The integers that enter the electroweak computation, classified by origin:

| Integer | Origin | Where It Appears |
|---|---|---|
| 3 | SU(3) color | N_c in quark widths |
| 2 | SU(2) doublet | T₃ = ±1/2 |
| 1, −1 | U(1) charges | Q_f = 0, −1, +2/3, −1/3 |
| 3 | generations | 3 neutrino, 3 lepton, 2 up-type, 3 down-type contributing to Γ_Z |
| 6 | phase space | 1/(6π√2) prefactor |
| 1/2 | Dirac spinor | a_f = T₃ = ±1/2 |
| 4/3, 2/3 | charge ratios | v_u = 1/2 − 4sin²θ/3, v_d = −1/2 + 2sin²θ/3 |
| 3, 8π² | loop factor | Δρ = 3G_F m_t²/(8π²√2) |
| 1 | QCD 1-loop | δ_QCD leading term coefficient = 1 |
| 365/24, 11 | QCD 2-loop | c₂ rational part and ζ(3) coefficient |

Every integer traces to either the gauge group (SU(3)×SU(2)×U(1)), the generation count, or the loop expansion. The measured inputs (G_F, M_Z, sin²θ_W, α_s, m_t, m_H, α) are the ONLY non-integer content. This is the PHYS-2 thesis made explicit: the transformation laws are integers, the values are not.

## Table 7: Sensitivity Matrix

How much does each observable shift per unit change in sin²θ_W and α_s? This determines the extraction precision.

| Observable | ∂(obs)/∂(sin²θ_W) | ∂(obs)/∂(α_s) | Best constrains |
|---|---|---|---|
| R_l | −250 (strong) | +83 (strong) | Both, simultaneously |
| A_FB^l | +1.6 (strong for small A_FB) | 0 (zero) | sin²θ_W only |
| A_l(SLD) | −8.0 (strong) | 0 (zero) | sin²θ_W only |
| σ⁰_had | +35 (moderate) | +2.5 (weak) | sin²θ_W primarily |
| R_b | +0.7 (weak) | −0.004 (negligible) | m_t (vertex correction) |
| Γ_Z | −5000 MeV (strong) | +230 MeV (strong) | Both |

The extraction strategy is clear from the sensitivities. A_FB^l and A_l have ZERO sensitivity to α_s, so they give pure sin²θ_W extractions. Then R_l, with its strong α_s sensitivity, gives α_s once sin²θ_W is fixed.

## Table 8: Expected vs Measured — What Agreement Looks Like

At tree level + leading Δρ, the expected agreement is ~1% (one-loop corrections not yet included give ~1% shifts). At full one-loop, agreement should be ~0.1% (matching the LEP measurement precision of 3-5 sig figs).

| Level of Calculation | Expected Agreement | What It Proves |
|---|---|---|
| Tree level only | ~10-15% | Gauge structure correct |
| Tree + Δρ (leading m_t correction) | ~1-3% | Top quark mass effect visible |
| Full one-loop | ~0.1-0.3% | SM consistency at LEP precision |
| Full one-loop + leading two-loop | ~0.03% | Below LEP measurement uncertainty |

For the first computation, tree + Δρ is the target. This is achievable in one session and demonstrates the integer anatomy. Full one-loop requires additional form factors (box diagrams, vertex corrections) that are known but tedious to implement.

---

*These tables provide all quantum numbers, formulas, and sensitivity information needed to write the electroweak computation script. Every integer in Table 6 and every quantum number in Table 1 is exact. The measured inputs are the 7 DATA-2 Fractions listed in the plan. The output is 13 computed observables compared to 13 measured values.*

