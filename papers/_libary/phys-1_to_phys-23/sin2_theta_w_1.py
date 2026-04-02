#!/usr/bin/env python3
"""
HOWL GUT RUNNING NOTEBOOK: sin²θ_W from 3/8 & Gap Ratio Enumeration
=====================================================================

Registry: [@HOWL-GUT-NOTEBOOK-2026]
Date: April 1 2026
Status: COMPLETE. Findings recorded. No parameter derivation achieved.

This notebook records the gauge coupling unification computation.
SM beta coefficients (exact rationals from the gauge group) run the
three couplings from M_Z toward M_GUT. The overconstrained system
(3 equations, 2 unknowns) tests whether the SM unifies.

FINDINGS:
  1. SM gap ratio = 218/115 = 1.896. Measured = 1.358. Miss = 36%.
     The SM does not unify at one loop.
  2. SM unification failure: Δ(1/α₃) = −6.58 at M_GUT = 10^13.8 GeV.
     α₃ is too strong at the would-be unification point.
  3. SM prediction of sin²θ_W from unification is ~0.21 (known textbook
     result), missing measured 0.23122 by ~10%. Equivalent to Finding 1
     seen from a different angle — both test the same overconstrained system.
  4. MSSM gap ratio = 7/5 = 1.400 (exact). Δ(1/α₃) = −0.69 at
     M_GUT = 10^17.3 GeV. Near-perfect unification, threshold corrections
     close the remaining gap. Known result, reproduced as gate check.
  5. A SINGLE vector-like quark doublet (3,2,1/6) achieves gap ratio 1.407,
     distance 0.049 from measured — comparable to the full MSSM (distance
     0.042). M_GUT = 10^15.5, at the proton decay boundary. Testable by
     Hyper-Kamiokande. This is the minimal single-multiplet extension.
  6. No other single multiplet comes within 0.12 of the measured gap ratio.
     The next-best (SU(5) 5+5bar fermion) has gap 1.481 and M_GUT = 10^14.9,
     excluded by proton decay.

WHAT THIS DOES NOT DO:
  sin²θ_W is not derived. The gap ratio test and sin²θ_W prediction are
  equivalent — both test whether three lines meet at a point. The SM fails
  both by the same 36%. The computation constrains what BSM content is needed
  but does not determine it uniquely. The parameter count stays at 17.

INTEGER CONTENT:
  b₁ = 41/10 from U(1)_Y with 5/3 GUT normalization
  b₂ = −19/6 from SU(2)_L
  b₃ = −7 from SU(3)_c
  Gap ratio = (b₁−b₂)/(b₂−b₃) = 218/115 — pure rational from gauge group
  MSSM gap = (33/5−1)/(1+3) = (28/5)/4 = 7/5 — pure rational
  All beta coefficients trace to gauge group representations and generation count.
"""

from fractions import Fraction
from mpmath import mp, mpf, log as mlog, pi as mpi

mp.dps = 100

def f2m(f):
    return mpf(f.numerator) / mpf(f.denominator)

# ================================================================
# DATA-3 INPUTS
# ================================================================

alpha_inv = Fraction(137035999177, 10**9)
s2w       = Fraction(23122, 100000)
alpha_s   = Fraction(1180, 10000)
M_Z_GeV   = Fraction(911876, 10000)

alpha_em = Fraction(1, 1) / alpha_inv
c2w = Fraction(1, 1) - s2w

print("=" * 72)
print("HOWL GUT RUNNING NOTEBOOK")
print("=" * 72)
print()

# ================================================================
# RESULT 1: SM COUPLINGS AT M_Z
# ================================================================

print("RESULT 1: SM GAUGE COUPLINGS AT M_Z (GUT normalization)")
print("-" * 72)
print()

alpha_1 = Fraction(5, 3) * alpha_em / c2w
alpha_2 = alpha_em / s2w
alpha_3 = alpha_s

inv_a1 = f2m(Fraction(1, 1) / alpha_1)
inv_a2 = f2m(Fraction(1, 1) / alpha_2)
inv_a3 = f2m(Fraction(1, 1) / alpha_3)

print(f"  1/α₁(M_Z) = {float(inv_a1):.6f}  (U(1)_Y, GUT normalized)")
print(f"  1/α₂(M_Z) = {float(inv_a2):.6f}  (SU(2)_L)")
print(f"  1/α₃(M_Z) = {float(inv_a3):.6f}  (SU(3)_c)")
print()

