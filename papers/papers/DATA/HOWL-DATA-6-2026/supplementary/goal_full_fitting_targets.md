## FULL FITTING TARGET BOARD

The goal: every SM observable derivable from the minimum set of measured inputs plus integer laws. When a value moves from "measured" to "derived," the parameter count drops. When a derivation chain connects two previously independent measurements, the system gains predictive power.

### CURRENT STATE: What We Can Derive

| Output | From | Via | Miss | Status |
|---|---|---|---|---|
| α⁻¹ | a_e | QED A₁-A₅ Newton inversion | 3.3 ppb | DERIVED |
| R∞ | a_e, m_e | α² m_e c/(2h) | 8.0 ppb | DERIVED |
| a₀ | a_e, m_e | ℏ/(m_e c α) | 4.0 ppb | DERIVED |
| μ₀ | a_e | 2αh/(ce²) | 4.0 ppb | DERIVED |
| m_τ | m_e, m_μ | Koide K=2/3 | 0.006% | CONDITIONAL |
| θ_QCD | none | Energy minimization | exact | DERIVED |
| DM/baryon | b₂_mod integers | (22/13)π | 0.073% | DERIVED (if integers structural) |
| gap_CD | SM betas + CD | 38/27 | 3.6% | DERIVED |
| GPS correction | G, M_earth, R, v | GR time dilation | ~1% | DERIVED |

### TARGET BOARD: What We Need

Organized by what's blocking each derivation.

---

### TIER 1: IMMEDIATE — Missing corrections to close existing chains

These are known values we need as DATA-6 nodes to improve existing derivations from ~ppb to sub-ppb.

| Target Value | What It Is | Needed For | Estimated Effect | Source | Difficulty |
|---|---|---|---|---|---|
| a_e(mass-dep, 2-loop) | μ/τ VP in electron g-2 | α extraction | +2.5 ppb | Kinoshita et al. | Easy — published |
| a_e(mass-dep, 3-loop) | Higher-order mass-dep | α extraction | +0.1 ppb | Laporta, Passera | Easy — published |
| a_e(hadronic VP, LO) | Hadronic vacuum polarization | α extraction | +1.7 ppb | Davier et al. / lattice | Easy — published |
| a_e(hadronic VP, NLO) | Next-to-leading hadronic | α extraction | -0.2 ppb | Kurz et al. | Easy — published |
| a_e(hadronic LbL) | Light-by-light scattering | α extraction | +0.3 ppb | WP 2020 | Easy — published |
| a_e(electroweak) | W/Z loop corrections | α extraction | +0.03 ppb | Czarnecki et al. | Easy — published |
| A₅(resolved) | 5-loop coefficient | α extraction | ±0.5 ppb | Volkov vs AHKN | Hard — 5σ tension |
| Laporta convention map | C81/C83 → A₄/A₅ | α at 4900-digit precision | unknown | Investigation | Medium |

**When complete:** α from a_e at <1 ppb. R∞, a₀, μ₀ at <2 ppb. Four CODATA values from two measurements.

---

### TIER 2: NEAR-TERM — Extend existing derivation chains

| Target Value | What It Is | Needed For | What Derives It | Current Status | Difficulty |
|---|---|---|---|---|---|
| α(M_Z) | Running coupling at Z pole | Electroweak predictions | VP running from α(0) | Framework in PHYS-9 | Medium — hadronic VP limits |
| sin²θ_W(predicted) | Weak mixing angle | EW sector derivation | GUT running from α(M_Z) | 1.2% miss at 1-loop | Medium — needs 2-loop |
| α_s(predicted) | Strong coupling | QCD sector | Two-loop CD unification | 0.33% miss (platform) | Medium — fix two-loop bug |
| M_GUT | Unification scale | Proton decay prediction | One-loop CD crossing | 10^15.54 GeV | Done (1-loop) |
| τ_proton | Proton decay lifetime | Hyper-K prediction | M_GUT⁴ scaling | 10^34-35 yr | Medium — threshold corrections |
| M_W(predicted) | W mass from sin²θ_W | EW precision test | M_W = M_Z cos θ_W | Not yet attempted | Medium |
| Γ_Z(predicted) | Z width | EW precision test | From α(M_Z) + sin²θ_W | Not yet attempted | Hard — needs full EW |
| a_μ(predicted) | Muon g-2 | BSM test | QED series + mass-dep + hadronic | Not yet attempted | Hard — hadronic dominates |

**When complete:** The electroweak sector predicted from coupling extraction + running. W mass, Z width, sin²θ_W become derived.

---

### TIER 3: MEDIUM-TERM — New derivation chains

