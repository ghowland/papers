#!/usr/bin/env python3
"""
Convert Laporta QED coefficients from laporta.dat to DATA-6 value JSON.

Input:  data/laporta.dat (whitespace-separated label + value per line)
Output: values_qed_laporta_v0.json

Stores each coefficient as a full-precision plain decimal string.
No truncation. No Fraction conversion. value_type = "approximate".
"""

import json
import sys
import os


def parse_laporta(filepath):
    """Parse laporta.dat: lines of 'LABEL  VALUE' with possible continuation."""
    entries = {}
    current_label = None
    current_value = ""

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(None, 1)
            if len(parts) == 2 and parts[0].startswith("C8"):
                # New entry
                if current_label is not None:
                    entries[current_label] = current_value.strip()
                current_label = parts[0]
                current_value = parts[1]
            else:
                # Continuation of previous value
                current_value += line

    if current_label is not None:
        entries[current_label] = current_value.strip()

    return entries


def make_node(key_suffix, label, value_str, description):
    """Build one DATA-6 value node."""
    return {
        "key": "qed_%s_v0" % key_suffix,
        "canonical": "qed_%s" % key_suffix,
        "version": 0,
        "node_type": "value",
        "topic": "qed",
        "term": key_suffix,
        "level": 1,
        "value": value_str,
        "value_type": "approximate",
        "unit": "dimensionless",
        "digits": len(value_str.replace("-", "").replace(".", "")),
        "source": "Laporta (private communication, 2026). Label: %s" % label,
        "tags": ["QED", "g-2", "Laporta", "coefficient"],
        "notes": description,
    }


# Map from file labels to our keys and descriptions
LABEL_MAP = {
    "C81a": ("c81a", "4-loop mass-independent (8th order, a)"),
    "C81b": ("c81b", "4-loop electron VP (8th order, b)"),
    "C81c": ("c81c", "4-loop light-by-light (8th order, c)"),
    "C83a": ("c83a", "5-loop mass-independent (10th order, a)"),
    "C83b": ("c83b", "5-loop electron VP (10th order, b)"),
    "C83c": ("c83c", "5-loop light-by-light (10th order, c)"),
}


def main():
    dat_path = os.path.join("data", "laporta.dat")
    if not os.path.exists(dat_path):
        print("ERROR: %s not found" % dat_path)
        return 1

    entries = parse_laporta(dat_path)
    print("Parsed %d entries from %s" % (len(entries), dat_path))

    nodes = []
    for label in ["C81a", "C81b", "C81c", "C83a", "C83b", "C83c"]:
        if label not in entries:
            print("WARNING: %s not found in file" % label)
            continue

        key_suffix, description = LABEL_MAP[label]
        value_str = entries[label]

        # Verify it's a valid decimal
        try:
            float(value_str[:20])
        except ValueError:
            print("ERROR: %s value doesn't parse as number" % label)
            continue

        node = make_node(key_suffix, label, value_str, description)
        digits = node["digits"]
        print("  %s -> qed_%s_v0  (%d digits)" % (label, key_suffix, digits))
        nodes.append(node)

    # Also compute and store the sums C8 = C81a+b+c, C10 = C83a+b+c
    # These need mpmath at full precision
    from mpmath import mp, mpf
    mp.dps = 3000

    if all(l in entries for l in ["C81a", "C81b", "C81c"]):
        c8 = mpf(entries["C81a"]) + mpf(entries["C81b"]) + mpf(entries["C81c"])
        c8_str = mp.nstr(c8, 1500)
        nodes.append(make_node("c8_total", "C81a+C81b+C81c", c8_str,
                               "4-loop total: C8 = C81a + C81b + C81c"))
        print("  C8 total -> qed_c8_total_v0  (%d digits)" % len(c8_str.replace("-","").replace(".","")))

    if all(l in entries for l in ["C83a", "C83b", "C83c"]):
        c10 = mpf(entries["C83a"]) + mpf(entries["C83b"]) + mpf(entries["C83c"])
        c10_str = mp.nstr(c10, 1500)
        nodes.append(make_node("c10_total", "C83a+C83b+C83c", c10_str,
                               "5-loop total: C10 = C83a + C83b + C83c"))
        print("  C10 total -> qed_c10_total_v0  (%d digits)" % len(c10_str.replace("-","").replace(".","")))

    output = {"nodes": nodes}
    out_path = os.path.join("data", "values_qed_laporta_v0.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print("\nWritten: %s (%d nodes)" % (out_path, len(nodes)))

    return 0


if __name__ == "__main__":
    sys.exit(main())
    