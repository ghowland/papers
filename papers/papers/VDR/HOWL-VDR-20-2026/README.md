# Operational Deployment

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

VDR-19 established that a hybrid LLM-integer-Prolog architecture self-extends through usage — each session deposits persistent Prolog rules, Python scripts, and provenanced facts that compose with prior accumulated state. VDR-20 specifies how to deploy that architecture as a running system. Four prompt runner types — interactive, polling, processor, and internal processing — share identical VDR infrastructure differentiated only by trigger pattern and grant scope. An owner-local filesystem interface provides directories for data ingress, task specification, configuration, output, and review. A coverage loop driven by VDR's exact Remainder arithmetic converts topic specifications into measurable gap descriptions, autonomously fetching and compacting documents until coverage targets are met. The practical on-ramp is local directories: Project Gutenberg, man pages, source repositories, and language documentation exercising every component of the compaction pipeline with zero external dependencies. The owner directs the system using the full tool stack — VDR interactive chat, conventional LLMs for planning, web search, manual configuration — with every decision becoming facts and rules that prompt runners execute. All runner types, directory interfaces, task pipelines, and coverage mechanisms operate through the same primitive pipeline governed by the same visibility, scope, grant, and audit model specified in VDR-16. This paper introduces no new primitives, builtins, struct fields, or modules.

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
@article{ HOWL-VDR-20-2026,
  title={ Operational Deployment },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20241035},
  url = {https://zenodo.org/record/20241035},
  note={Howland Archive: HOWL-VDR-20-2026. Prerequisites: None (foundation paper) }
}
```
---
