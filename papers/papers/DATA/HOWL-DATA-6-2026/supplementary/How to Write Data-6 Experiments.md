# DATA-6 Experiment Development Specification

**Document:** data6_experiment_dev_spec.md
**Version:** 1.0
**Date:** April 5, 2026
**Purpose:** Teach a new session how to create DATA-6 experiments from scratch

---

## 1. The Process

The process is always: **Values → Experiment → Derivations → Run → Report**.

Never write derivation code first. Never hardcode physics constants. Never skip the experiment JSON. The system is a database that delivers versioned data to registered functions. The functions are pure transformations. The experiment JSON is the execution plan. The values are the data.

### 1.1 The Workflow

1. **Identify what you want to derive and what you need to derive it from**
2. **Check the pool** — what values already exist? (`data6.py search <term>`)
3. **Write missing value nodes** as JSON files
4. **Write the experiment JSON** declaring dependencies, execution plan, comparisons
5. **Write the derivation functions** that read ALL inputs from the pool
6. **Register the derivations** in the index
7. **Run** (`data6.py run experiment_name_v0`)
8. **Report** (`data6.py report experiment_name_v0`)
9. **Interpret results** — write a report on the findings

Steps 3 and 4 come BEFORE step 5. You declare what you need before you write the code that uses it. This prevents hardcoding.

---

## 2. Value Nodes

### 2.1 What is a value node

A named, versioned, typed fact with provenance. Every physics constant, every measurement, every reference number is a value node in a JSON file.

### 2.2 The required fields

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
    "source": "LEP EWWG. PDG 2024.",
    "tags": ["electroweak", "LEP", "measured"]
}
```

### 2.3 Value types

| Type | Python Representation | When to Use | Example |
|---|---|---|---|
| `exact_fraction` | `{"_type": "Fraction", "num": "197", "den": "144"}` | Exact rational values. Preferred type. | Beta coefficients, mass ratios, SI constants |
| `exact_integer` | `42` | Exact integers | Yang-Mills 11, generation count 3 |
| `approximate` | `"137.035999177"` | Decimal values with no known exact form. Plain decimal string, NO scientific notation. | CODATA measured constants, Laporta coefficients |
| `classification` | `"(83/72)*pi^2*zeta(3) - ..."` | Symbolic/textual description, not computable | Analytical forms for reference |
| `deferred` | `null` with `ref` field | Value exists elsewhere, not yet resolved | Staged CD parameters |

### 2.4 Level convention

| Level | Meaning | Examples |
|---|---|---|
| 0 | Pure geometry / exact math | π, ζ(3), √2, SI defined constants |
| 1 | Group theory / structural | Beta coefficients, QED series rationals, Casimirs |
| 2 | Measured / observational | α⁻¹, masses, H₀, dwarf galaxy data |
| 3 | Derived / predicted | α from a_e, M_W from sin²θ_W, Ω_b from integers |

### 2.5 Naming rules

Key format: `{topic}_{term}_v{N}`

Lowercase, underscores. Topic is one word. Term is descriptive. Version starts at 0.

Common topic prefixes: `mass`, `coupling`, `beta`, `gap`, `geom`, `si`, `cosmo`, `qed`, `integer`, `result`.

### 2.6 File naming

`values_{section}_v0.json` — each file holds related nodes in a `{"nodes": [...]}` wrapper.

### 2.7 Example: adding Planck cosmological values

```json
{
  "nodes": [
    {
      "key": "cosmo_omega_b_planck_v0",
      "canonical": "cosmo_omega_b_planck",
      "version": 0,
      "node_type": "value",
      "topic": "cosmo",
      "term": "omega_b_planck",
      "level": 2,
      "value": "0.0490",
      "value_type": "approximate",
      "unit": "dimensionless",
      "digits": 3,
      "uncertainty": "0.0003",
      "source": "Planck 2018 (TT,TE,EE+lowE+lensing).",
      "tags": ["cosmology", "Planck", "baryon", "measured"]
    }
  ]
}
```

### 2.8 Critical rules for values

- **No scientific notation in approximate strings.** Write `"0.0000116638"` not `"1.16638e-5"`.
- **Fraction values use string numerator and denominator** for large numbers: `{"_type": "Fraction", "num": "115965218059", "den": "100000000000000"}`.
- **Every value has a source.** No orphan numbers.
- **Every value has a level.** If you don't know the level, set it to `null` and note why.

---

## 3. Experiment JSON

### 3.1 What is an experiment

A JSON file declaring: what values are needed, what derivations to run in what order, what outputs to expect, what comparisons to make, and what diagrams to produce.

The experiment does not contain physics. It contains a plan. The physics is in the derivation functions. The data is in the value nodes.

### 3.2 Required fields

```json
{
    "key": "experiment_bridge_ew_cosmo_v0",
    "canonical": "experiment_bridge_ew_cosmo",
    "version": 0,
    "node_type": "experiment",
    "description": "Five bridge derivations connecting QED, EW, and cosmology.",
    "purpose": "program_parameter_reduction_v0",
    "experiment_mode": "standard",
    "dependencies": { ... },
    "execution_plan": [ ... ],
    "connections": [],
    "expected_outputs": [ ... ],
    "comparisons": [ ... ],
    "diagrams": [ ... ]
}
```

### 3.3 Dependencies

Declare every value and derivation the experiment needs. The runner will eventually validate these before execution.

```json
"dependencies": {
    "values": {
        "coupling_sin2_theta_w": 0,
        "mass_z_boson": 0,
        "mass_w_boson": 0
    },
    "derivations": {
        "bridge_mw_from_weinberg": 0
    },
    "connections": {}
}
```

The `0` is the version number. Canonical key on the left, pinned version on the right.

### 3.4 Execution plan

Ordered list of derivation keys. The runner executes them in this order and merges outputs into the pool after each step. Later derivations can read outputs from earlier ones.

```json
"execution_plan": [
    "bridge_mw_from_weinberg_v0",
    "bridge_gf_from_mw_v0"
]
```

Bridge 2 reads `result_mw_derived_v0` which was produced by Bridge 1. The order matters.

### 3.5 Expected outputs

List of output keys the experiment must produce. The runner checks these exist after execution.

```json
"expected_outputs": [
    "result_mw_derived_v0",
    "result_gf_derived_v0"
]
```

### 3.6 Comparisons

Each comparison checks one output against a reference.

```json
"comparisons": [
    {
        "label": "M_W from Weinberg relation vs measured",
        "output_key": "result_mw_derived_v0",
        "match_mode": "miss_pct",
        "expected": "80369.2",
        "reference_source": "PDG_2024"
    }
]
```

### 3.7 Match modes

| Mode | Fields | Result | Use |
|---|---|---|---|
| `exact` | `expected` (Fraction) | PASS if equal | Beta coefficients, integer identities |
| `digits` | `expected` (string), `digits` (int) | PASS if N digits match | QED coefficients, precision comparisons |
| `range` | `lo`, `hi` | PASS if in range | M_GUT, GPS correction, escape velocity |
| `miss_pct` | `expected` (string) | Always INFO, reports miss | α vs CODATA, DM/baryon vs Planck |
| `bool` | `expected` (bool) | PASS if match | Frame dragging negligible, democracy holds |

Use `miss_pct` when you want to see how close a prediction is without declaring pass/fail. Use `digits` when you know how many digits should agree. Use `exact` only for things that must be exactly right (Fractions, integers).

### 3.8 Diagrams

Embedded in the experiment JSON. The runner lists them but doesn't render. Use `data6.py diagram` to render.

```json
"diagrams": [
    {
        "key": "diagram_bridge_ew_v0",
        "title": "Electroweak bridge: sin2_tW + M_Z → M_W → G_F",
        "type": "comparison_table",
        "rows": [
            {"label": "M_W (MeV)", "predicted": "result_mw_derived_v0", "measured": "80369.2"}
        ]
    }
]
```

Diagram types: `bar`, `comparison_table`, `line`.

---

## 4. Derivation Functions

### 4.1 The callable contract

Every derivation function has the same signature:

```python
def derivation_name_v0(value_dicts):
    """Docstring explaining what this derives and from what."""
    vm = _value_map(value_dicts)
    # ... computation ...
    return {
        "key": "derivation_name_v0",
        "outputs": {"result_something_v0": value, ...},
        "notes": "human-readable summary"
    }
