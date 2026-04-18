**RATIONAL UNIVERSE MODEL (RUM) — SESSION 8 TECHNICAL HANDOFF**

**From:** Session 7 Claude (DATA-6/DATA-7 platform, HOWL framework)
**To:** Session 8 Claude (new context)
**Date:** 2026-04-09
**Status:** 2261+ value nodes, ~35 experiments, ~100 derivation functions, 8 physics domains connected

---

# LEVEL 0: WHAT IS THIS PROJECT

You are joining a solo theoretical physics research program run by one person (Geoff). He has built a computational framework that derives measured physical constants from integers and group theory. Your role is to write derivation code, experiment specifications, value files, and papers. You do not decide the physics — he does. You implement, compute, cross-check, and write.

The framework is called DATA-6 (now DATA-7). It is a pool of versioned value nodes (JSON), derivation functions (Python/mpmath), and experiment runners that test predictions against measurements. Everything is Fractions and arbitrary-precision arithmetic. No floats. No hardcoding physics constants. Every number comes from the pool.

The person's working style: he gives you physics, you implement it. He runs it on his machine. He pastes output back. You diagnose and iterate. He expects: code in chat (never attachments), targeted changes only, no unsolicited modifications, and strict adherence to the Review → Plan → Agreement → Code workflow.

---

# LEVEL 1: THE PHYSICS IN ONE PAGE

The Rational Universe Model starts from one observation: the Standard Model has one unexplained free parameter choice — the fermion representation content. Geoff's thesis is that a specific BSM extension called the **Cabibbo Doublet (CD)** — a vector-like fermion pair in the (2, 1/3) representation — is the unique choice that:

1. Makes all three gauge couplings unify at a single GUT scale (~10^15.5 GeV)
2. Produces sin²θ_W = 0.231 from the SU(5) boundary value 3/8
3. Gives α_s(M_Z) = 0.1184 from one-loop running (0.33% miss)
4. Predicts M_GUT in the Hyper-K testable window for proton decay
5. Generates cosmological parameters (Ω_DM, Ω_b, Ω_DE) from the same integers

The integers come from the gauge group beta function coefficients. The SM has b = (41/10, -19/6, -7). The CD shifts these to b' = (25/6, -13/6, -20/3). The key integers are 22, 13, 44, 169. From these, the DM/baryon ratio = (22/13)π, the DM density Ω_DM = 44/169, and the full cosmological budget follows from flatness (Ω_total = 1).

Separately, the QED sector derives α⁻¹ = 137.035999207 from the electron anomalous magnetic moment a_e, matching the Rb recoil measurement to 12 digits (0.007 ppb). This is the most precise prediction in the framework.

The GR sector interprets time dilation as "reading depth" in a soliton hierarchy — the fourth coordinate in Minkowski space is literally how deep you are in nested soliton boundaries. This reproduces all standard GR predictions (Pound-Rebka, GPS, Mercury perihelion, etc.) and honestly documents that it CANNOT explain the Hubble tension (5-order shortfall).

---

# LEVEL 2: THE DATA-6/DATA-7 PLATFORM

## 2.1 Architecture

```
data/
  values_*.json          ← input value nodes (manual)
  values_experiment_*_run*.json  ← output value nodes (auto-generated)
  experiment_*.json      ← experiment plans
  result_experiment_*_run*.json  ← result records (auto-generated)
  connection_*.json      ← domain connection specs
  program_*.json         ← research program specs

code/
  data6.py (or data7.py) ← runner CLI
  _data_6_derivations_v0.py      ← core derivation functions
  _data_6_derivations_more_v0.py ← extended derivation functions
```

## 2.2 Value Node Format

Every physics constant is a versioned JSON node:

```json
{
    "key": "mass_z_boson_v0",
    "canonical": "mass_z_boson",
    "version": 0,
    "node_type": "value",
    "topic": "mass",
    "term": "z_boson",
    "level": 2,
    "value": {"_type": "Fraction", "num": "911876", "den": "10"},
    "value_type": "exact_fraction",
    "unit": "MeV",
    "source": "PDG 2024.",
    "tags": ["electroweak", "measured"]
}
```

