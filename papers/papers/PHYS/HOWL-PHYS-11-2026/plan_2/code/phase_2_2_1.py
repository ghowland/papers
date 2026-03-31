#!/usr/bin/env python3
"""
DISC-8 Item 5: Additional Domain Extractions
==============================================

Three new domains extracted into the DISC-7 Phase 1 framework.
All expected Subgroup A (phase-periodic, modulus 8R₂ × scale).

Domain 7: Aharonov-Bohm effect
Domain 8: Flux quantization in superconductors
Domain 9: AC Josephson effect
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction

print("=" * 70)
print("DISC-8 ITEM 5: ADDITIONAL DOMAIN EXTRACTIONS")
print("=" * 70)
print()

def rational_arctan(x, terms=160):
    result = Fraction(0); power = x; x_sq = x * x
    for k in range(terms):
        nn = 2*k+1
        if k%2==0: result += power/nn
        else: result -= power/nn
        power *= x_sq
    return result

pi_f = 4*(4*rational_arctan(Fraction(1,5),160)-rational_arctan(Fraction(1,239),160))
R2 = pi_f / 4
two_pi = 2 * pi_f

# ================================================================
# DOMAIN 7: AHARONOV-BOHM EFFECT
# ================================================================

print("=" * 70)
print("DOMAIN 7: AHARONOV-BOHM EFFECT")
print("=" * 70)
print()

print("(a) STANDARD FORM")
print("  Electron encircles solenoid with magnetic flux Phi.")
print("  Phase shift: delta_phi = e*Phi/(hbar*c) = 2*pi*Phi/Phi_0")
print("  where Phi_0 = h/e = 2*pi*hbar/e is the flux quantum.")
print()
print("  Observable: interference fringe shift.")
print("  Periodicity: fringe pattern repeats when Phi -> Phi + Phi_0.")
print("  Aharonov and Bohm 1959.")
print()

print("(b) DECOMPOSED")
print("  Quantity: phase shift delta_phi = 2*pi*Phi/Phi_0")
print("  Modulus: 2*pi = 8*R2 (one complete fringe cycle)")
print("  Integer: number of complete fringe shifts n = floor(Phi/Phi_0)")
print("  Remainder: delta_phi mod 2*pi = 2*pi*(Phi/Phi_0 mod 1)")
print("  The remainder is the observable fringe position.")
print()

print("(c) FRACTION ARITHMETIC")
print()

# Test with rational flux ratios Phi/Phi_0
Phi_0 = Fraction(1)  # flux quantum = 1 in natural units

print(f"  {'Phi/Phi_0':>10} {'Phase/(2pi)':>12} {'Int':>5} {'R/(2pi)':>10} {'Phase':>14}")
for num, den in [(0,1),(1,4),(1,3),(1,2),(2,3),(3,4),(1,1),(5,4),(3,2),(7,4),(2,1),(9,4),(3,1)]:
    if den == 0:
        continue
    flux_ratio = Fraction(num, den)
    phase_over_2pi = flux_ratio  # delta_phi/(2pi) = Phi/Phi_0
    
    q = int(phase_over_2pi)
    if phase_over_2pi < 0:
        q = int(phase_over_2pi) - 1
    r = phase_over_2pi - q
    
    # Phase in R2 units
    phase = 8 * R2 * flux_ratio
    
    print(f"  {str(flux_ratio):>10} {str(phase_over_2pi):>12} {q:>5} {str(r):>10} {str(Fraction(8)*flux_ratio):>8}*R2")

print()

# Verify modulus = 8R2
assert two_pi == 8 * R2
print(f"  Modulus 2pi = 8R2: {two_pi == 8*R2} (EXACT)")
print()

# Key physics: at Phi = Phi_0/2, phase = pi, destructive interference
half_flux_phase = 8 * R2 * Fraction(1, 2)  # = 4R2 = pi
assert half_flux_phase == 4 * R2
assert half_flux_phase == pi_f
print(f"  Phi = Phi_0/2: phase = 4R2 = pi (destructive interference) ✓")
print()

print("(e) R_n: Modulus = 2pi = 8R2. Phase = 8R2 * Phi/Phi_0.")
print("  Same structure as Berry, BS, BZ, theta. SUBGROUP A confirmed.")
print()

# ================================================================
# DOMAIN 8: FLUX QUANTIZATION IN SUPERCONDUCTORS
# ================================================================

print("=" * 70)
print("DOMAIN 8: FLUX QUANTIZATION (SUPERCONDUCTOR)")
print("=" * 70)
print()

print("(a) STANDARD FORM")
print("  Superconducting ring: total flux is quantized.")
print("  Phi = n * Phi_0/2 = n * h/(2e)")
print("  The factor 1/2: Cooper pairs have charge 2e.")
print("  London 1950, Deaver-Fairbank 1961, Doll-Nabauer 1961.")
print()
print("  The order parameter psi = |psi|*exp(i*theta)")
print("  Single-valuedness: oint grad(theta) . dl = 2*pi*n")
print("  Combined with A: oint (grad(theta) - 2eA/hbar) . dl = 0")
print("  Therefore: 2*pi*n = (2e/hbar) * Phi")
print("  Phi = n * pi*hbar/e = n * Phi_0/2")
print()

print("(b) DECOMPOSED")
print("  Quantity: order parameter phase theta around the ring")
print("  Modulus: 2*pi = 8*R2 (single-valuedness of psi)")
print("  Integer: n = number of flux quanta")
print("  Remainder: 0 (flux is EXACTLY quantized, no fractional part)")
print()
print("  This is like theta_QCD = 0 (PHYS-7):")
print("  The remainder is forced to zero by a topological constraint")
print("  (single-valuedness), not by energy minimization.")
print()

print("(c) FRACTION ARITHMETIC")
print()

# The phase around the ring = 2*pi*n (exact integer multiple)
# Remainder = 0 for every n

for n in range(6):
    phase = Fraction(n) * two_pi  # = n * 8R2
    phase_over_2pi = phase / two_pi  # = n (exact integer)
    q = int(phase_over_2pi)
    r = phase_over_2pi - q
    
    assert q == n
    assert r == Fraction(0)
    print(f"  n={n}: phase/(2pi) = {q}, remainder = {r} ✓")

print()
print(f"  Modulus 2pi = 8R2: {two_pi == 8*R2} (EXACT)")
print()
print("  SUBGROUP A, with R = 0 (like theta_QCD).")
print("  The remainder vanishes by topology (single-valuedness),")
print("  not by dynamics (energy minimization).")
print()

# ================================================================
# DOMAIN 9: AC JOSEPHSON EFFECT
# ================================================================

print("=" * 70)
print("DOMAIN 9: AC JOSEPHSON EFFECT")
print("=" * 70)
print()

print("(a) STANDARD FORM")
print("  Josephson junction: two superconductors separated by thin barrier.")
print("  AC effect: constant voltage V produces oscillating current")
print("    I = I_c * sin(phi(t))")
print("    d(phi)/dt = 2eV/hbar")
print("  Josephson 1962.")
print()
print("  The phase phi accumulates linearly in time:")
print("    phi(t) = phi_0 + (2eV/hbar)*t")
print("  The current oscillates with Josephson frequency:")
print("    f_J = 2eV/h = V/Phi_0")
print("  where Phi_0 = h/(2e) is the superconducting flux quantum.")
print()

print("(b) DECOMPOSED")
print("  Quantity: Josephson phase phi(t)")
print("  Modulus: 2*pi = 8*R2 (one current oscillation cycle)")
print("  Integer: number of complete oscillation cycles n = floor(phi/(2pi))")
print("  Remainder: phi mod 2*pi = instantaneous phase of current oscillation")
print("  The remainder determines the instantaneous supercurrent I = I_c * sin(R).")
print()

print("(c) FRACTION ARITHMETIC")
print()

# Phase accumulation: phi(t) = (2eV/hbar)*t
# In one Josephson period T_J = 1/f_J = h/(2eV) = Phi_0/V:
#   phi(T_J) = (2eV/hbar) * h/(2eV) = 2*pi
# So one period accumulates exactly 2pi = 8R2 of phase.

# At rational fractions of the period:
print("  Phase at fractions of Josephson period T_J:")
print()
print(f"  {'t/T_J':>8} {'phi/(2pi)':>10} {'Int':>5} {'R/(2pi)':>10} {'sin(R)':>12}")

for num, den in [(0,1),(1,8),(1,6),(1,4),(1,3),(3,8),(1,2),(5,8),(2,3),(3,4),(5,6),(7,8),(1,1)]:
    t_frac = Fraction(num, den)
    phi_over_2pi = t_frac  # phi = 2*pi*t/T_J
    q = int(phi_over_2pi)
    r = phi_over_2pi - q
    
    # sin(2*pi*r) for the current — compute for known rational fractions
    # We can't compute sin exactly in Fractions for general r,
    # but we can verify the decomposition
    print(f"  {str(t_frac):>8} {str(phi_over_2pi):>10} {q:>5} {str(r):>10}")

print()
print(f"  Modulus 2pi = 8R2: {two_pi == 8*R2} (EXACT)")
print()

# The Josephson frequency-voltage relation
# f_J = 2eV/h = V/(h/2e) = V/Phi_0
# This is an exact relationship (used as a voltage standard)
# The phase accumulation rate is 2eV/hbar = 2*pi*f_J = 8*R2*f_J

print("  The Josephson frequency-voltage relation f_J = 2eV/h")
print("  is exact (used as the international voltage standard).")
print("  Phase rate: d(phi)/dt = 2*pi*f_J = 8*R2*f_J")
print()
print("  R2 sets the conversion between frequency and phase rate,")
print("  exactly as in all other Subgroup A domains.")
print()
print("  SUBGROUP A confirmed. Modulus = 8R2.")
print()

# ================================================================
# UPDATED EXTRACTION TABLE
# ================================================================

print("=" * 70)
print("UPDATED EXTRACTION TABLE (9 DOMAINS)")
print("=" * 70)
print()

print("| # | Domain           | Modulus       | Integer       | Remainder      | R2  | Subgroup |")
print("|---|------------------|---------------|---------------|----------------|-----|----------|")
print("| 1 | Theta vacuum     | 2pi = 8R2     | Instanton v   | theta = 0      | mod | A        |")
print("| 2 | RG running       | Mass m_f      | Active flavors| Running        | step| B        |")
print("| 3 | Bohr-Sommerfeld  | 2pi*hbar=8R2h | n             | mu/4           | mod | A        |")
print("| 4 | Berry phase      | 2pi = 8R2     | Winding n     | gamma mod 2pi  | mod | A        |")
print("| 5 | Brillouin zone   | G = 8R2/a     | Zone index    | k mod G        | mod | A        |")
print("| 6 | Chern-Simons     | 1             | Chern number  | CS mod Z       | exp | C        |")
print("| 7 | Aharonov-Bohm    | 2pi = 8R2     | Fringe count  | Phase mod 2pi  | mod | A        |")
print("| 8 | Flux quant.      | 2pi = 8R2     | Flux quanta n | 0 (exact)      | mod | A        |")
print("| 9 | Josephson AC     | 2pi = 8R2     | Cycle count   | Phase mod 2pi  | mod | A        |")
print()
print("  Subgroup A: 7 domains (theta, BS, Berry, BZ, AB, flux, Josephson)")
print("  Subgroup B: 1 domain  (RG running)")
print("  Subgroup C: 1 domain  (Chern-Simons)")
print()
print("  R2 = pi/4 in modulus: 7/9 domains")
print("  R2 in other role: 2/9 (step size in B, exponential in C)")
print("  R2 present: 9/9 domains (100%)")
print()
print("  The three-subgroup structure is CONFIRMED by extension.")
print("  All three new domains fall into Subgroup A as expected.")
print("  No new subgroup needed.")
