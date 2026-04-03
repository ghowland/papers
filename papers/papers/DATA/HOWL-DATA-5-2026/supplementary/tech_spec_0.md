## DATA-5 Technical Specification

**Registry:** [@HOWL-DATA-5-2026]
**Date:** April 3 2026
**Purpose:** Complete data platform for Sessions 4+, replacing phys24_lib as the computational foundation
**Predecessor:** phys24_lib.py (21/21 self-test, 148/148 platform test)

---

### 1. WHAT DATA-5 IS

DATA-5 is a Python library (data5.py) and test suite (data5_test.py) that contains every verified number, every derivation chain, every documented pitfall, and every helper function accumulated through PHYS-25 to PHYS-35. It extends phys24_lib — every value in phys24_lib appears in DATA-5 unchanged. New values, derivation functions, and documented conventions are added.

DATA-5 is NOT a physics paper. It does not assert physics claims. It stores data about physics things. A future session imports DATA-5 and has the complete computational platform without reading any PHYS paper.

---

### 2. STRUCTURE

```
data5.py                 # The library
data5_test.py            # The test suite (~250 checks)
```

**Sections in data5.py:**

```
A. INFRASTRUCTURE        # mp.dps, imports, helper functions
B. MEASURED CONSTANTS     # From DATA-4, all Level 2
C. DERIVED CONSTANTS      # Exact Fractions, all Level 1
D. SM BETA COEFFICIENTS   # One-loop, exact Fractions
E. CD BETA COEFFICIENTS   # One-loop, exact Fractions
F. TWO-LOOP MATRICES      # SM b_ij, VL db_ij, full b_ij
G. GROUP THEORY           # Casimirs, Dynkin indices, dimensions
H. DECOMPOSITION DATA     # Per-constituent pieces of each beta
I. THRESHOLD DATA         # GUT threshold coefficients
J. PREDICTIONS            # Values computed by the series
K. KOIDE DATA             # Lepton mass relations
L. STATISTICAL RESULTS    # PHYS-31 Monte Carlo outcomes
M. DERIVATION FUNCTIONS   # How to compute from inputs
N. PITFALL DOCUMENTATION  # What goes wrong and why
O. NAME MAPPINGS          # Aliases, series terminology
```

---

### 3. SECTION A: INFRASTRUCTURE

Unchanged from phys24_lib:

```python
from fractions import Fraction
from mpmath import mp, mpf, nstr
mp.dps = 100

def f2m(frac):
    """Fraction to mpf at working precision."""
    return mpf(frac.numerator) / mpf(frac.denominator)

def digits_of(got, expected):
    ...

def show(label, value):
    ...

def chk(tag, got, expected, need, checks):
    ...

def chk_exact(tag, got, expected, checks):
    ...

def chk_bool(tag, condition, detail, checks):
    ...

def chk_precision(tag, frac, pub_str, need, checks):
    ...

def precision_report(frac, pub_str):
    ...

def count_sig_digits(s):
    ...

def print_summary(checks):
    ...
```

All helper signatures unchanged. API only grows.

---

### 4. SECTION B: MEASURED CONSTANTS (Level 2)

Every value from DATA-4, carried forward from phys24_lib. Source: PDG 2022 via DATA-3 (32/32 verified).

| Variable | Value | Unit | DATA-4 Entry | Description |
|---|---|---|---|---|
| alpha_inv | 137.035999177 (as Q335 Fraction) | dimensionless | B1 | 1/α_EM at M_Z |
| alpha_s | 0.1180 (as Fraction) | dimensionless | B2 | Strong coupling at M_Z |
| sin2_tW | 0.23122 (as Fraction) | dimensionless | B3 | Weak mixing angle at M_Z |
| M_Z | 91187.6 (as Fraction) | MeV | B7 | Z boson mass |
| m_e | 0.51099895069 (as Q335 Fraction) | MeV | B4 | Electron mass |
| m_mu | 105.6583755 (as Q335 Fraction) | MeV | B5 | Muon mass |
| m_tau | 1776.86 (as Q335 Fraction) | MeV | B6 | Tau mass |
| m_u | 2.16 (as Fraction) | MeV | C1 | Up quark mass |
| m_d | 4.67 (as Fraction) | MeV | C2 | Down quark mass |
| m_s | 93.4 (as Fraction) | MeV | C3 | Strange quark mass |
| m_c | 1275 (as Fraction) | MeV | C4 | Charm quark mass |
| m_b | 4180 (as Fraction) | MeV | C5 | Bottom quark mass |
| m_t | 172760 (as Fraction) | MeV | C6 | Top quark mass |
| G_F | 1.1663788e-5 (as Q335 Fraction) | GeV⁻² | B8 | Fermi constant |
| M_W | 80379 (as Fraction) | MeV | B9 | W boson mass |
| m_H | 125250 (as Fraction) | MeV | B10 | Higgs mass |

Plus all additional DATA-4 entries already in phys24_lib. Every value has a `_full` variant for maximum available precision.

---

### 5. SECTION C: DERIVED CONSTANTS (Level 1)

Exact Fractions computed from the framework. These are mathematical consequences of the gauge group structure.