| Target Value | What It Is | Needed For | What Would Derive It | Current Status | Difficulty |
|---|---|---|---|---|---|
| G_F(predicted) | Fermi constant | EW unification | From M_W, sin²θ_W, α | Not attempted | Hard — full EW |
| m_e/m_μ ratio | Lepton mass ratio | Koide extension | Unknown — no known law | OPEN PROBLEM | Unknown |
| m_e absolute | Electron mass in MeV | Reducing to 1 input | Unknown — no known law | OPEN PROBLEM | Unknown |
| Ω_b(predicted) | Baryon density | Cosmology from integers | Ω_DM/(DM/baryon) | Framework exists | Easy — needs normalization |
| Ω_DE(predicted) | Dark energy density | Flatness constraint | 1 - Ω_m | Framework exists | Easy — follows from Ω_m |
| H₀(predicted) | Hubble constant | Cosmology | Boundary running | Hypothesis only | Hard — N unknown |
| a₀(MOND) | MOND acceleration | Galaxy dynamics | cH₀/(8R₂) | 15% match | Medium — H₀ input needed |
| V_CKM elements | CKM matrix | Flavor physics | CD mixing angles | STAGED (6 parameters) | Hard — CD mass needed |

**When complete:** Cosmological parameters from integers. EW sector from running. CKM from CD.

---

### TIER 4: LONG-TERM — The open problems

| Target Value | What It Is | Why It's Hard | What Would Break It Open | Status |
|---|---|---|---|---|
| Yukawa couplings | All fermion masses | No known law connects them | Derivation of a²=2 from physics → Koide for all sectors | OPEN |
| CKM phase δ | CP violation | Requires CD mass + mixing | LHC detection of VL quarks | STAGED |
| Neutrino masses | ν₁, ν₂, ν₃ | Unknown mechanism (seesaw?) | DUNE / JUNO / Hyper-K oscillation | OPEN |
| Strong CP (beyond θ=0) | Why θ=0 exactly | Energy minimization only gives θ=0, not WHY | Axion detection or lattice proof | DERIVED (but shallow) |
| Cosmological constant | Λ | 120 orders of magnitude problem | Unknown | OPEN |
| Number of generations | Why N_gen = 3 | No known constraint from gauge group | Anomaly cancellation with CD? | OPEN |
| α_s from first principles | Strong coupling | Confinement wall blocks perturbative derivation | Lattice QCD at sub-percent | HARD |

---

### THE PARAMETER SCORECARD

| Parameter | SM Count | Current Status | From | Derivation |
|---|---|---|---|---|
| θ_QCD | 1 → 0 | DERIVED | none | Energy minimization |
| α (via a_e) | relabel | DERIVED | a_e | QED 5-loop Newton |
| m_τ (via Koide) | 1 → 0 | CONDITIONAL | m_e, m_μ | K=2/3 quadratic |
| R∞ | redundant | DERIVED | a_e, m_e | α² formula |
| a₀ | redundant | DERIVED | a_e, m_e | 1/α formula |
| μ₀ | redundant | DERIVED | a_e | α formula |
| sin²θ_W | 1 | PREDICTED (1.2%) | α, α_s, betas | CD 1-loop running |
| α_s | 1 | PREDICTED (0.33%) | α, sin²θ_W, betas | CD 2-loop running |
| M_W | 1 | NOT YET | sin²θ_W, M_Z | M_Z cos θ_W |
| G_F | 1 | NOT YET | M_W, sin²θ_W, α | Full EW |
| m_e | 1 | MEASURED | — | No known law |
| m_μ | 1 | MEASURED | — | No known law |
| m_u | 1 | MEASURED | — | No known law |
| m_d | 1 | MEASURED | — | No known law |
| m_s | 1 | MEASURED | — | No known law |
| m_c | 1 | MEASURED | — | No known law |
| m_b | 1 | MEASURED | — | No known law |
| m_t | 1 | MEASURED | — | No known law |
| V_us, V_cb, V_ub | 3 | MEASURED | — | CD mixing (staged) |
| δ_CKM | 1 | MEASURED | — | CD phase (staged) |
| m_H | 1 | MEASURED | — | No known law |
| DM/baryon | — | DERIVED (0.073%) | b₂_mod integers | (22/13)π |
| Ω_DM | — | PREDICTED (~21%) | integers + R₂ | (44/169)R₂ |
| H₀ | — | MEASURED | — | Running hypothesis |
| M_VL (CD mass) | +1 | STAGED [1.5-6 TeV] | — | LHC search |
| θ₁₄ (CD mixing) | +1 | STAGED [~0.045] | — | CKM deficit |
| 4 more CD params | +4 | STAGED | — | B physics, kaon, nEDM |

**Current SM count:** 19 standard → 18 (θ_QCD) → 17 (Koide conditional) → +6 CD = 23

**Derived (not counted):** α, R∞, a₀, μ₀, DM/baryon (if integers structural)

