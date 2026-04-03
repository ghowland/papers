## Plan: phys39_lib.py — The Session 4 Platform Upgrade

**When:** After PHYS-39 (Complete Unification Summary) is written.
**What:** A new library that extends phys24_lib with all Session 4 accumulated knowledge.
**Test:** Run all Session 4 scripts against phys39_lib and verify identical results.

---

### WHAT THE NEW LIBRARY ADDS

**Category 1: New verified values (from Session 4 scripts)**

| Value | Source | Paper |
|---|---|---|
| db_ij_VL (9 Fractions) | PHYS-28 two-loop b_ij matrix | PHYS-28 |
| b_ij_full (9 combined SM+VL) | PHYS-28 | PHYS-28 |
| C_T = −1/12 | GUT threshold triplet coefficient | PHYS-29 |
| C_Sigma = −1/6 | GUT threshold Sigma coefficient | PHYS-29 |
| C_total = −1/4 | Combined threshold coefficient | PHYS-29 |
| db1_T, db2_T, db3_T | Triplet beta shifts (1/15, 0, 1/12) | PHYS-29 |
| db3_Sigma8 = 1/2 | Sigma octet beta shift | PHYS-29 |
| db2_Sigma3 = 1/3 | Sigma weak triplet beta shift | PHYS-29 |
| alpha_s_pred = 0.11838 | Two-loop no-threshold prediction | PHYS-30 |
| sin2_tW_1loop = 0.22845 | One-loop no-threshold prediction | PHYS-27 |
| b3_gauge = −11 | Gauge self-coupling decomposition | PHYS-32 |
| b3_fermion_per_gen = 4/3 | Fermion per generation | PHYS-32 |

**Category 2: Derivation chains (new to phys39_lib, not in phys24_lib)**

These are the step-by-step computations that a new session needs to understand HOW values connect, not just WHAT they are.

```python
# DERIVATION: How to get 1/alpha_1 and 1/alpha_2 from alpha_EM and sin2_tW
# sin2_tW = alpha_EM / alpha_2
# => 1/alpha_2 = sin2_tW * (1/alpha_EM)    [MULTIPLY, not divide]
# => 1/alpha_1 = (3/5) * (1/alpha_EM - 1/alpha_2)
# Common error: dividing alpha_inv BY sin2_tW instead of multiplying.
# That gives 1/alpha_2 = 593 instead of 31.7. Garbage.
def derive_inv_a1_a2(alpha_inv_frac, sin2_tW_frac):
    """From alpha_EM and sin2_tW, derive 1/alpha_1 and 1/alpha_2.
    Uses MULTIPLICATION: 1/alpha_2 = sin2_tW * (1/alpha_EM).
    Returns (inv_a1, inv_a2) as Fractions."""
    inv_a2 = sin2_tW_frac * alpha_inv_frac
    inv_a1 = Fraction(3, 5) * (alpha_inv_frac - inv_a2)
    return inv_a1, inv_a2
```

```python
# DERIVATION: The sign convention for coupling running
# RGE: d(1/alpha_i)/d(ln mu) = -b_i/(2*pi)
# Therefore: 1/alpha_i(mu) = 1/alpha_i(mu0) - b_i * L
# where L = ln(mu/mu0) / (2*pi), L > 0 for mu > mu0
# The MINUS sign means:
#   b > 0 => 1/alpha DECREASES running up (coupling grows)
#   b < 0 => 1/alpha INCREASES running up (coupling shrinks)
# For unification: b1 > 0 (U(1) grows), b2 < 0 (SU(2) shrinks)
# => 1/alpha_1 decreases, 1/alpha_2 increases => they CONVERGE
# Common error: using + b*L instead of - b*L. This makes couplings diverge.
def run_one_loop(inv_a_start, betas, L):
    """One-loop running: 1/alpha(mu) = 1/alpha(mu0) - b*L.
    inv_a_start: list of 3 mpf values
    betas: list of 3 mpf values
    L: mpf, ln(mu/mu0)/(2*pi), positive for running UP.
    Returns: list of 3 mpf values."""
    return [inv_a_start[i] - betas[i] * L for i in range(3)]
```

```python
# DERIVATION: Finding the GUT crossing
# At crossing: 1/a1(VL) - b1*L = 1/a2(VL) - b2*L
# Rearranging: (1/a1 - 1/a2) = (b1 - b2)*L
# L = (1/a1 - 1/a2) / (b1 - b2)
# Since 1/a1 > 1/a2 (63 > 31) and b1 > b2 (4.17 > -2.17):
# L = positive/positive = positive. Good: crossing is ABOVE starting point.
# Common error: getting the subtraction order wrong, giving negative L.
def find_crossing_L(inv_a1, inv_a2, b1, b2):
    """Find L where 1/alpha_1 = 1/alpha_2 in one-loop running.
    Returns L (positive means crossing is at higher energy)."""
    return (inv_a1 - inv_a2) / (b1 - b2)
```