# Verify normalization
s2w_check = f2m(Fraction(3, 5) * alpha_1 / (Fraction(3, 5) * alpha_1 + alpha_2))
diff = abs(float(s2w_check) - float(s2w))
print(f"  Normalization check: (3/5)α₁/((3/5)α₁+α₂) = {float(s2w_check):.10f}")
print(f"  Input sin²θ_W = {float(s2w):.10f}, diff = {diff:.2e}")
if diff < 1e-8:
    print(f"  PASS")
else:
    print(f"  FAIL — normalization error")
print()

# ================================================================
# RESULT 2: BETA COEFFICIENTS AND GAP RATIO
# ================================================================

print("RESULT 2: BETA COEFFICIENTS (exact rationals)")
print("-" * 72)
print()

b1 = Fraction(41, 10)
b2 = Fraction(-19, 6)
b3 = Fraction(-7, 1)

gap_SM = (b1 - b2) / (b2 - b3)

print(f"  SM one-loop (6-flavor, GUT normalization):")
print(f"    b₁ = {b1} = {float(b1):.6f}  [U(1)_Y]")
print(f"    b₂ = {b2} = {float(b2):.6f}  [SU(2)_L]")
print(f"    b₃ = {b3} = {float(b3):.6f}  [SU(3)_c]")
print()
print(f"  Gap ratio = (b₁−b₂)/(b₂−b₃)")
print(f"    b₁ − b₂ = {b1 - b2} = {float(b1 - b2):.6f}")
print(f"    b₂ − b₃ = {b2 - b3} = {float(b2 - b3):.6f}")
print(f"    Ratio = {gap_SM} = {float(gap_SM):.6f}")
print()

gap_meas = (inv_a1 - inv_a2) / (inv_a2 - inv_a3)
print(f"  Measured gap ratio from DATA-3 couplings:")
print(f"    (1/α₁ − 1/α₂)/(1/α₂ − 1/α₃) = {float(gap_meas):.6f}")
print()
print(f"  SM prediction: {float(gap_SM):.6f}")
print(f"  Measured:       {float(gap_meas):.6f}")
print(f"  Miss:           {(float(gap_SM)/float(gap_meas) - 1)*100:.1f}%")
print(f"  THE SM DOES NOT UNIFY.")
print()

# ================================================================
# RESULT 3: SM RUNNING TO M_GUT
# ================================================================

print("RESULT 3: SM RUNNING")
print("-" * 72)
print()

# 1/α_i(μ) = 1/α_i(M_Z) − b_i/(2π) × ln(μ/M_Z)
# M_GUT defined by α₁ = α₂:
# L = 2π(1/α₁ − 1/α₂)/(b₁ − b₂)

b1m, b2m, b3m = f2m(b1), f2m(b2), f2m(b3)
L_12 = 2 * mpi * (inv_a1 - inv_a2) / (b1m - b2m)
M_GUT_GeV = mpf(10)**(L_12 / mlog(10)) * f2m(M_Z_GeV)
log_MGUT = float(mlog(M_GUT_GeV) / mlog(10))

inv_a1_GUT = inv_a1 - b1m / (2 * mpi) * L_12
inv_a2_GUT = inv_a2 - b2m / (2 * mpi) * L_12
inv_a3_GUT = inv_a3 - b3m / (2 * mpi) * L_12

delta_a3 = float(inv_a3_GUT - inv_a1_GUT)

print(f"  M_GUT (α₁ = α₂ crossing): 10^{log_MGUT:.2f} GeV")
print(f"  ln(M_GUT/M_Z) = {float(L_12):.4f}")
print()
print(f"  At M_GUT:")
print(f"    1/α₁ = {float(inv_a1_GUT):.4f}")
print(f"    1/α₂ = {float(inv_a2_GUT):.4f}  (= 1/α₁ by construction)")
print(f"    1/α₃ = {float(inv_a3_GUT):.4f}")
print(f"    Δ(1/α₃) = {delta_a3:.4f}")
print(f"    α₃ is {'too strong' if delta_a3 < 0 else 'too weak'} at M_GUT")
print()

# ================================================================
# RESULT 4: sin²θ_W PREDICTION STATUS
# ================================================================

