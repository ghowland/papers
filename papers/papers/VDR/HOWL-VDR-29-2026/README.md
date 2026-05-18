# VDR in Zig SIMD and GPU Performance versus Floating Point

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

Every floating-point operation can round. One rounding is negligible. Millions compound. This paper presents performance projections for VDR — Value, Denominator, Remainder — exact integer arithmetic implemented in Zig targeting AVX-512 SIMD and NVIDIA H100 GPU tensor cores. VDR eliminates accumulated arithmetic error by replacing floating-point operations with integer multiply, shift, and mask on a fixed power-of-two denominator basis, storing exact remainders rather than discarding them.

The reference VDR implementation (vdr-math, Python) uses a 335-bit basis tuned for physics and transcendental computation. This paper retunes the basis to match machine register widths for LLM inference and diffusion model workloads: 8-bit for weights, 16-bit for activations, 64-bit for gradient accumulation. At these widths, VDR's divmod operation reduces to a bit shift and mask — native hardware operations on all modern processors.

Projected results on H100: 1.6-1.8× throughput improvement on GEMM via INT8 tensor cores, 3-4× improvement on softmax via elimination of the Special Function Unit bottleneck, 2× effective memory bandwidth from half-size weights, and zero accumulated drift over arbitrarily long operation chains. Full transformer forward pass for a 7B parameter model projects to approximately 2× throughput versus optimized FP16, with exact results at every step.

All projections are conservative estimates based on published hardware specifications. VDR delivers exact arithmetic not by trading performance for correctness, but by targeting integer execution units that are faster than their floating-point counterparts for the operations ML pipelines actually perform.

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
@article{ HOWL-VDR-29-2026,
  title={ VDR in Zig SIMD and GPU Performance versus Floating Point },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20266675},
  url = {https://zenodo.org/record/20266675},
  note={Howland Archive: HOWL-VDR-29-2026. Prerequisites: None (foundation paper) }
}
```
---
