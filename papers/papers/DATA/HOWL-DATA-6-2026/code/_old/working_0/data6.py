#!/usr/bin/env python3
"""
DATA-6 CLI
===========
Single entry point for all DATA-6 operations.

Usage:
    python data6.py run <experiment>
    python data6.py diagram <experiment>
    python data6.py test
    python data6.py validate
    python data6.py index
    python data6.py compile
    python data6.py list values|derivations|connections|experiments|results
    python data6.py search <query>
    python data6.py export
    python data6.py info <key>
"""

import sys
import os
import json
import glob

DIR = os.path.dirname(os.path.abspath(__file__))


def get_all_json_files():
    """Return sorted list of all JSON files in the working directory."""
    return sorted(glob.glob(os.path.join(DIR, "*.json")))


def _deserialize(obj):
    """Recursively convert Fraction/mpf markers."""
    if isinstance(obj, dict):
        if obj.get("_type") == "Fraction":
            return obj  # keep as dict for display
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
    """Load all value nodes from values_*.json files."""
    nodes = []
    for path in sorted(glob.glob(os.path.join(DIR, "values_*.json"))):
        data = load_json(path)
        for node in data.get("nodes", []):
            nodes.append(node)
    return nodes


# ================================================================
# COMMAND: run
# ================================================================

def cmd_run(args):
    """Run an experiment."""
    if not args:
        print("Usage: data6.py run <experiment_name>")
        return 1

    # Import and delegate to data_6_run.py
    sys.path.insert(0, DIR)
    from data_6_run import run_experiment
    return run_experiment(args[0], DIR)


# ================================================================
# COMMAND: diagram
# ================================================================

def cmd_diagram(args):
    """Generate diagrams for an experiment."""
    if not args:
        print("Usage: data6.py diagram <experiment_name>")
        return 1

    sys.path.insert(0, DIR)
    from data_6_diagrams import generate_diagrams
    return generate_diagrams(args[0], DIR)


# ================================================================
# COMMAND: test
# ================================================================

def cmd_test(args):
    """Run the super test."""
    script = os.path.join(DIR, "_data_6_super_test_v0.py")
    if not os.path.exists(script):
        print("ERROR: %s not found" % script)
        return 1
    return os.system("%s %s" % (sys.executable, script))


# ================================================================
# COMMAND: validate
# ================================================================

