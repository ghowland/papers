# Exact Rational Arithmetic for Sequential Computation

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

Decimal arithmetic — including arbitrary-precision libraries like mpmath — represents numbers in base 10. The only fractions with terminating decimal representations are those whose denominators factor exclusively into 2s and 5s. Every other fraction — 1/3, 1/7, 1/11, 1/13, every fraction whose denominator contains any prime factor other than 2 or 5 — becomes an infinite repeating decimal that must be truncated. This truncation is not a precision issue solvable by carrying more digits. It is a structural incompatibility between the representation and the value.

This paper identifies twenty computational domains where this structural incompatibility produces materially wrong results, and demonstrates that VDR exact rational arithmetic [VDR-1] eliminates the problem entirely. VDR represents 1/3 as [1, 3, 0] — exact, with zero truncation. Chains of operations on exact rationals produce exact rationals. The denominator grows but nothing is discarded. This is not "more precision." It is a categorically different relationship with the numbers.

No prior reading is required. VDR arithmetic is summarized where first used; full specifications are in [VDR-1] and [VDR-14].

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
@article{ HOWL-VDR-28-2026,
  title={ Exact Rational Arithmetic for Sequential Computation },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20260736},
  url = {https://zenodo.org/record/20260736},
  note={Howland Archive: HOWL-VDR-28-2026. Prerequisites: None (foundation paper) }
}
```
---
