---

The 4 FAILs reveal a critical bug in the script. The gap ratio computation is wrong because I'm adding the VL shifts to b1_SM for all three components instead of to each respective b_i_SM. Let me trace the error:

```python
b_mod_weyl = [b1_SM + vl_weyl[i] for i in range(3)]
```

This adds vl_weyl[0], vl_weyl[1], vl_weyl[2] all to **b1_SM**. It should be:

```python
b_sm = [b1_SM, b2_SM, b3_SM]
b_mod_weyl = [b_sm[i] + vl_weyl[i] for i in range(3)]
```

That's a straightforward indexing bug. The SM betas are three different values but the list comprehension uses b1_SM for all three.

With this fix:
- Library: (41/10 + 1/15, −19/6 + 1, −7 + 1/3) = (25/6, −13/6, −20/3) → gap = 38/27 ✓
- Weyl: (41/10 + 1/15, −19/6 + 1, −7 + 2/3) = (25/6, −13/6, −19/3) → gap = (25/6+13/6)/(−13/6+19/3) = (38/6)/((−13+38)/6) = 38/25. Hmm, not 19/12. Let me recompute: (−13/6+19/3) = (−13+38)/6 = 25/6. So gap = (38/6)/(25/6) = 38/25 = 1.52. Not 19/12.
- Dirac: (41/10 + 2/15, −19/6 + 2, −7 + 4/3) = (127/30, −7/6, −17/3) → numerator = 127/30 + 7/6 = (127+35)/30 = 162/30 = 27/5. Denominator = −7/6 + 17/3 = (−7+34)/6 = 27/6 = 9/2. Gap = (27/5)/(9/2) = 54/45 = 6/5. ✓

So the Weyl gap ratio is 38/25 = 1.52, not 19/12. My supporting tables had an error too. Let me also verify: for Weyl convention the VL pair is one Weyl in (3,2,1/6), so the shifts are (1/15, 1, 2/3). But a VL pair is NOT one Weyl — it's one Dirac = two Weyl. Convention A (one Weyl) doesn't correspond to the physical VL pair. Only Convention B (Dirac) does.

The table with "Convention A applied to the VL" is physically meaningless — you'd never add just one Weyl fermion without its partner. The real question is between Convention B (Dirac, standard) and Convention C (library). Convention A is only useful for summing over chiral SM fermions.

Here is the corrected script:

