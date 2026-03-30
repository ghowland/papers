"""
Alpha_EM from Integer Arithmetic — Threshold Matching

Instead of running one beta function from M_Z to m_e with fixed
coefficients, we run in segments. At each quark and lepton mass
threshold, the beta function coefficients change because the
particle counting changes.

Each threshold is a boundary crossing in the PHYS-2 sense.
The integers update at each boundary.

Segments (running down from M_Z = 91.2 GeV):
  M_Z → m_b:     6 quarks, 3 charged leptons (e, mu, tau)
  m_b → m_tau:    5 quarks, 3 charged leptons  
  m_tau → m_c:    5 quarks, 2 charged leptons (e, mu)
  m_c → m_mu:     4 quarks, 2 charged leptons
  m_mu → m_s:     4 quarks, 1 charged lepton (e)
  ...actually, let me be more careful about what's active where.

For the electromagnetic coupling alpha_EM, the running depends on
vacuum polarization from ALL charged particles lighter than the
energy scale. This means quarks AND leptons contribute.

The one-loop QED beta function coefficient for alpha_EM is:
  b0_EM = -(4/3) * sum over active charged fermions of Q_f^2 * N_c

where Q_f is the electric charge in units of e, N_c is the number
of colors (3 for quarks, 1 for leptons), and the sum runs over
fermions with mass < mu.

Wait — I need to be careful about conventions. Let me use the 
standard QED running formula directly rather than going through
the SU(2)xU(1) decomposition for this first pass.

The QED vacuum polarization running of alpha_EM:

  alpha_EM^{-1}(mu_low) = alpha_EM^{-1}(mu_high) 
                          + (2/(3*pi)) * sum_f N_c * Q_f^2 * ln(mu_high/mu_low)

where the sum is over fermions active between mu_low and mu_high.

Actually, the standard formula is:

  alpha_EM^{-1}(q^2) = alpha_EM^{-1}(mu^2) 
                       - (1/(3*pi)) * sum_f N_c * Q_f^2 * ln(q^2/mu^2)

  = alpha_EM^{-1}(mu) - (2/(3*pi)) * sum_f N_c * Q_f^2 * ln(q/mu)

Running DOWN from high to low energy (q < mu):
  ln(q/mu) < 0
  The negative sign in front means alpha_EM^{-1} INCREASES going down
  (coupling weakens at low energy, as expected for QED screening).

Let me rewrite clearly:
  alpha_EM^{-1}(low) = alpha_EM^{-1}(high) 
                       + (2/(3*pi)) * sum_f N_c * Q_f^2 * ln(high/low)

This is positive because ln(high/low) > 0, so alpha^{-1} increases
going to low energy. Coupling weakens. Correct for QED.

The coefficient for each fermion species:
  (2/3) * N_c * Q_f^2

For quarks (N_c = 3):
  up-type (u, c, t):    Q = 2/3,  contribution = (2/3) * 3 * (4/9) = 8/9
  down-type (d, s, b):  Q = -1/3, contribution = (2/3) * 3 * (1/9) = 2/9

For leptons (N_c = 1):
  charged (e, mu, tau):  Q = -1,  contribution = (2/3) * 1 * 1 = 2/3

All exact rationals from particle counting and charge assignments.
"""

from fractions import Fraction
from mpmath import mp, mpf

# ============================================================
# Transcendentals as integer pairs (from MATH-2)
# ============================================================

def rational_arctan(x, terms=80):
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

def rational_pi(terms=80):
    a1 = rational_arctan(Fraction(1, 5), terms)
    a2 = rational_arctan(Fraction(1, 239), terms)
    return 4 * (4 * a1 - a2)

def rational_arctanh(x, terms=120):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        result += power / n
        power *= x_sq
    return result

def rational_ln2(terms=120):
    return 2 * rational_arctanh(Fraction(1, 3), terms)

def rational_ln_ratio(p, q, terms=120):
    """Compute ln(p/q) using reduction to arctanh."""
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


# ============================================================
# Compute pi as integer pair
# ============================================================

print("Computing pi...")
pi_rat = rational_pi(80)
print(f"Done. {pi_rat.numerator.bit_length()} bit numerator.")


# ============================================================
# Particle content — exact rationals from counting
# ============================================================

# Contribution of each fermion to QED vacuum polarization coefficient:
# coefficient = (2/3) * N_c * Q_f^2
# This multiplies (1/pi) * ln(high/low)

# Quarks (N_c = 3):
#   up-type:   Q = 2/3 → coeff = (2/3)*3*(4/9) = 8/9
#   down-type: Q = 1/3 → coeff = (2/3)*3*(1/9) = 2/9

# Leptons (N_c = 1):
#   charged:   Q = 1   → coeff = (2/3)*1*1 = 2/3

