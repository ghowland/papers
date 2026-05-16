# VDR-LLM-Prolog: Safe by Contract

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

This paper demonstrates that the VDR-LLM-Prolog system, specified across the preceding fifteen papers, produces structural safety as an emergent property of its architecture. No safety-specific features were designed. No safety-specific modules exist. The safety properties arise from three architectural layers that were built for other purposes: knowledge base visibility controls built for data scoping produce access control, the positive credential grant system built for operational primitive governance produces default-denial authorization, and grammar-layer output validation built for format correctness produces content restriction. The language model operates as an untrusted component between pre-filtered input and post-validated output. It cannot surface data the user lacks access to because that data never enters its context — knowledge base queries return only in-scope, visibility-matched results through integer comparison in the primitive layer. It cannot perform unauthorized operations because the grant system rejects ungrated requests before execution. It cannot render restricted content because grammar-layer constraints catch flagged material after generation but before output. Session-level access decisions are computed by Prolog rules evaluating exact integer counters against declared thresholds, with zero language model involvement in the decision. Jailbreaking is structurally impossible for data access because no prompt can change the result of an integer comparison in compiled code. This paper introduces no new primitives, struct fields, builtins, or modules. Every mechanism uses existing components. Safety is not a feature of this system. It is a consequence of it.

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
@article{ HOWL-VDR-16-2026,
  title={ VDR-LLM-Prolog: Safe by Contract },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20234102},
  url = {https://zenodo.org/record/20234102},
  note={Howland Archive: HOWL-VDR-16-2026. Prerequisites: None (foundation paper) }
}
```
---