```python
#!/usr/bin/env python3
"""
HOWL PHYS-25 DEMONSTRATION: Beta Normalization Diagnostic
===========================================================
phys25_beta_normalization.py

Definitive diagnostic: compute SM one-loop betas field-by-field
in two conventions (standard Weyl, library Dynkin) and identify
exactly where the library's VL formulas diverge.

The finding: the library's Dynkin coefficient for SU(3) is 1/3
where the standard Weyl formula gives 2/3. Applied to SM chiral
fermions, Convention C gives b_3_fermion = 2 instead of 4,
yielding b_3_SM = -9 instead of -7. Convention A gives -7.

For the VL pair (one Dirac fermion), only Convention B (Dirac)
is physically correct. Convention C (library) gives Db_3 = 1/3
where Dirac gives 4/3 — a factor of 4 discrepancy.

The gap ratio depends on which convention is used:
  Library (Db_3=1/3): 38/27 = 1.407
  Dirac   (Db_3=4/3): 6/5   = 1.200

Both improve on the SM (218/115 = 1.896), but by different amounts.
An external reference is needed to settle which is correct.

Backed by: sin2_theta_w_1.py (9/9 checks)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *

# ================================================================
# HEADER
# ================================================================

print("=" * 70)
print("HOWL PHYS-25: BETA NORMALIZATION DIAGNOSTIC")
print("=" * 70)
print()

# ================================================================
# THE CONVENTIONS
# ================================================================
# All conventions use d(1/alpha_i)/d(ln mu) = -b_i/(2*pi) - ...
#
# Convention A: "Standard Weyl"
#   For one LEFT-HANDED Weyl fermion in (R_3, R_2, Y):
#     Db_1 = (2/5)*Y^2*d2*d3
#     Db_2 = (2/3)*T2*d3
#     Db_3 = (2/3)*T3*d2
#   Coefficient pattern: (2/5, 2/3, 2/3)
#   Used for: summing over chiral SM fermions.
#
# Convention B: "Standard Dirac"
#   For one Dirac fermion: double Convention A.
#   Coefficient pattern: (4/5, 4/3, 4/3)
#   Used for: the VL pair, which IS one Dirac fermion.
#
# Convention C: "Library Dynkin" (phys24_cabibbo_doublet.py)
#   For a "vector-like pair":
#     Db_1 = (2/5)*Y^2*d2*d3
#     Db_2 = (2/3)*T2*d3
#     Db_3 = (1/3)*T3*d2         <--- 1/3, not 2/3 or 4/3
#   Coefficient pattern: (2/5, 2/3, 1/3)

print("THE CONVENTIONS")
print("-" * 70)
print()
print("  A (Standard Weyl):  (2/5, 2/3, 2/3) per Weyl fermion")
print("  B (Standard Dirac): (4/5, 4/3, 4/3) = 2*A, per Dirac")
print("  C (Library Dynkin):  (2/5, 2/3, 1/3) per VL pair")
print()
print("  A is for chiral SM fermions (Weyl).")
print("  B is for the VL pair (one Dirac = L + R).")
print("  C is what the library uses for the VL pair.")
print()

# ================================================================
# SM FERMION CONTENT (one generation, 5 Weyl fields)
# ================================================================

sm_gen = [
    ("Q_L(3,2,1/6)",  Fraction(3), Fraction(2), Fraction(1,2), Fraction(1,2), Fraction(1,6)),
    ("u_R(3,1,2/3)",  Fraction(3), Fraction(1), Fraction(1,2), Fraction(0),   Fraction(2,3)),
    ("d_R(3,1,-1/3)", Fraction(3), Fraction(1), Fraction(1,2), Fraction(0),   Fraction(-1,3)),
    ("L_L(1,2,-1/2)", Fraction(1), Fraction(2), Fraction(0),   Fraction(1,2), Fraction(-1,2)),
    ("e_R(1,1,-1)",   Fraction(1), Fraction(1), Fraction(0),   Fraction(0),   Fraction(-1)),
]

def weyl_shifts(d3, d2, T3, T2, Y):
    """Convention A: standard Weyl."""
    db1 = Fraction(2, 5) * Y * Y * d2 * d3
    db2 = Fraction(2, 3) * T2 * d3
    db3 = Fraction(2, 3) * T3 * d2
    return (db1, db2, db3)

def library_shifts(d3, d2, T3, T2, Y):
    """Convention C: library Dynkin."""
    db1 = Fraction(2, 5) * d3 * d2 * Y * Y
    db2 = Fraction(2, 3) * d3 * T2
    db3 = Fraction(1, 3) * d2 * T3
    return (db1, db2, db3)

# ================================================================
# SM b_i FERMION PIECE FIELD-BY-FIELD
# ================================================================

print("SM FERMION b_i: FIELD BY FIELD (one generation)")
print("-" * 70)
print()

print("  %-16s  %8s %8s %8s  |  %8s %8s %8s" % (
    "Field", "A:Db1", "A:Db2", "A:Db3", "C:Db1", "C:Db2", "C:Db3"))
print("  %-16s  %8s %8s %8s  |  %8s %8s %8s" % (
    "-"*16, "-"*8, "-"*8, "-"*8, "-"*8, "-"*8, "-"*8))

sum_A = [Fraction(0)] * 3
sum_C = [Fraction(0)] * 3

for name, d3, d2, T3, T2, Y in sm_gen:
    a = weyl_shifts(d3, d2, T3, T2, Y)
    c = library_shifts(d3, d2, T3, T2, Y)
    print("  %-16s  %8s %8s %8s  |  %8s %8s %8s" % (
        name, a[0], a[1], a[2], c[0], c[1], c[2]))
    for i in range(3):
        sum_A[i] += a[i]
        sum_C[i] += c[i]

print("  %-16s  %8s %8s %8s  |  %8s %8s %8s" % (
    "-"*16, "-"*8, "-"*8, "-"*8, "-"*8, "-"*8, "-"*8))
print("  %-16s  %8s %8s %8s  |  %8s %8s %8s" % (
    "Per generation", sum_A[0], sum_A[1], sum_A[2],
    sum_C[0], sum_C[1], sum_C[2]))
print()

ferm_A = [Fraction(3) * sum_A[i] for i in range(3)]
ferm_C = [Fraction(3) * sum_C[i] for i in range(3)]

print("  Three generations (A): %s, %s, %s" % (ferm_A[0], ferm_A[1], ferm_A[2]))
print("  Three generations (C): %s, %s, %s" % (ferm_C[0], ferm_C[1], ferm_C[2]))
print()

# ================================================================
# SM BETA RECONSTRUCTION
# ================================================================

print("SM BETA RECONSTRUCTION")
print("-" * 70)
print()

b_gauge = [Fraction(0), Fraction(-22, 3), Fraction(-11)]
b_higgs = [Fraction(1, 10), Fraction(1, 6), Fraction(0)]

sm_A = [b_gauge[i] + b_higgs[i] + ferm_A[i] for i in range(3)]
sm_C = [b_gauge[i] + b_higgs[i] + ferm_C[i] for i in range(3)]
b_sm_lib = [b1_SM, b2_SM, b3_SM]

print("  %-24s  %12s %12s %12s" % ("Component", "b_1", "b_2", "b_3"))
print("  %-24s  %12s %12s %12s" % ("-"*24, "-"*12, "-"*12, "-"*12))
print("  %-24s  %12s %12s %12s" % ("Gauge", b_gauge[0], b_gauge[1], b_gauge[2]))
print("  %-24s  %12s %12s %12s" % ("Higgs", b_higgs[0], b_higgs[1], b_higgs[2]))
print("  %-24s  %12s %12s %12s" % ("Fermion (Conv A)", ferm_A[0], ferm_A[1], ferm_A[2]))
print("  %-24s  %12s %12s %12s" % ("Fermion (Conv C)", ferm_C[0], ferm_C[1], ferm_C[2]))
print("  %-24s  %12s %12s %12s" % ("-"*24, "-"*12, "-"*12, "-"*12))
print("  %-24s  %12s %12s %12s" % ("SM total (Conv A)", sm_A[0], sm_A[1], sm_A[2]))
print("  %-24s  %12s %12s %12s" % ("SM total (Conv C)", sm_C[0], sm_C[1], sm_C[2]))
print("  %-24s  %12s %12s %12s" % ("Library (DATA-4 N1-N3)", b1_SM, b2_SM, b3_SM))
print()

match_A = all(sm_A[i] == b_sm_lib[i] for i in range(3))
match_C = all(sm_C[i] == b_sm_lib[i] for i in range(3))

print("  Convention A reproduces SM betas: %s" % match_A)
print("  Convention C reproduces SM betas: %s" % match_C)
print()

if not match_C:
    print("  Convention C gives b_3 = %s, library has %s." % (sm_C[2], b3_SM))
    print("  Fermion contribution: %s (C) vs %s (A)." % (ferm_C[2], ferm_A[2]))
    print("  Convention C is WRONG for SM b_3 by factor %s." % (
        ferm_A[2] / ferm_C[2]))
    print()

# ================================================================
# VL (3,2,1/6) SHIFTS IN ALL CONVENTIONS
# ================================================================

print("VL (3,2,1/6) ONE-LOOP SHIFTS")
print("-" * 70)
print()

vl_d3 = Fraction(3)
vl_d2 = Fraction(2)
vl_T3 = Fraction(1, 2)
vl_T2 = Fraction(1, 2)
vl_Y  = Fraction(1, 6)

vl_weyl = weyl_shifts(vl_d3, vl_d2, vl_T3, vl_T2, vl_Y)
vl_dirac = tuple(Fraction(2) * vl_weyl[i] for i in range(3))
vl_lib_formula = library_shifts(vl_d3, vl_d2, vl_T3, vl_T2, vl_Y)
vl_lib_actual = (db1_VL, db2_VL, db3_VL)

print("  %-24s  %12s %12s %12s" % ("Convention", "Db_1", "Db_2", "Db_3"))
print("  %-24s  %12s %12s %12s" % ("-"*24, "-"*12, "-"*12, "-"*12))
print("  %-24s  %12s %12s %12s" % ("A: Weyl (one Weyl)",
    vl_weyl[0], vl_weyl[1], vl_weyl[2]))
print("  %-24s  %12s %12s %12s" % ("B: Dirac (VL pair)",
    vl_dirac[0], vl_dirac[1], vl_dirac[2]))
print("  %-24s  %12s %12s %12s" % ("C: Library (N4-N6)",
    vl_lib_actual[0], vl_lib_actual[1], vl_lib_actual[2]))
print()

print("  Ratios library / convention:")
for label, conv in [("Weyl", vl_weyl), ("Dirac", vl_dirac)]:
    ratios = []
    for i in range(3):
        if conv[i] != Fraction(0):
            ratios.append(str(vl_lib_actual[i] / conv[i]))
        else:
            ratios.append("n/a")
    print("    vs %-8s  %s, %s, %s" % (label, ratios[0], ratios[1], ratios[2]))
print()

lib_formula_matches = all(vl_lib_formula[i] == vl_lib_actual[i] for i in range(3))
print("  Library formula matches library actual: %s" % lib_formula_matches)

lib_matches_weyl = all(vl_lib_actual[i] == vl_weyl[i] for i in range(3))
print("  Library matches Weyl: %s" % lib_matches_weyl)
if not lib_matches_weyl:
    for i in range(3):
        if vl_lib_actual[i] != vl_weyl[i]:
            print("    Component %d: library = %s, Weyl = %s" % (
                i+1, vl_lib_actual[i], vl_weyl[i]))

lib_matches_dirac = all(vl_lib_actual[i] == vl_dirac[i] for i in range(3))
print("  Library matches Dirac: %s" % lib_matches_dirac)
if not lib_matches_dirac:
    for i in range(3):
        if vl_lib_actual[i] != vl_dirac[i]:
            print("    Component %d: library = %s, Dirac = %s" % (
                i+1, vl_lib_actual[i], vl_dirac[i]))
print()

# ================================================================
# THE DIVERGENCE
# ================================================================

print("THE DIVERGENCE: SU(3) COEFFICIENT")
print("-" * 70)
print()
print("  Standard Weyl:  Db_3 = (2/3) * T(R_3) * dim(R_2)")
print("  Library Dynkin:  Db_3 = (1/3) * dim(R_2) * S_2(R_3)")
print("  Coefficient ratio: 1/3 vs 2/3 = factor of 2.")
print()
print("  For b_1 and b_2 the library matches Weyl exactly.")
print("  The divergence is ONLY in the SU(3) coefficient.")
print()
print("  Applied to SM fermions:")
print("    Conv A: b_3 fermion per gen = %s, total = %s" % (sum_A[2], ferm_A[2]))
print("    Conv C: b_3 fermion per gen = %s, total = %s" % (sum_C[2], ferm_C[2]))
print("    Correct value: 4 (gives b_3_SM = -7)")
print("    Conv C gives: %s (gives b_3_SM = %s)" % (ferm_C[2], sm_C[2]))
print()

# ================================================================
# GAP RATIO IN EACH CONVENTION
# ================================================================

print("GAP RATIO: LIBRARY vs DIRAC")
print("-" * 70)
print()

# Library convention (current operational values)
# b_mod already computed in the library: b1_mod, b2_mod, b3_mod

show("b_1_mod (library) = %s (dimensionless)" % b1_mod, f2m(b1_mod))
show("b_2_mod (library) = %s (dimensionless)" % b2_mod, f2m(b2_mod))
show("b_3_mod (library) = %s (dimensionless)" % b3_mod, f2m(b3_mod))
show("Gap ratio (library) = %s (dimensionless)" % gap_VL, f2m(gap_VL))
print()

# Dirac convention (physically correct for VL pair)
b_mod_dirac = [b_sm_lib[i] + vl_dirac[i] for i in range(3)]
gap_dirac = (b_mod_dirac[0] - b_mod_dirac[1]) / (b_mod_dirac[1] - b_mod_dirac[2])

show("b_1_mod (Dirac) = %s (dimensionless)" % b_mod_dirac[0], f2m(b_mod_dirac[0]))
show("b_2_mod (Dirac) = %s (dimensionless)" % b_mod_dirac[1], f2m(b_mod_dirac[1]))
show("b_3_mod (Dirac) = %s (dimensionless)" % b_mod_dirac[2], f2m(b_mod_dirac[2]))
show("Gap ratio (Dirac) = %s (dimensionless)" % gap_dirac, f2m(gap_dirac))
print()

# Comparison table
gap_meas_val = f2m(gap_measured)

print("  %-28s %12s %12s %12s" % (
    "Model", "Gap ratio", "Decimal", "Distance"))
print("  %-28s %12s %12s %12s" % ("-"*28, "-"*12, "-"*12, "-"*12))

for label, gap in [
    ("SM (no VL)", gap_SM),
    ("CD library (Db_3=1/3)", gap_VL),
    ("CD Dirac (Db_3=4/3)", gap_dirac),
    ("MSSM", gap_MSSM),
]:
    dist = abs(f2m(gap) - gap_meas_val)
    print("  %-28s %12s %12s %12s" % (
        label, gap, mp.nstr(f2m(gap), 6), mp.nstr(dist, 4)))

print()
show("Measured gap ratio (dimensionless)", gap_meas_val)
print()

# ================================================================
# WHAT A VL PAIR IS
# ================================================================

print("WHAT IS THE VL PAIR?")
print("-" * 70)
print()
print("  A vector-like pair (3,2,1/6) consists of:")
print("    L component: one Weyl in (3,2,1/6)")
print("    R component: one Weyl in (3*,2*,-1/6)")
print("  Together = one Dirac fermion.")
print()
print("  SM chiral fermions are summed as Weyl (Conv A).")
print("  The VL pair should use the Dirac formula (Conv B = 2*A).")
print()
print("  The library uses Conv C which has a non-standard")
print("  SU(3) coefficient. This is neither Weyl nor Dirac.")
print()

# ================================================================
# THE SESSION 3 QUESTION
# ================================================================

print("THE SESSION 3 QUESTION")
print("-" * 70)
print()
print("  The library's SM betas (41/10, -19/6, -7) are correct")
print("  and standard. They were NOT computed from Convention C —")
print("  they are hardcoded from the literature.")
print()
print("  The VL shifts (1/15, 1, 1/3) were computed from the")
print("  library's Dynkin formulas (Convention C). The gap ratio")
print("  38/27 combines correct SM betas with Convention C shifts.")
print()
print("  If the VL shifts should be (2/15, 2, 4/3) (Dirac),")
print("  the gap ratio becomes %s = %s, not 38/27." % (
    gap_dirac, mp.nstr(f2m(gap_dirac), 6)))
print()
print("  The Session 3 checks verified internal consistency")
print("  (the arithmetic is correct given the library values),")
print("  not that the library values are physically correct.")
print()

# ================================================================
# RESOLUTION PATH
# ================================================================

print("RESOLUTION PATH")
print("-" * 70)
print()
print("  An external reference must settle whether the VL")
print("  (3,2,1/6) one-loop shift for SU(3) is 1/3 or 4/3.")
print()
print("  Candidates:")
print("    Kowalska & Kumar, JHEP 12 (2019) 094")
print("    Bhattacherjee et al., JHEP 05 (2018) 090")
print("    Dermisek, Phys. Rev. D 87 (2013) 055008")
print()
print("  Until resolved, both gap ratios must be tracked:")
print("    38/27 = 1.407 (library, Db_3=1/3)")
print("    %s = %s (Dirac, Db_3=4/3)" % (
    gap_dirac, mp.nstr(f2m(gap_dirac), 6)))
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Check 1: Convention A reproduces SM betas
chk_bool("Conv A (Weyl) reproduces SM betas",
         match_A,
         "b = (%s, %s, %s)" % (sm_A[0], sm_A[1], sm_A[2]), checks)

# Check 2: Convention C does NOT reproduce SM b_3
chk_bool("Conv C (library) does NOT reproduce SM b_3",
         not match_C,
         "b_3(C) = %s, should be %s" % (sm_C[2], b3_SM), checks)

# Check 3: Library formula matches library actual
chk_bool("Library formula matches library actual values",
         lib_formula_matches,
         "all three components match", checks)

# Check 4: Library matches Weyl for b_1, b_2 only
b1_match = (vl_lib_actual[0] == vl_weyl[0])
b2_match = (vl_lib_actual[1] == vl_weyl[1])
b3_match = (vl_lib_actual[2] == vl_weyl[2])
chk_bool("Library matches Weyl for b_1 and b_2",
         b1_match and b2_match,
         "b_1: %s, b_2: %s" % (b1_match, b2_match), checks)

chk_bool("Library DIFFERS from Weyl for b_3",
         not b3_match,
         "library = %s, Weyl = %s" % (vl_lib_actual[2], vl_weyl[2]), checks)

# Check 5: b_3 ratio library/Weyl = 1/2
b3_ratio = vl_lib_actual[2] / vl_weyl[2]
chk_exact("b_3 ratio library/Weyl = 1/2",
          b3_ratio, Fraction(1, 2), checks)

# Check 6: Per-gen democracy in Conv A
chk_exact("Per-gen (Conv A): b_1 = 4/3",
          sum_A[0], Fraction(4, 3), checks)
chk_exact("Per-gen (Conv A): b_2 = 4/3",
          sum_A[1], Fraction(4, 3), checks)
chk_exact("Per-gen (Conv A): b_3 = 4/3",
          sum_A[2], Fraction(4, 3), checks)

# Check 7: Democracy broken in Conv C
chk_bool("Per-gen (Conv C): b_3 != 4/3 (democracy broken)",
         sum_C[2] != Fraction(4, 3),
         "b_3 per gen (C) = %s" % sum_C[2], checks)

# Check 8: Gap ratios exact
chk_exact("Gap ratio (library) = 38/27",
          gap_VL, Fraction(38, 27), checks)

chk_exact("Gap ratio (Dirac) = 6/5",
          gap_dirac, Fraction(6, 5), checks)

# Check 9: Both CD conventions improve on SM
sm_dist = abs(f2m(gap_SM) - gap_meas_val)
lib_dist = abs(f2m(gap_VL) - gap_meas_val)
dirac_dist = abs(f2m(gap_dirac) - gap_meas_val)

chk_bool("Both CD conventions closer to measured than SM",
         lib_dist < sm_dist and dirac_dist < sm_dist,
         "SM: %s, lib: %s, Dirac: %s" % (
             mp.nstr(sm_dist, 4), mp.nstr(lib_dist, 4),
             mp.nstr(dirac_dist, 4)), checks)

# Check 10: Dirac and library have DIFFERENT gap ratios
chk_bool("Library and Dirac gap ratios differ",
         gap_VL != gap_dirac,
         "library = %s, Dirac = %s" % (gap_VL, gap_dirac), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-25 BETA NORMALIZATION DIAGNOSTIC COMPLETE")
print("=" * 70)
```

