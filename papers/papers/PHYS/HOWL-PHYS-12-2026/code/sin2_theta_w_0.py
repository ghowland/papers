#!/usr/bin/env python3
"""
HOWL: sin²θ_W from 3/8 + Running & Gap Ratio Enumeration
==========================================================

Phase 1: Extract SM couplings at M_Z from DATA-3
Phase 2: Run up to M_GUT, predict sin²θ_W(M_Z) from 3/8
Phase 3: Verify MSSM (hard gate)
Phase 4: Enumerate BSM candidates
Phase 5: Results table
"""

from fractions import Fraction
from mpmath import mp, mpf, log as mlog, pi as mpi, sqrt as msqrt

mp.dps = 100

def f2m(f):
    return mpf(f.numerator) / mpf(f.denominator)

# ================================================================
# DATA-3 INPUTS
# ================================================================

alpha_inv = Fraction(137035999177, 10**9)    # 137.035999177
s2w       = Fraction(23122, 100000)           # 0.23122
alpha_s   = Fraction(1180, 10000)             # 0.1180
M_Z_GeV   = Fraction(911876, 10000)           # 91.1876 GeV
m_t_GeV   = Fraction(172570, 1000)            # 172.570 GeV

alpha_em = Fraction(1, 1) / alpha_inv
c2w = Fraction(1, 1) - s2w  # cos²θ_W

print("=" * 78)
print("HOWL: sin²θ_W FROM 3/8 + RUNNING & GAP RATIO ENUMERATION")
print("=" * 78)
print()

# ================================================================
# PHASE 1: EXTRACT COUPLINGS AT M_Z (GUT normalization)
# ================================================================

print("PHASE 1: SM GAUGE COUPLINGS AT M_Z")
print("-" * 78)
print()

# GUT normalization: α₁ = (5/3) × α_Y = (5/3) × α_em / cos²θ_W
# Standard:          α₂ = α_em / sin²θ_W
#                    α₃ = α_s

alpha_1 = Fraction(5, 3) * alpha_em / c2w
alpha_2 = alpha_em / s2w
alpha_3 = alpha_s

inv_a1 = Fraction(1, 1) / alpha_1
inv_a2 = Fraction(1, 1) / alpha_2
inv_a3 = Fraction(1, 1) / alpha_3

print(f"  α₁(M_Z) = (5/3) × α_em / cos²θ_W")
print(f"           = (5/3) × {float(alpha_em):.10e} / {float(c2w):.8f}")
print(f"           = {float(alpha_1):.10e}")
print(f"  1/α₁    = {float(inv_a1):.6f}")
print()
print(f"  α₂(M_Z) = α_em / sin²θ_W")
print(f"           = {float(alpha_em):.10e} / {float(s2w):.8f}")
print(f"           = {float(alpha_2):.10e}")
print(f"  1/α₂    = {float(inv_a2):.6f}")
print()
print(f"  α₃(M_Z) = α_s = {float(alpha_3):.8f}")
print(f"  1/α₃    = {float(inv_a3):.6f}")
print()

# Verify: sin²θ_W = (3/5)α₁ / ((3/5)α₁ + α₂)
s2w_check = Fraction(3, 5) * alpha_1 / (Fraction(3, 5) * alpha_1 + alpha_2)
print(f"  GATE 1: sin²θ_W from coupling ratio")
print(f"    (3/5)α₁ / ((3/5)α₁ + α₂) = {float(s2w_check):.10f}")
print(f"    Input sin²θ_W              = {float(s2w):.10f}")
diff = abs(float(s2w_check) - float(s2w))
if diff < 1e-8:
    print(f"    PASS (diff = {diff:.2e})")
else:
    print(f"    FAIL (diff = {diff:.2e}) — normalization error!")
print()

# ================================================================
# PHASE 2: SM RUNNING TO M_GUT
# ================================================================

print("PHASE 2: SM RUNNING (one-loop, 6-flavor)")
print("-" * 78)
print()

# SM beta coefficients (GUT normalization for α₁)
b1 = Fraction(41, 10)    # U(1)_Y with 5/3 normalization
b2 = Fraction(-19, 6)    # SU(2)_L
b3 = Fraction(-7, 1)     # SU(3)_c