**Predicted (partial):** sin²θ_W (1.2%), α_s (0.33%), M_GUT, τ_proton

---

### THE ATTACK ORDER

| Priority | Target | Why Now | Experiment Needed |
|---|---|---|---|
| 1 | Mass-dependent + hadronic a_e corrections | Published values, just need to add as nodes | experiment_qed_full_corrections_v0 |
| 2 | Fix two-loop α_s bug | Blocks α_s prediction at 0.33% | experiment_two_loop_investigation_v0 |
| 3 | sin²θ_W from CD running | Already have 1-loop at 1.2% | experiment_sin2_prediction_v0 |
| 4 | M_W from sin²θ_W | Simple formula, big payoff | experiment_mw_prediction_v0 |
| 5 | Complete what-if scan (10 remaining) | Direct-db derivation ready | 10 more whatif experiments |
| 6 | Statistical control | BLOCKING — must compute p-value | experiment_statistical_control_v0 |
| 7 | Ω_b, Ω_m, Ω_DE flatness chain | Framework exists, needs normalization | experiment_cosmology_chain_v0 (defined) |
| 8 | α(M_Z) from VP running | PHYS-9 framework, hadronic VP limits | experiment_alpha_running_v0 |
| 9 | a_μ prediction | Ties to muon g-2 anomaly | experiment_muon_g2_v0 |
| 10 | G_F from full EW | Requires M_W + sin²θ_W + α chain | experiment_fermi_constant_v0 |

---

### THE END STATE

When everything derivable is derived, the irreducible measured inputs are:

| # | Input | What It Determines | Precision |
|---|---|---|---|
| 1 | a_e | α, R∞, a₀, μ₀ | 0.11 ppb |
| 2 | m_e | Mass scale for R∞, a₀ | 0.03 ppb |
| 3 | m_μ | m_τ (via Koide), VP thresholds | 0.002 ppm |
| 4 | Δ_had | Hadronic VP across confinement wall | 73 ppm |
| 5 | M_Z | Electroweak reference scale | 22 ppm |
| 6 | α_s or M_GUT | Strong sector (one determines the other via CD) | ~1% |
| 7-12 | 6 quark masses | No known derivation law | 0.1-30% |
| 13-16 | 4 CKM parameters | CD mixing (partially staged) | 0.1-5% |
| 17 | m_H | Higgs mass, no known law | 0.08% |
| 18 | M_VL | CD mass, LHC search | STAGED |

**18 irreducible inputs** from the universe. Everything else is integers plus these 18 numbers. That's the full fitting target. Each time one of these becomes derivable from the others (like m_τ from m_e and m_μ), the count drops by one.

The truly open problems — the ones no known law addresses — are the 6 quark masses, the Higgs mass, and why there are exactly 3 generations. Those are the universe's choices that no integer structure has yet explained.

---

Yes. Here's where we are and where the paths go.

**What we have:** 17 derived values. The derivation graph is connected across QED, electroweak, cosmology, and nuclear physics. Koide floats as an atoll.

**The paths to more:**

**Path 1: Close the existing chains (5-10 more values).** The G_F at 3% needs the v2 EW approach — flip the logic, use G_F as input, derive M_W from it. This gives a second independent M_W derivation. If both M_W paths agree, that's a consistency proof. Then sin²θ_eff from on-shell M_W. Then Γ_Z partial widths (e⁺e⁻, μ⁺μ⁻, hadronic, invisible separately — each is a derived value checkable against LEP). That's M_W(from G_F), sin²θ_eff(derived), plus 4-5 partial widths = 6-7 new values.

**Path 2: Add the a_e corrections and close α to sub-ppb (improves 4 existing values).** Six published corrections as value nodes. α goes from 3.3 ppb to <1 ppb. R∞, a₀, μ₀ improve proportionally. Not new values but dramatically better precision on existing ones. This also unblocks the muon g-2 prediction.

**Path 3: Muon g-2 (2-3 new values).** With corrected α, compute a_μ(QED) + a_μ(hadronic) + a_μ(EW) = a_μ(SM). Compare to Fermilab. That's a_μ predicted, plus the individual components as derived values. Connects to the muon g-2 anomaly — one of the biggest open questions in particle physics.

**Path 4: BBN extension (2-3 more values).** Lithium-7 abundance from the same η. Lithium is the BBN problem — the predicted Li-7/H is 3× higher than observed. Our chain would reproduce this tension, which is itself a result. Also helium-3.

**Path 5: CKM from CD mixing (3-4 new values).** The Cabibbo Doublet has 6 staged parameters (M_VL, θ₁₄, θ₂₄, θ₃₄, δ₁, δ₂). If M_VL is fixed (say 3 TeV), the CKM first-row deficit gives θ₁₄ ≈ 0.045. This derives V_ud, V_us corrections from the CD mixing matrix — connecting the gauge island to the flavor sector for the first time.

