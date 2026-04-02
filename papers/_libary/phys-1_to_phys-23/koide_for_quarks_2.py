from fractions import Fraction
from math import gcd, sqrt, atan2, cos, sin, pi, acos

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

def koide_float(m1, m2, m3):
    s1, s2, s3 = sqrt(m1), sqrt(m2), sqrt(m3)
    return (m1 + m2 + m3) / (s1 + s2 + s3)**2

# ================================================================
# FIX 4: Test with POLE masses for quarks
# ================================================================

print("=" * 65)
print("QUARK KOIDE: POLE MASSES vs MSbar")
print("=" * 65)
print()

# MSbar at 2 GeV (PDG 2024)
m_u_ms = 2.16
m_d_ms = 4.67
m_s_ms = 93.4
m_c_ms = 1270.0
m_b_ms = 4180.0
m_t_pole = 172690.0
m_t_ms = 163000.0

# Pole masses (PDG / lattice estimates)
m_c_pole = 1670.0   # ~1.67 GeV
m_b_pole = 4780.0   # ~4.78 GeV

# Lepton reference
m_e = 0.51099895
m_mu = 105.6583755
m_tau = 1776.86

r_lep = koide_float(m_e, m_mu, m_tau)

print(f"  Leptons (pole):          {r_lep:.6f} (target: 0.666667)")
print()

# Down-type: MSbar
r_d_ms = koide_float(m_d_ms, m_s_ms, m_b_ms)
print(f"  Down MSbar (d,s,b):      {r_d_ms:.6f}")

# Down-type: pole for b
r_d_pole_b = koide_float(m_d_ms, m_s_ms, m_b_pole)
print(f"  Down pole-b (d,s,b):     {r_d_pole_b:.6f}")
print()

# Up-type: MSbar
r_u_ms = koide_float(m_u_ms, m_c_ms, m_t_pole)
print(f"  Up MSbar-c (u,c,t):      {r_u_ms:.6f}")

# Up-type: pole for c
r_u_pole_c = koide_float(m_u_ms, m_c_pole, m_t_pole)
print(f"  Up pole-c (u,c,t):       {r_u_pole_c:.6f}")

# Up-type: pole c, MSbar t
r_u_pole_c_ms_t = koide_float(m_u_ms, m_c_pole, m_t_ms)
print(f"  Up pole-c MSbar-t:       {r_u_pole_c_ms_t:.6f}")
print()

# ================================================================
# FIX 3: Test same a=sqrt(2), different theta_0
# ================================================================

print("=" * 65)
print("FIX 3: SAME a=sqrt(2), DIFFERENT theta_0")
print("=" * 65)
print()
print("Koide parametrization: sqrt(m_i) = M*(1 + sqrt(2)*cos(theta_0 + 2*pi*i/3))")
print("Two free params: M (scale) and theta_0 (phase).")
print("For leptons: theta_0 ~ 0.2222 rad ~ 12.7 degrees.")
print()
print("If quarks have a=sqrt(2) but different theta_0,")
print("what Koide ratio results?")
print()

# For a = sqrt(2), the Koide ratio is ALWAYS 2/3 regardless of theta_0.
# This is the content of the PHYS-8 proof!
# (1 + a^2/2)/N = (1 + 2/2)/3 = 2/3 for ANY theta_0.
# The ratio does NOT depend on theta_0 — only M and theta_0 drop out.

print("WAIT — the PHYS-8 identity says:")
print("  (sum m) / (sum sqrt(m))^2 = (1 + a^2/2)/N")
print("This is INDEPENDENT of theta_0 and M.")
print("If a = sqrt(2) and N = 3, the ratio is 2/3 for ANY theta_0.")
print()
print("So 'same a, different theta_0' gives the SAME ratio 2/3.")
print("The quark ratio differs from 2/3, therefore a != sqrt(2).")
print("The amplitude MUST differ. The phase can't explain it.")
print()

# Verify numerically
a = sqrt(2)
print("Verification: Koide ratio at a=sqrt(2) for various theta_0:")
for theta_deg in range(0, 180, 15):
    theta = theta_deg * pi / 180
    s = [1 + a*cos(theta + 2*pi*i/3) for i in range(3)]
    if all(x > 0 for x in s):
        masses = [x**2 for x in s]
        r = sum(masses) / sum(sqrt(m) for m in masses)**2
        print(f"  theta_0 = {theta_deg:>3d} deg: ratio = {r:.8f}")
    else:
        print(f"  theta_0 = {theta_deg:>3d} deg: negative sqrt(m), skip")
