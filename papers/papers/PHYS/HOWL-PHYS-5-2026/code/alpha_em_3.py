"""
Alpha_EM — Segmented Running + Boundary Correction

Correct approach: run segment by segment as before, but at each
threshold where a fermion deactivates, apply the -5/6 correction
for that specific fermion.

The asymptotic VP formula says: when a fermion of mass m_f has been
active over a range from mu_high down to m_f, its total contribution is:

  coeff_f * [ln(mu_high/m_f) - 5/6] / pi

instead of the step-function:

  coeff_f * ln(mu_high/m_f) / pi

The -5/6 accounts for the fact that at its own mass threshold,
the fermion wasn't fully contributing. The ramp-up costs 5/6.

So the total correction is: subtract (coeff_f * 5/6 / pi) for each
fermion that has a threshold between M_Z and m_e.

The step-function total was 138.3636 (= 127.906 + 10.458).
The correction is sum_f coeff_f * (5/6) / pi.
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 120

# ============================================================
# Transcendentals
# ============================================================

def rational_arctan(x, terms=160):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        if k % 2 == 0:
            result += power / n
        else:
            result -= power / n
        power *= x_sq
    return result

def rational_pi(terms=160):
    a1 = rational_arctan(Fraction(1, 5), terms)
    a2 = rational_arctan(Fraction(1, 239), terms)
    return 4 * (4 * a1 - a2)

def rational_arctanh(x, terms=160):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        result += power / n
        power *= x_sq
    return result

def rational_ln2(terms=160):
    return 2 * rational_arctanh(Fraction(1, 3), terms)

def rational_ln_ratio(p, q, terms=160):
    ratio = Fraction(p, q)
    ln2 = rational_ln2(terms)
    powers_of_2 = 0
    reduced = ratio
    while reduced > 2:
        reduced = reduced / 2
        powers_of_2 += 1
    while reduced < Fraction(1, 2):
        reduced = reduced * 2
        powers_of_2 -= 1
    arg = (reduced - 1) / (reduced + 1)
    ln_reduced = 2 * rational_arctanh(arg, terms)
    return powers_of_2 * ln2 + ln_reduced

print("Computing pi (160 terms)...")
pi_rat = rational_pi(160)
print(f"  Done. {pi_rat.numerator.bit_length()} bits.")

# ============================================================
# Particle coefficients — exact rationals
# ============================================================

coeff_up   = Fraction(8, 9)    # (2/3)*3*(2/3)^2
coeff_down = Fraction(2, 9)    # (2/3)*3*(1/3)^2
coeff_lep  = Fraction(2, 3)    # (2/3)*1*1^2

# Boundary shape correction
five_sixths = Fraction(5, 6)   # = (3^2 - 2^2)/(2*3)

# ============================================================
# Masses in MeV
# ============================================================

M_Z   = Fraction(911876, 10)
m_b   = Fraction(4180, 1)
m_tau = Fraction(17768, 10)
m_c   = Fraction(1270, 1)
m_mu  = Fraction(105658, 1000)
m_s   = Fraction(93, 1)
m_d   = Fraction(47, 10)
m_u   = Fraction(22, 10)
m_e   = Fraction(511, 1000)

# ============================================================
# Segments (same as before)
# ============================================================

def seg_coeff(n_up, n_down, n_lep):
    return n_up * coeff_up + n_down * coeff_down + n_lep * coeff_lep

segments = [
    ('M_Z -> m_b',    M_Z,   m_b,   2, 3, 3, 'b quark (down-type)'),
    ('m_b -> m_tau',   m_b,   m_tau, 2, 2, 3, 'tau lepton'),
    ('m_tau -> m_c',   m_tau, m_c,   2, 2, 2, 'charm quark (up-type)'),
    ('m_c -> m_mu',    m_c,   m_mu,  1, 2, 2, 'muon'),
    ('m_mu -> m_s',    m_mu,  m_s,   1, 2, 1, 'strange quark (down-type)'),
    ('m_s -> m_d',     m_s,   m_d,   1, 1, 1, 'down quark (down-type)'),
    ('m_d -> m_u',     m_d,   m_u,   1, 0, 1, 'up quark (up-type)'),
    ('m_u -> m_e',     m_u,   m_e,   0, 0, 1, 'electron'),
]

# The species that deactivates at each boundary:
# At m_b: b quark deactivates → coeff = 2/9
# At m_tau: tau deactivates → coeff = 2/3
# At m_c: c quark deactivates → coeff = 8/9
# At m_mu: muon deactivates → coeff = 2/3
# At m_s: s quark deactivates → coeff = 2/9
# At m_d: d quark deactivates → coeff = 2/9
# At m_u: u quark deactivates → coeff = 8/9
# At m_e: electron deactivates → coeff = 2/3 (but this is the endpoint)

deactivating_coeff = [
    coeff_down,  # b
    coeff_lep,   # tau
    coeff_up,    # c  -- WAIT. The segment m_tau -> m_c means c is still 
                 # active above m_c. It deactivates at m_c. So the boundary
                 # correction for c applies at the m_c threshold.
                 # But which segment does it belong to?
]

# Actually, let me think about this differently.
# 
# The step function says: above m_f, species f contributes fully.
#                         below m_f, species f contributes zero.
# 
# The exact VP says: above m_f, species f contributes [ln - 5/6],
#                    which is LESS than the step function's ln.
#
# The difference is: the step function overcounts by 5/6 * coeff_f / pi
# for each species that has a threshold crossing in our range.
#
# Species with thresholds between m_e and M_Z:
#   b, tau, c, mu, s, d, u  (7 species)
#   The electron is the endpoint — it doesn't have a threshold CROSSING,
#   it's where we stop.
#
# Total overcounting = (5/6) * sum_f coeff_f / pi
# where f runs over {b, tau, c, mu, s, d, u}

species_corrections = [
    ('b',   coeff_down),  # 2/9
    ('tau', coeff_lep),   # 2/3
    ('c',   coeff_up),    # 8/9
    ('mu',  coeff_lep),   # 2/3
    ('s',   coeff_down),  # 2/9
    ('d',   coeff_down),  # 2/9
    ('u',   coeff_up),    # 8/9
]

# ============================================================
# Run the computation
# ============================================================

print()
print("=" * 74)
print("ALPHA_EM: SEGMENTED RUNNING + BOUNDARY CORRECTION")
print("=" * 74)
print()

# PART 1: Step-function running (same as before)
alpha_inv = Fraction(127906, 1000)
total_step = Fraction(0)

print("PART 1: Step-function running")
print(f"{'Segment':<16} {'Coeff':>8} {'ln(hi/lo)':>14} {'Delta':>12} {'1/alpha':>12}")
print("-" * 65)

for name, hi, lo, nu, nd, nl, species in segments:
    c = seg_coeff(nu, nd, nl)
    p = hi.numerator * lo.denominator
    q = hi.denominator * lo.numerator
    ln_seg = rational_ln_ratio(p, q, terms=160)
    delta = c * ln_seg / pi_rat
    alpha_inv += delta
    total_step += delta
    print(f"{name:<16} {float(c):>8.4f} {float(ln_seg):>14.8f} "
          f"{float(delta):>12.6f} {float(alpha_inv):>12.6f}")

print("-" * 65)
print(f"Step-function result: 1/alpha = {float(alpha_inv):.6f}")
print(f"Step-function total delta:      {float(total_step):.6f}")
print()

# PART 2: Boundary shape correction
print("PART 2: Boundary shape corrections (-5/6 per threshold crossing)")
print()

total_correction = Fraction(0)

print(f"{'Species':<8} {'Coeff':>8} {'5/6*Coeff':>12} {'Correction':>14}")
print("-" * 45)

for species_name, species_coeff in species_corrections:
    # Correction = -(5/6) * coeff / pi  (negative — reduces the running)
    correction = five_sixths * species_coeff / pi_rat
    total_correction += correction
    print(f"{species_name:<8} {float(species_coeff):>8.4f} "
          f"{float(five_sixths * species_coeff):>12.6f} "
          f"{float(correction):>14.8f}")

print("-" * 45)
print(f"{'Total':<8} {'':>8} {float(five_sixths * sum(c for _,c in species_corrections)):>12.6f} "
      f"{float(total_correction):>14.8f}")
print()

# PART 3: Apply correction
alpha_inv_corrected = alpha_inv - total_correction

print("=" * 74)
print("COMBINED RESULT")
print("=" * 74)
print()
print(f"Step-function 1/alpha:       {float(alpha_inv):.10f}")
print(f"Boundary correction:        -{float(total_correction):.10f}")
print(f"Corrected 1/alpha:           {float(alpha_inv_corrected):.10f}")
print(f"CODATA target:               137.035999177")
print()

diff = float(alpha_inv_corrected) - 137.035999177
print(f"Difference:     {diff:+.10f}")
print(f"Relative error: {abs(diff)/137.036 * 100:.6f}%")
print()

# 100-digit verification
print("=" * 74)
print("100-DIGIT VERIFICATION")
print("=" * 74)
print()

result_mp = mpf(alpha_inv_corrected.numerator) / mpf(alpha_inv_corrected.denominator)
print(f"Integer pair result (100 digits):")
print(f"  {mp.nstr(result_mp, 100)}")
print()
print(f"CODATA: 137.035999177 (11 significant figures)")
print()

diff_mp = result_mp - mpf('137.035999177')
print(f"Difference: {mp.nstr(diff_mp, 20)}")
print(f"Relative:   {mp.nstr(abs(diff_mp)/mpf('137.036') * 100, 10)}%")
print()

# ============================================================
# Summary of what is integer and what is measured
# ============================================================

print("=" * 74)
print("WHAT IS INTEGER, WHAT IS MEASURED")
print("=" * 74)
print()
print("PURE INTEGER (from particle counting):")
print(f"  Charges:         Q_up = 2/3, Q_down = 1/3, Q_lepton = 1")
print(f"  Color factor:    Nc = 3 for quarks, 1 for leptons")
print(f"  VP coefficients: (2/3)*Nc*Q^2 per species")
print(f"  Boundary shape:  5/6 = (3^2 - 2^2)/(2*3)")
print(f"  Species count:   7 thresholds between m_e and M_Z")
print()
print("INTEGER PAIR (from MATH-2):")
print(f"  pi: ratio of two integers, {pi_rat.numerator.bit_length()} bits")
print(f"  All ln(ratio) values: ratios of two integers")
print()
print("MEASURED (Tier 3):")
print(f"  Starting value:  1/alpha_EM(M_Z) = 127.906")
print(f"  Threshold masses: m_b, m_tau, m_c, m_mu, m_s, m_d, m_u, m_e")
print(f"  (9 measured values total)")
print()
print("THE LAW IS INTEGERS.")
print("The boundary locations and starting value are from the universe.")
print(f"The output is a ratio of two integers with {alpha_inv_corrected.numerator.bit_length()} bit numerator.")