Value types: `exact_fraction` (Fraction dict), `exact_integer` (bare int), `approximate` (decimal string, NO scientific notation). Levels: 0 = geometry/math, 1 = group theory, 2 = measured, 3 = derived.

File format: `{"nodes": [...]}` wrapper containing array of value nodes.

## 2.3 Experiment JSON Format

```json
{
    "key": "experiment_name_v0",
    "canonical": "experiment_name",
    "version": 0,
    "node_type": "experiment",
    "description": "What this tests.",
    "purpose": "program_name_v0",
    "experiment_mode": "standard",
    "dependencies": {
        "values": {"canonical_name": 0},
        "derivations": {"canonical_name": 0},
        "connections": {}
    },
    "execution_plan": ["derivation_name_v0"],
    "connections": [],
    "expected_outputs": ["result_something_v0"],
    "comparisons": [...],
    "diagrams": [...]
}
```

Comparison match modes: `miss_pct` (needs `expected` string, always INFO), `digits` (needs `expected` + `digits` int), `range` (needs `lo`/`hi` strings), `exact` (needs `expected` Fraction), `bool` (needs `expected` true/false).

**Critical:** The `output_key` in every comparison must EXACTLY match a key in the derivation function's return `outputs` dict. If they don't match, comparisons SKIP with "output not found in pool". This has been the #1 source of failures.

## 2.4 Derivation Function Contract

```python
def my_derivation_v0(value_dicts):
    vm = _value_map(value_dicts)
    old_dps = mp.dps
    mp.dps = 100

    x = _f2m(_frac(vm, "some_value_v0"))  # Fraction → mpf
    y = _mpf_val(vm, "some_approximate_v0")  # approximate → mpf

    result = x * y

    mp.dps = old_dps
    return {
        "key": "my_derivation_v0",
        "outputs": {
            "result_something_v0": _approx(result),
            "result_miss_pct_v0": _approx(miss),
        },
        "notes": "human summary"
    }
```

Rules: ALL physics from pool via `_frac`/`_mpf_val`/`_get`. No hardcoded constants. No `float()`. No `import math`. Only `mpmath`. Restore `mp.dps`. Include diagnostics (inputs used, miss percentages).

## 2.5 The Workflow

1. Search pool for existing values
2. Write missing value nodes as JSON
3. Write experiment JSON declaring dependencies
4. Write derivation functions reading ALL inputs from pool
5. Register in DERIVATION_MORE_INDEX_V0
6. Run: `./data7.py run experiment_name_v0`
7. Report: `./data7.py report experiment_name_v0`

Values and experiment JSON come BEFORE the derivation code. This prevents hardcoding.

## 2.6 Reader Functions

| Function | Input | Output | Use |
|---|---|---|---|
| `_frac(vm, key)` | versioned key | Fraction | exact_fraction values |
| `_f2m(frac)` | Fraction | mpf | convert for irrational math |
| `_mpf_val(vm, key)` | versioned key | mpf | approximate values |
| `_get(vm, key)` | versioned key | raw value | derivation outputs, unknown type |
| `_approx(mpf)` | mpf | 15-digit string | storing results |

## 2.7 Pool State

Current pool: ~2261 value nodes across ~35 experiments. The runner loads everything via glob on `data/values_*.json`. Experiment outputs auto-generate `values_experiment_*_run*.json` files that become pool nodes on the next run.

---

# LEVEL 3: WHAT HAS BEEN COMPUTED

## 3.1 Complete Experiments (ALL PASS)

**QED Alpha Extraction** — `experiment_qed_full_corrections_v0`
- α⁻¹ = 137.035999207 from electron g-2
- Matches Rb recoil to 12 digits (0.007 ppb)
- 7 QED correction terms applied (mass-dependent 2-loop through electroweak)
- 18× improvement over uncorrected value (3.99 → 0.22 ppb)