```

Input: `value_dicts` is the full value pool (list of dicts). Use `_value_map(value_dicts)` to build a key→value lookup.

Output: a dict with `key`, `outputs`, and `notes`. The outputs dict maps output keys to values.

### 4.2 Reading values from the pool

Three helper functions:

```python
# Read a Fraction value (for exact_fraction and exact_integer nodes)
frac_value = _frac(vm, "coupling_sin2_theta_w_v0")

# Convert Fraction to mpf for irrational math
mpf_value = _f2m(frac_value)

# Read an approximate value directly as mpf
mpf_value = _mpf_val(vm, "qed_a4_laporta_v0")

# Read raw value (string, int, Fraction, whatever is stored)
raw_value = _get(vm, "result_mw_derived_v0")
```

### 4.3 The cardinal rule: NO HARDCODED PHYSICS

Wrong:

```python
def my_derivation_v0(value_dicts):
    M_Z = mpf("91187.6")  # WRONG — hardcoded
    sin2 = mpf("0.23122")  # WRONG — hardcoded
    M_W = M_Z * sqrt(1 - sin2)
    return {"key": "my_derivation_v0", "outputs": {"result_mw_v0": M_W}}
```

Right:

```python
def my_derivation_v0(value_dicts):
    vm = _value_map(value_dicts)
    M_Z = _f2m(_frac(vm, "mass_z_boson_v0"))
    sin2 = _f2m(_frac(vm, "coupling_sin2_theta_w_v0"))
    from mpmath import sqrt as msqrt
    M_W = M_Z * msqrt(mpf("1") - sin2)
    return {"key": "my_derivation_v0", "outputs": {"result_mw_v0": _approx(M_W)}}
