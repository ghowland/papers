#!/usr/bin/env python3
"""
HOWL: A₂ Coefficient Decomposition in R₂/R₄ Form
===================================================

Decompose the QED 2-loop coefficient A₂ into three pieces:
  1. Rational: 197/144 (diagram combinatorics)
  2. Number-theoretic: (3/4)ζ(3) (Feynman parameter integrals)
  3. Geometric: R₄ × (8/3 − 16ln2) (4D phase space)

All computation in Fraction arithmetic using DATA-3 Q335 numerators.
"""

from fractions import Fraction
from mpmath import mp, mpf, pi as mpi, zeta as mzeta, log as mlog

mp.dps = 100

def f2m(f):
    return mpf(f.numerator) / mpf(f.denominator)

# ================================================================
# Q335 BASIS FROM DATA-3
# ================================================================

Q = 2**335

p_pi2   = 690793580147337726804277647484346770338921354138994508002872352435529393755796399964695383625668575976
p_zeta3 = 84134394645319852071522700710261177454128732241134555234516209978359598548186272768450592529361881680
p_ln2   = 48514773537953331556699584584828624926234404478840896710102416707062925979128257345653169777835518667
p_pi    = 219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314
p_sqrt2 = 98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506

pi2_frac   = Fraction(p_pi2, Q)
zeta3_frac = Fraction(p_zeta3, Q)
ln2_frac   = Fraction(p_ln2, Q)
pi_frac    = Fraction(p_pi, Q)

# Verify Q335 numerators against mpmath
mp.dps = 40
checks_ok = True
for name, frac, ref in [("pi^2", pi2_frac, mpi**2),
                         ("zeta(3)", zeta3_frac, mzeta(3)),
                         ("ln(2)", ln2_frac, mlog(2))]:
    val = f2m(frac)
    s1, s2 = mp.nstr(val, 30), mp.nstr(ref, 30)
    if s1 != s2:
        print(f"  WARNING: {name} Q335 mismatch at 30 digits")
        checks_ok = False

mp.dps = 100

print("=" * 72)
print("HOWL: A₂ COEFFICIENT DECOMPOSITION IN R₂/R₄ FORM")
print("=" * 72)
print()

if checks_ok:
    print("  Q335 basis verification: all 30-digit matches OK")
else:
    print("  Q335 basis verification: MISMATCH detected")
print()

# ================================================================
# STEP 1: COMPUTE A₂ IN ORIGINAL FORM (Fraction arithmetic)
# ================================================================

print("STEP 1: A₂ IN ORIGINAL FORM")
print("-" * 72)
print()
print("  A₂ = 197/144 + π²/12 + (3/4)ζ(3) − (π²/2)ln(2)")
print()

# Each term as exact Fraction (over Q or Q² as needed)
term_rational = Fraction(197, 144)
term_pi2_12   = pi2_frac / 12
term_zeta3    = Fraction(3, 4) * zeta3_frac
term_pi2_ln2  = pi2_frac * ln2_frac / 2  # this has denominator Q²

A2_frac = term_rational + term_pi2_12 + term_zeta3 - term_pi2_ln2

# Convert to float for display
A2_float = float(f2m(A2_frac))

# Reference value from mpmath
mp.dps = 50
A2_ref = mpf(197)/144 + mpi**2/12 + mpf(3)/4*mzeta(3) - mpi**2/2*mlog(2)
A2_ref_float = float(A2_ref)

print(f"  Term by term:")
print(f"    197/144          = {float(term_rational):+.10f}")
print(f"    π²/12            = {float(f2m(term_pi2_12)):+.10f}")
print(f"    (3/4)ζ(3)        = {float(f2m(term_zeta3)):+.10f}")
print(f"    −(π²/2)ln(2)     = {-float(f2m(term_pi2_ln2)):+.10f}")
print(f"    ─────────────────────────────────────")
print(f"    A₂ (Fraction)    = {A2_float:+.10f}")
print(f"    A₂ (mpmath ref)  = {A2_ref_float:+.10f}")
print()

diff_A2 = abs(A2_float - A2_ref_float)
if diff_A2 < 1e-10:
    print(f"  Fraction vs mpmath: agree to {-mp.nstr(mlog(diff_A2)/mlog(10),4) if diff_A2 > 0 else 'exact'} digits")
    print(f"  PASS")
else:
    print(f"  Fraction vs mpmath: diff = {diff_A2:.2e}")
    print(f"  CHECK — possible precision issue")
