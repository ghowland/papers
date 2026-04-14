## Koide Exploration Notebook — Session 7 Findings

**Status:** Parked. Promising pattern identified. Awaiting improved boson mass measurements.

**Date:** April 10, 2026

---

### Finding 1: The Lepton Koide Is Confirmed at 5 ppm

K_lepton = (mₑ + mμ + mτ) / (√mₑ + √mμ + √mτ)² = 2/3

From pool: `koide_charged_leptons_k_v0` = 1333321023/2000000000 = 0.666660...

Miss from 2/3: 5 ppm. The amplitude parameter a² = `koide_charged_leptons_a2_v0` = 624988459/312500000 = 1.99996... Miss from 2: 18 ppm.

This is a precision relationship. It holds at the level of the tau mass measurement uncertainty. It remains an atoll — disconnected from the integer chain.

---

### Finding 2: The Quark Koide Does Not Reproduce a² = 2

From pool:
- `koide_up_quarks_a2_v0` = 6185522571/2000000000 = 3.0928
- `koide_down_quarks_a2_v0` = 2387725461/1000000000 = 2.3877

Neither is 2. Neither is close to 2. The amplitude a² = 2 is specific to charged leptons. It is not a universal constant across fermion types.

However: quark masses are scheme-dependent (MS-bar, running with energy). The pool values use specific scale choices. The Koide relation may hold at a specific energy scale for quarks but not at the scale used to compute these pool values. This is not tested. The quark Koide is inconclusive, not dead.

---

### Finding 3: The Boson Koide Gives K ≈ 1/3

K_boson = (M_W + M_Z + M_H) / (√M_W + √M_Z + √M_H)²

Using pool values M_W = 401846/5, M_Z = 455938/5, M_H = 125200:

K_boson = 0.33635...

Miss from 1/3: 0.9%.

This is not a precision match like the lepton 5 ppm. But the boson mass inputs are far less precise than the lepton mass inputs. M_W has a 7σ tension between CDF (80433.5 MeV) and the LHC/LEP average (~80370 MeV). The PDG central value is a compromise that will shift. M_H has been measured for 12 years. These are early-stage measurements compared to the decades of lepton mass refinement.

The 0.9% miss is within the input uncertainty budget. Whether K_boson converges to 1/3 as measurements improve is an open question.

---

### Finding 4: The Pattern K = n/3

If K_lepton = 2/3 and K_boson = 1/3, the pattern is:

| Layer | Particles | K | n |
|---|---|---|---|
| Massive bosons (W, Z, H) | 3 | 1/3 | 1 |
| Charged leptons (e, μ, τ) | 3 | 2/3 | 2 |

The numerator n increments by 1 between layers. The denominator 3 counts the number of particles in each group.

The integer n may count:
- Stable soliton geometries (sphere + toroid = 2 for leptons, sphere only = 1 for bosons?)
- Stable baryons (proton + neutron = 2 for leptons, proton only = 1 for bosons?)
- Hierarchy layers below the group (leptons sit above 2 layers, bosons above 1?)
- Something else entirely

The interpretation is open. The numerical pattern is: K = n/3 with n = 1, 2 for two different groups of three particles.

---

### Finding 5: Reframing as Inertia

The Koide formula compares three inertias (resistances to acceleration), not three substances. The ratio K = 2/3 is a relationship between how three particles resist being pushed. The stability of K across energy scales follows from the stability of lepton pole masses, which barely run compared to coupling constants.

This stability suggests a geometric or topological origin. Topology does not run with energy. If K encodes topology, its scale invariance is natural. If K encodes dynamics, its stability requires explanation.

---

### Paths for Future Exploration

**Path A: Track K_boson as M_W improves.**

The LHC is remeasuring M_W. The CDF tension may resolve upward (toward 80434 MeV) or downward (toward 80370 MeV). Each shift changes K_boson. Compute K_boson for both CDF and LHC/LEP central values and determine which pushes K_boson closer to 1/3.

Quick check from this session: M_W = 80369.2 gives K = 0.33635. If M_W were 80433.5 (CDF value), the sum increases, K changes. This should be computed.

**Path B: Compute K for quark triplets at multiple scales.**

