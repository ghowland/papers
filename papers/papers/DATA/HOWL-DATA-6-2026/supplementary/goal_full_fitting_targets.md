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