print()

# ================================================================
# STEP 2: DECOMPOSITION INTO R₄ FORM
# ================================================================

print("STEP 2: DECOMPOSITION INTO R₄ FORM")
print("-" * 72)
print()
print("  Substitution: π² = 32R₄  where R₄ = π²/32 (MATH-5 4-ball remainder)")
print()
print("  π²/12        = 32R₄/12      = (8/3)R₄")
print("  (π²/2)ln(2)  = (32/2)R₄ln(2) = 16R₄ln(2)")
print()
print("  A₂ = 197/144 + (3/4)ζ(3) + R₄(8/3 − 16ln(2))")
print()
print("  Three pieces:")
print("    RATIONAL:        197/144")
print("    NUMBER-THEORETIC: (3/4)ζ(3)")
print("    GEOMETRIC:       R₄ × (8/3 − 16ln(2))")
print()

# Compute the geometric coefficient: c_geom = 8/3 - 16*ln(2)
c_geom_frac = Fraction(8, 3) - 16 * ln2_frac
c_geom_float = float(f2m(c_geom_frac))

# R₄ in Fraction
R4_frac = pi2_frac / 32

# The three pieces
piece_rational = Fraction(197, 144)
piece_number   = Fraction(3, 4) * zeta3_frac
piece_geom     = R4_frac * c_geom_frac

# Verify sum
A2_decomp = piece_rational + piece_number + piece_geom
A2_decomp_float = float(f2m(A2_decomp))

print(f"  Geometric coefficient:")
print(f"    c_geom = 8/3 − 16ln(2)")
print(f"    8/3      = {8/3:+.10f}")
print(f"    16ln(2)  = {16*float(f2m(ln2_frac)):+.10f}")
print(f"    c_geom   = {c_geom_float:+.10f}")
print()
print(f"  R₄ = π²/32 = {float(f2m(R4_frac)):.10f}")
print()
print(f"  Three pieces:")
print(f"    Rational:         197/144              = {float(piece_rational):+.10f}")
print(f"    Number-theoretic: (3/4)ζ(3)           = {float(f2m(piece_number)):+.10f}")
print(f"    Geometric:        R₄×(8/3−16ln2)      = {float(f2m(piece_geom)):+.10f}")
print(f"    ──────────────────────────────────────────────")
print(f"    Sum                                    = {A2_decomp_float:+.10f}")
print(f"    A₂ from Step 1                         = {A2_float:+.10f}")
print()

decomp_diff = abs(A2_decomp_float - A2_float)
if decomp_diff < 1e-15:
    print(f"  Decomposition consistency: EXACT (diff = {decomp_diff:.2e})")
else:
    print(f"  Decomposition consistency: diff = {decomp_diff:.2e}")
print()

# ================================================================
# STEP 3: ANATOMY TABLE
# ================================================================

print("STEP 3: ANATOMY OF A₂")
print("-" * 72)
print()

abs_A2 = abs(A2_float)
val_rat = float(piece_rational)
val_num = float(f2m(piece_number))
val_geo = float(f2m(piece_geom))

print(f"  {'Piece':<22} {'Expression':<24} {'Value':>12} {'|Frac| of |A₂|':>16} {'Sign':>6}")
print(f"  {'-'*22} {'-'*24} {'-'*12} {'-'*16} {'-'*6}")
print(f"  {'Rational':<22} {'197/144':<24} {val_rat:>+12.6f} {abs(val_rat)/abs_A2*100:>15.1f}% {'  +':>6}")
print(f"  {'Number-theoretic':<22} {'(3/4)ζ(3)':<24} {val_num:>+12.6f} {abs(val_num)/abs_A2*100:>15.1f}% {'  +':>6}")
print(f"  {'Geometric':<22} {'R₄×(8/3−16ln2)':<24} {val_geo:>+12.6f} {abs(val_geo)/abs_A2*100:>15.1f}% {'  −':>6}")
print(f"  {'-'*22} {'-'*24} {'-'*12} {'-'*16}")
print(f"  {'TOTAL A₂':<22} {'':<24} {A2_float:>+12.6f}")
print()

