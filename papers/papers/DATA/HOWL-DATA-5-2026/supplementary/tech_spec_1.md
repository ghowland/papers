## DATA-5 Technical Specification v2

**Registry:** [@HOWL-DATA-5-2026]
**Date:** April 3 2026
**Supersedes:** DATA-5 Tech Spec v1
**Predecessor:** DATA-4 (146 entries, 38/38 checks), phys24_lib.py (21/21 self-test, 148/148 platform test)

---

### 1. WHAT DATA-5 IS

DATA-5 is the Session 4 data platform. It consists of:

```
data5.py          # The library (inherits phys24_lib + all DATA-4 entries + Session 4 additions)
data5_test.py     # The test suite (~250 checks)
data5_fast.py     # Float-speed utility functions (separate, explicitly imported)
```

DATA-5 inherits every value from phys24_lib and DATA-4 with ZERO changes. New values from PHYS-25 through PHYS-35 are added. New derivation functions and pitfall documentation are added. The API only grows — nothing is removed or renamed.

DATA-5 is NOT a physics paper. It stores data about physics things. It does not assert that the CD exists, that unification is real, or that any prediction is correct. It provides the numbers and the functions that produce them.

---

### 2. INHERITANCE RULE

Every value in phys24_lib appears in DATA-5 with the same variable name and the same value. Every entry in DATA-4 is referenced by its DATA-4 entry ID (B1, B2, ..., C1, ..., D1, ..., N1, ...). No entry IDs are renumbered.

If a phys24_lib variable name and a DATA-4 entry ID refer to the same value, both references are documented in DATA-5. Example: `alpha_inv` (phys24_lib variable) = DATA-4 entry B1.

---

### 3. SECTIONS IN data5.py

```
A. INFRASTRUCTURE        # Unchanged from phys24_lib
B. MEASURED CONSTANTS     # Inherited from phys24_lib/DATA-4, all Level 2
C. DERIVED CONSTANTS      # Exact Fractions, all Level 1
D. SM BETA COEFFICIENTS   # One-loop, exact Fractions (DATA-4 N1–N3)
E. CD BETA COEFFICIENTS   # One-loop, exact Fractions (DATA-4 N4–N9)
F. TWO-LOOP MATRICES      # SM b_ij (DATA-4 N14), VL db_ij (new), full b_ij (new)
G. GROUP THEORY           # Casimirs, Dynkin indices, dimensions (new)
H. DECOMPOSITION DATA     # Per-constituent pieces of each beta (new)
I. THRESHOLD DATA         # GUT threshold coefficients (new)
J. PREDICTIONS            # Computed values from series scripts (new)
K. KOIDE DATA             # Lepton mass relations (new, extends DATA-4 K section)
L. DERIVATION FUNCTIONS   # How to compute from inputs (new)
M. PITFALL DOCUMENTATION  # What goes wrong and why (new)
N. NAME MAPPINGS          # Aliases, series terminology (new)
```

---

### 4. SECTION A: INFRASTRUCTURE

Unchanged from phys24_lib. All helper functions carry forward with identical signatures:

`f2m`, `digits_of`, `show`, `chk`, `chk_exact`, `chk_bool`, `chk_precision`, `precision_report`, `count_sig_digits`, `print_summary`

`mp.dps = 100` as standing precision.

---

### 5. SECTION B: MEASURED CONSTANTS (Level 2)

Every value inherited from phys24_lib. Source: DATA-4 entries, which inherit from DATA-3 (32/32), which inherit from CODATA 2022 / PDG 2024. All values are exact Fractions or Q335 Fractions.