print(f"  Beta coefficients (SM, one-loop):")
print(f"    b₁ = {b1} = {float(b1):.6f}  (U(1), not AF)")
print(f"    b₂ = {b2} = {float(b2):.6f}  (SU(2), AF)")
print(f"    b₃ = {b3} = {float(b3):.6f}  (SU(3), AF)")
print()

# Gap ratio from PHYS-5
gap_SM = (b1 - b2) / (b2 - b3)
print(f"  SM gap ratio: (b₁−b₂)/(b₂−b₃) = ({b1}-({b2})) / (({b2})-({b3}))")
print(f"    = {b1 - b2} / {b2 - b3}")
print(f"    = {gap_SM} = {float(gap_SM):.6f}")
print(f"  Measured gap ratio: ~1.395")
print(f"  Miss: {float(gap_SM) / 1.395:.4f}x ({(float(gap_SM)/1.395 - 1)*100:.1f}%)")
print()

# Running formula: 1/α_i(μ) = 1/α_i(M_Z) − b_i/(2π) × ln(μ/M_Z)
# Find M_GUT where α₁ = α₂ (first crossing):
# 1/α₁(M_GUT) = 1/α₂(M_GUT)
# 1/α₁(M_Z) − b₁/(2π) × L = 1/α₂(M_Z) − b₂/(2π) × L
# where L = ln(M_GUT/M_Z)
# L × (b₁ − b₂)/(2π) = 1/α₁(M_Z) − 1/α₂(M_Z)
# L = 2π × (1/α₁ − 1/α₂) / (b₁ − b₂)

inv_a1_mpf = f2m(inv_a1)
inv_a2_mpf = f2m(inv_a2)
inv_a3_mpf = f2m(inv_a3)
b1_mpf = f2m(b1)
b2_mpf = f2m(b2)
b3_mpf = f2m(b3)

L_12 = 2 * mpi * (inv_a1_mpf - inv_a2_mpf) / (b1_mpf - b2_mpf)

M_GUT_over_MZ = mpf(10)**( L_12 / mlog(10) )  # exp(L) but compute via log10
M_GUT_GeV = M_GUT_over_MZ * f2m(M_Z_GeV)

print(f"  M_GUT (where α₁ = α₂):")
print(f"    ln(M_GUT/M_Z) = 2π × (1/α₁ − 1/α₂) / (b₁ − b₂)")
print(f"                   = 2π × ({float(inv_a1_mpf):.4f} − {float(inv_a2_mpf):.4f}) / {float(b1_mpf - b2_mpf):.4f}")
print(f"                   = {float(L_12):.6f}")
print(f"    M_GUT/M_Z     = {float(M_GUT_over_MZ):.6e}")
print(f"    M_GUT          = {float(M_GUT_GeV):.4e} GeV")
print(f"    log₁₀(M_GUT)  = {float(mlog(M_GUT_GeV)/mlog(10)):.2f}")
print()

# Value of all three couplings at M_GUT
inv_a1_GUT = inv_a1_mpf - b1_mpf / (2 * mpi) * L_12
inv_a2_GUT = inv_a2_mpf - b2_mpf / (2 * mpi) * L_12
inv_a3_GUT = inv_a3_mpf - b3_mpf / (2 * mpi) * L_12

print(f"  Couplings at M_GUT:")
print(f"    1/α₁(M_GUT) = {float(inv_a1_GUT):.6f}")
print(f"    1/α₂(M_GUT) = {float(inv_a2_GUT):.6f}")
print(f"    1/α₃(M_GUT) = {float(inv_a3_GUT):.6f}")
print(f"    α₁ = α₂ check: diff = {float(abs(inv_a1_GUT - inv_a2_GUT)):.2e}")
print()

# Unification failure: how far is α₃ from α₁=α₂ at M_GUT?
delta_inv_a3 = inv_a3_GUT - inv_a1_GUT
print(f"  Unification failure:")
print(f"    Δ(1/α₃) = 1/α₃(M_GUT) − 1/α₁(M_GUT) = {float(delta_inv_a3):.4f}")
print(f"    α₃ is {'too weak' if delta_inv_a3 > 0 else 'too strong'} at M_GUT")
print()

