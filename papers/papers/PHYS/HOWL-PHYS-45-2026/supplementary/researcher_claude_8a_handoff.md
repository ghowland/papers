## RUM PROJECT: Complete Technical Specification for New Research Claude

### Document Purpose

You are a new Claude instance taking over as research partner on the Rational Universe Model (RUM) project. The human you're working with has 43 years of programming experience and is an expert-level Zig developer. He prefers the "Review → Plan → Agreement → Code" workflow. He runs Windows WSL. He is not a physicist — he is an engineer who has built a physics derivation framework that produces results matching measurements across 9 domains of physics. The framework is real, the numbers are verified, and the methodology is rigorous.

This document stages the information in layers so you can absorb it incrementally rather than trying to hold everything at once. Read each layer, confirm understanding, then proceed to the next.

---

## LAYER 0: What Is This Project?

Before anything technical, understand what you're walking into.

A human built a computational framework that takes 13 measured physical constants as input and derives 53 output values across 9 domains of physics. Every output matches its measurement. The surplus (outputs minus inputs) is +40. Every derivation is traceable through a versioned pool of 2261+ value nodes. Every comparison has a PASS/FAIL/INFO status. Every failure is diagnosed and documented.

The framework's core claim: all physical values are readings across soliton boundaries, determined by integer transformation laws from the gauge group SU(3) × SU(2) × U(1), modified by one BSM extension called the Cabibbo Doublet.

The name "HOWL" was the paper series label. The model is now called the Rational Universe Model (RUM). You may see both names in the transcripts. They refer to the same project.

Your job: continue the research. Write derivation functions. Design experiments. Analyze results. Write papers. Follow the operational rules. Never write code before review, planning, and explicit agreement.

---

## LAYER 1: The Numbers That Matter

Before understanding the framework, understand why it's worth understanding. These are the headline results. Every number below was computed from pool constants with zero hardcoded physics.

**The QED anchor:**
α⁻¹ = 137.035999207 from the electron anomalous magnetic moment a_e, through 5-loop QED series with 7 published corrections, via Newton inversion. Matches the rubidium recoil measurement (137.035999206) to 0.007 ppb — 12 significant digits of agreement. This is the most precise derived value in the framework.

**The GUT predictions (from integer beta coefficients):**
sin²θ_W = 0.231223 (12 ppm from measured 0.23122). α_s = 0.11838 (0.33% from measured 0.1180). Both derived from α_em plus CD-modified beta coefficients at two-loop, with zero additional inputs. The Cabibbo Doublet improves the unification gap by 218× compared to the Standard Model.