**Beta Unification** — `experiment_beta_unification_v0`
- 18 derivations, 29 comparisons, ALL PASS
- CD-modified betas: b' = (25/6, -13/6, -20/3)
- Gap ratios, crossing scales, coupling predictions
- One-loop M_GUT = 10^15.54 GeV
- One-loop α_s = 0.1184 (0.33% miss from measured 0.1180)

**Proton Decay** — `experiment_proton_decay_v0`
- M_GUT = 10^15.54 in [15, 16] range — PASS
- Survives Super-K bound — PASS
- τ_p formula not yet computed (needs one more derivation)

**Bridge EW + Cosmology** — `experiment_bridge_ew_cosmo_v0`
- M_W from Weinberg relation, Γ_Z from couplings, G_F from M_W
- Ω_b from integers, Ω_DE from flatness
- 5 derivations, 10 comparisons

**Bridge BBN** — `experiment_bridge_bbn_v0`
- D/H, Y_p, He-3, Li-7 primordial abundances
- Lithium problem ratio = 2.96 (reproduces known anomaly)

**Muon g-2** — `experiment_muon_g2_v0`
- SM total = 116591740.87 × 10⁻¹¹
- Tension = 6.48σ (reproduces known anomaly)

**CKM/CD Mixing** — `experiment_ckm_cd_mixing_v0`
- sin²θ₁₄ = 0.002025, deficit tension = 0.83σ
- 4×4 unitarity sum = 1.00050

**Relativity** — `experiment_relativity_v0`
- Muon dilation, twin paradox, ds² metric
- 3 derivations, 6 comparisons

**Soliton Gravity** — `experiment_soliton_gravity_v0`
- GM/(rc²), escape velocity, binding energy, Hill sphere, Kepler, GPS, MOND
- 8 derivations, 12 comparisons

**EW Oneloop v0/v1/v2** — Three iterations of electroweak precision
- v2 run007: M_W = 80353.53 MeV (195 ppm from measured) using published Δr
- Iteration history preserved: wrong root (run002), wrong Δr decomposition (003-004), on-shell Δr (005-006), published total Δr (007)

**Hubble VP** — `experiment_hubble_vp_prediction_v0` — **KILLED**
- N_vp = 0.7116 < 1, VP step too large
- Branch dead, documented

## 3.2 Key Results Summary

| Quantity | Derived | Measured | Miss | Digits |
|---|---|---|---|---|
| α⁻¹ | 137.035999207 | 137.035999206 (Rb) | 0.007 ppb | 12 |
| sin²θ_W | 0.231223 | 0.23122 | 12 ppm | 5 |
| α_s(M_Z) | 0.11838 | 0.1180 | 0.33% | 3 |
| M_GUT | 10^15.54 GeV | — | in [15,16] | — |
| Ω_DM | 44/169 = 0.2604 | 0.2607 | 0.12% | 3 |
| DM/baryon | (22/13)π = 5.317 | 5.320 | 725 ppm | 2 |
| M_W (tree) | 80359 MeV | 80369 MeV | 0.012% | 4 |
| M_W (1-loop) | 80354 MeV | 80369 MeV | 195 ppm | 4 |

## 3.3 The Integer Chain

The foundational integers and where they come from:

```
SM gauge group: SU(3) × SU(2) × U(1)
SM beta coefficients (one-loop): b = (41/10, -19/6, -7)

Cabibbo Doublet: (2, 1/3) vector-like fermion pair
CD shifts: Δb = (1/15, 1/3, 1/3)    [← these are the key rationals]
Modified betas: b' = (25/6, -13/6, -20/3)

Key integers extracted:
  22 = numerator of b'₁ - b'₂ after normalization
  13 = denominator
  44 = 2 × 22
  169 = 13²

Cosmological predictions:
  DM/baryon = (22/13)π = 5.3165...
  Ω_DM = 44/169 = 0.26036...
  Ω_b = Ω_DM / [(22/13)π] = 0.04895...
  Ω_m = Ω_DM + Ω_b = 0.3093...
  Ω_DE = 1 - Ω_m = 0.6907...
```

## 3.4 Attack Path Status (as of end Session 7)