**Path 6: Proton decay lifetime (1 value).** M_GUT is already computed at 10^15.54 GeV. τ_proton = M_GUT⁴ × (known factors). Compare to Super-K bound (>10^34 yr) and Hyper-K sensitivity. One derived value testable within the next decade.

**Path 7: α_s from derived α (1 value, improved).** Currently α_s is predicted at 0.33% from the platform but 10-12% from DATA-6 (two-loop bug). Fix the bug, and α_s becomes a sub-percent derived value from the coupling running. That's a strong constraint.

**Path 8: H₀ tension (1 value, speculative).** If the Hubble running hypothesis holds (H₀ decreases with distance via boundary transit), H₀(local) and H₀(CMB) are both correct at different depths. The running parameter r comes from integer-derived VP step size. Deriving H₀(CMB) from H₀(local) + running would resolve the tension. Speculative but testable.

**The count:** 17 current + 7 (Path 1) + 3 (Path 3) + 3 (Path 4) + 4 (Path 5) + 1 (Path 6) + 1 (Path 7) + 1 (Path 8) = roughly 37 derived values. Plus the 4 improved from Path 2.

**The constraint:** each new derived value that matches its measurement reduces the free parameter space. At 17 values from 12 inputs, we have 5 more outputs than inputs. At 37 values from maybe 15 inputs, we'd have 22 more outputs than inputs. Each additional output that matches is a test the system passes. Each test it passes makes the next derivation more credible.

The system doesn't need a breakthrough to grow. It needs the same thing it's been doing: identify a measured value, find the formula that connects it to values already in the graph, write the experiment, run it, report the miss. Every value that connects is a new bridge. Every bridge enables more values. The graph grows combinatorially once enough nodes are connected.

---

## Full Fitting Attack Plan — All 8 Paths

---

### PATH 1: Close the EW chains (7 new derived values)

**Goal:** Use G_F as input (flipped logic), derive M_W independently, derive sin²θ_eff, derive individual Z partial widths.

**Experiment:** `experiment_ew_v2_v0`

**New value nodes needed:**

| Key | Value | Source | Why |
|---|---|---|---|
| `ew_gamma_z_ee_measured_v0` | 83.91 MeV | LEP EWWG | Z→e⁺e⁻ partial width |
| `ew_gamma_z_mumu_measured_v0` | 83.99 MeV | LEP EWWG | Z→μ⁺μ⁻ partial width |
| `ew_gamma_z_tautau_measured_v0` | 84.08 MeV | LEP EWWG | Z→τ⁺τ⁻ partial width |
| `ew_gamma_z_had_measured_v0` | 1744.4 MeV | LEP EWWG | Z→hadrons total |
| `ew_gamma_z_inv_measured_v0` | 499.0 MeV | LEP EWWG | Z→invisible (3ν) |
| `ew_r_l_measured_v0` | 20.767 | LEP EWWG | Γ_had/Γ_lep ratio |
| `ew_sigma_had_measured_v0` | 41.541 nb | LEP EWWG | σ⁰_had peak cross section |

**Derivations:**

| Function | Formula | Inputs from Pool | Outputs |
|---|---|---|---|
| `ew_mw_from_gf_v0` | M_W² sin²θ_W = πα/(√2 G_F) × 1/(1−Δr). Iterate: start with M_W(tree), compute Δr(M_W, m_t, m_H, α), update M_W. | G_F, α(M_Z), M_Z, m_t, m_H, π | result_mw_from_gf_v0, result_delta_r_v0 |
| `ew_sin2_eff_from_mw_v0` | sin²θ_os = 1 − M_W²/M_Z². Then sin²θ_eff = κ_Z × sin²θ_os where κ_Z is computed from M_W, not stored. | result_mw_from_gf_v0, M_Z, m_t, α(M_Z) | result_sin2_eff_from_mw_v0 |
| `ew_z_partial_widths_v0` | Γ(Z→ff̄) individually for each channel using α(M_Z), sin²θ_eff(derived), ρ, δ_vb, QCD(quarks), FSR(leptons). | α(M_Z), sin²θ_eff(derived), ρ, δ_vb, α_s, FSR | result_gamma_z_ee_v0, result_gamma_z_mumu_v0, result_gamma_z_tautau_v0, result_gamma_z_had_v0, result_gamma_z_inv_v0 |
| `ew_mw_consistency_v0` | Compare M_W(from sin²θ_W) and M_W(from G_F). Report agreement. | Both M_W values | result_mw_consistency_ppm_v0 |

**Comparisons:** M_W(from G_F) vs PDG, sin²θ_eff vs LEP, 5 partial widths vs LEP, R_l vs LEP, σ_had vs LEP, M_W consistency < 0.1%.

