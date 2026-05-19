# VDR-Zig Q16 Integer LLM

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

We benchmark a single-block transformer language model implemented in Zig using Q16 fixed-denominator integer arithmetic (D = 2^16 = 65536). The implementation uses no floating-point operations, no heap allocations, and no SIMD intrinsics. On a 2019 laptop (Intel Core i7-10th gen class, single core, scalar execution), the model achieves 688 ns per forward pass, 1,159 ns per training step, and 1.42 million tokens per second for greedy generation. All 5 verification tests pass including bit-identical determinism and exact softmax sum-to-one. From this scalar baseline, we project performance under SIMD vectorization, GPU integer tensor cores, and datacenter-scale deployment, comparing directly against conventional float16/float32 and quantized INT8 inference at each level. The central finding is that VDR Q16 arithmetic maps to the same hardware instructions as quantized integer inference — widening multiply-accumulate with right-shift epilogue — placing it at computational parity with INT8/INT16 quantization while providing stronger precision guarantees.

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
@article{ HOWL-VDR-32-2026,
  title={ VDR-Zig Q16 Integer LLM },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20280821},
  url = {https://zenodo.org/record/20280821},
  note={Howland Archive: HOWL-VDR-32-2026. Prerequisites: None (foundation paper) }
}
```
---