# Predict sin²θ_W(M_Z) from sin²θ_W(M_GUT) = 3/8
# Run α₁ and α₂ DOWN from M_GUT with α₁(GUT) = α₂(GUT) = α_GUT
# Then compute sin²θ_W(M_Z) = (3/5)α₁(M_Z) / ((3/5)α₁(M_Z) + α₂(M_Z))
# Since we're using SM running from exact unification:
# 1/α_i(M_Z) = 1/α_GUT + b_i/(2π) × L_12  (running DOWN by L_12)
# Wait — running from GUT down to MZ: μ decreases, ln(M_Z/M_GUT) = -L_12
# 1/α_i(M_Z) = 1/α_i(M_GUT) − b_i/(2π) × ln(M_Z/M_GUT)
#             = 1/α_GUT − b_i/(2π) × (−L_12)
#             = 1/α_GUT + b_i/(2π) × L_12

alpha_GUT = 1 / inv_a1_GUT  # = 1/α₂ at GUT, they're equal

# Predicted couplings at M_Z from GUT boundary
inv_a1_pred = inv_a1_GUT + b1_mpf / (2 * mpi) * L_12
inv_a2_pred = inv_a2_GUT + b2_mpf / (2 * mpi) * L_12
inv_a3_pred = inv_a1_GUT + b3_mpf / (2 * mpi) * L_12  # α₃(GUT) = α_GUT from unification

# sin²θ_W predicted
a1_pred = 1 / inv_a1_pred
a2_pred = 1 / inv_a2_pred
s2w_pred = (mpf(3)/5 * a1_pred) / (mpf(3)/5 * a1_pred + a2_pred)

print(f"  Predicted sin²θ_W(M_Z) from 3/8 + SM running:")
print(f"    1/α₁(M_Z) predicted = {float(inv_a1_pred):.6f}  (actual: {float(inv_a1_mpf):.6f})")
print(f"    1/α₂(M_Z) predicted = {float(inv_a2_pred):.6f}  (actual: {float(inv_a2_mpf):.6f})")
print(f"    sin²θ_W predicted    = {float(s2w_pred):.8f}")
print(f"    sin²θ_W measured     = {float(s2w):.8f}")
print(f"    Difference           = {float(s2w_pred - f2m(s2w)):+.6f}")
print(f"    Relative miss        = {(float(s2w_pred)/float(s2w) - 1)*100:+.2f}%")
print()

# Also predict α₃(M_Z) from unification
a3_pred = 1 / inv_a3_pred
print(f"  Predicted α₃(M_Z) from unification:")
print(f"    α₃ predicted = {float(a3_pred):.6f}")
print(f"    α₃ measured  = {float(alpha_s):.6f}")
print(f"    Ratio        = {float(a3_pred)/float(alpha_s):.4f}")
print()

# GATE 2
s2w_miss = abs(float(s2w_pred) - float(s2w))
if 0.01 < s2w_miss < 0.05:
    print(f"  GATE 2: PASS — SM misses sin²θ_W by {s2w_miss:.4f} (~{s2w_miss/float(s2w)*100:.1f}%), expected range")
elif s2w_miss < 0.01:
    print(f"  GATE 2: UNEXPECTED — SM nearly matches?! diff = {s2w_miss:.6f}")
else:
    print(f"  GATE 2: LARGE MISS — diff = {s2w_miss:.4f}, check formulas")
print()

# ================================================================
# PHASE 3: MSSM VERIFICATION (hard gate)
# ================================================================

print("PHASE 3: MSSM VERIFICATION (hard gate)")
print("-" * 78)
print()

# MSSM beta coefficients (known values)
b1_MSSM = Fraction(33, 5)    # = 6.6
b2_MSSM = Fraction(1, 1)     # = 1.0
b3_MSSM = Fraction(-3, 1)    # = -3.0

b1m = f2m(b1_MSSM)
b2m = f2m(b2_MSSM)
b3m = f2m(b3_MSSM)