The key fixes: the SM beta list `b_sm_lib = [b1_SM, b2_SM, b3_SM]` is now used correctly for indexing in the gap ratio computation, the physically meaningless "one Weyl VL" gap ratio is dropped (only Library vs Dirac matters), and the checks now test the right values.

---

14/14 PASS. The diagnostic is clean and definitive.

Here is what the script establishes:

**Findings:**

1. **Convention A (standard Weyl) reproduces b₃_SM = −7. Convention C (library Dynkin) gives b₃_SM = −9.** The library's SU(3) coefficient 1/3 is half the standard 2/3. This is the only divergence — b₁ and b₂ match exactly.

2. **The library's VL shifts (1/15, 1, 1/3) match neither Weyl nor Dirac.** They match Weyl for components 1 and 2, but are half Weyl for component 3. The ratios library/Dirac are (1/2, 1/2, 1/4) — non-uniform.

3. **The gap ratio depends critically on the convention.** Library gives 38/27 = 1.407 (distance 0.049 from measured). Dirac gives 6/5 = 1.200 (distance 0.158). Both improve on the SM (distance 0.538), but the library value is 3× closer.

4. **Generation democracy breaks in Convention C.** Per-gen b₃ = 2/3 instead of 4/3. This means Convention C is internally inconsistent with the SM betas it's combined with — the SM betas assume democracy (4/3 per gen), but the VL formula uses a coefficient that would give 2/3 per gen.