| Variable | DATA-4 ID | Value | Unit | Precision |
|---|---|---|---|---|
| alpha_inv | B1 | 137035999177/10⁹ | dimensionless | 12 sf |
| m_e | B2 | 51099895069/10¹¹ | MeV | 11 sf |
| m_mu | B3 | 1056583755/10⁷ | MeV | 10 sf |
| m_tau | B4 | 177686/100 | MeV | 6 sf |
| m_p | B5 | 93827208943/10⁸ | MeV | 11 sf |
| mp_me | B6 | 183615267343/10⁸ | dimensionless | 13 sf |
| R_inf | B7 | 10973731568157/10⁶ | m⁻¹ | 13 sf |
| a_0 | B8 | 529177210544/10²² | m | 12 sf |
| a_e | B9 | 115965218059/10¹⁴ | dimensionless | 12 sf |
| a_mu | B10 | 116592059/10¹¹ | dimensionless | 9 sf |
| sin2_tW | B11 | 23122/100000 | dimensionless | 5 sf |
| alpha_s | B12 | 1180/10000 | dimensionless | 4 sf |
| mu_0 | B13 | 125663706127/10¹⁷ | N/A² | 12 sf |
| M_Z | C1 | 911876/10 | MeV | 6 sf |
| Gamma_Z | C2 | 24952/10 | MeV | 5 sf |
| M_W | C3 | 803692/10 | MeV | 6 sf |
| m_t | C4 | 172570/1 | MeV | 5 sf |
| m_H | C5 | 125200/1 | MeV | 5 sf |
| G_F | C6 | 11663788/10¹² | GeV⁻² | 8 sf |
| m_u | D1 | 216/100 | MeV | 3 sf |
| m_d | D2 | 470/100 | MeV | 3 sf |
| m_s | D3 | 935/10 | MeV | 3 sf |
| m_c | D4 | 1273/1 | MeV | 4 sf |
| m_b | D5 | 4183/1 | MeV | 4 sf |

Plus all remaining DATA-4 entries (D6–D11, E1–E8, F1, G1–G14, K1–K8, L1–L6, N1–N17). Every value exactly as stored in data_4.py.

---

### 6. SECTION C: DERIVED CONSTANTS (Level 1)

Exact Fractions computed from the framework. Not measured — determined by gauge group mathematics.

| Variable | Value | Fraction | DATA-4 source | Derivation | Paper |
|---|---|---|---|---|---|
| k1 | 3/5 | Fraction(3, 5) | — | SU(5) normalization: Tr(T₃²)/Tr(Y²) | PHYS-26 |
| k1_inv | 5/3 | Fraction(5, 3) | — | 1/k₁ | PHYS-26 |
| gap_SM | 218/115 | Fraction(218, 115) | N10 | (b₁_SM − b₂_SM)/(b₂_SM − b₃_SM) | PHYS-13 |
| gap_CD | 38/27 | Fraction(38, 27) | N11 | (b₁' − b₂')/(b₂' − b₃') | PHYS-13 |
| gap_MSSM | 7/5 | Fraction(7, 5) | N12 | MSSM convention check | PHYS-26 |
| sin2_tree | 3/8 | Fraction(3, 8) | — | GUT tree-level sin²θ_W | PHYS-27 |
| sin2_3_13 | 3/13 | Fraction(3, 13) | — | N_gen/\|b₂' numerator\| | PHYS-27 |
| correction_exact | 15/104 | Fraction(15, 104) | — | 3/8 − 3/13 | PHYS-27 |
| b_EM_CD | 43/9 | Fraction(43, 9) | — | (5/3)b₁' + b₂' | PHYS-34 |
| n_f_crit_SU3 | 33/4 | Fraction(33, 4) | — | b₃ = 0 at n_f = 33/4 | PHYS-32 |

Note: `gap_CD` is an alias for DATA-4's `gap_VL`. Both names refer to Fraction(38, 27). See Section N (Name Mappings).

---

### 7. SECTION D: SM BETA COEFFICIENTS (Level 1)

Inherited from DATA-4 N1–N3. Unchanged.

| Variable | Value | DATA-4 ID | Fraction |
|---|---|---|---|
| b1_SM | 41/10 | N1 | Fraction(41, 10) |
| b2_SM | −19/6 | N2 | Fraction(-19, 6) |
| b3_SM | −7 | N3 | Fraction(-7, 1) |

---

### 8. SECTION E: CD BETA COEFFICIENTS (Level 1)

Inherited from DATA-4 N4–N9. Unchanged.

| Variable | Value | DATA-4 ID | Fraction |
|---|---|---|---|
| db1_VL | 1/15 | N4 | Fraction(1, 15) |
| db2_VL | 1 | N5 | Fraction(1, 1) |
| db3_VL | 1/3 | N6 | Fraction(1, 3) |
| b1_mod | 25/6 | N7 | Fraction(25, 6) |
| b2_mod | −13/6 | N8 | Fraction(-13, 6) |
| b3_mod | −20/3 | N9 | Fraction(-20, 3) |

**The Dynkin formulas for any (R₃, R₂, Y) VL pair:**

