# VDR Toy LLM

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

We present a complete transformer language model — embedding, self-attention, feed-forward network, backpropagation, weight updates, and text generation — running entirely in exact rational arithmetic with no floating-point operations. The model uses the vdr-math Python library, which represents every value as an ordered triple [V, D, R] (Value, Denominator, Remainder) with a fixed denominator D = 2^32. We describe the denominator growth problem that arises when standard rational arithmetic operators are applied in a fixed-frame system, the operator-level solution we implemented to prevent it, and the quadratic softmax surrogate that eliminates transcendental functions from the forward pass. The resulting toy model — 181 parameters, vocabulary of 5, trained for 20 epochs on a 6-word corpus — passes 9 verification tests including bit-identical determinism across runs and exact sum-to-one softmax outputs. All denominators remain at 2^32 through every operation chain. The work demonstrates that a fixed-denominator rational arithmetic system can support a complete LLM training and inference pipeline, and identifies the engineering steps required to scale beyond toy dimensions.

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
@article{ HOWL-VDR-31-2026,
  title={ VDR Toy LLM },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.zzz},
  url = {https://zenodo.org/record/zzz},
  note={Howland Archive: HOWL-VDR-31-2026. Prerequisites: None (foundation paper) }
}
```
---