**New derived values:** M_W(from G_F), sin²θ_eff(derived), Γ(Z→ee), Γ(Z→μμ), Γ(Z→ττ), Γ(Z→had), Γ(Z→inv) = 7 values.

**Difficulty:** Medium. The Δr computation requires careful treatment of the full one-loop correction. The standard approach (Sirlin 1980) gives Δr = Δα − cos²θ/sin²θ × Δρ + Δr_remainder. The remainder is the hardest part — involves vertex and box diagrams.

**New value node for Δr remainder:**

| Key | Value | Source |
|---|---|---|
| `ew_delta_r_remainder_v0` | 0.0010 | Awramik et al. 2004. Non-universal remainder after Δα and Δρ are extracted. |

---

### PATH 2: Close α to sub-ppb (0 new values, 4 improved)

**Goal:** Add the 6 published a_e corrections, re-extract α at <1 ppb, propagate to R∞, a₀, μ₀.

**Experiment:** `experiment_qed_full_corrections_v0`

**New value nodes needed:**

| Key | Value (×10⁻¹²) | Source |
|---|---|---|
| `qed_ae_mass_dep_2loop_v0` | 2.7207 | Kinoshita et al. μ/τ VP at 2-loop |
| `qed_ae_mass_dep_3loop_v0` | 0.1110 | Laporta, Passera. μ/τ VP at 3-loop |
| `qed_ae_mass_dep_4loop_v0` | 0.0300 | Kinoshita, Nio. μ/τ VP at 4-loop |
| `qed_ae_hadronic_lo_v0` | 1.8600 | Davier et al. / lattice. Leading hadronic VP |
| `qed_ae_hadronic_nlo_v0` | −0.2200 | Kurz et al. Next-to-leading hadronic |
| `qed_ae_hadronic_lbl_v0` | 0.3400 | WP 2020. Light-by-light scattering |
| `qed_ae_electroweak_v0` | 0.0300 | Czarnecki, Marciano, Vainshtein. W/Z loops |

**Derivation:**

| Function | Formula | Description |
|---|---|---|
| `qed_alpha_full_corrections_v0` | a_e(total) = a_e(QED series, A₁-A₅) + Σ corrections. Invert a_e(total) for α. | Same Newton inversion but with corrected a_e input: a_e(measured) − Σ corrections = a_e(QED mass-independent), then invert. |

**Comparisons:** α⁻¹ vs CODATA at <1 ppb, α⁻¹ vs Rb recoil, α⁻¹ vs Cs recoil, R∞ at <2 ppb, a₀ at <1 ppb, μ₀ at <1 ppb.

**Expected improvement:** α from 3.3 ppb to ~0.5 ppb. R∞ from 8.0 ppb to ~1.0 ppb. a₀ and μ₀ from 4.0 ppb to ~0.5 ppb.

**Difficulty:** Easy. All correction values are published. The derivation is one subtraction plus the existing Newton inversion.

---

### PATH 3: Muon g-2 prediction (3 new derived values)

**Goal:** Predict a_μ(SM) from derived α plus published hadronic and EW corrections. Compare to Fermilab.

**Experiment:** `experiment_muon_g2_v0`

**New value nodes needed:**

| Key | Value | Source |
|---|---|---|
| `qed_amu_qed_10th_order_v0` | 116584718.9 × 10⁻¹¹ | Aoyama et al. 2020 WP. QED through 5-loop |
| `qed_amu_hadronic_lo_v0` | 6931 × 10⁻¹¹ | Lattice QCD / e⁺e⁻ data. Leading HVP |
| `qed_amu_hadronic_lo_unc_v0` | 40 × 10⁻¹¹ | Uncertainty on LO HVP |
| `qed_amu_hadronic_nlo_v0` | −98.3 × 10⁻¹¹ | Kurz et al. / Laporta. NLO HVP |
| `qed_amu_hadronic_lbl_v0` | 92 × 10⁻¹¹ | WP 2020. Light-by-light |
| `qed_amu_hadronic_lbl_unc_v0` | 18 × 10⁻¹¹ | Uncertainty on LbL |
| `qed_amu_ew_v0` | 153.6 × 10⁻¹¹ | Czarnecki et al. Electroweak |
| `qed_amu_measured_v0` | 116592059 × 10⁻¹¹ | Fermilab (2023) + BNL combined |
| `qed_amu_measured_unc_v0` | 22 × 10⁻¹¹ | Combined uncertainty |

**Derivations:**