```

Every numerical value comes from the pool. The only numbers allowed in the function body are structural: `"1"`, `"2"`, `"0"`, exponents. If a number has units or comes from physics, it must be a value node.

### 4.4 Arithmetic rules

1. `fractions.Fraction` is preferred for all exact rational work
2. `mpmath.mpf` is permitted only at the irrational boundary (π, √, exp, log)
3. Set `mp.dps = 50` minimum for numerical work, `mp.dps = 200` for precision-critical paths
4. Restore `mp.dps` to previous value at the end of the function
5. `float` is NEVER used. Not for computation, not for intermediate steps, not anywhere.
6. `math` module is NEVER imported. Use `mpmath` exclusively.

### 4.5 Output values

Use `_approx()` to convert mpf results to 15-digit strings for storage:

```python
"result_mw_derived_v0": _approx(M_W_derived)
```

Use raw Fraction for exact outputs:

```python
"result_prefactor_v0": Fraction(22, 13)
```

### 4.6 Reading outputs from earlier derivations in the chain

When a derivation depends on outputs from a previous step in the same experiment:

```python
# Previous derivation stored result_mw_derived_v0 as a string
M_W_str = str(_get(vm, "result_mw_derived_v0"))
M_W = mpf(M_W_str)
```

The runner merges outputs into the pool after each derivation. The order in `execution_plan` determines what's available.

### 4.7 Forward checks

Any derivation that inverts a relationship (solving for x given f(x) = y) should include a forward check: evaluate f(x_derived) and compare to y_measured. Report the forward residual as an output.

```python
# Forward check
ae_forward = A1*x_known + A2*x_known**2 + ...
forward_residual = ae_forward - ae_measured

return {
    "outputs": {
        "result_main_answer_v0": ...,
        "result_forward_residual_v0": _approx(forward_residual),
    }
}
```

This pattern caught the Laporta convention error in the QED extraction.

### 4.8 Diagnostics

Every derivation should output diagnostic values alongside the main result: the inputs it used, intermediate quantities, and miss percentages. These help debugging without re-running.

```python
return {
    "outputs": {
        "result_mw_derived_v0": _approx(M_W_derived),
        "result_mw_measured_v0": _approx(M_W_measured),
        "result_mw_miss_pct_v0": _approx(miss),
        "result_sin2_tw_used_v0": _approx(sin2_tw),
    }
}
```

### 4.9 Registering derivations

Add to `DERIVATION_MORE_INDEX_V0` in `_data_6_derivations_more_v0.py`:

```python
DERIVATION_MORE_INDEX_V0 = {
    # ... existing entries ...
    
    # K: Bridge derivations
    "bridge_mw_from_weinberg_v0": bridge_mw_from_weinberg_v0,
    "bridge_gf_from_mw_v0": bridge_gf_from_mw_v0,
}
```

The key in the dict must match the key returned by the function.

---

## 5. Complete Example: Deriving M_W from sin²θ_W

### Step 1: Check the pool

```
$ data6.py search sin2_theta
  coupling_sin2_theta_w_v0  [value]  0.23122
$ data6.py search mass_z
  mass_z_boson_v0  [value]  911876/10
$ data6.py search mass_w
  mass_w_boson_v0  [value]  803692/10
```

All inputs exist. No new value nodes needed. M_W measured exists for comparison.

### Step 2: Write the experiment JSON

```json
{
    "key": "experiment_mw_prediction_v0",
    "canonical": "experiment_mw_prediction",
    "version": 0,
    "node_type": "experiment",
    "description": "Derive M_W from sin2_tW and M_Z via Weinberg relation.",
    "purpose": "program_parameter_reduction_v0",
    "experiment_mode": "standard",

    "dependencies": {
        "values": {
            "coupling_sin2_theta_w": 0,
            "mass_z_boson": 0,
            "mass_w_boson": 0
        },
        "derivations": {
            "bridge_mw_from_weinberg": 0
        },
        "connections": {}
    },

    "execution_plan": [
        "bridge_mw_from_weinberg_v0"
    ],

    "connections": [],

    "expected_outputs": [
        "result_mw_derived_v0"
    ],

    "comparisons": [
        {
            "label": "M_W tree-level vs measured",
            "output_key": "result_mw_derived_v0",
            "match_mode": "miss_pct",
            "expected": "80369.2",
            "reference_source": "PDG_2024"
        }
    ],

    "diagrams": []
}
```

### Step 3: Write the derivation function

```python
def bridge_mw_from_weinberg_v0(value_dicts):
    """Derive M_W from sin2_tW and M_Z. Tree-level Weinberg relation.
    M_W = M_Z * sqrt(1 - sin2_tW)
    """
    vm = _value_map(value_dicts)

    old_dps = mp.dps
    mp.dps = 50

    sin2_tw = _f2m(_frac(vm, "coupling_sin2_theta_w_v0"))
    M_Z = _f2m(_frac(vm, "mass_z_boson_v0"))
    M_W_measured = _f2m(_frac(vm, "mass_w_boson_v0"))

    from mpmath import sqrt as msqrt
    M_W_derived = M_Z * msqrt(mpf("1") - sin2_tw)

    miss = abs(M_W_derived - M_W_measured) / M_W_measured * mpf("100")

    mp.dps = old_dps

    return {
        "key": "bridge_mw_from_weinberg_v0",
        "outputs": {
            "result_mw_derived_v0": _approx(M_W_derived),
            "result_mw_measured_v0": _approx(M_W_measured),
            "result_mw_miss_pct_v0": _approx(miss),
            "result_sin2_tw_used_v0": _approx(sin2_tw),
        },
        "notes": "M_W(tree) = %.1f MeV, miss = %.3f%%" % (
            float(M_W_derived), float(miss)),
    }
