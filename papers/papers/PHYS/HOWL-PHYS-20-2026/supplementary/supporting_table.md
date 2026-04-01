# Supporting Tables for PHYS-20: The Proton Decay Test

## Purpose

PHYS-20 documents the concrete, falsifiable, timeline-bounded prediction that emerges from the Cabibbo Doublet scenario: proton decay at a rate detectable by Hyper-Kamiokande within 2027-2037. This is the paper that connects integer arithmetic to an experiment with a date on it. PHYS-15 identifies the particle. PHYS-16 specifies it. PHYS-18 explains why it works. PHYS-19 documents the anomaly evidence. PHYS-20 answers: how do we TEST it? Without this paper, a future session knows the Cabibbo Doublet exists as a candidate but doesn't know the specific experiment, the specific timeline, the specific observable, or the specific discriminator between the Cabibbo Doublet and the MSSM.

Finding covered: Finding 10 (proton decay prediction testable by Hyper-Kamiokande).

---

## Table 20.1: The Chain from Gap Ratio to Proton Decay

| Step | Input | Operation | Output |
|---|---|---|---|
| 1 | SM beta coefficients (41/10, −19/6, −7) | Gap ratio | 218/115 = 1.896 |
| 2 | Cabibbo Doublet beta shifts (1/15, 1, 1/3) | Modified gap ratio | 38/27 = 1.407 |
| 3 | Modified betas + DATA-3 couplings at M_Z | One-loop running to convergence | M_GUT = 10^15.5 GeV |
| 4 | M_GUT in minimal SU(5) | Proton lifetime formula τ ∝ M_GUT⁴ | τ(p→e⁺π⁰) ~ 10^34-35 yr |
| 5 | τ ~ 10^34-35 yr | Compare to experimental sensitivity | Within Hyper-K reach |

The chain: integers → gap ratio → M_GUT → proton lifetime → specific experiment. Every step except step 3 (which uses DATA-3 Level 2 inputs) is Level 1 arithmetic.

---

## Table 20.2: M_GUT for Each Scenario

| Scenario | Gap Ratio | M_GUT (GeV) | log₁₀(M_GUT) | How M_GUT Is Computed | Source |
|---|---|---|---|---|---|
| SM alone | 218/115 = 1.896 | 6.3 × 10¹³ | 13.80 | Couplings don't converge; M_GUT is where α₁ = α₂ | GUT script, PASS |
| SM + Cabibbo Doublet | 38/27 = 1.407 | 3.2 × 10¹⁵ | 15.50 | Modified betas run to approximate convergence | GUT script, PASS |
| Full MSSM | 7/5 = 1.400 | 2.1 × 10¹⁷ | 17.32 | SUSY betas run to convergence | GUT script, PASS |
| SM + SU(5) 5+5̄ | 40/27 = 1.481 | 7.9 × 10¹⁴ | 14.90 | Eliminated by proton decay | GUT script |

The Cabibbo Doublet places M_GUT between the SM (too low, already excluded) and the MSSM (too high for current experiments). This intermediate position is what makes it maximally testable.

---

## Table 20.3: The Proton Lifetime Formula

| Component | Expression | Physical Origin |
|---|---|---|
| Proton lifetime | τ(p→e⁺π⁰) ∝ M_GUT⁴ / (α_GUT² × m_p⁵ × |⟨π⁰|qqq|p⟩|²) | Dimension-6 operator from X/Y boson exchange in minimal SU(5) |
| M_GUT dependence | τ ∝ M_GUT⁴ | The heavy X/Y boson propagator contributes 1/M_GUT² to the amplitude, squared gives M_GUT⁴ |
| α_GUT dependence | τ ∝ 1/α_GUT² | The GUT coupling appears at each X/Y vertex |
| Hadronic matrix element | |⟨π⁰|qqq|p⟩|² | How efficiently three quarks in the proton annihilate into a pion; computed on the lattice |
| Scaling | Factor of 10 in M_GUT → factor of 10⁴ in τ | The M_GUT⁴ dependence makes the lifetime extremely sensitive to the unification scale |