| Variable | Value | Fraction | Derivation | Paper |
|---|---|---|---|---|
| k1 | 3/5 | Fraction(3, 5) | SU(5) normalization: Tr(T₃²)/Tr(Y²) | PHYS-26 |
| k1_inv | 5/3 | Fraction(5, 3) | 1/k₁, the GUT normalization multiplier | PHYS-26 |
| gap_SM | 218/115 | Fraction(218, 115) | (b₁_SM − b₂_SM)/(b₂_SM − b₃_SM) | PHYS-13 |
| gap_CD | 38/27 | Fraction(38, 27) | (b₁' − b₂')/(b₂' − b₃') | PHYS-13 |
| gap_MSSM | 7/5 | Fraction(7, 5) | MSSM gap ratio (convention check) | PHYS-26 |
| sin2_tree | 3/8 | Fraction(3, 8) | GUT tree-level sin²θ_W | PHYS-27 |
| sin2_3_13 | 3/13 | Fraction(3, 13) | N_gen/\|b₂' numerator\| | PHYS-27 |
| correction_exact | 15/104 | Fraction(15, 104) | 3/8 − 3/13 = exact running correction | PHYS-27 |
| b_EM_CD | 43/9 | Fraction(43, 9) | (5/3)b₁' + b₂', EM beta combination | PHYS-34 |

---

### 6. SECTION D: SM BETA COEFFICIENTS (Level 1)

One-loop beta coefficients for the Standard Model with 3 generations and 1 Higgs doublet.

| Variable | Value | Fraction | Decomposition (over common denom) | Paper |
|---|---|---|---|---|
| b1_SM | 41/10 | Fraction(41, 10) | U(1): fermion + Higgs, no gauge (abelian) | PHYS-26 |
| b2_SM | −19/6 | Fraction(-19, 6) | SU(2): (−44 + 24 + 1)/6, gauge + fermion + Higgs | PHYS-32 |
| b3_SM | −7 | Fraction(-7, 1) | SU(3): (−33 + 12 + 0)/3, gauge + fermion + Higgs(0) | PHYS-32 |

---

### 7. SECTION E: CD BETA COEFFICIENTS (Level 1)

Modified betas with the Cabibbo Doublet (3,2,1/6) vector-like pair.

| Variable | Value | Fraction | How computed | Paper |
|---|---|---|---|---|
| db1_VL | 1/15 | Fraction(1, 15) | (2/5)×3×2×(1/6)² = (2/5)×(1/6) = 1/15 | PHYS-26 |
| db2_VL | 1 | Fraction(1, 1) | (2/3)×3×(1/2) = 1 | PHYS-26 |
| db3_VL | 1/3 | Fraction(1, 3) | (1/3)×2×(1/2) = 1/3 | PHYS-26/32 |
| b1_mod | 25/6 | Fraction(25, 6) | b₁_SM + Δb₁ = 41/10 + 1/15 = 25/6 | PHYS-26 |
| b2_mod | −13/6 | Fraction(-13, 6) | b₂_SM + Δb₂ = −19/6 + 1 = −13/6 | PHYS-26 |
| b3_mod | −20/3 | Fraction(-20, 3) | b₃_SM + Δb₃ = −7 + 1/3 = −20/3 | PHYS-26/32 |

**The Dynkin formulas (general, for any (R₃, R₂, Y) VL pair):**

```python
# Δb₁ = (2/5) × dim(R₃) × dim(R₂) × Y²
# Δb₂ = (2/3) × dim(R₃) × S₂(R₂)
# Δb₃ = (1/3) × dim(R₂) × S₂(R₃)
# Coefficients: 2/5 for U(1), 2/3 for SU(2), 1/3 for SU(3)
# These are the COMPLETE VL pair contributions, not per-Weyl
```

---

### 8. SECTION F: TWO-LOOP MATRICES (Level 1)

**The VL two-loop contribution db_ij_VL (9 exact Fractions):**

| Entry | Fraction | Decimal | Formula | Paper |
|---|---|---|---|---|
| db₁₁ | 7/15 | 0.4667 | (10/3)×S₁×(C₂(3)+C₂(2)+k₁Y²) | PHYS-28 |
| db₁₂ | 1/15 | 0.0667 | (4/3)×S₁×C₂(2) | PHYS-28 |
| db₁₃ | 16/135 | 0.1185 | (4/3)×S₁×C₂(3) | PHYS-28 |
| db₂₁ | 1/30 | 0.0333 | (4/3)×S₂(2)×d₃×k₁Y² | PHYS-28 |
| db₂₂ | 15/4 | 3.75 | (10/3)×S₂(2)×d₃×C₂(2) | PHYS-28 |
| db₂₃ | 8/3 | 2.6667 | (4/3)×S₂(2)×d₃×C₂(3) | PHYS-28 |
| db₃₁ | 1/45 | 0.0222 | (4/3)×S₂(3)×d₂×k₁Y² | PHYS-28 |
| db₃₂ | 1 | 1.0 | (4/3)×S₂(3)×d₂×C₂(2) | PHYS-28 |
| db₃₃ | 40/9 | 4.4444 | (10/3)×S₂(3)×d₂×C₂(3) | PHYS-28 |

**CRITICAL CONVENTION:** The diagonal formula uses (10/3)×S×d×C_R(fund), the FERMION-ONLY piece. NOT (2×C_G + (10/3)×C_R) which includes the gauge self-coupling already in SM b_ij. Using the full MV diagonal gives db₂₂ = 39/4 (WRONG). Correct: db₂₂ = 15/4.

**The SM b_ij matrix:** Stored as `b_ij_SM`, a 3×3 list of Fractions from the standard two-loop SM result.

**The full combined matrix:** `b_ij_full[i][j] = b_ij_SM[i][j] + db_ij_VL[i][j]`

---

### 9. SECTION G: GROUP THEORY (Level 1)

