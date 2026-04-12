# Tall-Infra, Data-Only Development

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

This paper defines and distinguishes **tall-infra, data-only** architecture from the commonly used term "data-driven." While data-driven development has been industry standard for decades, it has always preserved a wall between data (assets, tuning values) and behavior (compiled code). Tall-infra, data-only eliminates this wall entirely. The runtime binary contains no gameplay types, no behavior code, no knowledge of what a "goblin" or "quest" or "fireball" is. All semantics—every enemy, mechanic, system interaction—exist purely as dataset rows that can be hot-swapped without recompilation.

This is not a proposal. It describes a working system running 200 entities with 100 followers each at 60fps, unoptimized, with a clear path to 10,000+ entities.

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
@article{ HOWL-COMP-2-2026,
  title={ Tall-Infra, Data-Only Development },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.18655378},
  url = {https://zenodo.org/record/18655378},
  note={Howland Archive: HOWL-COMP-2-2026. Prerequisites: None (foundation paper) }
}
```
---