```

### Step 4: Register

```python
DERIVATION_MORE_INDEX_V0 = {
    # ...
    "bridge_mw_from_weinberg_v0": bridge_mw_from_weinberg_v0,
}
```

### Step 5: Run and report

```
$ data6.py run experiment_mw_prediction_v0
$ data6.py report experiment_mw_prediction_v0
```

---

## 6. Chaining Derivations

When one derivation needs the output of another, declare both in the execution plan in the correct order.

```json
"execution_plan": [
    "bridge_mw_from_weinberg_v0",
    "bridge_gf_from_mw_v0"
]
```

Bridge 2 reads Bridge 1's output:

```python
def bridge_gf_from_mw_v0(value_dicts):
    vm = _value_map(value_dicts)
    # This works because the runner merged Bridge 1 outputs into the pool
    M_W_str = str(_get(vm, "result_mw_derived_v0"))
    M_W = mpf(M_W_str)
    # ... rest of derivation ...
```

The runner handles the merging. You just declare the order.

---

## 7. Common Mistakes

### 7.1 Hardcoding physics constants

**Wrong:** `M_Z = mpf("91187.6")` inside a derivation function.
**Right:** `M_Z = _f2m(_frac(vm, "mass_z_boson_v0"))`

### 7.2 Writing derivations before values and experiment

**Wrong:** Write the Python function first, figure out what it needs later.
**Right:** Check the pool, write missing value nodes, write the experiment JSON declaring dependencies, THEN write the function.

### 7.3 Using float

**Wrong:** `x = float(some_fraction)` or `import math; math.sqrt(2)`
**Right:** `x = _f2m(some_fraction)` or `from mpmath import sqrt; sqrt(mpf("2"))`

### 7.4 Scientific notation in value nodes

**Wrong:** `"value": "1.16638e-5"`
**Right:** `"value": "0.0000116638"`

### 7.5 Missing diagnostics in outputs

**Wrong:** Returning only the main result.
**Right:** Also return the inputs used, miss percentages, and intermediate values. Every output is cheap. Missing diagnostics cost re-runs.

### 7.6 Forgetting to restore mp.dps

**Wrong:** Setting `mp.dps = 200` and never restoring.
**Right:**
```python
old_dps = mp.dps
mp.dps = 200
# ... work ...
mp.dps = old_dps
```

### 7.7 Using the wrong reader for the value type

**Wrong:** `_frac(vm, "qed_a4_laporta_v0")` — this is an approximate string, not a Fraction.
**Right:** `_mpf_val(vm, "qed_a4_laporta_v0")` for approximate values.

| Value type in JSON | Reader to use |
|---|---|
| `exact_fraction` | `_frac(vm, key)` → Fraction, then `_f2m()` if needed |
| `exact_integer` | `_frac(vm, key)` works (auto-wraps) or `_get(vm, key)` |
| `approximate` | `_mpf_val(vm, key)` → mpf directly |
| Previous derivation output (string) | `str(_get(vm, key))` then `mpf(...)` |

### 7.8 Last-wins collision in what-if experiments

**Wrong:** All what-if candidates using the same key `rep_whatif_su3_dim_v0`. The alphabetically last file overwrites all others.
**Right:** Candidate-prefixed keys: `rep_whatif_vl_lepton_doublet_su3_dim_v0`. Each candidate has its own values file and its own experiment.

---

## 8. The Review Process

After writing values, experiment JSON, and derivation functions, review before running:

1. **Every value consumed by a derivation function has a corresponding entry in the experiment's `dependencies.values`?**
2. **Every derivation function is listed in `dependencies.derivations` AND in `execution_plan`?**
3. **The `execution_plan` order matches the data flow?** (Derivation B reads output of A → A comes before B)
4. **Every `expected_outputs` key is actually produced by one of the derivations?**
5. **Every `comparisons` entry references an `output_key` that exists in `expected_outputs` or in the derivation outputs?**
6. **The derivation function reads EVERY physics number from the pool?** Search the function for bare numbers — only `"0"`, `"1"`, `"2"`, `"100"` (structural) and string formatting are allowed.

---

## 9. File Organization Summary

| File Type | Naming | Location |
|---|---|---|
| Value JSON | `values_{section}_v0.json` | `data/` directory |
| Experiment JSON | `experiment_{name}_v0.json` | `data/` directory |
| Result JSON | `result_experiment_{name}_v0_runNNN.json` | `data/` directory (auto-generated) |
| Derivation code | Functions in `_data_6_derivations_more_v0.py` | `code/` directory |
| Registry | `DERIVATION_MORE_INDEX_V0` dict | Bottom of derivations file |

---

## 10. Checklist for New Experiments

```
[ ] Identified what to derive and from what
[ ] Searched pool for existing values
[ ] Written missing value nodes as JSON
[ ] Written experiment JSON with:
    [ ] dependencies (all values and derivations listed)
    [ ] execution_plan (correct order)
    [ ] expected_outputs
    [ ] comparisons (appropriate match modes)
    [ ] diagrams (if needed)