| Variable | Value | Fraction | Meaning | Used in |
|---|---|---|---|---|
| C2_adj_SU3 | 3 | Fraction(3) | Adjoint Casimir of SU(3) = N | PHYS-32 |
| C2_adj_SU2 | 2 | Fraction(2) | Adjoint Casimir of SU(2) = N | PHYS-32 |
| C2_fund_SU3 | 4/3 | Fraction(4, 3) | Fundamental Casimir (N²−1)/(2N) | PHYS-28 |
| C2_fund_SU2 | 3/4 | Fraction(3, 4) | Fundamental Casimir (N²−1)/(2N) | PHYS-28 |
| S2_fund | 1/2 | Fraction(1, 2) | Dynkin index of fundamental rep (any SU(N)) | PHYS-26/28/32 |
| dim_fund_SU3 | 3 | Fraction(3) | Dimension of fundamental SU(3) | PHYS-26 |
| dim_fund_SU2 | 2 | Fraction(2) | Dimension of fundamental SU(2) | PHYS-26 |
| Y_CD | 1/6 | Fraction(1, 6) | Hypercharge of the CD | PHYS-26 |
| Y2_CD | 1/36 | Fraction(1, 36) | Y² for the CD | PHYS-26 |
| S1_VL | 1/15 | Fraction(1, 15) | Effective U(1) Dynkin: (2/5)×3×2×(1/36) | PHYS-28 |
| N_gen | 3 | Fraction(3) | Number of fermion generations | PHYS-26 |
| n_f_SM | 6 | Fraction(6) | Number of quark flavors in SM | PHYS-32 |
| n_f_crit_SU3 | 33/4 | Fraction(33, 4) | Critical flavor number for AF: b₃=0 at n_f=33/4 | PHYS-32 |

---

### 10. SECTION H: DECOMPOSITION DATA (Level 1)

**SU(3) beta decomposition (PHYS-32):**

| Variable | Value | Fraction | Source |
|---|---|---|---|
| b3_gauge | −11 | Fraction(-11) | −(11/3)×C₂(adj SU(3)) = −(11/3)×3 |
| b3_fermion_per_gen | 4/3 | Fraction(4, 3) | 4 Weyl triplets × (2/3)×S₂ |
| b3_fermion_SM | 4 | Fraction(4) | 3 generations × 4/3 |
| b3_higgs | 0 | Fraction(0) | Higgs is SU(3) singlet |
| b3_cd | 1/3 | Fraction(1, 3) | VL Dynkin formula |
| b3_numerator | −20 | Fraction(-20) | −33 + 12 + 0 + 1 = −20 |

**SU(2) beta decomposition (PHYS-32 cross-check):**

| Variable | Value | Fraction | Source |
|---|---|---|---|
| b2_gauge | −22/3 | Fraction(-22, 3) | −(11/3)×C₂(adj SU(2)) = −(11/3)×2 |
| b2_fermion_SM | 4 | Fraction(4) | 3 gen × 4 Weyl doublets × (2/3)×S₂ |
| b2_higgs | 1/6 | Fraction(1, 6) | (1/3)×S₂(fund SU(2)) |
| b2_numerator | −19 | Fraction(-19) | −44 + 24 + 1 = −19 |

**Per-generation Weyl census for SU(3) (PHYS-32):**

| Multiplet | SU(3) rep | Weyl count | Contribution to b₃ |
|---|---|---|---|
| Q_L(3,2,1/6) | triplet | 2 (doublet) | 2/3 |
| u_R(3,1,2/3) | triplet | 1 | 1/3 |
| d_R(3,1,−1/3) | triplet | 1 | 1/3 |
| L_L(1,2,−1/2) | singlet | 0 colored | 0 |
| e_R(1,1,−1) | singlet | 0 colored | 0 |
| **Per gen total** | | **4 Weyl** | **4/3** |

---

### 11. SECTION I: THRESHOLD DATA (Level 1 + Level 2)

**GUT threshold coefficients (PHYS-29):**

| Variable | Value | Fraction | Source | Level |
|---|---|---|---|---|
| C_T | −1/12 | Fraction(-1, 12) | Color triplet Higgs threshold coefficient | 1 |
| C_Sigma | −1/6 | Fraction(-1, 6) | Sigma_8 + Sigma_3 combined coefficient | 1 |
| C_total | −1/4 | Fraction(-1, 4) | C_T + C_Sigma | 1 |
| db1_T | 1/15 | Fraction(1, 15) | Triplet Higgs U(1) beta shift | 1 |
| db2_T | 0 | Fraction(0) | Triplet Higgs SU(2) beta shift (singlet) | 1 |
| db3_T | 1/12 | Fraction(1, 12) | Triplet Higgs SU(3) beta shift | 1 |
| db2_Sigma3 | 1/3 | Fraction(1, 3) | Sigma weak triplet SU(2) shift | 1 |
| db3_Sigma8 | 1/2 | Fraction(1, 2) | Sigma color octet SU(3) shift | 1 |
| M_X_over_M_min_SU5 | 23228 (approx) | — | Minimal SU(5) requires M_X/M = 23,228 | 2 |

**No-threshold finding (PHYS-35):**

| Variable | Value | Type | Source |
|---|---|---|---|
| no_thresh_advantage | 12.3 | float | No-threshold beats M_VL=500 by this factor |
| no_thresh_persists_at_2000 | True | bool | Advantage unchanged at 2000 Euler steps |
| no_thresh_conclusion | "PHYSICAL" | string | Not a numerical artifact |

---

### 12. SECTION J: PREDICTIONS (Level 2 — computed from Level 1 + Level 2 inputs)

