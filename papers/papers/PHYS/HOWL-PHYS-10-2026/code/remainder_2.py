from mpmath import mp, mpf, pi, e, log, zeta, sqrt, phi, catalan
mp.dps = 30

# Our DERIVED alpha_inv from a_e (exact to ~12 digits from 4-loop)
a_derived = mpf('137.035998583231')
# CODATA recommended
a_codata = mpf('137.035999177')

basis = [
    ('pi',     pi),      ('2pi',    2*pi),
    ('pi^2',   pi**2),   ('pi^2/6', pi**2/6),
    ('e',      e),       ('ln2',    log(2)),
    ('sqrt2',  sqrt(2)), ('sqrt5',  sqrt(5)),
    ('phi',    phi),     ('zeta3',  zeta(3)),
    ('zeta5',  zeta(5)), ('Li4h',   mp.polylog(4,mpf(1)/2)),
    ('Catalan',catalan),
]

for label, alpha_inv in [('DERIVED (from a_e)', a_derived), ('CODATA', a_codata)]:
    print(f'alpha^-1 = {alpha_inv}  [{label}]')
    print(f"  {'mod':<10} {'q':>5} {'R':>16} {'R/mod':>12}")
    for name, val in basis:
        q = int(alpha_inv / val)
        r = alpha_inv - q * val
        rm = r / val
        line = f'  {name:<10} {q:>5} {float(r):>16.10f} {float(rm):>12.8f}'
        for d in range(1, 21):
            n = round(float(rm) * d)
            if abs(float(rm) - n/d) < 0.001 and n > 0:
                line += f'  ~{n}/{d}'
                break
        print(line)
    print()
    