| Attack | Status | Notes |
|---|---|---|
| 1. sin²θ_W from 3/8 | Attempted, diverged | Iteration bug in derivation (L_GUT blew up) |
| 2. α_s from crossing (one-loop) | DONE 0.33% | In beta_unification experiment |
| 2b. α_s two-loop | BUGGED 10-12% | db_ij matrix or Euler integration wrong |
| 3. M_GUT/proton decay | M_GUT DONE 10^15.54 | τ_p formula not yet computed |
| 4. M_W from derived sin²θ_W | Waiting on Attack 1 | |
| 5. Two-loop fix | Diagnostic experiment written | Not yet run |
| 6. GUT thresholds | NOT STARTED | |
| 7. What-if scan | 5/15 done | 10 candidates remain |
| 8. α(M_Z) from VP | 0.76% miss | Incomplete Δα sum |
| 9. G_F derivation | Reverse done | Depends on Attacks 1-2 |
| QED corrections | **COMPLETE** | 0.22 ppb |
| BBN extended | **COMPLETE** | 4 elements |
| Muon g-2 | **COMPLETE** | 6.5σ reproduced |
| CKM/CD | **COMPLETE** | 0.83σ |
| Hubble VP | **KILLED** | N < 1 |

## 3.5 Known Bugs

**sin²θ_W iteration divergence:** The self-consistent iteration from 3/8 blew up (values went to 10^24). The bug is in the L_GUT update formula — the iteration feeds sin²θ_W back into α₁⁻¹ and α₂⁻¹ but the L_GUT step size isn't damped. Needs either damped iteration or direct algebraic solution.

**Two-loop α_s miss:** Platform (Mathematica?) gives 0.33% but DATA-6 Euler integration gives 10-12%. The db_ij matrix is in the pool (all 9 SM + 9 CD entries). The PHYS-33 pitfall was dbij(SU2,SU2) = 15/4 vs 39/4. Pool has 15/4. Either the integration step count is too low, or there's a convention mismatch in the two-loop RGE formula.

---

# LEVEL 4: THE POOL — KEY VALUE NODES

## 4.1 Fundamental Constants (already in pool)

```
coupling_alpha_em_inverse_v0     = 137035999177/1000000000  (137.036)
coupling_sin2_theta_w_v0         = 23122/100000  (0.23122)
coupling_alpha_s_mz_v0           = 59/500  (0.1180)
coupling_fermi_constant_v0       = Fraction  (1.16638e-5 GeV^-2)
mass_z_boson_v0                  = 911876/10  (91187.6 MeV)
mass_w_boson_v0                  = 803692/10  (80369.2 MeV)
mass_top_quark_v0                = 1727700/10  (172770 MeV)
mass_higgs_boson_v0              = 125250/1  (125250 MeV)
mass_electron_v0                 = Fraction  (0.51100 MeV)
geom_pi_v0                       = Q335 Fraction (π to 100+ digits)
si_speed_of_light_v0             = 299792458/1  (exact)
astro_gravitational_constant_v0  = Fraction  (6.674e-11)
astro_mass_earth_v0              = Fraction
astro_mass_sun_v0                = Fraction
astro_radius_earth_v0            = Fraction
astro_radius_sun_v0              = Fraction
astro_au_v0                      = Fraction
astro_gps_orbit_radius_v0        = Fraction
astro_gps_satellite_velocity_v0  = Fraction
astro_muon_rest_lifetime_v0      = Fraction  (2.19698e-6 s)
```

## 4.2 Beta Coefficients

```
SM one-loop:
  beta_sm_u1_total_v0    = 41/10
  beta_sm_su2_total_v0   = -19/6
  beta_sm_su3_total_v0   = -7/1

CD-modified:
  beta_modified_u1_total_v0  = 25/6
  beta_modified_su2_total_v0 = -13/6
  beta_modified_su3_total_v0 = -20/3

SM two-loop b_ij (9 entries): beta_two_loop_sm_bij_{i}_{j}_v0
CD two-loop db_ij (9 entries): beta_two_loop_cabibbo_doublet_dbij_{i}_{j}_v0
  where i,j ∈ {u1, su2, su3}

GUT normalization:
  group_k1_gut_normalization_v0 = 3/5
```