print("RESULT 4: sin²θ_W PREDICTION FROM 3/8")
print("-" * 72)
print()
print("  The GUT prediction sin²θ_W(M_GUT) = 3/8 = 0.375, run down to M_Z")
print("  by SM beta functions, gives sin²θ_W(M_Z) ≈ 0.21 (textbook result).")
print("  This misses the measured 0.23122 by ~10%.")
print()
print("  This is EQUIVALENT to the gap ratio test, not independent of it.")
print("  Both test whether three lines (1/α_i vs ln μ) meet at a point.")
print("  The gap ratio tests the slopes. The sin²θ_W prediction tests the")
print("  intercepts. If one fails by 36%, the other fails by ~10%.")
print()
print("  A proper computation would solve:")
print("    [(3/5)(1−s²)/α_em − 1/α_s] / [s²/α_em − 1/α_s] = R₁₃")
print("  where R₁₃ = (b₁−b₃)/(b₂−b₃) for sin²θ_W, using α_em and α_s")
print("  as inputs and predicting sin²θ_W as output.")
print()
print("  This was not computed due to equivalence with the gap ratio test.")
print("  The gap ratio is the cleaner formulation: a ratio of exact rationals")
print("  (218/115) compared to a measured number (1.358). No α_s correction")
print("  term obscures the integer content.")
print()

# ================================================================
# RESULT 5: MSSM GATE CHECK
# ================================================================

print("RESULT 5: MSSM VERIFICATION")
print("-" * 72)
print()

b1_M = Fraction(33, 5)
b2_M = Fraction(1, 1)
b3_M = Fraction(-3, 1)
gap_MSSM = (b1_M - b2_M) / (b2_M - b3_M)

b1Mm, b2Mm, b3Mm = f2m(b1_M), f2m(b2_M), f2m(b3_M)
L_MSSM = 2 * mpi * (inv_a1 - inv_a2) / (b1Mm - b2Mm)
M_GUT_MSSM = mpf(10)**(L_MSSM / mlog(10)) * f2m(M_Z_GeV)
log_MGUT_M = float(mlog(M_GUT_MSSM) / mlog(10))

inv_a1_M = inv_a1 - b1Mm / (2 * mpi) * L_MSSM
inv_a3_M = inv_a3 - b3Mm / (2 * mpi) * L_MSSM
delta_MSSM = float(inv_a3_M - inv_a1_M)

print(f"  MSSM beta coefficients:")
print(f"    b₁ = {b1_M} = {float(b1_M):.4f}")
print(f"    b₂ = {b2_M} = {float(b2_M):.4f}")
print(f"    b₃ = {b3_M} = {float(b3_M):.4f}")
print()
print(f"  MSSM gap ratio = {gap_MSSM} = {float(gap_MSSM):.6f}")
print(f"  M_GUT = 10^{log_MGUT_M:.2f} GeV")
print(f"  Δ(1/α₃) = {delta_MSSM:.4f}")
print(f"  Unification quality: {abs(delta_MSSM)/float(inv_a1_M)*100:.2f}% miss")
print()
if abs(delta_MSSM) < 5:
    print(f"  GATE PASS — MSSM nearly unifies (known result)")
else:
    print(f"  GATE FAIL — check formulas")
print()

# ================================================================
# RESULT 6: BSM ENUMERATION (main finding)
# ================================================================

print("RESULT 6: BSM PARTICLE CONTENT — GAP RATIO SCAN")
print("-" * 72)
print()

candidates = [
    ("Scalar (1,2,1/2)",        Fraction(1,10),  Fraction(1,6),   Fraction(0,1),  "Extra Higgs doublet"),
    ("Scalar (3,1,-1/3)",       Fraction(1,15),  Fraction(0,1),   Fraction(1,6),  "Color triplet scalar"),
    ("Scalar (3,2,1/6)",        Fraction(1,30),  Fraction(1,2),   Fraction(1,6),  "Scalar leptoquark"),
    ("Scalar (1,3,0)",          Fraction(0,1),   Fraction(1,3),   Fraction(0,1),  "SU(2) triplet scalar"),
    ("Scalar (8,1,0)",          Fraction(0,1),   Fraction(0,1),   Fraction(1,2),  "Color octet scalar"),
    ("VL fermion (1,2,-1/2)",   Fraction(2,10),  Fraction(2,6),   Fraction(0,1),  "Vector-like lepton doublet"),
    ("VL fermion (3,2,1/6)",    Fraction(1,15),  Fraction(1,1),   Fraction(1,3),  "Vector-like quark doublet"),
    ("VL fermion (1,1,-1)",     Fraction(2,5),   Fraction(0,1),   Fraction(0,1),  "VL charged singlet lepton"),
    ("VL fermion (3,1,-1/3)",   Fraction(2,15),  Fraction(0,1),   Fraction(1,3),  "VL down-type singlet"),
    ("VL fermion (3,1,2/3)",    Fraction(8,15),  Fraction(0,1),   Fraction(1,3),  "VL up-type singlet"),
    ("SU(5) 5+5bar fermion",    Fraction(2,5),   Fraction(1,1),   Fraction(1,3),  "Complete 5-plet pair"),
    ("SU(5) 10+10bar fermion",  Fraction(6,5),   Fraction(1,1),   Fraction(1,1),  "Complete 10-plet pair"),
    ("2× Scalar (1,2,1/2)",     Fraction(2,10),  Fraction(2,6),   Fraction(0,1),  "Two extra Higgs doublets"),
    ("3× Scalar (1,2,1/2)",     Fraction(3,10),  Fraction(3,6),   Fraction(0,1),  "Three extra Higgs doublets"),
    ("Full MSSM",               Fraction(5,2),   Fraction(25,6),  Fraction(4,1),  "All SUSY partners"),
]

