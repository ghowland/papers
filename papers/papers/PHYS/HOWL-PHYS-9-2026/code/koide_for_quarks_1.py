from fractions import Fraction
from math import gcd, sqrt

def simplify(f, max_digits=40):
    n, d = f.numerator, f.denominator
    while n.bit_length() > int(max_digits * 3.32) or d.bit_length() > int(max_digits * 3.32):
        n //= 2
        d //= 2
    if d == 0: d = 1
    g = gcd(abs(n), abs(d))
    return Fraction(n // g, d // g)

def rat_sqrt(x, iters=20):
    if x == Fraction(0): return Fraction(0)
    g = Fraction(int(float(x) ** 0.5 * 10**18), 10**18)
    for i in range(iters):
        g = (g + x / g) / 2
        if i % 3 == 2: g = simplify(g, 40)
    return simplify(g, 40)

# MSbar quark masses at 2 GeV
m_u = Fraction(216, 100)
m_d = Fraction(467, 100)
m_s = Fraction(934, 10)
m_c = Fraction(1270, 1)
m_b = Fraction(4180, 1)
m_t = Fraction(172690, 1)

print("=" * 65)
print("CONFINEMENT CORRECTION TO QUARK KOIDE")
print("=" * 65)
print()
print("LOGIC: Confinement inflates apparent inertia of light quarks.")
print("The MSbar mass includes binding/confinement effects that")
print("don't affect the underlying pattern inertia.")
print()
print("PHYS-6 found: below 2 GeV, measured/perturbative ~ 0.61")
print("This means the 'true' perturbative contribution is LARGER")
print("than what's measured. Or equivalently: the confinement")
print("boundary REDUCES the VP from perturbative by factor 0.61.")
print()
print("But for masses, the question is different: does confinement")
print("change the MASS or the MEASUREMENT of the mass?")
print()
print("In PHYS-2: mass values are boundary-depth readings.")
print("MSbar at 2 GeV is a specific boundary depth reading.")
print("The 'true inertia' of the quark pattern may differ from")
print("the MSbar reading at 2 GeV.")
print()

# Approach 1: What correction factor on light quark masses
# would make the down-type Koide ratio = 2/3?
#
# If m_d -> m_d * f and m_s -> m_s * f (same factor for both
# light quarks) and m_b stays fixed:
# Test a range of correction factors

print("=" * 65)
print("APPROACH 1: Uniform correction to light quarks")
print("What factor f on m_d and m_s makes down-type Koide = 2/3?")
print("=" * 65)
print()

# Actually, the correction should depend on how deep each quark
# is inside confinement. m_b at 4.18 GeV is above the ~2 GeV
# confinement scale. m_s at 93 MeV is below. m_d at 4.7 MeV is
# deep below.
#
# Try: correct only quarks below confinement scale (~2 GeV)
# m_d and m_s are below. m_b is above.
# What single factor f on BOTH m_d and m_s gives Koide = 2/3?

def koide_ratio_val(m1, m2, m3):
    s1 = float(rat_sqrt(m1))
    s2 = float(rat_sqrt(m2))
    s3 = float(rat_sqrt(m3))
    num = float(m1 + m2 + m3)
    den = (s1 + s2 + s3)**2
    return num / den

# Scan f
print(f"  {'f':>8} {'m_d_corr':>10} {'m_s_corr':>10} {'Koide':>10} {'vs 2/3':>10}")
for f_num in range(20, 120):
    f = Fraction(f_num, 100)
    m_d_c = m_d * f
    m_s_c = m_s * f
    r = koide_ratio_val(m_d_c, m_s_c, m_b)
    if abs(r - 2/3) < 0.005:
        print(f"  {float(f):>8.2f} {float(m_d_c):>10.3f} {float(m_s_c):>10.3f} {r:>10.6f} {r-2/3:>+10.6f}")

print()

# Approach 2: Each quark gets a correction based on its distance
# from the confinement scale
# The running mass from scale mu to scale mu_0:
# m(mu_0) = m(mu) * (alpha_s(mu_0)/alpha_s(mu))^(gamma/b0)
# where gamma is the anomalous dimension
#
# But this IS what MSbar already does. The question is whether
# there's a FURTHER correction at the confinement boundary.

# Approach 3: What if quarks use a different Koide amplitude?
# From the data: down-type a^2 = 2.39, up-type a^2 = 3.09
# Is there a pattern?
print("=" * 65)
print("APPROACH 3: Different amplitudes per sector")
print("=" * 65)
print()

a2_lep = 2.0000
a2_down = 2.3886
a2_up = 3.0939

print(f"  Leptons:    a^2 = {a2_lep:.4f}")
print(f"  Down quarks: a^2 = {a2_down:.4f}")
print(f"  Up quarks:   a^2 = {a2_up:.4f}")
print()
print(f"  Ratios:")
print(f"    a^2_down / a^2_lep = {a2_down/a2_lep:.4f}")
print(f"    a^2_up / a^2_lep = {a2_up/a2_lep:.4f}")
print(f"    a^2_up / a^2_down = {a2_up/a2_down:.4f}")
print()

# Are these simple rationals?
for label, ratio in [
    ("down/lep", a2_down/a2_lep),
    ("up/lep", a2_up/a2_lep),
    ("up/down", a2_up/a2_down),
]:
    # Test nearby simple rationals
    candidates = []
    for p in range(1, 20):
        for q in range(1, 20):
            r = p/q
            if abs(r - ratio) / ratio < 0.05:
                candidates.append((p, q, r, abs(r-ratio)/ratio*100))
    candidates.sort(key=lambda x: x[3])
    print(f"  {label} = {ratio:.4f}")
    for p, q, r, pct in candidates[:5]:
        print(f"    {p}/{q} = {r:.4f} ({pct:+.2f}%)")
    print()

# Approach 4: What if the Koide parametrization uses RUNNING masses
# at a COMMON scale — and that scale matters?
# MSbar at 2 GeV is the conventional choice. What about MSbar at M_Z?
# Or MSbar at m_t?
# The quark masses run. At higher scales, light quark masses are SMALLER
# (they run down with increasing energy in QCD).
# Running m_d and m_s DOWN (to lower values) would REDUCE the Koide ratio
# toward 2/3.

print("=" * 65)
print("APPROACH 4: Scale dependence of quark Koide ratio")
print("=" * 65)
print()
print("  Quark masses RUN with scale in QCD.")
print("  At higher scales, light masses are SMALLER.")
print("  The QCD running factor from mu1 to mu2:")
print("  m(mu2)/m(mu1) = (alpha_s(mu2)/alpha_s(mu1))^(4/b0)")
print("  where b0 = 23/3 (5 flavors) or 7 (6 flavors)")
print()

# Estimate: running from 2 GeV to M_Z
# alpha_s(2 GeV) ~ 0.30, alpha_s(M_Z) = 0.1180
# gamma_m = 4 (one-loop mass anomalous dimension)
# b0 = 23/3 for 5 flavors
# m(M_Z)/m(2GeV) = (0.1180/0.30)^(12/23)
import math
ratio_alpha = 0.1180 / 0.30
b0_5f = 23/3
gamma_over_b0 = 4 / b0_5f  # = 12/23
running_factor = ratio_alpha ** gamma_over_b0

print(f"  alpha_s(2 GeV) ~ 0.30")
print(f"  alpha_s(M_Z)  = 0.1180")
print(f"  gamma_m/b0 = 4/(23/3) = 12/23 = {gamma_over_b0:.6f}")
print(f"  Running factor 2 GeV -> M_Z: {running_factor:.4f}")
print()

# All light quark masses scale by the same factor
m_u_MZ = float(m_u) * running_factor
m_d_MZ = float(m_d) * running_factor
m_s_MZ = float(m_s) * running_factor
m_c_MZ = float(m_c) * running_factor
m_b_MZ = float(m_b) * running_factor

print(f"  At M_Z (approximate):")
print(f"    m_u = {m_u_MZ:.3f} MeV")
print(f"    m_d = {m_d_MZ:.3f} MeV")
print(f"    m_s = {m_s_MZ:.3f} MeV")
print(f"    m_c = {m_c_MZ:.1f} MeV")
print(f"    m_b = {m_b_MZ:.1f} MeV")
print()

# Koide at M_Z scale
def koide_float(m1, m2, m3):
    s1, s2, s3 = sqrt(m1), sqrt(m2), sqrt(m3)
    return (m1 + m2 + m3) / (s1 + s2 + s3)**2

r_d_MZ = koide_float(m_d_MZ, m_s_MZ, m_b_MZ)
r_u_MZ = koide_float(m_u_MZ, m_c_MZ, 172690)  # pole mass for t

print(f"  Koide at M_Z scale:")
print(f"    Down (d,s,b): {r_d_MZ:.6f} (was {0.731428:.6f} at 2 GeV)")
print(f"    Up (u,c,t):   {r_u_MZ:.6f} (was {0.848981:.6f} at 2 GeV)")
print(f"    Change: same — universal scaling doesn't change Koide ratio!")
print()
print("  KEY INSIGHT: The Koide ratio is SCALE-INVARIANT under")
print("  universal QCD mass running (all masses scale by same factor).")
print("  The ratio (sum m)/(sum sqrt(m))^2 is invariant under m -> c*m")
print("  because both numerator and denominator scale as c.")
print()
print("  This means the Koide failure for quarks is NOT a running")
print("  scale artifact. It's a genuine structural difference between")
print("  lepton and quark sectors.")
print()

# Wait — is it really invariant? Let me check.
# (c*m1 + c*m2 + c*m3) / (sqrt(c*m1) + sqrt(c*m2) + sqrt(c*m3))^2
# = c*(m1+m2+m3) / (sqrt(c))^2*(sqrt(m1)+sqrt(m2)+sqrt(m3))^2
# = c*(sum m) / (c * (sum sqrt(m))^2)
# = (sum m) / (sum sqrt(m))^2
# YES, exactly invariant. The c cancels perfectly.

print("  PROOF: Under m_i -> c*m_i for all i:")
print("  (sum c*m_i) / (sum sqrt(c*m_i))^2")
print("  = c*(sum m_i) / (sqrt(c) * sum sqrt(m_i))^2")
print("  = c*(sum m_i) / (c * (sum sqrt(m_i))^2)")
print("  = (sum m_i) / (sum sqrt(m_i))^2")
print("  QED. The Koide ratio is exactly scale-invariant.")
print()
print("  CONSEQUENCE: The quark Koide failure cannot be fixed by")
print("  choosing a different renormalization scale. The failure is")
print("  structural, not an artifact of the scale choice.")
print()

# BUT — what if the correction is NOT universal?
# Confinement affects light quarks MORE than heavy quarks.
# That's a NON-universal correction that WOULD change the ratio.
print("=" * 65)
print("NON-UNIVERSAL CONFINEMENT CORRECTION")
print("=" * 65)
print()
print("  Universal scaling preserves Koide (proven above).")
print("  NON-universal correction (different factor per quark) changes it.")
print("  Confinement is non-universal: it affects m_d >> m_s >> m_b.")
print()
print("  The question: is there a physically motivated non-universal")
print("  correction that restores Koide for quarks?")
print()
print("  This requires knowing how confinement affects each quark's")
print("  apparent inertia differently. That's the inside face of the")
print("  confinement boundary (PHYS-6) — where measurement begins.")
print("  We cannot compute this from perturbative QCD.")
print()
print("  STATUS: Logical path exists but is blocked at the")
print("  confinement boundary. Same wall as hadronic VP.")
