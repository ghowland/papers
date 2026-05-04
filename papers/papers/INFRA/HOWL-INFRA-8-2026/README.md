# The OpsDB Shared Library Suite

**AI Usage Disclosure:** Only the top metadata, figures, MD to PDF conversion formatting, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

The shared library suite is the framework that keeps OpsDB-coordinated runners small and consistent. INFRA-4 introduced the suite as a category and made the case that runners stay small because the libraries do the heavy lifting; this paper specifies what the libraries are, what contracts they expose, what the library/runner boundary looks like, and how the suite enforces policy at world-side action time. The suite is a contract specification, not an implementation; multiple implementations of the same library can coexist (different languages, different transports), but they expose the same contract that runners are written against.

The paper specifies the contract for each library category: the OpsDB API client (the mandatory client every runner uses), world-side substrate libraries (Kubernetes operations, cloud operations, host operations, container/registry operations, secret backend access, identity provider operations, monitoring authority operations, authority pointer resolution), coordination and resilience libraries (retry, circuit breaker, hedger, bulkhead, failover routing), observation libraries (logging, metrics, tracing — mandatory and uniform across the runner population), notification libraries (email, chat, page, ticket creation), templating and rendering libraries (deliberately dumb), git and version-control libraries.

The structural payoff is two-sided policy enforcement. The API gate (INFRA-5) enforces policy at OpsDB write time. The library suite enforces policy at world-side action time. Runner declarations — `runner_*_target` bridges, `runner_capability` rows, `runner_report_key` rows — are the input to both. A runner cannot, through any path, perform an action outside its declared scope: OpsDB writes are caught at the gate, world-side actions are caught at the library. The library suite is the operational realization of "one way to do each thing" applied to runner-world interaction.

What this paper does not specify: implementation languages, specific function signatures, deployment topologies for the libraries themselves, or specific runner implementations that consume them.

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
@article{ HOWL-INFRA-8-2026,
  title={ The OpsDB Shared Library Suite },
  author={Howland, Geoffrey},
  journal={Zenodo},
  year={2026},
  doi = {10.5281/zenodo.20017988},
  url = {https://zenodo.org/record/20017988},
  note={Howland Archive: HOWL-INFRA-8-2026. Prerequisites: None (foundation paper) }
}
```
---