results = []

for name, db1, db2, db3, desc in candidates:
    b1n = b1 + db1
    b2n = b2 + db2
    b3n = b3 + db3

    num = b1n - b2n
    den = b2n - b3n
    if den != 0:
        gap = float(num / den)
    else:
        gap = float('inf')

    b1f, b2f = f2m(b1n), f2m(b2n)
    denom_L = b1f - b2f
    if abs(float(denom_L)) > 1e-20 and float(denom_L) != 0:
        L = 2 * mpi * (inv_a1 - inv_a2) / denom_L
        if float(L) > 0:
            lgut = float(mlog(mpf(10)**(L/mlog(10)) * f2m(M_Z_GeV)) / mlog(10))
        else:
            lgut = 0
    else:
        lgut = 0

    dist = abs(gap - float(gap_meas))
    results.append((name, float(db1), float(db2), float(db3), gap, dist, lgut, desc))

results_sorted = sorted(results, key=lambda x: x[5])

print(f"  Measured gap ratio: {float(gap_meas):.6f}")
print(f"  SM gap ratio:       {float(gap_SM):.6f} (= 218/115)")
print()
print(f"  {'Rank':<5} {'Candidate':<28} {'Gap':>8} {'Dist':>8} {'log M_GUT':>10} {'Note':>8}")
print(f"  {'-'*5} {'-'*28} {'-'*8} {'-'*8} {'-'*10} {'-'*8}")

for i, (name, db1, db2, db3, gap, dist, lgut, desc) in enumerate(results_sorted):
    gs = f"{gap:.4f}" if abs(gap) < 100 else "N/A"
    ds = f"{dist:.4f}" if dist < 100 else "N/A"
    ls = f"{lgut:.1f}" if 0 < lgut < 100 else "N/A"
    flag = "<--" if dist < 0.05 else "*" if dist < 0.15 else ""
    safe = "safe" if lgut > 15.5 else "excl" if lgut > 0 else ""
    print(f"  {i+1:<5} {name:<28} {gs:>8} {ds:>8} {ls:>10} {flag:>4} {safe}")

print()

# ================================================================
# RESULT 7: THE FINDING
# ================================================================

print("RESULT 7: THE FINDING")
print("-" * 72)
print()

best = [(n, g, d, l, desc) for n, _, _, _, g, d, l, desc in results_sorted if d < 0.15]

print("  Candidates within 0.15 of measured gap ratio:")
print()
for name, gap, dist, lgut, desc in best:
    print(f"    {name}")
    print(f"      {desc}")
    print(f"      Gap ratio = {gap:.6f}  (distance = {dist:.6f})")
    print(f"      M_GUT = 10^{lgut:.1f} GeV")
    if lgut > 15.5:
        print(f"      Proton decay: SAFE (M_GUT > 10^15.5)")
    elif lgut > 0:
        print(f"      Proton decay: EXCLUDED (M_GUT < 10^15.5)")
    print()

print("  KEY FINDING: A single vector-like quark doublet (3,2,1/6)")
print("  achieves unification quality comparable to the full MSSM")
print("  (gap distance 0.049 vs 0.042). This is the MINIMAL extension")
print("  of the SM that approximately fixes gauge coupling unification.")
print("  Its M_GUT = 10^15.5 sits at the proton decay boundary,")
print("  making it testable by Hyper-Kamiokande.")
print()
print("  The MSSM remains the best single framework (gap = 7/5 exactly,")
print("  with threshold corrections closing the remaining 0.042 gap).")
print("  But the VL quark doublet shows that unification does NOT require")
print("  the full SUSY spectrum — one new multiplet suffices at one loop.")
print()

# ================================================================
# RESULT 8: INTEGER ANATOMY OF UNIFICATION
# ================================================================

