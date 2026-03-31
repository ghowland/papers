Phase 4: Parameter reduction. The synthesis tells us where to look.

**Strategy A (from DISC-6):** Nonlinear PSLQ — test log(X), X², 1/X, √X against the basis. Never done.

**Strategy B (from DISC-6):** Modular search with the synthesis-informed moduli. The synthesis says: Subgroup A parameters should be tested mod 8R₂, Subgroup C parameters mod 1 with R₄ normalization.

Let me start with Strategy A since it's the identified gap — the one search we said we'd do but haven't.

```python
from mpmath import mp, mpf, pi, zeta, log, sqrt, e as me, phi
from mpmath import catalan, ellipk, ellipe

mp.dps = 50

print("=" * 70)
print("PHASE 4: PARAMETER REDUCTION")
print("Strategy A: Nonlinear PSLQ")
print("=" * 70)
print()
print("The PSLQ null tested: is X a linear combination of basis constants?")
print("Strategy A tests: is f(X) a linear combination, where f is")
print("log, square, reciprocal, square root, or cube root?")
print()

# The basis pool (same as PSLQ scan)
pool = [
    ("1",      mpf(1)),
    ("pi",     pi),
    ("pi^2",   pi**2),
    ("e",      me),
    ("ln2",    log(2)),
    ("sqrt2",  sqrt(2)),
    ("sqrt3",  sqrt(3)),
    ("phi",    phi),
    ("zeta3",  zeta(3)),
    ("zeta5",  zeta(5)),
]
pnames = [n for n,_ in pool]

# High-precision targets (only use targets known to enough digits)
targets = [
    ("alpha_inv",    mpf('137.035999177')),
    ("sin2_tW",      mpf('0.23122')),
    ("alpha_s",      mpf('0.1180')),
    ("m_mu/m_e",     mpf('206.7682830')),
    ("m_tau/m_mu",   mpf('16.8170')),
    ("M_W/M_Z",      mpf('0.88147')),
    ("M_H/M_Z",      mpf('1.37193')),
    ("M_H/M_W",      mpf('1.55670')),
]

# Transforms to apply
transforms = [
    ("X",        lambda x: x),
    ("ln(X)",    lambda x: log(x) if x > 0 else None),
    ("X^2",      lambda x: x**2),
    ("1/X",      lambda x: 1/x if x != 0 else None),
    ("sqrt(X)",  lambda x: sqrt(x) if x > 0 else None),
    ("X^(1/3)",  lambda x: x**(mpf(1)/3) if x > 0 else None),
    ("X*pi",     lambda x: x * pi),
    ("X/pi",     lambda x: x / pi),
    ("X*2pi",    lambda x: x * 2 * pi),
    ("X/(2pi)",  lambda x: x / (2*pi)),
]

print(f"Targets: {len(targets)}")
print(f"Transforms: {len(transforms)}")
print(f"Pool: {len(pool)} constants")
print(f"Total tests: {len(targets) * len(transforms)} at maxcoeff=1000")
print()

hits = []
nulls = 0

for tname, tval in targets:
    for fname, func in transforms:
        fval = func(tval)
        if fval is None or fval == 0:
            continue
        
        vec = [fval] + [v for _, v in pool]
        result = mp.pslq(vec, maxcoeff=1000)
        
        if result is not None and result[0] != 0:
            # Found something — interpret
            terms = []
            for i, (pn, _) in enumerate(pool):
                if result[i+1] != 0:
                    terms.append(f"({result[i+1]})*{pn}")
            expr = " + ".join(terms)
            
            # Verify
            total = sum(result[i] * ([fval] + [v for _,v in pool])[i] for i in range(len(result)))
            
            print(f"  ** HIT: {fname}({tname})")
            print(f"     {result[0]}*{fname}({tname}) + {expr} = 0")
            print(f"     verify: {mp.nstr(total, 10)}")
            
            # Check if this is trivial (e.g., ln(X) finding X = e^something)
            hits.append((tname, fname, result, total))
        else:
            nulls += 1

print()
print(f"Results: {len(hits)} hits, {nulls} nulls")
print()

if not hits:
    print("ALL NULL. No nonlinear transcendental relation found")
    print("for any SM parameter under any transform tested.")
    print()
    print("This extends the PSLQ null from linear to nonlinear:")
    print("  Linear (PHYS-10): 17 targets × 35 pool × maxcoeff 10000 → null")
    print("  Nonlinear (this):  8 targets × 10 transforms × 10 pool × maxcoeff 1000 → null")
    print()
    print("The SM parameters are not simple nonlinear functions")
    print("of the transcendental basis either.")
else:
    print("HITS FOUND — need careful analysis:")
    for tname, fname, result, total in hits:
        print(f"  {fname}({tname}): coefficients {result}")
        print(f"    residual: {mp.nstr(total, 10)}")
```80/80 null. No nonlinear relation either. Now Strategy B — modular search informed by the Phase 3 synthesis. The synthesis says: Subgroup A parameters should be tested mod 8R₂, and the CKM phase δ_CP is a literal phase that might live on the 8R₂ domain.