print(f"  The geometric piece dominates ({abs(val_geo)/abs_A2*100:.0f}% of |A₂|) with OPPOSITE sign.")
print(f"  A₂ is small (−0.328) because of a large cancellation:")
print(f"    Positive: rational + number-theoretic = {val_rat + val_num:+.6f}")
print(f"    Negative: geometric                   = {val_geo:+.6f}")
print(f"    Net:      {val_rat + val_num + val_geo:+.6f}")
print(f"    Cancellation: {abs(val_rat + val_num)/abs(val_geo)*100:.1f}% of geometric piece cancelled")
print()

# ================================================================
# STEP 4: PHYSICAL ORIGIN
# ================================================================

print("STEP 4: PHYSICAL ORIGIN OF EACH PIECE")
print("-" * 72)
print()
print(f"  {'Piece':<22} {'Origin':<50}")
print(f"  {'-'*22} {'-'*50}")
print(f"  {'197/144':<22} {'Algebraic reduction of 7 two-loop diagrams':<50}")
print(f"  {'':<22} {'197 is prime. 144 = 2⁴×3² = 12².':<50}")
print(f"  {'':<22} {'No transcendental content — pure counting.':<50}")
print()
print(f"  {'(3/4)ζ(3)':<22} {'Feynman parameter integral over polylogarithms':<50}")
print(f"  {'':<22} {'Li₃(1) = ζ(3) at integration boundary x=1.':<50}")
print(f"  {'':<22} {'Coefficient 3/4 is rational from diagram topology.':<50}")
print()
print(f"  {'R₄×(8/3)':<22} {'4D momentum phase space integral':<50}")
print(f"  {'':<22} {'∫d⁴k → π² = 32R₄ from solid angle in 4D.':<50}")
print(f"  {'':<22} {'The 8/3 comes from angular integration limits.':<50}")
print()
print(f"  {'R₄×(−16ln2)':<22} {'Infrared mass singularity regulation':<50}")
print(f"  {'':<22} {'Electron mass regulates IR → ln(m²/μ²) → ln(2).':<50}")
print(f"  {'':<22} {'16 = 2⁴ from diagram topology.':<50}")
print()

# ================================================================
# STEP 5: THE CANCELLATION STRUCTURE
# ================================================================

print("STEP 5: THE CANCELLATION STRUCTURE")
print("-" * 72)
print()
print("  A₂ = +1.368 + 0.902 − 2.598 = −0.328")
print()
print("  The positive pieces (+2.270) are 87% of the geometric piece (2.598).")
print("  The net A₂ is only 13% of either side of the cancellation.")
print()
print("  This means: the 2-loop QED correction to (g−2) is accidentally small.")
print("  It's small not because the physics is small, but because geometry")
print("  (4D phase space) nearly cancels the combinatorics (diagram counting)")
print("  and number theory (polylogarithm integrals).")
print()
print("  In the HOWL language: R₄ (Level 1 geometric structure) nearly")
print("  cancels the Level 2 content (rational + number-theoretic).")
print("  The remaining −0.328 is the net effect after cancellation.")
print()

# ================================================================
# STEP 6: CONNECTION TO BROWN-SCHNETZ PROGRAM
# ================================================================

print("STEP 6: CONNECTION TO AMPLITUDES LITERATURE")
print("-" * 72)
print()
print("  The decomposition A₂ = rational + ζ(3) term + R₄ term is a")
print("  specific instance of the general separation studied by Brown,")
print("  Schnetz, and Panzer in their work on the Galois coaction of")
print("  multiple zeta values in perturbative QFT.")
print()
print("  Their framework: Feynman integrals decompose into 'periods'")
print("  (geometric integrals over moduli spaces) and 'coefficients'")
print("  (arithmetic data from the motivic structure). The Galois")
print("  coaction separates these systematically.")
print()
print("  The HOWL decomposition maps onto this as:")
print("    R₄ content  ←→  period (geometric, from spacetime dimension)")
print("    ζ(3) content ←→  arithmetic (from polylogarithm depth)")
print("    197/144      ←→  rational coefficient (diagram combinatorics)")
print()
print("  At 3-loop (A₃), the decomposition becomes richer:")
print("    R₄ appears with new coefficients")
print("    R₄² = (π²/32)² appears (products of periods)")
print("    ζ(5) appears (deeper polylogarithm)")
print("    Li₄(1/2) appears (polylogarithm at non-trivial argument)")
print("    Products like R₄×ζ(3) appear (period × arithmetic)")
print()
print("  The geometric and arithmetic content multiply but remain")
print("  separable — they sit in different factors of each term.")
print("  The R₂/R₄ language makes the geometric factor explicit")
print("  in every term, connecting HOWL to this program.")
print()

