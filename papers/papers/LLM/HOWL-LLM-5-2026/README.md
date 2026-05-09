# Incompatibility by Construction

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

LLM-assisted software development operates under two success criteria that are incompatible by construction. The model's success criterion is locally coherent output — code that is syntactically valid, responsive to the current prompt, and consistent with whatever context is loaded this turn. The engineer's success criterion is total system correctness — a finished product where every component aligns with every other component across all conditions, including conditions no one enumerated. The first is a per-turn local property that the transformer architecture can provide. The second is a continuous global property that requires persistent constraint maintenance the architecture does not have. No sequence of locally successful outputs guarantees the global property, because the global property depends on cross-output consistency that no individual output can ensure. This paper identifies eighteen specific cases where the two criteria diverge, demonstrates why tests, specifications, and agentic workflows each fail to bridge the gap, and establishes that the incompatibility follows from what per-turn generation is — not from how good it currently is. The incompatibility cannot be fixed with more LLM. It can only be managed by an engineer who knows it exists and scopes their use of the tool accordingly.

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
@article{ HOWL-LLM-4-2026,
  title={ Incompatibility by Construction },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20097126},
  url = {https://zenodo.org/record/20097126},
  note={Howland Archive: HOWL-LLM-4-2026. Prerequisites: None (foundation paper) }
}
```
---
