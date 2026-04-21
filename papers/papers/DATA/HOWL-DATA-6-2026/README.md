# A Versioned Node System for Integer Fraction Physics

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

DATA-6 is a versioned node-based system for physics research built on integer fraction arithmetic. Every entity — constant, derivation, connection, experiment, result, program — is a versioned node with a canonical key, provenance, and level classification. The system stores 414 value nodes across 24 JSON files, 57 derivation functions and 9 connection functions in two Python registries, 13 experiment definitions with 85+ comparisons, and 13 research programs with 26 kill switches.

The system is operational and has produced results. Three case studies demonstrate its capabilities: (1) the beta unification experiment with 29 comparisons covering gauge coupling extraction, gap ratio correction, Koide analysis, and cosmological predictions from integers, all passing; (2) a what-if BSM scan testing 5 of 15 candidates against the measured gap ratio, identifying the Cabibbo Doublet as the unique winner by a factor of 7; (3) a QED alpha extraction chain that derives four CODATA values (α⁻¹, R∞, a₀, μ₀) from one measurement (a_e) plus integer transformation laws, matching independent measurements at 3.3-8.0 ppb with error propagation following exact α-power scaling.

DATA-6 succeeds DATA-4 (146 entries, 38/38 checks) and DATA-5 (222 objects, 322/323 checks). It differs from both in architecture: where DATA-4 was a flat verified registry and DATA-5 was an object-oriented platform library, DATA-6 is an experiment-driven system where computation is declared in JSON, executed by a generic runner, and results are stored as versioned nodes with full provenance. Nothing is overwritten. Nothing is deleted. The database only grows.

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
@article{ HOWL-DATA-6-2026,
  title={ A Versioned Node System for Integer Fraction Physics },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.19665914},
  url = {https://zenodo.org/record/19665914},
  note={Howland Archive: HOWL-DATA-6-2026. Prerequisites: None (foundation paper) }
}
```
---