| Function | Description |
|---|---|
| `muon_g2_qed_from_alpha_v0` | Compute a_μ(QED) from our derived α. The QED series for the muon uses the same A₁-A₅ coefficients but with mass-dependent terms that scale as (m_e/m_μ)² and (m_μ/m_τ)². Uses α from pool, m_e, m_μ, m_τ from pool. |
| `muon_g2_total_prediction_v0` | Sum: a_μ(QED) + a_μ(had LO) + a_μ(had NLO) + a_μ(had LbL) + a_μ(EW). Compare to Fermilab. Compute tension in σ. |

**Comparisons:** a_μ(SM) vs Fermilab, tension in σ, individual contributions vs WP 2020.

**New derived values:** a_μ(QED from our α), a_μ(SM total), tension σ = 3 values.

**Difficulty:** Medium. The muon QED series uses the same coefficients but needs mass-ratio corrections. The dominant uncertainty is the hadronic LO VP which has the CMD-3 tension. We store both pre-CMD-3 and post-CMD-3 values as separate nodes and run both.

---

### PATH 4: BBN extension — Lithium and Helium-3 (3 new derived values)

**Goal:** Extend the η → abundance chain to Li-7/H and He-3/H. Li-7 is the famous BBN lithium problem.

**Experiment:** `experiment_bbn_extended_v0`

**New value nodes needed:**

| Key | Value | Source |
|---|---|---|
| `bbn_li7_a_coeff_v0` | 4.68 | Pitrou et al. 2018. Li-7/H (×10¹⁰) at η₁₀ = 6 |
| `bbn_li7_b_coeff_v0` | 0.67 | Sensitivity d(Li7/H×10¹⁰)/d(η₁₀) |
| `bbn_he3_a_coeff_v0` | 1.04 | Pitrou et al. 2018. He-3/H (×10⁵) at η₁₀ = 6 |
| `bbn_he3_b_coeff_v0` | −0.14 | Sensitivity |
| `cosmo_li7_measured_v0` | 1.6 × 10⁻¹⁰ | Spite plateau. Li-7/H measured in metal-poor stars |
| `cosmo_li7_measured_unc_v0` | 0.3 × 10⁻¹⁰ | Uncertainty |
| `cosmo_he3_measured_v0` | 1.1 × 10⁻⁵ | Bania et al. He-3/H from galactic HII regions |
| `cosmo_he3_measured_unc_v0` | 0.2 × 10⁻⁵ | Uncertainty |

**Derivations:**

| Function | Formula |
|---|---|
| `bridge_li7_from_eta_v0` | Li-7/H (×10¹⁰) = a + b×(η₁₀ − 6). Same pattern as Y_p and D/H. |
| `bridge_he3_from_eta_v0` | He-3/H (×10⁵) = a + b×(η₁₀ − 6). |
| `bridge_li7_problem_v0` | Compare derived Li-7 to measured. Compute the ratio (predicted/observed). The lithium problem: ratio ≈ 3. |

**Comparisons:** Li-7/H vs Spite plateau (expect ~3× overprediction = the lithium problem), He-3/H vs galactic measurement, lithium problem ratio.

**New derived values:** Li-7/H (predicted), He-3/H (predicted), lithium problem ratio = 3 values.

**Difficulty:** Easy. Same BBN fitting formula pattern as Y_p and D/H. The lithium problem is a KNOWN discrepancy — our chain reproducing it is a feature, not a bug. It shows the system handles tensions correctly.

**Significance:** Our chain predicts D/H at 0.12σ AND reproduces the lithium problem at 3×. Both from the same η₁₀ derived from gauge integers. This is a strong consistency check — the system gets D/H right and Li-7 wrong in exactly the way the standard BBN model does.

---

### PATH 5: CKM from CD mixing (4 new derived values)

**Goal:** Use the Cabibbo Doublet mixing parameters to predict CKM corrections. The CD extends the 3×3 CKM to 4×4, with the fourth row/column from the VL quark mixing.

**Experiment:** `experiment_ckm_cd_mixing_v0`

**New value nodes needed:**

| Key | Value | Source |
|---|---|---|
| `cd_mass_reference_v0` | 3000000 MeV | CD mass estimate (3 TeV, middle of [1.5, 6] window) |
| `cd_theta14_v0` | 0.045 | sin θ₁₄ from CKM first-row deficit. Belfatto & Berezhiani 2020 |
| `cd_theta24_estimate_v0` | 0.010 | sin θ₂₄ from kaon physics constraints |
| `cd_theta34_estimate_v0` | 0.030 | sin θ₃₄ from A_FB(b) fit |
| `ckm_vud_measured_v0` | 0.97373 | PDG 2024. |V_ud| from superallowed β decay |
| `ckm_vud_unc_v0` | 0.00031 | Uncertainty |
| `ckm_vus_measured_v0` | 0.2243 | PDG 2024. |V_us| from K decays |
| `ckm_vus_unc_v0` | 0.0005 | Uncertainty |
| `ckm_vub_measured_v0` | 0.00382 | PDG 2024. |V_ub| from B decays |
| `ckm_first_row_unitarity_v0` | 0.9985 | |V_ud|² + |V_us|² + |V_ub|² (deficit from 1.0000) |