**α_s prediction (PHYS-30):**

| Variable | Value | Method | Miss from measured | Paper |
|---|---|---|---|---|
| alpha_s_1L_no_thresh | 0.10769 | One-loop, no threshold | 8.74% | PHYS-30 |
| alpha_s_2L_SM_no_thresh | 0.11753 | Two-loop SM b_ij, no threshold | 0.397% | PHYS-30 |
| alpha_s_2L_full_no_thresh | 0.11838 | Two-loop full b_ij, no threshold | **0.325%** | PHYS-30 |
| alpha_s_2L_full_thresh500 | 0.11211 | Two-loop full b_ij, M_VL=500 | 4.99% | PHYS-30 |

**sin²θ_W prediction (PHYS-27, PHYS-34):**

| Variable | Value | Method | Miss from measured | Paper |
|---|---|---|---|---|
| sin2_1L_no_thresh | 0.22845 | One-loop, no threshold | 1.199% | PHYS-27 |
| sin2_2L_SM_no_thresh | 0.23108 | Two-loop SM b_ij | 0.060% | PHYS-34 |
| sin2_2L_full_no_thresh | 0.23133 | Two-loop full b_ij | **0.048%** | PHYS-34 |

**Ordering (PHYS-34):**
1-loop (0.22845) < 3/13 (0.23077) < measured (0.23122) < 2-loop (0.23133)
Two-loop overshoots 3/13. Overshoot within method uncertainty (0.048%).

---

### 13. SECTION K: KOIDE DATA (Level 1 identity + Level 2 values)

| Variable | Value | Level | Source | Paper |
|---|---|---|---|---|
| K_lep | 0.66666051 | 2 | sum_m / (sum_sqrt)² for leptons | PHYS-33 |
| K_target | 2/3 | 1 | Koide formula | PHYS-8 |
| a2_lep | 1.9999631 | 2 | 2×(3K−1) for leptons | PHYS-33 |
| a2_target | 2 | 1 (conditional) | K = 2/3 ⟺ a² = 2 | PHYS-8 |
| a2_down | 2.3877 | 2 | For (d, s, b) | PHYS-24 |
| a2_up | 3.0928 | 2 | For (u, c, t) | PHYS-24 |
| m_tau_pred | 1776.969 MeV | 2 (conditional on a²=2) | Quadratic from (m_e, m_mu) + K=2/3 | PHYS-33 |
| m_tau_miss | 0.006% | 2 | |m_tau_pred − m_tau_meas| / m_tau_meas | PHYS-33 |
| m_tau_other_root | 3.317 MeV | 2 | Second quadratic root | PHYS-33 |
| M_koide | 17.716 MeV^(1/2) | 2 | sum_sqrt / 3 | PHYS-33 |
| theta_koide | 2.317 rad | 2 | Phase from m_e extraction | PHYS-33 |

**The Koide identity (Level 1):** K = (1 + a²/2)/3. Proof: cosines at 120° sum to zero, cos² at 120° sum to 3/2. Independent of M and θ.

**The quadratic for m_tau (Level 1):** Given K = 2/3, s = √m_e + √m_mu, S = m_e + m_mu: x² − 4sx + (3S − 2s²) = 0 where x = √m_tau.

---

### 14. SECTION L: STATISTICAL RESULTS (Level 2)

| Variable | Value | Source | Paper |
|---|---|---|---|
| stat_p_value | 0.8128 | Monte Carlo, 10,000 trials | PHYS-31 |
| stat_beta_score | 6 | Beta pool hits out of 8 targets | PHYS-31 |
| stat_mean_random | 6.195 | Mean hits for random 15-integer pools | PHYS-31 |
| stat_std_random | 0.814 | Std of random scores | PHYS-31 |
| stat_beta_sigma | −0.24 | Beta pool at −0.24σ (below average) | PHYS-31 |
| track_B_status | "PARKED" | p ≥ 0.05, gate fires | PHYS-31 |

---

### 15. SECTION M: DERIVATION FUNCTIONS

These functions encode HOW to compute key values. Each includes inline documentation of the derivation chain, the sign convention, and the common errors.

**M1. Coupling extraction from measured inputs:**

```python
def derive_inv_a1_a2(alpha_inv_frac, sin2_tW_frac):
    """From α_EM and sin²θ_W, derive 1/α₁ and 1/α₂.
    
    DERIVATION:
      sin²θ_W = α_EM / α₂
      => 1/α₂ = sin²θ_W × (1/α_EM)     [MULTIPLY, not divide]
      => 1/α₁ = (3/5) × (1/α_EM − 1/α₂)
    
    PITFALL (PHYS-30 iteration 1):
      Wrong: 1/α₂ = (1/α_EM) / sin²θ_W = 137/0.231 = 593
      Right: 1/α₂ = sin²θ_W × (1/α_EM) = 0.231 × 137 = 31.7
      The wrong formula divides instead of multiplying.
      593 is garbage — it should be ~30.
    
    Returns: (inv_a1, inv_a2) as Fractions.
    """
    inv_a2 = sin2_tW_frac * alpha_inv_frac
    inv_a1 = Fraction(3, 5) * (alpha_inv_frac - inv_a2)
    return inv_a1, inv_a2
```

**M2. One-loop running:**

