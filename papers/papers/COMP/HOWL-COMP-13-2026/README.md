# Runtime Struct Navigation in Compiled Languages Without Reflection or Code Generation

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

Compiled languages discard struct layout information after compilation. Programs that need runtime access to field metadata — for serialization, property editors, data binding, or path-based navigation — resort to runtime reflection, code generation, or manual registration. All three scale poorly with struct count. This paper presents a fourth approach: capture struct field metadata at build time into a static descriptor table, then walk arbitrary nested structs at runtime through pointer arithmetic using pre-computed offsets. The technique requires no runtime type information, no generated source files, no dynamic dispatch, and no heap allocation. A working implementation covering 140+ structs reduced compile time from 15 seconds to 2 seconds by eliminating the code generation pipeline it replaced. The approach is portable to any compiled language with access to `offsetof` or equivalent.

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
@article{ HOWL-COMP-13-2026,
  title={ Runtime Struct Navigation in Compiled Languages Without Reflection or Code Generation },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20846381},
  url = {https://zenodo.org/record/20846381},
  note={Howland Archive: HOWL-COMP-13-2026. Prerequisites: None (foundation paper) }
}
```
---
