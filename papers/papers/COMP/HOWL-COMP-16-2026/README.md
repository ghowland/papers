# Parallelism as a Consequence of Normalized Behavior

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

A prior paper in this series, *The General Theory of State Change* [@HOWL-INFO-17-2026], normalized behavior: it reduced all state change to one verb — a guarded, staged, recorded movement of quantities between addresses — applied by a single closed interpreter with no path around it. That paper argued its rules from correctness: whole-set atomicity, a complete audit ledger, validation that cannot be bypassed.

This paper states a consequence the prior paper left implicit. Two of its rules — staged delivery and nonsubversion — jointly determine not only *what* a change is but *when memory changes*. Any realization honoring both rules acquires a two-phase execution structure: a serialized mutation window in which the single executor applies all staged change, followed by a read phase in which the entire world is immutable. This structure, which we name the frozen frame, is a complete memory model, a parallelism strategy, and an elimination of concurrency overhead — obtained as a corollary rather than built as a feature. Four of the five components of the concurrency tax [@HOWL-INFO-14-2026] go to zero structurally; the fifth becomes an explicit, tunable data-layout variable, which is exactly the variable data-oriented design practice knows how to tune. The paper derives the corollary, accounts for the tax, describes the execution strategies the freeze permits, draws the boundary of what does not become data, states the costs honestly, and closes with falsifiable claims. The claims are of three kinds, tagged throughout: the phase structure and its properties are theory, holding for any realization of the rules; the batching, placement, and thread substrate described are engineering, illustrative of one running realization; the closing claims are the test.

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
@article{ HOWL-COMP-16-2026,
  title={ Parallelism as a Consequence of Normalized Behavior },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.22585474},
  url = {https://zenodo.org/record/22585474},
  note={Howland Archive: HOWL-COMP-16-2026. Prerequisites: None (foundation paper) }
}
```
---
