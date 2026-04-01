# Independent Anomaly Evidence for the Cabibbo Doublet
## Three experiments, two roads, one particle. The data was already there. The connection was not.

**Registry:** [@HOWL-PHYS-19-2026]

**Series Path:** [@HOWL-PHYS-1-2026] → [@HOWL-PHYS-2-2026] → [@HOWL-PHYS-6-2026] → [@HOWL-PHYS-7-2026] -> [@HOWL-PHYS-8-2026] -> [@HOWL-PHYS-9-2026] -> [@HOWL-PHYS-10-2026] -> [@HOWL-PHYS-11-2026] -> [@HOWL-PHYS-12-2026] -> [@HOWL-PHYS-13-2026] -> [@HOWL-PHYS-14-2026] -> [@HOWL-PHYS-15-2026] -> [@HOWL-PHYS-17-2026] -> [@HOWL-PHYS-18-2026] -> [@HOWL-PHYS-19-2026]

**Date:** April 1 2026

**Domain:** Precision Flavor Physics, Beyond Standard Model Evidence

**DOI:** 10.5281/zenodo.zzz

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

**Backed by:** Anomaly data matrix (web-search verified), sin2_theta_w_1.py (9/9 checks), DATA-3 (32/32 checks)

---

## Abstract

Three independent experimental anomalies — the CKM first-row unitarity deficit (2.5-4σ), the forward-backward b-quark asymmetry at LEP (~3σ), and the Higgs signal strength excess at the LHC (~2σ) — each independently point to a vector-like quark doublet in the (3,2,1/6) representation at the TeV scale. These anomalies were identified by precision flavor physics groups between 2019 and 2024 using data from nuclear beta decays, the LEP electron-positron collider, and the LHC proton-proton collider — three different experiments at three different facilities across three different decades. Separately, exact rational arithmetic on gauge coupling beta coefficients (PHYS-15) identifies the same (3,2,1/6) representation as the minimal single-multiplet fix for gauge coupling unification. Neither community knew about the other's method. The gap ratio path determines the representation and the unification scale M_GUT = 10^15.5 GeV. The anomaly path determines the mass window (1.5-6 TeV) and the mixing structure (|V_ub'| ≈ 0.045). Together they specify a concrete particle — the Cabibbo Doublet — with testable predictions at both the energy frontier and the intensity frontier. This paper documents the anomaly evidence, the mass window, the extended CKM matrix, and the convergence of two independent roads on one particle. The data was already there. The connection was not.

---

## 1. What the CKM Matrix Is and Why Unitarity Matters

Quarks interact through the weak nuclear force, but the quarks that feel the weak force are not the same as the quarks that have definite masses. The relationship between these two sets of quarks is described by the Cabibbo-Kobayashi-Maskawa (CKM) matrix — a 3×3 matrix introduced by Cabibbo in 1963 for two generations and extended by Kobayashi and Maskawa in 1973 to three.

The CKM matrix element V_ij describes the strength of the weak-force transition between up-type quark i and down-type quark j. The element V_ud governs the transition between the up quark and the down quark — the process responsible for nuclear beta decay, where a neutron (udd) converts to a proton (uud) by emitting an electron and an antineutrino. V_us governs the transition between the up quark and the strange quark — the process responsible for kaon decays. V_ub governs the transition to the bottom quark — measured in B meson decays.

The CKM matrix must be unitary. This is not an approximation or a model assumption — it is a consequence of quantum mechanics. Probability must be conserved: if an up quark transitions to some down-type quark, the probabilities of transitioning to each possible down-type quark must sum to 1. For the first row:

|V_ud|² + |V_us|² + |V_ub|² = 1.00000 (required by quantum mechanics)

This sum has been measured with increasing precision for decades. V_ud is known to 0.03% from superallowed nuclear beta decays — transitions between nuclei that differ only in the replacement of a proton by a neutron, with no change in spin or parity. These are the cleanest beta decays in nature, measured in over a dozen different nuclear species. V_ud is also measured independently from neutron beta decay, though with slightly lower precision. V_us is known to 0.2% from kaon decays — both leptonic (K → μν) and semileptonic (K → πeν). V_ub is known to 5% from B meson decays but contributes negligibly to the sum (|V_ub|² ≈ 0.000015).