print(f"  MSSM beta coefficients:")
print(f"    b₁ = {b1_MSSM} = {float(b1_MSSM):.4f}")
print(f"    b₂ = {b2_MSSM} = {float(b2_MSSM):.4f}")
print(f"    b₃ = {b3_MSSM} = {float(b3_MSSM):.4f}")
print()

# MSSM gap ratio
gap_MSSM = (b1_MSSM - b2_MSSM) / (b2_MSSM - b3_MSSM)
print(f"  MSSM gap ratio: {gap_MSSM} = {float(gap_MSSM):.6f}")
print(f"  Target: ~1.0 (exact unification) or measured ~1.395")
print()

# Run with MSSM betas (assume SUSY threshold at M_Z for simplicity)
L_12_MSSM = 2 * mpi * (inv_a1_mpf - inv_a2_mpf) / (b1m - b2m)
M_GUT_MSSM = mpf(10)**(L_12_MSSM / mlog(10)) * f2m(M_Z_GeV)

inv_a1_GUT_M = inv_a1_mpf - b1m / (2 * mpi) * L_12_MSSM
inv_a2_GUT_M = inv_a2_mpf - b2m / (2 * mpi) * L_12_MSSM
inv_a3_GUT_M = inv_a3_mpf - b3m / (2 * mpi) * L_12_MSSM

delta_MSSM = inv_a3_GUT_M - inv_a1_GUT_M

print(f"  MSSM running (SUSY at M_Z approximation):")
print(f"    ln(M_GUT/M_Z)       = {float(L_12_MSSM):.4f}")
print(f"    M_GUT               = {float(M_GUT_MSSM):.4e} GeV")
print(f"    log₁₀(M_GUT)        = {float(mlog(M_GUT_MSSM)/mlog(10)):.2f}")
print(f"    1/α₁(M_GUT)         = {float(inv_a1_GUT_M):.4f}")
print(f"    1/α₂(M_GUT)         = {float(inv_a2_GUT_M):.4f}")
print(f"    1/α₃(M_GUT)         = {float(inv_a3_GUT_M):.4f}")
print(f"    Δ(1/α₃)             = {float(delta_MSSM):.4f}")
print(f"    Unification quality  = {abs(float(delta_MSSM))/float(inv_a1_GUT_M)*100:.2f}% miss")
print()

# MSSM sin²θ_W prediction
a1_pred_M = 1 / (inv_a1_GUT_M + b1m / (2 * mpi) * L_12_MSSM)
a2_pred_M = 1 / (inv_a2_GUT_M + b2m / (2 * mpi) * L_12_MSSM)
s2w_pred_M = (mpf(3)/5 * a1_pred_M) / (mpf(3)/5 * a1_pred_M + a2_pred_M)
print(f"  MSSM sin²θ_W prediction: {float(s2w_pred_M):.8f}")
print(f"  (Should match input since we used same M_Z couplings)")
print()

# GATE 3: MSSM should approximately unify (Δ < 5 in 1/α units)
if abs(float(delta_MSSM)) < 5:
    print(f"  GATE 3: PASS — MSSM unification Δ(1/α₃) = {float(delta_MSSM):.2f}")
    print(f"  (Known result: MSSM nearly unifies, small threshold corrections fix the rest)")
else:
    print(f"  GATE 3: FAIL — MSSM Δ(1/α₃) = {float(delta_MSSM):.2f}, expected < 5")
    print(f"  CHECK FORMULA SIGNS AND CONVENTIONS")
print()

# ================================================================
# PHASE 4: BSM ENUMERATION
# ================================================================

print("PHASE 4: BSM PARTICLE CONTENT ENUMERATION")
print("-" * 78)
print()
print("  For each candidate, compute modified beta coefficients and")
print("  the resulting gap ratio and sin²θ_W prediction.")
print()

