# VDR-LLM-Prolog: Functional Remainder Hardware

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

The VDR arithmetic system represents every value as a triple [Value, Denominator, Remainder] where the Remainder slot can hold a callable function that produces exact rational values at any requested depth. This functional remainder mechanism — specified in [@HOWL-VDR-1-2026] and used throughout the system for transcendental evaluation — has implications for hardware that prior papers in the series did not explore. On the VDR-22 integer-native ASIC [@HOWL-VDR-22-2026], each Q335 Integer Unit already contains a 384-bit ALU with 1-2 cycle multiply and free power-of-two division via fixed wiring. This paper specifies a Functional Remainder Unit (FRU) that extends each QIU to evaluate functional remainders — Taylor recurrences, Newton iterations, and series summations — in hardware using the existing ALU, without round-tripping to the host processor. The FRU adds approximately 500,000 transistors per QIU (3.4% die area increase across 5,120 units) and enables three capabilities that the base VDR-22 chip cannot provide: hardware-native exact exponential softmax at competitive latency with float implementations (25-40 nanoseconds for 1,024 logits versus host-bound milliseconds without the FRU), continuous per-step remainder resolution during training that replaces periodic Q-basis reprojection stalls with microsecond-level maintenance, and complete Prolog unification over active VDR values carrying nonzero remainders. At single-query scale, the FRU does not change wall-clock latency — the language model forward pass at approximately 30 microseconds per command token dominates primitive execution at 1-100 nanoseconds by 300-30,000×. At datacenter scale with millions of concurrent sessions, the FRU eliminates host round-trips for remainder resolution, keeping the entire rule-driven execution path on the data-plane chip and removing the serialization bottleneck that would otherwise limit throughput as accumulated Prolog rules handle an increasing fraction of work autonomously. The paper specifies the FRU microarchitecture, traces the full inference chain with adaptive precision, analyzes the datacenter throughput implications, and identifies the boundary between what the FRU changes (capability and throughput at scale) and what it does not (single-query latency).

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
@article{ HOWL-VDR-23-2026,
  title={ VDR-LLM-Prolog: Functional Remainder Hardware },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20252877},
  url = {https://zenodo.org/record/20252877},
  note={Howland Archive: HOWL-VDR-23-2026. Prerequisites: None (foundation paper) }
}
```
---