```python
def run_one_loop(inv_a_start, betas, L):
    """One-loop running: 1/α_i(μ) = 1/α_i(μ₀) − b_i × L.
    
    SIGN CONVENTION (PHYS-28 iterations 1–3):
      RGE: d(1/α_i)/d(ln μ) = −b_i/(2π)
      Therefore: 1/α_i(μ) = 1/α_i(μ₀) − b_i × L
      where L = ln(μ/μ₀)/(2π), L > 0 for μ > μ₀.
      
      The MINUS sign means:
        b > 0 (U(1)): 1/α₁ DECREASES running up → coupling GROWS
        b < 0 (SU(2), SU(3)): 1/α₂,₃ INCREASES running up → coupling SHRINKS
        => 1/α₁ and 1/α₂ CONVERGE at high energy (unification)
      
      PITFALL: Using +b×L instead of −b×L makes couplings DIVERGE.
    
    Args:
      inv_a_start: list of 3 mpf [1/α₁, 1/α₂, 1/α₃] at μ₀
      betas: list of 3 mpf [b₁, b₂, b₃]
      L: mpf, ln(μ/μ₀)/(2π), positive for running UP
    Returns: list of 3 mpf [1/α₁, 1/α₂, 1/α₃] at μ
    """
    return [inv_a_start[i] - betas[i] * L for i in range(3)]
```

**M3. GUT crossing finder:**

```python
def find_crossing_L(inv_a1, inv_a2, b1, b2):
    """Find L where 1/α₁ = 1/α₂ at one loop.
    
    DERIVATION:
      At crossing: 1/α₁ − b₁L = 1/α₂ − b₂L
      (1/α₁ − 1/α₂) = (b₁ − b₂)L
      L = (1/α₁ − 1/α₂) / (b₁ − b₂)
      
      Since 1/α₁ > 1/α₂ (63 > 31) and b₁ > b₂ (4.17 > −2.17):
      L = positive / positive = positive → crossing is ABOVE M_Z
      
    PITFALL: Wrong subtraction order gives negative L.
    
    Returns: L (mpf, positive means crossing above starting scale)
    """
    return (inv_a1 - inv_a2) / (b1 - b2)
```

**M4. Two-loop Euler integrator:**

```python
def run_two_loop_euler(inv_a_start, b1loop, bij, L_total, n_steps):
    """Euler integration of two-loop RGEs.
    
    EQUATION:
      d(1/α_i)/dL = −b_i − Σ_j b_ij × α_j / (4π)
      
      Both terms have MINUS signs.
      The second term uses α_j = 1/(1/α_j), computed at each step.
    
    PITFALL (PHYS-28): Wrong sign on two-loop term.
    PITFALL (PHYS-31): Using mpf at 100 dps makes this hang for
      10,000 trials. Use Python float for speed when 4-5 digits suffice.
    
    Args:
      inv_a_start: list of 3 float [1/α₁, 1/α₂, 1/α₃]
      b1loop: list of 3 float [b₁, b₂, b₃]
      bij: 3×3 list of float, two-loop matrix
      L_total: float, total L to integrate
      n_steps: int, number of Euler steps
    Returns: list of 3 float [1/α₁, 1/α₂, 1/α₃] at end
    """
    import math
    fourpi = 4.0 * math.pi
    inv_a = list(inv_a_start)
    dL = L_total / float(n_steps)
    for _ in range(n_steps):
        alphas = [1.0 / inv_a[k] for k in range(3)]
        d_inv = [0.0, 0.0, 0.0]
        for i in range(3):
            d_inv[i] = -b1loop[i] * dL
            for j in range(3):
                d_inv[i] -= bij[i][j] * alphas[j] / fourpi * dL
        for i in range(3):
            inv_a[i] += d_inv[i]
    return inv_a
```

**M5. VL two-loop b_ij computation:**

```python
def compute_vl_bij(C2_3, C2_2, S2_3, S2_2, d3, d2, Y, k1):
    """Compute the VL two-loop b_ij matrix for (R₃, R₂, Y).
    
    FORMULAS (Machacek-Vaughn fermion contribution):
      Off-diagonal: db_ab = (4/3) × S_a(R) × d_other × C_b(R)
      Diagonal (FERMION ONLY):
        db_aa = (10/3) × S_a(R) × d_other × C_a(R)
    
    CRITICAL PITFALL (PHYS-28 iteration 2):
      The FULL MV diagonal is: 2×C_G + (10/3)×C_R
      The 2×C_G is gauge self-coupling — ALREADY in SM b_ij.
      Adding a new fermion adds ONLY (10/3)×C_R.
      
      Wrong (including 2×C_G): db₂₂ = 39/4 = 9.75
      Correct (fermion only):  db₂₂ = 15/4 = 3.75
    
    Returns: 3×3 list of Fractions
    """
    Y2 = Y * Y
    S1 = Fraction(2, 5) * d3 * d2 * Y2
    
    db = [[None]*3 for _ in range(3)]
    db[0][0] = Fraction(10,3) * S1 * (C2_3 + C2_2 + k1*Y2)
    db[0][1] = Fraction(4,3) * S1 * C2_2
    db[0][2] = Fraction(4,3) * S1 * C2_3
    db[1][0] = Fraction(4,3) * S2_2 * d3 * k1 * Y2
    db[1][1] = Fraction(10,3) * S2_2 * d3 * C2_2
    db[1][2] = Fraction(4,3) * S2_2 * d3 * C2_3
    db[2][0] = Fraction(4,3) * S2_3 * d2 * k1 * Y2
    db[2][1] = Fraction(4,3) * S2_3 * d2 * C2_2
    db[2][2] = Fraction(10,3) * S2_3 * d2 * C2_3
    return db
```

**M6. α_s prediction (two-input method):**