# BSM candidates with their (Δb₁, Δb₂, Δb₃) contributions
# Format: (name, spin, (R3, R2, Y), Δb₁, Δb₂, Δb₃, notes)
#
# Conventions:
#   - Δb values are for ONE copy of the multiplet
#   - Complex scalar: Δb_i computed from Dynkin index and dimension
#   - Weyl fermion: 2× the scalar contribution
#   - Vector-like fermion (L+R): 2× Weyl = 4× scalar
#
# Sources: Martin "SUSY Primer" Table 9.1, Langacker "Grand Unification"
# Verified: MSSM = SM + all SUSY partners gives b = (33/5, 1, -3)

candidates = [
    # (name, Δb₁, Δb₂, Δb₃, description)

    # === Scalars ===
    ("Scalar (1,2,1/2)",
     Fraction(1, 10), Fraction(1, 6), Fraction(0, 1),
     "Extra Higgs doublet (2HDM)"),

    ("Scalar (3,1,-1/3)",
     Fraction(1, 15), Fraction(0, 1), Fraction(1, 6),
     "Color triplet scalar (SU(5) partner)"),

    ("Scalar (3,2,1/6)",
     Fraction(1, 30), Fraction(1, 2), Fraction(1, 6),
     "Scalar leptoquark doublet"),

    ("Scalar (1,3,0)",
     Fraction(0, 1), Fraction(1, 3), Fraction(0, 1),
     "Scalar SU(2) triplet (Type-II seesaw)"),

    ("Scalar (8,1,0)",
     Fraction(0, 1), Fraction(0, 1), Fraction(1, 2),
     "Color octet scalar"),

    ("Scalar (3,1,-4/3)",
     Fraction(16, 15), Fraction(0, 1), Fraction(1, 6),
     "Color triplet scalar Q=-4/3"),

    ("Scalar (1,2,3/2)",
     Fraction(9, 10), Fraction(1, 6), Fraction(0, 1),
     "Doubly-charged scalar doublet"),

    # === Vector-like fermions (L + R) ===
    ("VL fermion (1,2,-1/2)",
     Fraction(2, 10), Fraction(2, 6), Fraction(0, 1),
     "Vector-like lepton doublet"),

    ("VL fermion (3,2,1/6)",
     Fraction(1, 15), Fraction(1, 1), Fraction(1, 3),
     "Vector-like quark doublet"),

    ("VL fermion (1,1,-1)",
     Fraction(2, 5), Fraction(0, 1), Fraction(0, 1),
     "Vector-like charged singlet lepton"),

    ("VL fermion (3,1,-1/3)",
     Fraction(2, 15), Fraction(0, 1), Fraction(1, 3),
     "Vector-like down-type singlet quark"),

    ("VL fermion (3,1,2/3)",
     Fraction(8, 15), Fraction(0, 1), Fraction(1, 3),
     "Vector-like up-type singlet quark"),

    # === Complete SU(5) multiplets ===
    ("SU(5) 5+5bar (fermion)",
     Fraction(2, 5), Fraction(1, 1), Fraction(1, 3),
     "Complete 5-plet: (3,1,-1/3) + (1,2,1/2) fermion"),

    ("SU(5) 10+10bar (fermion)",
     Fraction(6, 5), Fraction(1, 1), Fraction(1, 1),
     "Complete 10-plet: (3,2,1/6)+(3bar,1,-2/3)+(1,1,1) fermion"),

    # === Multiple copies ===
    ("2× Scalar (1,2,1/2)",
     Fraction(2, 10), Fraction(2, 6), Fraction(0, 1),
     "Two extra Higgs doublets"),

    ("3× Scalar (1,2,1/2)",
     Fraction(3, 10), Fraction(3, 6), Fraction(0, 1),
     "Three extra Higgs doublets"),
]

# Also test complete MSSM as sanity check
# MSSM adds: all SM partners → Δb = (33/5 - 41/10, 1 - (-19/6), -3 - (-7))
#           = (66/10 - 41/10, 1 + 19/6, -3 + 7) = (25/10, 25/6, 4)
#           = (5/2, 25/6, 4)
candidates.append((
    "Full MSSM spectrum",
    Fraction(5, 2), Fraction(25, 6), Fraction(4, 1),
    "All SUSY partners (gate check)"
))

