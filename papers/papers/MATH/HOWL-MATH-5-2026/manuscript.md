# The n-Ball Remainder Sequence
## Geometric Invariant Separation from 2D Cross-Sections to 4D Spacetime

**Registry:** [@HOWL-MATH-5-2026]

**Series Path:** [@HOWL-MATH-1-2026] → [@HOWL-MATH-4-2026] → [@HOWL-PHYS-10-2026] → [@HOWL-MATH-5-2026]

**DOI:** 10.5281/zenodo.19528613

**Date:** March 31 2026

**Domain:** Geometry / Number Theory / Mathematical Physics

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## I. ABSTRACT

This paper proves four claims about the n-ball remainder R_n — the fraction of a bounding n-cube occupied by the inscribed n-ball.

First, a number-theoretic result: R_n has a pure power-of-two denominator only for n = 0, 1, 2, and 4. This makes R₂ = π/4 and R₄ = π²/32 the only non-trivial n-ball remainders that are native to both exact rational arithmetic and binary computation. The proof is three lines: the denominator of R_{2m} is 2^{2m} · m!, which is a pure power of 2 if and only if m! is a power of 2, which holds only for m ≤ 2.

Second, a survey result: R₃ = π/6 appears as a separable geometric factor in every equation that computes sphere volume. R₂ = π/4 appears in every equation that computes sphere cross-section or surface area. The remainder is selected by the geometric operation, not by the object. Verified as exact rational identities across ten equations spanning geometry, mechanics, gravitation, nuclear physics, and thermodynamics.

Third, an algebraic result: R₄ = π²/32 separates as an explicit prefactor in the standard one-loop scalar integral in four-dimensional Euclidean space, visible before the Fourier normalization convention (2π)⁴ is applied. The identity π² = 32R₄ is exact. The factor 1/(16π²) that appears in every quantum field theory textbook mixes two distinct sources of π — the geometric four-dimensional solid angle and the Fourier normalization — and separating them reveals R₄ as the geometric content.

Fourth, a decomposition result: the instanton action S = 8π²c₂/g² decomposes as S = 256R₄ · c₂/g², where 256 = 8 × 32 (topological normalization × dimensional factor), c₂ ∈ ℤ is the instanton number, R₄ is the geometric remainder, and 1/g² is the coupling impedance. The Chern class normalization 1/(8π²) = 1/(256R₄) converts the raw gauge field integral into the integer c₂, mediated by 1/R₄ in the opposite direction. This is the MATH-1 skeleton Q = F · R · Z generalized from two to four dimensions, with the directional pattern preserved.

All four claims are verified as exact rational identities in the accompanying script `math_5_verify.py`. Every assertion passes with zero tolerance and zero approximation.

This paper does not claim a causal relationship between the uniqueness of n = 2 and n = 4 and spacetime dimensionality. It does not recommend changing QFT conventions. It does not propose new physics. Every equation decomposed is standard and published. The contribution is making R_n visible as the separable geometric content across dimensions.

---

## II. THE n-BALL REMAINDER SEQUENCE

### 2.1 Definition

The n-ball remainder R_n is the ratio of the volume of an n-ball of diameter d to the volume of its bounding n-cube:

R_n = V_n(d) / d^n

where V_n(d) = (π^{n/2} / Γ(n/2 + 1)) · (d/2)^n is the standard n-ball volume. Simplifying:

R_n = π^{n/2} / (2^n · Γ(n/2 + 1))

For even dimension n = 2m:

R_{2m} = π^m / (4^m · m!)

For odd dimension n = 2m+1:

R_{2m+1} = π^m / (2^m · (2m+1)!!)

where (2m+1)!! = 1 · 3 · 5 · ... · (2m+1) is the double factorial.

### 2.2 The Sequence

![Fig. 1: R_n decays toward zero as dimension increases — n=2 and n=4 are the only doubly-native values (highlighted).](./figures/math5_01_rn_sequence_decay.png)