print()
print("ALL give 2/3 exactly (to numerical precision).")
print("The phase theta_0 determines WHICH masses you get,")
print("but the RATIO is always 2/3 at a=sqrt(2).")
print()

# ================================================================
# FIX 3b: So what amplitude DO the quarks have?
# And: reconstruct (a, theta_0) for each sector properly
# ================================================================

print("=" * 65)
print("PROPER PARAMETER EXTRACTION")
print("=" * 65)
print()

def extract_koide_params(m1, m2, m3, label):
    """Extract M, a, theta_0 from three masses."""
    s1, s2, s3 = sqrt(m1), sqrt(m2), sqrt(m3)
    S = s1 + s2 + s3
    M = S / 3
    
    # residuals r_i = sqrt(m_i) - M = a*M*cos(theta_0 + 2*pi*i/3)
    r = [s1 - M, s2 - M, s3 - M]
    
    # a*M from sum of squares: sum(r_i^2) = (3/2)*a^2*M^2
    sum_r2 = sum(x**2 for x in r)
    a_sq = 2 * sum_r2 / (3 * M**2)
    a_val = sqrt(a_sq) if a_sq > 0 else 0
    
    # theta_0 from atan2 on the residuals
    # r_0 = a*M*cos(theta_0)
    # r_1 = a*M*cos(theta_0 + 2*pi/3)
    # r_2 = a*M*cos(theta_0 + 4*pi/3)
    # 
    # Use: sum(r_i * cos(2*pi*i/3)) = (3/2)*a*M*cos(theta_0)
    #      sum(r_i * sin(2*pi*i/3)) = -(3/2)*a*M*sin(theta_0)
    
    cos_part = sum(r[i] * cos(2*pi*i/3) for i in range(3))
    sin_part = sum(r[i] * sin(2*pi*i/3) for i in range(3))
    # cos_part = (3/2)*a*M*cos(theta_0)
    # sin_part = -(3/2)*a*M*sin(theta_0)
    
    theta_0 = atan2(-sin_part, cos_part)
    theta_0_deg = theta_0 * 180 / pi
    
    # Koide ratio
    ratio = (m1 + m2 + m3) / (s1 + s2 + s3)**2
    
    print(f"  {label}:")
    print(f"    masses: {m1:.4f}, {m2:.4f}, {m3:.4f}")
    print(f"    M = {M:.6f}")
    print(f"    a = {a_val:.6f}  (Koide: sqrt(2) = {sqrt(2):.6f})")
    print(f"    a^2 = {a_sq:.6f}  (Koide: 2)")
    print(f"    theta_0 = {theta_0:.6f} rad = {theta_0_deg:.2f} deg")
    print(f"    Koide ratio = {ratio:.6f}")
    print()
    
    # Verify reconstruction
    recon = [M * (1 + a_val * cos(theta_0 + 2*pi*i/3)) for i in range(3)]
    print(f"    Reconstructed sqrt(m): {recon[0]:.4f}, {recon[1]:.4f}, {recon[2]:.4f}")
    print(f"    Original sqrt(m):      {s1:.4f}, {s2:.4f}, {s3:.4f}")
    print()
    
    return M, a_val, a_sq, theta_0, theta_0_deg, ratio

print("--- Charged Leptons (pole masses) ---")
M_l, a_l, a2_l, t0_l, t0d_l, r_l = extract_koide_params(m_e, m_mu, m_tau, "e, mu, tau")

print("--- Down-type Quarks (MSbar 2 GeV) ---")
M_d, a_d, a2_d, t0_d, t0d_d, r_d = extract_koide_params(m_d_ms, m_s_ms, m_b_ms, "d, s, b MSbar")

print("--- Down-type Quarks (pole b) ---")
M_dp, a_dp, a2_dp, t0_dp, t0d_dp, r_dp = extract_koide_params(m_d_ms, m_s_ms, m_b_pole, "d, s, b (pole b)")

print("--- Up-type Quarks (MSbar c, pole t) ---")
M_u, a_u, a2_u, t0_u, t0d_u, r_u = extract_koide_params(m_u_ms, m_c_ms, m_t_pole, "u, c, t MSbar-c")

print("--- Up-type Quarks (pole c, pole t) ---")
M_up, a_up, a2_up, t0_up, t0d_up, r_up = extract_koide_params(m_u_ms, m_c_pole, m_t_pole, "u, c, t pole-c")

