from mpmath import mp, mpf, pi, zeta, log, sqrt, e as me, phi

mp.dps = 50

Q = 2**335

# Basis numerators from MATH-4 (copy-paste from the paper)
p_pi    = 219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314
p_e     = 190258044782769202588129925521314757831284456026137946619894798297742927086075833929023100244479638112
p_ln2   = 48514773537953331556699584584828624926234404478840896710102416707062925979128257345653169777835518667
p_sqrt2 = 98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506
p_phi   = 113249472467736168604496750010842101773570690275806888818880481552730738076053012711350611809151189412
p_pi2   = 690793580147337726804277647484346770338921354138994508002872352435529393755796399964695383625668575976
p_ln3   = 76894096788635086096158790585166115140009649181250777410832538562395270797691729322128736655820466233
p_ln5   = 112647815694871799155432631259623524245586803429977893615314774516410370135500048646041895614334987799
p_sqrt3 = 121229740294912895234576661752159696642961157181742464717663915473198765686797807393142352785809790154
p_sqrt5 = 156506921742415955629073428753920319855839958763030979672136303700342980177725995879548801953564656455
p_zeta2 = 115132263357889621134046274580724461723153559023165751333812058739254898959299399994115897270944762663
p_zeta3 = 84134394645319852071522700710261177454128732241134555234516209978359598548186272768450592529361881680
p_zeta5 = 72576671487518636549061590533542457287978428544763113598602740326685645428855657003519154452098433211

# alpha^-1 from our derivation: 137.035998583231
# Convert to 2^335 numerator: round(137.035998583231 * 2^335)
# But we should use the EXACT derived value. We derived it from a_e.
# Let's compute it properly from the mpf
alpha_inv_derived = mpf('137.035998583231')
p_alpha_inv = int(alpha_inv_derived * mpf(Q) + mpf('0.5'))

# Also CODATA
alpha_inv_codata = mpf('137.035999177')
p_alpha_inv_codata = int(alpha_inv_codata * mpf(Q) + mpf('0.5'))

print("alpha^-1 numerators over 2^335:")
print(f"  derived: {p_alpha_inv}")
print(f"  CODATA:  {p_alpha_inv_codata}")
print(f"  diff:    {p_alpha_inv_codata - p_alpha_inv}")
print()

# 114 * zeta(3) as integer arithmetic on numerators
p_114_zeta3 = 114 * p_zeta3
print(f"114 * p(zeta3) = {p_114_zeta3}")
print()

# Residual: p(alpha_inv) - 114 * p(zeta3), all over 2^335
residual_p_derived = p_alpha_inv - p_114_zeta3
residual_p_codata = p_alpha_inv_codata - p_114_zeta3

print(f"Residual numerator (derived): {residual_p_derived}")
print(f"Residual numerator (CODATA):  {residual_p_codata}")
print(f"Residual float (derived):     {float(mpf(residual_p_derived)/mpf(Q)):.15f}")
print(f"Residual float (CODATA):      {float(mpf(residual_p_codata)/mpf(Q)):.15f}")
print()

# Now: is this residual a simple combination of other basis numerators?
# residual_p ~ c1*p_pi + c2*p_ln2 + c3*p_zeta5 + c4*1 ?
# This is integer PSLQ on the numerators directly!

# Convert residual and basis to mpf for PSLQ
res_mpf = mpf(residual_p_codata) / mpf(Q)
print(f"residual = {res_mpf}")
print()

pool = [
    ("1",      mpf(1)),
    ("pi",     pi),
    ("ln2",    log(2)),
    ("zeta3",  zeta(3)),
    ("zeta5",  zeta(5)),
    ("e",      me),
    ("sqrt2",  sqrt(2)),
    ("pi^2",   pi**2),
    ("phi",    phi),
    ("ln3",    log(3)),
    ("sqrt3",  sqrt(3)),
]

print("PSLQ: residual (alpha^-1 - 114*zeta3) vs basis")
for maxc in [100, 1000, 10000]:
    vec = [res_mpf] + [v for _,v in pool]
    result = mp.pslq(vec, maxcoeff=maxc)
    if result:
        print(f"  maxcoeff={maxc}: HIT")
        expr = f"  {result[0]}*R"
        for i,(n,_) in enumerate(pool):
            if result[i+1] != 0:
                expr += f" + ({result[i+1]})*{n}"
        print(expr + " = 0")
        total = result[0]*res_mpf + sum(result[i+1]*pool[i][1] for i in range(len(pool)))
        print(f"  verify: {total}")
    else:
        print(f"  maxcoeff={maxc}: null")

print()

# Also try PSLQ on alpha_inv directly with zeta3 in pool
print("PSLQ: alpha^-1 directly (zeta3 in pool)")
a_mpf = mpf(p_alpha_inv_codata) / mpf(Q)
for maxc in [200, 1000, 10000]:
    vec = [a_mpf] + [v for _,v in pool]
    result = mp.pslq(vec, maxcoeff=maxc)
    if result:
        print(f"  maxcoeff={maxc}: HIT")
        expr = f"  {result[0]}*a_inv"
        for i,(n,_) in enumerate(pool):
            if result[i+1] != 0:
                expr += f" + ({result[i+1]})*{n}"
        print(expr + " = 0")
        total = result[0]*a_mpf + sum(result[i+1]*pool[i][1] for i in range(len(pool)))
        print(f"  verify: {total}")
    else:
        print(f"  maxcoeff={maxc}: null")

        