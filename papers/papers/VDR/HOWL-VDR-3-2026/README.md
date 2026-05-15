# VDR Gym: Exact Arithmetic Across Fifteen Domains

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

HOWL-VDR-1-2026 introduced VDR, an exact finite arithmetic system in irreducible triple form, and demonstrated its core capabilities: zero-drift rational arithmetic, exact matrix inversion, recursive irrational construction, and discrete calculus. This companion paper reports the results of a systematic exercise program — the VDR Gym — that pushes the system across fifteen mathematical domains to map its working boundaries. 290 tests were executed across number theory, polynomial algebra, continued fractions, matrix decomposition, recursive sequences, combinatorics, signal processing, computational geometry, differential equations, optimization, probability, cryptographic primitives, symbolic algebra, fixed-point iteration, and chaotic dynamics. 282 passed. 6 failed due to identifiable test-authoring errors. 2 domains (chaotic iteration at r=4) were terminated due to exponential representation cost — a genuine and important boundary of exact arithmetic that this paper documents as a finding rather than a defect. Every passing result was computed with zero drift using exact VDR rational arithmetic. No floating-point numbers were used in any computation.

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
@article{ HOWL-VDR-2-2026,
  title={ VDR Gym: Exact Arithmetic Across Fifteen Domains },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20208950},
  url = {https://zenodo.org/record/20208950},
  note={Howland Archive: HOWL-VDR-2-2026. Prerequisites: None (foundation paper) }
}
```
---
