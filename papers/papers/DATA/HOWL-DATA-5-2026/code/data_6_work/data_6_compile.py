#!/usr/bin/env python3
"""
DATA-6 COMPILER
==================
Reads the entire data6/ directory tree and compiles all live-version
JSON files into a single master JSON file, organized by layer.

The master file is a complete snapshot — every entity, every connection,
every evidence file, every program, every index. An LLM can ingest
this single file and have the full knowledge base.

The loose files remain the source of truth. This compiler produces
a read-only view. Edit the loose files, re-run the compiler.

Run: python compile_data6.py
Requires: data6/ directory (from generate_data6.py)

Output: data6_compiled.json (single file, all layers)
"""

import sys
import os
import json

DATA_ROOT = "data6"
OUTPUT = "data6_compiled.json"


def load_json(path):
    """Load a JSON file, return dict or None on error."""
    try:
        with open(path) as f:
            return json.load(f)
    except Exception as e:
        print("  WARNING: failed to load %s: %s" % (path, e))
        return None


def collect_layer(subdir):
    """Walk a subdirectory, collect all JSON files into a dict keyed by
    relative path (without the data6/ prefix)."""
    layer = {}
    full_dir = os.path.join(DATA_ROOT, subdir)
    if not os.path.exists(full_dir):
        return layer

    for dirpath, dirnames, filenames in os.walk(full_dir):
        for fname in filenames:
            if not fname.endswith(".json"):
                continue
            fpath = os.path.join(dirpath, fname)
            rel = os.path.relpath(fpath, DATA_ROOT)
            data = load_json(fpath)
            if data is not None:
                layer[rel] = data

    return layer


def build_id_lookup(entities):
    """Build a flat dict: str(id) -> entity data, for cross-reference."""
    lookup = {}
    for rel_path, data in entities.items():
        if isinstance(data, dict) and "id" in data:
            lookup[str(data["id"])] = {
                "path": rel_path,
                "name": data.get("name", ""),
                "type": data.get("type", ""),
                "subtype": data.get("subtype", ""),
            }
    return lookup


def count_by_subtype(layer):
    """Count objects by subtype."""
    counts = {}
    for rel_path, data in layer.items():
        if isinstance(data, dict):
            st = data.get("subtype", data.get("type", "unknown"))
            counts[st] = counts.get(st, 0) + 1
    return counts