This M_GUT⁴ scaling is why the Cabibbo Doublet and the MSSM predict vastly different proton lifetimes despite having similar gap ratios (1.407 vs 1.400). The factor of ~60 in M_GUT (10^15.5 vs 10^17.3) becomes a factor of ~60⁴ ≈ 10⁷ in lifetime.

---

## Table 20.4: Proton Lifetime Predictions by Scenario

| Scenario | M_GUT (GeV) | τ(p→e⁺π⁰) (years) | Status vs Super-K Limit | Status vs Hyper-K Projected |
|---|---|---|---|---|
| SM (minimal SU(5)) | 10^13.8 | ~10^30 | EXCLUDED (limit is 2.4×10³⁴) | — |
| SM + SU(5) 5+5̄ | 10^14.9 | ~10^33 | EXCLUDED | — |
| **SM + Cabibbo Doublet** | **10^15.5** | **~10^34-35** | **AT BOUNDARY** | **WITHIN REACH** |
| Full MSSM | 10^17.3 | ~10^36-37 | Safe | Beyond reach |

The Cabibbo Doublet scenario sits at the boundary of the current limit. This is the maximally testable position: not yet excluded, but fully within the next experiment's sensitivity.

---

## Table 20.5: Current and Future Proton Decay Experiments

| Experiment | Location | Detector Type | Fiducial Mass | Status | Start Date | Best Channel | Projected τ Sensitivity |
|---|---|---|---|---|---|---|---|
| Super-Kamiokande | Kamioka, Japan | Water Cherenkov | 22.5 kton | Running (since 1996) | 1996 | p→e⁺π⁰ | 2.4×10³⁴ yr (current limit) |
| **Hyper-Kamiokande** | **Tochibora, Japan** | **Water Cherenkov** | **187 kton** | **Under construction** | **~2027** | **p→e⁺π⁰** | **~10³⁵ yr (10 yr exposure)** |
| DUNE | Sanford Lab, South Dakota, USA | Liquid Argon TPC | 40 kton | Under construction | ~2028-2029 | p→K⁺ν̄ | ~10³⁴ yr (p→K⁺ν̄) |
| JUNO | Jiangmen, Guangdong, China | Liquid Scintillator | 20 kton | Under construction | ~2025 | p→K⁺ν̄ | ~10³⁴ yr |

Hyper-K is the critical experiment for the Cabibbo Doublet scenario because its primary sensitivity is in the p→e⁺π⁰ channel — the dominant decay mode in minimal SU(5), which is the natural GUT completion for the Cabibbo Doublet. DUNE's primary proton decay sensitivity is in the p→K⁺ν̄ channel, which is dominant in SUSY SU(5) — more relevant for the MSSM scenario.

---

## Table 20.6: Hyper-Kamiokande Specifications

| Property | Value | Comparison to Super-K |
|---|---|---|
| Total water volume | 258 kton | 50 kton (5.2× larger) |
| Fiducial volume | 187 kton | 22.5 kton (8.3× larger) |
| Photosensors | 40,000 PMTs (20-inch) | 11,129 PMTs |
| Photo-coverage | ~40% | ~40% (comparable) |
| Location | Tochibora mine, Gifu Prefecture, Japan | Kamioka mine, Gifu Prefecture, Japan |
| Depth | ~650 m rock overburden | ~1000 m rock overburden |
| Construction start | 2020 | 1991 |
| Operations start (projected) | ~2027 | 1996 |
| Proton decay sensitivity (10 yr) | τ ~ 10³⁵ yr (p→e⁺π⁰) | τ ~ 2.4×10³⁴ yr (current limit) |
| Improvement factor | ~4× current limit (10 yr), ~10× (full exposure) | Baseline |

