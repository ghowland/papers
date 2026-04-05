#!/usr/bin/env python3
"""
DATA-6 CLI v0.3
================
Single entry point for all DATA-6 operations.

Usage:
    python data6.py run <experiment>
    python data6.py diagram <experiment>
    python data6.py validate
    python data6.py index
    python data6.py compile
    python data6.py list values|derivations|connections|experiments|results
    python data6.py search <query>
    python data6.py info <key>
"""

import sys
import os
import json
import glob

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
FIGURES = os.path.join(ROOT, "figures")

sys.path.insert(0, ROOT)
try:
    from _data_6_derivations_v0 import DERIVATION_INDEX_V0, CONNECTION_INDEX_V0
    from _data_6_derivations_more_v0 import (
        DERIVATION_MORE_INDEX_V0, CONNECTION_MORE_INDEX_V0)
    DERIVATION_INDEX_V0.update(DERIVATION_MORE_INDEX_V0)
    CONNECTION_INDEX_V0.update(CONNECTION_MORE_INDEX_V0)
except ImportError:
    pass


def ensure_dirs():
    os.makedirs(DATA, exist_ok=True)
    os.makedirs(FIGURES, exist_ok=True)


def get_all_json_files():
    return sorted(glob.glob(os.path.join(DATA, "*.json")))


def _deserialize(obj):
    if isinstance(obj, dict):
        if obj.get("_type") == "Fraction":
            return obj
        if obj.get("_type") == "mpf":
            return obj.get("value", obj)
        return {k: _deserialize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_deserialize(x) for x in obj]
    return obj


def load_json(path):
    with open(path) as f:
        return _deserialize(json.load(f))


def load_all_value_nodes():
    nodes = []
    for path in sorted(glob.glob(os.path.join(DATA, "values_*.json"))):
        data = load_json(path)
        for node in data.get("nodes", []):
            nodes.append(node)
    return nodes


# ================================================================
# COMMAND: run
# ================================================================

def cmd_run(args):
    if not args:
        print("Usage: data6.py run <experiment_name>")
        return 1
    sys.path.insert(0, ROOT)
    from data_6_run import run_experiment
    return run_experiment(args[0], DATA)


# ================================================================
# COMMAND: diagram
# ================================================================

def cmd_diagram(args):
    if not args:
        print("Usage: data6.py diagram <experiment_name>")
        return 1
    sys.path.insert(0, ROOT)
    from data_6_diagrams import generate_diagrams
    return generate_diagrams(args[0], DATA, FIGURES)


# ================================================================
# COMMAND: validate
# ================================================================

def cmd_validate(args):
    print("=" * 70)
    print("DATA-6 VALIDATE")
    print("=" * 70)
    print()

    required_value = ["key", "canonical", "version", "node_type",
                      "value", "value_type", "unit", "level", "source"]
    required_envelope = ["key", "canonical", "version", "node_type", "source"]

    files = get_all_json_files()
    total_nodes = 0
    total_warnings = 0

    for path in files:
        fname = os.path.basename(path)
        try:
            data = load_json(path)
        except Exception as e:
            print("  [ERROR] %-45s %s" % (fname, e))
            total_warnings += 1
            continue

        nodes = []
        if isinstance(data, dict) and "nodes" in data:
            nodes = data["nodes"]
        elif isinstance(data, dict) and "node_type" in data:
            nodes = [data]
        else:
            continue

        file_warnings = 0
        for node in nodes:
            total_nodes += 1
            node_type = node.get("node_type", "unknown")
            key = node.get("key", "???")

            if node_type == "value":
                required = required_value
            else:
                required = required_envelope

            for field in required:
                if field not in node:
                    print("  [WARN] %-45s missing '%s'" % (key, field))
                    file_warnings += 1
                    total_warnings += 1

        if file_warnings == 0:
            print("  [OK]   %-45s %3d nodes" % (fname, len(nodes)))

    print()
    print("  Total nodes: %d" % total_nodes)
    print("  Warnings:    %d" % total_warnings)
    print()

    if total_warnings == 0:
        print("  ALL NODES VALID")
    else:
        print("  %d WARNINGS" % total_warnings)

    print()
    print("=" * 70)
    return 0 if total_warnings == 0 else 1


