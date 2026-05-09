# Calibrate, Extract, Refine

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

This paper documents a method for using LLM chat sessions to produce usable engineering output. The method treats each chat session as a finite instrument that must be calibrated through diagnostic probing before use, used for bounded one-shot extraction within the model's coherence ceiling, and left behind while the engineer refines the output by hand. The method is grounded in architectural properties of transformer models — the absence of constraint checking, the degradation of attention across context length, the gravitational pull toward training-weight medians — and shaped by fifteen months of empirical observation that the coherence ceiling for real code generation has not moved across model generations. Chat is the only LLM interface that provides a correction channel: the ability to observe output, diagnose session-specific misalignment, and correct it before further generation. All other interfaces — tab completion, agentic, autonomous — remove this channel and leave the engineer with output that trends toward generic patterns that violate system-specific constraints. The paper is not a claim that this method is universally superior. It is a claim that for engineers working on systems that exceed the model's coherence ceiling, the correction channel is the feature that makes AI usable at all, and this method is how to use it.

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
@article{ HOWL-LLM-2-2026,
  title={ Calibrate, Extract, Refine },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20096290},
  url = {https://zenodo.org/record/20096290},
  note={Howland Archive: HOWL-LLM-2-2026. Prerequisites: None (foundation paper) }
}
```
---