The sum does not equal 1.

---

## 2. Anomaly 1: The Cabibbo Angle Anomaly

The measured first-row CKM unitarity sum:

|V_ud|² + |V_us|² + |V_ub|² = 0.99798 ± 0.00038

This is a deficit of 0.00202 from unity — a deviation of 2.5 to 4 standard deviations depending on which theoretical inputs are used.

The significance range requires explanation. The extraction of V_ud from nuclear beta decay requires radiative corrections — quantum electrodynamic and electroweak loop calculations that relate the measured decay rate to the underlying CKM element. In 2018-2019, improved calculations of these corrections (particularly the inner radiative corrections to the axial-vector coupling) shifted the extracted V_ud, changing the deficit significance. Belfatto, Beradze, and Berezhiani at the University of L'Aquila first identified the deficit as a potential signal of new physics in 2019 (arXiv:1906.02714, published as Eur. Phys. J. C 80, 149, 2020), reporting a deviation exceeding 4σ using the radiative correction inputs available at that time. Subsequent recalculations have moderated the significance. Kitahara (Int. J. Mod. Phys. A 39, 2442011, 2024, arXiv:2407.00122) reports approximately 3σ in a current status review, stating that "the prime candidate for the UV completion is the vector-like quark extension." Cirigliano et al. (JHEP 03, 033, 2024, arXiv:2311.00021) confirm approximately 3σ tension in a global Standard Model Effective Field Theory analysis with updated inputs.

The deficit persists across all analyses. Its precise significance is debated. Its existence is not.

Berezhiani's interpretation (2020): if a fourth quark exists and mixes with the known quarks, the 3×3 CKM matrix that experimentalists measure is actually a 3×4 submatrix of a larger 4×4 unitary matrix. The apparent deficit in the first row is not a violation of quantum mechanics — it is the missing fourth column. The missing probability |V_ub'|² ≈ 0.00202 goes to the new quark, giving |V_ub'| ≈ 0.045. This is a small but nonzero mixing — comparable in magnitude to |V_cb| ≈ 0.041, the mixing between the charm and bottom quarks.

For this mixing to be large enough to produce the observed deficit while keeping the Yukawa coupling perturbative, the new quark must have a mass below approximately 6 TeV. The new quark must be vector-like — a chiral fourth generation (where left-handed and right-handed components transform differently under the weak force) is excluded by Higgs boson coupling measurements at the LHC. A vector-like quark (where both chiralities transform identically) evades this constraint because it does not require the Higgs for its mass.

The natural candidate is a vector-like quark doublet in the (3,2,1/6) representation — the Cabibbo Doublet.

---

## 3. Anomaly 2: The Forward-Backward b-Quark Asymmetry at LEP

At the Large Electron-Positron Collider (LEP) at CERN, which operated from 1989 to 2000, electron-positron collisions at the Z boson mass produced pairs of quarks and leptons. The angular distribution of the produced particles is not symmetric — more particles go forward (along the electron beam direction) than backward. This forward-backward asymmetry, denoted A_FB, is a sensitive probe of the coupling structure between the Z boson and the fermions it produces.

For b quarks produced in Z → bb̄:

Measured: A_FB^b = 0.0992 ± 0.0016 (LEP Electroweak Working Group, Phys. Rept. 427, 257, 2006)

SM prediction: approximately 0.1038

Discrepancy: approximately 2.9σ

This anomaly has persisted for over 25 years. It was first noted when the LEP experiments published their final combined electroweak results. Every subsequent review of electroweak precision data — by the LEP Electroweak Working Group, the Particle Data Group, and independent analyses — notes it as an unresolved tension. No Standard Model correction (higher-order QCD, QED radiation, non-perturbative effects) has resolved it.

A critical feature of this anomaly: it cannot be remeasured with current experiments. LEP was decommissioned in 2000 to make way for the LHC in the same tunnel. No electron-positron collider currently operates at the Z pole. The measurement is frozen at 0.0992 ± 0.0016 until a future Z factory (the proposed FCC-ee at CERN or CEPC in China) is built — neither is approved or funded as of this writing. This makes A_FB^b simultaneously the most persistent anomaly in particle physics (25+ years, unchanged) and the most frustrating (no path to direct resolution from the same observable).

