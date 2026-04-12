# The n-Ball Remainder Sequence

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

This paper proves four claims about the n-ball remainder R_n — the fraction of a bounding n-cube occupied by the inscribed n-ball.

First, a number-theoretic result: R_n has a pure power-of-two denominator only for n = 0, 1, 2, and 4. This makes R₂ = π/4 and R₄ = π²/32 the only non-trivial n-ball remainders that are native to both exact rational arithmetic and binary computation. The proof is three lines: the denominator of R_{2m} is 2^{2m} · m!, which is a pure power of 2 if and only if m! is a power of 2, which holds only for m ≤ 2.

Second, a survey result: R₃ = π/6 appears as a separable geometric factor in every equation that computes sphere volume. R₂ = π/4 appears in every equation that computes sphere cross-section or surface area. The remainder is selected by the geometric operation, not by the object. Verified as exact rational identities across ten equations spanning geometry, mechanics, gravitation, nuclear physics, and thermodynamics.

Third, an algebraic result: R₄ = π²/32 separates as an explicit prefactor in the standard one-loop scalar integral in four-dimensional Euclidean space, visible before the Fourier normalization convention (2π)⁴ is applied. The identity π² = 32R₄ is exact. The factor 1/(16π²) that appears in every quantum field theory textbook mixes two distinct sources of π — the geometric four-dimensional solid angle and the Fourier normalization — and separating them reveals R₄ as the geometric content.

Fourth, a decomposition result: the instanton action S = 8π²c₂/g² decomposes as S = 256R₄ · c₂/g², where 256 = 8 × 32 (topological normalization × dimensional factor), c₂ ∈ ℤ is the instanton number, R₄ is the geometric remainder, and 1/g² is the coupling impedance. The Chern class normalization 1/(8π²) = 1/(256R₄) converts the raw gauge field integral into the integer c₂, mediated by 1/R₄ in the opposite direction. This is the MATH-1 skeleton Q = F · R · Z generalized from two to four dimensions, with the directional pattern preserved.

All four claims are verified as exact rational identities in the accompanying script `math_5_verify.py`. Every assertion passes with zero tolerance and zero approximation.

This paper does not claim a causal relationship between the uniqueness of n = 2 and n = 4 and spacetime dimensionality. It does not recommend changing QFT conventions. It does not propose new physics. Every equation decomposed is standard and published. The contribution is making R_n visible as the separable geometric content across dimensions.

---

## Howland Archive Context

This publication is part of the **Howland Archive**, a collection of research spanning information theory, computational architecture, physics, and philosophy. All work unified by axiomatic methodology: derive complex systems from minimal constraint sets with zero free parameters.

### Series Position

**Prerequisites:** None (foundation paper)

---

**Methodology Principles:**

1. **Maximum Constraints:** Start with minimal axioms
2. **Necessary Derivation:** All results follow logically from axioms
3. **Extreme Falsifiability:** Clear failure conditions
4. **Working Implementations:** Build it, don't just theorize
5. **Measured Results:** Empirical validation where possible

---

## Repository Contents

```
zenodo_package/
├── manuscript.md              # Main paper
├── README.md                  # This file
└── zenodo.json                # Zenodo metadata
```


---

## Citation
If you use this work in a pedagogical or research context, please cite:

```bibtex
@article{ HOWL-MATH-5-2026,
  title={ The n-Ball Remainder Sequence },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.zzz},
  url = {https://zenodo.org/record/zzz},
  note={Howland Archive: HOWL-MATH-5-2026. Prerequisites: None (foundation paper) }
}
```
---