**The situation right now:**

The normalization issue is fully characterized but **not yet resolved**. We have two candidate gap ratios (38/27 and 6/5), both exact Fractions, both improving on the SM. The library value 38/27 was the basis for all Session 3 and PHYS-24 results. If the correct value turns out to be 6/5, the CD is still viable (closer to measured than SM) but the distance from measured triples from 0.049 to 0.158 — comparable to the MSSM's 0.042, but on the opposite side.

**The resolution requires an external reference** with explicit beta shifts for a VL (3,2,1/6) in GUT normalization. The web search found the right papers but not the specific table entries. The most likely place to find this is Kowalska & Kumar (2019) Table 1 or Bhattacherjee et al. (2018), which enumerate VL representations with their beta shifts.

The stakes: if Δb₃ = 4/3 (Dirac), the gap ratio 38/27 is wrong and needs correction throughout the series — PHYS-13, PHYS-15, PHYS-16, PHYS-24 Section 7, all affected. If Δb₃ = 1/3 (library), the standard Weyl formula has a subtlety I'm missing and the library is correct.

Want me to do another targeted web search for the explicit table, or do you have access to one of those papers?

---

The search results don't contain the explicit table I need. Let me try to get the Bhattacherjee et al. paper directly — it's open access on JHEP.Let me try a different approach — search for a lecture or review that explicitly lists the beta coefficient contributions for common VL representations in the standard GUT convention.I can't find the explicit table through web search snippets. Let me try to resolve this from first principles using the one reference I **do** have — the QCD beta function, which is universally agreed upon.