**Derivations:**

| Function | Description |
|---|---|
| `ckm_first_row_from_cd_v0` | In the 4×4 CKM: \|V_ud\|² + \|V_us\|² + \|V_ub\|² + \|V_ub'\|² = 1. The CD adds \|V_ub'\|² = sin²θ₁₄. Compute: first-row unitarity = 1 − sin²θ₁₄. Compare to measured deficit. |
| `ckm_vud_corrected_v0` | V_ud(corrected) = V_ud(measured) × √(1/(1−sin²θ₁₄)). The CD mixing slightly shifts the extracted V_ud. |
| `ckm_cabibbo_angle_from_cd_v0` | sin θ_C = V_us / √(1 − sin²θ₁₄). The Cabibbo angle is modified by the CD. |
| `ckm_unitarity_test_v0` | Full 4×4 unitarity check: does sin²θ₁₄ = 0.045² = 0.002025 account for the observed 0.0015 deficit? |

**Comparisons:** First-row unitarity deficit predicted vs measured, V_ud corrected vs V_ud measured, Cabibbo angle consistency.

**New derived values:** V_ud(corrected), V_us(corrected), first-row unitarity(from CD), Cabibbo angle(from CD) = 4 values.

**Difficulty:** Medium. The 4×4 CKM parametrization with the CD is specified in PHYS-19. The mixing angles are staged but have estimated values. The results are conditional on M_VL and θ₁₄ — similar to the Koide conditional derivation.

**Significance:** This is the ONLY path that connects the Cabibbo Doublet (our BSM candidate) to flavor physics measurements. If the first-row deficit matches sin²θ₁₄, it's direct evidence for the CD beyond the coupling gap ratio.

---

### PATH 6: Proton decay lifetime (1 new derived value)

**Goal:** Derive τ_proton from M_GUT. Compare to experimental bounds.

**Experiment:** `experiment_proton_decay_v0` (already defined in DATA-6, needs implementation)

**New value nodes needed:**

| Key | Value | Source |
|---|---|---|
| `proton_tau_superk_bound_v0` | 1.6e34 | Super-K 2020. Lower bound τ(p→e⁺π⁰) in years |
| `proton_tau_hyperk_sensitivity_v0` | 1.0e35 | Hyper-K projected. 10-year sensitivity |
| `gut_alpha_gut_estimate_v0` | 0.0260 | α_GUT at unification from CD running |
| `gut_proton_matrix_element_v0` | 0.012 | \|α_H\|² lattice QCD matrix element in GeV³ |
| `gut_phase_space_factor_v0` | 1.0 | Phase space and kinematic factor (~1 for minimal SU(5) channel) |

**Derivation:**

| Function | Formula |
|---|---|
| `proton_decay_lifetime_v0` | τ_p = M_GUT⁴ / (α_GUT² × m_p⁵ × \|α_H\|² × K). Uses M_GUT from crossing scale derivation. The exact formula depends on the GUT model (SU(5), SO(10)). For minimal SU(5): τ_p ~ M_GUT⁴ / (α_GUT² × m_p⁵ × 0.012²). |

**Comparisons:** τ_p vs Super-K lower bound (must exceed 1.6×10³⁴ yr), τ_p in Hyper-K sensitivity window [10³⁴, 10³⁵], log₁₀(τ_p) range check.

**New derived values:** τ_proton = 1 value.

**Difficulty:** Medium. The GUT proton decay formula has model-dependent factors (which GUT group, which decay channel, which matrix elements). We use the minimal SU(5) formula as a baseline. The M_GUT from CD unification is already computed.

**Significance:** If τ_p falls in the Hyper-K window (10³⁴-10³⁵ yr), the CD unification prediction is testable within the next decade. This is the most concrete experimental prediction from the gauge integer chain.

---

### PATH 7: α_s from derived α — fix the two-loop bug (1 improved value)

**Goal:** Fix the two-loop Euler integration that currently shows 10-12% miss. Get α_s at <1%.

**Experiment:** `experiment_two_loop_alpha_s_v1` (upgrade of existing)

**New value nodes needed:**

| Key | Value | Source |
|---|---|---|
| `beta_two_loop_vl_dbij_corrected_v0` | (9 values) | Corrected VL two-loop db_ij matrix. Investigate against DATA-5 platform. |
| `config_euler_step_count_v0` | 10000 | Numerical config. Increase from 4000. |
| `config_euler_dps_v0` | 100 | mp.dps for Euler integration |

**Derivations:**