```
Δb₁ = (2/5) × dim(R₃) × dim(R₂) × Y²
Δb₂ = (2/3) × dim(R₃) × S₂(R₂)
Δb₃ = (1/3) × dim(R₂) × S₂(R₃)
```

Coefficients: 2/5 for U(1), 2/3 for SU(2), 1/3 for SU(3). These are the COMPLETE VL pair contributions, not per-Weyl.

---

### 9. SECTION F: TWO-LOOP MATRICES (Level 1)

**SM b_ij matrix (DATA-4 N14, inherited):**

```
b_ij_SM = [
    [199/50,  27/10,  44/5],
    [9/10,    35/6,   12  ],
    [11/10,   9/2,   −26  ],
]
```

**VL db_ij matrix (NEW — from PHYS-28, 11/11 checks):**

| Entry | Fraction | Formula | PHYS-28 check |
|---|---|---|---|
| db₁₁ | 7/15 | (10/3)×S₁×(C₂(3)+C₂(2)+k₁Y²) | EXACT |
| db₁₂ | 1/15 | (4/3)×S₁×C₂(2) | EXACT |
| db₁₃ | 16/135 | (4/3)×S₁×C₂(3) | EXACT |
| db₂₁ | 1/30 | (4/3)×S₂(2)×d₃×k₁Y² | EXACT |
| db₂₂ | 15/4 | (10/3)×S₂(2)×d₃×C₂(2) | EXACT |
| db₂₃ | 8/3 | (4/3)×S₂(2)×d₃×C₂(3) | EXACT |
| db₃₁ | 1/45 | (4/3)×S₂(3)×d₂×k₁Y² | EXACT |
| db₃₂ | 1 | (4/3)×S₂(3)×d₂×C₂(2) | EXACT |
| db₃₃ | 40/9 | (10/3)×S₂(3)×d₂×C₂(3) | EXACT |

**CRITICAL CONVENTION (Pitfall N3):** The diagonal uses (10/3)×S×d×C_R(fund), the FERMION-ONLY Machacek-Vaughn piece. NOT 2×C_G + (10/3)×C_R. The 2×C_G gauge self-coupling is already in SM b_ij. Wrong: db₂₂ = 39/4. Correct: db₂₂ = 15/4.

**Full combined matrix (NEW):**

```
b_ij_full[i][j] = b_ij_SM[i][j] + db_ij_VL[i][j]
```

All 9 entries stored as Fractions.

---

### 10. SECTION G: GROUP THEORY (Level 1)

| Variable | Value | Fraction | Meaning |
|---|---|---|---|
| C2_adj_SU3 | 3 | Fraction(3) | Adjoint Casimir of SU(3) = N |
| C2_adj_SU2 | 2 | Fraction(2) | Adjoint Casimir of SU(2) = N |
| C2_fund_SU3 | 4/3 | Fraction(4, 3) | Fundamental Casimir (N²−1)/(2N) |
| C2_fund_SU2 | 3/4 | Fraction(3, 4) | Fundamental Casimir (N²−1)/(2N) |
| S2_fund | 1/2 | Fraction(1, 2) | Dynkin index of fundamental (any SU(N)) |
| dim_fund_SU3 | 3 | Fraction(3) | Dimension of fundamental SU(3) |
| dim_fund_SU2 | 2 | Fraction(2) | Dimension of fundamental SU(2) |
| Y_CD | 1/6 | Fraction(1, 6) | Hypercharge of the CD |
| Y2_CD | 1/36 | Fraction(1, 36) | Y² for the CD |
| S1_VL | 1/15 | Fraction(1, 15) | Effective U(1) Dynkin: (2/5)×3×2×(1/36) |
| N_gen | 3 | Fraction(3) | Number of fermion generations |

---

### 11. SECTION H: DECOMPOSITION DATA (Level 1)

**SU(3) decomposition (PHYS-32, 14/14 ALL EXACT):**

| Variable | Value | Fraction | Source |
|---|---|---|---|
| b3_gauge | −11 | Fraction(-11) | −(11/3)×C₂(adj SU(3)) |
| b3_fermion_per_gen | 4/3 | Fraction(4, 3) | 4 Weyl triplets × (2/3)×S₂ |
| b3_fermion_SM | 4 | Fraction(4) | 3 × 4/3 |
| b3_higgs | 0 | Fraction(0) | SU(3) singlet |
| b3_numerator | −20 | Fraction(-20) | −33 + 12 + 0 + 1 |

**SU(2) decomposition (PHYS-32 cross-check):**

