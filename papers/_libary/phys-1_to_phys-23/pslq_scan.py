import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from mpmath import mp, mpf, pi as mpi, zeta, log, polylog, sqrt as msqrt
from mpmath import phi as mphi, catalan, ellipk, ellipe, e as me

mp.dps = 200  # high precision for PSLQ

print("=" * 70)
print("PSLQ SCAN: MEASURED SM RATIOS vs 34-CONSTANT BASIS")
print("=" * 70)
print()

# ================================================================
# Build the 34-constant pool at 200 digits (mpmath, for PSLQ)
# ================================================================

pool = [
    ("1",         mpf(1)),
    ("pi",        mpi),
    ("pi^2",      mpi**2),
    ("pi^3",      mpi**3),
    ("pi^4",      mpi**4),
    ("e",         me),
    ("e^pi",      mp.exp(mpi)),
    ("ln2",       log(2)),
    ("ln3",       log(3)),
    ("ln5",       log(5)),
    ("ln7",       log(7)),
    ("ln10",      log(10)),
    ("ln2^2",     log(2)**2),
    ("ln2^4",     log(2)**4),
    ("sqrt2",     msqrt(2)),
    ("sqrt3",     msqrt(3)),
    ("sqrt5",     msqrt(5)),
    ("sqrt7",     msqrt(7)),
    ("phi",       mphi),
    ("zeta2",     zeta(2)),
    ("zeta3",     zeta(3)),
    ("zeta5",     zeta(5)),
    ("zeta7",     zeta(7)),
    ("zeta9",     zeta(9)),
    ("Li4h",      polylog(4, mpf(1)/2)),
    ("Li5h",      polylog(5, mpf(1)/2)),
    ("Li6h",      polylog(6, mpf(1)/2)),
    ("Li7h",      polylog(7, mpf(1)/2)),
    ("Catalan",   catalan),
    ("K_14",      ellipk(mpf(1)/4)),
    ("K_12",      ellipk(mpf(1)/2)),
    ("K_34",      ellipk(mpf(3)/4)),
    ("E_14",      ellipe(mpf(1)/4)),
    ("E_12",      ellipe(mpf(1)/2)),
    ("E_34",      ellipe(mpf(3)/4)),
]

print(f"Pool: {len(pool)} constants (including 1 for rational part)")
print()

# ================================================================
# Measured SM dimensionless quantities
# ================================================================

targets = [
    # Coupling constants
    ("alpha_EM_inv",     mpf('137.035999177')),
    ("alpha_EM_inv_MZ",  mpf('127.906')),
    ("alpha_s_MZ",       mpf('0.1180')),
    ("sin2_tW",          mpf('0.23122')),

    # Lepton mass ratios
    ("m_mu/m_e",         mpf('105.6583755') / mpf('0.51099895')),
    ("m_tau/m_e",        mpf('1776.86') / mpf('0.51099895')),
    ("m_tau/m_mu",       mpf('1776.86') / mpf('105.6583755')),

    # Quark mass ratios (MSbar 2 GeV)
    ("m_d/m_u",          mpf('4.67') / mpf('2.16')),
    ("m_s/m_d",          mpf('93.4') / mpf('4.67')),
    ("m_c/m_s",          mpf('1270') / mpf('93.4')),
    ("m_b/m_c",          mpf('4180') / mpf('1270')),
    ("m_t/m_b",          mpf('172690') / mpf('4180')),

    # CKM angles
    ("sin_theta12",      mpf('0.2253')),
    ("sin_theta23",      mpf('0.0412')),
    ("sin_theta13",      mpf('0.00350')),

    # Boson mass ratios
    ("M_W/M_Z",          mpf('80369') / mpf('91187.6')),
    ("M_H/M_Z",          mpf('125100') / mpf('91187.6')),
    ("M_H/M_W",          mpf('125100') / mpf('80369')),

    # Koide-related
    ("Koide_ratio_lep",  mpf('0.666661')),

    # Derived
    ("G_F_v2",           mpf('246220')),  # v in MeV (= 1/sqrt(sqrt(2)*G_F))
]