```python
# DERIVATION: Two-loop Euler integration
# The two-loop RGE adds: - sum_j b_ij * alpha_j / (8*pi^2)
# In terms of L = ln(mu/mu0)/(2*pi):
# d(1/alpha_i)/dL = -b_i - sum_j b_ij * alpha_j / (4*pi)
# The MINUS signs on both terms are critical.
# Common error: wrong sign on the two-loop term.
# Use Python float for speed (sufficient for 4-5 digit accuracy).
def run_two_loop_euler(inv_a_start, b1loop, bij, L_total, n_steps):
    """Euler integration of two-loop RGEs using float arithmetic.
    All inputs as float or list of float.
    Returns list of 3 float values (1/alpha_i at end)."""
    import math
    fourpi = 4.0 * math.pi
    inv_a = [inv_a_start[0], inv_a_start[1], inv_a_start[2]]
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

```python
# DERIVATION: The VL two-loop b_ij matrix
# Machacek-Vaughn fermion contribution for a Dirac fermion in (R3, R2, Y):
# Off-diagonal: db_ab = (4/3) * S_a(R) * d_other * C_b(R)
# Diagonal (FERMION ONLY, no gauge self-coupling):
#   db_aa = (10/3) * S_a(R) * d_other * C_a(R)
# Common error: using the FULL MV diagonal (2*C_G + (10/3)*C_R).
# The 2*C_G term is the gauge self-coupling — already in the SM b_ij.
# Adding a new fermion adds ONLY the (10/3)*C_R piece.
# Wrong diagonal (including 2*C_G): db22 = 39/4 = 9.75 (167% of SM!)
# Correct diagonal (fermion only):  db22 = 15/4 = 3.75 (64% of SM)
def compute_vl_bij(C2_3, C2_2, S2_3, S2_2, d3, d2, Y, k1):
    """Compute the VL two-loop b_ij matrix for representation (R3, R2, Y).
    Returns 3x3 list of Fractions."""
    Y2 = Y * Y
    S1 = Fraction(2, 5) * d3 * d2 * Y2  # effective U(1) Dynkin index
    
    db11 = Fraction(10, 3) * S1 * (C2_3 + C2_2 + k1 * Y2)
    db12 = Fraction(4, 3) * S1 * C2_2
    db13 = Fraction(4, 3) * S1 * C2_3
    db21 = Fraction(4, 3) * S2_2 * d3 * k1 * Y2
    db22 = Fraction(10, 3) * S2_2 * d3 * C2_2
    db23 = Fraction(4, 3) * S2_2 * d3 * C2_3
    db31 = Fraction(4, 3) * S2_3 * d2 * k1 * Y2
    db32 = Fraction(4, 3) * S2_3 * d2 * C2_2
    db33 = Fraction(10, 3) * S2_3 * d2 * C2_3
    
    return [[db11, db12, db13],
            [db21, db22, db23],
            [db31, db32, db33]]
```

**Category 3: Documented pitfalls (comments in the library)**

Each pitfall gets a comment block explaining:
- What the wrong answer looks like
- Why it's wrong
- What the right answer is
- Which PHYS paper discovered and resolved it

| Pitfall | Wrong | Right | Paper |
|---|---|---|---|
| 1/α₂ from sin²θ_W | divide: 137/0.231 = 593 | multiply: 0.231 × 137 = 31.7 | PHYS-30 iter 1 |
| Sign of running | +b×L (diverge) | −b×L (converge) | PHYS-28 iters 1-3 |
| VL diagonal coefficient | 2C_G + (10/3)C_R | (10/3)C_R only | PHYS-28 iter 2 |
| Threshold direction | SM above, CD below | SM below M_VL, CD above | PHYS-27 |
| GUT threshold target | One-loop Delta = −1.17 | Two-loop Delta = −0.40 | PHYS-29 iter 1-2 |
| Euler speed | mpf at 100 dps (hangs) | Python float (fast, 5 digit sufficient) | PHYS-31 |
| Monte Carlo speed | mpf scan (hangs) | float scan with early exit | PHYS-31 |

**Category 4: The self-test upgrade**

phys39_lib_test.py will verify:
- All phys24_lib values still present and identical
- All new values from Category 1
- All derivation functions from Category 2 produce correct outputs
- Cross-checks: derivation functions reproduce the script results from PHYS-27 through PHYS-32

Expected test count: phys24_lib_test has 148 checks. The upgrade adds approximately 60-80 new checks. Target: ~220 checks total.

---

### THE TRACKING LIST

As each paper is written, add new values and methods to this list:

| Paper | Values to add | Methods to add | Pitfalls to document |
|---|---|---|---|
| PHYS-28 | db_ij_VL (9), b_ij_full (9) | compute_vl_bij() | Wrong diagonal coefficient |
| PHYS-29 | C_T, C_Sigma, C_total, triplet/Sigma shifts | — | Wrong Delta target |
| PHYS-30 | alpha_s_pred, sin2_tW_pred | derive_inv_a1_a2(), run_one_loop(), find_crossing_L() | Multiply not divide |
| PHYS-31 | p_value = 0.81, beta_pool_score = 6 | scan_pool_fast() | mpf speed |
| PHYS-32 | b3 decomposition (gauge, fermion, Higgs) | — | Weyl counting discrepancy |
| PHYS-33 | (Koide values, TBD) | (TBD) | (TBD) |
| PHYS-34 | (sin²θ_W two-loop, TBD) | (TBD) | (TBD) |
| PHYS-35 | (no-threshold analysis, TBD) | (TBD) | (TBD) |
| PHYS-36 | (SO(10) coefficients, TBD) | (TBD) | (TBD) |
| PHYS-37 | (RK4 precise values, TBD) | run_two_loop_rk4() | (TBD) |
| PHYS-38 | (three-loop estimate, TBD) | (TBD) | (TBD) |
| PHYS-39 | Compilation — triggers lib upgrade | All above compiled | All above compiled |

---

### THE UPGRADE PROCESS

1. Write PHYS-39 paper (compilation)
2. Write phys39_lib.py extending phys24_lib.py with all tracked items
3. Write phys39_lib_test.py with ~220 checks
4. Run phys39_lib_test.py — must get 220/220 PASS
5. Re-run all Session 4 scripts with `from phys39_lib import *` — must get identical output
6. The equality test IS the validation: same inputs, same Fractions, same outputs

---

*This plan is tracked across all remaining papers. Each paper adds to the tracking list. The upgrade happens after PHYS-39.*