coeff_up_type   = Fraction(8, 9)    # per up-type quark
coeff_down_type = Fraction(2, 9)    # per down-type quark
coeff_lepton    = Fraction(2, 3)    # per charged lepton

# ============================================================
# Threshold masses (measured, Tier 3) as exact rationals in MeV
# ============================================================

# We need these as rationals for the ln computation
m_top_MeV  = Fraction(173000, 1)       # 173.0 GeV (above M_Z, not used running down)
m_b_MeV    = Fraction(4180, 1)         # 4.18 GeV
m_tau_MeV  = Fraction(17768, 10)       # 1.7768 GeV  
m_c_MeV    = Fraction(1270, 1)         # 1.27 GeV
m_mu_MeV   = Fraction(105658, 1000)    # 105.658 MeV = 0.10566 GeV
m_s_MeV    = Fraction(93, 1)           # 93 MeV = 0.093 GeV
m_d_MeV    = Fraction(47, 10)          # 4.7 MeV
m_u_MeV    = Fraction(22, 10)          # 2.2 MeV
m_e_MeV    = Fraction(511, 1000)       # 0.511 MeV

M_Z_MeV    = Fraction(911876, 10)      # 91187.6 MeV


# ============================================================
# Define the segments
# ============================================================

# Running down from M_Z. At each threshold, remove one species.
# 
# Active species at M_Z (~91 GeV):
#   Quarks:  u, d, s, c, b (5 flavors — top is above M_Z)
#   Leptons: e, mu, tau (3 charged leptons)
#
# Segments running down:
#   M_Z → m_b:    5 quarks (u,d,s,c,b) + 3 leptons (e,mu,tau)
#   m_b → m_tau:   4 quarks (u,d,s,c) + 3 leptons (e,mu,tau)
#   m_tau → m_c:   4 quarks (u,d,s,c) + 2 leptons (e,mu)
#   m_c → m_mu:    3 quarks (u,d,s) + 2 leptons (e,mu)
#   m_mu → m_s:    3 quarks (u,d,s) + 1 lepton (e)
#   m_s → m_d:     2 quarks (u,d) + 1 lepton (e)
#   m_d → m_u:     1 quark (u) + 1 lepton (e)
#   m_u → m_e:     0 quarks + 1 lepton (e)
#   Below m_e:     nothing running (pure QED, no vacuum polarization)

# For each segment, compute the total coefficient:
# sum_f (2/3) * N_c * Q_f^2

def compute_segment_coeff(up_quarks, down_quarks, leptons):
    """Compute the total vacuum polarization coefficient for a segment.
    up_quarks: number of active up-type quarks (u, c, t)
    down_quarks: number of active down-type quarks (d, s, b)
    leptons: number of active charged leptons (e, mu, tau)
    """
    return (up_quarks * coeff_up_type + 
            down_quarks * coeff_down_type + 
            leptons * coeff_lepton)

# Define segments: (name, mu_high, mu_low, n_up, n_down, n_lepton)
# Quarks by type:
#   up-type:   u, c  (t is above M_Z)
#   down-type: d, s, b

segments = [
    # M_Z to m_b: u,c active (2 up), d,s,b active (3 down), e,mu,tau active (3 leptons)
    ("M_Z → m_b",    M_Z_MeV,  m_b_MeV,   2, 3, 3),
    # m_b to m_tau: remove b → u,c (2 up), d,s (2 down), e,mu,tau (3 leptons)
    ("m_b → m_tau",  m_b_MeV,  m_tau_MeV,  2, 2, 3),
    # m_tau to m_c: remove tau → u,c (2 up), d,s (2 down), e,mu (2 leptons)
    ("m_tau → m_c",  m_tau_MeV, m_c_MeV,   2, 2, 2),
    # m_c to m_mu: remove c → u (1 up), d,s (2 down), e,mu (2 leptons)  
    ("m_c → m_mu",   m_c_MeV,  m_mu_MeV,   1, 2, 2),
    # m_mu to m_s: remove mu → u (1 up), d,s (2 down), e (1 lepton)
    ("m_mu → m_s",   m_mu_MeV, m_s_MeV,    1, 2, 1),
    # m_s to m_d: remove s → u (1 up), d (1 down), e (1 lepton)
    ("m_s → m_d",    m_s_MeV,  m_d_MeV,    1, 1, 1),
    # m_d to m_u: remove d → u (1 up), 0 down, e (1 lepton)
    ("m_d → m_u",    m_d_MeV,  m_u_MeV,    1, 0, 1),
    # m_u to m_e: remove u → 0 up, 0 down, e (1 lepton)
    ("m_u → m_e",    m_u_MeV,  m_e_MeV,    0, 0, 1),
]


# ============================================================
# Run the segmented transformation
# ============================================================

