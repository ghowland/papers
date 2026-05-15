# VDR Arithmetic: Value, Decimal, Remainder

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

Floating-point and decimal arithmetic systems lose exact equality under repeated operations. This loss is structural — it comes from representing values as single scalars that discard intermediate structure at every step. This paper introduces VDR, an arithmetic system that represents every value as a finite tree of integer triples `[V, D, R]` where V is the value slot, D is the denominator frame, and R is the remainder — exact unresolved structure that scalar systems would discard. The remainder is not error. It is part of the value.

The system provides exact rational arithmetic with zero drift over arbitrary operation chains, exact matrix inversion of ill-conditioned matrices where floating-point fails, recursive construction of irrational values where every expansion step is itself exact, and discrete calculus operators where every derivative and integral is an exact rational at every step size. A working Python implementation accompanies this paper. Every claim is verified by executable tests. The code is the specification.

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
@article{ HOWL-VDR-1-2026,
  title={ VDR Arithmetic: Value, Decimal, Remainder },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20207144},
  url = {https://zenodo.org/record/20207144},
  note={Howland Archive: HOWL-VDR-1-2026. Prerequisites: None (foundation paper) }
}
```
---
