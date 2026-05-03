# OpsDB Schema Construction

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

The OpsDB schema is itself data. This paper specifies a schema construction system in which the entire schema lives as hierarchical YAML or JSON files in a git repository, processed by a deterministic loader that produces both the relational database and the API's validation metadata from the same source. The schema files are self-contained, declarative, and bounded in expressive power. A small closed vocabulary of types, modifiers, and constraints describes every field of every entity. There is no embedded logic, no regex, no templating, no computed defaults, no conditional constraints, no inheritance. The constraint vocabulary is what the system permits; everything else is refused, by design, to keep the schema inspectable and to keep validation deterministic at the API gate.

The schema repository contains a `directory.yaml` listing the import order of all entity files. Each file describes one entity: its fields, types, foreign keys, range and length bounds, enum sets, and the FK references that act as set-membership constraints. Schema evolution is governed: no field deletions, no renames, no type changes. Type changes happen by duplicating the field, double-writing during a transition window of N successful releases, and removing the original after the transition. Renames do not happen at all. The schema repo creates the OpsDB initially and modifies it through the same change-management discipline INFRA-5 specifies, keeping schema, database, and API validation synchronized.

What this paper does not specify: the storage engine, the loader's implementation language, the file format choice between YAML and JSON, or the specific authoring tooling. The schema is relational; the relations are declared as data; the rest is implementation choice.

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
@article{ HOWL-INFRA-6-2026,
  title={ OpsDB Schema Construction },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20011418},
  url = {https://zenodo.org/record/20011418},
  note={Howland Archive: HOWL-INFRA-6-2026. Prerequisites: None (foundation paper) }
}
```
---