| Variable | Value | Fraction | Source |
|---|---|---|---|
| b2_gauge | −22/3 | Fraction(-22, 3) | −(11/3)×C₂(adj SU(2)) |
| b2_fermion_SM | 4 | Fraction(4) | 3 gen × 4 Weyl doublets × (2/3)×S₂ |
| b2_higgs | 1/6 | Fraction(1, 6) | (1/3)×S₂(fund SU(2)) |
| b2_numerator | −19 | Fraction(-19) | −44 + 24 + 1 |

---

### 12. SECTION I: THRESHOLD DATA (Level 1 + Level 2)

**GUT threshold coefficients (PHYS-29, 10/11, 1 abort):**

| Variable | Value | Fraction | Level |
|---|---|---|---|
| C_T | −1/12 | Fraction(-1, 12) | 1 |
| C_Sigma | −1/6 | Fraction(-1, 6) | 1 |
| C_total | −1/4 | Fraction(-1, 4) | 1 |
| db1_T | 1/15 | Fraction(1, 15) | 1 |
| db2_T | 0 | Fraction(0) | 1 |
| db3_T | 1/12 | Fraction(1, 12) | 1 |
| db2_Sigma3 | 1/3 | Fraction(1, 3) | 1 |
| db3_Sigma8 | 1/2 | Fraction(1, 2) | 1 |

**No-threshold advantage (PHYS-35, 9/10, 1 informative FAIL):**

| Variable | Value | Type | Note |
|---|---|---|---|
| no_thresh_advantage_ratio | 12.3 | float | No-threshold / M_VL=500 miss ratio |
| no_thresh_persists_at_2000_steps | True | bool | Ratio unchanged at 2000 Euler steps |

---

### 13. SECTION J: PREDICTIONS (Level 2 — computed from Level 1 + Level 2 inputs)

**α_s predictions (PHYS-30, 9/9):**

| Variable | Value | Method | Miss from measured |
|---|---|---|---|
| alpha_s_1L_no_thresh | 0.10769 | One-loop, CD betas from M_Z | 8.74% |
| alpha_s_2L_SM_no_thresh | 0.11753 | Two-loop SM b_ij, no threshold | 0.397% |
| alpha_s_2L_full_no_thresh | 0.11838 | Two-loop full b_ij, no threshold | 0.325% |
| alpha_s_2L_full_thresh500 | 0.11211 | Two-loop full b_ij, M_VL=500 | 4.99% |

**sin²θ_W predictions (PHYS-27, PHYS-34):**

| Variable | Value | Method | Miss from measured |
|---|---|---|---|
| sin2_1L_no_thresh | 0.22845 | One-loop, no threshold | 1.199% |
| sin2_2L_SM_no_thresh | 0.23108 | Two-loop SM b_ij | 0.060% |
| sin2_2L_full_no_thresh | 0.23133 | Two-loop full b_ij | 0.048% |

**Two-loop Delta values (DATA-4 N15–N17 + PHYS-28 extensions):**

| Variable | Value | DATA-4 ID | Source |
|---|---|---|---|
| delta_1loop_500 | −1.17 | N15 | DATA-4 |
| delta_2loop_500 | −0.40 | N16 | DATA-4 |
| delta_2L_SM_bij | −0.490 | — | PHYS-28 Scenario B |
| delta_2L_full_bij | −0.436 | — | PHYS-28 Scenario C |

**Koide prediction (PHYS-33, 8/8):**

| Variable | Value | Method |
|---|---|---|
| m_tau_pred_koide | 1776.969 MeV | Quadratic from (m_e, m_mu) + K=2/3 |
| m_tau_other_root | 3.317 MeV | Second quadratic root |
| m_tau_miss_pct | 0.006 | Percentage miss from measured |

---

### 14. SECTION K: KOIDE DATA (Level 1 identity + Level 2 values)

Extends DATA-4 K section (K1–K8 inherited).

| Variable | Value | DATA-4 ID | Level | Source |
|---|---|---|---|---|
| K_koide | 0.6666605115 | K8 | 2 | DATA-4 inherited |
| a2_lep | 1.9999630688 | — | 2 | 2×(3K−1), PHYS-24/33 |
| a2_down | 2.3877 | — | 2 | PHYS-24 |
| a2_up | 3.0928 | — | 2 | PHYS-24 |
| M_koide | 17.716 MeV^(1/2) | — | 2 | sum_sqrt/3, PHYS-33 |
| theta_koide | 2.317 rad | — | 2 | arccos((√m_e/M−1)/a), PHYS-33 |