```python
def predict_alpha_s(inv_a1, inv_a2, b1loop, bij, n_steps=500):
    """Predict α_s from (1/α₁, 1/α₂) using unification.
    
    METHOD (PHYS-30):
      1. Run 1/α₁ and 1/α₂ from M_Z to crossing (binary search)
      2. At crossing: 1/α_GUT = average of 1/α₁ and 1/α₂
      3. Run all three couplings back from GUT to M_Z
         starting from (α_GUT, α_GUT, α_GUT)
      4. The predicted 1/α₃ at M_Z gives α_s = 1/(1/α₃)
    
    Returns: (alpha_s_pred, Delta, L_GUT)
    """
    # Implementation uses run_two_loop_euler with binary search
    ...
```

**M7. sin²θ_W prediction (two-input method):**

```python
def predict_sin2_tW(alpha_inv_f, alpha_s_f, b1loop, bij, n_steps=500):
    """Predict sin²θ_W from (α_EM, α_s) using unification.
    
    METHOD (PHYS-34):
      1. Use b_EM = (5/3)b₁ + b₂ and b₃ to find crossing
         via: L = (1/α_EM − (8/3)/α_s) / (b_EM − (8/3)b₃)
      2. Binary search for exact crossing at two loops
      3. At crossing: 1/α₂ = 1/α_GUT
      4. Run 1/α₂ back to M_Z
      5. sin²θ_W = (1/α₂) / (1/α_EM)
    
    PITFALL (PHYS-30 iteration 1):
      sin²θ_W = (1/α₂)/(1/α_EM), NOT (1/α_EM)/(1/α₂).
      = inv_a2 / alpha_inv
      NOT alpha_inv / inv_a2
    
    Returns: (sin2_pred, L_GUT, inv_aGUT)
    """
    ...
```

---

### 16. SECTION N: PITFALL DOCUMENTATION

Every pitfall encountered in Sessions 1–4, with the wrong answer, the right answer, and the PHYS paper that resolved it.

| # | Pitfall | Wrong answer | Right answer | Paper | Iteration |
|---|---|---|---|---|---|
| N1 | 1/α₂ from sin²θ_W | 593 (divided) | 31.7 (multiplied) | PHYS-30 | 1 |
| N2 | Sign of running | +b×L (diverge) | −b×L (converge) | PHYS-28 | 1–3 |
| N3 | VL diagonal coefficient | 2C_G+(10/3)C_R=39/4 | (10/3)C_R=15/4 | PHYS-28 | 2 |
| N4 | GUT threshold target | One-loop Δ=−1.17 | Two-loop Δ=−0.40 | PHYS-29 | 1–2 |
| N5 | Euler with mpf speed | Hangs at 10,000 trials | Use Python float | PHYS-31 | 1 |
| N6 | Monte Carlo scan speed | mpf scan (hangs) | Float scan, early exit | PHYS-31 | 1 |
| N7 | Koide K convention | K=(sum_sqrt)²/(3×sum_m)=0.5 | K=sum_m/(sum_sqrt)²=0.667 | PHYS-33 | 1 |
| N8 | Koide a² extraction | a²=2(1/K−1) with wrong K | a²=2(3K−1) with correct K | PHYS-33 | 1 |
| N9 | Soft threshold function | ln(1+(μ/M)²)/norm → 30% miss | 1/(1+(M/μ)²) → 7% miss | PHYS-35 | 1 |
| N10 | Bounding box balloon | Text at y=−7 → 11,000px tall | All text inside axis limits | PHYS-30 diag | 1 |
| N11 | Dict key vs list index | counts[s] where s=score value | counts[i] where i=loop index | PHYS-31 diag | 1 |
| N12 | Weyl counting for VL | 4 Weyl → Δb₃=4/3 | VL formula → Δb₃=1/3 | PHYS-32 | noted |

---

### 17. SECTION O: NAME MAPPINGS

| Series name | Standard name | Variable in data5 | Definition |
|---|---|---|---|
| Cabibbo Doublet (CD) | (3,2,1/6) vector-like quark doublet | — | Named entity |
| Gap ratio | (b₁−b₂)/(b₂−b₃) | gap_SM, gap_CD | Exact Fraction ratio |
| Generation democracy | Δb per complete generation is equal | — | From SU(5) anomaly cancellation |
| Boson problem | Gap ratio set by gauge+Higgs only | — | Fermions cancel exactly |
| Confinement wall | Λ_QCD boundary (~0.3–2 GeV) | — | Non-perturbative zone |
| Track A | Gauge coupling unification program | — | PHYS-26 through PHYS-30 |
| Track B | Cosmological formula investigation | track_B_status="PARKED" | PHYS-31 gate fired |
| Track C | Structure papers | — | PHYS-32 forward |
| Vortex | Particle / field excitation | — | R4: field=standing pattern=vortex |
| Soliton boundary | Mass threshold | — | R5: integer rules change at boundary |
| Level 1 | Framework-determined (integers, geometry) | — | R6 |
| Level 2 | Universe-supplied (measured) | — | R7 |

---

### 18. THE COMPLETE INTEGER MAP

Every integer that appears in the computation chain, its origin, and where it connects.

