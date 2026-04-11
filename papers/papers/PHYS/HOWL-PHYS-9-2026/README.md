# The Electromagnetic Chain in Integer Arithmetic

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

This paper demonstrates three claims, stated precisely.

First: the QED perturbative series through 3-loop order, which relates the electron anomalous magnetic moment a_e to the fine structure constant α, is an integer transformation law. The coefficients A₁ through A₃ are exact rational linear combinations of five transcendental constants (π, ln(2), ζ(3), ζ(5), Li₄(1/2)), each represented as an exact ratio of two integers via [@HOWL-MATH-2-2026]. The 4-loop coefficient A₄ is a numerical constant computed to 1100 digits whose partial analytical structure involves the same transcendental families plus elliptic integrals, but whose full decomposition remains open. The law through 3-loop contains no measured input. At 4-loop, it contains numerical content (A₄) not yet fully decomposed into named transcendentals.

Second: inverting this law — solving for α given the experimentally measured a_e — is performed entirely in exact Fraction arithmetic via Newton's method. The measured input is one rational number: a_e = 115965218059/10¹⁴. The output is α⁻¹ = 137.035998583, matching CODATA 2022 (137.035999177 ± 0.000000021) to 4.3 parts per billion. The residual decomposes into known missing contributions at 5-loop and beyond, totaling approximately 4.2 ppb. The residual is accounted for.

Third: combining the inversion with the vacuum polarization running from [@HOWL-PHYS-5-2026] produces the electromagnetic coupling at every energy scale from atomic to Z-boson, with the full chain executed in Fraction arithmetic. The endpoint α⁻¹(M_Z) is a prediction testable against the direct LEP measurement, limited by the hadronic VP uncertainty (±73 ppm).

This paper demonstrates the integer structure of the electromagnetic transformation law. It does not claim parameter reduction. The relationship a_e ↔ α via QED is standard physics, used by the institution to extract α from a_e measurements. What is shown here is that this extraction, and the subsequent running to all energy scales, can be expressed as integer operations on exact rationals — making explicit what the law IS (integers and transcendentals) versus what the universe supplies (one measured rational).

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
@article{ HOWL-PHYS-9-2026,
  title={ The Electromagnetic Chain in Integer Arithmetic },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.zzz},
  url = {https://zenodo.org/record/zzz},
  note={Howland Archive: HOWL-PHYS-9-2026. Prerequisites: None (foundation paper) }
}
```
---