The connection to the PHYS-12 electroweak computation in this series: PHYS-12 computed R_b (the fraction of Z decays producing bb̄ pairs) at tree level + leading Δρ correction and found a 1.6% overshoot compared to the LEP measurement (R_b computed = 0.2197, measured = 0.2163, ratio 1.016). This overshoot is consistent with the known missing t-b-W vertex correction — a one-loop diagram where the top quark circulates in a triangle connecting the b quark to the W and Z bosons. This correction reduces the effective b-quark coupling to the Z and brings R_b into agreement with data. But A_FB^b is more sensitive than R_b to the details of the Z-b-b coupling, and even after all SM corrections, the residual A_FB^b tension remains.

The Cabibbo Doublet resolves this through a different mechanism than the SM vertex correction. If the Cabibbo Doublet mixes with the b quark (through the mixing angle θ₃₄), it modifies the right-handed b-quark coupling to the Z boson. In the SM, the right-handed coupling g_bR is small and determined by the b quark's hypercharge alone: g_bR = −(1/3)sin²θ_W ≈ −0.077. The VL mixing shifts g_bR by an amount proportional to sin²(θ₃₄). This shift moves A_FB^b from the SM prediction toward the measured value. The same mixing angle θ₃₄ that fixes A_FB^b is constrained independently by B⁰-B̄⁰ meson mixing and electroweak precision data — and consistent values exist.

---

## 4. Anomaly 3: The Higgs Signal Strength Excess

The Higgs boson, discovered at the LHC in 2012, is produced primarily through gluon-gluon fusion — a process where two gluons from the colliding protons interact through a triangle loop of top quarks (the heaviest SM particle, with the strongest Higgs coupling) to produce a Higgs boson. The overall production rate times decay rate, normalized to the SM prediction, is the signal strength μ.

Measured: μ ≈ 1.06-1.10 (ATLAS and CMS combined, LHC Run 1 at 7+8 TeV and Run 2 at 13 TeV)

SM prediction: μ = 1.000

Excess: approximately 2σ

This must be stated honestly: a 2σ excess is not significant by particle physics standards. Discovery requires 5σ. An excess at 2σ has roughly a 5% probability of arising from statistical fluctuation alone. It could vanish with more data from LHC Run 3 and the HL-LHC upgrade. It is the weakest of the three anomalies.

But it is consistent with the Cabibbo Doublet interpretation through two mechanisms. First, the VL quark doublet circulates in the gluon-gluon-Higgs triangle loop alongside the top quark. Since the VL doublet carries color charge (it is an SU(3) triplet), it contributes to this loop and slightly enhances the gluon-fusion production cross section. Second, if the VL doublet mixes with the b quark, it reduces the effective bottom Yukawa coupling. Since H → bb̄ is the dominant Higgs decay mode (approximately 58% branching ratio), reducing this rate increases the branching ratios to all other channels (γγ, ZZ, WW, ττ), enhancing the apparent signal strength measured in those channels.

Cheung, Lee, and Tseng first identified the VL doublet as a candidate for the Higgs excess in combination with A_FB^b (Phys. Lett. B 798, 134983, 2019, arXiv:1901.05626).

---

## 5. Each Anomaly Uses a Different Property

A critical observation: each anomaly is resolved by a different quantum number of the Cabibbo Doublet.

The CKM unitarity deficit is resolved by the weak doublet structure — the SU(2) quantum number. A weak doublet can mix with SM quarks through the CKM mechanism, expanding the 3×3 matrix to 4×3. A color singlet without weak charge could not do this.

The A_FB^b anomaly is resolved by the Z-b-b vertex modification — which requires both color charge (to be a quark that mixes with b) and weak charge (to modify the Z coupling). The mixing angle θ₃₄ is a different parameter from the CKM mixing angle θ₁₄.

The Higgs signal strength excess is resolved by the color triplet in the gluon-fusion loop — the SU(3) quantum number. A colorless particle would not contribute to gg → H.