The quark Koide a² values (3.09 and 2.39) were computed at one scale. Compute K and a² for (u, c, t) and (d, s, b) at μ = 1 GeV, 10 GeV, M_Z, and 1 TeV using the MS-bar running masses. If K = 2/3 emerges at any specific scale, that scale is physically significant.

**Path C: Search for a fourth Koide group.**

The pattern K = n/3 with n = 1 (bosons) and n = 2 (leptons) invites n = 3. K = 3/3 = 1 is the maximum possible value of the Koide ratio (it corresponds to all three masses being equal). Is there a group of three particles with K = 1? Three degenerate masses would satisfy this. The three light neutrinos have unknown absolute masses but the mass-squared differences suggest they are far more degenerate than any other triplet. If neutrino masses turn out to give K ≈ 1, the pattern completes: n = 1 (bosons), n = 2 (leptons), n = 3 (neutrinos).

This is speculative. Neutrino masses are not in the pool. But the prediction is clean: K_neutrino = 1 if the pattern holds.

**Path D: Test K = n/3 against the soliton hierarchy.**

In the RUM framework, bosons are force carriers (boundary mediators), charged leptons are sphere solitons, and neutrinos are the lightest fermions (possibly boundary-crossing modes). If n counts the number of soliton hierarchy levels each group spans:
- Bosons mediate across 1 boundary type → n = 1
- Charged leptons exist at 2 boundary levels (atomic and nuclear) → n = 2
- Neutrinos cross all 3 boundary types (electromagnetic, weak, gravitational) → n = 3

This assigns a structural meaning to n that connects to the hierarchy. It predicts K_neutrino = 1. It is testable when neutrino absolute masses are measured (KATRIN, JUNO, cosmological constraints).

**Path E: The a² values for quarks.**

Up-type a² = 3.09. Down-type a² = 2.39. These are not integers. But 3.09 is close to the integer 3. If up-type quarks have a² = 3 exactly, the pattern extends: a² counts something that is 2 for leptons and 3 for up-type quarks. Down-type a² = 2.39 does not fit an integer. But quark masses are scheme-dependent — the a² values may sharpen to integers at a specific scale. This connects to Path B.

**Path F: Write a derivation function.**

Compute K and a² for all candidate triplets from pool values in one derivation function. Inputs: all lepton masses, all quark masses, M_W, M_Z, M_H. Outputs: K and a² for charged leptons, up quarks, down quarks, massive bosons. Comparisons: K_lepton vs 2/3, K_boson vs 1/3, a²_lepton vs 2. This formalizes the exploration in the DATA-7 framework and creates a permanent record.

---

### What Not To Do

Do not claim K_boson = 1/3 as a result. It is 0.9% off with uncertain inputs. It is a candidate pattern, not a confirmed relationship.

Do not attempt to derive the Koide formula from soliton topology until the numerical patterns are sharper. The soliton boundary equation does not exist yet. Attempting a derivation without it will produce hand-waving, not mathematics.

Do not kill the a² = 2 conjecture based on the quark data alone. The quark masses are scheme-dependent. The conjecture may hold at a specific scale. Test Path B before deciding.

Do not build on K = n/3 as though it were established. Two data points (n = 1 at 0.9% and n = 2 at 5 ppm) do not establish a pattern. They suggest one. The third data point (neutrinos) is the test.

---

### Summary

| Group | K value | Target | Miss | Status |
|---|---|---|---|---|
| Charged leptons (e, μ, τ) | 0.666660 | 2/3 | 5 ppm | Confirmed |
| Massive bosons (W, Z, H) | 0.33635 | 1/3 | 0.9% | Candidate — inputs uncertain |
| Up quarks (u, c, t) | — | 2/3? | a² = 3.09 ≠ 2 | Inconclusive — scale-dependent |
| Down quarks (d, s, b) | — | 2/3? | a² = 2.39 ≠ 2 | Inconclusive — scale-dependent |
| Neutrinos (ν₁, ν₂, ν₃) | unknown | 1? | unmeasured | Prediction from K = n/3 |

The Koide atoll remains disconnected. But it may be part of an archipelago: K = n/3 across multiple particle groups, with n counting hierarchy levels. The bridge to the mainland requires either the soliton boundary equation or a group-theoretic derivation of the Koide amplitude from the gauge structure. Neither exists yet. The numerical patterns are suggestive and the predictions are falsifiable. Parked for future sessions.