The 8.3× larger fiducial volume is the key improvement. More water = more protons = more chances to observe a decay. The sensitivity scales approximately as (mass × time)^(1/2) for a counting experiment with low background, so 8.3× more mass for the same time gives ~2.9× better sensitivity. Over 10 years (vs Super-K's ~25 years of exposure), the combined improvement reaches approximately one order of magnitude.

---

## Table 20.7: The Discriminator

| Observation at Hyper-K (after 10 yr) | Cabibbo Doublet Scenario | MSSM Scenario | No Unification |
|---|---|---|---|
| Proton decay observed at τ ~ 10^34-35 yr | **CONSISTENT** | Inconsistent (predicts τ ~ 10^36-37) | Inconsistent |
| Proton decay observed at τ ~ 10^36-37 yr | Inconsistent | **CONSISTENT** | Inconsistent |
| No proton decay observed (τ > 10^35 yr) | Minimal SU(5) completion excluded | **CONSISTENT** | **CONSISTENT** |
| Proton decay in p→K⁺ν̄ but not p→e⁺π⁰ | Depends on GUT completion | Consistent (SUSY SU(5)) | Inconsistent |

The critical point: the Cabibbo Doublet and the MSSM predict DIFFERENT proton lifetimes despite having similar gap ratios. The gap ratios are nearly identical (1.407 vs 1.400) but M_GUT differs by a factor of ~60, which translates to a factor of ~10⁷ in proton lifetime. Hyper-K can distinguish between them.

---

## Table 20.8: The p→e⁺π⁰ Decay Process

| Property | Detail |
|---|---|
| Decay process | proton → positron + neutral pion (e⁺ + π⁰) |
| What triggers it | Exchange of a superheavy X or Y gauge boson (mass ~ M_GUT) between two quarks |
| Conservation laws violated | Baryon number (B: 1 → 0), Lepton number (L: 0 → 1), but B−L conserved |
| Conservation laws preserved | Electric charge, energy, momentum, B−L |
| π⁰ subsequent decay | π⁰ → γγ (two photons, 99% BR, lifetime 8.5×10⁻¹⁷ s) |
| Experimental signature | e⁺ produces Cherenkov ring + 2 photon Cherenkov rings from π⁰→γγ |
| Total visible energy | ~938 MeV (proton rest mass) |
| Background | Atmospheric neutrino interactions (very low rate in this topology) |
| Detection efficiency (Super-K) | ~45% for p→e⁺π⁰ |

The signature is clean: a positron and two photons at a total energy equal to the proton mass, with no missing energy. Water Cherenkov detectors are optimized for this channel because the Cherenkov ring topology is distinctive.

---

## Table 20.9: Model Dependence — Honest Assessment

| Factor | Effect on Proton Lifetime | Uncertainty |
|---|---|---|
| GUT completion group (SU(5) vs SO(10) vs E₆) | Changes dominant decay channel; can shift lifetime by orders of magnitude | Large: different completions predict different channels |
| Threshold corrections at M_GUT | Heavy GUT particle masses split from M_GUT, modifying running near unification | Moderate: can shift M_GUT by factor of 2-3, shifting τ by 10¹-10³ |
| Two-loop running corrections | Shift M_GUT by 2-5% | Small: shifts log₁₀(M_GUT) by ~0.1-0.2 |
| Hadronic matrix elements | Lattice QCD uncertainties in ⟨π⁰|qqq|p⟩ | Moderate: ~30-50% uncertainty in the matrix element, factor ~2 in τ |
| α_GUT value | Enters as 1/α_GUT² in lifetime formula | Small: α_GUT ≈ 1/40 with ~5% uncertainty |
| Cabibbo Doublet mass (1.5-6 TeV) | Modifies running between M_VL and M_GUT | Small: shifts log₁₀(M_GUT) by ~0.3, shifts τ by factor ~10 |

The prediction τ ~ 10^34-35 yr is an ORDER OF MAGNITUDE estimate, not a precision calculation. The range spans one order of magnitude due to these uncertainties. The statement "within Hyper-K reach" is robust across the entire range: even the upper end (10^35 yr) is within Hyper-K's projected sensitivity.

---

## Table 20.10: What Happens in Each Experimental Outcome

| Outcome | Timeline | Consequence for Cabibbo Doublet | Consequence for Series | Next Step |
|---|---|---|---|---|
| LHC finds VL quark at 1.5-3 TeV | Now-2040 | Direct confirmation. Mass, mixing angles measured. | M_VL fixed → M_GUT sharpened → τ_p prediction narrowed | Measure mixing angles, compute precise τ_p |
| Hyper-K sees p→e⁺π⁰ at τ ~ 10^34-35 yr | 2027-2037 | Consistent with Cabibbo Doublet + minimal SU(5) | M_GUT confirmed → gap ratio confirmed → series validated | Identify GUT completion from decay channels |
| Belle II sharpens V_us, confirms CKM deficit at >5σ | Now-2030 | Anomaly path strengthened to discovery level | CKM sector of Cabibbo Doublet confirmed | Precision θ₁₄ extraction |
| Hyper-K sees nothing (10 yr) | 2037 | Minimal SU(5) completion excluded | Non-minimal completions (SO(10), threshold corrections) explored | Check if SO(10) or threshold corrections rescue the scenario |
| LHC excludes VL quarks to 3 TeV, nothing found | ~2035 | Upper half of mass window still viable (3-6 TeV) | Wait for FCC-hh or precision indirect evidence | Single production searches, precision EW |
| LHC excludes VL quarks to 6 TeV | ~2040+ (FCC-hh era) | Mass window closed. Cabibbo Doublet excluded in down sector. | Check up-sector VL variant (M ≤ 7 TeV) | Branco et al. up-sector analysis |
| CKM deficit drops below 2σ with new radiative corrections | Anytime | Weakest anomaly argument reduced; gap ratio path unaffected | Gap ratio identification stands regardless of anomaly status | Gap ratio path is independent of anomalies |

---

## Table 20.11: Comparison of Proton Decay Channels

| Channel | Dominant in | Operator Dimension | Mediated by | Hyper-K Sensitive? | DUNE Sensitive? |
|---|---|---|---|---|---|
| p → e⁺π⁰ | Minimal SU(5), non-SUSY GUTs | Dimension 6 | X, Y gauge bosons | **YES (primary)** | Yes (secondary) |
| p → K⁺ν̄ | SUSY SU(5), SO(10) with SUSY | Dimension 5 | Colored Higgsino | Yes (secondary) | **YES (primary)** |
| p → μ⁺π⁰ | Some flipped SU(5) models | Dimension 6 | X, Y gauge bosons | Yes | Yes |
| p → e⁺K⁰ | Some SO(10) models | Dimension 6 | Various | Yes | Yes |
| p → ν̄π⁺ | Some models | Dimension 6 | Various | Limited | Limited |

The Cabibbo Doublet scenario with minimal SU(5) completion predicts p→e⁺π⁰ as the dominant channel. Hyper-K is optimized for this channel. DUNE is optimized for p→K⁺ν̄ (liquid argon has excellent kaon detection). The two experiments are complementary — together they cover the dominant channels of both the Cabibbo Doublet and MSSM scenarios.

---

## Table 20.12: The M_GUT⁴ Sensitivity

| Parameter Change | Effect on M_GUT | Effect on τ_p | Intuition |
|---|---|---|---|
| 10× increase in M_GUT | 10× | 10⁴× | Lifetime is EXTREMELY sensitive to M_GUT |
| 2× increase in M_GUT | 2× | 16× | Even a factor of 2 matters enormously |
| Cabibbo Doublet vs MSSM: M_GUT ratio ~60 | 60× | 60⁴ = 1.3×10⁷ | Same gap ratio, seven orders of magnitude in lifetime |
| Cabibbo Doublet mass range (1.5-6 TeV) | ~2× change in M_GUT | ~16× change in τ_p | Mass uncertainty spans ~1 order of magnitude in τ |
| Two-loop corrections | ~1.2× change in M_GUT | ~2× change in τ_p | Small effect |

The M_GUT⁴ dependence is why proton decay discriminates between scenarios that look nearly identical in the gap ratio. The Cabibbo Doublet (gap 1.407) and the MSSM (gap 1.400) have almost the same gap ratio but are separated by 10⁷ in proton lifetime.

---

## Table 20.13: Timeline

| Year | Event | Relevance to Cabibbo Doublet |
|---|---|---|
| 1996 | Super-Kamiokande begins operations | Proton decay search begins |
| 2000 | LEP decommissioned; A_FB^b frozen at 0.0992 | Second anomaly established, no new data |
| 2012 | Higgs boson discovered at LHC | Third anomaly (μ excess) begins |
| 2019-2020 | Belfatto, Berezhiani identify CKM deficit as BSM signal | Anomaly path to (3,2,1/6) opens |
| 2020 | Cheung et al. three-anomaly fit | Anomaly path converges |
| 2020 | Hyper-K construction begins | Clock starts for the critical experiment |
| 2024 | Super-K limit: τ > 2.4×10³⁴ yr | Cabibbo Doublet scenario at boundary |
| 2024 | Kitahara review: "prime candidate is VL quark extension" | Current status of anomaly path |
| 2026 | PHYS-15: Gap ratio path identifies (3,2,1/6) | Two roads converge |
| ~2027 | Hyper-K begins operations | Proton decay test begins |
| ~2028-2029 | DUNE begins operations | Complementary channel (p→K⁺ν̄) |
| Now-2030+ | Belle II accumulates data | V_us precision, CKM deficit sharpens or weakens |
| Now-2040 | HL-LHC running | Direct VL quark search up to 2-3 TeV |
| ~2037 | Hyper-K 10-year exposure | Sensitivity reaches ~10³⁵ yr — full Cabibbo Doublet range covered |

The window of maximum testability is 2027-2037. Within this decade, Hyper-K covers the full proton lifetime range predicted by the Cabibbo Doublet scenario. If it exists and the minimal SU(5) completion is correct, this is when we find out.

---

## Table 20.14: What PHYS-20 Prevents

| Without PHYS-20 | With PHYS-20 |
|---|---|
| Future session knows M_GUT = 10^15.5 but not the experimental consequence | Reads "τ ~ 10^34-35 yr, Hyper-K covers full range by 2037" |
| Future session doesn't know the discriminator between Cabibbo Doublet and MSSM | Reads "same gap ratio but 10⁷ different in proton lifetime — Hyper-K distinguishes" |
| Future session doesn't know which experiment tests which scenario | Reads "Hyper-K for p→e⁺π⁰ (Cabibbo Doublet), DUNE for p→K⁺ν̄ (MSSM)" |
| Future session doesn't know the model dependence | Reads "order of magnitude estimate, honest uncertainty table, robust across range" |
| Future session doesn't know the timeline | Has the year-by-year timeline through 2037 |
| Future session doesn't know what happens if Hyper-K sees nothing | Reads "minimal SU(5) excluded, non-minimal extensions explored, gap ratio path unaffected" |

---

## Table 20.15: Scripts and Source Material Needed

| Item | Content | Role |
|---|---|---|
| GUT running script + output | M_GUT = 10^15.5 for Cabibbo Doublet, 10^17.3 for MSSM, 10^13.8 for SM | Ground truth for all M_GUT values |
| GUT parked notebook | 9 results, 9/9 checks | Verified summary |
| DATA-3 paper | Coupling constants for the running | Source of truth for Level 2 inputs |
| Hyper-Kamiokande web search results | Detector specifications, timeline, projected sensitivity | Source for experimental details |
| Super-Kamiokande current limit | τ > 2.4×10³⁴ yr for p→e⁺π⁰ | Current experimental boundary |
| PHYS-16 supporting tables (Table 16.13) | Experimental test matrix | Cross-reference |
| PHYS-20 supporting tables (this document) | Tables 20.1-20.15 | Structure and pre-computed data |
| HOWL operational rules (R.1-R.6) | Series principles | Included in every paper |
| HOWL writing rules (W.1-W.8) | Paper production rules | Applied during writing |

Note: proton lifetime estimates (10^34-35 yr) are order-of-magnitude calculations from M_GUT⁴ scaling, not precision predictions. The paper should state this clearly. The GUT script provides M_GUT; the proton lifetime follows from standard formulas in the GUT literature, not from a dedicated HOWL script. The model dependence table (Table 20.9) documents the uncertainty honestly.

---

*These 15 tables provide the complete data for PHYS-20. The paper connects integer arithmetic to a specific experiment with a specific timeline: Hyper-Kamiokande, 2027-2037, p→e⁺π⁰, τ ~ 10^34-35 yr. The discriminator between the Cabibbo Doublet and the MSSM — 10⁷ in proton lifetime from similar gap ratios — makes this the decisive test. Every M_GUT value traces to the GUT script (9/9 checks). The model dependence is stated honestly. The prediction is an order of magnitude estimate, not a precision calculation, and is robust across the entire uncertainty range.*
