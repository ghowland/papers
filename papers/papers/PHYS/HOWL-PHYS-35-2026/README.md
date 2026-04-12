# The No-Threshold Puzzle — More CD Running Means Better Predictions

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

The Cabibbo Doublet — a hypothetical vector-like quark doublet in the (3,2,1/6) representation — modifies the gauge coupling beta functions and enables precise unification predictions. The best α_s prediction (PHYS-30: 0.11838, miss 0.33% from measured 0.1180) uses the CD betas from M_Z (91 GeV) to M_GUT with no physical threshold. When a threshold is applied at M_VL = 500 GeV (SM betas below, CD betas above), the miss worsens to 4.0% — a factor of 12× degradation. This is puzzling because the CD has a physical mass and should decouple below it. This paper investigates the puzzle through three tests. First, a scan of 12 threshold positions from 200 GeV to 6 TeV: the miss increases monotonically with M_VL, and no threshold position matches the no-threshold quality. The best hard threshold (M_VL = 200 GeV, miss 1.72%) is still 5.3× worse. Second, a step sensitivity test at 200/500/1000/2000 Euler steps: the 12.3× advantage is unchanged at every step count, ruling out numerical artifact. Third, a soft threshold test using a sigmoid transition f(μ) = 1/(1+(M_VL/μ)²): the soft threshold is WORSE than the hard threshold at every M_VL, with misses of 7–13%. The pattern is clear and monotonic: more CD running = better prediction. The puzzle is documented with three possible explanations: virtual propagation below M_VL, effective resummation, or cancellation of missing higher-order corrections. Future papers (PHYS-37: RK4 integrator, PHYS-38: three-loop estimate) will test which explanation holds.

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
@article{ HOWL-PHYS-35-2026,
  title={ The No-Threshold Puzzle — More CD Running Means Better Predictions },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.19528709},
  url = {https://zenodo.org/record/19528709},
  note={Howland Archive: HOWL-PHYS-35-2026. Prerequisites: None (foundation paper) }
}
```
---