**The identity (Level 1):** K = (1 + a²/2)/3. At a² = 2: K = 2/3.

**The quadratic (Level 1):** x² − 4sx + (3S − 2s²) = 0 where s = √m_e + √m_mu, S = m_e + m_mu, x = √m_tau.

---

### 15. SECTION L: DERIVATION FUNCTIONS

Each function includes inline documentation of the derivation chain, sign convention, and pitfalls. All use Fraction/mpf arithmetic (no `import math`, no floats in the computation chain).

**L1. derive_inv_a1_a2(alpha_inv_frac, sin2_tW_frac)**
Returns (inv_a1, inv_a2) as Fractions.
Pitfall N1: multiply, not divide.

**L2. run_one_loop(inv_a_start, betas, L)**
Returns list of 3 mpf. Sign: 1/α_i(μ) = 1/α_i(μ₀) − bᵢ × L.
Pitfall N2: minus sign.

**L3. find_crossing_L(inv_a1, inv_a2, b1, b2)**
Returns L as mpf. L = (1/α₁ − 1/α₂)/(b₁ − b₂).

**L4. run_two_loop_euler_exact(inv_a_start, b1loop, bij, L_total, n_steps)**
Euler integration using mpf at working precision. Slow but exact to 100 dps.
d(1/αᵢ)/dL = −bᵢ − Σⱼ bᵢⱼ × αⱼ/(4π). Both terms negative.
Pitfall N2: sign convention.

**L5. compute_vl_bij(C2_3, C2_2, S2_3, S2_2, d3, d2, Y, k1)**
Returns 3×3 list of Fractions. Diagonal: (10/3)×S×d×C_R. Off-diagonal: (4/3)×S×d×C_other.
Pitfall N3: diagonal is fermion-only, not full MV.

**L6. predict_alpha_s(inv_a1, inv_a2, b1loop, bij, n_steps)**
Full prediction chain: find crossing → run back → extract α_s.
Uses L4 (exact Euler). Returns (alpha_s_pred, Delta, L_GUT).

**L7. predict_sin2_tW(alpha_inv_f, alpha_s_f, b1loop, bij, n_steps)**
Full prediction chain: b_EM crossing → run back → extract sin²θ_W.
Pitfall N1: sin²θ_W = (1/α₂)/(1/α_EM), not the inverse.

---

### 16. SEPARATE FILE: data5_fast.py

Float-speed utility functions for scanning and Monte Carlo. NOT in the main library. Scripts import explicitly: `from data5_fast import run_two_loop_euler_fast`.

```python
import math

def run_two_loop_euler_fast(inv_a_start, b1loop, bij, L_total, n_steps):
    """Float Euler for speed. ~4-5 digit accuracy. For scanning only."""
    ...

def scan_pool_fast(pool, targets):
    """Float formula scan for Monte Carlo. From PHYS-31."""
    ...
```

The `import math` ban (script rules Section 16) applies to the main library and to PHYS scripts. data5_fast.py is a clearly marked speed-utility that scripts import when they need performance. The separation makes the violation explicit and contained.

---

### 17. SECTION M: PITFALL DOCUMENTATION

| # | Pitfall | Wrong | Right | Paper | Iteration |
|---|---|---|---|---|---|
| N1 | 1/α₂ from sin²θ_W | divide: 593 | multiply: 31.7 | PHYS-30 | 1 |
| N2 | Sign of running | +b×L (diverge) | −b×L (converge) | PHYS-28 | 1–3 |
| N3 | VL diagonal coefficient | 2C_G+(10/3)C_R = 39/4 | (10/3)C_R = 15/4 | PHYS-28 | 2 |
| N4 | GUT threshold target | 1-loop Δ = −1.17 | 2-loop Δ = −0.40 | PHYS-29 | 1–2 |
| N5 | Euler with mpf speed | Hangs at 10,000 trials | Python float (data5_fast) | PHYS-31 | 1 |
| N6 | Monte Carlo scan speed | mpf scan (hangs) | Float + early exit | PHYS-31 | 1 |
| N7 | Koide K convention | K = (sum_sqrt)²/(3×sum_m) = 0.5 | K = sum_m/(sum_sqrt)² = 0.667 | PHYS-33 | 1 |
| N8 | Koide a² extraction | a² = 2(1/K−1) with wrong K | a² = 2(3K−1) with correct K | PHYS-33 | 1 |
| N9 | Soft threshold function | ln(1+(μ/M)²)/norm → 30% miss | 1/(1+(M/μ)²) → 7% miss | PHYS-35 | 1 |
| N10 | Bounding box balloon | Text at y = −7 → 11,000px | All text inside axis limits | PHYS-30 diag | 1 |
| N11 | Dict key vs list index | counts[s] where s = score | counts[i] where i = loop index | PHYS-31 diag | 1 |
| N12 | Weyl counting for VL | 4 Weyl → Δb₃ = 4/3 | VL formula → Δb₃ = 1/3 | PHYS-32 | noted |