| Integer | Appears in | Origin | Connects to |
|---|---|---|---|
| 1 | Δb₂, Δb₃ denom, many | Unity | Everywhere |
| 2 | a²=2, C₂(adj SU(2)), dim(fund SU(2)) | SU(2) structure | Koide, gauge running, CD shifts |
| 3 | N_gen, C₂(adj SU(3)), dim(fund SU(3)), k₁ num, b₃' denom | SU(3) structure, generation count | Unification, Koide, sin²θ_W=3/13 |
| 4 | b₃_fermion, b₂_fermion, C₂(fund SU(3)) num | Weyl count per gen (4 triplets, 4 doublets) | Beta decomposition |
| 5 | k₁ denom (k₁=3/5) | SU(5) embedding | GUT normalization |
| 6 | Common beta denom (b₁'=25/6, b₂'=−13/6) | LCM of representation theory fractions | All CD betas |
| 7 | b₃_SM=−7 | 11−4=7, gauge minus fermion balance | Asymptotic freedom, α_s running |
| 8 | 8/3 in SU(5) crossing condition | 5/3+1=8/3, from k₁_inv+1 | GUT crossing, sin²θ_W prediction |
| 10 | b₁_SM denom (41/10) | LCM of U(1) representation fractions | U(1) running |
| 11 | Gauge self-coupling (11/3)×N | Yang-Mills one-loop coefficient | All gauge betas, AF |
| 13 | b₂' numerator (\|−13/6\|=13) | −44+24+1=−19 becomes −19+6=−13 after CD | Gap ratio, sin²θ_W=3/13, DM formula |
| 15 | Δb₁ denom (1/15), db₂₂ num (15/4) | Product 3×5 from SU(3)dim×k₁denom | U(1) shift, two-loop SU(2) diagonal |
| 19 | b₂_SM numerator (\|−19/6\|=19) | −44+24+1=−19, gauge+fermion+Higgs | SM SU(2) running, identity 57/39=19/13 |
| 20 | b₃' numerator (\|−20/3\|=20) | −33+12+0+1=−20 | SU(3) running, gap denominator |
| 22 | DM formula numerator (22/13)π | 2×11, derived combination | Cosmological formula (Track B, parked) |
| 25 | b₁' numerator (25/6) | U(1) hypercharge sum with CD | U(1) running |
| 27 | Gap denom (38/27) | b₂'−b₃'=(−13+40)/6=27/6 | Unification test |
| 33 | b₃ gauge numerator ×3 | 11×3 from (11/3)×C₂(SU(3))=11, ×3 for denom | SU(3) decomposition |
| 38 | Gap numerator (38/27) | b₁'−b₂'=(25+13)/6=38/6 | Unification test |
| 41 | b₁_SM numerator (41/10) | U(1) hypercharge running sum over SM | U(1) running |
| 43 | b_EM numerator (43/9) | (125−39)/18 = 86/18 = 43/9 | EM running, sin²θ_W prediction |

---

### 19. THE DERIVATION CHAIN — FROM INPUTS TO PREDICTIONS

```
MEASURED INPUTS (Level 2):
  α_EM = 1/137.036     (DATA-4 B1)
  sin²θ_W = 0.23122    (DATA-4 B3)
  α_s = 0.1180         (DATA-4 B2)
  m_e, m_mu, m_tau      (DATA-4 B4–B6)

FRAMEWORK INPUTS (Level 1):
  SU(5) embedding → k₁ = 3/5
  CD representation (3,2,1/6) → Dynkin formulas → Δb₁, Δb₂, Δb₃
  SM particle content → b₁_SM, b₂_SM, b₃_SM
  Modified betas: b_i' = b_i_SM + Δb_i

DERIVATION CHAIN:
  1. α_EM + sin²θ_W → 1/α₁, 1/α₂          [M1: derive_inv_a1_a2]
     PITFALL N1: multiply, not divide
  
  2. b₁', b₂' → L_GUT = (1/α₁−1/α₂)/(b₁'−b₂') [M3: find_crossing_L]
     PITFALL N2: sign convention, −b×L
  
  3. At crossing: 1/α_GUT → Δ = 1/α₃(GUT) − 1/α_GUT
     One-loop Δ = −1.17 (PHYS-28)
     Two-loop Δ = −0.44 (PHYS-28, full b_ij)
     PITFALL N3: diagonal coefficient
  
  4. Run back: 1/α₃(M_Z) → α_s_pred = 1/(1/α₃)
     Best: α_s = 0.11838, miss 0.33%          [M6: predict_alpha_s]
  
  5. Alternative: α_EM + α_s → sin²θ_W
     b_EM = 43/9, crossing condition → L_GUT
     Run 1/α₂ back → sin²θ_W = (1/α₂)/α_inv
     Best: sin²θ_W = 0.23133, miss 0.048%    [M7: predict_sin2_tW]
     PITFALL N1: same multiply-not-divide issue
  
  6. m_e + m_mu + K=2/3 → m_tau = 1776.97 MeV  [Koide quadratic]
     miss 0.006%, within measurement uncertainty
     PITFALL N7, N8: K convention

INDEPENDENT RESULTS:
  Parameter count: 19 → 16
    Koide (m_tau derived): 19 → 18
    θ_QCD = 0:            18 → 17
    α_s from unification:  17 → 16
```

---

### 20. THE SOLITON BOUNDARY MAP — FROM QED TO GR

The complete map of vortex configurations and their geometric overlaps, from lowest to highest energy, in series language.