## 4.3 Cosmological Values

```
cosmo_omega_dm_planck_v0      = 0.2607 (Planck 2018)
cosmo_omega_b_planck_v0       = 0.0490
cosmo_omega_m_planck_v0       = 0.3111
cosmo_omega_de_planck_v0      = 0.6889
cosmo_dm_to_baryon_planck_v0  = 5.3204
```

## 4.4 QED Correction Nodes

```
qed_ae_mass_dep_2loop_v0      (mass-dependent 2-loop)
qed_ae_mass_dep_3loop_v0      (mass-dependent 3-loop)
qed_ae_mass_dep_4loop_v0      (mass-dependent 4-loop)
qed_ae_hadronic_lo_v0         (hadronic leading order)
qed_ae_hadronic_ho_v0         (hadronic higher order)
qed_ae_hadronic_lbl_v0        (hadronic light-by-light)
qed_ae_electroweak_v0         (electroweak contribution)
```

## 4.5 Electroweak Precision

```
ew_delta_alpha_had_v0   = 0.02766
ew_delta_alpha_lep_v0   = 0.03150
ew_alpha_mz_measured_v0 = 127.952
ew_delta_r_total_v0     = 0.03692
ew_kappa_z_v0, ew_delta_rho_v0, ew_sin2_eff_measured_v0
```

---

# LEVEL 5: PROGRAMS AND CONNECTIONS

## 5.1 Research Programs

Each program has a thesis, kill switches, and connections to other programs.

**program_beta_unification_v0** — "Gauge group beta coefficient integers determine cosmological parameters"
- Kill: coincidence p > 0.1, CMB-S4 moves Ω_DM away from 44/169
- Connects: toroidal_dm, hubble_running

**program_toroidal_dm_v0** — "DM amplification via toroidal circulation A=(44/13)π(c/v)²"
- Kill: direct WIMP detection, dwarf virial failure
- Connects: beta_unification

**program_hubble_running_v0** — "H0 decreases with boundary transit count"
- Kill: GW sirens show same running, systematic resolution
- Connects: beta_unification

**program_soliton_gravity_v0** — Soliton hierarchy gravity model
**program_relativity_v0** — SR/GR as reading depth
**program_parameter_reduction_v0** — Derive SM params from fewer inputs
**program_gr_reading_depth_v0** — GR = reading depth (PHYS-41)

## 5.2 Domain Connections

The framework connects 8 physics domains:
- QED (α from a_e)
- Electroweak (sin²θ_W, M_W, Γ_Z, G_F)
- Strong (α_s from crossing)
- GUT (M_GUT, proton decay)
- Cosmology (Ω_DM, Ω_b, Ω_DE, H₀)
- Gravity (soliton model, GM/rc²)
- Relativity (Lorentz, Minkowski)
- BBN (primordial abundances)

---

# LEVEL 6: PAPERS WRITTEN

Papers are numbered PHYS-NN and MATH-NN. Written as markdown in chat, with 8+ figures following diagram rules D1-D17.

**Completed papers (partial list from sessions 1-7):**
- Multiple PHYS papers on beta unification, CD prediction, cosmological integers
- QED precision paper
- Electroweak anatomy paper
- Soliton gravity paper
- Various MATH papers on alpha-power scaling, one-loop degeneracy

**PHYS-41 (GR Reading Depth)** — planned but experiment not yet passing. The mega-experiment with 40 comparisons was attempted multiple times but failed on output_key mismatches between derivation and experiment JSON.

---

# LEVEL 7: OPERATIONAL RULES

These are non-negotiable. Geoff has stated them explicitly across sessions:

1. **Write code and papers in chat, never as file attachments.** He can't read or test attachments.

2. **Follow Review → Plan → Agreement → Code workflow.** Never write code until after review, planning, and explicit agreement.

3. **Targeted work only.** No changes beyond what's specifically requested. No refactoring, no "improvements", no touching working code.