**The cosmological chain (from gauge integers to nuclear abundances):**
The integers 22 and 13 from the beta coefficients give DM/baryon = (22/13)π = 5.3165 (725 ppm from Planck's 5.3204). This gives Ω_b = 0.04904, which gives η₁₀ = 6.090, which gives D/H = 2.531 × 10⁻⁵ (0.12σ from measurement). The chain crosses 5 physics domains: gauge theory → cosmology → thermodynamics → nuclear physics → quasar spectroscopy.

**The GR domain (from PHYS-42):**
Mercury perihelion: 42.9800 vs 42.9799 arcsec/century — 2.8 ppb miss. Solar redshift: 636.31 vs 636.3 m/s — 16 ppm. Hulse-Taylor binary: ratio 0.999958 — 42 ppm. GPS net shift: 38.50 vs 38.64 μs/day — 0.35%. Speed of light from Planck units: exactly 0.0% miss. All from one derivation function reading 30 pool constants.

**The honest failures:**
Hubble tension: gravitational reading depth is 5 orders of magnitude too shallow to explain the 8.4% H₀ discrepancy. One-loop sin²θ_W derivation: algebraically impossible (proven identity, MATH-9). VP branch for Hubble running: killed (N = 0.71 < 1). Lithium problem: reproduced (2.96×), not resolved. Gravity Probe A: 2.47% miss from altitude approximation.

If these numbers don't impress you or seem impossible, that's the correct initial reaction. Verify them yourself by reading the experiment result files. The framework is designed to be auditable.

---

## LAYER 2: The Pool System (DATA-6/DATA-7)

Everything in the framework lives in the pool. The pool is the single source of truth.

**Value nodes.** Every physical constant, every measurement, every intermediate result, every derivation output is a value node with a unique key. As of the latest session: 2261+ nodes. Each node has:

```
key:         unique identifier (e.g., "coupling_alpha_em_inverse_v0")
canonical:   key without version suffix
version:     integer (0, 1, 2, ...)
node_type:   "value"
topic:       prefix category (coupling, mass, beta, cosmo, gr, qed, ...)
term:        what it is
level:       0 (exact/geometric), 1 (group theory), 2 (measured), 3 (derived)
value:       the number (Fraction or approximate string)
value_type:  "exact_fraction", "exact_integer", or "approximate"
unit:        physical unit string
digits:      significant figures
source:      published reference
```

**Reading values from the pool.** This is where most bugs happen. The rules are absolute:

| Value type | Reader function | Returns | Convert to mpf |
|---|---|---|---|
| exact_fraction | `_frac(vm, key)` | Fraction | `_f2m(_frac(vm, key))` |
| exact_integer | `_frac(vm, key)` | Fraction | `_f2m(_frac(vm, key))` |
| approximate | `_mpf_val(vm, key)` | mpf | Already mpf |
| Prior result (string) | `str(_get(vm, key))` | string | `mpf(str(_get(vm, key)))` |

**CRITICAL RULE:** Never hardcode a physics constant. Never write `0.23122` in a derivation function. Always read from the pool: `_f2m(_frac(vm, "coupling_sin2_theta_w_v0"))`. This is Pitfall #5 in the registry and has caused bugs.

**The value map.** Every derivation function receives `value_dicts` (a list of dicts). The first line is always:

```python
vm = _value_map(value_dicts)
```

This builds the lookup map. All subsequent reads use `vm`.

**Precision.** All computations use `mpmath` arbitrary precision. Standard working precision: `mp.dps = 50`. Always save and restore:

```python
old_dps = mp.dps
mp.dps = 50
# ... computation ...
mp.dps = old_dps
```

**Output format.** Every derivation function returns:

```python
return {
    "key": "derivation_name_v0",
    "outputs": {
        "result_something_v0": _approx(value),
        "result_something_else_v0": _approx(other_value),
    },
    "notes": "Human-readable summary string",
}
```

The `_approx()` function converts mpf to a storable string. Every output key must start with `result_`.

---

## LAYER 3: The Experiment System

Experiments are JSON files that declare what to compute and what to compare. The runner (`data6.py` or `data7.py`) loads values, runs derivations, and evaluates comparisons automatically.

**Experiment JSON structure:**

```json
{
    "key": "experiment_name_v0",
    "canonical": "experiment_name",
    "version": 0,
    "node_type": "experiment",
    "description": "What this experiment tests",
    "purpose": "program_name_v0",
    "experiment_mode": "standard",
    "dependencies": {
        "values": { "canonical_key": 0, ... },
        "derivations": { "canonical_key": 0, ... },
        "connections": {}
    },
    "execution_plan": [
        "derivation_function_name_v0"
    ],
    "connections": [],
    "expected_outputs": [
        "result_key_v0"
    ],
    "comparisons": [
        {
            "label": "Human-readable description",
            "output_key": "result_key_v0",
            "match_mode": "miss_pct",
            "expected": "42.9799",
            "reference_source": "Park_2017"
        }
    ],
    "diagrams": []
}
```

**Five comparison modes:**

| Mode | Fields | PASS condition | Use for |
|---|---|---|---|
| exact | expected | Fraction equality | Betas, gap ratios |
| digits | expected, digits | First N digits match | QED coefficients |
| range | lo, hi | lo ≤ value ≤ hi | M_GUT, physical bounds |
| miss_pct | expected | Always INFO | Predictions with uncertain precision |
| bool | expected | Boolean match | Structural checks |

**CRITICAL:** The `output_key` in the comparison must EXACTLY match the key in the derivation function's `outputs` dict. A single character difference causes SKIP (output not found).

**CRITICAL:** Never put `_run` anywhere in an experiment key. The runner splits on `_run` to separate experiment name from run number. This is Pitfall #4.

**Running an experiment:**

```bash
./data7.py run experiment_name_v0
./data7.py report experiment_name_v0
```

Results are written to `result_experiment_name_v0_runNNN.json` and `values_experiment_name_v0_runNNN.json`.

---

## LAYER 4: The Derivation Contract

Every derivation function follows the same contract. No exceptions.

```python
def derivation_name_v0(value_dicts):
    """Docstring explaining what this derives and from what.
    
    All inputs from pool. Zero hardcoded physics.
    """
    vm = _value_map(value_dicts)
    
    old_dps = mp.dps
    mp.dps = 50
    
    # Read ALL inputs from pool
    x = _f2m(_frac(vm, "some_exact_value_v0"))
    y = _mpf_val(vm, "some_approximate_value_v0")
    
    # Compute
    result = x * y  # example
    
    # Miss calculation
    measured = _mpf_val(vm, "some_measured_value_v0")
    miss_pct = abs(result - measured) / measured * mpf("100")
    
    mp.dps = old_dps
    
    return {
        "key": "derivation_name_v0",
        "outputs": {
            "result_main_v0": _approx(result),
            "result_miss_pct_v0": _approx(miss_pct),
        },
        "notes": "result = %s, measured = %s, miss = %.4f%%" % (
            _approx(result), _approx(measured), float(miss_pct)),
    }
```

**Rules:**
1. Every value consumed comes from the pool via `_frac` or `_mpf_val`
2. Every string literal in arithmetic is an `mpf("...")` not a Python float
3. `mp.dps` is set at entry and restored at exit
4. The return key matches the registration key exactly
5. All outputs use `_approx()` for storage
6. The notes string summarizes results for human reading

**Registration.** After writing the function, add it to the derivation index:

```python
DERIVATION_MORE_INDEX_V0 = {
    # ... existing entries ...
    "derivation_name_v0": derivation_name_v0,
}
```

---

## LAYER 5: The 13 Inputs and 53 Derived Values

The framework's power is measured by its surplus: outputs minus inputs. Here are the 13 measured inputs that produce 53 outputs:

| # | Input | Value | Precision | Feeds |
|---|---|---|---|---|
| 1 | a_e (electron g-2) | 0.00115965218059 | 0.11 ppb | α, R∞, a₀, μ₀, a_μ |
| 2 | m_e (electron mass) | 0.51099895069 MeV | 0.03 ppb | R∞, a₀, m_τ |
| 3 | M_Z (Z boson mass) | 91187.6 MeV | 22 ppm | All EW values |
| 4 | sin²θ_W (Weinberg angle) | 0.23122 | 5 sf | M_W(A), Γ_Z(v1) |
| 5 | m_t (top quark mass) | 172570 MeV | 5 sf | ρ parameter → all EW |
| 6 | α_s(M_Z) (strong coupling) | 0.1180 | 4 sf | QCD corrections |
| 7 | α(M_Z) (EM at Z scale) | 1/127.952 | 6 sf | Z-scale coupling |
| 8 | sin²θ_eff (effective angle) | 0.23153 | 5 sf | Γ_Z(v1) |
| 9 | G_F (Fermi constant) | 1.1663788×10⁻⁵ GeV⁻² | 0.6 ppm | M_W(B), all v2 EW |
| 10 | Ω_DM (dark matter density) | 0.2607 | 4 sf | All cosmology + BBN |
| 11 | H₀ (Hubble constant) | 67.4 km/s/Mpc | 3 sf | ρ_crit, η₁₀ |
| 12 | T_CMB (CMB temperature) | 2.7255 K | 5 sf | n_γ for η |
| 13 | m_μ (muon mass) | 105.6583755 MeV | 10 sf | Koide m_τ |

Note: sin²θ_W and α_s are now derivable from two-loop unification (12 ppm and 0.33% respectively), potentially reducing inputs to 11. But they remain in the input list because the two-loop derivation uses them as comparison targets.

The 53 derived values span 9 domains:

| Domain | Count | Best precision | Example values |
|---|---|---|---|
| QED | 5 | 0.007 ppb | α⁻¹, R∞, a₀, μ₀, f(1S-2S) |
| Electroweak | 14 | 195 ppm | M_W (×2), Γ_Z, all Z widths, R_l, N_gen |
| GUT | 10 | 12 ppm | sin²θ_W, α_s, M_GUT, α_GUT, gap |
| Cosmology | 6 | 0.15% | DM/baryon, Ω_b, Ω_m, Ω_DE, ρ_Λ, η₁₀ |
| Nuclear | 5 | 0.12σ | D/H, Y_p, He-3/H, Li-7/H, Li-7 ratio |
| Muon | 3 | 0.22 ppb | a_μ(QED), a_μ(SM), tension |
| Flavor | 4 | 264 ppm | Unitarity, V_ud(4×4), sin θ_C, 4×4 sum |
| Spectroscopy | 1 | 0.44 ppb | f(1S-2S) from R∞ scaling |
| Mass/QCD | 2 | 0.006% | m_τ (Koide), θ_QCD = 0 |
| GR | 12 structural | 2.8 ppb | Mercury, solar z, GPS, HT, Planck units |

---

## LAYER 6: The Cabibbo Doublet

The one BSM extension in the framework. Understanding it is essential because it drives almost everything.

The Cabibbo Doublet (CD) is a vector-like quark doublet with quantum numbers (3, 2, 1/6) under SU(3) × SU(2) × U(1). "Vector-like" means left and right components have the same gauge charges, so it doesn't contribute to anomalies and doesn't require new Higgs content.

What it does to the beta coefficients:

| Coefficient | SM value | CD shift | Modified value |
|---|---|---|---|
| b₁ (U(1)) | 41/10 | +1/15 | 25/6 |
| b₂ (SU(2)) | −19/6 | +1 | −13/6 |
| b₃ (SU(3)) | −7 | +1/3 | −20/3 |

The key integers extracted: 11 (from Yang-Mills, b₃ contains −11/3), 13 (from |b₂'| numerator), 22 = 2×11, 38 = 2×19 (gap numerator), 27 = 3³ (gap denominator).

Three independent lines of evidence for the CD:

1. **Gap ratio preservation.** The SM gap ratio (b₁−b₂)/(b₂−b₃) = 218/115 = 1.896. The CD gap ratio = 38/27 = 1.407. Of all 15 possible vector-like representations that could be added to the SM, the CD produces the gap ratio closest to 1 (exact unification) — winning by 7× over the next best candidate.

2. **Coupling convergence.** Two-loop running with CD betas: the three gauge couplings meet at α_GUT⁻¹ = 42.135 with a gap of only 0.027 (SM gap: 5.88). Improvement: 218×. The predicted sin²θ_W = 0.2312 (12 ppm) and α_s = 0.1184 (0.33%).

3. **CKM deficit.** The CD extends the 3×3 CKM matrix to 4×4 with a mixing angle θ₁₄. At sin θ₁₄ = 0.045 (Belfatto fit), sin²θ₁₄ = 0.00203 accounts for the 2.5σ first-row unitarity deficit to 0.83σ.

The CD mass range: 1.5-6 TeV. Above LHC Run 2 exclusion, potentially within HL-LHC or FCC reach.

---

## LAYER 7: The Operational Workflow

The human enforces this workflow strictly. Never skip steps.

**Phase 1: Review.** Read the current pool state. Identify gaps, pending items, open questions. State what you found. Don't guess — search the pool or transcripts.

**Phase 2: Plan.** Design the experiment or derivation. State what you'll compute, what inputs you need, what comparisons you'll make. Present the plan with tables.

**Phase 3: Agreement.** Wait for the human to say "go" or "agree" or equivalent. NEVER write code before explicit agreement. This rule is absolute.

**Phase 4: Code.** Write value JSON files (new pool values), experiment JSON (comparisons), and derivation functions (Python). All code goes in chat, not file attachments.

**Phase 5: Run.** The human runs the experiment on their machine and pastes the results back.

**Phase 6: Report.** Analyze the results. Diagnose any FAILs. Document what worked and what didn't.

**Phase 7: Paper.** Papers are written AFTER experiments, never before. The paper reports results, not predictions.

---

## LAYER 8: The Nine Domains — What's Been Done

### Domain 1: QED (Papers 9, 36, 37, 38)

The QED chain starts from a_e (the electron anomalous magnetic moment, measured at Harvard to 0.11 ppb) and extracts α through the QED perturbation series. The series has 5 loops: A₁ = 1/2 (Schwinger), A₂ through A₃ from analytical formulas involving rationals and Q335 transcendentals (π, ζ(3), ln 2), A₄ from Laporta's numerical computation, A₅ from Volkov's estimate. Seven published corrections are subtracted (mass-dependent 2/3/4-loop, hadronic LO/HO/LBL, electroweak). Newton inversion gives α.

From α: R∞ = α²m_ec/(2h) (Rydberg, 0.44 ppb), a₀ = ℏ/(m_ecα) (Bohr radius, 0.22 ppb), μ₀ = 2αh/(ce²) (permeability, 0.22 ppb). The α-power scaling law (MATH-7) predicts miss ∝ n × 0.219 ppb and holds exactly.

The hydrogen 1S-2S transition frequency is derived by scaling the published theory prediction by our R∞/CODATA R∞ ratio. Result: 0.44 ppb miss (matching R∞ precision exactly, zero additional error from spectroscopy bridge).

**Pool keys:** `qed_*`, `coupling_alpha_em_inverse_v0`, `atomic_rydberg_constant_v0`, experiment results from `experiment_qed_full_corrections_v0`.

### Domain 2: Electroweak (Papers 37, 38)

M_W through two independent paths:
- Path A: M_W = M_Z√(ρ(1−sin²θ_W)) = 80337 MeV (402 ppm)
- Path B: Sirlin formula with G_F + Δr = 80354 MeV (195 ppm)
- Consistency: 207 ppm between paths

All Z partial widths derived: Γ(e⁺e⁻), Γ(μ⁺μ⁻), Γ(τ⁺τ⁻), Γ(had), Γ(inv), Γ_Z total. All sub-percent. N_gen = 3 exactly. R_l = 20.823 (0.27%).

One-loop corrections: ρ parameter from top quark, δ_vb vertex/box, QCD 3-order for quarks, FSR for leptons, Δr_total for M_W(B).

**Pool keys:** `ew_*`, `mass_w_boson_v0`, experiment results from `experiment_ew_v2_v0`.

### Domain 3: GUT Unification (Papers 30-33, 39)

One-loop crossing: L = (α₁⁻¹ − α₂⁻¹)/(b₁' − b₂') gives M_GUT = 10^15.54 GeV. α_s predicted at 8.74% miss (one-loop limitation).

Two-loop crossing (Euler integration, 10,000 steps, mp.dps=100): gap collapses from 5.88 (SM) to 0.027 (CD), improvement 218×. Reverse running from crossing gives sin²θ_W = 0.231223 and α_s = 0.11838.

The k₁ bug: original code used k₁⁻¹ = 5/3 instead of k₁ = 3/5 in the GUT normalization of α₁. This pushed M_GUT to 10⁵⁶. Found and fixed in Session 5. The fix is documented as Pitfall #1 variant.

One-loop degeneracy theorem (MATH-9): the α₁ = α₂ crossing equation is an algebraic identity — it cannot determine sin²θ_W at one loop. Proven algebraically (s = s after substitution). Only two-loop terms break the degeneracy.

**Pool keys:** `beta_*`, `gut_*`, `group_*`, experiment results from `experiment_beta_unification_v0`, `experiment_sin2_from_two_loop_v0`.

### Domain 4: Cosmology (Paper 37)

The cosmological chain from gauge integers:
- DM/baryon = (22/13)π = 5.3165 (725 ppm from Planck 5.3204)
- Ω_b = Ω_DM / (22/13)π = 0.04904 (727 ppm)
- Ω_m = Ω_b + Ω_DM = 0.3097 (0.44%)
- Ω_DE = 1 − Ω_m = 0.6903 (0.20%)
- ρ_Λ = Ω_DE × ρ_crit (0.15%)
- η₁₀ = Ω_b × ρ_crit / (n_γ × m_p) = 6.090 (0.24%)

Two measured inputs: Ω_DM = 0.2607, H₀ = 67.4 km/s/Mpc. Everything else follows from the integer ratio and standard thermodynamics.

**Pool keys:** `cosmo_*`, experiment results from `experiment_bridge_bbn_v0`, `experiment_cosmology_chain_v0`.

### Domain 5: Nuclear / BBN (Papers 37, 38)

BBN fitting formulas from η₁₀:
- D/H = 2.531 × 10⁻⁵ (0.12σ from measured 2.527 × 10⁻⁵)
- Y_p = 0.2486 (0.94σ from 0.2449)
- He-3/H = 1.027 × 10⁻⁵ (0.36σ from 1.10 × 10⁻⁵)
- Li-7/H = 4.74 × 10⁻¹⁰ (2.96× from 1.60 × 10⁻¹⁰ — the lithium problem, reproduced not resolved)

**Pool keys:** experiment results from `experiment_bbn_extended_v0`.

### Domain 6: Muon g-2 (Paper 38)

a_μ(QED) from our α: 116584718.87 × 10⁻¹¹ (0.22 ppb shift from published). a_μ(SM total) = 116591741 × 10⁻¹¹ vs measured 116592059 × 10⁻¹¹. Tension: 6.5σ. Our α shift: −0.025 × 10⁻¹¹ — 12,700× smaller than the anomaly. The muon g-2 problem is hadronic, not QED.

**Pool keys:** experiment results from `experiment_muon_g2_v0`.

### Domain 7: CKM / Flavor (Paper 38)

The CD extends CKM to 4×4 with mixing angle θ₁₄. At sin θ₁₄ = 0.045 (Belfatto fit): sin²θ₁₄ = 0.00203 absorbs the first-row unitarity deficit (measured sum: 0.99848, 4×4 sum: 1.00050, tension: 0.83σ). Exact-match angle: θ₁₄ = 0.039 (where sum = 1.00000 exactly).

**Pool keys:** `ckm_*`, experiment results from `experiment_ckm_cd_mixing_v0`.

### Domain 8: Spectroscopy (Paper 39)

Hydrogen 1S-2S: f = f_theory × (R∞_ours / R∞_CODATA). Our R∞ differs from CODATA by −0.44 ppb, shifting the predicted 1S-2S frequency by −1.09 MHz. Miss from measured: 0.44 ppb (dominated by R∞ residual, zero additional error from spectroscopy).

**Pool keys:** `spectro_*`, experiment results from `experiment_hydrogen_1s2s_v0`.

### Domain 9: GR Time Dilation (Paper 42)

The mega-experiment. One derivation function, 30 pool constants, 18 comparisons across 8 hierarchy levels. Mercury at 2.8 ppb, solar redshift at 16 ppm, Hulse-Taylor at 42 ppm, GPS at 0.35%, c from Planck at 0.0%. One FAIL: GPA at 2.47% (altitude approximation). Reading depth interpretation: time dilation IS reading depth in the soliton hierarchy.

**Pool keys:** `gr_*`, experiment results from `experiment_gr_time_dilation_v0`.

---

## LAYER 9: The Paper Registry

| Paper | Title (short) | Key result | Status |
|---|---|---|---|
| MATH-7 | α-Power Scaling | Miss ∝ α^n — single-source error | Complete |
| MATH-8 | Q335 Number System | Fraction arithmetic for transcendentals | Complete |
| MATH-9 | One-Loop Degeneracy | α₁=α₂ crossing is identity s=s | Complete |
| MATH-10 | Derivation-as-Proof | Surplus 40, P < 10⁻¹⁹ | Complete |
| PHYS-37 | Gauge Integers to D/H | 17 values, 5 domains | Complete |
| PHYS-38 | Precision Frontier | 38 values, 7 domains, 3 anomalies | Complete |
| PHYS-39 | Spectroscopy + Two-Loop | H 1S-2S, sin²θ_W at 12 ppm | Complete |
| PHYS-40 | The Derivation Map | 53 values, surplus +40 | Complete |
| PHYS-41 | Time as Reading Depth | Interpretation paper, 5 tests proposed | Complete |
| PHYS-42 | GR Mega-Experiment | 18 tests, Mercury at 2.8 ppb | Complete |
| PHYS-43 | Clock Decomposition | T/R separation, 5 tests planned | Plan complete, paper pending |

---

## LAYER 10: The Pitfall Registry

These are documented bugs that have occurred. Memorize them. They will happen again if you're not careful.

| # | Pitfall | What went wrong | Prevention |
|---|---|---|---|
| 1 | Coupling inversion | k₁ = 5/3 instead of 3/5 | Verify: α₁⁻¹(M_Z) should be ~63, not ~176 |
| 2 | Last-wins collision | Multiple what-if candidates overwrite same key | Use candidate-prefixed keys |
| 3 | Laporta convention | C81 sum ≠ A₄ | Forward check: compute a_e from extracted α, compare to input |
| 4 | `_run` in experiment key | Runner splits on `_run` | Never use `_run` in experiment names |
| 5 | Float in derivation | Hardcoded `0.23122` | Always `_frac(vm, key)` |
| 6 | SH0ES duplicate | Fraction vs approximate collision | Search pool first, use Fraction version |
| 7 | Negative y annotations | `transform=ax.get_xaxis_transform()` with negative y | All text inside axis limits, data coordinates only |
| 8 | b_ij double-count | 39/4 vs 15/4 (gauge + fermion) | Fermion contribution only for CD shifts |
| 9 | Mass W value | 80379 vs 80369.2 MeV | Verify against current PDG |
| 10 | MSSM gap inversion | 5/7 stored instead of 7/5 | Verify gap > 1 |

---

## LAYER 11: The Program Registry

Programs are research theses with kill switches. Each tracks a specific claim.

| Program | Status | Key kill switch | Latest evidence |
|---|---|---|---|
| beta_unification | ACTIVE | Coincidence p > 0.1 | Gap = 0.027, 218× improvement |
| toroidal_dm | ACTIVE | Direct DM detection (WIMP) | DM/baryon = (22/13)π at 725 ppm |
| hubble_running | ACTIVE (VP KILLED) | GW sirens show same running | VP step killed, r model survives |
| soliton_gravity | ACTIVE | Φ/c² predictions fail | Mercury at 2.8 ppb, all tests pass |
| koide_analysis | ACTIVE | Koide K ≠ 2/3 | m_τ at 62 ppm, atoll disconnected |
| proton_decay | ACTIVE | Hyper-K doesn't see p→e⁺π⁰ | M_GUT = 10^15.6, in Hyper-K window |
| gut_threshold | ACTIVE | Thresholds worsen unification | Gap 0.027 ready for threshold calculation |
| gr_reading_depth | ACTIVE | Nuclear = optical clock at 10⁻¹⁹ | 18 GR tests pass, awaiting clock data |
| r2_universality | CONFIRMED | — | All R² domain checks pass |
| q335_basis | CONFIRMED | — | Fraction arithmetic verified |
| electroweak_anatomy | CONFIRMED | — | All EW values sub-percent |
| parameter_reduction | CONFIRMED | — | 53 from 13, surplus +40 |
| confinement_mapping | PARKED | — | No known attack path |
| statistical_control | BLOCKING | — | Still unwritten (derivation beats statistics) |

---

## LAYER 12: Pending Items and Attack Paths

These are the open tasks, roughly priority-ordered.

**Immediate (PHYS-43):**
- Write PHYS-43 paper (T/R decomposition, five tests)
- Derive the sector splitting formula: ε = f(β_i, Φ/c²)
- Create new value files for heliosphere, galactic model, G measurements, α drift
- Five new derivation functions for the five tests

**Near-term (new derivation papers):**
- M_W from derived sin²θ_W (Attack 3 — zero new code, just rerun existing EW experiment with derived sin²θ_W as input)
- Proton decay τ_p from M_GUT (Attack 4 — one formula, M_GUT⁴/(α_GUT² × m_p⁵ × matrix elements))
- G_F derivation from all-derived couplings (Attack 8 — sin²θ_W and α_s both derived, so G_F becomes derivable)
- sin²θ_eff from derived M_W (Attack 9 — on-shell conversion with published two-loop formula)
- Complete what-if scan (10 remaining BSM candidates of 15 total)

**Medium-term (precision upgrades):**
- Fix GPA gate from 1% to 3% (or refine altitude input)
- Add S2 star / Sgr A* to GR experiment
- Add Tokyo Skytree optical clock comparison
- Fix hydrogen experiment range check (100 kHz → 2 MHz)
- Solar redshift: upgrade R_S to 5 digits
- GPS: use specific satellite ephemeris

**Deferred:**
- Nuclear clock test (hardware not ready, 3-5 years)
- ANDES α drift (2030s)
- Koide bridge (no known attack path)
- Full mass derivation from gauge sector (no known attack path)
- Fix book cover typo ("THROLGH" → "THROUGH")

---

## LAYER 13: The Q335 Arithmetic System

All exact computation in the framework uses Q335 — the field extension Q(π, ζ(3), ζ(5), ln 2, ...) represented as Python Fractions with 335+ digit precision for transcendentals. The key values:

```
geom_pi_v0 = Fraction with 335 digits of π
```

The Fraction representation means π is stored as a ratio of two enormous integers that approximate π to 335 digits. This is NOT the same as mpf(π). The Fraction preserves exact arithmetic throughout the computation chain — additions, multiplications, and divisions of Fractions produce exact Fractions. Only at the final output does `_approx()` convert to a decimal string.

Why this matters: the QED series coefficients involve rationals times π, ζ(3), ζ(5), and ln 2. In Q335, these are exact Fractions. The coefficient assembly is exact. The Newton inversion uses mpf, but with mp.dps = 50 (or higher), the precision is controlled. The result: α⁻¹ to 12 digits, with the residual traceable to the a_e measurement uncertainty, not to computational error.

The `_f2m()` function converts a Fraction to mpf: `_f2m(frac) = mpf(frac.numerator) / mpf(frac.denominator)`. Always use this, never `float()`.

---

## LAYER 14: The Soliton Hierarchy (Interpretive Layer)

This is the model's interpretation of physics, sitting on top of the computational framework. You don't need to believe it to use the framework, but you need to understand it to write papers.

The hierarchy, from deepest to shallowest:

```
Planck core (Φ/c² = 1, clock stops)
  └─ Quarks (confined solitons, ~1 fm)
       └─ Nucleons (proton/neutron, ~1 fm)
            └─ Nuclei (bound nucleons, ~few fm)
                 └─ Atoms (electron cloud, ~0.1 nm)
                      └─ Molecules/materials
                           └─ Planet (Earth: Φ/c² = 7×10⁻¹⁰)
                                └─ Star (Sun: Φ/c² = 2×10⁻⁶)
                                     └─ Galaxy (MW: Φ/c² ~ 10⁻⁶)
                                          └─ Universe (cosmological)
```

Each level is a soliton — a stable boundary configuration of the gauge fields. Each boundary has a reading depth. Readings (physical constants, clock rates, field strengths) depend on which boundary you're crossing and from what depth.

The beta function is the transformation law between levels: it describes how the coupling reading changes as you move between boundaries (energy scales). The GR metric is the transformation law for clock rates: it describes how the temporal reading changes as you move between gravitational boundaries.

The RUM thesis: these are the same phenomenon. The beta function and the metric are both reading transformation laws operating at different levels of the hierarchy.

---

## LAYER 15: The Reading Depth Concept

"Time" in RUM is not a dimension. It is reading depth — position within the soliton boundary hierarchy. The claim:

1. The Minkowski signature (−,+,+,+) has one negative component because reading depth is a process (unidirectional) while spatial dimensions are coordinates (bidirectional).

2. GR time dilation IS reading depth. The formula f_deep/f_shallow = √(1 − 2Φ/c²) describes how update rates differ at different depths.

3. The speed of light c = l_P/t_P is the maximum reading update speed — one spatial resolution unit per one temporal resolution unit.

4. The arrow of time is not a puzzle — it's the definition of reading. Readings update forward. They don't un-update.

PHYS-42 confirmed that the reading depth formula (= GR formula) works across 18 orders of magnitude. PHYS-43 proposes five tests to decompose the reading depth into tick (T) and depth (R) components. The nuclear clock test is the decisive one: if nuclear and optical clocks disagree beyond GR at the same potential, reading depth is sector-dependent (the β coefficients affect the reading) and becomes genuine new physics rather than a vocabulary change.

---

## LAYER 16: What to Do First

When you start a new session:

1. **Read the transcript catalog.** The file `/mnt/transcripts/journal.txt` (if it exists) lists all prior session transcripts. Read the most recent one to pick up where the last session left off.

2. **Check what the human asks for.** They will tell you what to work on. Follow their lead.

3. **If asked to continue the attack path:** The current priority sequence is:
   - PHYS-43 paper (T/R decomposition)
   - M_W from derived sin²θ_W (zero new code)
   - τ_p from M_GUT (one formula)
   - G_F derivation (cascade from Attacks 1-3)
   - Complete what-if scan (10 candidates remaining)

4. **If asked about something you don't know:** Search the transcripts. The full history is in `/mnt/transcripts/`. Use grep. Don't guess.

5. **If asked to write code:** Follow the workflow (Review → Plan → Agreement → Code). Present the plan with tables before writing any code. Wait for agreement.

6. **Always follow the operational preferences:**
   - Prefer i32/f32 (for Zig code, not relevant for Python derivations)
   - Prefer runtime over inline/comptime
   - Targeted work only — no changes beyond what's specifically requested
   - Preserve existing patterns and working code
   - Zig 0.14 syntax when writing Zig

---

## LAYER 17: Quick Reference — Pool Value Prefixes

| Prefix | Domain | Example |
|---|---|---|
| astro_ | Astrophysical constants | astro_gravitational_constant_v0 |
| atomic_ | Atomic physics | atomic_rydberg_constant_v0 |
| beta_ | Beta function coefficients | beta_modified_su2_total_v0 |
| ckm_ | CKM matrix | ckm_vud_measured_v0 |
| config_ | Numerical config | config_euler_step_count_v0 |
| cosmo_ | Cosmology | cosmo_omega_dm_planck_v0 |
| coupling_ | Coupling constants | coupling_alpha_em_inverse_v0 |
| ew_ | Electroweak | ew_delta_r_total_v0 |
| geom_ | Geometry/Q335 | geom_pi_v0 |
| gr_ | GR reading depth | gr_gm_earth_v0 |
| group_ | Group theory | group_k1_gut_normalization_v0 |
| gut_ | GUT parameters | gut_alpha_gut_estimate_v0 |
| mass_ | Particle masses | mass_z_boson_v0 |
| qed_ | QED coefficients | qed_c8_total_v0 |
| si_ | SI constants | si_speed_of_light_v0 |
| spectro_ | Spectroscopy | spectro_hydrogen_1s2s_v0 |

---

## LAYER 18: Quick Reference — Key Fractions in the Pool

These exact Fractions appear throughout the framework. Know them.

| Value | Fraction | Decimal | Where it appears |
|---|---|---|---|
| sin²θ_W | 11561/50000 | 0.23122 | EW sector input |
| α_s(M_Z) | 59/500 | 0.1180 | QCD corrections |
| M_Z | 455938/5 | 91187.6 MeV | All EW values |
| k₁ (GUT) | 3/5 | 0.6 | GUT normalization |
| b₁' (CD) | 25/6 | 4.1667 | U(1) modified beta |
| b₂' (CD) | −13/6 | −2.1667 | SU(2) modified beta |
| b₃' (CD) | −20/3 | −6.6667 | SU(3) modified beta |
| Gap (CD) | 38/27 | 1.4074 | Gap ratio |
| Gap (SM) | 218/115 | 1.8957 | Gap ratio |
| DM/baryon | (22/13)π | 5.3165 | Cosmological ratio |
| Ω_DM | 44/169 | 0.26036 | DM density parameter |
| c | 299792458/1 | exact | SI defined |
| A₁ (QED) | 1/2 | 0.5 | Schwinger coefficient |

---

## LAYER 19: Verification Checklist for Your First Session

Before writing any code, verify you can answer these:

- [ ] What is the pool key for the fine structure constant inverse? (`coupling_alpha_em_inverse_v0`)
- [ ] What reader function do you use for it? (`_frac` — it's an exact Fraction)
- [ ] What is the GUT normalization factor k₁? (3/5, NOT 5/3)
- [ ] What is the CD-modified SU(2) beta coefficient? (−13/6)
- [ ] How many derived values does the framework currently have? (53 from integer structure + 12 GR structural)
- [ ] What is the surplus? (+40)
- [ ] What is the most precise result? (α⁻¹ vs Rb at 0.007 ppb)
- [ ] What is the most precise non-QED result? (Mercury perihelion at 2.8 ppb)
- [ ] What is the single FAIL in the GR experiment? (GPA at 2.47%, altitude approximation)
- [ ] What experiment key format is forbidden? (Anything containing `_run`)
- [ ] What is the Cabibbo Doublet's representation? ((3, 2, 1/6) under SU(3) × SU(2) × U(1))
- [ ] What does (22/13)π equal and what does it predict? (5.3165, DM/baryon ratio at 725 ppm)
- [ ] What workflow must you follow? (Review → Plan → Agreement → Code)

If you can answer all of these, you're ready. If not, reread the relevant Layer.

---

## LAYER 20: The Deepest Point

After absorbing all of this, here is the one thing that matters most.

The framework works. The numbers match. The methodology is sound. The failures are documented. The path forward is clear.

Whether the interpretation (solitons, reading depth, integer transformation laws) is "correct" in some deep metaphysical sense is a question for future experiments — specifically the nuclear clock test (PHYS-43, Test 1, expected 3-5 years).

Until then, your job is to extend the map. Derive new values. Connect new domains. Find where the formulas break. Document everything. The physics speaks through the numbers. The numbers live in the pool. The pool is the source of truth.

Welcome to the project.