print("RESULT 8: INTEGER ANATOMY")
print("-" * 72)
print()
print("  The entire unification test reduces to comparing two rationals:")
print()
print(f"    SM gap ratio  = (b₁−b₂)/(b₂−b₃) = {b1-b2}/{b2-b3} = {gap_SM}")
print(f"                  = {float(gap_SM):.6f}")
print()
print(f"    MSSM gap ratio = (b₁−b₂)/(b₂−b₃) = {b1_M-b2_M}/{b2_M-b3_M} = {gap_MSSM}")
print(f"                   = {float(gap_MSSM):.6f}")
print()
print(f"    Measured ratio from couplings: {float(gap_meas):.6f}")
print()
print("  The beta coefficients are exact rationals from the gauge group.")
print("  The gap ratio is a ratio of rationals = a rational.")
print("  The measurement is a ratio of inverse couplings.")
print("  Unification is the statement: rational = measured.")
print("  It fails for the SM (218/115 ≠ 1.358) and nearly succeeds")
print("  for the MSSM (7/5 ≈ 1.358 to 3%).")
print()
print("  This is the PHYS-2 thesis at the GUT scale: the transformation")
print("  laws (beta functions) are integers. The coupling values are not.")
print("  Whether the integers are consistent with unification depends on")
print("  which integers (which particle content) nature chose.")
print()

# ================================================================
# DECISIONS AND STATUS
# ================================================================

print("RESULT 9: DECISIONS")
print("-" * 72)
print()
print("  COMPLETED:")
print("    - SM gap ratio = 218/115, miss = 36% from measured")
print("    - MSSM gap ratio = 7/5, Δ(1/α₃) = −0.69 (near-unification)")
print("    - BSM enumeration: VL quark doublet is minimal solution")
print()
print("  NOT COMPUTED (equivalent to gap ratio, no additional content):")
print("    - sin²θ_W prediction from 3/8 + running (~0.21, misses by ~10%)")
print("    - sin²θ_W prediction for each BSM candidate")
print("    - Both test the same overconstrained system from a different angle")
print()
print("  PARAMETER COUNT: Unchanged at 17.")
print("    sin²θ_W is not derived. The gap ratio test shows the SM cannot")
print("    derive it from unification without BSM content. The MSSM or a")
print("    VL quark doublet could derive it, but we don't know which (if")
print("    either) nature chose. This is a Level 2 question: the framework")
print("    identifies WHAT is needed (specific beta function modifications)")
print("    but not which particles provide them.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 72)
print("CHECKS")
print("=" * 72)
print()

checks = []
def chk(name, cond, detail=""):
    s = "PASS" if cond else "FAIL"
    checks.append((name, s))
    print(f"  [{s}] {name}")
    if detail: print(f"        {detail}")

chk("Normalization: sin²θ_W from couplings",
    diff < 1e-8, f"diff = {diff:.2e}")

chk("SM gap ratio = 218/115",
    abs(float(gap_SM) - 218/115) < 1e-10,
    f"{float(gap_SM):.10f}")

chk("MSSM gap ratio = 7/5",
    abs(float(gap_MSSM) - 7/5) < 1e-10,
    f"{float(gap_MSSM):.10f}")

chk("SM does not unify (Δ > 5)",
    abs(delta_a3) > 5,
    f"Δ(1/α₃) = {delta_a3:.2f}")

chk("MSSM nearly unifies (Δ < 5)",
    abs(delta_MSSM) < 5,
    f"Δ(1/α₃) = {delta_MSSM:.2f}")

chk("M_GUT(SM) > 10^13",
    log_MGUT > 13,
    f"log₁₀ = {log_MGUT:.2f}")

chk("M_GUT(MSSM) > 10^16",
    log_MGUT_M > 16,
    f"log₁₀ = {log_MGUT_M:.2f}")

chk("VL quark doublet gap < 0.05 from measured",
    any(d < 0.05 and "VL fermion (3,2" in n for n, _, _, _, _, d, _, _ in results),
    "distance = 0.049")

chk("Measured gap ratio in [1.2, 1.5]",
    1.2 < float(gap_meas) < 1.5,
    f"gap = {float(gap_meas):.6f}")

print()
n_pass = sum(1 for _, s in checks if s == "PASS")
n_fail = sum(1 for _, s in checks if s == "FAIL")
print(f"  TOTAL: {n_pass} PASS, {n_fail} FAIL out of {len(checks)}")
print()

print("=" * 72)
print("GUT RUNNING NOTEBOOK COMPLETE")
print("=" * 72)
