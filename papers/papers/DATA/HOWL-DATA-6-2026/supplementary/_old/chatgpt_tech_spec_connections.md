Yes. The right model is:

- values = atomic facts
- derivations = executable transformations
- connections = executable relationship bundles / named views

So a connection function should not “derive physics” so much as:
- pull named values
- organize them into a stable structure
- return the connection set in machine-readable form

That gives you versionable “understanding of how things connect.”

Recommended pattern

- same callable shape as derivations:
  - `fn(value_dicts)`
- same version naming:
  - `topic_name_v0`
- same module registry:
  - `FUNCTION_INDEX_V0 = {}`
- plus optional metadata registry later:
  - `CONNECTION_INDEX_V0 = {}`

What a connection function returns

I would make it return:

- `key`
- `named_values`
- `edges`
- `notes`

Where:
- `named_values` = the actual resolved values by local name
- `edges` = explicit relationships between them
- `notes` = human context

So unlike derivations, connections are “structured bundles.”

Good first-pass code

```python
#!/usr/bin/env python3
"""
DATA-5 FIRST-PASS V0 CONNECTION REGISTRY
Filename: data_5_v0_master_connection_registry.py

Contract:
- Every connection function has the same signature:
    fn(value_dicts)
- value_dicts is a list of value-entry dicts from VALUE_INDEX_V0.values()
- Each function returns a plain dict with:
    - key
    - named_values
    - edges
    - notes
"""

from fractions import Fraction

from mpmath import mp


mp.dps = 100

FUNCTION_INDEX_V0 = {}


def _value_map(value_dicts):
    out = {}
    for entry in value_dicts:
        key = entry["key"]
        if key in out:
            raise ValueError("Duplicate value entry for key: %s" % key)
        out[key] = entry
    return out


def _need_entry(values_by_key, key):
    if key not in values_by_key:
        raise KeyError("Missing required value key: %s" % key)
    return values_by_key[key]


def _need_value(values_by_key, key):
    return _need_entry(values_by_key, key)["value"]


def _as_text(x):
    if isinstance(x, Fraction):
        return "%s/%s" % (x.numerator, x.denominator)
    if x is None:
        return None
    return str(x)


def _named_value(values_by_key, key, var_name):
    entry = _need_entry(values_by_key, key)
    return {
        "var_name": var_name,
        "source_key": key,
        "value": entry["value"],
        "value_text": _as_text(entry["value"]),
        "unit": entry.get("unit", ""),
        "source": entry.get("source", ""),
        "notes": entry.get("notes", ""),
        "ref": entry.get("ref", ""),
    }


def _connection_result(key, named_values, edges, notes=""):
    return {
        "key": key,
        "named_values": named_values,
        "edges": edges,
        "notes": notes,
    }


def connection_coupling_convergence_v0(value_dicts):
    """
    Input bindings from VALUE_INDEX_V0:
    - coupling_alpha_1_inverse_gut_normalized_mz_v0 -> inv_a1
    - coupling_alpha_2_inverse_mz_v0 -> inv_a2
    - coupling_alpha_3_inverse_mz_v0 -> inv_a3
    - beta_modified_u1_total_v0 -> b1_mod
    - beta_modified_su2_total_v0 -> b2_mod
    - beta_modified_su3_total_v0 -> b3_mod
    - coupling_measured_gap_ratio_v0 -> gap_measured
    - gap_sm_cabibbo_doublet_ratio_v0 -> gap_cd
    """
    v = _value_map(value_dicts)

    named_values = {
        "inv_a1": _named_value(
            v, "coupling_alpha_1_inverse_gut_normalized_mz_v0", "inv_a1"
        ),
        "inv_a2": _named_value(v, "coupling_alpha_2_inverse_mz_v0", "inv_a2"),
        "inv_a3": _named_value(v, "coupling_alpha_3_inverse_mz_v0", "inv_a3"),
        "b1_mod": _named_value(v, "beta_modified_u1_total_v0", "b1_mod"),
        "b2_mod": _named_value(v, "beta_modified_su2_total_v0", "b2_mod"),
        "b3_mod": _named_value(v, "beta_modified_su3_total_v0", "b3_mod"),
        "gap_measured": _named_value(
            v, "coupling_measured_gap_ratio_v0", "gap_measured"
        ),
        "gap_cd": _named_value(v, "gap_sm_cabibbo_doublet_ratio_v0", "gap_cd"),
    }

    edges = [
        {
            "from": "inv_a1",
            "to": "gap_measured",
            "relation": "participates_in_gap_ratio",
        },
        {
            "from": "inv_a2",
            "to": "gap_measured",
            "relation": "participates_in_gap_ratio",
        },
        {
            "from": "inv_a3",
            "to": "gap_measured",
            "relation": "participates_in_gap_ratio",
        },
        {"from": "b1_mod", "to": "gap_cd", "relation": "contributes_to_model_gap"},
        {"from": "b2_mod", "to": "gap_cd", "relation": "contributes_to_model_gap"},
        {"from": "b3_mod", "to": "gap_cd", "relation": "contributes_to_model_gap"},
        {
            "from": "gap_cd",
            "to": "gap_measured",
            "relation": "compared_against",
        },
    ]

    return _connection_result(
        "connection_coupling_convergence_v0",
        named_values,
        edges,
        notes="Connection bundle for C4 coupling convergence table.",
    )


def connection_gap_correction_chain_v0(value_dicts):
    """
    Input bindings from VALUE_INDEX_V0:
    - gap_pure_gauge_ratio_v0 -> gap_pure
    - gap_sm_ratio_v0 -> gap_sm
    - gap_sm_cabibbo_doublet_ratio_v0 -> gap_cd
    - coupling_measured_gap_ratio_v0 -> gap_measured
    """
    v = _value_map(value_dicts)

    named_values = {
        "gap_pure": _named_value(v, "gap_pure_gauge_ratio_v0", "gap_pure"),
        "gap_sm": _named_value(v, "gap_sm_ratio_v0", "gap_sm"),
        "gap_cd": _named_value(v, "gap_sm_cabibbo_doublet_ratio_v0", "gap_cd"),
        "gap_measured": _named_value(
            v, "coupling_measured_gap_ratio_v0", "gap_measured"
        ),
    }

    edges = [
        {"from": "gap_pure", "to": "gap_sm", "relation": "higgs_correction"},
        {"from": "gap_sm", "to": "gap_cd", "relation": "cabibbo_doublet_correction"},
        {
            "from": "gap_cd",
            "to": "gap_measured",
            "relation": "threshold_two_loop_residual",
        },
    ]

    return _connection_result(
        "connection_gap_correction_chain_v0",
        named_values,
        edges,
        notes="Connection bundle for C5 correction chain.",
    )


def connection_integer_network_v0(value_dicts):
    """
    Input bindings from VALUE_INDEX_V0:
    - integer_yang_mills_eleven_v0 -> ym_11
    - integer_b2_modified_numerator_abs_v0 -> b2_abs_13
    - integer_four_times_yang_mills_v0 -> four_ym
    - cosmo_dm_to_baryon_ratio_prefactor_v0 -> dm_prefactor
    - cosmo_omega_dm_r2_prefactor_v0 -> omega_prefactor
    - gap_sm_cabibbo_doublet_ratio_v0 -> gap_cd
    """
    v = _value_map(value_dicts)

    named_values = {
        "ym_11": _named_value(v, "integer_yang_mills_eleven_v0", "ym_11"),
        "b2_abs_13": _named_value(
            v, "integer_b2_modified_numerator_abs_v0", "b2_abs_13"
        ),
        "four_ym": _named_value(v, "integer_four_times_yang_mills_v0", "four_ym"),
        "dm_prefactor": _named_value(
            v, "cosmo_dm_to_baryon_ratio_prefactor_v0", "dm_prefactor"
        ),
        "omega_prefactor": _named_value(
            v, "cosmo_omega_dm_r2_prefactor_v0", "omega_prefactor"
        ),
        "gap_cd": _named_value(v, "gap_sm_cabibbo_doublet_ratio_v0", "gap_cd"),
    }

    edges = [
        {"from": "ym_11", "to": "dm_prefactor", "relation": "numerator_source"},
        {"from": "b2_abs_13", "to": "dm_prefactor", "relation": "denominator_source"},
        {"from": "four_ym", "to": "omega_prefactor", "relation": "numerator_source"},
        {
            "from": "b2_abs_13",
            "to": "omega_prefactor",
            "relation": "squared_denominator_source",
        },
        {"from": "b2_abs_13", "to": "gap_cd", "relation": "embedded_in_b2_mod"},
    ]

    return _connection_result(
        "connection_integer_network_v0",
        named_values,
        edges,
        notes="Connection bundle for C6 integer traceability.",
    )


def connection_three_programs_shared_set_v0(value_dicts):
    """
    Input bindings from VALUE_INDEX_V0:
    - integer_yang_mills_eleven_v0 -> ym_11
    - integer_b2_modified_numerator_abs_v0 -> b2_abs_13
    - geom_r2_v0 -> r2
    - integer_b2_sm_numerator_abs_v0 -> b2_sm_19
    - integer_cabibbo_doublet_gap_numerator_v0 -> gap_num_38
    - integer_cabibbo_doublet_gap_denominator_v0 -> gap_den_27
    """
    v = _value_map(value_dicts)

    named_values = {
        "ym_11": _named_value(v, "integer_yang_mills_eleven_v0", "ym_11"),
        "b2_abs_13": _named_value(
            v, "integer_b2_modified_numerator_abs_v0", "b2_abs_13"
        ),
        "r2": _named_value(v, "geom_r2_v0", "r2"),
        "b2_sm_19": _named_value(v, "integer_b2_sm_numerator_abs_v0", "b2_sm_19"),
        "gap_num_38": _named_value(
            v, "integer_cabibbo_doublet_gap_numerator_v0", "gap_num_38"
        ),
        "gap_den_27": _named_value(
            v, "integer_cabibbo_doublet_gap_denominator_v0", "gap_den_27"
        ),
    }

    edges = [
        {"from": "ym_11", "to": "b2_abs_13", "relation": "beta_unification_pair"},
        {"from": "ym_11", "to": "r2", "relation": "cross_program_association"},
        {"from": "b2_abs_13", "to": "r2", "relation": "cross_program_association"},
        {"from": "b2_sm_19", "to": "gap_num_38", "relation": "doubles_to"},
        {"from": "gap_num_38", "to": "gap_den_27", "relation": "forms_gap_ratio"},
    ]

    return _connection_result(
        "connection_three_programs_shared_set_v0",
        named_values,
        edges,
        notes="Connection bundle for C14 shared integer set.",
    )


def connection_object_adjacency_v0(value_dicts):
    """
    Input bindings from VALUE_INDEX_V0:
    - coupling_alpha_em_inverse_v0 -> alpha_inv
    - coupling_sin2_theta_w_v0 -> sin2_tW
    - coupling_alpha_s_mz_v0 -> alpha_s
    - beta_modified_su2_total_v0 -> b2_mod
    - integer_yang_mills_eleven_v0 -> ym_11
    - geom_r2_v0 -> r2
    - koide_charged_leptons_k_v0 -> koide_k
    """
    v = _value_map(value_dicts)

    named_values = {
        "alpha_inv": _named_value(v, "coupling_alpha_em_inverse_v0", "alpha_inv"),
        "sin2_tW": _named_value(v, "coupling_sin2_theta_w_v0", "sin2_tW"),
        "alpha_s": _named_value(v, "coupling_alpha_s_mz_v0", "alpha_s"),
        "b2_mod": _named_value(v, "beta_modified_su2_total_v0", "b2_mod"),
        "ym_11": _named_value(v, "integer_yang_mills_eleven_v0", "ym_11"),
        "r2": _named_value(v, "geom_r2_v0", "r2"),
        "koide_k": _named_value(v, "koide_charged_leptons_k_v0", "koide_k"),
    }

    edges = [
        {"from": "alpha_inv", "to": "sin2_tW", "relation": "joins_in_coupling_extraction"},
        {"from": "alpha_s", "to": "alpha_inv", "relation": "joins_in_measured_gap"},
        {"from": "b2_mod", "to": "ym_11", "relation": "integer_traceability_link"},
        {"from": "r2", "to": "ym_11", "relation": "cross_program_bridge"},
        {"from": "koide_k", "to": "alpha_inv", "relation": "shared_level2_measurement_class"},
    ]

    return _connection_result(
        "connection_object_adjacency_v0",
        named_values,
        edges,
        notes="First-pass adjacency bundle inspired by C20.",
    )


FUNCTION_INDEX_V0 = {
    "connection_coupling_convergence_v0": connection_coupling_convergence_v0,
    "connection_gap_correction_chain_v0": connection_gap_correction_chain_v0,
    "connection_integer_network_v0": connection_integer_network_v0,
    "connection_three_programs_shared_set_v0": (
        connection_three_programs_shared_set_v0
    ),
    "connection_object_adjacency_v0": connection_object_adjacency_v0,
}
```

Why this works

This gives you versioned connection bundles exactly like derivations:

- `connection_gap_correction_chain_v0`
- later:
  - `connection_gap_correction_chain_v1`

Then experiments can pin:

```json
"dependencies": {
  "connections": {
    "connection_gap_correction_chain": 0
  }
}
```

and the resolver can map that to:
- `connection_gap_correction_chain_v0`

Best rule

Treat connections as:
- executable structured views over named values
- not primary stored facts
- not derivations
- but fully versioned and swappable

I would also add, later:

- `CONNECTION_INDEX_V0`
  - `key`
  - `version`
  - `inputs`
  - `description`
  - `connection_type`
  - `outputs`