```python
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
```42 hits, but let me assess them honestly.

**The critical question:** With 11 targets × 18 moduli × checking denominators up to 20, that's roughly 3960 total p/d combinations tested. At 0.05% threshold (0.0005), the expected false positive rate is ~0.1% per test = ~4 hits expected by chance. We got 42. That's elevated — about 10× the random expectation.

**But:** Many hits are duplicates (sin²θ_W mod R₄ shows 3/4 = 6/8 = 9/12 = 12/16 = 15/20 — that's one hit counted five times). Let me count unique hits:

**Genuinely interesting:**

| Target | Modulus | Remainder | Quality |
|---|---|---|---|
| α⁻¹ | R₂·e | q=64, R/mod ≈ 3/16 | 0.00002 off |
| α_s | R₂·ζ(3) | q=0, R/mod ≈ 1/8 | 0.00001 off |
| m_μ/m_e | π² | q=20, R/mod ≈ 19/20 | 0.00001 off |
| m_μ/m_e | R₂·e | q=96, R/mod ≈ 17/20 | 0.00001 off |
| sin²θ_W | R₄ | q=0, R/mod ≈ 3/4 | 0.00032 off |

The **α_s ≈ R₂·ζ(3)/8** hit is very clean (off by 0.00001):

α_s ≈ R₂·ζ(3)/8 = (π/4)·ζ(3)/8 = πζ(3)/32

Let me check: πζ(3)/32 = 3.14159 × 1.20206 / 32 = 3.77611/32 = 0.11800. Measured: 0.1180. That's... suspiciously good.

And **sin²θ_W ≈ (3/4)R₄ = (3/4)(π²/32) = 3π²/128 = 0.23087**. Measured: 0.23122. Off by 0.15%.

But these need the same statistical caution. With 3960 tests at 0.05% threshold, finding 2-3 hits at 0.001% quality is expected about once. The α_s hit is the best quality. Let me run PSLQ specifically on α_s = πζ(3)/32:Here's the honest assessment:

**α_s ≈ πζ(3)/32:** Match to 0.01%. The difference 0.0000117 is WELL within the measurement uncertainty of ±0.0009. But α_s is only known to 0.76% precision — any formula that gives 0.118-ish will be "within uncertainty." The formula πζ(3)/32 = 0.11801 can't be distinguished from coincidence at the current experimental precision. We'd need α_s measured to 0.01% (5× better than current) to test it.

**sin²θ_W ≈ 3π²/128:** Match to 0.04%. The difference 0.0000989 is OUTSIDE the measurement uncertainty of ±0.00003 by a factor of 3. This is ruled out as an exact relation. sin²θ_W ≠ 3π²/128.

**α⁻¹ ≈ (1027/16)·R₂·e:** Match to 0.000035%. Impressive numerically but 1027/16 is not a structurally motivated number. And α⁻¹ from CODATA has uncertainty ±0.000000021, which is ±0.015 ppb. Our difference is 0.00005, which is ~350 ppb — far outside CODATA uncertainty. Ruled out.

**Phase 4 summary so far:**

| Strategy | Tests | Hits | Significant? |
|---|---|---|---|
| A: Nonlinear PSLQ | 80 | 0 | Solid null |
| B: Modular search | ~3960 | 42 (raw), ~15 unique | Most are statistical noise |

**The one interesting candidate:** α_s = πζ(3)/32. It matches within current experimental uncertainty but cannot be tested further without better α_s measurements. It's a CANDIDATE, not a finding. The formula has structural content: π and ζ(3) are both basis constants, 32 = 2⁵ is a pure power of 2, and the combination πζ(3)/32 = R₂·ζ(3)/8 uses the Subgroup A geometric constant R₂ times the Subgroup A transcendental ζ(3) divided by 8. But without a derivation or a sharper experimental test, it cannot be promoted to a result.

**Everything else is either outside measurement uncertainty (ruled out) or within uncertainty but untestable at current precision.**

Do you want me to pursue the α_s candidate further (look for a derivation pathway), or report the Phase 4 null and write DISC-7?