# Target gap ratio from measured couplings
# The measured gap ratio uses actual 1/α values:
# gap_meas = (1/α₁ - 1/α₂) / (1/α₂ - 1/α₃) at M_Z
gap_meas_num = inv_a1_mpf - inv_a2_mpf
gap_meas_den = inv_a2_mpf - inv_a3_mpf
gap_meas = gap_meas_num / gap_meas_den
print(f"  Measured gap ratio from DATA-3 couplings:")
print(f"    (1/α₁ − 1/α₂) / (1/α₂ − 1/α₃) = {float(gap_meas):.6f}")
print()

# For each BSM candidate, the gap ratio becomes:
# gap = (b₁+Δb₁ − b₂−Δb₂) / (b₂+Δb₂ − b₃−Δb₃)

print(f"  {'Candidate':<30s} {'Δb₁':>8s} {'Δb₂':>8s} {'Δb₃':>8s} {'Gap':>8s} {'vs 1.40':>8s} {'M_GUT':>10s}")
print(f"  {'-'*30} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*10}")

results = []

for name, db1, db2, db3, desc in candidates:
    b1_new = b1 + db1
    b2_new = b2 + db2
    b3_new = b3 + db3

    # Gap ratio
    num = b1_new - b2_new
    den = b2_new - b3_new
    if den == 0:
        gap = None
        gap_f = float('inf')
    else:
        gap = num / den
        gap_f = float(gap)

    # M_GUT from α₁ = α₂ crossing
    b1n = f2m(b1_new)
    b2n = f2m(b2_new)
    b3n = f2m(b3_new)

    denom_L = b1n - b2n
    if abs(float(denom_L)) < 1e-20:
        L_val = mpf('inf')
        M_GUT_val = mpf('inf')
        log_MGUT = float('inf')
    else:
        L_val = 2 * mpi * (inv_a1_mpf - inv_a2_mpf) / denom_L
        if float(L_val) > 0:
            M_GUT_val = mpf(10)**(L_val / mlog(10)) * f2m(M_Z_GeV)
            log_MGUT = float(mlog(M_GUT_val) / mlog(10))
        else:
            M_GUT_val = mpf(0)
            log_MGUT = 0

    # Distance from measured gap ratio
    dist = abs(gap_f - float(gap_meas)) if gap is not None else float('inf')

    results.append((name, float(db1), float(db2), float(db3), gap_f, dist, log_MGUT, desc))

    # Print
    mgut_str = f"{log_MGUT:.1f}" if 0 < log_MGUT < 100 else "N/A"
    gap_str = f"{gap_f:.4f}" if gap is not None and abs(gap_f) < 100 else "N/A"
    dist_str = f"{dist:+.4f}" if dist < 100 else "N/A"

    print(f"  {name:<30s} {float(db1):>8.4f} {float(db2):>8.4f} {float(db3):>8.4f} {gap_str:>8s} {dist_str:>8s} {mgut_str:>10s}")

print()

# ================================================================
# PHASE 5: SORTED RESULTS
# ================================================================

print("PHASE 5: RESULTS SORTED BY DISTANCE FROM MEASURED GAP RATIO")
print("-" * 78)
print()

results_sorted = sorted(results, key=lambda x: x[5])

print(f"  Measured gap ratio: {float(gap_meas):.6f}")
print(f"  SM gap ratio:       {float(gap_SM):.6f} (218/115)")
print()
print(f"  {'Rank':<5s} {'Candidate':<30s} {'Gap ratio':>10s} {'Distance':>10s} {'log₁₀M_GUT':>12s}")
print(f"  {'-'*5} {'-'*30} {'-'*10} {'-'*10} {'-'*12}")

for i, (name, db1, db2, db3, gap_f, dist, log_MGUT, desc) in enumerate(results_sorted):
    gap_str = f"{gap_f:.4f}" if abs(gap_f) < 100 else "N/A"
    dist_str = f"{dist:.4f}" if dist < 100 else "N/A"
    mgut_str = f"{log_MGUT:.1f}" if 0 < log_MGUT < 100 else "N/A"
    flag = " <--" if dist < 0.05 else " *" if dist < 0.2 else ""
    print(f"  {i+1:<5d} {name:<30s} {gap_str:>10s} {dist_str:>10s} {mgut_str:>12s}{flag}")