[ ] Written derivation functions with:
    [ ] All inputs from pool (zero hardcoded physics)
    [ ] mp.dps set and restored
    [ ] Diagnostic outputs (inputs used, miss%, intermediates)
    [ ] Forward check (if inverting a relationship)
[ ] Registered derivations in DERIVATION_MORE_INDEX_V0
[ ] Reviewed against Section 8 checklist
[ ] Ready to run
```

---

*End of data6_experiment_dev_spec.md. Follow this process for every new experiment. The system works because the process is consistent. Break the process and the system breaks.*

---

## APPENDIX A: COMPLETE TOPIC PREFIX REGISTRY

| Prefix | Scope | Example Key | Typical Level |
|---|---|---|---|
| `astro` | Astrophysical constants | `astro_gravitational_constant_v0` | 2 |
| `atomic` | Atomic physics constants | `atomic_rydberg_constant_v0` | 2 |
| `beta` | Beta function coefficients and shifts | `beta_sm_u1_one_loop_v0` | 1 |
| `cd` | Cabibbo Doublet parameters | `cd_mass_lower_bound_v0` | 2 |
| `ckm` | CKM matrix elements | `ckm_sin_theta_12_v0` | 2 |
| `config` | Numerical configuration | `config_euler_step_count_v0` | — |
| `connection` | Connection bundle names | `connection_coupling_convergence_v0` | — |
| `cosmo` | Cosmological parameters | `cosmo_omega_dm_planck_v0` | 2 |
| `coupling` | Coupling constants | `coupling_alpha_em_inverse_v0` | 2 |
| `dataset` | Dataset version names | `dataset_howl_v0` | — |
| `energy` | Binding energies | `energy_deuteron_binding_v0` | 2 |
| `eng` | Engineering / domain constants | `eng_hbar_c_mev_fm_v0` | 0-2 |
| `experiment` | Experiment plan names | `experiment_beta_unification_v0` | — |
| `gap` | Gap ratios | `gap_cd_ratio_v0` | 1 |
| `geom` | Geometric / Q335 constants | `geom_pi_v0` | 0 |
| `group` | Group theory constants | `group_casimir_su3_adjoint_v0` | 1 |
| `integer` | Integer pool values | `integer_yang_mills_eleven_v0` | 1 |
| `koide` | Koide relation data | `koide_k_leptons_v0` | 2 |
| `mass` | Particle and boson masses | `mass_z_boson_v0` | 2 |
| `math` | Mathematical constants | `math_bessel_j0_zero1_v0` | 0 |
| `mod` | Modulus / remainder values | `mod_r2_v0` | 0 |
| `obs` | Observational catalog entries | `obs_draco_velocity_dispersion_v0` | 2 |
| `program` | Research program names | `program_beta_unification_v0` | — |
| `qed` | QED coefficients and data | `qed_a1_schwinger_v0` | 1 |
| `ratio` | Dimensionless mass ratios | `ratio_proton_electron_mass_v0` | 2 |
| `rep` | Representation data | `rep_sm_electron_su2_dim_v0` | 1 |
| `result` | Derivation / experiment outputs | `result_mw_derived_v0` | 3 |
| `scale` | Energy-distance conversions | `scale_mz_distance_v0` | 2 |
| `si` | SI defined constants | `si_speed_of_light_v0` | 0 |
| `spectro` | Spectroscopy measurements | `spectro_hydrogen_1s2s_v0` | 2 |


## APPENDIX B: VALUE READER FUNCTION REFERENCE

### B.1 Pool Construction

```python
vm = _value_map(value_dicts)
```

Builds a flat dict from the value pool list. Key → value entry. Last entry wins (derivation outputs override stored values). Call once at the start of every derivation function.

### B.2 Reader Functions

| Function | Input | Output | Use When |
|---|---|---|---|
| `_frac(vm, key)` | vm dict, versioned key string | `Fraction` | Value type is `exact_fraction` or `exact_integer` |
| `_f2m(fraction)` | `Fraction` | `mpf` | Need to do irrational math with a Fraction |
| `_mpf_val(vm, key)` | vm dict, versioned key string | `mpf` | Value type is `approximate` (decimal string) |
| `_get(vm, key)` | vm dict, versioned key string | raw value (str, int, Fraction) | Reading a derivation output or unknown type |
| `_approx(mpf_value)` | `mpf` | 15-digit decimal string | Storing an mpf result as an output |

### B.3 Type Matching Table

| Value Type in JSON | Stored As | Reader | Convert To mpf |
|---|---|---|---|
| `exact_fraction` | `{"_type": "Fraction", ...}` | `_frac(vm, key)` | `_f2m(_frac(vm, key))` |
| `exact_integer` | `42` | `_frac(vm, key)` or `_get(vm, key)` | `mpf(str(_get(vm, key)))` |
| `approximate` | `"137.035999177"` | `_mpf_val(vm, key)` | Already mpf |
| Previous step output (string) | `"80359.4..."` | `str(_get(vm, key))` | `mpf(str(_get(vm, key)))` |
| Previous step output (Fraction) | `Fraction(22, 13)` | `_frac(vm, key)` | `_f2m(_frac(vm, key))` |

### B.4 Common Patterns

**Reading a measured constant and computing with it:**
```python
M_Z = _f2m(_frac(vm, "mass_z_boson_v0"))
```

**Reading an approximate numerical value:**
```python
A4 = _mpf_val(vm, "qed_a4_laporta_v0")
```

**Reading an output from a previous derivation in the chain:**
```python
M_W_str = str(_get(vm, "result_mw_derived_v0"))
M_W = mpf(M_W_str)
```

**Reading a Q335 transcendental and using it:**
```python
pi_f = _frac(vm, "geom_pi_v0")       # Fraction
pi_m = _f2m(pi_f)                     # mpf at current mp.dps
pi2_m = pi_m * pi_m                   # exact to mp.dps digits
```

**Computing a miss percentage:**
```python
miss = abs(derived - measured) / measured * mpf("100")
```


## APPENDIX C: MATCH MODE REFERENCE

### C.1 exact

```json
{
    "label": "Gap ratio = 38/27",
    "output_key": "gap_cd_ratio_derived_v0",
    "match_mode": "exact",
    "expected": {"_type": "Fraction", "num": "38", "den": "27"},
    "reference_source": "group_theory"
}
```

PASS if `got == expected` as Fraction. No tolerance. No rounding.

Report format:
```
  [PASS] Gap ratio = 38/27
    expected: 38/27
    got:      38/27
    status:   PASS (exact Fraction match)
