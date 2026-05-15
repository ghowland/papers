# Exact-Fraction Language Model Architecture

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

VDR-1 introduced exact finite arithmetic in irreducible triple form. VDR-2 tested it across 15 mathematical domains. VDR-3 extended coverage to 23 domains and integrated the MATH-3/MATH-4 transcendental basis, establishing that VDR has no unique computational boundaries. This paper reports what happened when that arithmetic system was extended into a complete machine learning stack: 24 modules implementing exact-fraction softmax, reverse-mode autodiff, trainable neural network layers, optimizers, attention, a transformer architecture, token sampling, checkpointing, datasets, metrics, and a shared-denominator basis system. 181 tests pass across 7 test batches. A working tiny transformer language model runs forward passes, computes exact logits, produces exact attention weights that sum to exactly 1, and exposes every intermediate value as an inspectable exact fraction. No floating-point arithmetic is used at any point in any computation.

The central finding is not that exact-fraction LLMs are practical at scale — they are not, yet. The central finding is that every component of a language model architecture can be expressed as exact rational arithmetic, that the approximation boundary can be placed exactly where the designer chooses rather than where hardware precision forces it, and that the resulting system produces outputs that are bit-for-bit reproducible, fully inspectable, and provably normalized. This changes the status of VDR from "an exact arithmetic library with ML potential" to "a system that has actually built and run an exact transformer."

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
@article{ HOWL-VDR-4-2026,
  title={ Exact-Fraction Language Model Architecture },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20211285},
  url = {https://zenodo.org/record/20211285},
  note={Howland Archive: HOWL-VDR-4-2026. Prerequisites: None (foundation paper) }
}
```
---