# ================================================================
# STEP 7: EXTENSION PREVIEW — A₃ STRUCTURE
# ================================================================

print("STEP 7: A₃ STRUCTURE (preview, not computed)")
print("-" * 72)
print()
print("  A₃ = 1.181241... (72 diagrams, Laporta-Remiddi 1996)")
print()
print("  Known analytic terms include:")
print("    Rational parts")
print("    ζ(3) terms         (same class as A₂)")
print("    ζ(5) terms         (NEW: weight-5 zeta value)")
print("    π²ζ(3) terms      (NEW: product of period × arithmetic)")
print("    π⁴ terms           (= 1024 R₄² — geometric at higher order)")
print("    π²ln(2) terms     (same class as A₂ geometric piece)")
print("    Li₄(1/2) terms    (NEW: polylogarithm at x=1/2)")
print("    ln⁴(2) terms      (NEW: fourth power of ln2)")
print()
print("  Every π² → 32R₄, every π⁴ → 1024R₄².")
print("  The geometric content proliferates but remains separable.")
print()
print("  A₃ decomposition would require the full Laporta-Remiddi")
print("  analytic result with all coefficients. This is known but")
print("  lengthy. The A₂ decomposition demonstrates the method.")
print()

# ================================================================
# STEP 8: KEY NUMBERS FOR DATA-3 EXTENSION
# ================================================================

print("STEP 8: KEY NUMBERS")
print("-" * 72)
print()
print(f"  A₂ = {A2_float:+.15f}")
print(f"    = 197/144 + (3/4)ζ(3) + R₄×(8/3 − 16ln2)")
print()
print(f"  Piece values (Fraction arithmetic, Q335 basis):")
print(f"    Rational:         {float(piece_rational):+.15f}")
print(f"    Number-theoretic: {float(f2m(piece_number)):+.15f}")
print(f"    Geometric:        {float(f2m(piece_geom)):+.15f}")
print()
print(f"  Geometric coefficient:")
print(f"    c_geom = 8/3 − 16ln(2) = {c_geom_float:+.15f}")
print()
print(f"  R₄ = π²/32 = {float(f2m(R4_frac)):.15f}")
print()
print(f"  Cancellation ratio: positive/|geometric| = {(val_rat+val_num)/abs(val_geo)*100:.2f}%")
print(f"  Net/|geometric| = {abs(A2_float)/abs(val_geo)*100:.2f}%")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 72)
print("CHECKS")
print("=" * 72)
print()

checks = []
def chk(name, cond, detail=""):
    s = "PASS" if cond else "FAIL"
    checks.append((name, s))
    print(f"  [{s}] {name}")
    if detail: print(f"        {detail}")

chk("Q335 basis verified at 30 digits", checks_ok)

chk("A₂ Fraction matches mpmath to 10 digits",
    abs(A2_float - A2_ref_float) < 1e-10,
    f"diff = {abs(A2_float - A2_ref_float):.2e}")

chk("Decomposition sums to A₂",
    decomp_diff < 1e-15,
    f"diff = {decomp_diff:.2e}")

chk("A₂ is negative",
    A2_float < 0,
    f"A₂ = {A2_float:+.10f}")

chk("Geometric piece is negative",
    val_geo < 0,
    f"geometric = {val_geo:+.6f}")

chk("Rational + number-theoretic is positive",
    val_rat + val_num > 0,
    f"sum = {val_rat + val_num:+.6f}")

chk("Geometric piece dominates (>70% of |A₂|)",
    abs(val_geo) / abs_A2 > 0.70,
    f"{abs(val_geo)/abs_A2*100:.1f}%")

chk("|A₂| < 0.5 (small due to cancellation)",
    abs(A2_float) < 0.5,
    f"|A₂| = {abs(A2_float):.6f}")

chk("A₂ ≈ −0.3285 (known value)",
    abs(A2_float - (-0.32848)) < 0.001,
    f"A₂ = {A2_float:.6f}")

print()
n_pass = sum(1 for _, s in checks if s == "PASS")
n_fail = sum(1 for _, s in checks if s == "FAIL")
print(f"  TOTAL: {n_pass} PASS, {n_fail} FAIL out of {len(checks)}")
print()

print("=" * 72)
print("A₂ DECOMPOSITION COMPLETE")
print("=" * 72)
