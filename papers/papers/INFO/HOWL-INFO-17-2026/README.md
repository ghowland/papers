# The General Theory of State Change

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

Codd normalized the form of data. He identified what all stored information has in common, made that common structure the only structure, and stated falsifiable rules that test whether a system genuinely realizes the model. The behavioral half of computing never received the equivalent treatment. Applications still consist of bespoke verbs: hand-written functions that each privately validate, mutate, and log state. The costs practitioners treat as inevitable — duplicated validation, integration defects between features, unauditable state, decision layers that disagree with the rules they act under — are all costs of verbs being many, private, and mutually ignorant.

This paper states the missing symmetric theory: a normalization of behavior. The claim divides into three parts of different kinds. The principles are theory: twelve statements about what state change is, culminating in one sentence — every change of state is a guarded, staged, recorded, scoreable movement of quantities between addresses, interpreted by a single closed engine. The primitive set is engineering: a concrete set of record shapes, presented in full, that realizes the principles and is directly implementable by others. The rules are the test: thirteen falsifiable rules, paralleling Codd's, that determine whether an arbitrary primitive set genuinely realizes the principles rather than realizing them in name. The paper closes by demonstrating that the same primitive set expresses domains as distant as enterprise resource planning, agent simulation at the depth of Dwarf Fortress, and declarative infrastructure orchestration, because under the theory a domain is an assignment of meaning to records, not a body of code.

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
@article{ HOWL-INFO-17-2026,
  title={ The General Theory of State Change },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.22493091},
  url = {https://zenodo.org/record/22493091},
  note={Howland Archive: HOWL-INFO-17-2026. Prerequisites: None (foundation paper) }
}
```
---