def compile():
    print("=" * 70)
    print("DATA-6 COMPILER")
    print("=" * 70)
    print()

    # Collect each layer
    print("  Collecting layers...")

    entities = collect_layer("entities")
    connections = collect_layer("connections")
    evidence = collect_layer("evidence")
    programs = collect_layer("programs")
    index = collect_layer("index")

    print("    entities:    %d files" % len(entities))
    print("    connections: %d files" % len(connections))
    print("    evidence:    %d files" % len(evidence))
    print("    programs:    %d files" % len(programs))
    print("    index:       %d files" % len(index))
    print()

    # Build the master structure
    master = {
        "_metadata": {
            "format": "DATA-6 compiled snapshot",
            "version": 1,
            "source": "data6/ directory tree",
            "generator": "compile_data6.py",
            "note": "Read-only view. Edit loose files, re-compile.",
            "counts": {
                "entities": len(entities),
                "connections": len(connections),
                "evidence": len(evidence),
                "programs": len(programs),
                "total_files": len(entities) + len(connections) + len(evidence) + len(programs),
            },
            "entity_subtypes": count_by_subtype(entities),
            "connection_subtypes": count_by_subtype(connections),
        },

        # Layer 1: Index files (the registry)
        "index": index,

        # Layer 2: Entities by category
        "entities": {
            "si_constants": {},
            "couplings": {},
            "masses": {},
            "q335": {},
            "geometric": {},
            "group_theory": {},
            "betas": {},
            "two_loop": {},
            "representations": {},
            "boundaries": {},
            "gap_ratios": {},
            "koide": {},
            "cosmological": {},
            "domains": {},
            "cancellations": {},
            "moduli": {},
            "engineering": {},
            "hubble": {},
            "astrophysical": {},
        },

        # Layer 3: Connections by type
        "connections": {
            "containment": {},
            "membership": {},
            "adjacency": {},
            "cancellation": {},
            "integer_source": {},
            "produces": {},
            "consumes": {},
            "equivalent": {},
        },

        # Layer 4: Evidence
        "evidence": {
            "scripts": {},
            "results": {},
            "papers": {},
        },

        # Layer 5: Programs
        "programs": {},
    }

    # Sort entities into categories
    for rel_path, data in entities.items():
        # Determine category from path
        parts = rel_path.replace("\\", "/").split("/")
        # parts[0] = "entities", parts[1] = category, rest = filename
        if len(parts) < 3:
            continue

        category = parts[1]
        filename = "/".join(parts[2:])

        if category in master["entities"]:
            master["entities"][category][filename] = data
        else:
            # Sub-categories like engineering/discs
            if category == "engineering" and len(parts) >= 4:
                sub = parts[2]
                fname = "/".join(parts[3:])
                key = "engineering"
                if key not in master["entities"]:
                    master["entities"][key] = {}
                if sub not in master["entities"][key]:
                    master["entities"][key][sub] = {}
                master["entities"][key][sub][fname] = data
            else:
                master["entities"].setdefault(category, {})[filename] = data

    # Sort connections into types
    for rel_path, data in connections.items():
        parts = rel_path.replace("\\", "/").split("/")
        if len(parts) < 3:
            continue
        conn_type = parts[1]
        filename = "/".join(parts[2:])
        if conn_type in master["connections"]:
            master["connections"][conn_type][filename] = data
        else:
            master["connections"].setdefault(conn_type, {})[filename] = data

    # Sort evidence
    for rel_path, data in evidence.items():
        parts = rel_path.replace("\\", "/").split("/")
        if len(parts) < 3:
            continue
        evid_type = parts[1]
        filename = "/".join(parts[2:])
        if evid_type in master["evidence"]:
            master["evidence"][evid_type][filename] = data
        else:
            master["evidence"].setdefault(evid_type, {})[filename] = data

    # Programs
    for rel_path, data in programs.items():
        parts = rel_path.replace("\\", "/").split("/")
        filename = "/".join(parts[1:])
        master["programs"][filename] = data

    # Build the cross-reference lookup
    id_lookup = build_id_lookup(entities)
    id_lookup_conn = build_id_lookup(connections)
    id_lookup_evid = build_id_lookup(evidence)

    master["_id_lookup"] = {
        "entities": id_lookup,
        "connections": id_lookup_conn,
        "evidence": id_lookup_evid,
        "total": len(id_lookup) + len(id_lookup_conn) + len(id_lookup_evid),
    }

    # Remove empty categories
    for layer_key in ["entities", "connections", "evidence"]:
        to_remove = [k for k, v in master[layer_key].items()
                     if isinstance(v, dict) and len(v) == 0]
        for k in to_remove:
            del master[layer_key][k]

    # Write the compiled file
    print("  Writing %s..." % OUTPUT)
    with open(OUTPUT, "w") as f:
        json.dump(master, f, indent=2, default=str)

    file_size = os.path.getsize(OUTPUT)
    print("  File size: %d bytes (%.1f KB)" % (file_size, file_size / 1024))
    print()

    # Summary
    print("  COMPILED STRUCTURE:")
    print()
    print("  _metadata           (counts, subtypes)")
    print("  _id_lookup          (%d entries)" % master["_id_lookup"]["total"])
    print("  index/              (%d files)" % len(master["index"]))
    for cat, items in sorted(master["entities"].items()):
        if isinstance(items, dict):
            n = sum(1 for v in items.values() if isinstance(v, dict) and "id" in v)
            if n == 0:
                n = sum(1 for v in items.values() if isinstance(v, dict))
            print("  entities/%-16s (%d)" % (cat, n))
    for cat, items in sorted(master["connections"].items()):
        if isinstance(items, dict):
            print("  connections/%-14s (%d)" % (cat, len(items)))
    for cat, items in sorted(master["evidence"].items()):
        if isinstance(items, dict):
            print("  evidence/%-16s (%d)" % (cat, len(items)))
    print("  programs/            (%d)" % len(master["programs"]))

    print()
    print("  To load in Python:")
    print("    import json")
    print("    with open('%s') as f:" % OUTPUT)
    print("        db = json.load(f)")
    print("    alpha = db['entities']['couplings']['alpha_inv.json']")
    print("    b2 = db['entities']['betas']['b2_mod.json']")
    print()

    # Verify round-trip: can we read back key values?
    print("  VERIFICATION:")
    with open(OUTPUT) as f:
        check = json.load(f)

    # alpha_inv
    ai = check["entities"]["couplings"].get("alpha_inv.json")
    if ai is not None:
        n = int(ai["value"]["fraction"]["numerator"])
        d = int(ai["value"]["fraction"]["denominator"])
        from fractions import Fraction
        got = Fraction(n, d)
        expected = Fraction(137035999177, 1000000000)
        if got == expected:
            print("    [PASS] alpha_inv = %s" % got)
        else:
            print("    [FAIL] alpha_inv: got %s" % got)

    # b2_mod
    b2 = check["entities"]["betas"].get("b2_mod.json")
    if b2 is not None:
        n = int(b2["value"]["fraction"]["numerator"])
        d = int(b2["value"]["fraction"]["denominator"])
        got = Fraction(n, d)
        if got == Fraction(-13, 6):
            print("    [PASS] b2_mod = %s" % got)
        else:
            print("    [FAIL] b2_mod: got %s" % got)

    # R2
    r2 = check["entities"]["geometric"].get("R2.json")
    if r2 is not None:
        n = int(r2["value"]["fraction"]["numerator"])
        d = int(r2["value"]["fraction"]["denominator"])
        got = Fraction(n, d)
        from mpmath import mp, mpf, pi as mpi
        mp.dps = 50
        our = mpf(n) / mpf(d)
        ref = mpi / 4
        if mp.nstr(our, 30) == mp.nstr(ref, 30):
            print("    [PASS] R2 = pi/4 to 30 digits")
        else:
            print("    [FAIL] R2 mismatch")

    # Integer source connection
    ym = check["connections"].get("integer_source", {}).get("YM_11_to_DM_22.json")
    if ym is not None:
        if ym["integer"] == 11:
            print("    [PASS] YM integer = 11")
        else:
            print("    [FAIL] YM integer: got %s" % ym["integer"])

    # Containment chain
    cont = check["connections"].get("containment", {})
    if len(cont) >= 10:
        print("    [PASS] containment chain: %d levels" % len(cont))
    else:
        print("    [FAIL] containment chain: only %d" % len(cont))

    # Evidence count
    scripts = check["evidence"].get("scripts", {})
    results = check["evidence"].get("results", {})
    print("    [PASS] evidence: %d scripts, %d results" % (len(scripts), len(results)))

    print()
    print("=" * 70)
    print("DATA-6 COMPILER: COMPLETE")
    print("    Loose files: data6/ (%d files)" % master["_metadata"]["counts"]["total_files"])
    print("    Compiled:    %s (%.1f KB)" % (OUTPUT, file_size / 1024))
    print("=" * 70)


if __name__ == "__main__":
    compile()