No single quantum number resolves all three anomalies. The CKM deficit needs weak charge. The A_FB^b needs both weak and color. The Higgs excess needs color. The full representation (3,2,1/6) — color triplet, weak doublet, hypercharge 1/6 — is required to address all three simultaneously. This is why the anomaly literature converged specifically on a VL quark doublet, not on a VL lepton or a VL singlet quark.

---

## 6. The Three-Anomaly Fit

Cheung, Keung, Lu, and Tseng (JHEP 05, 117, 2020, arXiv:2001.02853) performed the first simultaneous global fit of a vector-like quark doublet in the down sector against all three anomalies. Their analysis constrained the model against: the CKM first-row unitarity condition, the Z-pole observables A_FB^b, R_b, and the total hadronic Z width Γ_had, the electroweak oblique parameters S and T, B⁰-B̄⁰ meson mixing, the decay B⁺ → π⁺ℓ⁺ℓ⁻, the decay B⁰ → μ⁺μ⁻, and direct LHC searches for VL quarks.

Result: viable parameter space exists. A single VL quark doublet at the TeV scale simultaneously reduces all three tensions while satisfying every other experimental constraint. The fit to data with the VL doublet is better than the SM fit without it.

Belfatto and Trifinopoulos (Phys. Rev. D 108, 035022, 2023, arXiv:2302.14097) further demonstrated what they called "the remarkable role of the vectorlike quark doublet" — showing that the tree-level mixing that fixes CKM unitarity simultaneously generates the right oblique T parameter correction, connecting the Cabibbo Angle Anomaly to the electroweak precision data in a single framework.

Belfatto and Berezhiani (JHEP 10, 079, 2021, arXiv:2103.05549) comprehensively examined the flavor-changing and SM precision limits, concluding that "an extra vector-like weak doublet can in principle resolve all tensions."

---

## 7. The Mass Window

The Cabibbo Doublet mass is not determined by the gap ratio analysis (PHYS-15). The gap ratio identifies the representation (3,2,1/6) and the unification scale M_GUT = 10^15.5 GeV, but the mass is a free parameter — it is Level 2, supplied by the universe through measurement. The mass window comes entirely from independent experimental constraints.

Lower bound: M > 1.5 TeV. CMS and ATLAS at the LHC have searched for pair-produced vector-like quarks in Run 2 data. Pair production proceeds through the strong force (gluon fusion and quark-antiquark annihilation) and depends only on the mass and the color charge — not on mixing angles. The absence of any excess in multi-lepton, multi-b-jet final states excludes VL quark doublet masses below approximately 1.5 TeV.

Upper bound: M < approximately 6 TeV. If the Cabibbo Doublet is responsible for the CKM unitarity deficit, the mixing element |V_ub'| ≈ 0.045 requires the Yukawa coupling to be y ≈ M_VL × |V_ub'| / v, where v = 246 GeV is the electroweak vacuum expectation value. For the Yukawa coupling to remain perturbative (y < 4π), the mass cannot exceed approximately 6 TeV. Belfatto and Berezhiani (2020) derive this bound. Branco et al. (JHEP 07, 099, 2021, arXiv:2103.13409) derive a slightly weaker bound of approximately 7 TeV for a VL up-type quark variant.

Combined window: 1.5 TeV < M < 6 TeV.

This is narrow — less than half a decade in energy. The HL-LHC (operating through approximately 2040) will extend the pair production reach to approximately 2-3 TeV. If the Cabibbo Doublet is in the lower half of its window, the HL-LHC discovers it. If it is in the upper half, a future higher-energy collider (the proposed FCC-hh at 100 TeV) would be needed for pair production, though single production at the HL-LHC can probe higher masses if the mixing angle is large enough.

The complementarity of the two paths is sharp here. The gap ratio analysis provides the representation and M_GUT but says nothing about the mass. The anomaly analysis provides the mass and mixing but says nothing about unification. Neither path alone specifies the particle completely. Together they do.

---

## 8. The Extended CKM Matrix

Adding the Cabibbo Doublet to the down-type quark sector extends the CKM matrix from 3×3 to 3×4. The Standard Model matrix:

|  | d | s | b |
|---|---|---|---|
| u | 0.974 | 0.224 | 0.004 |
| c | 0.224 | 0.974 | 0.041 |
| t | 0.009 | 0.040 | 0.999 |

