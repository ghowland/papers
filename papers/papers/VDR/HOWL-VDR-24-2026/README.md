# LM Software

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

This paper defines LM Software — a new category of software where applications are developed by configuring language model sessions with structured state, encoding logic as Prolog rules over exact arithmetic primitives, validating behavior interactively, snapshotting working state as deployable artifacts, and cloning those artifacts on demand as running instances. The language model is the runtime. A hierarchical knowledge base tree is the address space. Prolog is the programming language. Snapshots are the binaries. Usage improves the application without rebuilding it.

LM Software is distinct from conventional software (compiled code, static behavior, developer-built), from AI tooling (LLMs wrapped in conventional orchestration code), and from conventional LLM applications (stateless models behind prompt templates). It is software developed by users through conversation, deployed as frozen state snapshots, and improved by usage through rule accumulation — where every session deposits reusable logic that makes future sessions cheaper and more capable.

This paper introduces all necessary concepts from the VDR-LLM-Prolog architecture [VDR-14] so that no prior reading is required, then develops the theory and practice of LM Software through two complete worked examples.

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
@article{ HOWL-VDR-24-2026,
  title={ LM Software },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.zzz},
  url = {https://zenodo.org/record/zzz},
  note={Howland Archive: HOWL-VDR-24-2026. Prerequisites: None (foundation paper) }
}
```
---