print("\n" + "=" * 70)
print("ALPHA_EM WITH THRESHOLD MATCHING")
print("Boundaries tell the law what to do")
print("=" * 70)

# Starting value
alpha_inv = Fraction(127906, 1000)  # 1/alpha_EM(M_Z) = 127.906

print(f"\nStarting: 1/alpha_EM(M_Z) = {float(alpha_inv):.6f}")
print(f"\n{'Segment':<16} {'Coeff':>10} {'ln(hi/lo)':>14} {'Delta':>12} {'1/alpha':>14}")
print("-" * 70)

total_delta = Fraction(0)

for name, mu_hi, mu_lo, n_up, n_down, n_lep in segments:
    # Coefficient for this segment
    coeff = compute_segment_coeff(n_up, n_down, n_lep)
    
    # ln(mu_hi / mu_lo) as integer pair
    ln_seg = rational_ln_ratio(
        mu_hi.numerator * mu_lo.denominator,
        mu_hi.denominator * mu_lo.numerator,
        terms=120
    )
    
    # Delta for this segment:
    # delta = coeff * ln(hi/lo) / pi
    delta = coeff * ln_seg / pi_rat
    
    alpha_inv += delta
    total_delta += delta
    
    print(f"{name:<16} {float(coeff):>10.6f} {float(ln_seg):>14.8f} "
          f"{float(delta):>12.6f} {float(alpha_inv):>14.6f}")

print("-" * 70)
print(f"{'Total delta':<16} {'':>10} {'':>14} {float(total_delta):>12.6f} {float(alpha_inv):>14.6f}")

print(f"\n{'=' * 70}")
print(f"RESULT")
print(f"{'=' * 70}")
print(f"")
print(f"1/alpha_EM at m_e scale (integer arithmetic): {float(alpha_inv):.10f}")
print(f"CODATA value:                                  137.035999177")
print(f"Difference:                                    {float(alpha_inv) - 137.036:.6f}")
print(f"Relative error:                                {abs(float(alpha_inv) - 137.036)/137.036 * 100:.4f}%")

# ============================================================
# Verification with mpmath
# ============================================================

print(f"\n--- Verification ---")
mp.dps = 50
result_mp = mpf(alpha_inv.numerator) / mpf(alpha_inv.denominator)
codata = mpf('137.035999177')
diff = abs(result_mp - codata)
print(f"Integer result (30 digits): {mp.nstr(result_mp, 30)}")
print(f"CODATA:                     137.035999177")
print(f"Absolute difference:        {mp.nstr(diff, 10)}")
print(f"Relative difference:        {mp.nstr(diff/codata * 100, 6)}%")

# ============================================================
# Show the integer structure
# ============================================================

print(f"\n--- Integer structure ---")
print(f"Type: {type(alpha_inv)}")
print(f"Numerator:   {alpha_inv.numerator.bit_length()} bits, {len(str(abs(alpha_inv.numerator)))} digits")
print(f"Denominator: {alpha_inv.denominator.bit_length()} bits, {len(str(alpha_inv.denominator))} digits")

print(f"\n--- Segment coefficients (all exact rationals) ---")
for name, mu_hi, mu_lo, n_up, n_down, n_lep in segments:
    coeff = compute_segment_coeff(n_up, n_down, n_lep)
    print(f"  {name:<16}: {coeff} = {float(coeff):.6f}  "
          f"({n_up} up + {n_down} down quarks, {n_lep} leptons)")

print(f"\n--- What is integer, what is measured ---")
print(f"INTEGER (from counting):")
print(f"  Quark charges:    2/3, -1/3")
print(f"  Color factor:     3")
print(f"  Lepton charge:    1")  
print(f"  VP coefficient:   (2/3) * N_c * Q^2 per species")
print(f"  All segment coefficients are exact rationals")
print(f"")
print(f"INTEGER PAIR (from MATH-2):")
print(f"  pi = p/q with {pi_rat.numerator.bit_length()}-bit integers")
print(f"  Each ln(threshold ratio) = p/q with exact integer pairs")
print(f"")
print(f"MEASURED (Tier 3, from universe):")
print(f"  alpha_EM(M_Z) = 1/127.906")
print(f"  Quark masses: m_b={float(m_b_MeV)} MeV, m_c={float(m_c_MeV)} MeV, etc.")
print(f"  Lepton masses: m_tau={float(m_tau_MeV)} MeV, m_mu={float(m_mu_MeV)} MeV, m_e={float(m_e_MeV)} MeV")
print(f"")
print(f"The transformation law (beta function + thresholds) is integers.")
print(f"The boundary locations (particle masses) are measured.")
print(f"The starting value (alpha at M_Z) is measured.")
print(f"The output (alpha at m_e) is computed from integers + measurements.")