```

### C.2 digits

```json
{
    "label": "A2 from Q335 analytical",
    "output_key": "result_qed_a2_v0",
    "match_mode": "digits",
    "expected": "-0.328478965579",
    "digits": 12,
    "reference_source": "Petermann_1957"
}
```

PASS if first N significant digits of rendered value match expected string.

Report format:
```
  [PASS] A2 from Q335 analytical
    expected: -0.328478965579
    got:      -0.328478965579194
    agree:    12 of 15 digits
    miss:     0.059 ppb
```

### C.3 range

```json
{
    "label": "M_GUT in [10^15, 10^16] GeV",
    "output_key": "result_m_gut_gev_v0",
    "match_mode": "range",
    "lo": "1e15",
    "hi": "1e16",
    "reference_source": "proton_decay_bounds"
}
```

PASS if `lo <= got <= hi`.

Report format:
```
  [PASS] M_GUT in [10^15, 10^16] GeV
    got:      3.47e+15
    range:    [1e+15, 1e+16]
```

### C.4 miss_pct

```json
{
    "label": "DM/baryon vs Planck",
    "output_key": "cosmo_dm_to_baryon_ratio_predicted_derived_v0",
    "match_mode": "miss_pct",
    "expected": "5.3204",
    "reference_source": "Planck_2018"
}
```

Always INFO. Never PASS or FAIL. Reports the miss in appropriate units (ppb, ppm, or %).

Report format:
```
  [INFO] DM/baryon vs Planck
    predicted:  5.31654141377
    measured:   5.3204
    agree:      2 of 5 digits
    diverge:    position 3: '1' vs '2'
    miss:       725.2 ppm
    status:     INFO
```

### C.5 bool

```json
{
    "label": "Frame dragging negligible",
    "output_key": "result_frame_dragging_negligible_v0",
    "match_mode": "bool",
    "expected": true,
    "reference_source": "physics"
}
```

PASS if `got == expected`.

Report format:
```
  [PASS] Frame dragging negligible
    got:      True
    status:   PASS (bool match)
```


## APPENDIX D: EXPERIMENT MODES

| Mode | Purpose | Behavior |
|---|---|---|
| `standard` | Normal experiment run | Execute all derivations, evaluate all comparisons |
| `whatif` | BSM candidate scan | Same as standard, but values file contains candidate-specific quantum numbers |
| `verification` | Self-consistency check | All comparisons should PASS at high precision |
| `consistency` | Cross-check between methods | Compare outputs from different derivation paths |


## APPENDIX E: OUTPUT KEY NAMING CONVENTIONS

| Pattern | Meaning | Example |
|---|---|---|
| `result_{quantity}_derived_v0` | The main derived output | `result_mw_derived_v0` |
| `result_{quantity}_measured_v0` | The measured reference (echoed for diagnostics) | `result_mw_measured_v0` |
| `result_{quantity}_miss_pct_v0` | Percentage miss between derived and measured | `result_mw_miss_pct_v0` |
| `result_{quantity}_miss_ppb_v0` | Miss in parts per billion | `result_diff_vs_codata_ppb_v0` |
| `result_{quantity}_used_v0` | Input value echoed for traceability | `result_sin2_tw_used_v0` |
| `result_{quantity}_digits_v0` | Digits of agreement computed internally | `result_rydberg_digits_v0` |
| `result_{check}_v0` | Boolean or verification output | `result_frame_dragging_negligible_v0` |
| `cosmo_{quantity}_predicted_derived_v0` | Cosmological prediction from derivation | `cosmo_dm_to_baryon_ratio_predicted_derived_v0` |


## APPENDIX F: DERIVATION FUNCTION TEMPLATE

```python
def my_new_derivation_v0(value_dicts):
    """One-line summary of what this derives.
    
    Formula: Q = f(input_1, input_2, ...)
    
    All inputs from pool. Zero hardcoded values.
    """
    vm = _value_map(value_dicts)

    old_dps = mp.dps
    mp.dps = 50  # or 200 for precision-critical

    # Read inputs from pool
    input_1 = _f2m(_frac(vm, "some_exact_value_v0"))
    input_2 = _mpf_val(vm, "some_approximate_value_v0")
    
    # Optional: read output from earlier derivation in chain
    # chained_input = mpf(str(_get(vm, "result_earlier_step_v0")))

    # Computation
    result = input_1 * input_2  # your formula here

    # Comparison to measured reference
    measured = _f2m(_frac(vm, "some_measured_reference_v0"))
    miss = abs(result - measured) / measured * mpf("100")

    mp.dps = old_dps

    return {
        "key": "my_new_derivation_v0",
        "outputs": {
            "result_my_quantity_derived_v0": _approx(result),
            "result_my_quantity_measured_v0": _approx(measured),
            "result_my_quantity_miss_pct_v0": _approx(miss),
            "result_input_1_used_v0": _approx(input_1),
        },
        "notes": "Derived = %s, measured = %s, miss = %.4f%%" % (
            _approx(result), _approx(measured), float(miss)),
    }
