#!/usr/bin/env python3
"""
HOWL DATA-4 DERIVATION LIBRARY
================================
Extends phys24_lib.py with derivation functions, group theory,
two-loop machinery, and predictions.

Every function encodes HOW to compute, not just WHAT the answer is.
Pitfalls from Sessions 3-4 are documented inline.

Import:
    from phys24_lib import *
    from phys24_derivations import *

Or run directly for self-test:
    python phys24_derivations.py

Platform: phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from phys24_lib import *
from mpmath import pi as mpi, log as mlog, exp as mexp, sqrt as msqrt


# ================================================================
# SECTION G: GROUP THEORY CONSTANTS (Level 1, exact)
# All from SU(N) representation theory.
# ================================================================

# Adjoint Casimirs: C_2(adj) = N for SU(N)
C2_adj_SU3 = Fraction(3, 1)          # SU(3): C_2(adj) = 3
C2_adj_SU2 = Fraction(2, 1)          # SU(2): C_2(adj) = 2

# Fundamental Casimirs: C_2(fund) = (N^2 - 1) / (2N)
C2_fund_SU3 = Fraction(4, 3)         # SU(3): (9-1)/6 = 4/3
C2_fund_SU2 = Fraction(3, 4)         # SU(2): (4-1)/4 = 3/4

# Dynkin index of fundamental: S_2(fund) = 1/2 for any SU(N)
S2_fund = Fraction(1, 2)

# Dimensions of fundamental representations
dim_fund_SU3 = Fraction(3, 1)
dim_fund_SU2 = Fraction(2, 1)

# GUT normalization factor: k_1 = 3/5 from SU(5) embedding
k1_GUT = Fraction(3, 5)
k1_inv = Fraction(5, 3)              # 1/k_1 = 5/3

# Number of SM generations
N_gen = Fraction(3, 1)

# Gauge self-coupling coefficient: -(11/3) * C_2(adj)
gauge_coeff = Fraction(-11, 3)

# Cabibbo Doublet quantum numbers (also in phys24_lib as CD_SU3 etc.)
Y_CD = Fraction(1, 6)
Y2_CD = Y_CD * Y_CD                  # = 1/36


# ================================================================
# SECTION M1: COUPLING EXTRACTION
# From measured alpha_EM, sin2_tW, alpha_s → inverse GUT couplings
# ================================================================

def derive_couplings(alpha_inv_f, sin2_tW_f, alpha_s_f):
    """Extract GUT-normalized inverse couplings at M_Z.

    DERIVATION:
      alpha_EM = alpha_2 * sin^2(theta_W)
      => 1/alpha_2 = sin^2(theta_W) * (1/alpha_EM)

      1/alpha_EM = (5/3) * (1/alpha_1) + (1/alpha_2)
      => 1/alpha_1 = (3/5) * (1/alpha_EM - 1/alpha_2)

      1/alpha_3 = 1/alpha_s

    PITFALL (PHYS-30 iteration 1):
      Wrong: 1/alpha_2 = (1/alpha_EM) / sin^2(theta_W) = 593
      Right: 1/alpha_2 = sin^2(theta_W) * (1/alpha_EM) = 31.7
      The wrong formula DIVIDES instead of MULTIPLYING.

    Args: all Fractions from phys24_lib
    Returns: (inv_a1, inv_a2, inv_a3) as Fractions
    """
    inv_a2 = sin2_tW_f * alpha_inv_f
    inv_a1 = Fraction(3, 5) * (alpha_inv_f - inv_a2)
    inv_a3 = Fraction(1, 1) / alpha_s_f
    return inv_a1, inv_a2, inv_a3


# ================================================================
# SECTION M2: VL BETA SHIFT COMPUTATION (Dynkin formulas)
# For any vector-like pair (R_3, R_2, Y)
# ================================================================

def compute_vl_one_loop(dim_R3, dim_R2, Y, S2_R3, S2_R2):
    """One-loop beta shifts for a vector-like fermion pair.

    FORMULAS:
      Db_1 = (2/5) * dim(R_3) * dim(R_2) * Y^2
      Db_2 = (2/3) * dim(R_3) * S_2(R_2)
      Db_3 = (1/3) * dim(R_2) * S_2(R_3)

    Coefficients encode normalization:
      2/5 = (2/3) * (3/5) where 3/5 is GUT normalization
      2/3 for SU(2) Dirac fermion Dynkin contribution
      1/3 for SU(3) Dirac fermion Dynkin contribution

    Args: all Fractions
    Returns: (db1, db2, db3) as Fractions
    """
    db1 = Fraction(2, 5) * dim_R3 * dim_R2 * Y * Y
    db2 = Fraction(2, 3) * dim_R3 * S2_R2
    db3 = Fraction(1, 3) * dim_R2 * S2_R3
    return db1, db2, db3


def compute_vl_two_loop(C2_R3, C2_R2, S2_R3, S2_R2, dim_R3, dim_R2, Y, k1):
    """Two-loop beta shift matrix for a vector-like fermion pair.

    FORMULAS (Machacek-Vaughn FERMION contribution only):
      Off-diagonal: db_ab = (4/3) * S_a(R) * d_other * C_b(R)
      Diagonal:     db_aa = (10/3) * S_a(R) * d_other * C_a(R)

    CRITICAL PITFALL (PHYS-28 iteration 2):
      The FULL MV diagonal is: 2*C_G + (10/3)*C_R
      The 2*C_G is gauge self-coupling — ALREADY in SM b_ij.
      Adding a new fermion adds ONLY (10/3)*C_R.

      Wrong (including 2*C_G): db_22 = 2*2 + (10/3)*(3/4)*3 = 39/4
      Correct (fermion only):  db_22 = (10/3)*(1/2)*3*(3/4) = 15/4

    For U(1): the effective Dynkin index is S_1 = (2/5)*d3*d2*Y^2
    and the effective Casimir for U(1) is k1*Y^2.

    Args: all Fractions
    Returns: 3x3 list of Fractions
    """
    Y2 = Y * Y
    # Effective U(1) Dynkin index for the VL pair
    S1_eff = Fraction(2, 5) * dim_R3 * dim_R2 * Y2

    db = [[Fraction(0)] * 3 for _ in range(3)]

    # Row 0: U(1)
    db[0][0] = Fraction(10, 3) * S1_eff * (C2_R3 + C2_R2 + k1 * Y2)
    db[0][1] = Fraction(4, 3) * S1_eff * C2_R2
    db[0][2] = Fraction(4, 3) * S1_eff * C2_R3

    # Row 1: SU(2)
    db[1][0] = Fraction(4, 3) * S2_R2 * dim_R3 * k1 * Y2
    db[1][1] = Fraction(10, 3) * S2_R2 * dim_R3 * C2_R2
    db[1][2] = Fraction(4, 3) * S2_R2 * dim_R3 * C2_R3

    # Row 2: SU(3)
    db[2][0] = Fraction(4, 3) * S2_R3 * dim_R2 * k1 * Y2
    db[2][1] = Fraction(4, 3) * S2_R3 * dim_R2 * C2_R2
    db[2][2] = Fraction(10, 3) * S2_R3 * dim_R2 * C2_R3

    return db


# ================================================================
# SECTION M3: ONE-LOOP RUNNING
# ================================================================

def run_one_loop_frac(inv_a_start, betas, L):
    """One-loop running in exact Fraction arithmetic.

    EQUATION:
      1/alpha_i(mu) = 1/alpha_i(mu_0) - b_i * L
      where L = ln(mu/mu_0) / (2*pi), L > 0 for mu > mu_0.

    SIGN CONVENTION (PHYS-28 iterations 1-3):
      The MINUS sign means:
        b > 0 (U(1)): 1/alpha_1 DECREASES running up -> coupling GROWS
        b < 0 (SU(2), SU(3)): 1/alpha_2,3 INCREASES -> coupling SHRINKS
        => 1/alpha_1 and 1/alpha_2 CONVERGE at high energy

      PITFALL: Using +b*L instead of -b*L makes couplings DIVERGE.

    Args:
      inv_a_start: list of 3 Fractions [1/a1, 1/a2, 1/a3]
      betas: list of 3 Fractions [b1, b2, b3]
      L: mpf, ln(mu/mu_0)/(2*pi)
    Returns: list of 3 mpf [1/a1, 1/a2, 1/a3] at mu
    """
    return [f2m(inv_a_start[i]) - f2m(betas[i]) * L for i in range(3)]


def find_crossing_L(inv_a1_f, inv_a2_f, b1_f, b2_f):
    """Find L where 1/alpha_1 = 1/alpha_2 at one loop.

    DERIVATION:
      At crossing: 1/a1 - b1*L = 1/a2 - b2*L
      => (1/a1 - 1/a2) = (b1 - b2) * L
      => L = (1/a1 - 1/a2) / (b1 - b2)

      Since 1/a1 > 1/a2 (~63 > ~31) and b1 > b2 (~4.17 > ~-2.17):
      L = positive / positive = positive -> crossing is ABOVE M_Z.

    PITFALL: Wrong subtraction order gives negative L.

    Args: all Fractions
    Returns: L as Fraction (exact)
    """
    return (inv_a1_f - inv_a2_f) / (b1_f - b2_f)


def L_to_scale(L_val, M_Z_MeV):
    """Convert L = ln(mu/M_Z)/(2*pi) to scale mu in MeV.

    Args:
      L_val: mpf, the L parameter
      M_Z_MeV: mpf, M_Z in MeV
    Returns: mu in MeV (mpf), log10(mu/GeV) (mpf)
    """
    mu = M_Z_MeV * mexp(mpf("2") * mpi * L_val)
    log10_mu_GeV = mlog(mu / mpf("1000"), 10)
    return mu, log10_mu_GeV


# ================================================================
# SECTION M4: GAP RATIO
# ================================================================

def gap_ratio_from_betas(b1_f, b2_f, b3_f):
    """Compute gap ratio from three beta coefficients.

    gap = (b1 - b2) / (b2 - b3)

    Args: all Fractions
    Returns: Fraction (exact)
    """
    return (b1_f - b2_f) / (b2_f - b3_f)


# ================================================================
# SECTION M5: TWO-LOOP EULER INTEGRATOR (mpf version)
# ================================================================

def run_two_loop_euler(inv_a_start, b1loop, bij, L_total, n_steps):
    """Euler integration of two-loop RGEs using mpf arithmetic.

    EQUATION:
      d(1/alpha_i)/dL = -b_i - sum_j b_ij * alpha_j / (4*pi)

      Both terms have MINUS signs.
      The second term uses alpha_j = 1/(1/alpha_j) at each step.

    SIGN CONVENTION:
      d(1/a_i)/dL = -b_i (one-loop, negative because d/d(ln mu) = -b/(2pi)
                          and L = ln(mu/mu0)/(2pi), so d/dL = -b)
                    -sum_j b_ij * a_j / (4*pi) (two-loop correction)

    PITFALL (PHYS-28): Wrong sign on two-loop term.

    Uses mpf throughout for verified precision. For high-speed
    scanning (Monte Carlo), use a separate float-based integrator.

    Args:
      inv_a_start: list of 3 mpf
      b1loop: list of 3 mpf
      bij: 3x3 list of mpf
      L_total: mpf, total L to integrate (positive = running UP)
      n_steps: int, Euler steps
    Returns: list of 3 mpf [1/a1, 1/a2, 1/a3] at end
    """
    fourpi = mpf("4") * mpi
    inv_a = [mpf(x) for x in inv_a_start]
    dL = L_total / mpf(n_steps)

    for _ in range(n_steps):
        alphas = [mpf("1") / inv_a[k] for k in range(3)]
        d_inv = [mpf("0")] * 3
        for i in range(3):
            d_inv[i] = -b1loop[i] * dL
            for j in range(3):
                d_inv[i] -= bij[i][j] * alphas[j] / fourpi * dL
        for i in range(3):
            inv_a[i] += d_inv[i]

    return inv_a


# ================================================================
# SECTION M6: ALPHA_S PREDICTION (one-loop and two-loop)
# ================================================================

def predict_alpha_s_one_loop(inv_a1_f, inv_a2_f, inv_a3_f, b1_f, b2_f, b3_f):
    """Predict alpha_s from one-loop unification.

    METHOD:
      1. Find L_GUT where 1/a1 = 1/a2
      2. Compute 1/a_GUT = 1/a1(L_GUT) = 1/a2(L_GUT)
      3. Compute 1/a3(L_GUT) from running
      4. Delta = 1/a3(L_GUT) - 1/a_GUT
      5. Predict: 1/a3(M_Z) = 1/a_GUT + b3 * L_GUT
         => alpha_s_pred = 1 / (1/a3_pred)

    Args: all Fractions from the library
    Returns: dict with alpha_s_pred, Delta, L_GUT, inv_a_GUT (all mpf)
    """
    L_GUT = f2m(find_crossing_L(inv_a1_f, inv_a2_f, b1_f, b2_f))
    inv_a_GUT = f2m(inv_a1_f) - f2m(b1_f) * L_GUT
    inv_a3_at_GUT = f2m(inv_a3_f) - f2m(b3_f) * L_GUT
    Delta = inv_a3_at_GUT - inv_a_GUT

    # Predict: if unified, 1/a3 starts at inv_a_GUT and runs back
    inv_a3_pred = inv_a_GUT + f2m(b3_f) * L_GUT
    alpha_s_pred = mpf("1") / inv_a3_pred

    return {
        "alpha_s_pred": alpha_s_pred,
        "Delta": Delta,
        "L_GUT": L_GUT,
        "inv_a_GUT": inv_a_GUT,
        "inv_a3_at_GUT": inv_a3_at_GUT,
    }


def predict_alpha_s_two_loop(inv_a1_f, inv_a2_f, inv_a3_f,
                              b1loop, bij, n_steps=500):
    """Predict alpha_s from two-loop unification via binary search.

    METHOD:
      1. Binary search for L where 1/a1(L) = 1/a2(L) at two loops
      2. At crossing: 1/a_GUT = average of 1/a1 and 1/a2
      3. Run all three from (a_GUT, a_GUT, a_GUT) back to M_Z
      4. Predicted 1/a3 at M_Z -> alpha_s

    Args:
      inv_a1_f, inv_a2_f, inv_a3_f: Fractions (couplings at M_Z)
      b1loop: list of 3 Fractions (one-loop betas)
      bij: 3x3 list of Fractions (two-loop matrix)
      n_steps: Euler steps per integration
    Returns: dict with alpha_s_pred, Delta, L_GUT, inv_a_GUT
    """
    inv_a_start = [f2m(inv_a1_f), f2m(inv_a2_f), f2m(inv_a3_f)]
    b1_mpf = [f2m(b) for b in b1loop]
    bij_mpf = [[f2m(bij[i][j]) for j in range(3)] for i in range(3)]

    # One-loop estimate for initial L range
    L_est = f2m(find_crossing_L(inv_a1_f, inv_a2_f, b1loop[0], b1loop[1]))

    # Binary search for two-loop crossing
    L_lo = L_est * mpf("0.8")
    L_hi = L_est * mpf("1.2")

    for _ in range(60):  # 60 bisections = ~18 digits of L
        L_mid = (L_lo + L_hi) / mpf("2")
        result = run_two_loop_euler(inv_a_start, b1_mpf, bij_mpf,
                                     L_mid, n_steps)
        diff = result[0] - result[1]  # 1/a1 - 1/a2 at L_mid
        if diff > mpf("0"):
            # 1/a1 still > 1/a2, need to go further
            L_lo = L_mid
        else:
            L_hi = L_mid

    L_GUT = (L_lo + L_hi) / mpf("2")

    # Run to crossing to get GUT values
    at_GUT = run_two_loop_euler(inv_a_start, b1_mpf, bij_mpf,
                                 L_GUT, n_steps)
    inv_a_GUT = (at_GUT[0] + at_GUT[1]) / mpf("2")
    Delta = at_GUT[2] - inv_a_GUT

    # Run back from GUT to M_Z with unified starting point
    inv_a_unified = [inv_a_GUT, inv_a_GUT, inv_a_GUT]
    at_MZ = run_two_loop_euler(inv_a_unified, b1_mpf, bij_mpf,
                                -L_GUT, n_steps)
    alpha_s_pred = mpf("1") / at_MZ[2]

    return {
        "alpha_s_pred": alpha_s_pred,
        "Delta": Delta,
        "L_GUT": L_GUT,
        "inv_a_GUT": inv_a_GUT,
    }


# ================================================================
# SECTION M7: SIN2_THETA_W PREDICTION (one-loop and two-loop)
# ================================================================

def predict_sin2_one_loop(alpha_inv_f, alpha_s_f, b1_f, b2_f, b3_f):
    """Predict sin2_tW from one-loop unification using alpha_EM and alpha_s.

    METHOD:
      At the GUT scale, SU(5) gives sin2_tW = 3/8.
      Running down:
        sin2_tW(M_Z) = (1/alpha_2(M_Z)) / (1/alpha_EM)

      To find 1/alpha_2(M_Z):
        1. Use the combination b_EM = (5/3)*b1 + b2 which runs 1/alpha_EM
        2. Find L_GUT where (5/3)*1/a1 = (8/3)*1/a3
           equivalently: 1/a_EM - (8/3)/a_s = (b_EM - (8/3)*b3) * L
        3. At crossing: 1/a_GUT determined
        4. Run 1/a2 back: 1/a2(M_Z) = 1/a_GUT + b2 * L_GUT
        5. sin2_tW = 1/a2(M_Z) / alpha_inv

    PITFALL (PHYS-30):
      sin2_tW = inv_a2 / alpha_inv, NOT alpha_inv / inv_a2

    Args: all Fractions
    Returns: dict with sin2_pred, L_GUT, inv_a_GUT
    """
    # b_EM = (5/3)*b1 + b2
    b_EM = k1_inv * b1_f + b2_f

    # 1/alpha_EM and (8/3)/alpha_s at M_Z
    inv_a_EM = f2m(alpha_inv_f)
    eight_thirds_inv_as = f2m(Fraction(8, 3) / alpha_s_f)

    # L_GUT from crossing condition
    b_EM_mpf = f2m(b_EM)
    b3_mpf = f2m(b3_f)
    eight_thirds = f2m(Fraction(8, 3))

    L_GUT = (inv_a_EM - eight_thirds_inv_as) / (b_EM_mpf - eight_thirds * b3_mpf)

    # 1/alpha_GUT from the alpha_s side (correct)
    inv_a3_val = f2m(Fraction(1, 1) / alpha_s_f)
    inv_a_GUT = inv_a3_val - f2m(b3_f) * L_GUT

    # 1/alpha_2 at M_Z: run from GUT back with b2
    inv_a2_pred = inv_a_GUT + f2m(b2_f) * L_GUT

    # sin2_tW = inv_a2 / alpha_inv
    sin2_pred = inv_a2_pred / inv_a_EM

    return {
        "sin2_pred": sin2_pred,
        "L_GUT": L_GUT,
        "inv_a_GUT": inv_a_GUT,
        "inv_a2_pred": inv_a2_pred,
        "b_EM": b_EM,
    }


def predict_sin2_two_loop(alpha_inv_f, alpha_s_f, b1loop, bij, n_steps=500):
    """Predict sin2_tW from two-loop unification using alpha_EM and alpha_s.

    METHOD:
      1. Extract 1/a1 and 1/a3 from inputs (1/a2 is unknown — we predict it)
      2. Use one-loop estimate of L_GUT as starting point
      3. Binary search: at each L, run two-loop from M_Z,
         check if (5/3)*1/a1(L) + 1/a2_trial(L) = 1/a_EM running holds
         Actually: run 1/a1 and 1/a3 to crossing where they meet,
         then 1/a2 at that L gives sin2_tW
      4. Run 1/a_GUT back to M_Z as 1/a2
      5. sin2_tW = inv_a2(M_Z) / alpha_inv

    Simpler two-input approach:
      We know alpha_EM and alpha_s. We don't know sin2_tW (that's what
      we're predicting). So we can't extract 1/a1 and 1/a2 separately.

      Instead:
      - Use b_EM = (5/3)*b1 + b2 to run 1/alpha_EM
      - Use b3 to run 1/alpha_3
      - Find L where they cross in the (1/a_EM, (8/3)/a_3) sense
      - At crossing: 1/a_GUT → run 1/a2 back → sin2_tW

    For two-loop: integrate the coupled system with b_EM effective running.

    Args:
      alpha_inv_f, alpha_s_f: Fractions
      b1loop: list of 3 Fractions
      bij: 3x3 list of Fractions
      n_steps: Euler steps
    Returns: dict with sin2_pred, L_GUT, inv_a_GUT
    """
    # One-loop estimate first
    result_1L = predict_sin2_one_loop(alpha_inv_f, alpha_s_f,
                                       b1loop[0], b1loop[1], b1loop[2])
    L_est = result_1L["L_GUT"]

    # For full two-loop: we need all three couplings.
    # Use the one-loop sin2 estimate to extract initial 1/a1, 1/a2.
    sin2_est = result_1L["sin2_pred"]
    inv_a2_est = sin2_est * f2m(alpha_inv_f)
    inv_a1_est = f2m(Fraction(3, 5)) * (f2m(alpha_inv_f) - inv_a2_est)
    inv_a3_val = f2m(Fraction(1, 1) / alpha_s_f)

    inv_a_start = [inv_a1_est, inv_a2_est, inv_a3_val]
    b1_mpf = [f2m(b) for b in b1loop]
    bij_mpf = [[f2m(bij[i][j]) for j in range(3)] for i in range(3)]

    # Binary search for crossing (1/a1 = 1/a2)
    L_lo = L_est * mpf("0.8")
    L_hi = L_est * mpf("1.2")

    for _ in range(60):
        L_mid = (L_lo + L_hi) / mpf("2")
        result = run_two_loop_euler(inv_a_start, b1_mpf, bij_mpf,
                                     L_mid, n_steps)
        diff = result[0] - result[1]
        if diff > mpf("0"):
            L_lo = L_mid
        else:
            L_hi = L_mid

    L_GUT = (L_lo + L_hi) / mpf("2")

    # At crossing
    at_GUT = run_two_loop_euler(inv_a_start, b1_mpf, bij_mpf,
                                 L_GUT, n_steps)
    inv_a_GUT = (at_GUT[0] + at_GUT[1]) / mpf("2")

    # Run back from GUT to get 1/a2(M_Z)
    inv_a_unified = [inv_a_GUT, inv_a_GUT, inv_a_GUT]
    at_MZ = run_two_loop_euler(inv_a_unified, b1_mpf, bij_mpf,
                                -L_GUT, n_steps)

    # sin2_tW = inv_a2(M_Z) / alpha_inv
    sin2_pred = at_MZ[1] / f2m(alpha_inv_f)

    return {
        "sin2_pred": sin2_pred,
        "L_GUT": L_GUT,
        "inv_a_GUT": inv_a_GUT,
    }


# ================================================================
# SECTION M8: KOIDE COMPUTATIONS
# ================================================================

def koide_ratio(m1_f, m2_f, m3_f):
    """Compute Koide ratio K = sum(m) / (sum(sqrt(m)))^2.

    PITFALL (PHYS-33 iteration 1):
      Wrong: K = (sum_sqrt)^2 / (3 * sum_m) = 0.5
      Right: K = sum_m / (sum_sqrt)^2 = 0.667

    Args: three Fractions (masses)
    Returns: mpf
    """
    s1 = msqrt(f2m(m1_f))
    s2 = msqrt(f2m(m2_f))
    s3 = msqrt(f2m(m3_f))
    num = f2m(m1_f + m2_f + m3_f)
    den = (s1 + s2 + s3) ** 2
    return num / den


def koide_amplitude_sq(K_val):
    """From Koide ratio K, compute a^2 = 2*(3*K - 1).

    The PHYS-8 identity: K = (1 + a^2/2) / 3
    Inverting: a^2 = 2*(3*K - 1)

    At K = 2/3: a^2 = 2 exactly.

    PITFALL (PHYS-33 iteration 1):
      Wrong: a^2 = 2*(1/K - 1) with inverted K
      Right: a^2 = 2*(3*K - 1) with correct K

    Args: K_val as mpf
    Returns: mpf
    """
    return mpf("2") * (mpf("3") * K_val - mpf("1"))


def koide_predict_m_tau(m_e_f, m_mu_f):
    """Predict m_tau from m_e and m_mu using K = 2/3.

    DERIVATION:
      K = 2/3 => sum_m / (sum_sqrt)^2 = 2/3
      Let s = sqrt(m_e) + sqrt(m_mu), S = m_e + m_mu, x = sqrt(m_tau).
      sum_m = S + x^2, sum_sqrt = s + x.
      K = 2/3 => 3(S + x^2) = 2(s + x)^2
      => 3S + 3x^2 = 2s^2 + 4sx + 2x^2
      => x^2 - 4sx + (3S - 2s^2) = 0
      => x = 2s +/- sqrt(4s^2 - 3S + 2s^2) = 2s +/- sqrt(6s^2 - 3S)

    Args: m_e_f, m_mu_f as Fractions
    Returns: dict with m_tau_pred, m_tau_other_root, M_koide, theta_koide
    """
    s_e = msqrt(f2m(m_e_f))
    s_mu = msqrt(f2m(m_mu_f))
    s = s_e + s_mu
    S = f2m(m_e_f + m_mu_f)

    discriminant = mpf("6") * s * s - mpf("3") * S
    sqrt_disc = msqrt(discriminant)

    x_plus = mpf("2") * s + sqrt_disc
    x_minus = mpf("2") * s - sqrt_disc

    m_tau_pred = x_plus * x_plus    # the physical root (large)
    m_tau_other = x_minus * x_minus  # the unphysical root (small)

    # Koide parameters
    sum_sqrt = s_e + s_mu + x_plus
    M_koide = sum_sqrt / mpf("3")

    return {
        "m_tau_pred": m_tau_pred,
        "m_tau_other": m_tau_other,
        "M_koide": M_koide,
        "sqrt_m_tau_pred": x_plus,
    }


# ================================================================
# SECTION M9: BETA DECOMPOSITION BY SOURCE
# ================================================================

def decompose_SM_betas():
    """Decompose SM betas into gauge + Higgs + fermion.

    Returns dict with all components as Fractions.
    """
    # Gauge: -(11/3) * C_2(adj)
    b1_gauge = Fraction(0, 1)         # U(1) is abelian, no self-coupling
    b2_gauge = gauge_coeff * C2_adj_SU2  # = -22/3
    b3_gauge = gauge_coeff * C2_adj_SU3  # = -11

    # Higgs doublet (1, 2, 1/2):
    # b1_higgs = (2/5) * (1/2)^2 * 1 * 2 / 2 = 1/10
    #   (the /2 is because Higgs is a scalar, not a Dirac fermion)
    b1_higgs = Fraction(1, 10)
    # b2_higgs = (1/3) * S_2(fund SU(2)) = (1/3)*(1/2) = 1/6
    b2_higgs = Fraction(1, 6)
    b3_higgs = Fraction(0, 1)         # Higgs is SU(3) singlet

    # Per-generation fermion (from phys24_lib: 4/3, 4/3, 4/3)
    b1_per_gen = Fraction(4, 3)
    b2_per_gen = Fraction(4, 3)
    b3_per_gen = Fraction(4, 3)

    b1_fermion = N_gen * b1_per_gen   # = 4
    b2_fermion = N_gen * b2_per_gen   # = 4
    b3_fermion = N_gen * b3_per_gen   # = 4

    return {
        "b1_gauge": b1_gauge, "b2_gauge": b2_gauge, "b3_gauge": b3_gauge,
        "b1_higgs": b1_higgs, "b2_higgs": b2_higgs, "b3_higgs": b3_higgs,
        "b1_fermion": b1_fermion, "b2_fermion": b2_fermion, "b3_fermion": b3_fermion,
        "b1_per_gen": b1_per_gen, "b2_per_gen": b2_per_gen, "b3_per_gen": b3_per_gen,
    }


# ================================================================
# PRECOMPUTED VALUES (from derivation functions applied to library)
# ================================================================

# VL one-loop shifts (should match phys24_lib)
_db1_comp, _db2_comp, _db3_comp = compute_vl_one_loop(
    dim_fund_SU3, dim_fund_SU2, Y_CD, S2_fund, S2_fund)

# VL two-loop b_ij matrix
db_ij_VL = compute_vl_two_loop(
    C2_fund_SU3, C2_fund_SU2, S2_fund, S2_fund,
    dim_fund_SU3, dim_fund_SU2, Y_CD, k1_GUT)

# Full two-loop matrix: SM + VL
b_ij_full = [[b_ij_SM[i][j] + db_ij_VL[i][j] for j in range(3)]
             for i in range(3)]

# b_EM = (5/3)*b1' + b2' for electromagnetic running
b_EM_CD = k1_inv * b1_mod + b2_mod


# ================================================================
# SELF-TEST
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PHYS24_DERIVATIONS SELF-TEST")
    print("=" * 70)
    print()

    checks = []

    # --------------------------------------------------------
    # Group theory constants
    # --------------------------------------------------------
    print("GROUP THEORY")
    print("-" * 70)
    print()

    chk_exact("C2(adj SU(3)) = 3",
              C2_adj_SU3, Fraction(3, 1), checks)

    chk_exact("C2(fund SU(3)) = 4/3",
              C2_fund_SU3, Fraction(4, 3), checks)

    chk_exact("C2(fund SU(2)) = 3/4",
              C2_fund_SU2, Fraction(3, 4), checks)

    chk_exact("k1_GUT = 3/5",
              k1_GUT, Fraction(3, 5), checks)

    # --------------------------------------------------------
    # Coupling extraction
    # --------------------------------------------------------
    print()
    print("COUPLING EXTRACTION")
    print("-" * 70)
    print()

    ia1, ia2, ia3 = derive_couplings(alpha_inv, sin2_tW, alpha_s)

    chk_exact("1/a1 from derive_couplings matches library",
              ia1, inv_a1, checks)

    chk_exact("1/a2 from derive_couplings matches library",
              ia2, inv_a2, checks)

    chk_exact("1/a3 from derive_couplings matches library",
              ia3, inv_a3, checks)

    # Sanity: 1/a2 should be ~31, not ~593
    chk_bool("1/a2 ~ 31.7 (not 593)",
             mpf("30") < f2m(ia2) < mpf("35"),
             "1/a2 = %s" % mp.nstr(f2m(ia2), 7), checks)

    # --------------------------------------------------------
    # VL one-loop shifts
    # --------------------------------------------------------
    print()
    print("VL ONE-LOOP SHIFTS (Dynkin)")
    print("-" * 70)
    print()

    chk_exact("Db1 from Dynkin = 1/15",
              _db1_comp, db1_VL, checks)

    chk_exact("Db2 from Dynkin = 1",
              _db2_comp, db2_VL, checks)

    chk_exact("Db3 from Dynkin = 1/3",
              _db3_comp, db3_VL, checks)

    # --------------------------------------------------------
    # VL two-loop b_ij matrix
    # --------------------------------------------------------
    print()
    print("VL TWO-LOOP b_ij MATRIX")
    print("-" * 70)
    print()

    # Expected values from the Machacek-Vaughn fermion formula
    db_ij_expected = [
        [Fraction(7, 15),  Fraction(1, 15),  Fraction(16, 135)],
        [Fraction(1, 30),  Fraction(15, 4),  Fraction(8, 3)],
        [Fraction(1, 45),  Fraction(1, 1),   Fraction(40, 9)],
    ]

    for i in range(3):
        for j in range(3):
            tag = "db_ij_VL[%d][%d] = %s" % (i, j, db_ij_expected[i][j])
            chk_exact(tag, db_ij_VL[i][j], db_ij_expected[i][j], checks)

    # Critical check: db_22 = 15/4, NOT 39/4
    chk_bool("db_22 is 15/4 (fermion only), NOT 39/4 (with gauge)",
             db_ij_VL[1][1] == Fraction(15, 4),
             "db_22 = %s" % db_ij_VL[1][1], checks)

    # --------------------------------------------------------
    # Gap ratio
    # --------------------------------------------------------
    print()
    print("GAP RATIOS")
    print("-" * 70)
    print()

    gap_sm_comp = gap_ratio_from_betas(b1_SM, b2_SM, b3_SM)
    chk_exact("SM gap from function = 218/115",
              gap_sm_comp, Fraction(218, 115), checks)

    gap_cd_comp = gap_ratio_from_betas(b1_mod, b2_mod, b3_mod)
    chk_exact("CD gap from function = 38/27",
              gap_cd_comp, Fraction(38, 27), checks)

    # --------------------------------------------------------
    # Beta decomposition
    # --------------------------------------------------------
    print()
    print("BETA DECOMPOSITION")
    print("-" * 70)
    print()

    decomp = decompose_SM_betas()

    b1_check = decomp["b1_gauge"] + decomp["b1_higgs"] + decomp["b1_fermion"]
    b2_check = decomp["b2_gauge"] + decomp["b2_higgs"] + decomp["b2_fermion"]
    b3_check = decomp["b3_gauge"] + decomp["b3_higgs"] + decomp["b3_fermion"]

    chk_exact("b1 decomposition sums to 41/10",
              b1_check, b1_SM, checks)

    chk_exact("b2 decomposition sums to -19/6",
              b2_check, b2_SM, checks)

    chk_exact("b3 decomposition sums to -7",
              b3_check, b3_SM, checks)

    # Fermion contribution to gap ratio = 0
    ferm_gap_num = decomp["b1_fermion"] - decomp["b2_fermion"]
    ferm_gap_den = decomp["b2_fermion"] - decomp["b3_fermion"]
    chk_exact("Fermion gap numerator = 0",
              ferm_gap_num, Fraction(0), checks)
    chk_exact("Fermion gap denominator = 0",
              ferm_gap_den, Fraction(0), checks)

    # --------------------------------------------------------
    # One-loop crossing
    # --------------------------------------------------------
    print()
    print("ONE-LOOP CROSSING")
    print("-" * 70)
    print()

    L_GUT_SM = find_crossing_L(inv_a1, inv_a2, b1_SM, b2_SM)
    show("L_GUT (SM betas, dimensionless)", f2m(L_GUT_SM))

    L_GUT_CD = find_crossing_L(inv_a1, inv_a2, b1_mod, b2_mod)
    show("L_GUT (CD betas, dimensionless)", f2m(L_GUT_CD))

    M_Z_mpf = f2m(M_Z)
    _, log10_MGUT_CD = L_to_scale(f2m(L_GUT_CD), M_Z_mpf)
    show("log10(M_GUT/GeV) for CD", log10_MGUT_CD)

    chk_bool("CD M_GUT in [10^15, 10^16]",
             mpf("15") < log10_MGUT_CD < mpf("16"),
             "log10(M_GUT) = %s" % mp.nstr(log10_MGUT_CD, 4), checks)

    # --------------------------------------------------------
    # One-loop alpha_s prediction
    # --------------------------------------------------------
    print()
    print("ONE-LOOP ALPHA_S PREDICTION")
    print("-" * 70)
    print()

    as_1L = predict_alpha_s_one_loop(inv_a1, inv_a2, inv_a3,
                                      b1_mod, b2_mod, b3_mod)
    show("alpha_s predicted (one-loop, dimensionless)", as_1L["alpha_s_pred"])
    show("Delta (dimensionless)", as_1L["Delta"])

    as_miss_1L = abs(as_1L["alpha_s_pred"] - f2m(alpha_s)) / f2m(alpha_s) * mpf("100")
    show("Miss from measured (%%)", as_miss_1L)

    chk_bool("One-loop alpha_s miss < 15%%",
             as_miss_1L < mpf("15"),
             "miss = %s%%" % mp.nstr(as_miss_1L, 4), checks)

    # --------------------------------------------------------
    # One-loop sin2_tW prediction
    # --------------------------------------------------------
    print()
    print("ONE-LOOP SIN2_THETA_W PREDICTION")
    print("-" * 70)
    print()

    sin2_1L = predict_sin2_one_loop(alpha_inv, alpha_s,
                                     b1_mod, b2_mod, b3_mod)
    show("sin2_tW predicted (one-loop, dimensionless)", sin2_1L["sin2_pred"])
    show("b_EM = %s" % sin2_1L["b_EM"], f2m(sin2_1L["b_EM"]))

    sin2_miss_1L = abs(sin2_1L["sin2_pred"] - f2m(sin2_tW)) / f2m(sin2_tW) * mpf("100")
    show("Miss from measured (%%)", sin2_miss_1L)

    chk_bool("One-loop sin2_tW miss < 2%%",
             sin2_miss_1L < mpf("2"),
             "miss = %s%%" % mp.nstr(sin2_miss_1L, 4), checks)

    # --------------------------------------------------------
    # Two-loop alpha_s prediction (SM b_ij only)
    # --------------------------------------------------------
    print()
    print("TWO-LOOP ALPHA_S PREDICTION (SM b_ij)")
    print("-" * 70)
    print()

    as_2L_SM = predict_alpha_s_two_loop(
        inv_a1, inv_a2, inv_a3,
        [b1_mod, b2_mod, b3_mod],
        b_ij_SM,
        n_steps=500)

    show("alpha_s predicted (two-loop SM b_ij, dimensionless)",
         as_2L_SM["alpha_s_pred"])
    show("Delta (dimensionless)", as_2L_SM["Delta"])

    as_miss_2L_SM = abs(as_2L_SM["alpha_s_pred"] - f2m(alpha_s)) / f2m(alpha_s) * mpf("100")
    show("Miss from measured (%%)", as_miss_2L_SM)

    chk_bool("Two-loop SM alpha_s miss < 1%%",
             as_miss_2L_SM < mpf("1"),
             "miss = %s%%" % mp.nstr(as_miss_2L_SM, 4), checks)

    # --------------------------------------------------------
    # Two-loop alpha_s prediction (full b_ij = SM + VL)
    # --------------------------------------------------------
    print()
    print("TWO-LOOP ALPHA_S PREDICTION (full b_ij = SM + VL)")
    print("-" * 70)
    print()

    as_2L_full = predict_alpha_s_two_loop(
        inv_a1, inv_a2, inv_a3,
        [b1_mod, b2_mod, b3_mod],
        b_ij_full,
        n_steps=500)

    show("alpha_s predicted (two-loop full b_ij, dimensionless)",
         as_2L_full["alpha_s_pred"])
    show("Delta (dimensionless)", as_2L_full["Delta"])

    as_miss_2L_full = abs(as_2L_full["alpha_s_pred"] - f2m(alpha_s)) / f2m(alpha_s) * mpf("100")
    show("Miss from measured (%%)", as_miss_2L_full)

    chk_bool("Two-loop full alpha_s miss < 1%%",
             as_miss_2L_full < mpf("1"),
             "miss = %s%%" % mp.nstr(as_miss_2L_full, 4), checks)

    chk_bool("Full b_ij improves over SM b_ij",
             as_miss_2L_full < as_miss_2L_SM,
             "full=%s%% < SM=%s%%" % (
                 mp.nstr(as_miss_2L_full, 4),
                 mp.nstr(as_miss_2L_SM, 4)), checks)

    # --------------------------------------------------------
    # Koide
    # --------------------------------------------------------
    print()
    print("KOIDE COMPUTATIONS")
    print("-" * 70)
    print()

    K_lep = koide_ratio(m_e, m_mu, m_tau)
    a2_lep_comp = koide_amplitude_sq(K_lep)

    show("K(e, mu, tau) (dimensionless)", K_lep)
    show("a^2(leptons) (dimensionless)", a2_lep_comp)

    chk("Koide K(leptons) matches library",
        K_lep, f2m(K_koide), 6, checks)

    chk("a^2(leptons) matches library",
        a2_lep_comp, f2m(a2_lep), 4, checks)

    # m_tau prediction
    mtau_result = koide_predict_m_tau(m_e, m_mu)
    show("m_tau predicted (MeV)", mtau_result["m_tau_pred"])
    show("m_tau measured (MeV)", f2m(m_tau))

    mtau_miss = abs(mtau_result["m_tau_pred"] - f2m(m_tau)) / f2m(m_tau) * mpf("100")
    show("Miss (%%)", mtau_miss)

    chk_bool("Koide m_tau miss < 0.01%%",
             mtau_miss < mpf("0.01"),
             "miss = %s%%" % mp.nstr(mtau_miss, 4), checks)

    show("Other quadratic root (MeV)", mtau_result["m_tau_other"])

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    print()
    print("=" * 70)
    print("DERIVATION RESULTS SUMMARY")
    print("=" * 70)
    print()
    print("  %-45s %12s %10s" % ("Prediction", "Value", "Miss"))
    print("  %-45s %12s %10s" % ("-" * 45, "-" * 12, "-" * 10))
    print("  %-45s %12s %10s" % ("alpha_s (one-loop, CD betas)",
          mp.nstr(as_1L["alpha_s_pred"], 6),
          "%s%%" % mp.nstr(as_miss_1L, 4)))
    print("  %-45s %12s %10s" % ("alpha_s (two-loop, SM b_ij)",
          mp.nstr(as_2L_SM["alpha_s_pred"], 6),
          "%s%%" % mp.nstr(as_miss_2L_SM, 4)))
    print("  %-45s %12s %10s" % ("alpha_s (two-loop, full b_ij)",
          mp.nstr(as_2L_full["alpha_s_pred"], 6),
          "%s%%" % mp.nstr(as_miss_2L_full, 4)))
    print("  %-45s %12s %10s" % ("sin2_tW (one-loop, CD betas)",
          mp.nstr(sin2_1L["sin2_pred"], 6),
          "%s%%" % mp.nstr(sin2_miss_1L, 4)))
    print("  %-45s %12s %10s" % ("m_tau (Koide K=2/3)",
          mp.nstr(mtau_result["m_tau_pred"], 7),
          "%s%%" % mp.nstr(mtau_miss, 4)))
    print("  %-45s %12s %10s" % ("Measured alpha_s",
          mp.nstr(f2m(alpha_s), 6), "—"))
    print("  %-45s %12s %10s" % ("Measured sin2_tW",
          mp.nstr(f2m(sin2_tW), 6), "—"))
    print("  %-45s %12s %10s" % ("Measured m_tau (MeV)",
          mp.nstr(f2m(m_tau), 7), "—"))
    print()

    print_summary(checks)

    n_pass = sum(1 for _, s in checks if s == "PASS")
    n_fail = sum(1 for _, s in checks if s == "FAIL")

    print()
    if n_fail == 0:
        print("  DERIVATION LIBRARY: OPERATIONAL")
    else:
        print("  DERIVATION LIBRARY: %d FAILURES — INVESTIGATE" % n_fail)
        for tag, status in checks:
            if status == "FAIL":
                print("    - %s" % tag)

    print()
    print("=" * 70)
    print("PHYS24_DERIVATIONS SELF-TEST COMPLETE")
    print("=" * 70)

