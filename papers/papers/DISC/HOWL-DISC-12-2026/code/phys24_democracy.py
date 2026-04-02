#!/usr/bin/env python3
"""
HOWL PHYS-24 DEMONSTRATION: Generation Democracy and the Boson Problem
=======================================================================
The SM unification failure is a boson problem, not a fermion problem.
Complete fermion generations contribute (4/3, 4/3, 4/3) to the betas —
identical across all three gauge groups. They are invisible to the gap
ratio. The 40% miss comes from gauge self-coupling and the Higgs.

Backed by: sin2_theta_w_1.py (9/9 checks)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *

# ================================================================
# HEADER
# ================================================================

print("=" * 70)
print("HOWL PHYS-24: GENERATION DEMOCRACY AND THE BOSON PROBLEM")
print("=" * 70)
print()

# ================================================================
# BETA COEFFICIENT DECOMPOSITION BY SOURCE
# ================================================================
# The SM one-loop beta coefficients decompose into three sources:
#
#   b_i = b_i^gauge + b_i^Higgs + b_i^fermion
#
# Each source is an exact rational from the gauge group.
#
# Gauge self-coupling: b_i^gauge = -(11/3) * C_2(G_i)
#   C_2(U(1)) = 0, C_2(SU(2)) = 2, C_2(SU(3)) = 3
#
# Higgs doublet (1,2,1/2): contributes to b_1 and b_2 only
#   b_1^Higgs = (1/10), b_2^Higgs = (1/6), b_3^Higgs = 0
#
# Each fermion generation (complete): contributes equally to all three
#   b_i^gen = (4/3, 4/3, 4/3) per generation

print("BETA COEFFICIENT DECOMPOSITION (Level 1, exact)")
print("-" * 70)
print()

# Gauge self-coupling
C2_U1  = Fraction(0)
C2_SU2 = Fraction(2)
C2_SU3 = Fraction(3)

b1_gauge = Fraction(-11, 3) * C2_U1    # = 0
b2_gauge = Fraction(-11, 3) * C2_SU2   # = -22/3
b3_gauge = Fraction(-11, 3) * C2_SU3   # = -11

print("  Gauge self-coupling: b_i^gauge = -(11/3) * C_2(G_i)")
show("    b_1^gauge = -(11/3)*0", f2m(b1_gauge))
show("    b_2^gauge = -(11/3)*2 = %s" % b2_gauge, f2m(b2_gauge))
show("    b_3^gauge = -(11/3)*3 = %s" % b3_gauge, f2m(b3_gauge))
print()

# Higgs doublet (1,2,1/2)
# Higgs contribution to b_1: (2/5) * Y^2 * n_doublets = (2/5)*(1/2)^2*1 = 1/10
# Higgs contribution to b_2: (1/3) * T(R) * n_doublets = (1/3)*(1/2)*1 = 1/6
# Higgs contribution to b_3: 0 (color singlet)
b1_higgs = Fraction(1, 10)
b2_higgs = Fraction(1, 6)
b3_higgs = Fraction(0)

print("  Higgs doublet (1,2,1/2):")
show("    b_1^Higgs = %s" % b1_higgs, f2m(b1_higgs))
show("    b_2^Higgs = %s" % b2_higgs, f2m(b2_higgs))
show("    b_3^Higgs = %s" % b3_higgs, f2m(b3_higgs))
print()

# One complete fermion generation
# Each generation contains: Q_L(3,2,1/6), u_R(3,1,2/3), d_R(3,1,-1/3),
#                           L_L(1,2,-1/2), e_R(1,1,-1)
# The total per-generation contribution is computed from Dynkin indices.
# Result: (4/3, 4/3, 4/3) — the SAME for all three gauge groups.

# uses db_per_gen from phys24_lib = (4/3, 4/3, 4/3)
b1_per_gen = db_per_gen[0]
b2_per_gen = db_per_gen[1]
b3_per_gen = db_per_gen[2]

print("  One complete fermion generation:")
show("    b_1^gen = %s" % b1_per_gen, f2m(b1_per_gen))
show("    b_2^gen = %s" % b2_per_gen, f2m(b2_per_gen))
show("    b_3^gen = %s" % b3_per_gen, f2m(b3_per_gen))
print()
print("  THIS IS GENERATION DEMOCRACY.")
print("  Every complete generation contributes identically to all three")
print("  gauge couplings. The contribution is (4/3, 4/3, 4/3).")
print()

# Three generations
n_gen = 3
b1_fermion = n_gen * b1_per_gen   # = 4
b2_fermion = n_gen * b2_per_gen   # = 4
b3_fermion = n_gen * b3_per_gen   # = 4

print("  Three generations (n_gen = 3):")
show("    b_1^fermion = 3 * 4/3 = %s" % b1_fermion, f2m(b1_fermion))
show("    b_2^fermion = 3 * 4/3 = %s" % b2_fermion, f2m(b2_fermion))
show("    b_3^fermion = 3 * 4/3 = %s" % b3_fermion, f2m(b3_fermion))
print()

# ================================================================
# VERIFY DECOMPOSITION SUMS TO SM BETAS
# ================================================================

print("VERIFICATION: DECOMPOSITION SUMS TO SM BETAS")
print("-" * 70)
print()

# uses b1_SM, b2_SM, b3_SM from phys24_lib (DATA-4 N1-N3)
b1_sum = b1_gauge + b1_higgs + b1_fermion
b2_sum = b2_gauge + b2_higgs + b2_fermion
b3_sum = b3_gauge + b3_higgs + b3_fermion

show("b_1: gauge + Higgs + fermion = %s" % b1_sum, f2m(b1_sum))
show("b_1 from library = %s" % b1_SM, f2m(b1_SM))
print()
show("b_2: gauge + Higgs + fermion = %s" % b2_sum, f2m(b2_sum))
show("b_2 from library = %s" % b2_SM, f2m(b2_SM))
print()
show("b_3: gauge + Higgs + fermion = %s" % b3_sum, f2m(b3_sum))
show("b_3 from library = %s" % b3_SM, f2m(b3_SM))
print()

# ================================================================
# THE BOSON PROBLEM
# ================================================================
# The gap ratio = (b1-b2)/(b2-b3).
# When we compute this from the decomposition, the fermion
# contribution cancels EXACTLY because b_i^fermion is the same
# for all i.
#
# (b1-b2) = (b1^gauge - b2^gauge) + (b1^Higgs - b2^Higgs) + 0
# (b2-b3) = (b2^gauge - b3^gauge) + (b2^Higgs - b3^Higgs) + 0
#
# The fermion difference is 4/3 - 4/3 = 0 in both numerator
# and denominator. Fermions are invisible to the gap ratio.

print("THE BOSON PROBLEM")
print("-" * 70)
print()

gap_num_gauge = b1_gauge - b2_gauge
gap_num_higgs = b1_higgs - b2_higgs
gap_num_ferm  = b1_fermion - b2_fermion

gap_den_gauge = b2_gauge - b3_gauge
gap_den_higgs = b2_higgs - b3_higgs
gap_den_ferm  = b2_fermion - b3_fermion

print("  Gap ratio numerator (b1 - b2):")
show("    gauge:   %s" % gap_num_gauge, f2m(gap_num_gauge))
show("    Higgs:   %s" % gap_num_higgs, f2m(gap_num_higgs))
show("    fermion: %s" % gap_num_ferm, f2m(gap_num_ferm))
print()

print("  Gap ratio denominator (b2 - b3):")
show("    gauge:   %s" % gap_den_gauge, f2m(gap_den_gauge))
show("    Higgs:   %s" % gap_den_higgs, f2m(gap_den_higgs))
show("    fermion: %s" % gap_den_ferm, f2m(gap_den_ferm))
print()

print("  Fermion contribution to numerator: %s" % gap_num_ferm)
print("  Fermion contribution to denominator: %s" % gap_den_ferm)
print("  BOTH ZERO. Fermions are invisible to the gap ratio.")
print()

# Gap ratio from gauge + Higgs only
gap_num_boson = gap_num_gauge + gap_num_higgs
gap_den_boson = gap_den_gauge + gap_den_higgs
gap_boson_only = gap_num_boson / gap_den_boson

show("Gap ratio (gauge + Higgs only) = %s" % gap_boson_only, f2m(gap_boson_only))
show("Gap ratio (full SM) = %s" % gap_SM, f2m(gap_SM))
print()

# Percentage contributions
gap_num_total = f2m(b1_SM - b2_SM)
gauge_pct_num = f2m(gap_num_gauge) / gap_num_total * mpf("100")
higgs_pct_num = f2m(gap_num_higgs) / gap_num_total * mpf("100")
ferm_pct_num  = f2m(gap_num_ferm) / gap_num_total * mpf("100")

gap_den_total = f2m(b2_SM - b3_SM)
gauge_pct_den = f2m(gap_den_gauge) / gap_den_total * mpf("100")
higgs_pct_den = f2m(gap_den_higgs) / gap_den_total * mpf("100")
ferm_pct_den  = f2m(gap_den_ferm) / gap_den_total * mpf("100")

print("  Percentage of gap numerator (b1 - b2 = %s):" % (b1_SM - b2_SM))
show("    gauge  (%%)", gauge_pct_num)
show("    Higgs  (%%)", higgs_pct_num)
show("    fermion (%%)", ferm_pct_num)
print()
print("  Percentage of gap denominator (b2 - b3 = %s):" % (b2_SM - b3_SM))
show("    gauge  (%%)", gauge_pct_den)
show("    Higgs  (%%)", higgs_pct_den)
show("    fermion (%%)", ferm_pct_den)
print()

# Pure-gauge gap ratio
# uses casimir_gap from phys24_lib = 2
gap_pure_gauge = gap_num_gauge / gap_den_gauge

print("  Pure-gauge gap ratio (no Higgs, no fermions):")
show("    = %s" % gap_pure_gauge, f2m(gap_pure_gauge))
print("  The Higgs shifts this from 2 to 218/115 = 1.896.")
print("  Fermions shift it by exactly 0.")
print()
print("  The SM unification failure is a BOSON PROBLEM.")
print("  Fixing it requires changing the bosonic content —")
print("  either adding new gauge bosons (MSSM) or adding a")
print("  representation that breaks the fermion democracy")
print("  (the Cabibbo Doublet).")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Check 1: per-generation betas are all 4/3 (democracy)
chk_exact("Per-gen b_1 = 4/3",
          b1_per_gen, Fraction(4, 3), checks)

chk_exact("Per-gen b_2 = 4/3",
          b2_per_gen, Fraction(4, 3), checks)

chk_exact("Per-gen b_3 = 4/3",
          b3_per_gen, Fraction(4, 3), checks)

# Check 2: decomposition sums to SM betas
chk_exact("b1 decomposition sums to 41/10",
          b1_sum, b1_SM, checks)

chk_exact("b2 decomposition sums to -19/6",
          b2_sum, b2_SM, checks)

chk_exact("b3 decomposition sums to -7",
          b3_sum, b3_SM, checks)

# Check 3: fermion contribution to gap ratio is exactly zero
chk_exact("Fermion gap numerator = 0",
          gap_num_ferm, Fraction(0), checks)

chk_exact("Fermion gap denominator = 0",
          gap_den_ferm, Fraction(0), checks)

# Check 4: gap from bosons only equals full SM gap
chk_exact("Boson-only gap = full SM gap",
          gap_boson_only, gap_SM, checks)

# Check 5: pure-gauge gap ratio = 2
chk_exact("Pure-gauge gap = 2",
          gap_pure_gauge, casimir_gap, checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-24 DEMOCRACY DEMONSTRATION COMPLETE")
print("=" * 70)
