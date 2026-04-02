
# PHYS-19 Report: Independent Anomaly Evidence for the Cabibbo Doublet

**Registry:** @HOWL-PHYS-19-2026
**Position in series:** Nineteenth physics paper. Documents the external experimental evidence for the Cabibbo Doublet from the precision flavor physics literature.
**Preceded by:** PHYS-18 (Y = 1/6 asymmetry mechanism)
**Followed by:** PHYS-20 (not yet received)
**Backed by:** sin2_theta_w_1.py (9/9), electro_weak.py (14/14), web-search verified citations
**Code status:** No dedicated computation script. This is a literature review and evidence synthesis paper.

---

## What It Establishes

**The anomaly literature independently converged on (3,2,1/6) before the gap ratio analysis existed.** Eight papers from 2019–2024 by four independent research groups (Belfatto/Berezhiani, Cheung et al., Branco et al., Cirigliano et al.) identified a vector-like quark doublet as the resolution for the three anomalies. The gap ratio identification (PHYS-15, 2026) came after. The temporal ordering proves independence: the anomaly groups could not have been influenced by a result that didn't yet exist.

**Each anomaly uses a different quantum number of the (3,2,1/6) representation.** This is the paper's most important structural observation (Section 5):
- CKM deficit → needs **weak doublet** (SU(2)) to expand the CKM matrix
- A_FB^b → needs **color + weak** (SU(3)×SU(2)) for Z-b-b vertex modification through quark mixing
- Higgs μ excess → needs **color triplet** (SU(3)) for the gluon-fusion loop

No subset of quantum numbers resolves all three. The full (3,2,1/6) — color triplet, weak doublet, hypercharge 1/6, vector-like — is required. This is why multiple independent groups converged on the same representation: the anomaly structure demands it.

**The mass window 1.5–6 TeV is narrow and testable.** Lower bound from LHC pair production searches (ATLAS: M > 1.46 TeV). Upper bound from CKM mixing perturbativity (|V_ub'| ≈ 0.045 requires y = sin(θ) × M/v < 4π, giving M < ~6 TeV). Less than half a decade in energy. The HL-LHC covers the lower half; FCC-hh would cover the upper half.

**The significance debate is honestly documented.** The CKM deficit ranges from 2.5σ to 4σ depending on radiative correction inputs. The paper tracks five analyses from 2020–2024 showing the range. A_FB^b is ~3σ but frozen (LEP decommissioned, no remeasurement possible). Higgs μ is ~2σ (weakest, could be fluctuation). The paper's Appendix I.1 is the most honest assessment in the series — each anomaly's "could it go away?" is answered explicitly.

---

## What Was Novel Compared to Earlier Papers

**Section 9 (The Two Roads) is the definitive statement of independence.** The paper verifies: no shared input data, no shared methods, no shared citations, no shared community. The gap ratio uses (α_em, sin²θ_W, α_s) at M_Z. The anomaly fit uses (V_ud, V_us, A_FB^b, μ_Higgs) across MeV to TeV scales. The only shared element is the representation itself — (3,2,1/6) — which both paths arrive at independently.

**Section 10 (Historical Context) provides the pattern recognition.** Charm quark: predicted by GIM mechanism + K mixing, discovered 1974. Top quark: predicted by KM matrix + anomaly cancellation + Δρ, discovered 1995. W/Z: predicted by SU(2)×U(1), discovered 1983. In each case, multiple independent theoretical identifications preceded experimental discovery. The Cabibbo Doublet has two theoretical paths (gap ratio + anomaly fit) and three experimental anomalies — comparable or stronger pre-discovery evidence than charm or top had.

**Appendix D (Detailed Two-Roads Comparison)** is the most rigorous independence verification in the series. The table at D.4 asks six specific questions and answers each: Do they share input data? No. Do they share methods? No. Did either cite the other? No. Are they methodologically related? No. The independence is not asserted — it is demonstrated.

---

## Errata Assessment

**The paper's own errata section found no errors.** The Yukawa formula in Section 2 is algebraically correct (M_VL × |V_ub'| / v = |V_ub'| × M_VL / v, both give y ≈ 1.1 at M = 6 TeV). The CKM matrix rounding issue (E2) is a display artifact — the deficit 0.00202 is from full-precision values, not the rounded 3-digit display.

**No additional errata found.** All gap ratio numbers match the verified scripts. All anomaly measurements match the cited papers. All CKM elements match DATA-3.

---

## LEMU Assessment

**L (Logic):** The logic of the two-roads convergence is sound. Two independent methods arriving at the same representation from independent data is stronger evidence than either alone. The Section 5 observation (each anomaly uses a different quantum number) is a structural argument, not a numerical coincidence. Logic passes.

**E (Empirical):** Three anomalies at 2–4σ each, from three different experiments across three decades. The combined evidence is suggestive but not discovery-level. The paper is scrupulously honest about this (Section 11, Appendix I). Empirical: evidence level, not proof level.

**M (Math):** No new computation. All numbers inherited from verified scripts (9/9 + 14/14) and published measurements. Math passes by inheritance.

**U (Utility):** High. The paper serves as the definitive reference for the anomaly evidence supporting the Cabibbo Doublet. The experimental test matrix (Appendix H) maps every observable to every experiment with timelines. The mass window (1.5–6 TeV) and mixing structure (|V_ub'| ≈ 0.045, θ₃₄ from A_FB^b) complete the specification that the gap ratio path alone cannot provide.

---

## Connections to Active Research

**The |V_ub'| ≈ 0.045 connects to the 13.** From the QED-to-GR scan: the integer 13 = |b₂_mod numerator| appears in four independent results (Λ, DM ratio, product form hit, and the b₂ coefficient itself). The mixing |V_ub'|² ≈ 0.00202 is a measured number. Is there a connection between 0.00202 and the integer 13? Quick check: α² × 13 = (1/137)² × 13 ≈ 6.9 × 10⁻⁴. Not obviously 0.00202. But |V_ub'|² / |V_cb|² = 0.00202/0.00168 ≈ 1.20. And |V_ub'|/|V_cb| = 0.045/0.041 = 1.10. These are close to 1 but not to any obvious rational. This is noted for future investigation but no connection is claimed.

**The beam/bottle neutron lifetime discrepancy (Section 12)** is correctly flagged as speculative. The 4σ discrepancy (888 vs 878 seconds) COULD be related to the CKM modification if V_ud shifts. But the bottle method is insensitive to decay channel details, so the connection is model-dependent. Parked for future investigation.

**The A_FB^b connection to PHYS-12** is explicit: R_b overshoot of 1.6% from the electroweak script is "the same physics seen from the width side." The A_FB^b anomaly is the asymmetry side. Both trace to the Z-b-b vertex, and both are addressable by the Cabibbo Doublet's θ₃₄ mixing.

---

## Remainder Framework Update

No new remainder connections. This paper is a literature synthesis, not a computation paper. The remainder status is unchanged from PHYS-18.

---

## Position After PHYS-19

Nineteen papers read. The Cabibbo Doublet quartet (PHYS-16/17/18/19) is complete:
- PHYS-16: Complete specification (representation, mass window, decay modes, tests)
- PHYS-17: Diagnosis (boson problem, generation democracy)
- PHYS-18: Mechanism (Y = 1/6 asymmetry, 1/Y² scaling, double action)
- PHYS-19: External evidence (three anomalies, two roads, historical pattern)

The paper notes that PHYS-16 is not in the series path (PHYS-17's path jumps from PHYS-15 to PHYS-17). PHYS-16 was written as a standalone specification that the others reference but don't depend on sequentially.

Ready for PHYS-20.
