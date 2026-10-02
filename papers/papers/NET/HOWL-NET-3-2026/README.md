# IPv4-64 Reference Implementation on P4 Programmable Hardware

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

This document specifies a complete P4 forwarding plane for IPv4-64 as defined in [@HOWL-NET-1-2026]. It covers packet parsing, validation, authentication, classification, routing, load balancing, firewall policy, QoS marking, metering, connection tracking, and egress transformation. It includes an IPv4 edge conversion system that allows a carrier to run IPv4-64 as the internal core protocol while accepting and emitting standard IPv4 at network boundaries.

The specification targets P4-programmable DPUs (NVIDIA BlueField-3, AMD Pensando Elba, Intel IPU E2100) and FPGA-based SmartNICs (AMD/Xilinx Alveo SN1000). A carrier that deploys these devices can load the IPv4-64 forwarding plane as a P4 program without replacing hardware, without coordinating with other carriers, and without waiting for industry-wide adoption.

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
@article{ HOWL-NET-3-2026,
  title={ IPv4-64 Reference Implementation on P4 Programmable Hardware },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.zzz},
  url = {https://zenodo.org/record/zzz},
  note={Howland Archive: HOWL-NET-3-2026. Prerequisites: None (foundation paper) }
}
```
---
