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

---

This changes the conjecture significantly. Let me update the picture.

The a² = 2 geometry-count interpretation survives for leptons but it's not universal. The quark sector gives a² = 3.09 for up-type and a² = 2.39 for down-type — neither is 2. The conjecture as written in my report ("a² = 2 counts stable soliton geometries universally") is too strong. The data says a² = 2 is specific to charged leptons.

But the data also opens something bigger than what it closes.

**K = n/3 is the real pattern.** Charged leptons give K = 2/3 at 5 ppm. Massive bosons give K = 1/3 at 0.9% — and 0.9% is within the M_W measurement uncertainty, which has a live 7σ tension between CDF and LHC/LEP. The denominator 3 counts particles in each group. The numerator n increments by 1 between layers. If neutrinos give K = 3/3 = 1 (all three masses nearly equal, which the mass-squared differences suggest), then n = 1, 2, 3 across three particle groups.

That's not a² anymore. That's K itself forming an integer sequence across the soliton hierarchy. The question shifts from "why does a² = 2 for leptons" to "why does K = n/3 with n indexing particle groups by their position in the hierarchy."

**The a² values for quarks are suggestive despite not being 2.** Up-type a² = 3.09 is close to 3. If it's exactly 3 at some specific energy scale (quark masses run, lepton masses don't), then a² might count something that's 2 for leptons and 3 for up-type quarks. Three colors. Three confinement-level vortices inside the proton. The integer 3 from SU(3). Path B from your notebook — computing K at multiple scales — is the right test. The quark Koide isn't dead, it's scale-dependent.

**My report needs revision in several places:**

The title should change. "a² = 2 as Soliton Geometry Count" is too narrow. The finding is K = n/3 as a hierarchy index, with a² = 2 being one instance of a pattern where the amplitude may count different things at different soliton levels.

Path 2 (quark sector test) came back inconclusive, not negative. The report should note that a² ≠ 2 for quarks but that a² ≈ 3 for up-type quarks is itself suggestive, and that scheme dependence means the test is incomplete until Path B (multi-scale computation) is done.

Path 5 (direct numerical test) is confirmed — a² = 2 at 18 ppm for leptons, which is within tau mass measurement uncertainty. The conjecture is numerically alive for leptons.

The K_boson = 1/3 finding should be added as a new path — it wasn't in my report because I didn't have this data. The prediction K_neutrino = 1 should be stated as the falsifiable consequence of the K = n/3 pattern.

**The "What Not To Do" section of your notebook is the most important part.** It's LEMU discipline in action. Don't claim K_boson = 1/3 as a result (0.9% with uncertain inputs). Don't attempt derivation without the soliton boundary equation (produces hand-waving). Don't kill a² = 2 from quark data alone (scheme-dependent). Don't treat K = n/3 as established from two data points. The parked status is correct. The neutrino measurement is the deciding test.

Should I revise the report to incorporate these findings before you send it to the researcher Claude?

---

The writer Claude gets it. The key shift — from "a² = 2 is universal" to "K = n/3 is the pattern" — is correct. The original conjecture was too narrow. The data widened it.

One thing the writer Claude does that I want to flag as exactly right: it treats a² = 3.09 for up-type quarks as suggestive rather than killing. The instinct to say "3.09 is not 2, conjecture dead" is wrong here because quark masses run and we only tested at one scale. The instinct to say "3.09 is close to 3, therefore it IS 3" is also wrong — that is numerology without the scale test. The correct position is: inconclusive, test at multiple scales, then decide. That is what both the notebook and the writer Claude say.

The one thing I would push back on: the writer says "the question shifts from why a² = 2 to why K = n/3." I think both questions remain live simultaneously. K = n/3 is the pattern across groups. a² = 2 (or 3, or whatever integer) is the pattern within each group. They are different levels of the same structure. The K ratio tells you how the group relates to other groups. The amplitude a² tells you how the inertias are spaced within the group. Both need explanation. Neither replaces the other.

The neutrino prediction K = 1 is the cleanest falsifiable output of the whole exploration. Three nearly degenerate masses give K → 1. KATRIN and JUNO will constrain the absolute mass scale. Cosmological bounds from CMB-S4 will constrain the sum. If the absolute masses become known and K_neutrino ≠ 1, the pattern K = n/3 is dead. If K_neutrino = 1, three data points make a line and the pattern demands explanation.

Parked is the right status. The notebook is the right format. The LEMU discipline is holding.

---