print(f"Targets: {len(targets)} measured quantities")
print()

# ================================================================
# PSLQ scan function
# ================================================================

def run_pslq(target_name, target_val, candidates, maxcoeff=1000):
    """Run PSLQ: find integers c_i such that c_0*target + c_1*x_1 + ... = 0."""
    names = [n for n, v in candidates]
    vals = [v for n, v in candidates]
    vec = [target_val] + vals

    result = mp.pslq(vec, maxcoeff=maxcoeff)

    if result is None:
        return None

    # Interpret: result[0]*target + sum(result[i+1]*x_i) = 0
    # target = -sum(result[i+1]*x_i) / result[0]
    if result[0] == 0:
        return None

    # Build expression
    terms = []
    for i, (name, val) in enumerate(candidates):
        if result[i+1] != 0:
            terms.append((result[i+1], name))

    return result, terms

# ================================================================
# Run progressive PSLQ on each target
# ================================================================

# Stage 1: Small pool (1, pi, e, ln2, sqrt2, sqrt3, phi, zeta3)
small_pool = [c for c in pool if c[0] in [
    "1", "pi", "pi^2", "e", "ln2", "sqrt2", "sqrt3", "phi", "zeta3"
]]

# Stage 2: Medium pool (add zeta5, Li4, pi^3, pi^4, ln3, ln5, sqrt5, sqrt7)
medium_pool = [c for c in pool if c[0] in [
    "1", "pi", "pi^2", "pi^3", "pi^4", "e", "ln2", "ln3", "ln5",
    "ln2^2", "sqrt2", "sqrt3", "sqrt5", "sqrt7", "phi",
    "zeta2", "zeta3", "zeta5", "Li4h", "Catalan"
]]

# Stage 3: Full pool
full_pool = pool

print("=" * 70)
print("STAGE 1: SMALL POOL (9 constants), maxcoeff=1000")
print("=" * 70)
print()

for name, val in targets:
    result = run_pslq(name, val, small_pool, maxcoeff=1000)
    if result is not None:
        coeffs, terms = result
        print(f"  ** {name}: RELATION FOUND **")
        print(f"     {coeffs[0]}*{name} + ", end="")
        print(" + ".join(f"{c}*{n}" for c, n in terms))
        # Verify
        check = sum(coeffs[i+1] * pool_val for i, (_, pool_val) in enumerate(small_pool))
        check += coeffs[0] * val
        print(f"     residual: {mp.nstr(check, 10)}")
    else:
        print(f"  {name}: null")

print()

print("=" * 70)
print("STAGE 2: MEDIUM POOL (20 constants), maxcoeff=1000")
print("=" * 70)
print()

for name, val in targets:
    result = run_pslq(name, val, medium_pool, maxcoeff=1000)
    if result is not None:
        coeffs, terms = result
        print(f"  ** {name}: RELATION FOUND **")
        print(f"     {coeffs[0]}*{name} + ", end="")
        print(" + ".join(f"{c}*{n}" for c, n in terms))
    else:
        print(f"  {name}: null")

print()

print("=" * 70)
print("STAGE 3: FULL POOL (35 constants), maxcoeff=10000")
print("=" * 70)
print()

for name, val in targets:
    result = run_pslq(name, val, full_pool, maxcoeff=10000)
    if result is not None:
        coeffs, terms = result
        print(f"  ** {name}: RELATION FOUND **")
        print(f"     {coeffs[0]}*{name} + ", end="")
        print(" + ".join(f"{c}*{n}" for c, n in terms))
        # Verify: compute target from the relation
        if coeffs[0] != 0:
            predicted = -sum(c * v for (c, n), (_, v) in zip(terms, 
                [(n,v) for n,v in full_pool if n in [t[1] for t in terms]])) 
            # simpler verification
            total = sum(coeffs[i] * ([val] + [v for _,v in full_pool])[i] for i in range(len(coeffs)))
            print(f"     verify: sum = {mp.nstr(total, 20)}")
    else:
        print(f"  {name}: null")

print()

print("=" * 70)
print("SUMMARY")
print("=" * 70)
