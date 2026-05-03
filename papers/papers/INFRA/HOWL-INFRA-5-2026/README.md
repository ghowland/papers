# OpsDB API Layer

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

The OpsDB API is the single gate through which all interactions with OpsDB data pass. It is self-contained operational software: it does not depend on Kubernetes, on a specific cloud, on any orchestrator, or on any system the OpsDB models. It calls out only to authoritative external systems for the authority those systems own — identity providers (LDAP, Active Directory, OIDC, SAML) for human authentication, secret backends (Vault and equivalents) for credential resolution. Every other governance concern — authorization, validation, change management routing, versioning, audit — is enforced at this gate, uniformly, against all entity types in the schema.

This paper specifies the API surface. The get-set operations work uniformly across all entity types. The search API supports filter predicates, named join paths through the schema, projection, ordering, and bounded pagination. Field-level versioning bundles per change_set, with full-state version rows that make point-in-time reconstruction a single lookup. Five layers of authorization (role, per-entity governance, per-field classification, per-runner authority, policy rules) all evaluate as data. Runner report keys gate every runner's writable surface, making the answer to "who can write this metric" a queryable declaration rather than implicit trust. Change_sets pass through a defined lifecycle as OpsDB rows; the to-perform queue is approved-not-yet-applied rows; the change-set executor that drains it is a runner per [@HOWL-INFRA-4-2026], not the API. Notification dispatch is a runner concern. The API gates, validates, routes, records, and responds; runners do the world-side work.

What this paper does not specify: storage engine, wire protocol, deployment topology, identity provider integration specifics, UI design, specific runner implementations. The schema is the long-lived artifact per [@HOWL-INFRA-2-2026]; the API surface specified here is stable across implementations of the schema.

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
@article{ HOWL-INFRA-5-2026,
  title={ OpsDB API Layer },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20011432},
  url = {https://zenodo.org/record/20011432},
  note={Howland Archive: HOWL-INFRA-5-2026. Prerequisites: None (foundation paper) }
}
```
---
