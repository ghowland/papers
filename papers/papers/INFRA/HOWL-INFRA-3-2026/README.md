# An Example OpsDB Schema

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

This paper specifies a relational schema demonstrating the OpsDB design from HOWL-INFRA-2-2026. The schema is comprehensive across the operational substrate: site and location, identity, hardware, virtualization (with nested megavisor instances spanning bare metal, virtual machines, containers, and pods), Kubernetes, cloud resources, services and packages, runners, schedules, policies, configuration, cached observation, authority pointers, documentation metadata, monitoring and alerting, evidence, change management, audit, and the schema's record of itself.

The naming convention used throughout is the Database Schema Naming Convention, abbreviated DSNC. DSNC rules: all names are singular (`company_employee`, never `company_employees`); all names are lower_case_with_underscores; names are composed hierarchically with prefixes going from more specific to less specific (`web_site`, `web_site_widget`); foreign keys are named as `referenced_table_id` (`company_id` references `company.id`), with role prefixes when multiple FKs to the same table coexist (`vendor_company_id`, `service_company_id`); type suffixes are mandatory for time and date fields (`_time` for DATETIME, `_date` for DATE); booleans use tense prefixes (`is_active` for present, `was_activated` for past). Reserved fields appear on every table where applicable: `id`, `created_time`, `updated_time`, `parent_id` for self-hierarchy. Governance and admin metadata fields carry a leading underscore (`_requires_group`, `_audit_chain_hash`, `_retention_policy_id`) to keep them visually separated from the operational vocabulary the schema models. The benefits at scale: collisions are prevented by structural rules rather than memorized vocabulary; the schema is self-documenting; new domains slot into existing prefix trees without reorganization. DSNC has its own specification document; this paper applies the convention without re-specifying it.

The schema is presented as relational tables with explicit foreign keys, type constraints, and reserved fields. Storage engine choice, API implementation, deployment patterns, and runner implementations are out of scope; INFRA-2 covered those design boundaries. This paper demonstrates that the OpsDB design produces a workable, comprehensive schema; it does not prescribe the canonical schema. The reader is assumed to have read INFRA-1 (taxonomy of mechanisms, properties, principles) and INFRA-2 (OpsDB design); no other prior reading is assumed.

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
@article{ HOWL-INFRA-3-2026,
  title={ An Example OpsDB Schema },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20008274},
  url = {https://zenodo.org/record/20008274},
  note={Howland Archive: HOWL-INFRA-3-2026. Prerequisites: None (foundation paper) }
}
```
---
