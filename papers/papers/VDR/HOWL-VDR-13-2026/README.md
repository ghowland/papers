# Grammar-Directed Compaction and Generation

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

Language models waste most of their computation predicting tokens that are structurally determined. When generating a Python function, the tokens `def`, `(`, `)`, `:`, and the indentation are not creative decisions — they are grammatical facts. When presenting data in a table, the column separators, row boundaries, and alignment characters are format requirements, not content. Current language models spend a full forward pass on every one of these tokens, running attention over the entire context and softmax over the full vocabulary to predict a closing parenthesis that was inevitable the moment the opening parenthesis appeared.

This paper specifies two systems that eliminate this waste. The first is Universal Compaction — a formal system for compressing any structured source material into pipe-delimited tables with typed columns, ID-based cross-references, and self-describing grammars, achieving 75-93% compression while preserving every named concept, relationship, and constraint. The second is Grammar-Directed Generation — a system where Prolog grammars provide the structural tokens of output (brackets, punctuation, formatting, boilerplate) while the language model provides only the content tokens (names, values, creative text), reducing the number of forward passes by 40-80% depending on output type.

Both systems are built on the VDR-LLM-Prolog architecture: an exact-arithmetic language model where every number is an exact fraction with zero drift (VDR-1 through VDR-4), knowledge is stored in scoped Knowledge Bases with logical provenance (VDR-5), computation is performed by 448 deterministic primitives invoked through command tokens (VDR-6, VDR-8, VDR-10), and structured reasoning is conducted through an orchestrated inference loop (VDR-9). The grammars live on the Knowledge Base struct as a persistent field, inheriting through the KB tree like constraints, and the language model can create new grammars at any time by asserting facts — making the system self-extending.

A working Python implementation with 178 passing tests validates the compaction system's roundtrip fidelity, grammar generation, cross-KB usage grammar creation, and grammar inheritance with override shadowing.

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
@article{ HOWL-VDR-12-2026,
  title={ Grammar-Directed Compaction and Generation },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20226594},
  url = {https://zenodo.org/record/20226594},
  note={Howland Archive: HOWL-VDR-12-2026. Prerequisites: None (foundation paper) }
}
```
---