First-row sum: |V_ud|² + |V_us|² + |V_ub|² = 0.998 (deficit)

The extended matrix with the Cabibbo Doublet (b'):

|  | d | s | b | b' |
|---|---|---|---|---|
| u | V_ud | V_us | V_ub | V_ub' ≈ 0.045 |
| c | V_cd | V_cs | V_cb | V_cb' |
| t | V_td | V_ts | V_tb | V_tb' |

First-row sum: |V_ud|² + |V_us|² + |V_ub|² + |V_ub'|² = 1.000 (unitarity restored)

The deficit 0.00202 is absorbed by |V_ub'|² ≈ 0.00202.

The extension introduces six new parameters, all Level 2 (supplied by measurement, not by the gap ratio integers):

The mass M_VL (1.5-6 TeV from the mass window).

The mixing angle θ₁₄ — mixing with the first generation. This is the primary mixing responsible for the CKM unitarity deficit. |V_ub'| ≈ sin(θ₁₄) ≈ 0.045. It is measured through precision nuclear beta decay (V_ud) and kaon decay (V_us).

The mixing angle θ₂₄ — mixing with the second generation. Constrained by kaon physics: K⁰-K̄⁰ mixing and the rare decay K → πνν̄ (measured by NA62 at CERN).

The mixing angle θ₃₄ — mixing with the third generation. This is the mixing responsible for the A_FB^b correction. It modifies the Z-b-b vertex and is constrained by LEP data, B⁰-B̄⁰ mixing, and B meson rare decays.

Two new CP-violating phases δ₁ and δ₂. These appear in the extended CKM matrix and contribute to CP violation in the quark sector beyond the single SM phase. They are constrained by the neutron electric dipole moment (currently measured at less than 10⁻²⁶ e·cm) and by CP asymmetries in B meson decays.

What this means operationally: in every nuclear beta decay measured since the 1950s, in every kaon decay measured since the 1960s, a fraction |V_ub'|² ≈ 0.2% of the transition amplitude has been leaking into the Cabibbo Doublet instead of the three known down-type quarks. This leakage is the unitarity deficit. It has been present in every measurement but was too small to notice until the experimental precision improved to the 0.04% level — which happened in the late 2010s with improved radiative corrections.

---

## 9. The Two Roads

The gap ratio path and the anomaly path arrive at the same (3,2,1/6) representation through completely independent methods from completely independent data.

The gap ratio path begins with three numbers measured at one energy scale: α_em = 1/137.036, sin²θ_W = 0.23122, and α_s = 0.1180, all at M_Z = 91 GeV (DATA-3). It computes the SM beta coefficients b₁ = 41/10, b₂ = −19/6, b₃ = −7 from the gauge group, constructs the gap ratio 218/115 = 1.896, compares it to the measured 1.358, and enumerates 15 single-multiplet extensions in exact Fraction arithmetic. The elimination cascade — gap ratio distance plus proton decay — leaves two survivors: the MSSM (gap 7/5 = 1.400) and the Cabibbo Doublet (gap 38/27 = 1.407). The entire computation uses no floating point. The output is a representation and a unification scale.

The anomaly path begins with four observables measured across six orders of magnitude in energy: V_ud from nuclear beta decays at the MeV scale, V_us from kaon decays at the GeV scale, A_FB^b from the Z pole at 91 GeV, and μ_Higgs from the LHC at the TeV scale. It identifies three independent tensions with the SM, performs global χ² fits with numerical minimization, and finds that a single VL quark doublet at 1-6 TeV resolves all three while satisfying every other constraint. The output is a representation, a mass window, and a mixing structure.

The gap ratio path determines the representation and M_GUT but says nothing about the mass or mixing. The anomaly path determines the mass and mixing but says nothing about M_GUT or proton decay. Neither group read the other's papers. Neither method uses the other's data. The gap ratio works at 10^15 GeV. The anomalies work at 10³ GeV. Different data, different methods, different communities, different journals, different decades. They arrive at the same (3,2,1/6) from opposite ends of the energy spectrum.

The connection was discovered during this session through a web search to verify whether the Cabibbo Doublet identified by the gap ratio had any independent experimental support. It does. The anomaly literature has been pointing at (3,2,1/6) since 2019.

---

## 10. Historical Context

The pattern of multiple independent lines of evidence converging on a single particle before its discovery has occurred repeatedly in particle physics.

The charm quark was identified before discovery by two independent arguments: the GIM mechanism (Glashow, Iliopoulos, Maiani 1970) required a fourth quark to cancel flavor-changing neutral currents in K meson decays, and the observed K⁰-K̄⁰ mixing rate was consistent with a fourth quark below approximately 2 GeV. The charm quark was discovered in 1974 at approximately 1.5 GeV.

The top quark was identified before discovery by three independent arguments: the KM matrix (1973) required three generations for CP violation (an integer argument), the b quark (discovered 1977) needed an isospin partner for anomaly cancellation (a representation theory argument), and the electroweak precision parameter Δρ required a heavy quark with mass approximately 170 GeV (a precision data argument). The top quark was discovered in 1995 at 176 GeV.

The W and Z bosons were identified before discovery by the SU(2)×U(1) gauge theory (Weinberg 1967, Salam 1968), which predicted their masses from sin²θ_W and G_F. Neutral current interactions consistent with the Z were observed in 1973. The W and Z were discovered in 1983 at the predicted masses.

The Cabibbo Doublet has two independent theoretical identifications (gap ratio arithmetic and anomaly fitting) and three independent experimental anomalies. This level of convergence — multi-path, multi-anomaly, multi-decade — has historically preceded experimental confirmation. This is not a prediction that the Cabibbo Doublet will be found. It is a historical observation that this pattern has been predictive in the past.

---

## 11. What This Paper Does Not Claim

This paper does not claim the three anomalies constitute discovery. In particle physics, discovery requires 5σ significance. The strongest anomaly (CKM deficit) is 2.5-4σ. The weakest (Higgs excess) is 2σ. Three anomalies at these levels constitute evidence, not proof.

This paper does not claim the CKM deficit is settled science. The significance ranges from 2.5σ to 4σ depending on which radiative correction calculations are used for nuclear beta decay. The debate is active as of 2024. The deficit persists across all analyses, but its precise significance is not resolved.

This paper does not claim A_FB^b proves new physics. It is a 25-year-old measurement from a decommissioned experiment with no prospect of improvement from the same observable until a future Z factory is built. It is the most persistent tension in electroweak data, but persistence alone does not equal proof.

This paper does not claim the Higgs excess is significant. At 2σ, it has a 5% probability of being a statistical fluctuation. It could vanish with LHC Run 3 data.

This paper does not claim the convergence of two roads proves the Cabibbo Doublet exists. Two independent theoretical analyses pointing to the same representation is strong evidence but not discovery. Discovery requires experimental observation — either direct production at the LHC or proton decay detection at Hyper-Kamiokande.

This paper does not claim the gap ratio and anomaly communities should have connected their work earlier. The gap ratio analysis works at 10^15 GeV energy scales and appears in the gauge unification literature. The anomaly analyses work at 10³ GeV and appear in the precision flavor physics literature. The connection is non-obvious and spans 12 orders of magnitude in energy. Different communities, different conferences, different journals.

---

## 12. What This Paper Seeds

The mapping between mixing angles and anomalies — θ₁₄ for the CKM deficit, θ₃₄ for A_FB^b — enables a future cross-check computation. Using the PHYS-12 electroweak infrastructure, compute the Z-b-b vertex correction from VL-b mixing as a function of θ₃₄. Determine for what θ₃₄ the computed A_FB^b matches the LEP measurement 0.0992. Then check: is this θ₃₄ consistent with the B-meson mixing constraints? Is the simultaneously required θ₁₄ ≈ 0.045 consistent with the CKM deficit? If all constraints are simultaneously satisfiable, the Cabibbo Doublet passes a cross-check between the Z-pole sector, the flavor sector, and the unitarity sector.

The extended CKM matrix structure enables analysis of rare processes. The tree-level FCNC from the extended mixing predicts specific rates for K → πνν̄ (testable at NA62) and B → K*μμ (testable at LHCb). These rates depend on the mixing angles θ₂₄ and θ₃₄, which are not yet measured but are constrained by existing data.

The mass window 1.5-6 TeV constrains the LHC search strategy and the Cabibbo Doublet's contribution to precision observables. If the mass is below approximately 2-3 TeV, the HL-LHC will produce Cabibbo Doublet pairs at observable rates.

The connection between the beam and bottle neutron lifetime measurements (~2.3σ discrepancy) and the CKM deficit is speculative but worth noting: if the Cabibbo Doublet modifies V_ud, it modifies the neutron lifetime extraction. A future analysis could check whether a consistent value of θ₁₄ simultaneously explains the CKM deficit and reduces the beam/bottle tension. This is not a finding — it is an open question.

---

## 13. Summary

Three experiments across three decades produced three anomalies that each point to a vector-like quark doublet in the (3,2,1/6) representation at the TeV scale. The CKM first-row unitarity deficit (2.5-4σ, identified 2019-2020 by Belfatto, Berezhiani, and independently fitted by Cheung, Keung, Lu, Tseng) uses the weak doublet structure to expand the CKM matrix. The forward-backward b-quark asymmetry at LEP (~3σ, persistent since 2000) uses the Z-b-b vertex modification from VL-b mixing. The Higgs signal strength excess (~2σ, the weakest anomaly) uses the color triplet in the gluon-fusion loop. No single quantum number resolves all three. The full (3,2,1/6) is required.

Independently, exact rational arithmetic on gauge coupling beta coefficients identifies the same (3,2,1/6) as the minimal single-multiplet fix for gauge coupling unification (gap ratio 38/27 = 1.407, verified by the GUT script, 9/9 checks pass). The gap ratio path gives the representation and M_GUT = 10^15.5. The anomaly path gives the mass (1.5-6 TeV) and the mixing (|V_ub'| ≈ 0.045). Together they specify the Cabibbo Doublet: a concrete particle with known quantum numbers, bounded mass, constrained mixing, and testable predictions at the LHC (direct production), Belle II (CKM precision), and Hyper-Kamiokande (proton decay, 2027-2037).

The three anomalies are Level 2 — measured by experiments, supplied by the universe. The gap ratio identification is Level 1 — forced by exact rational arithmetic on the gauge group integers. The convergence of Level 1 and Level 2 on the same representation from independent starting points is the evidence documented in this paper. The data was already there. The connection was not.

---

## Appendix: Verification and Sources

All anomaly measurements and paper citations verified by web search during this session. Source provenance:

| Citation | Journal | arXiv | Verified |
|---|---|---|---|
| Belfatto, Beradze, Berezhiani (2020) | Eur. Phys. J. C 80, 149 | 1906.02714 | Yes |
| Cheung, Keung, Lu, Tseng (2020) | JHEP 05, 117 | 2001.02853 | Yes |
| Cheung, Lee, Tseng (2019) | Phys. Lett. B 798, 134983 | 1901.05626 | Yes |
| Belfatto, Berezhiani (2021) | JHEP 10, 079 | 2103.05549 | Yes |
| Belfatto, Trifinopoulos (2023) | Phys. Rev. D 108, 035022 | 2302.14097 | Yes |
| Kitahara (2024) | Int. J. Mod. Phys. A 39 | 2407.00122 | Yes |
| Cirigliano et al. (2024) | JHEP 03, 033 | 2311.00021 | Yes |
| Branco et al. (2021) | JHEP 07, 099 | 2103.13409 | Yes |
| LEP EWWG (2006) | Phys. Rept. 427, 257 | — | Yes |

Gap ratio numbers from the GUT running script (sin2_theta_w_1.py), 9/9 checks pass. Cabibbo Doublet gap ratio = 38/27 = 1.407, distance 0.049, M_GUT = 10^15.5.

R_b overshoot from the electroweak script (electro_weak.py), 14/14 checks pass. R_b computed = 0.2197, measured = 0.2163, ratio = 1.016.

All measured values from DATA-3 (123 entries, 32/32 consistency checks pass).

---

*PHYS-19: Independent Anomaly Evidence for the Cabibbo Doublet. Three experiments, two roads, one particle. The data was already there. The connection was not. Published April 1, 2026. This paper is never edited after publication.*

---