---

### 18. SECTION N: NAME MAPPINGS

| Session 4 name | phys24_lib name | DATA-4 ID | Note |
|---|---|---|---|
| gap_CD | gap_VL | N11 | Same value: Fraction(38, 27) |
| Cabibbo Doublet (CD) | VL (vector-like) | — | Named entity |
| Track A | — | — | Gauge coupling unification program (PHYS-26–30) |
| Track B | — | — | Cosmological formulas (PARKED by PHYS-31) |
| Track C | — | — | Structure papers (PHYS-32 forward) |
| b_ij_full | — | — | b_ij_SM + db_ij_VL |
| b_EM_CD | — | — | (5/3)b₁' + b₂' = 43/9 |

---

### 19. THE INTEGER MAP (Verified Track A only)

Every integer in the verified computation chain, its origin, and connections.

| Integer | Appears in | Origin | Connects to |
|---|---|---|---|
| 3 | N_gen, C₂(adj SU(3)), dim(fund SU(3)), k₁ num | SU(3) structure, generation count | Unification, Koide, sin²θ_W=3/13 |
| 4 | b₃_fermion, b₂_fermion | 4 Weyl triplets per gen, 4 Weyl doublets per gen | Beta decomposition |
| 5 | k₁ denom (k₁=3/5) | SU(5) embedding | GUT normalization |
| 6 | Common beta denom | LCM of representation fractions | All CD betas |
| 7 | b₃_SM = −7 | 11 − 4 = 7 | Asymptotic freedom |
| 8 | 8/3 in SU(5) crossing | 5/3 + 1 = 8/3 | sin²θ_W prediction method |
| 10 | b₁_SM denom (41/10) | U(1) representation LCM | U(1) running |
| 11 | Gauge self-coupling (11/3)×N | Yang-Mills one-loop | All gauge betas, AF |
| 13 | b₂' numerator (\|−13/6\|) | −44+24+1=−19, then +6=−13 with CD | Gap ratio, α_s running |
| 15 | Δb₁ denom (1/15), db₂₂ num (15/4) | 3×5 from dim(SU(3))×k₁ denom | Two-loop diagonal |
| 19 | b₂_SM numerator (\|−19/6\|) | −44+24+1=−19 | SM SU(2) running |
| 20 | b₃' numerator (\|−20/3\|) | −33+12+0+1=−20 | SU(3) running, gap denominator |
| 25 | b₁' numerator (25/6) | U(1) hypercharge sum with CD | U(1) running |
| 27 | Gap denom (38/27) | b₂'−b₃'=27/6 | Unification test |
| 33 | b₃ gauge × 3 | 11×3 | SU(3) decomposition numerator |
| 38 | Gap numerator (38/27) | b₁'−b₂'=38/6 | Unification test |
| 41 | b₁_SM numerator (41/10) | U(1) hypercharge sum | U(1) running |
| 43 | b_EM numerator (43/9) | (125−39)/18 = 43/9 | EM running, sin²θ_W |

---

### 20. THE DERIVATION CHAIN

