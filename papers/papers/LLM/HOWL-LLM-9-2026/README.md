# Softmax Is VDR

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

Softmax turns a list of scores into a probability distribution. Every implementation in every deployed language model computes a distribution that sums to approximately one — 0.9999999997, 1.0000000002 — and the field has treated this as unavoidable, because the exponentials in softmax are transcendental and transcendentals cannot be stored exactly in floating point. This paper shows the near-miss is not a property of softmax. It is a property of floating point. Softmax has an exact partition-of-unity identity that holds regardless of the values of the exponentials, and an exact-arithmetic system that preserves the shared denominator through the sum recovers that identity exactly: the outputs sum to the integer one, structurally, not approximately. We show this is not a coincidence but a structural fact — softmax is a normalization, normalization is the VDR triple [Value, Denominator, Remainder], and floating point breaks softmax precisely by fragmenting the one shared denominator that makes the identity fire. The result is demonstrated in the vdr-math library, where a full transformer runs in exact arithmetic and every softmax sums to exactly one. The contribution is not a faster or more precise softmax. It is the observation that softmax was already exact, and we had been rounding away the exactness at the last step.

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
@article{ HOWL-LLM-9-2026,
  title={ Softmax Is VDR },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.22542644},
  url = {https://zenodo.org/record/22542644},
  note={Howland Archive: HOWL-LLM-9-2026. Prerequisites: None (foundation paper) }
}
```
---