print()

# ================================================================
# PHASE 6: ANALYSIS
# ================================================================

print("PHASE 6: ANALYSIS")
print("-" * 78)
print()

# Best candidates
best = [r for r in results_sorted if r[5] < 0.2]

if best:
    print(f"  Candidates within 0.2 of measured gap ratio ({float(gap_meas):.4f}):")
    print()
    for name, db1, db2, db3, gap_f, dist, log_MGUT, desc in best:
        print(f"    {name}")
        print(f"      {desc}")
        print(f"      Δb = ({db1:.4f}, {db2:.4f}, {db3:.4f})")
        print(f"      Gap ratio = {gap_f:.6f}, distance = {dist:.6f}")
        print(f"      M_GUT ~ 10^{log_MGUT:.1f} GeV")
        # Check proton decay constraint: M_GUT > 10^{15.5} GeV
        if log_MGUT > 15.5:
            print(f"      Proton decay: SAFE (M_GUT > 10^15.5)")
        elif log_MGUT > 0:
            print(f"      Proton decay: EXCLUDED (M_GUT < 10^15.5)")
        print()
else:
    print(f"  No single-multiplet extension matches gap ratio within 0.2")
    print(f"  The SM gap ratio ({float(gap_SM):.4f}) is far from measured ({float(gap_meas):.4f})")
    print(f"  Multiple new particles or a complete framework (like MSSM) may be needed")
    print()

# SM vs MSSM summary
print(f"  SUMMARY:")
print(f"    SM:   gap = {float(gap_SM):.4f}, sin²θ_W(pred) = {float(s2w_pred):.6f}, miss = {float(s2w_pred - f2m(s2w)):+.4f}")
mssm_result = [r for r in results if r[0] == "Full MSSM spectrum"][0]
print(f"    MSSM: gap = {mssm_result[4]:.4f}, Δ(1/α₃) = {float(delta_MSSM):.2f}")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 78)
print("CHECKS")
print("=" * 78)
print()

checks = []
def chk(name, cond, detail=""):
    s = "PASS" if cond else "FAIL"
    checks.append((name, s))
    print(f"  [{s}] {name}")
    if detail: print(f"        {detail}")

chk("Gate 1: sin²θ_W from couplings",
    abs(float(s2w_check) - float(s2w)) < 1e-8,
    f"diff = {abs(float(s2w_check) - float(s2w)):.2e}")

chk("Gate 2: SM sin²θ_W miss in range [0.01, 0.05]",
    0.01 < s2w_miss < 0.05,
    f"miss = {s2w_miss:.4f}")

chk("Gate 3: MSSM Δ(1/α₃) < 5",
    abs(float(delta_MSSM)) < 5,
    f"Δ = {float(delta_MSSM):.2f}")

chk("SM gap ratio = 218/115",
    abs(float(gap_SM) - 218/115) < 1e-10,
    f"gap = {float(gap_SM):.10f}")

chk("1/α₁ = 1/α₂ at M_GUT",
    abs(float(inv_a1_GUT - inv_a2_GUT)) < 1e-8,
    f"diff = {float(abs(inv_a1_GUT - inv_a2_GUT)):.2e}")

chk("M_GUT > 10^13 GeV",
    float(mlog(M_GUT_GeV)/mlog(10)) > 13,
    f"log₁₀(M_GUT) = {float(mlog(M_GUT_GeV)/mlog(10)):.2f}")

chk("SM sin²θ_W prediction < measured (expected for SM)",
    float(s2w_pred) < float(s2w),
    f"predicted {float(s2w_pred):.6f} < measured {float(s2w):.6f}")

print()
n_pass = sum(1 for _, s in checks if s == "PASS")
n_fail = sum(1 for _, s in checks if s == "FAIL")
print(f"  TOTAL: {n_pass} PASS, {n_fail} FAIL out of {len(checks)}")
print()

print("=" * 78)
print("SCRIPT COMPLETE")
print("=" * 78)
