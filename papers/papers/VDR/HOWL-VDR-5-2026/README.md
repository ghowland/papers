# Exact Arithmetic Meets Logical Provenance

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

This paper specifies VDR-LLM-Prolog, a language model architecture where every value is an exact fraction, every derivation is recorded in a logic programming knowledge base, every constraint is a first-class queryable object, and every piece of knowledge is directly surfaceable to the user without passing through the language model's token generation. The specification integrates four prior results: VDR exact arithmetic (VDR-1 through VDR-3), the VDR machine learning stack (VDR-4), transcendental constant representation (MATH-3/MATH-4), and a custom Prolog-style knowledge engine designed for LLM provenance.

The system has three layers. The arithmetic layer (VDR) ensures every number is an exact fraction with zero drift and zero silent truncation. The logic layer (Prolog) records how every value was derived, what it depends on, and what constraints it satisfies. The conversation layer manages scoped knowledge bases, working data sets, topic tracking, and constraint activation — giving the language model structured persistent memory that survives topic switches, supports inheritance and shadowing, and is directly queryable by the user.

The central claim is that data provenance, constraint enforcement, and conversational state tracking are not features to be bolted onto a language model after the fact. They are architectural requirements that should be present from the foundation. This paper specifies what that foundation looks like.

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
@article{ HOWL-VDR-5-2026,
  title={ Exact Arithmetic Meets Logical Provenance },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.zzz},
  url = {https://zenodo.org/record/zzz},
  note={Howland Archive: HOWL-VDR-5-2026. Prerequisites: None (foundation paper) }
}
```
---