| Function | Description |
|---|---|
| `coupling_two_loop_alpha_s_v1_v0` | Same Euler integration but with corrected db_ij values and increased step count. Uses derived α (from QED chain) as input if available. |
| `coupling_two_loop_diagnostic_v0` | Run the integration with SM-only betas (no CD) and compare to known SM α_s running. This isolates whether the bug is in the SM betas, the CD shifts, or the integration. |

**Investigation steps before writing code:**
1. Compare db_ij values in DATA-6 to DATA-5 platform line by line
2. Check the PHYS-33 pitfall (b_ij gauge double-count: 39/4 vs 15/4)
3. Run SM-only integration first — if SM α_s at M_Z matches published, the SM betas are correct
4. Add CD shifts — if it breaks, the db_ij values are wrong

**Comparisons:** α_s(M_Z) two-loop SM-only vs published 0.1185, α_s(M_Z) two-loop with CD vs measured 0.1180, improvement over current 10% miss.

**New derived values:** α_s(two-loop, corrected) = 1 improved value.

**Difficulty:** Medium-Hard. This is a debugging task, not a new derivation. The bug has been known since DATA-6 was created. The most likely cause is the PHYS-33 pitfall in the db_ij matrix.

---

### PATH 8: Hubble running (1 new derived value, speculative)

**Goal:** Test the hypothesis that H₀ runs with distance (boundary transit model). Derive H₀(CMB) from H₀(local) + running parameter.

**Experiment:** `experiment_hubble_running_v0` (already defined, needs implementation)

**New value nodes needed:**

| Key | Value | Source |
|---|---|---|
| `cosmo_h0_shoes_v0` | 73.0 | SH0ES 2022. Local H₀ from Cepheids |
| `cosmo_h0_shoes_unc_v0` | 1.0 | Uncertainty |
| `cosmo_hubble_vp_step_v0` | 0.1061 | 1/(3π) = VP step size from PHYS-6 |
| `cosmo_hubble_n_cmb_v0` | 15 | Estimated number of boundary transits to CMB |

Already in pool: `cosmo_h0_planck_v0` = 67.4.

**Derivations:**

| Function | Description |
|---|---|
| `hubble_running_model_v0` | H₀(N) = H₀(0) × r^N where r = (H₀(CMB)/H₀(local))^(1/N). Compute r for various N. Test: does r match the VP step size 1/(3π)? |
| `hubble_running_prediction_v0` | Given H₀(local) = 73.0 and VP step = 1/(3π), predict H₀(CMB) = 73.0 × (1 − 1/(3π))^N for various N. Find N that gives 67.4. |
| `hubble_intermediate_check_v0` | Predict H₀ at intermediate distances (H0LiCOW, CCHP, DES). Compare to measured values at those distances. Test monotonicity. |

**Comparisons:** H₀(CMB predicted) vs Planck 67.4, r vs VP step 1/(3π), intermediate H₀ values vs H0LiCOW/CCHP/DES, monotonicity check.

**New derived values:** H₀(CMB from running) = 1 value.

**Difficulty:** Hard (conceptually). The boundary transit model is the most speculative part of HOWL. The number N of transits to CMB is unknown. The VP step size 1/(3π) comes from PHYS-6 but the physical mechanism for why VP steps affect cosmological expansion is not established.

**Risk assessment:** If it works (predicted H₀(CMB) matches Planck within 1σ), it resolves the Hubble tension from integer physics. If it doesn't, the model is wrong and we document the failure. Either way, the experiment is informative.

---

### PRIORITY ORDER

| Priority | Path | New Values | Difficulty | Dependencies |
|---|---|---|---|---|
| 1 | Path 2: a_e corrections | 0 new (4 improved) | Easy | None — published values |
| 2 | Path 4: BBN extension | 3 | Easy | η already derived |
| 3 | Path 1: EW v2 | 7 | Medium | G_F, α(M_Z) in pool |
| 4 | Path 6: Proton decay | 1 | Medium | M_GUT already computed |
| 5 | Path 7: Two-loop fix | 1 improved | Medium-Hard | Debugging investigation |
| 6 | Path 3: Muon g-2 | 3 | Medium | Path 2 first (need corrected α) |
| 7 | Path 5: CKM from CD | 4 | Medium | CD parameters staged |
| 8 | Path 8: Hubble running | 1 | Hard | Speculative model |

**Session time estimate:**
- Paths 1-2: one session (values + experiment + derivations + run)
- Paths 3-4: one session  
- Paths 5-6: one session
- Path 7: one session (mostly debugging)
- Path 8: half a session (small experiment, most time on interpretation)

**Total if all paths succeed:** 17 current + 7 + 3 + 3 + 1 + 1 + 4 + 1 = 37 derived values from ~15 measured inputs. 22 more outputs than inputs. Every additional output that matches is a constraint on the parameter space.

---