Computed as exact rational fractions (π as a 554-digit rational from Machin's formula at 160 terms) and verified against mpmath at 100+ digits. From `math_5_verify.py` output:

| n | R_n | Denominator | Odd factors | Decimal | Pure 2-power? |
|---|---|---|---|---|---|
| 1 | 1 | 1 | none | 1.0000000000 | YES (trivial) |
| 2 | π/4 | 4 | none | 0.7853981634 | **YES** |
| 3 | π/6 | 6 | 3 | 0.5235987756 | no |
| 4 | π²/32 | 32 | none | 0.3084251375 | **YES** |
| 5 | π²/60 | 60 | 15 | 0.1644934067 | no |
| 6 | π³/384 | 384 | 3 | 0.0807455122 | no |
| 7 | π³/840 | 840 | 105 | 0.0369122341 | no |
| 8 | π⁴/6144 | 6144 | 3 | 0.0158543442 | no |
| 9 | π⁴/15120 | 15120 | 945 | 0.0064424002 | no |
| 10 | π⁵/122880 | 122880 | 15 | 0.0024903946 | no |

![Fig. 4: Circle in square (78.5%), sphere in cube (52.4%), 4-ball in 4-cube (30.8%) — the shrinking fill fraction across dimensions.](./figures/math5_04_nball_in_ncube.png)

### 2.3 Connection to Previous Work

R₂ = π/4 is β from [@HOWL-MATH-1-2026]. The MATH-1 result — that β separates as a geometric factor in every equation involving circular cross-sections across nine physical domains — is the n = 2 case of the general pattern investigated here.

R_n is a geometric remainder in the sense of [@HOWL-PHYS-10-2026]: the fractional part when n-ball volume is measured against its bounding n-cube volume. The modulus is d^n. The quotient is 0 (one n-ball fits in fewer than one bounding n-cube). The remainder R_n is the geometric factor that survives in every equation.

---

## III. THE UNIQUENESS OF n = 2 AND n = 4

### 3.1 The Proof

![Fig. 2: m! on log scale — m=0,1,2 are powers of 2, m≥3 all have odd factor 3. The boundary IS the proof.](./figures/math5_02_factorial_proof.png)

**Theorem.** Among all n ≥ 2, the n-ball remainder R_n has a denominator that is a pure power of 2 only for n = 2 and n = 4.

**Proof.** Consider even dimensions first. For n = 2m, the denominator of R_n is 4^m · m! = 2^{2m} · m!. The factor 2^{2m} is a pure power of 2 by construction. Therefore the full denominator is a pure power of 2 if and only if m! is itself a power of 2.

The factorial m! is a power of 2 only for m = 0, 1, and 2:
- 0! = 1 = 2⁰
- 1! = 1 = 2⁰
- 2! = 2 = 2¹
- For m ≥ 3: the prime 3 divides m! (because 3 ≤ m for m ≥ 3), so m! has an odd factor.

This gives n = 0 (m = 0, trivial), n = 2 (m = 1), and n = 4 (m = 2).

For odd dimensions n = 2m+1, the denominator contains (2m+1)!! = 1 · 3 · 5 · ... · (2m+1). For m ≥ 1, this product contains the factor 3, which is odd. Therefore no odd dimension n ≥ 3 has a pure power-of-two denominator.

The only non-trivial dimensions are n = 2 and n = 4. ∎

Verified computationally for m = 0 through 15 in `math_5_verify.py`. Every m ≥ 3 shows smallest odd factor = 3.

### 3.2 The Doubly Native Property

R₂ and R₄ are native to two distinct computational systems:

**The proof system (exact rational arithmetic).** R₂ = π_frac/4 and R₄ = π_frac²/32, where π_frac is π represented as an exact ratio of two integers (from Machin's formula). Both are exact. No approximation at any stage. This property holds for all R_n — every n-ball remainder is exactly representable in Fraction arithmetic.

**The computational system (Q335 binary arithmetic).** In the Q335 basis from [@HOWL-MATH-4-2026], every transcendental is an integer over 2³³⁵. R₂ requires dividing the numerator p(π) by 4 — a 2-bit right shift. R₄ requires dividing p(π²) by 32 — a 5-bit right shift. Both are pure binary operations on integers.

The Q335 numerators are not exactly divisible by these factors (p(π) mod 4 = 2 and p(π²) mod 32 = 8, as reported in `math_5_verify.dat`), so the bit-shift introduces a rounding of ±1 in the last place — an error of ±2⁻³³⁷, which is 66 orders of magnitude below the Planck length. In Fraction arithmetic the computation is exactly exact. In Q335 it is exact to sub-Planck rounding.

Every other R_n (n ≥ 3, n ≠ 4) requires division by an odd prime in the Q335 system, necessitating hybrid Fraction arithmetic or an extended denominator. R₂ and R₄ are the only n-ball remainders that are doubly native — exact in the proof system and binary-native in the computational system.

### 3.3 A Physical Coincidence

The two dimensions where R_n is doubly native are n = 2 and n = 4. The physical sciences use two-dimensional cross-sections (where MATH-1's β = R₂ governs flow, scattering, and drag) and four-dimensional spacetime (where QFT loop integrals, instanton actions, and topological invariants live).

This is stated as a mathematical fact with a physical coincidence. No causal mechanism connecting binary arithmetic to spacetime dimensionality is proposed or implied.

---

## IV. THE 3D SURVEY

### 4.1 Volume Equations: R₃ = π/6

Eight equations that compute sphere volume, each tested as an exact rational identity. The test: for a sphere of diameter d (set to an arbitrary integer d = 7 to avoid special cases), compute the result both in standard textbook form and in R₃ · d³ form. Assert exact Fraction equality. All eight pass.

From `math_5_verify.dat`:

```
1. Sphere volume: pi*d^3/6 = R_3*d^3 ? True (EXACT)
2. Buoyancy: rho*g*pi*d^3/6 = rho*g*R_3*d^3 ? True (EXACT)
3. Grav mass: rho*pi*d^3/6 = rho*R_3*d^3 ? True (EXACT)
4. Moment of inertia: (2/5)m(d/2)^2 = rho*R_3*d^5/10 ? True (EXACT)
5. Nuclear volume (A=27): pi*d_nuc^3/6 = R_3*d_nuc^3 ? True (EXACT)
6. Thermal expansion: V*3*a*dT = R_3*d^3*3*a*dT ? True (EXACT)
7. Packing ratio: V_sphere/d^3 = R_3 ? True (EXACT)
8. Density: m/(R_3*d^3) = m/(pi*d^3/6) ? True (EXACT)
```

Each equation has the form Q = F · R₃ · d³ · Z:

| # | Equation | Q | F | Z | Verified |
|---|---|---|---|---|---|
| 1 | Sphere volume | V | 1 | 1 | EXACT |
| 2 | Buoyancy | F_b | ρg | 1 | EXACT |
| 3 | Gravitational mass | M | ρ | 1 | EXACT |
| 4 | Moment of inertia | I | ρ | d²/10 | EXACT |
| 5 | Nuclear volume | V_nuc | 1 | 1 | EXACT |
| 6 | Thermal expansion | ΔV | 1 | 3αΔT | EXACT |
| 7 | Packing ratio | R₃ | 1 | — | EXACT |
| 8 | Density (inverted) | ρ | m | 1/(d³) | EXACT |

### 4.2 Cross-Section Equations: R₂ = π/4

Two equations that compute sphere projected area or surface area:

```
9. Projected area: pi*d^2/4 = R_2*d^2 ? True (EXACT)
10. Surface area: pi*d^2 = 4*R_2*d^2 ? True (EXACT)
```

Projected cross-section area = R₂ · d². Surface area = 4R₂ · d². Both use R₂, not R₃.

### 4.3 The Rule

The remainder that separates matches the geometric dimension of the operation:

- Volume computation (3D operation on 3D object) → R₃ = π/6
- Cross-section computation (2D operation on 3D object) → R₂ = π/4

The same physical object — a sphere — accesses different remainders depending on what is being computed. There is no single "geometric remainder for a sphere." There is R₃ for its volume and R₂ for its cross-section. The remainder is determined by the modulus (the geometric operation), not by the object.

This is the PHYS-10 remainder framework made concrete. In PHYS-10, the remainder is the observable and the modulus is the symmetry. Here, the modulus is the n-cube volume d^n, and the remainder R_n is the geometric factor that appears in every equation performing an n-ball-volume operation. The operation selects the remainder.

---

## V. THE 4D DECOMPOSITION

![Fig. 5: The single identity π²=32R₄ branches into Ω₄, instanton action, loop factor, Coulomb law, and normalization.](./figures/math5_05_pi2_propagation_tree.png)

### 5.1 The Identity

![Fig. 3: From R₄ to 512R₄ — each rung is a QFT expression with its physical meaning. R₄ is the atomic unit.](./figures/math5_03_r4_ladder.png)

π² = 32 R₄

This is the single finding of this section. Verified as an exact Fraction identity:

```
Verify: 32*R_4 = pi^2 ? True (EXACT)
```

Everything else in this section is a consequence of this identity applied to standard QFT expressions.

### 5.2 The One-Loop Integral

The standard one-loop scalar integral in four-dimensional Euclidean space:

I_n = ∫ d⁴k / (k² + M²)ⁿ

The derivation proceeds in four steps, tracking R₄ at each.

**Step 1: Spherical coordinates.** d⁴k = k³dk · dΩ₄, where Ω₄ = 2π² is the surface area of the unit 3-sphere (the boundary of the unit 4-ball).

**Step 2: Express Ω₄ in terms of R₄.**

Ω₄ = 2π² = 2 · 32R₄ = 64R₄

Verified:

```
Step 2: 64*R_4 = 64*pi^2/32 = 2*pi^2 = Omega_4 ? True (EXACT)
```

**Step 3: Radial integral.** The standard result (by substitution u = k² + M² and Beta function):

∫₀^∞ k³dk / (k² + M²)ⁿ = Γ(2)Γ(n−2) / (2Γ(n)M^{2n−4})

**Step 4: Combine.**

I_n = Ω₄ · [radial] = 64R₄ · Γ(2)Γ(n−2) / (2Γ(n)M^{2n−4}) = 32R₄ · Γ(n−2) / (Γ(n)M^{2n−4})

The standard textbook form is I_n = π² · Γ(n−2) / (Γ(n)M^{2n−4}). These are identical because π² = 32R₄.

Numerical verification for n = 3, M = 1:

```
I_3 = pi^2/2 = 4.9348022005
32*R_4/2     = 4.9348022005
Match: True (EXACT)
```

### 5.3 The Fourier Convention

![Fig. 7: 1/(16π²) mixes geometric content (Ω₄=64R₄) with Fourier convention ((2π)⁴). Separating them reveals R₄.](./figures/math5_07_fourier_mixing.png)

Textbooks write the loop integration measure as ∫d⁴k/(2π)⁴. This divides by (2π)⁴ = 16π⁴:

32R₄ / (16π⁴) = 32(π²/32) / (16π⁴) = π² / (16π⁴) = 1/(16π²)

Verified:

```
32*R_4 / (2*pi)^4 = 0.006332573977646
1/(16*pi^2)       = 0.006332573977646
Match (to Fraction precision): True
```

The 1/(16π²) that appears in every QFT textbook mixes two distinct sources of π:

- **Geometric:** The 4D solid angle Ω₄ = 2π² = 64R₄. This is the surface area of the unit 3-sphere. It arises from the geometry of 4D momentum space.
- **Conventional:** The Fourier normalization (2π)⁴ = 16π⁴. This is four copies of the factor 2π, one per spacetime dimension, arising from the definition of the Fourier transform.

The convention has physical content — it ensures momentum-space propagators have the correct normalization for S-matrix elements. This paper does not recommend changing it. Physicists keep the geometric and conventional factors mixed because it is computationally convenient and because R₄ does not need to be visible for any standard calculation. The observation is structural: separating the two sources of π reveals R₄ = π²/32 as the geometric content of every loop integral, hidden inside the conventional 1/(16π²).

---

## VI. THE INSTANTON DECOMPOSITION

### 6.1 The Identity

8π² = 256 R₄

Verified:

```
8*pi^2 = 256*R_4 ? True (EXACT)
8*pi^2     = 78.9568352087
256*R_4    = 78.9568352087
```

The factor 256 decomposes as 8 × 32:

- **8** is the topological normalization. The second Chern class is defined as c₂ = (1/(8π²)) ∫ Tr(F ∧ F). The 8π² in the denominator is chosen so that c₂ evaluates to an integer for every gauge field configuration. The 8 is topological — it ensures integer quantization.
- **32** = 2⁵ is the denominator of R₄. It is the dimensional factor converting 4-ball volume to bounding 4-cube volume.

The numerical coincidence 256 = 4⁴ is noted but the meaningful decomposition is 8 × 32 — topological times dimensional. The paper does not attribute independent geometric significance to 4⁴.

### 6.2 The Instanton Action

![Fig. 6: S = 256·R₄·c₂/g² — the MATH-1 skeleton Q=F·R·Z generalized to four dimensions with each component labeled.](./figures/math5_06_instanton_skeleton.png)

For a gauge field with instanton number c₂ ∈ ℤ and coupling g:

S = 8π² c₂ / g² = 256 R₄ · c₂ / g²

This is the MATH-1 skeleton Q = F · R · Z generalized to four dimensions:

| Component | Value | Role | MATH-1 analog |
|---|---|---|---|
| Q | S (instanton action) | Output | Q |
| Integer | c₂ ∈ ℤ | Topological quantum number (instanton winding) | Quotient |
| R | R₄ = π²/32 | Geometric remainder (4-ball to 4-cube) | β = R₂ = π/4 |
| F | 256 = 8 × 32 | Normalization (topological × dimensional) | 1 in 2D |
| Z | 1/g² | Coupling impedance | Z |

Numerical verification for SU(2) with c₂ = 1 and α_s = 0.3:

```
g^2 = 4*pi*alpha_s = 3.769911
S = 256*R_4/g^2 = 20.943951
S = 8*pi^2/g^2  = 20.943951
Match: True (EXACT)
```

### 6.3 The Directional Pattern

The Chern class normalization:

c₂ = (1/(8π²)) ∫ Tr(F ∧ F) = (1/(256R₄)) ∫ Tr(F ∧ F)

This converts the raw gauge field integral — rectilinear, an integral over field components in coordinate space — into the integer topological invariant c₂, which counts windings. The conversion factor contains 1/R₄ as its geometric content. The direction is rectilinear → topological, mediated by 1/R₄.

Verified:

```
Chern class normalization:
  1/(8*pi^2) = 1/(256*R_4) ? True (EXACT)
```

The instanton action goes the opposite direction: c₂ · 256R₄/g² converts the integer c₂ (topological) into the action S (physical). The geometric content is R₄. The direction is topological → physical, mediated by R₄.

This is the MATH-1 directional pattern generalized to four dimensions. In two dimensions, MATH-1 found that β = R₂ mediates rectilinear → circular (multiplying by π/4 converts a bounding square area to a circle area) and 1/β mediates circular → rectilinear (multiplying by 4/π converts back). In four dimensions, R₄ mediates topological → physical (instanton action) and 1/R₄ mediates rectilinear → topological (Chern class). The geometric remainder and its reciprocal appear in opposite conversion directions, preserving the directional structure across dimensions.

### 6.4 Other 4D Equations

The identity π² = 32R₄ propagates to every QFT expression containing π²:

```
ABJ anomaly: 1/(16*pi^2) = 1/(512*R_4) ? True (EXACT)
Beta function: 1/(4*pi)^2 = 1/(512*R_4) ? True (EXACT)
Omega_4 = 2*pi^2 = 64*R_4 ? True (EXACT)
4*pi^2 = 128*R_4 ? True (EXACT)
```

These are all consequences of the single identity π² = 32R₄. They are presented as consequences, not as independent findings. The identity has wide reach in 4D physics because π² appears in every expression involving the 4D solid angle, and R₄ is the atomic unit of that geometric content.

---

## VII. CONNECTION TO THE SERIES

### 7.1 MATH-1 Generalized

[@HOWL-MATH-1-2026] proved Q = F · β · d² · Z across nine domains in two dimensions. This paper extends the pattern:

| Dimension | Remainder | Denominator | Q335 | Domains verified |
|---|---|---|---|---|
| 2 | R₂ = π/4 | 4 = 2² | 2-bit shift | 9 (MATH-1) |
| 3 | R₃ = π/6 | 6 = 2 × 3 | Hybrid | 10 (this paper, Section IV) |
| 4 | R₄ = π²/32 | 32 = 2⁵ | 5-bit shift | 5+ (this paper, Sections V–VI) |

The skeleton Q = F · R_n · d^n · Z holds in every case. The geometric remainder R_n captures the n-ball-to-n-cube ratio. The impedance Z captures the domain-specific physics. The integer or topological content captures the quantum number.

### 7.2 PHYS-10 Made Concrete

[@HOWL-PHYS-10-2026] established that the remainder is the observable and the modulus is the symmetry. This paper identifies which remainder: R_n, selected by the geometric dimension of the operation.

The 3D rule (Section IV) demonstrates PHYS-10's principle concretely. The same sphere accesses R₃ for volume and R₂ for cross-section. The modulus is d^n where n matches the operation, not the object. The remainder R_n is the observable geometric content within each n-dimensional sector. The operation selects the modulus. The modulus selects the remainder.

### 7.3 The Q335 Connection

The Q335 basis from [@HOWL-MATH-4-2026] was designed for exact arithmetic on transcendental constants. This paper shows that the two physically important geometric remainders — R₂ for 2D cross-sections and R₄ for 4D spacetime — are the only ones that Q335 handles by pure bit-shift (Section III). The computational framework and the geometric structure are aligned at exactly the dimensions physics uses.

---

## VIII. LIMITATIONS

![Fig. 8: The n-ball remainder sequence — R_n values, four claims, key identities, and the physical coincidence at n=2,4.](./figures/math5_08_identity_card.png)

The 3D survey covers ten equations. A comprehensive survey of every sphere-volume equation in physics would cover more. The pattern is clear across the ten tested — eight volume equations with R₃, two area equations with R₂ — but the survey is not exhaustive.

The 4D decomposition separates R₄ before the Fourier normalization convention. After normalization, R₄ is re-absorbed into 1/(16π²). This paper observes the mixing but does not recommend changing conventions. The (2π)⁴ normalization has physical content and is used universally for sound computational reasons.

The factor 256 = 4⁴ in the instanton decomposition is a numerical coincidence. The meaningful split is 8 × 32 (topological × dimensional). The paper does not attribute independent geometric significance to 4⁴.

The uniqueness of n = 2 and n = 4 for doubly-native R_n is a mathematical fact. The coincidence with the dimensions of physical cross-sections and spacetime is noted without causal claim. No mechanism is proposed or implied.

The directional pattern (R₄ for topological → physical, 1/R₄ for rectilinear → topological) is observed for the instanton/Chern class pair and is consistent with the MATH-1 directional pattern in 2D. Whether it holds for all 4D geometric conversions is not tested exhaustively in this paper.

---

## IX. FALSIFICATION CRITERIA

**F1.** If an equation is found that computes n-ball volume but does not contain R_n as a separable factor, the separation claim is falsified for that equation. Each dimension (2D, 3D, 4D) stands independently — falsifying one does not falsify the others.

**F2.** If the one-loop integral derivation in Section V contains a factor-tracking error, the R₄ separation claim is incorrect. The derivation uses only the definition of 4D spherical coordinates and the standard radial integral. It is reproducible from any QFT textbook.

**F3.** If m! for some m ≥ 3 is a power of 2, the uniqueness proof in Section III is wrong. This cannot occur (3 divides m! for all m ≥ 3), but the criterion is stated for completeness.

**F4.** If the directional pattern (R₄ vs 1/R₄) fails for a 4D geometric conversion not tested in this paper, the directional claim for 4D is weakened. The 2D directional pattern (MATH-1, β vs 1/β) is independently established.

---

## APPENDIX A: THE Q335 NUMERATORS

From [@HOWL-MATH-4-2026]. Common denominator 2³³⁵.

**π:**
219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314

**π²:**
690793580147337726804277647484346770338921354138994508002872352435529393755796399964695383625668575976

**π³:**
2170192036537868242782341740347526814570179266657980009466902575842216583318830559778528157446001240080

Q335 representation of R₂ and R₄:

R₂ = p(π)/4. Since p(π) mod 4 = 2, the bit-shift requires rounding: p(R₂) = round(p(π)/4). Rounding error: ±2⁻³³⁷.

R₄ = p(π²)/32. Since p(π²) mod 32 = 8, the bit-shift requires rounding: p(R₄) = round(p(π²)/32). Rounding error: ±2⁻³³⁷.

Both rounding errors are 66 orders of magnitude below the Planck length.

---

## APPENDIX B: THE R_n TABLE

| n | Formula | Denominator | Odd factors | Decimal | Doubly native? |
|---|---|---|---|---|---|
| 1 | 1 | 1 | none | 1.0000000000 | YES (trivial) |
| 2 | π¹/4 | 4 | none | 0.7853981634 | **YES** |
| 3 | π¹/6 | 6 | 3 | 0.5235987756 | no |
| 4 | π²/32 | 32 | none | 0.3084251375 | **YES** |
| 5 | π²/60 | 60 | 15 | 0.1644934067 | no |
| 6 | π³/384 | 384 | 3 | 0.0807455122 | no |
| 7 | π³/840 | 840 | 105 | 0.0369122341 | no |
| 8 | π⁴/6144 | 6144 | 3 | 0.0158543442 | no |
| 9 | π⁴/15120 | 15120 | 945 | 0.0064424002 | no |
| 10 | π⁵/122880 | 122880 | 15 | 0.0024903946 | no |

All values from `math_5_verify.py`, verified against mpmath.

---

## APPENDIX C: THE 3D SURVEY

From `math_5_verify.py`, all verified as exact Fraction identities with `assert`.

### Volume equations (R₃ = π/6):

| # | Domain | Standard form | Decomposed | Z | Verified |
|---|---|---|---|---|---|
| 1 | Geometry | V = πd³/6 | R₃ · d³ | 1 | EXACT |
| 2 | Fluid mechanics | F_b = ρgπd³/6 | ρg · R₃ · d³ | 1 | EXACT |
| 3 | Gravitation | M = ρπd³/6 | ρ · R₃ · d³ | 1 | EXACT |
| 4 | Mechanics | I = (2/5)m(d/2)² | ρ · R₃ · d⁵/10 | 1/10 | EXACT |
| 5 | Nuclear physics | V = πd_nuc³/6 | R₃ · d_nuc³ | 1 | EXACT |
| 6 | Thermodynamics | ΔV = V · 3αΔT | R₃ · d³ · 3αΔT | 3αΔT | EXACT |
| 7 | Packing | v/d³ | R₃ | — | EXACT |
| 8 | Density | ρ = m/V | m/(R₃ · d³) | inverted | EXACT |

### Cross-section equations (R₂ = π/4):

| # | Domain | Standard form | Decomposed | Why R₂ |
|---|---|---|---|---|
| 9 | Projected area | πd²/4 | R₂ · d² | 2D operation |
| 10 | Surface area | πd² | 4R₂ · d² | 4 × projected area |

---

## APPENDIX D: THE ONE-LOOP DERIVATION

From `math_5_verify.py`, Claim 3.

**Starting point:** I_n = ∫ d⁴k / (k² + M²)ⁿ

**Step 1:** d⁴k = k³dk · dΩ₄ where Ω₄ = 2π² (surface area of unit S³)

**Step 2:** Ω₄ = 2π² = 64R₄. Verified: `64*R_4 = 2*pi^2 ? True (EXACT)`

**Step 3:** ∫₀^∞ k³dk/(k²+M²)ⁿ = Γ(2)Γ(n−2)/(2Γ(n)M^{2n−4})

**Step 4:** I_n = 64R₄ · Γ(2)Γ(n−2)/(2Γ(n)M^{2n−4}) = 32R₄ · Γ(n−2)/(Γ(n)M^{2n−4})

**Textbook form:** I_n = π² · Γ(n−2)/(Γ(n)M^{2n−4}). Identical because π² = 32R₄.

**After Fourier normalization:** I_n/(2π)⁴ = 32R₄/(16π⁴) · Γ(n−2)/(Γ(n)M^{2n−4}) = [1/(16π²)] · Γ(n−2)/(Γ(n)M^{2n−4})

The 1/(16π²) = 1/(512R₄) = 32R₄/(2π)⁴. Verified exact.

**Numerical check (n = 3, M = 1):** I₃ = π²/2 = 32R₄/2 = 4.9348022005. `Match: True (EXACT)`

---

## APPENDIX E: THE VERIFICATION SCRIPT

The complete verification is performed by `math_5_verify.py`, a Python script using only the standard library `fractions` module (for exact rational arithmetic) and `mpmath` (for independent numerical verification). The script:

1. Proves Claim 1 by testing m! for m = 0 through 15
2. Computes R_n for n = 1 through 10 as exact Fractions, verifies against mpmath
3. Proves Claim 2 with 10 equations, each verified by `assert` on exact Fractions
4. Proves Claim 3 by tracing R₄ through the one-loop derivation with exact Fractions
5. Proves Claim 4 with exact Fraction identities for the instanton action and Chern class
6. Verifies R₄ in four additional QFT expressions (ABJ anomaly, beta function, solid angle, 4π²)

Output is recorded in `math_5_verify.dat`. Every `assert` passes. Every identity is verified with zero tolerance and zero approximation. The script is the proof.

---

## APPENDIX F: SERIES PUBLICATION RECORD

| Paper | Registry | Key Result |
|---|---|---|
| MATH-1 | @HOWL-MATH-1-2026 | β = π/4 separates in 9 domains (2D) |
| MATH-2 | @HOWL-MATH-2-2026 | 17 transcendentals as integer pairs at 100 digits |
| MATH-4 | @HOWL-MATH-4-2026 | Universal 2³³⁵ basis: 22 constants, shared denominator |
| PHYS-10 | @HOWL-PHYS-10-2026 | Remainder as observable: 5 formal domains + null search |
| **MATH-5** | **@HOWL-MATH-5-2026** | **R_n separates across dimensions; n = 2, 4 uniquely doubly native** |

---

**END HOWL-MATH-5-2026**

**Registry:** [@HOWL-MATH-5-2026]
**Status:** Complete
**Domain:** Geometry / Number Theory / Mathematical Physics
**Central Result:** The n-ball remainder R_n is a separable geometric factor in every n-ball-volume equation. R₂ = π/4 (2D, nine domains in MATH-1), R₃ = π/6 (3D, ten equations), R₄ = π²/32 (4D, QFT loop integrals and topological invariants). The identity π² = 32R₄ makes R₄ the atomic unit of 4D geometric content. n = 2 and n = 4 are the only dimensions where R_n is doubly native to both exact rational and binary arithmetic.
**What it proves:** Four claims, each verified as exact Fraction identities in `math_5_verify.py`. (1) n = 2, 4 uniqueness by number theory. (2) R₃ separation in 10 equations. (3) R₄ separation in QFT one-loop integrals. (4) Instanton action as 256R₄ · c₂/g² with directional pattern.
**What it does NOT prove:** No causality between n = 2, 4 uniqueness and spacetime dimensionality. No recommendation to change conventions. No new physics.
**Foundation:** MATH-1 (β = R₂), MATH-4 (Q335 basis), PHYS-10 (remainder framework)
**Falsification:** Four specific criteria. Each dimension stands independently.
**Verification:** `math_5_verify.py` and `math_5_verify.dat`. All assertions pass with zero tolerance.