```


## APPENDIX G: EXPERIMENT JSON TEMPLATE

```json
{
    "key": "experiment_my_experiment_v0",
    "canonical": "experiment_my_experiment",
    "version": 0,
    "node_type": "experiment",
    "description": "What this experiment tests, in one sentence.",
    "purpose": "program_some_program_v0",
    "experiment_mode": "standard",

    "dependencies": {
        "values": {
            "some_exact_value": 0,
            "some_approximate_value": 0,
            "some_measured_reference": 0
        },
        "derivations": {
            "my_new_derivation": 0
        },
        "connections": {}
    },

    "execution_plan": [
        "my_new_derivation_v0"
    ],

    "connections": [],

    "expected_outputs": [
        "result_my_quantity_derived_v0"
    ],

    "comparisons": [
        {
            "label": "Derived quantity vs measured",
            "output_key": "result_my_quantity_derived_v0",
            "match_mode": "miss_pct",
            "expected": "123.456",
            "reference_source": "PDG_2024"
        }
    ],

    "diagrams": []
}
```


## APPENDIX H: VALUE NODE JSON TEMPLATE

```json
{
  "nodes": [
    {
      "key": "topic_term_v0",
      "canonical": "topic_term",
      "version": 0,
      "node_type": "value",
      "topic": "topic",
      "term": "term",
      "level": 2,
      "value": "123.456",
      "value_type": "approximate",
      "unit": "MeV",
      "digits": 6,
      "uncertainty": "0.789",
      "source": "Author et al. Year. Journal. Measurement method.",
      "tags": ["domain", "subdomain", "measured"],
      "notes": "Any context about this value."
    }
  ]
}
```


## APPENDIX I: FRACTION ENCODING IN JSON

### I.1 Small fractions

```json
"value": {"_type": "Fraction", "num": "197", "den": "144"}
```

### I.2 Large fractions (Q335 basis)

```json
"value": {
    "_type": "Fraction",
    "num": "219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314",
    "den": "69805794224611060573508980531972755831587831503329841356763592928982254652702003843224245834961024"
}
```

Numerator and denominator as strings to avoid integer overflow in JSON parsers.

### I.3 Negative fractions

```json
"value": {"_type": "Fraction", "num": "-1", "den": "2"}
```

Sign goes on the numerator, never the denominator.

### I.4 Integer as fraction

```json
"value": {"_type": "Fraction", "num": "11", "den": "1"}
```

Or simply:

```json
"value": 11,
"value_type": "exact_integer"
```


## APPENDIX J: WHAT-IF EXPERIMENT PATTERN

For BSM candidate scans, each candidate gets its own values file and experiment.

### J.1 Candidate values file

```json
{
  "nodes": [
    {
      "key": "rep_whatif_vl_lepton_doublet_su3_dim_v0",
      "canonical": "rep_whatif_vl_lepton_doublet_su3_dim",
      "version": 0,
      "node_type": "value",
      "topic": "rep",
      "term": "whatif_vl_lepton_doublet_su3_dim",
      "level": 1,
      "value": 1,
      "value_type": "exact_integer",
      "unit": "dimensionless",
      "source": "SM quantum numbers for VL lepton doublet.",
      "tags": ["whatif", "BSM", "vl_lepton_doublet"]
    }
  ]
}
```

Note the candidate name `vl_lepton_doublet` in every key. This prevents the last-wins collision.

### J.2 Candidate experiment

Same structure as any experiment, but the execution plan calls a candidate-specific derivation wrapper that reads the candidate-prefixed keys.

### J.3 The anti-pattern (DO NOT DO THIS)

```json
"key": "rep_whatif_su3_dim_v0"
```

This key is the same for every candidate. When glob loads all files, the last one wins. All candidates compute the same result.


## APPENDIX K: DEVELOPMENT SESSION WORKFLOW

| Step | Action | Tool | Check |
|---|---|---|---|
| 1 | Identify derivation goal | Discussion | Can you state the formula? |
| 2 | Search pool for inputs | `data6.py search` | All inputs found? |
| 3 | Write missing value nodes | Text editor → JSON file | Valid JSON? Fields complete? |
| 4 | Write experiment JSON | Text editor → JSON file | Dependencies match plan? |
| 5 | Write derivation function | Text editor → Python file | Zero hardcoded physics? |
| 6 | Register in index | Text editor → Python file | Key matches function key? |
| 7 | Validate | `data6.py validate` | All nodes pass schema? |
| 8 | Run | `data6.py run experiment_v0` | Derivations OK? |
| 9 | Report | `data6.py report experiment_v0` | Results make sense? |
| 10 | Interpret | Discussion → report | What does this mean? |
| 11 | Paper if major | Markdown in chat | Does this deserve PHYS-NN? |
| 12 | Diagram if paper | Script in chat (D1-D17 rules) | 8 figures, 4+ types? |


## APPENDIX L: ERROR DIAGNOSIS GUIDE

| Symptom | Likely Cause | Fix |
|---|---|---|
| `KeyError: 'some_key_v0'` | Value not in pool | Add to values JSON file, or check spelling |
| `name 'X' is not defined` | Variable referenced outside its scope | Check: is it a local from another function? |
| `Derivation output is None` | Function doesn't return properly | Check return dict has `key`, `outputs`, `notes` |
| `All what-if candidates give same result` | Last-wins collision on shared keys | Use candidate-prefixed keys |
| `miss is 2752 ppb` (huge, unexpected) | Wrong convention or wrong coefficient | Add forward check: plug result back into formula |
| `SKIP on all comparisons` | Derivation errored, no outputs produced | Check derivation error message above the comparisons |
| `digits FAIL but miss_pct is small` | Digits threshold too strict for current precision | Lower the digits requirement or switch to miss_pct INFO |
| `mpf result is 0.0 or inf` | Division by zero or overflow at low mp.dps | Increase `mp.dps` or check denominator |
| `Fraction arithmetic is slow` | Q335 denominators are huge integers | Normal — Q335 fractions have 100-digit denominators. Use `_f2m()` to convert to mpf before heavy computation |


## APPENDIX M: THE DERIVATION CHAIN REGISTRY

Complete list of all derivation categories and their slot letters.

| Category | Letter | Count | Description |
|---|---|---|---|
| Coupling and prediction | A | 5 | GUT coupling extraction, α_s, sin²θ_W |
| Beta coefficients and gaps | B | 7 | SM betas, CD shifts, modified, gap, democracy, Y-dep |
| Koide | C | 2 | K ratio, m_τ prediction |
| Cosmology | D | 8 | DM/baryon, Ω_DM, Ω_b, amplification, virial, frame drag |
| Gravity and soliton | E | 8 | GM/(rc²), escape, binding, Hill, Kepler, GPS, MOND |
| Relativity | F | 3 | Muon, twins, ds² |
| Hubble | G | 6 | Ratio, tension, r(N), VP step, F1 tests |
| R2 domains | H | 8 | Wire, cap, RC cancel, disc, K_J×R_K, norms, vena |
| Dwarf solitons | I | 4 | Purity, cosmic ratio, FJ, TF |
| QED alpha extraction | J | 3 | Coefficient assembly, Newton inversion, CODATA derivation |
| Bridge derivations | K | 5 | M_W, Γ_Z, G_F, Ω_b, Ω_DE |
| What-if scan | W | 6 | Generic + 4 candidate + direct-db |
| Group theory | X | 1 | Casimirs verification |
| Scale conversion | Y | 2 | Energy ↔ distance |
| **Total** | | **68** | |


## APPENDIX N: COMPARISON RESULT STATUS MEANINGS

| Status | When Used | Implication |
|---|---|---|
| PASS | Exact match, digits match, in range, bool match | The derivation meets its specification |
| FAIL | Digits don't match, out of range, exact mismatch | Something is wrong — investigate |
| INFO | miss_pct mode (always INFO) | Reports the miss without judging pass/fail. Used for predictions where precision is uncertain |
| SKIP | Output key not found in pool | A derivation errored or the key was misspelled |

An experiment with 0 FAIL is status `complete`. Any FAIL makes it `partial`. SKIP means something upstream broke. INFO is neutral — it documents the result without gating.


## APPENDIX O: FILE INVENTORY CHECKLIST

For each new experiment, you should create or modify:

| # | File | Action | Location |
|---|---|---|---|
| 1 | `values_{section}_v0.json` | CREATE if new values needed | `data/` |
| 2 | `experiment_{name}_v0.json` | CREATE | `data/` |
| 3 | `_data_6_derivations_more_v0.py` | ADD derivation functions | `code/` |
| 4 | `_data_6_derivations_more_v0.py` | ADD to DERIVATION_MORE_INDEX_V0 | `code/` |
| 5 | `result_experiment_{name}_v0_runNNN.json` | AUTO-GENERATED by runner | `data/` |

Never modify existing value files to change values. Create `_v1` nodes if corrections are needed. Never delete result files — they are permanent records.