```
ENERGY SCALE              VORTEXES ACTIVE           INTEGER RULES
═══════════════════════════════════════════════════════════════════

m_e = 0.511 MeV          Electron vortex            b_EM = −4/3 × (1)² × 1
  │                       (1,1,−1): U(1) only         = −4/3
  │  QED domain           Photon gauge config         One charged vortex screening
  ↓

m_mu = 105.7 MeV         + Muon vortex              b_EM = −4/3 × (2 × 1²)
  │                       (1,1,−1): same charges       = −8/3
  │                       Two charged vortexes
  ↓

~300 MeV                  ════ CONFINEMENT WALL ════
                          α_s → O(1)
                          Integer rules BREAK
                          Non-perturbative vortex soup
~2 GeV                    ════ ABOVE WALL ════

m_tau = 1.777 GeV        + Tau vortex               b_EM grows by −4/3
  │
m_c = 1.275 GeV          + Charm vortex             b₃ changes: +2/3 per flavor
  │                       (3,1,2/3): SU(3) triplet
  ↓
m_b = 4.18 GeV           + Bottom vortex            b₃ changes: +2/3 per flavor
  │
  │  SM domain: 6 quarks, 3 leptons, gauge bosons, Higgs
  │  b₁ = 41/10, b₂ = −19/6, b₃ = −7
  │  Three gauge configs: SU(3)×SU(2)×U(1)
  │  All geometric overlaps active
  ↓

M_Z = 91.2 GeV           Z, W vortexes              Electroweak parameters measured here
  │
m_H = 125.3 GeV          Higgs vortex               Affects b₁, b₂ only (SU(3) singlet)
  │
m_t = 172.8 GeV          Top vortex                 Heaviest SM fermion
  │
  │  ═══ CD BOUNDARY (M_VL ~ 200–6000 GeV) ═══
  │  PHYS-35 finding: boundary is NOT a wall
  │  CD vortex geometric overlaps persist at all scales
  │  No-threshold (CD rules everywhere): best predictions
  │  Step function (CD rules above M_VL): 12× worse
  │
  │  With CD active:
  │  b₁' = 25/6, b₂' = −13/6, b₃' = −20/3
  │  Δb₁ = 1/15 (tiny, Y² suppressed)
  │  Δb₂ = 1 (large, 31% of |b₂_SM|)
  │  Δb₃ = 1/3 (moderate, 4.8% of |b₃_SM|)
  │
  │  Three couplings converge:
  │  1/α₁ decreases (b₁>0)
  │  1/α₂ increases (b₂<0)
  │  1/α₃ increases (b₃<0)
  ↓

M_GUT ~ 4×10¹⁵ GeV      ═══ UNIFICATION BOUNDARY ═══
  │                       Three gauge configs merge into one
  │                       SU(3)×SU(2)×U(1) → SU(5) [or SO(10)]
  │                       1/α₁ = 1/α₂ = 1/α_GUT ≈ 42
  │                       1/α₃ ≈ 1/α_GUT − Δ (Δ ≈ −0.04 no-thresh)
  │
  │  GUT domain: additional heavy vortexes
  │  X, Y gauge bosons (proton decay mediators)
  │  Color triplet Higgs (C_T = −1/12)
  │  Sigma octet + triplet (C_Sigma = −1/6)
  │  Threshold coefficients: C_total = −1/4
  │  Minimal SU(5): requires M_X/M = 23,228 (unnatural)
  ↓

M_Planck ~ 1.2×10¹⁹ GeV ═══ GRAVITATIONAL BOUNDARY ═══
                          Gauge geometry meets spacetime geometry
                          The vortex that carries gauge charges
                          also carries inertia (R3) which is
                          the source of gravitational curvature
                          
                          QED → GR bridge:
                          Same vortex → gauge overlaps (integer rules)
                                      → inertia (mass = energy in circulation)
                                      → gravitational source (E = mc²)
                          
                          Not yet computed in the series.
                          The connection is through the vortex itself:
                          geometric overlaps determine gauge running,
                          inertia determines gravitational coupling.
                          Both are properties of the same circulating
                          energy configuration.
```

---

### 21. TEST SUITE SPECIFICATION

**data5_test.py** runs all checks in order:

| Block | Description | Expected checks |
|---|---|---|
| T1 | All phys24_lib values present and identical | ~148 (carry forward) |
| T2 | New measured constants | ~5 |
| T3 | Derived constants (gap ratios, corrections) | ~10 |
| T4 | SM beta decomposition (gauge, fermion, Higgs) | ~15 |
| T5 | CD beta shifts from Dynkin formulas | ~6 |
| T6 | VL two-loop b_ij (9 Fractions) | ~9 |
| T7 | Group theory constants | ~10 |
| T8 | Threshold coefficients | ~5 |
| T9 | Derivation function outputs | ~20 |
| T10 | Pitfall tests (verify wrong answer ≠ right answer) | ~12 |
| T11 | Cross-check: functions reproduce script results | ~15 |
| T12 | Koide values and quadratic | ~8 |
| T13 | Statistical results | ~5 |
| **Total** | | **~268** |

Target: 268/268 PASS. Zero tolerance for failures.

---

### 22. WHAT DATA-5 DOES NOT CONTAIN

DATA-5 does not contain physics assertions. It does not say "the CD exists" or "unification is real." It stores the numbers that result from those computations and the functions that produce them. A future session uses DATA-5 as a toolkit, not as a claim.

DATA-5 does not contain diagram scripts or paper text. It is pure computation.

DATA-5 does not remove anything from phys24_lib. Every value, every function, every constant in phys24_lib appears in DATA-5 with the same name and the same value. The API only grows.

---

*End of DATA-5 Technical Specification. This document defines the complete data platform for Sessions 4+. Every integer, every Fraction, every derivation chain, every pitfall, every prediction from PHYS-25 through PHYS-35 is catalogued. The test suite targets 268 checks. The soliton boundary map covers QED through the Planck scale. The derivation functions encode not just HOW to compute but WHAT GOES WRONG and WHY.*

