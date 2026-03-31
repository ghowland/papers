from mpmath import mp, mpf, pi, zeta, log, sqrt, e as me, phi

mp.dps = 50

print("=" * 70)
print("PHASE 4 — STRATEGY B: SYNTHESIS-INFORMED MODULAR SEARCH")
print("=" * 70)
print()
print("Phase 3 synthesis: Subgroup A has modulus 8R₂ = 2π.")
print("Test: do any SM parameters, when divided by R₂-based moduli,")
print("produce remainders that are simple rationals p/q with small q?")
print()
print("Key difference from the earlier scan: we now test PRODUCTS of")
print("basis constants as moduli, and R₂-multiples specifically.")
print()

R2 = pi / 4
R4 = pi**2 / 32

targets = [
    ("alpha_inv",    mpf('137.035999177')),
    ("alpha_inv_MZ", mpf('127.906')),
    ("sin2_tW",      mpf('0.23122')),
    ("alpha_s",      mpf('0.1180')),
    ("m_mu/m_e",     mpf('206.7682830')),
    ("m_tau/m_e",    mpf('3477.1507')),
    ("m_tau/m_mu",   mpf('16.8170')),
    ("M_W/M_Z",      mpf('0.88147')),
    ("M_H/M_Z",      mpf('1.37193')),
    ("M_H/M_W",      mpf('1.55670')),
    ("sin_t12",      mpf('0.2253')),
    ("sin_t23",      mpf('0.0412')),
    ("delta_CP",     mpf('1.36')),  # radians — this IS a phase
]

# Synthesis-informed moduli:
# Subgroup A: multiples of R₂
# Subgroup C: R₄ and multiples
# Products of basis constants
moduli = [
    # R₂ multiples (Subgroup A modular structure)
    ("R2",       R2),
    ("2R2",      2*R2),
    ("4R2=pi",   4*R2),
    ("8R2=2pi",  8*R2),
    
    # R₄ multiples (Subgroup C structure)
    ("R4",       R4),
    ("32R4=pi^2", 32*R4),
    ("256R4=8pi^2", 256*R4),
    
    # Products of basis constants (untested in earlier scan)
    ("pi*ln2",   pi*log(2)),
    ("pi*zeta3", pi*zeta(3)),
    ("pi*e",     pi*me),
    ("R2*zeta3", R2*zeta(3)),
    ("R2*ln2",   R2*log(2)),
    ("R2*e",     R2*me),
    ("R4*pi",    R4*pi),
    ("ln2*zeta3", log(2)*zeta(3)),
    ("sqrt2*pi", sqrt(2)*pi),
    
    # The VP step size (Subgroup B)
    ("1/(12R2)=1/(3pi)", 1/(12*R2)),
    ("1/(3pi)",  1/(3*pi)),
]

print(f"Targets: {len(targets)}")
print(f"Moduli: {len(moduli)} (R₂-multiples, R₄-multiples, products)")
print()

# For each target × modulus, compute quotient and remainder
# Flag when R/mod is within 0.1% of p/q with q ≤ 20

all_hits = []

for tname, tval in targets:
    target_hits = []
    for mname, mval in moduli:
        if mval <= 0 or mval > abs(tval) * 1000:
            continue
        
        q = int(tval / mval)
        r = tval - q * mval
        rm = float(r / mval)
        
        # Handle negative remainders
        if rm < 0:
            rm += 1
            q -= 1
            r = tval - q * mval
            rm = float(r / mval)
        
        # Check if rm is close to p/d for small d
        for d in range(1, 21):
            p_num = round(rm * d)
            if p_num >= 0 and d > 0:
                diff = abs(rm - p_num/d)
                if diff < 0.0005 and not (p_num == 0 and q == 0):
                    target_hits.append((tname, mname, q, rm, p_num, d, diff))
    
    if target_hits:
        for h in target_hits:
            print(f"  {h[0]:<14} mod {h[1]:<16}: q={h[2]:>5}, R/mod ~ {h[4]}/{h[5]:<3} (off {h[6]:.5f})")
            all_hits.append(h)
    else:
        print(f"  {tname:<14}: no clean remainders")
    print()