# ================================================================
# Summary table
# ================================================================

print("=" * 65)
print("SUMMARY TABLE")
print("=" * 65)
print()
print(f"  {'Sector':<25} {'a':>8} {'a^2':>8} {'theta_0':>10} {'Koide':>8}")
print(f"  {'-'*25} {'-'*8} {'-'*8} {'-'*10} {'-'*8}")
print(f"  {'Leptons (pole)':<25} {a_l:>8.4f} {a2_l:>8.4f} {t0d_l:>9.2f}° {r_l:>8.6f}")
print(f"  {'Down MSbar':<25} {a_d:>8.4f} {a2_d:>8.4f} {t0d_d:>9.2f}° {r_d:>8.6f}")
print(f"  {'Down pole-b':<25} {a_dp:>8.4f} {a2_dp:>8.4f} {t0d_dp:>9.2f}° {r_dp:>8.6f}")
print(f"  {'Up MSbar-c':<25} {a_u:>8.4f} {a2_u:>8.4f} {t0d_u:>9.2f}° {r_u:>8.6f}")
print(f"  {'Up pole-c':<25} {a_up:>8.4f} {a2_up:>8.4f} {t0d_up:>9.2f}° {r_up:>8.6f}")
print(f"  {'Koide reference':<25} {'1.4142':>8} {'2.0000':>8} {'any':>10} {'0.6667':>8}")
print()

# ================================================================
# FIX 1: Proper 2-of-3 correction scan with wider range
# ================================================================

print("=" * 65)
print("FIX 1: 2-of-3 CORRECTION SCAN (wider range)")
print("=" * 65)
print()
print("Scaling m_d and m_s by factor f (NOT universal — m_b fixed).")
print("This IS non-universal, so the invariance proof does NOT apply.")
print()

# Fine scan
best = None
for f_num in range(1, 10000):
    f = f_num / 10000.0
    r = koide_float(m_d_ms * f, m_s_ms * f, m_b_ms)
    if best is None or abs(r - 2/3) < abs(best[1] - 2/3):
        best = (f, r)
    if abs(r - 2/3) < 0.0005:
        print(f"  f = {f:.4f}: m_d = {m_d_ms*f:.3f}, m_s = {m_s_ms*f:.3f}, Koide = {r:.6f}")

print(f"\n  Best f = {best[0]:.4f}, Koide = {best[1]:.6f}, vs 2/3 = 0.666667")
print(f"  Minimum achievable distance: {abs(best[1] - 2/3):.6f}")
print()

# Also scan wider: f from 0.001 to 100
print("  Extended scan f from 0.001 to 100:")
best2 = None
for exp in range(-30, 50):
    f = 10**(exp/10.0)
    r = koide_float(m_d_ms * f, m_s_ms * f, m_b_ms)
    if best2 is None or abs(r - 2/3) < abs(best2[1] - 2/3):
        best2 = (f, r)

print(f"  Best f = {best2[0]:.6f}, Koide = {best2[1]:.6f}")
print()

# Theoretical analysis: as f -> 0, m_d, m_s -> 0, only m_b contributes
# ratio -> m_b / (sqrt(m_b))^2 = 1 (single mass limit)
# As f -> inf, m_d, m_s dominate, m_b negligible
# ratio -> (m_d + m_s) / (sqrt(m_d) + sqrt(m_s))^2
# = Koide for just m_d, m_s — which for 2 masses is bounded below by 1/2
# So the ratio goes from ~1/2 (f large) through some minimum to 1 (f -> 0)
# The question is whether it passes through 2/3

r_large_f = koide_float(m_d_ms * 1e6, m_s_ms * 1e6, m_b_ms)
r_small_f = koide_float(m_d_ms * 1e-6, m_s_ms * 1e-6, m_b_ms)
print(f"  Koide at f = 1e6 (light quarks dominate):  {r_large_f:.6f}")
print(f"  Koide at f = 1e-6 (m_b dominates):         {r_small_f:.6f}")
print(f"  Koide at f = 1 (MSbar):                     {koide_float(m_d_ms, m_s_ms, m_b_ms):.6f}")
print()
print(f"  Range: [{min(r_large_f, r_small_f):.4f}, {max(r_large_f, r_small_f):.4f}]")
print(f"  2/3 = 0.6667 is {'IN' if min(r_large_f, r_small_f) < 2/3 < max(r_large_f, r_small_f) else 'OUTSIDE'} range")
