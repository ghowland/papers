# Riding the Rocket: Why LLM Generation Is Ballistic, Not Steerable

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

LLM code generation is a ballistic event, not a steerable process. The user aims, the model fires, and the output lands somewhere in a cone around the target at a distance the user does not control. Between prompt and completion, there is no steering. The generation has a minimum floor of roughly 400 lines and a ceiling of roughly 1,200 lines, with no comfortable low speed where the user can inspect and navigate as the output forms. The consequence is that LLM-produced code is a destination without a journey — the user possesses working code but not the micro-decision experience that constitutes understanding. This paper describes the ballistic model of LLM generation, the speed and directional constraints that follow from it, the comprehension cost paid after every landing, and the accumulation problem when hundreds of ballistic landings produce a codebase no single person fully understands. The paper provides a decision framework for when ballistic generation is worth the cost and when writing code by hand produces better outcomes despite being slower. This is a companion to [@HOWL-LLM-2-2026], which documents the method for using LLMs within their limits, and [@HOWL-INFO-8-2026], which names the category of system that produces these constraints.

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
@article{ HOWL-LLM-3-2026,
  title={ Riding the Rocket: Why LLM Generation Is Ballistic, Not Steerable },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20096630},
  url = {https://zenodo.org/record/20096630},
  note={Howland Archive: HOWL-LLM-3-2026. Prerequisites: None (foundation paper) }
}
```
---