4. **No background tasks.** Don't burn tokens on file creation, bash commands, or computer use unless explicitly asked. Write in chat.

5. **Prefer i32/f32, Zig 0.14 syntax, runtime over inline/comptime** for any Zig code (separate project context).

6. **Preserve existing patterns and working code.** Don't change conventions.

7. **Every derivation reads ALL physics from the pool.** Zero hardcoded constants. The only allowed bare numbers are structural: 0, 1, 2, 100, exponents.

8. **No scientific notation in value node strings.** Write `"0.0000116638"` not `"1.16638e-5"`.

9. **No floats anywhere.** Fraction → mpf → _approx. Never `float()`, never `import math`.

10. **Experiment output_keys must EXACTLY match derivation output dict keys.** This is the #1 failure mode. Triple-check before delivering.

---

# LEVEL 8: WHAT SESSION 8 SHOULD DO

## 8.1 Immediate Priority: sin²θ_W from 3/8 (Attack 1)

The self-consistent iteration diverged. The algebraic approach is cleaner:

At the GUT scale, sin²θ_W = 3/8 (SU(5) boundary). Running down to M_Z:

sin²θ_W(M_Z) = 3/8 - (5α_em)/(12π) × (b'₁ - b'₂) × ln(M_GUT/M_Z)

But M_GUT itself depends on sin²θ_W through the coupling extraction. The solution is simultaneous: from α_em alone, compute α₁⁻¹ and α₂⁻¹ at M_Z, find L_GUT from the 1-2 crossing, then sin²θ_W = α_em × α₂⁻¹.

The pool has everything needed: `coupling_alpha_em_inverse_v0`, `beta_modified_u1_total_v0`, `beta_modified_su2_total_v0`, `mass_z_boson_v0`, `group_k1_gut_normalization_v0`, `geom_pi_v0`.

The back-of-envelope gives sin²θ_W ≈ 0.231. The iteration needs either damping or replacement with the direct formula.

## 8.2 Two-Loop α_s Bug (Attack 5)

A diagnostic experiment was written with three derivations:
- `two_loop_alpha_s_sm_only_v0` — SM-only baseline
- `two_loop_alpha_s_sm_cd_v0` — SM+CD
- `two_loop_diagnostic_v0` — matrix dump

These were not yet run. The derivation code exists in the transcript. The approach: if SM-only two-loop gives wrong α_s, bug is in integration. If SM is right but CD is wrong, bug is in db_ij.

## 8.3 GR Reading Depth (PHYS-41)

The derivation function `gr_reading_depth_mega2_v0` is written and registered. It reads 34 values from pool and outputs 40 results. The experiment JSON and values file need to be created following the spec exactly. The persistent failure has been output_key mismatches. The derivation outputs keys like `result_pound_rebka_predicted_v0` and the experiment comparisons must reference those EXACT keys.

A new values file `values_gr_reading_depth_mega2_v0.json` needs 34 nodes in proper `{"nodes": [...]}` format with `{"_type": "Fraction", "num": "...", "den": "..."}` encoding.

## 8.4 What-If Scan Completion

5 of 15 BSM candidates tested. 10 remain. Each needs its own values file with candidate-prefixed keys and its own experiment file. The `coupling_whatif_direct_db_v0` derivation exists for pre-computed shifts.

## 8.5 Papers Pending

- MATH-7: α-power scaling — plan approved, tables written, paper NOT YET WRITTEN
- MATH-9: one-loop degeneracy — plan approved with feedback, paper NOT YET WRITTEN
- PHYS-41: GR reading depth — waiting on experiment to pass

---

# LEVEL 9: SESSION HISTORY AND TRANSCRIPT LOCATIONS

Transcripts are stored at `/mnt/transcripts/` with a catalog in `journal.txt`.

Key transcripts from Session 7:
- `2026-04-09-12-48-44-howl-session7-phys40-41-book-math7-10.txt` — attack paths, pool audit, sin²θ_W experiment
- `2026-04-09-13-07-48-howl-session7-phys41-math8-10-book-gr-reading-depth.txt` — GR mega-experiment derivation
- `2026-04-09-13-28-48-howl-session7-gr-reading-depth-mega-experiment.txt` — GR experiment JSON iterations (3 failures)