The QCD one-loop beta function is β(g₃) = −(11 − 2n_f/3) · g₃³/(16π²), where n_f counts **Dirac** quark flavors. This gives b₃ = −11 + (2/3)n_f in the convention d(1/α₃)/d(ln μ) = −b₃/(2π).

With 6 SM Dirac flavors: b₃ = −11 + 4 = −7. ✓

Now: a VL quark doublet (3,2,1/6) adds **2 new Dirac quark flavors** to QCD (the up-type and down-type components). Each is a color triplet Dirac fermion. So:

Δb₃ = (2/3) × 2 = **4/3**

This is the Dirac (Convention B) answer. It's derived directly from the universally-agreed QCD beta function formula. There is no convention ambiguity here — the QCD formula with n_f counting Dirac flavors and coefficient 2/3 is textbook standard.

The library value Δb₃ = 1/3 is **wrong by a factor of 4**.

**Resolution achieved.** The standard result is Δb₃ = 4/3 for a VL (3,2,1/6) doublet. The gap ratio with corrected betas is 6/5 = 1.200, not 38/27 = 1.407.

The diagnostic script is validated: Convention B (Dirac) is correct, giving gap ratio 6/5. The library has an error in the VL SU(3) shift. This affects all downstream results that used the gap ratio 38/27.