# ================================================================
# COMMAND: index
# ================================================================

def cmd_index(args):
    print("=" * 70)
    print("DATA-6 INDEX")
    print("=" * 70)
    print()

    manifest = {"files": [], "total_nodes": 0}
    files = get_all_json_files()

    for path in files:
        fname = os.path.basename(path)
        fsize = os.path.getsize(path)

        try:
            data = load_json(path)
        except Exception:
            manifest["files"].append({
                "filename": fname, "type": "invalid",
                "nodes": 0, "size_bytes": fsize})
            continue

        nodes = []
        ftype = "unknown"

        if isinstance(data, dict) and "nodes" in data:
            nodes = data["nodes"]
            if fname.startswith("values_"):
                ftype = "values"
            elif fname.startswith("connections_"):
                ftype = "connections"
            elif fname.startswith("programs"):
                ftype = "programs"
            else:
                ftype = "nodes"
        elif isinstance(data, dict) and "node_type" in data:
            ftype = data["node_type"]
            nodes = [data]
        elif isinstance(data, dict) and "experiment_key" in data:
            ftype = "result"

        entry = {
            "filename": fname, "type": ftype,
            "nodes": len(nodes), "size_bytes": fsize}
        manifest["files"].append(entry)
        manifest["total_nodes"] += len(nodes)

        print("  %-45s %-12s %4d nodes  %7d bytes" % (
            fname, ftype, len(nodes), fsize))

    print()
    print("  Total files: %d" % len(manifest["files"]))
    print("  Total nodes: %d" % manifest["total_nodes"])

    manifest_path = os.path.join(DATA, "data_6_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print()
    print("  Manifest written: %s" % manifest_path)
    print()
    print("=" * 70)
    return 0


# ================================================================
# COMMAND: compile
# ================================================================

def cmd_compile(args):
    print("=" * 70)
    print("DATA-6 COMPILE")
    print("=" * 70)
    print()

    compiled = {
        "version": "0.3",
        "values": {},
        "connections": [],
        "programs": [],
        "experiments": [],
        "results": [],
    }

    nodes = load_all_value_nodes()
    for node in nodes:
        section = node.get("section", "other")
        if section not in compiled["values"]:
            compiled["values"][section] = []
        compiled["values"][section].append(node)

    for path in sorted(glob.glob(os.path.join(DATA, "connections_*.json"))):
        data = load_json(path)
        for node in data.get("nodes", []):
            compiled["connections"].append(node)

    prog_path = os.path.join(DATA, "programs_v0.json")
    if os.path.exists(prog_path):
        data = load_json(prog_path)
        for node in data.get("nodes", []):
            compiled["programs"].append(node)

    for path in sorted(glob.glob(os.path.join(DATA, "experiment_*.json"))):
        data = load_json(path)
        compiled["experiments"].append(data)

    for path in sorted(glob.glob(os.path.join(DATA, "result_*.json"))):
        data = load_json(path)
        compiled["results"].append(data)

    sys.path.insert(0, ROOT)
    try:
        # from _data_6_derivations_v0 import (DERIVATION_INDEX_V0, CONNECTION_INDEX_V0)
        compiled["derivation_keys"] = sorted(DERIVATION_INDEX_V0.keys())
        compiled["connection_function_keys"] = sorted(
            CONNECTION_INDEX_V0.keys())
    except ImportError:
        compiled["derivation_keys"] = []
        compiled["connection_function_keys"] = []

    total_values = sum(len(v) for v in compiled["values"].values())
    compiled["summary"] = {
        "total_values": total_values,
        "value_sections": len(compiled["values"]),
        "connections": len(compiled["connections"]),
        "programs": len(compiled["programs"]),
        "experiments": len(compiled["experiments"]),
        "results": len(compiled["results"]),
        "derivation_functions": len(compiled["derivation_keys"]),
        "connection_functions": len(compiled["connection_function_keys"]),
    }

    out_path = os.path.join(DATA, "data_6_compiled.json")

    def _default(obj):
        if hasattr(obj, "numerator"):
            return {"_type": "Fraction",
                    "num": str(obj.numerator),
                    "den": str(obj.denominator)}
        return str(obj)

    with open(out_path, "w") as f:
        json.dump(compiled, f, indent=2, default=_default)

    print("  Values:       %d across %d sections" % (
        total_values, len(compiled["values"])))
    print("  Connections:  %d" % len(compiled["connections"]))
    print("  Programs:     %d" % len(compiled["programs"]))
    print("  Experiments:  %d" % len(compiled["experiments"]))
    print("  Results:      %d" % len(compiled["results"]))
    print("  Derivations:  %d" % len(compiled["derivation_keys"]))
    print("  Conn funcs:   %d" % len(compiled["connection_function_keys"]))
    print()
    print("  Compiled: %s" % out_path)
    print()
    print("=" * 70)
    return 0


# ================================================================
# COMMAND: list
# ================================================================

def cmd_list(args):
    if not args:
        print("Usage: data6.py list values|derivations|connections|experiments|results")
        return 1

    target = args[0].lower()

    if target == "values":
        nodes = load_all_value_nodes()
        print("=" * 70)
        print("VALUES: %d nodes" % len(nodes))
        print("=" * 70)
        for node in sorted(nodes, key=lambda n: n.get("key", "")):
            val = node.get("value", "")
            if isinstance(val, dict) and val.get("_type") == "Fraction":
                val_str = "%s/%s" % (val["num"], val["den"])
            elif isinstance(val, str) and len(val) > 30:
                val_str = val[:27] + "..."
            else:
                val_str = str(val)
            print("  %-55s %s" % (node["key"], val_str))
        return 0

    elif target == "derivations":
        sys.path.insert(0, ROOT)
        try:
            # from _data_6_derivations_v0 import DERIVATION_INDEX_V0
            keys = sorted(DERIVATION_INDEX_V0.keys())
            print("=" * 70)
            print("DERIVATIONS: %d functions" % len(keys))
            print("=" * 70)
            for k in keys:
                fn = DERIVATION_INDEX_V0[k]
                doc = (fn.__doc__ or "").strip().split("\n")[0]
                print("  %-55s %s" % (k, doc[:40]))
        except ImportError:
            print("ERROR: _data_6_derivations_v0.py not found")
            return 1
        return 0

    elif target == "connections":
        sys.path.insert(0, ROOT)
        try:
            from _data_6_derivations_v0 import CONNECTION_INDEX_V0
            keys = sorted(CONNECTION_INDEX_V0.keys())
            print("=" * 70)
            print("CONNECTIONS: %d functions" % len(keys))
            print("=" * 70)
            for k in keys:
                fn = CONNECTION_INDEX_V0[k]
                doc = (fn.__doc__ or "").strip().split("\n")[0]
                print("  %-55s %s" % (k, doc[:40]))
        except ImportError:
            print("ERROR: _data_6_derivations_v0.py not found")
            return 1
        return 0

    elif target == "experiments":
        files = sorted(glob.glob(os.path.join(DATA, "experiment_*.json")))
        print("=" * 70)
        print("EXPERIMENTS: %d files" % len(files))
        print("=" * 70)
        for path in files:
            fname = os.path.basename(path)
            data = load_json(path)
            n_deriv = len(data.get("execution_plan", []))
            n_comp = len(data.get("comparisons", []))
            print("  %-45s %2d derivations, %2d comparisons" % (
                fname, n_deriv, n_comp))
        return 0

    elif target == "results":
        files = sorted(glob.glob(os.path.join(DATA, "result_*.json")))
        print("=" * 70)
        print("RESULTS: %d files" % len(files))
        print("=" * 70)
        for path in files:
            fname = os.path.basename(path)
            data = load_json(path)
            status = data.get("status", "?")
            summary = data.get("summary", {})
            p = summary.get("comparisons_pass", 0)
            f = summary.get("comparisons_fail", 0)
            i = summary.get("comparisons_info", 0)
            print("  %-45s %s  P:%d F:%d I:%d" % (
                fname, status, p, f, i))
        return 0

    else:
        print("Unknown list target: %s" % target)
        print("Options: values, derivations, connections, experiments, results")
        return 1


# ================================================================
# COMMAND: search
# ================================================================

def cmd_search(args):
    if not args:
        print("Usage: data6.py search <query>")
        return 1

    query = " ".join(args).lower()

    print("=" * 70)
    print("SEARCH: '%s'" % query)
    print("=" * 70)
    print()

    matches = []

    nodes = load_all_value_nodes()
    for node in nodes:
        searchable = " ".join([
            node.get("key", ""),
            node.get("canonical", ""),
            node.get("section", ""),
            node.get("source", ""),
            node.get("notes", ""),
            " ".join(node.get("tags", [])),
        ]).lower()
        if query in searchable:
            matches.append(("value", node.get("key", "?"),
                           node.get("section", "")))

    for path in sorted(glob.glob(os.path.join(DATA, "connections_*.json"))):
        data = load_json(path)
        for node in data.get("nodes", []):
            searchable = " ".join([
                node.get("key", ""),
                node.get("description", ""),
                node.get("connection_type", ""),
                node.get("notes", ""),
            ]).lower()
            if query in searchable:
                matches.append(("connection", node.get("key", "?"),
                               node.get("connection_type", "")))

    prog_path = os.path.join(DATA, "programs_v0.json")
    if os.path.exists(prog_path):
        data = load_json(prog_path)
        for node in data.get("nodes", []):
            searchable = " ".join([
                node.get("key", ""),
                node.get("thesis", ""),
                node.get("status", ""),
            ]).lower()
            if query in searchable:
                matches.append(("program", node.get("key", "?"),
                               node.get("status", "")))

    sys.path.insert(0, ROOT)
    try:
        # from _data_6_derivations_v0 import (DERIVATION_INDEX_V0, CONNECTION_INDEX_V0)
        for k in DERIVATION_INDEX_V0:
            if query in k.lower():
                matches.append(("derivation", k, ""))
        for k in CONNECTION_INDEX_V0:
            if query in k.lower():
                matches.append(("conn_func", k, ""))
    except ImportError:
        pass

    if matches:
        for mtype, mkey, mextra in sorted(matches):
            print("  [%-12s] %-55s %s" % (mtype, mkey, mextra))
        print()
        print("  %d matches" % len(matches))
    else:
        print("  No matches found.")

    print()
    print("=" * 70)
    return 0


# ================================================================
# COMMAND: info
# ================================================================

def cmd_info(args):
    if not args:
        print("Usage: data6.py info <key>")
        return 1

    target = args[0]
    if not target.split("_")[-1].startswith("v"):
        target_v0 = target + "_v0"
    else:
        target_v0 = target

    nodes = load_all_value_nodes()
    for node in nodes:
        if node.get("key") == target or node.get("key") == target_v0:
            print("=" * 70)
            print("NODE: %s" % node["key"])
            print("=" * 70)
            print()
            for k, v in sorted(node.items()):
                if isinstance(v, (dict, list)):
                    print("  %-20s %s" % (k, json.dumps(v)))
                else:
                    print("  %-20s %s" % (k, v))
            print()
            print("=" * 70)
            return 0

    for path in sorted(glob.glob(os.path.join(DATA, "connections_*.json"))):
        data = load_json(path)
        for node in data.get("nodes", []):
            if node.get("key") == target or node.get("key") == target_v0:
                print("=" * 70)
                print("NODE: %s" % node["key"])
                print("=" * 70)
                print()
                for k, v in sorted(node.items()):
                    print("  %-20s %s" % (k, json.dumps(v)
                          if isinstance(v, (dict, list)) else v))
                print()
                print("=" * 70)
                return 0

    prog_path = os.path.join(DATA, "programs_v0.json")
    if os.path.exists(prog_path):
        data = load_json(prog_path)
        for node in data.get("nodes", []):
            if node.get("key") == target or node.get("key") == target_v0:
                print("=" * 70)
                print("NODE: %s" % node["key"])
                print("=" * 70)
                print()
                for k, v in sorted(node.items()):
                    print("  %-20s %s" % (k, json.dumps(v, indent=2)
                          if isinstance(v, (dict, list)) else v))
                print()
                print("=" * 70)
                return 0

    for path in sorted(glob.glob(os.path.join(DATA, "experiment_*.json"))):
        data = load_json(path)
        if data.get("key") == target or data.get("key") == target_v0:
            print("=" * 70)
            print("EXPERIMENT: %s" % data["key"])
            print("=" * 70)
            print()
            print("  description:    %s" % data.get("description", ""))
            print("  mode:           %s" % data.get("experiment_mode", ""))
            print("  purpose:        %s" % data.get("purpose", ""))
            print("  derivations:    %d" % len(data.get("execution_plan", [])))
            print("  connections:    %d" % len(data.get("connections", [])))
            print("  comparisons:    %d" % len(data.get("comparisons", [])))
            print("  diagrams:       %d" % len(data.get("diagrams", [])))
            print("  expected out:   %d" % len(data.get("expected_outputs", [])))
            print()
            print("=" * 70)
            return 0

    print("Key not found: %s" % target)
    return 1

# ================================================================
# COMMAND: report
# ================================================================

def cmd_report(args):
    if not args:
        print("Usage: data6.py report <experiment_name>")
        return 1

    name = args[0]

    # Find latest result file
    candidates = [
        "result_experiment_%s" % name,
        "result_%s" % name,
    ]
    if name.startswith("experiment_"):
        candidates.insert(0, "result_%s" % name)

    result_path = None
    for prefix in candidates:
        pattern = os.path.join(DATA, "%s_run*.json" % prefix)
        matches = sorted(glob.glob(pattern))
        if matches:
            result_path = matches[-1]
            break
        # Try without run number
        path = os.path.join(DATA, "%s.json" % prefix)
        if os.path.exists(path):
            result_path = path
            break

    if result_path is None:
        print("No result found for '%s'" % name)
        return 1

    result = load_json(result_path)

    # Find experiment file for execution plan context
    exp_path = None
    for prefix in ["experiment_", ""]:
        path = os.path.join(DATA, "%s%s.json" % (prefix, name))
        if os.path.exists(path):
            exp_path = path
            break

    experiment = None
    if exp_path:
        experiment = load_json(exp_path)

    exp_key = result.get("experiment_key", name)
    timestamp = result.get("timestamp", "?")
    status = result.get("status", "?")
    summary = result.get("summary", {})
    run_file = os.path.basename(result_path)

    print()
    print("=" * 70)
    print("DATA-6 REPORT: %s" % exp_key)
    print("=" * 70)
    print()
    print("  Result file:  %s" % run_file)
    print("  Timestamp:    %s" % timestamp)
    print("  Status:       %s" % status)
    if experiment:
        print("  Mode:         %s" % experiment.get("experiment_mode", "?"))
        print("  Purpose:      %s" % experiment.get("purpose", ""))
    print()

    # ---- DERIVATION OUTPUTS ----
    outputs = result.get("outputs", {})
    execution_log = result.get("execution_log", [])

    print("-" * 70)
    print("DERIVATION OUTPUTS: %d values" % len(outputs))
    print("-" * 70)
    print()

    # Group outputs by source derivation
    by_derivation = {}
    for key, val in outputs.items():
        # Find which derivation produced this key
        source = None
        for log_entry in execution_log:
            if log_entry.get("status") != "ok":
                continue
            deriv_key = log_entry.get("key", "")
            if source is None:
                source = deriv_key  # default to first
        # Without full provenance, just list all outputs
        by_derivation.setdefault("all", []).append((key, val))

    # If we have execution log, try to group by checking derivation order
    if execution_log:
        by_derivation = {}
        deriv_order = [e["key"] for e in execution_log
                       if e.get("status") == "ok"]

        # Build output->derivation map from experiment execution plan
        # by running derivations would be ideal, but we just have the
        # flat output dict. Group by prefix matching as best effort.
        for deriv_key in deriv_order:
            by_derivation[deriv_key] = []

        # Assign outputs to derivations by order they appear
        assigned = set()
        if experiment:
            # Use the derivation registry to check
            try:
                # from _data_6_derivations_v0 import DERIVATION_INDEX_V0
                pool_stub = load_all_value_nodes()
                for deriv_key in deriv_order:
                    fn = DERIVATION_INDEX_V0.get(deriv_key)
                    if fn is None:
                        continue
                    try:
                        r = fn(pool_stub)
                        for ok in r.get("outputs", {}).keys():
                            if ok in outputs and ok not in assigned:
                                by_derivation[deriv_key].append(
                                    (ok, outputs[ok]))
                                assigned.add(ok)
                            # Merge outputs for chaining
                            pool_stub.append({
                                "key": ok,
                                "value": r["outputs"][ok],
                                "node_type": "value",
                                "version": 0,
                                "canonical": ok.replace("_v0", ""),
                                "unit": "dimensionless",
                                "source": deriv_key,
                                "value_type": "approximate",
                            })
                    except Exception:
                        pass
            except ImportError:
                pass

        # Any unassigned outputs
        unassigned = [(k, v) for k, v in outputs.items()
                      if k not in assigned]
        if unassigned:
            by_derivation["(unassigned)"] = unassigned

    for deriv_key, output_list in by_derivation.items():
        if not output_list:
            continue
        print("  %s" % deriv_key)
        print("  %s" % ("-" * len(deriv_key)))
        for key, val in sorted(output_list):
            val_str = _format_value(val)
            print("    %-55s %s" % (key, val_str))
        print()

    # ---- COMPARISON RESULTS ----
    comp_results = result.get("comparison_results", [])

    if comp_results:
        print("-" * 70)
        print("COMPARISONS: %d checks" % len(comp_results))
        print("-" * 70)
        print()
        print("  %-40s %-10s %-10s %s" % (
            "Label", "Mode", "Status", "Detail"))
        print("  %-40s %-10s %-10s %s" % (
            "-" * 40, "-" * 10, "-" * 10, "-" * 30))

        for cr in comp_results:
            label = cr.get("label", "?")[:40]
            mode = cr.get("match_mode", "?")
            status = cr.get("status", "?")
            detail = cr.get("detail", "")

            print("  %-40s %-10s %-10s %s" % (label, mode, status, detail))

        print()

    # ---- SUMMARY ----
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("  Derivations OK:  %d" % summary.get("derivations_ok", 0))
    print("  Derivations err: %d" % summary.get("derivations_err", 0))
    print()
    print("  PASS: %d" % summary.get("comparisons_pass", 0))
    print("  FAIL: %d" % summary.get("comparisons_fail", 0))
    print("  INFO: %d" % summary.get("comparisons_info", 0))
    print("  SKIP: %d" % summary.get("comparisons_skip", 0))
    print()

    overall = result.get("status", "?")
    if overall == "complete":
        print("  EXPERIMENT: ALL COMPARISONS PASSED")
    else:
        print("  EXPERIMENT: %s" % overall.upper())

    print()
    print("=" * 70)
    return 0


def _format_value(val):
    """Format a value for report display."""
    if isinstance(val, dict) and val.get("_type") == "Fraction":
        num = val["num"]
        den = val["den"]
        if den == "1":
            return num
        return "%s/%s" % (num, den)
    if isinstance(val, bool):
        return str(val)
    if isinstance(val, str):
        if len(val) > 50:
            return val[:47] + "..."
        return val
    return str(val)


# ================================================================
# DISPATCH
# ================================================================

COMMANDS = {
    "run": cmd_run,
    "diagram": cmd_diagram,
    "validate": cmd_validate,
    "index": cmd_index,
    "compile": cmd_compile,
    "list": cmd_list,
    "search": cmd_search,
    "info": cmd_info,
    "report": cmd_report,
}


def main():
    if len(sys.argv) < 2:
        print("DATA-6 CLI v0.3")
        print()
        print("Usage: python data6.py <command> [args]")
        print()
        print("Commands:")
        print("  run <experiment>       Run experiment, write result JSON")
        print("  diagram <experiment>   Generate PNGs from diagram specs")
        print("  validate               Check all JSON against node schema")
        print("  index                  Rebuild manifest from all JSON files")
        print("  compile                Produce single compiled JSON")
        print("  list <type>            List nodes (values|derivations|connections|experiments|results)")
        print("  search <query>         Search across all nodes")
        print("  info <key>             Print full details for one node")
        print("  report <experiment>    Print human-readable result report")
        return 1

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    handler = COMMANDS.get(command)
    if handler is None:
        print("Unknown command: %s" % command)
        print("Available: %s" % ", ".join(sorted(COMMANDS.keys())))
        return 1

    ensure_dirs()
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
    