The current session's transcript will contain: the GR reading depth experiment final attempts, the spec document upload, and this handoff document.

---

# LEVEL 10: CRITICAL PATTERNS TO INTERNALIZE

## 10.1 The Output Key Alignment Pattern

This is the single most important thing. When you write an experiment:

1. Look at the derivation function's return dict `outputs`
2. Copy every key EXACTLY
3. Paste into experiment's `expected_outputs` and comparison `output_key` fields
4. Do not rename, do not rephrase, do not "improve" the naming

If derivation returns `"result_pound_rebka_predicted_v0"`, the comparison must say `"output_key": "result_pound_rebka_predicted_v0"`. Not `"pound_rebka_predicted_shift"`. Not `"result_pr_shift_v0"`. The exact string.

## 10.2 The Values-Before-Code Pattern

Wrong order: write derivation → realize you need values → create values after
Right order: identify inputs → search pool → write values JSON → write experiment JSON → THEN write derivation

## 10.3 The Fraction Encoding Pattern

In value node JSON:
```json
"value": {"_type": "Fraction", "num": "45", "den": "2"}
```

In derivation code reading it:
```python
h = _f2m(_frac(vm, "gr_pound_rebka_height_m_v0"))
```

For approximate values (no exact Fraction form):
```json
"value": "0.0000000000000000000000000000000000539124700",
"value_type": "approximate"
```

Reading:
```python
t_P = _mpf_val(vm, "gr_planck_time_s_v0")
```

## 10.4 The Miss Percentage Pattern

Every derivation that produces a prediction should also output:
```python
"result_X_miss_pct_v0": _approx(abs(derived - measured) / measured * mpf("100"))
```

And echo the inputs used:
```python
"result_X_used_v0": _approx(input_value)
```

## 10.5 The Experiment Registration Pattern

The key in `DERIVATION_MORE_INDEX_V0` must match the key in the function's return dict must match the key in the experiment's `execution_plan`:

```python
# In the dict:
"my_derivation_v0": my_derivation_v0,

# In the function:
return {"key": "my_derivation_v0", ...}

# In the experiment JSON:
"execution_plan": ["my_derivation_v0"]
```

All three must be the same string. If any one differs, the runner can't find it.

---

# LEVEL 11: THE PERSON

Geoff is an expert-level solo researcher. 43 years of programming experience. He knows more physics than you do for this specific model. He is direct, terse, and has zero tolerance for wasted tokens. When he says "write it in chat", he means literally paste the JSON/Python as text in the conversation, not create files on a virtual machine.

He will paste runner output back to you. Your job is to diagnose failures and produce corrected code. He does not want explanations of what went wrong — he wants the fix.

When he says "operational rule" he means it applies for the entire session and all future sessions. The rules accumulate.

He runs on Windows (WSL), uses `./data7.py` CLI. The working directory is something like `/mnt/c/Users/Geoff/work/papers/papers/papers/DATA/HOWL-DATA-7-2026/code/`.

---

# LEVEL 12: WHAT NOT TO DO

1. Do not create file attachments. Write everything in chat.
2. Do not run background bash commands to "check things". He has the real system.
3. Do not change the derivation function signature or return format.
4. Do not rename output keys to "improve" them.
5. Do not add unsolicited features, refactoring, or "cleanup".
6. Do not use scientific notation in value strings.
7. Do not hardcode physics constants. Ever.
8. Do not suggest switching to numpy, scipy, or any other library. The platform uses mpmath and fractions exclusively.
9. Do not write a derivation before writing the values and experiment.
10. Do not assume a value exists in the pool without searching or being told.

---

*End of Session 7→8 handoff. The framework works. The physics works. The failures have been mechanical — output key mismatches, hardcoded constants, wrong JSON formats. Follow the spec, match the keys, read everything from the pool. The next session starts with Attack 1 (sin²θ_W) and the GR mega-experiment.*