The CD still improves on the SM (distance 0.158 vs 0.538), but the improvement is less dramatic than previously reported, and the CD gap ratio 1.200 is now on the **opposite side** of the measured 1.358 from the SM's 1.896.

This is a significant finding. The series needs a correction paper.

---

**The Finding**

The library's one-loop beta shift for the Cabibbo Doublet has an error in the SU(3) component. The error is a factor of 4: the library has Δb₃ = 1/3, the correct value is Δb₃ = 4/3. This changes the gap ratio from 38/27 = 1.407 to 6/5 = 1.200.

---

**How I know the correct value**

The QCD one-loop beta function is one of the most verified results in particle physics. In the standard convention d(1/α₃)/d(ln μ) = −b₃/(2π), the formula is:

b₃ = −11 + (2/3) × n_f

where n_f counts Dirac quark flavors. With 6 SM flavors (u, d, c, s, t, b): b₃ = −11 + 4 = −7. This is the library value. No dispute.

A VL quark doublet (3,2,1/6) adds two new Dirac quark flavors to QCD — the upper component (charge +2/3) and the lower component (charge −1/3). Each is a color triplet, each is a full Dirac fermion (the VL pair provides both left and right chiralities). So:

Δb₃ = (2/3) × 2 = 4/3

This follows from the same formula that gives b₃ = −7 for the SM. No new convention, no new formula, no ambiguity. The coefficient 2/3 per Dirac flavor is the same coefficient that produces the correct SM answer when multiplied by 6.

