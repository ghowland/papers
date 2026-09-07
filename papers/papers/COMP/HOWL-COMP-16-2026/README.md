# Human Trust Based Federated Publication

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

Current federated publication systems bind a person to a global identity, carry a record of the path an item travelled, and require a directory or a registry for a server to participate. Each of these properties has a cost. A global identity makes a writer addressable across every server. A path record makes the first server of an item identifiable. A directory makes participation a thing that a third party can grant and withdraw.

This paper describes Human Trust Based Federated Publication, a protocol in which none of the three properties is present. A link between two servers is made by two people who exchange public keys outside the program. There is no directory and no registry. An item carries the writer handle, a topic string, a subject, a body, and a creation time, and carries nothing else. Loop control uses a hash that each server computes for itself from those fields and never transmits. A server that receives an item and publishes it again offers it onward as its own publication with a new local sequence number, so no path record is needed and none exists.

The result is a network in which the unit of trust is a pair of administrators, the unit of routing is a topic string that nobody owns, and the unit of storage is a fixed window that each server sets for itself. Growth in the number of servers makes the network more selective rather than larger, because each administrator accepts only the topics that the members of that server read.

The protocol requires one HTTP endpoint, one hash construction, one signature construction, one topic grammar, and one integer sequence. This paper gives the complete wire specification, the conformance requirements, and the test vectors necessary for an independent implementation.

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
@article{ HOWL-COMP-15-2026,
  title={ Human Trust Based Federated Publication },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.21901397},
  url = {https://zenodo.org/record/21901397},
  note={Howland Archive: HOWL-COMP-15-2026. Prerequisites: None (foundation paper) }
}
```
---