def cmd_validate(args):
    """Validate all JSON files against node schema."""
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

        # Determine node list
        nodes = []
        if isinstance(data, dict) and "nodes" in data:
            nodes = data["nodes"]
        elif isinstance(data, dict) and "node_type" in data:
            nodes = [data]
        else:
            continue  # result files, etc

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
    print("  Total nodes checked: %d" % total_nodes)
    print("  Total warnings:      %d" % total_warnings)
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
    """Build manifest index of all JSON files."""
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
                "filename": fname,
                "type": "invalid",
                "nodes": 0,
                "size_bytes": fsize,
            })
            continue

        # Classify file
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
            nodes = []

        entry = {
            "filename": fname,
            "type": ftype,
            "nodes": len(nodes),
            "size_bytes": fsize,
        }
        manifest["files"].append(entry)
        manifest["total_nodes"] += len(nodes)

        print("  %-45s %-12s %4d nodes  %7d bytes" % (
            fname, ftype, len(nodes), fsize))

    print()
    print("  Total files: %d" % len(manifest["files"]))
    print("  Total nodes: %d" % manifest["total_nodes"])

    manifest_path = os.path.join(DIR, "data_6_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print()
    print("  Manifest written: data_6_manifest.json")
    print()
    print("=" * 70)
    return 0


# ================================================================
# COMMAND: compile
# ================================================================

def cmd_compile(args):
    """Produce a single compiled JSON with everything."""
    print("=" * 70)
    print("DATA-6 COMPILE")
    print("=" * 70)
    print()

    compiled = {
        "version": "0.2",
        "values": {},
        "connections": [],
        "programs": [],
        "experiments": [],
        "results": [],
    }

    # Values — organized by section
    nodes = load_all_value_nodes()
    for node in nodes:
        section = node.get("section", "other")
        if section not in compiled["values"]:
            compiled["values"][section] = []
        compiled["values"][section].append(node)

    # Connections
    for path in sorted(glob.glob(os.path.join(DIR, "connections_*.json"))):
        data = load_json(path)
        for node in data.get("nodes", []):
            compiled["connections"].append(node)

    # Programs
    prog_path = os.path.join(DIR, "programs_v0.json")
    if os.path.exists(prog_path):
        data = load_json(prog_path)
        for node in data.get("nodes", []):
            compiled["programs"].append(node)

    # Experiments
    for path in sorted(glob.glob(os.path.join(DIR, "experiment_*.json"))):
        data = load_json(path)
        compiled["experiments"].append(data)

    # Results
    for path in sorted(glob.glob(os.path.join(DIR, "result_*.json"))):
        data = load_json(path)
        compiled["results"].append(data)

    # Derivation registry summary
    try:
        sys.path.insert(0, DIR)
        from _data_6_derivations_v0 import (
            DERIVATION_INDEX_V0, CONNECTION_INDEX_V0)
        compiled["derivation_keys"] = sorted(DERIVATION_INDEX_V0.keys())
        compiled["connection_function_keys"] = sorted(
            CONNECTION_INDEX_V0.keys())
    except ImportError:
        compiled["derivation_keys"] = []
        compiled["connection_function_keys"] = []

    # Summary counts
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

    out_path = os.path.join(DIR, "data_6_compiled.json")

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
    print("  Compiled: data_6_compiled.json")
    print()
    print("=" * 70)
    return 0


# ================================================================
# COMMAND: list
# ================================================================

def cmd_list(args):
    """List nodes by type."""
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
        sys.path.insert(0, DIR)
        try:
            from _data_6_derivations_v0 import DERIVATION_INDEX_V0
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
        sys.path.insert(0, DIR)
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
        files = sorted(glob.glob(os.path.join(DIR, "experiment_*.json")))
        print("=" * 70)
        print("EXPERIMENTS: %d files" % len(files))
        print("=" * 70)
        for path in files:
            fname = os.path.basename(path)
            data = load_json(path)
            desc = data.get("description", "")[:50]
            n_deriv = len(data.get("execution_plan", []))
            n_comp = len(data.get("comparisons", []))
            print("  %-45s %2d derivations, %2d comparisons" % (
                fname, n_deriv, n_comp))
        return 0

    elif target == "results":
        files = sorted(glob.glob(os.path.join(DIR, "result_*.json")))
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
    """Search across all node keys, tags, notes, source."""
    if not args:
        print("Usage: data6.py search <query>")
        return 1

    query = " ".join(args).lower()

    print("=" * 70)
    print("SEARCH: '%s'" % query)
    print("=" * 70)
    print()

    matches = []

    # Search value nodes
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

    # Search connection nodes
    for path in sorted(glob.glob(os.path.join(DIR, "connections_*.json"))):
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

    # Search program nodes
    prog_path = os.path.join(DIR, "programs_v0.json")
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

    # Search derivation keys
    sys.path.insert(0, DIR)
    try:
        from _data_6_derivations_v0 import (
            DERIVATION_INDEX_V0, CONNECTION_INDEX_V0)
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
# COMMAND: export
# ================================================================

def cmd_export(args):
    """Re-run the JSON exporter."""
    script = os.path.join(DIR, "data_6_export_json.py")
    if not os.path.exists(script):
        print("ERROR: data_6_export_json.py not found")
        return 1
    return os.system("%s %s" % (sys.executable, script))


# ================================================================
# COMMAND: info
# ================================================================

def cmd_info(args):
    """Print full details for one node by key."""
    if not args:
        print("Usage: data6.py info <key>")
        return 1

    target = args[0]
    # Add _v0 if not present
    if not target.split("_")[-1].startswith("v"):
        target_v0 = target + "_v0"
    else:
        target_v0 = target

    # Search value nodes
    nodes = load_all_value_nodes()
    for node in nodes:
        if node.get("key") == target or node.get("key") == target_v0:
            print("=" * 70)
            print("NODE: %s" % node["key"])
            print("=" * 70)
            print()
            for k, v in sorted(node.items()):
                if isinstance(v, dict):
                    print("  %-20s %s" % (k, json.dumps(v)))
                elif isinstance(v, list):
                    print("  %-20s %s" % (k, json.dumps(v)))
                else:
                    print("  %-20s %s" % (k, v))
            print()
            print("=" * 70)
            return 0

    # Search connection nodes
    for path in sorted(glob.glob(os.path.join(DIR, "connections_*.json"))):
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

    # Search programs
    prog_path = os.path.join(DIR, "programs_v0.json")
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

    # Search experiment files
    for path in sorted(glob.glob(os.path.join(DIR, "experiment_*.json"))):
        data = load_json(path)
        if data.get("key") == target or data.get("key") == target_v0:
            print("=" * 70)
            print("EXPERIMENT: %s" % data["key"])
            print("=" * 70)
            print()
            print("  description:    %s" % data.get("description", ""))
            print("  mode:           %s" % data.get("experiment_mode", ""))
            print("  purpose:        %s" % data.get("purpose", ""))
            print("  derivations:    %d" % len(
                data.get("execution_plan", [])))
            print("  connections:    %d" % len(
                data.get("connections", [])))
            print("  comparisons:    %d" % len(
                data.get("comparisons", [])))
            print("  diagrams:       %d" % len(
                data.get("diagrams", [])))
            print("  expected out:   %d" % len(
                data.get("expected_outputs", [])))
            print()
            print("=" * 70)
            return 0

    print("Key not found: %s" % target)
    return 1


# ================================================================
# COMMAND DISPATCH
# ================================================================

COMMANDS = {
    "run": cmd_run,
    "diagram": cmd_diagram,
    "test": cmd_test,
    "validate": cmd_validate,
    "index": cmd_index,
    "compile": cmd_compile,
    "list": cmd_list,
    "search": cmd_search,
    "export": cmd_export,
    "info": cmd_info,
}


def main():
    if len(sys.argv) < 2:
        print("DATA-6 CLI")
        print()
        print("Usage: python data6.py <command> [args]")
        print()
        print("Commands:")
        print("  run <experiment>       Run experiment, write result JSON")
        print("  diagram <experiment>   Generate PNGs from diagram specs")
        print("  test                   Run super test (values + derivations)")
        print("  validate               Check all JSON against node schema")
        print("  index                  Rebuild manifest from all JSON files")
        print("  compile                Produce single compiled JSON")
        print("  list <type>            List nodes (values|derivations|connections|experiments|results)")
        print("  search <query>         Search across all nodes")
        print("  export                 Re-run JSON exporter")
        print("  info <key>             Print full details for one node")
        return 1

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    handler = COMMANDS.get(command)
    if handler is None:
        print("Unknown command: %s" % command)
        print("Available: %s" % ", ".join(sorted(COMMANDS.keys())))
        return 1

    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
    