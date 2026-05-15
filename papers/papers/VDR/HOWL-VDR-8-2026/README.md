# Computational State Primitives, Universal Data Pathing, and Session Management

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

VDR-5 specified the knowledge architecture for an exact-arithmetic language model: scoped knowledge bases, constraints, provenance, and first-class data surfacing. VDR-6 specified the execution layer: 255 computational primitives, command tokens, operational environments, and credential gating. VDR-7 specified the complete lifecycle: training, feedback, evaluation, deployment, monitoring, and retirement as KB operations. All three papers describe systems that store knowledge and execute operations. None of them address the LLM's own runtime working memory, the addressing system that connects the growing KB tree, or the ability to capture and restore the live state of a session.

This paper specifies three tightly integrated capabilities. Runtime data primitives — LRU caches, counters, locks, queues, stacks, ring buffers, and bitsets — give the LLM bounded, named, scoped working memory inside the KB struct, accessible through command tokens. Universal dotted-path addressing with integer ID acceleration gives every KB, every data primitive, and every fact a structured namespace with O(1) runtime access. Session snapshots, cloning, and disposable operational clones give the system the ability to capture complete live state atomically, fork sessions for experimentation, and maintain stability through controlled recycling of drift-prone clones.

The paper also specifies how command tokens use dotted-path references to minimize the LLM's generative burden — command construction becomes reference selection from a known vocabulary, not freeform text generation.

The three capabilities depend on each other. Data primitives create state worth snapshotting. Dotted paths give snapshots efficient references to that state. Session management provides the lifecycle for data primitives that would otherwise accumulate drift indefinitely. Together they complete the runtime layer that sits between the knowledge architecture (VDR-5) and the execution layer (VDR-6).

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
@article{ HOWL-VDR-8-2026,
  title={ Computational State Primitives, Universal Data Pathing, and Session Management },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20215703},
  url = {https://zenodo.org/record/20215703},
  note={Howland Archive: HOWL-VDR-8-2026. Prerequisites: None (foundation paper) }
}
```
---
