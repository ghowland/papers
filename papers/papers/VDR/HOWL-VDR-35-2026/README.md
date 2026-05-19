# VDR-LLM-Prolog Integer GPU Compute Stack: TensorProlog

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

Current GPU compute stacks route integer inference through hardware designed for floating-point arithmetic, then compensate with conversion layers, precision negotiation, NaN handling, loss scaling, and rounding mode management. VDR-LLM-Prolog eliminates floating-point computation entirely — the model's forward pass, attention mechanism, softmax, training loop, and all infrastructure operations run on exact integer arithmetic with fixed denominators. TensorProlog is the GPU compute layer built for this architecture. It defines: a type system with three fixed-denominator Q-bases (Q16, Q32, Q335) and no float types; an instruction set where multiply-accumulate is a widening integer multiply plus bit shift; a memory model organized around fixed-size knowledge base structs at integer addresses; session-scoped streams with integer credential enforcement; a Prolog engine parallelized as batched cross-multiply unification across warps; grammar-directed structural token generation that bypasses the LLM forward pass; a runner system that provides autonomous background execution with snapshot-based recycling; and a server layer that clones sessions per connection with time-bounded integer credentials. The spec covers 23 modules, approximately 580 API functions (versus ~4,000+ in CUDA), approximately 30,000 lines of implementation across 168 files, and builds in six phases from pure-Zig CPU arithmetic through GCP GPU deployment. The entire float software stack — cuBLAS precision variants, cuDNN mixed-precision management, TensorRT quantization calibration, NCCL non-deterministic allreduce, loss scaling, gradient clipping, NaN recovery, and the Transformer Engine — is replaced, not optimized.

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
@article{ HOWL-VDR-35-2026,
  title={ VDR-LLM-Prolog Integer GPU Compute Stack: TensorProlog },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20289699},
  url = {https://zenodo.org/record/20289699},
  note={Howland Archive: HOWL-VDR-35-2026. Prerequisites: None (foundation paper) }
}
```
---
