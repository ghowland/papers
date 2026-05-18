# Economics of Scale: Floating Point vs Exact Integer ML Models

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

The ML industry is four years into commercial deployment. Datacenters costing hundreds of billions of dollars are under construction. The hardware going into those facilities, NVIDIA H100, B100, and their successors, contains integer execution units that deliver 2× the throughput of the floating-point units the industry currently uses. The software stack running on that hardware discards information at every arithmetic operation, produces non-deterministic output, cannot secure data access structurally, and spends 80–95% of generated tokens on infrastructure that deterministic tools handle better.

This paper presents the economic analysis of VDR, Value, Denominator, Remainder, exact integer arithmetic as a replacement foundation for ML inference and training. VDR is not a competing model architecture. It is a different computational substrate: every number is an integer triple, every operation is exact, every result is deterministic, and the hardware to run it already exists in every modern GPU and CPU.

The economics compound across three independent axes. First, per-token throughput improves 1.5–2× on existing hardware because INT8 tensor cores are faster than FP16 tensor cores. Second, total tokens per task reduce 70–98.6% because data lives in addressed knowledge bases, deduction runs in a Prolog engine, and grammars provide structural output, the LLM generates only judgment and prose. Third, cost scaling changes from quadratic to linear because state is stored at integer addresses rather than re-read through the attention window every turn.

The compound effect for structured workloads: 40× or greater reduction in total compute cost, with exact arithmetic, deterministic reproduction, and structural safety. For purely creative tasks, unconstrained prose, poetry, open conversation, VDR provides the per-token hardware speedup but minimal token reduction. The savings are task-shaped: the more structure a task has, the greater the reduction.

These numbers follow from instruction counts on published hardware specifications and measured token distributions across task categories. They do not require speculation about future hardware or unvalidated capabilities. The arithmetic is validated across 884 tests in 37 domains with zero computation errors. The hardware exists in production. The question is not whether exact integer ML is faster and cheaper. It is when the industry adopts it.

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
@article{ HOWL-VDR-30-2026,
  title={ Economics of Scale: Floating Point vs Exact Integer ML Models },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20270204},
  url = {https://zenodo.org/record/20270204},
  note={Howland Archive: HOWL-VDR-30-2026. Prerequisites: None (foundation paper) }
}
```
---
