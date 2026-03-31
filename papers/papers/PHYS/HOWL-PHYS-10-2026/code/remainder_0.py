from mpmath import mp, mpf, pi, e, log, zeta, sqrt, phi
from mpmath import catalan, ellipk, ellipe

mp.dps = 30

alpha_inv = mpf('137.035999177')

pool = [
    ("pi",      pi),
    ("2pi",     2*pi),
    ("pi^2",    pi**2),
    ("e",       e),
    ("e^pi",    mp.exp(pi)),
    ("ln2",     log(2)),
    ("sqrt2",   sqrt(2)),
    ("sqrt3",   sqrt(3)),
    ("phi",     phi),
    ("zeta3",   zeta(3)),
    ("zeta5",   zeta(5)),
    ("pi*e",    pi*e),
    ("pi^2/6",  pi**2/6),
    ("4*pi",    4*pi),
    ("pi/2",    pi/2),
    ("2*pi^2",  2*pi**2),
    ("137",     mpf(137)),
]

print("=" * 70)
print("alpha^-1 mod (basis constants)")
print("=" * 70)
print()
print(f"  alpha^-1 = {alpha_inv}")
print()
print(f"  {'Modulus':<12} {'Quotient':>10} {'Remainder':>15} {'R/mod':>10}")
print(f"  {'-'*12} {'-'*10} {'-'*15} {'-'*10}")

for name, val in pool:
    q = int(alpha_inv / val)
    r = float(alpha_inv - q * val)
    r_frac = r / float(val)
    print(f"  {name:<12} {q:>10} {r:>15.8f} {r_frac:>10.6f}")

print()

# Also check: is alpha_inv close to a simple rational times a basis constant?
# alpha_inv / constant ~ p/q for small p, q?
print("=" * 70)
print("alpha^-1 / (basis constant) — near simple rationals?")
print("=" * 70)
print()

for name, val in pool[:12]:
    ratio = float(alpha_inv / val)
    # Check nearby rationals p/q with q <= 20
    best = None
    for q in range(1, 21):
        p = round(ratio * q)
        diff = abs(ratio - p/q)
        if best is None or diff < best[2]:
            best = (p, q, diff)
    p, q, diff = best
    pct = diff / ratio * 100
    print(f"  alpha^-1/{name:<8} = {ratio:.8f} ~ {p}/{q} = {p/q:.8f} ({pct:.4f}%)")

print()

# Now do the same for other measured constants
print("=" * 70)
print("OTHER SM CONSTANTS mod pi")
print("=" * 70)
print()

targets = [
    ("alpha_inv",       137.035999177),
    ("m_mu/m_e",        206.7682830),
    ("m_tau/m_e",       3477.1507),
    ("m_tau/m_mu",      16.8170),
    ("sin2_tW",         0.23122),
    ("alpha_s",         0.1180),
    ("M_W/M_Z",         0.88147),
    ("M_H/M_Z",         1.37193),
]

for name, val in targets:
    val = mpf(val)
    for mod_name, mod_val in [("pi", pi), ("2pi", 2*pi), ("e", e)]:
        q = int(val / mod_val)
        r = float(val - q * mod_val)
        if mod_val > val:
            q = 0
            r = float(val)
        r_frac = r / float(mod_val) if float(mod_val) > 0 else 0
        # Is r_frac close to a simple fraction?
        best_rf = None
        for denom in range(1, 13):
            numer = round(r_frac * denom)
            diff_rf = abs(r_frac - numer/denom)
            if best_rf is None or diff_rf < best_rf[2]:
                best_rf = (numer, denom, diff_rf)
        n, d, diff_rf = best_rf
        close = " <-- CLOSE" if diff_rf < 0.01 else ""
        print(f"  {name:<14} mod {mod_name:<4}: q={q:>4}, R/mod={r_frac:.6f} ~ {n}/{d} (off {diff_rf:.4f}){close}")
    print()
    