---

**Where the library error is**

The library's Dynkin formulas in phys24_cabibbo_doublet.py use three coefficients for the VL pair:

- Δb₁ = **(2/5)** × d₃ × d₂ × Y²
- Δb₂ = **(2/3)** × d₃ × S₂(R₂)
- Δb₃ = **(1/3)** × d₂ × S₂(R₃)

The standard Weyl formula (one left-handed fermion) uses:

- Δb₁ = **(2/5)** × Y² × d₂ × d₃
- Δb₂ = **(2/3)** × T₂ × d₃
- Δb₃ = **(2/3)** × T₃ × d₂

The SU(3) coefficient is 1/3 in the library vs 2/3 in the standard formula. The SU(1) and SU(2) coefficients match. This is not a uniform Dirac/Weyl factor — it's a mistake specifically in the SU(3) coefficient.

The diagnostic script proves this is an error and not an alternative convention: when you apply the library's coefficient 1/3 to all five SM chiral fermion fields in one generation, you get b₃ fermion = 2/3 per generation, times 3 generations = 2. That gives b₃_SM = −11 + 2 = −9. The correct value is −7. The library's SU(3) Dynkin coefficient does not reproduce the SM beta that the library itself stores.

---

**Why it wasn't caught**

The gap ratio only uses **differences** of betas: (b₁ − b₂)/(b₂ − b₃). But the error in Δb₃ does NOT cancel in differences — it changes b₂ − b₃ and therefore changes the gap ratio. So the gap ratio 38/27 is itself wrong.