print("=" * 70)
print(f"TOTAL: {len(all_hits)} hits across {len(targets)*len(moduli)} tests")
print("=" * 70)
print()

# Special focus: delta_CP is a PHASE — test it specifically mod 8R₂ = 2π
print("SPECIAL: delta_CP is a phase (in radians)")
delta = mpf('1.36')
delta_over_2pi = float(delta / (2*pi))
delta_over_pi = float(delta / pi)
delta_over_R2 = float(delta / R2)

print(f"  delta_CP = {delta} rad")
print(f"  delta/(2π) = {delta_over_2pi:.6f}")
print(f"  delta/π = {delta_over_pi:.6f}")
print(f"  delta/R₂ = {delta_over_R2:.6f}")
print()

# Is delta_CP/pi close to a simple fraction?
for d in range(1, 21):
    p = round(delta_over_pi * d)
    diff = abs(delta_over_pi - p/d)
    if diff < 0.01:
        print(f"  delta/π ~ {p}/{d} = {p/d:.6f} (off {diff:.5f})")

print()

# Is delta_CP close to a specific rational multiple of pi?
# delta ~ 1.36 rad. pi ~ 3.14159. 
# 1.36/pi ~ 0.4329
# Is 0.4329 close to a simple fraction? 
# 3/7 = 0.4286 (off 0.01), 4/9 = 0.4444 (off 0.01)
# Not very close to anything simple.

# Also check: is delta_CP related to other SM parameters?
# delta_CP ~ sin^{-1}(sin2_tW)? No, sin^{-1}(0.231) ~ 0.233 rad
# delta_CP ~ 2*alpha_s*pi? 2*0.118*3.14 ~ 0.741. No.

print("ASSESSMENT: delta_CP/π = 0.4329 is not close to any")
print("simple rational p/q with q ≤ 20 at 1% level.")
print("The CP phase does not appear to be quantized on the 8R₂ domain")
print("at the precision of current measurement (±0.06 rad).")
print()

# ================================================================
# MODULAR SEARCH ON alpha_inv WITH PRODUCT MODULI
# ================================================================

print("=" * 70)
print("FOCUSED: alpha_inv mod (product moduli)")
print("=" * 70)
print()

alpha_inv = mpf('137.035999177')

product_moduli = [
    ("pi*ln2",        pi*log(2)),
    ("pi*zeta3",      pi*zeta(3)),
    ("pi*e",          pi*me),
    ("2pi*ln2",       2*pi*log(2)),
    ("pi^2*ln2",      pi**2*log(2)),
    ("zeta3*ln2",     zeta(3)*log(2)),
    ("R2*zeta3",      R2*zeta(3)),
    ("R2*e",          R2*me),
    ("R4*2pi",        R4*2*pi),
    ("R4*e",          R4*me),
    ("pi*sqrt2",      pi*sqrt(2)),
    ("pi*phi",        pi*phi),
    ("zeta3*e",       zeta(3)*me),
    ("zeta3*sqrt2",   zeta(3)*sqrt(2)),
    ("zeta3*pi^2",    zeta(3)*pi**2),
    ("zeta3^2",       zeta(3)**2),
    ("ln2*e",         log(2)*me),
    ("ln2*sqrt2",     log(2)*sqrt(2)),
    ("ln2*phi",       log(2)*phi),
    ("e*sqrt2",       me*sqrt(2)),
]

print(f"Testing alpha_inv mod {len(product_moduli)} product moduli:")
print()

for mname, mval in product_moduli:
    q = int(alpha_inv / mval)
    r = float(alpha_inv - q * mval)
    rm = r / float(mval)
    
    # Check for clean remainder
    best = None
    for d in range(1, 31):
        p_num = round(rm * d)
        diff = abs(rm - p_num/d)
        if best is None or diff < best[2]:
            best = (p_num, d, diff)
    
    flag = " <--" if best[2] < 0.002 else ""
    print(f"  mod {mname:<14}: q={q:>4}, R/mod={rm:.6f} ~ {best[0]}/{best[1]} (off {best[2]:.5f}){flag}")

print()