```
MEASURED INPUTS (Level 2, from DATA-4):
  α_EM = 1/137.036   (B1)
  sin²θ_W = 0.23122  (B11)
  α_s = 0.1180       (B12)
  m_e, m_mu, m_tau    (B2, B3, B4)

FRAMEWORK INPUTS (Level 1, from DATA-4 + Session 4):
  SU(5) embedding → k₁ = 3/5 (PHYS-26)
  CD (3,2,1/6) → Δb₁=1/15, Δb₂=1, Δb₃=1/3 (N4–N6)
  SM betas → b₁=41/10, b₂=−19/6, b₃=−7 (N1–N3)
  Modified → b₁'=25/6, b₂'=−13/6, b₃'=−20/3 (N7–N9)
  SM b_ij → 3×3 matrix (N14)
  VL db_ij → 9 Fractions (PHYS-28)
  Full b_ij = SM + VL (PHYS-28)
  Koide identity: K = (1+a²/2)/3 (PHYS-8)

DERIVATION CHAIN:
  1. α_EM + sin²θ_W → 1/α₁, 1/α₂     [L1: derive_inv_a1_a2]
     PITFALL N1: multiply not divide

  2. b₁', b₂' → L_GUT                   [L3: find_crossing_L]
     PITFALL N2: sign convention −b×L

  3. Two-loop Euler → Δ at M_GUT         [L4: run_two_loop_euler_exact]
     PITFALL N3: diagonal coefficient

  4. Run back → α_s = 0.11838 (0.33%)    [L6: predict_alpha_s]

  5. Or: α_EM + α_s → sin²θ_W = 0.23133 (0.048%)  [L7: predict_sin2_tW]
     Uses b_EM = 43/9

  6. m_e + m_mu + K=2/3 → m_tau = 1776.97 MeV (0.006%)
     PITFALL N7, N8: K convention

PARAMETER COUNT:
  Koide (m_tau derived): 19 → 18
  θ_QCD = 0:            18 → 17
  α_s from unification:  17 → 16
```

---

### 21. THE SOLITON BOUNDARY MAP (M_Z to M_GUT, verified)

```
M_Z = 91.2 GeV      Three gauge configs: SU(3)×SU(2)×U(1)
  │                  b₁' = 25/6, b₂' = −13/6, b₃' = −20/3
  │                  (No-threshold: CD betas from here)
  │
  │  CD BOUNDARY (M_VL ~ 200–6000 GeV)
  │  PHYS-35: step-function threshold is 12× worse
  │  CD vortex geometric overlaps persist at all scales
  │  No-threshold gives α_s miss 0.33%, threshold gives 4%
  │
  │  Couplings converge:
  │  1/α₁ decreases (b₁' > 0)
  │  1/α₂ increases (b₂' < 0)
  │  1/α₃ increases (b₃' < 0)
  │
M_GUT ~ 4×10¹⁵ GeV  1/α₁ = 1/α₂ = 1/α_GUT ≈ 42
                     Δ = 1/α₃ − 1/α_GUT ≈ −0.04 (no-thresh)
                     Heavy vortexes: X,Y bosons, triplet Higgs, Sigma
                     C_total = −1/4 (threshold coefficient)
                     Minimal SU(5) disfavored: M_X/M = 23,228
```

---

### 22. TEST SUITE SPECIFICATION

**data5_test.py** runs all checks:

| Block | Description | Checks |
|---|---|---|
| T1 | All phys24_lib values present and identical | ~148 |
| T2 | All DATA-4 Group G checks (gap ratios, modified betas) | 6 |
| T3 | New derived constants (k₁, sin2_tree, corrections, b_EM) | ~8 |
| T4 | Group theory constants | ~10 |
| T5 | Beta decomposition pieces (SU(3), SU(2)) | ~12 |
| T6 | VL db_ij (9 Fractions) | 9 |
| T7 | Full b_ij = SM + VL | 9 |
| T8 | Threshold coefficients | ~6 |
| T9 | Derivation functions reproduce script outputs | ~20 |
| T10 | Pitfall tests (wrong ≠ right for each pitfall) | ~12 |
| T11 | Koide values and quadratic | ~8 |
| T12 | Prediction values match PHYS-30/34 outputs | ~6 |
| **Total** | | **~254** |

Target: 254/254 PASS.

---

### 23. WHAT DATA-5 DOES NOT CONTAIN

- No physics assertions (does not claim CD exists or unification is real)
- No statistical interpretation strings ("PARKED," "PROMOTED")
- No Track B cosmological formula connections (parked by PHYS-31)
- No Planck-scale speculation
- No diagram scripts or paper text
- No `import math` in the main library
- No float arithmetic in the main library computation chain
- No renumbered DATA-4 entry IDs
- No measured constants that differ from DATA-4

---

*End of DATA-5 Technical Specification v2. This document supersedes v1. All corrections from the bijection map are applied. Every value traces to DATA-4 or to a verified Session 4 script. The test suite targets 254 checks. The API inherits phys24_lib unchanged and adds Session 4 values, functions, and pitfall documentation.*