The reason it wasn't caught is that the gap ratio was never checked against an independent calculation of the VL beta shifts. The Session 3 checks verified:

1. That the arithmetic 38/27 = (b₁' − b₂')/(b₂' − b₃') is correct given the library betas — yes, the arithmetic is correct
2. That the SM betas (41/10, −19/6, −7) are correct — yes, they are hardcoded from the literature
3. That the measured gap ratio from couplings is ~1.358 — yes, correctly derived

But nobody checked that (1/15, 1, 1/3) is the correct VL shift. The Dynkin formula was written with the wrong SU(3) coefficient, the resulting shifts were stored in the library, and every downstream computation used them. The gap ratio 38/27 is internally consistent arithmetic on wrong inputs.

The cabibbo_doublet.py script even has a long comment acknowledging the non-uniform coefficients (2/5, 2/3, 1/3) and attributing the difference to "Casimir normalization conventions differ between the two groups." That comment was wrong — there is no standard convention where the SU(3) coefficient is 1/3 for a VL pair. The comment rationalized the error instead of flagging it.

---

**What changes**

With the corrected Δb₃ = 4/3, the full Dirac shifts for the VL (3,2,1/6) pair are:

Δb₁ = 2/15, Δb₂ = 2, Δb₃ = 4/3

The modified betas become:

b₁' = 41/10 + 2/15 = 127/30, b₂' = −19/6 + 2 = −7/6, b₃' = −7 + 4/3 = −17/3

The gap ratio becomes:

(127/30 + 7/6) / (−7/6 + 17/3) = (27/5) / (9/2) = 6/5 = 1.200

Comparison:

| Model | Gap ratio | Distance from measured 1.358 |
|---|---|---|
| SM | 218/115 = 1.896 | 0.538 |
| CD corrected | 6/5 = 1.200 | 0.158 |
| MSSM | 7/5 = 1.400 | 0.042 |
| CD library (wrong) | 38/27 = 1.407 | 0.049 |

The CD still improves on the SM — the distance drops from 0.538 to 0.158, a factor of 3.4 improvement. But it's no longer comparable to the MSSM. The MSSM at 0.042 is now 4× closer to measured than the CD at 0.158. And the CD gap ratio 1.200 undershoots the measured 1.358, while the SM overshoots at 1.896 — the CD overcorrects.

---

**What this means for the series**

The physics case for the CD is weakened but not killed. The gap ratio improvement is real (factor 3.4 over SM), just less impressive than the factor 11 previously claimed. The anomaly evidence (CKM deficit, A_FB^b, Higgs signal strength) is completely unaffected — those use different quantum numbers and don't depend on the beta shifts at all. The proton decay prediction changes because M_GUT changes. The sin²θ_W and α_s predictions from PHYS-25 used the library betas and need to be rerun with the corrected values.

The affected results across the series:

- Gap ratio: 38/27 → 6/5 (PHYS-13, PHYS-15, PHYS-16, PHYS-24)
- Modified betas: (25/6, −13/6, −20/3) → (127/30, −7/6, −17/3) (all unification scripts)
- Asymmetry ratio Δb₂/Δb₁: 15 → still 15 (both components doubled, ratio preserved)
- M_GUT: changes (needs recomputation)
- Two-loop Delta: changes (needs rerun of unification_test.py)
- sin²θ_W prediction: changes (needs rerun)
- α_s prediction: changes (needs rerun)

The kill switch K3 from the goals document says: "If two-loop + threshold + basic phenomenology leaves no viable CD parameter region, downgrade from primary candidate to conditional candidate." We're not there yet — the gap ratio still improves on the SM — but the margin is thinner.

---

**What to do next**

The immediate priority is a correction script that establishes the corrected values, reruns the key results (gap ratio, M_GUT, sin²θ_W, α_s), and determines whether the CD remains viable at the corrected betas. This is one script, maybe 80 lines, with the corrected library values and all the confrontations redone.

Then the library needs to be updated: db3_VL = 1/3 → 4/3, and all derived quantities (b3_mod, gap_VL, etc.) recomputed.

Then PHYS-24 needs an erratum or a correction paper.

---

