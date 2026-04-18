#!/usr/bin/env python3
"""
Laporta Master Integral Parser and PSLQ Scanner
Reads laporta.dat, parses the 6 master integrals (C81a-c, C83a-c),
and runs PSLQ against a configurable basis of transcendental constants.

Usage:
  python laporta_pslq.py              # parse and show summary
  python laporta_pslq.py --scan       # run PSLQ on all 6 integrals
  python laporta_pslq.py --scan C81a  # run PSLQ on one integral
  python laporta_pslq.py --digits 500 # set working precision (default 300)
  python laporta_pslq.py --maxcoeff 50000  # set PSLQ coefficient bound
"""

# Run python3 laporta_pslq.py to see the parse summary. 
# Run python3 laporta_pslq.py --scan C81a --digits 500 to test one integral at 500-digit precision. 
# Run python3 laporta_pslq.py --scan --digits 300 to scan all six.
# The output goes to laporta_pslq_results.json with full coefficients for any relations found.

import sys
import os
import re
import json
from fractions import Fraction
from mpmath import mp, mpf, pi, log, zeta, sqrt, polylog, euler, catalan, pslq

# ================================================================
# CONFIGURATION
# ================================================================

DEFAULT_DIGITS = 300
DEFAULT_MAXCOEFF = 10000
DATA_FILE = "laporta.dat"
OUTPUT_FILE = "laporta_pslq_results.json"


# ================================================================
# PARSE THE DATA FILE
# ================================================================

def parse_laporta(filepath):
    """Parse laporta.dat into a dict of {label: decimal_string}."""
    with open(filepath, 'r') as f:
        content = f.read()

    entries = re.findall(r'(C\d+[a-z])\s+([-]?\d+\.\d+)', content)
    result = {}
    for label, value in entries:
        result[label] = value
    return result


def summarize(integrals):
    """Print summary of parsed integrals."""
    print("=" * 60)
    print("LAPORTA MASTER INTEGRALS — PARSED")
    print("=" * 60)
    for label, value in sorted(integrals.items()):
        sign = '-' if value.startswith('-') else '+'
        integer_part, decimal_part = value.split('.')
        n_digits = len(decimal_part)
        print("  %-8s  sign: %s  integer: %6s  decimal digits: %d  first 40: %s..." % (
            label, sign, integer_part, n_digits, value[:40]))
    print("=" * 60)
    print("  %d integrals parsed." % len(integrals))
    print()


# ================================================================
# BUILD THE TRANSCENDENTAL BASIS
# ================================================================

def build_basis(dps):
    """Build the basis of transcendental constants for PSLQ.

    Returns list of (name, value) pairs.

    The basis is organized by what appears at each loop order:
    - 2-loop: pi^2, zeta(3), ln(2)
    - 3-loop: pi^4, zeta(5), pi^2*ln(2), ln^2(2), pi^2*zeta(3), Li4(1/2)
    - 4-loop: pi^6, zeta(7), zeta(5)*pi^2, zeta(3)^2, zeta(3)*pi^2*ln(2),
              pi^4*ln(2), pi^2*ln^3(2), ln^4(2), ln^5(2), Li4(1/2)*pi^2,
              Li5(1/2), Li4(1/2)*ln(2), s6 related constants
    """
    old_dps = mp.dps
    mp.dps = dps + 50  # extra guard digits

    # Fundamental constants
    p = pi
    l2 = log(2)
    z3 = zeta(3)
    z5 = zeta(5)
    z7 = zeta(7)
    z9 = zeta(9)

    # Polylogarithms at 1/2 (standard 4-loop basis)
    li4_half = polylog(4, mpf("0.5"))   # a4 in standard notation
    li5_half = polylog(5, mpf("0.5"))   # a5
    li6_half = polylog(6, mpf("0.5"))   # a6

    basis = [
        # Pure rational (the "1" term — PSLQ finds the rational part)
        ("1",               mpf(1)),

        # Powers of pi
        ("pi",              p),
        ("pi2",             p**2),
        ("pi3",             p**3),
        ("pi4",             p**4),
        ("pi5",             p**5),
        ("pi6",             p**6),

        # Zeta values
        ("z3",              z3),
        ("z5",              z5),
        ("z7",              z7),
        ("z9",              z9),

        # Powers of ln(2)
        ("ln2",             l2),
        ("ln2_2",           l2**2),
        ("ln2_3",           l2**3),
        ("ln2_4",           l2**4),
        ("ln2_5",           l2**5),

        # pi^2 * powers of ln(2)
        ("pi2_ln2",         p**2 * l2),
        ("pi2_ln2_2",       p**2 * l2**2),
        ("pi2_ln2_3",       p**2 * l2**3),

        # pi^4 * ln(2)
        ("pi4_ln2",         p**4 * l2),
        ("pi4_ln2_2",       p**4 * l2**2),

        # Cross products with zeta
        ("pi2_z3",          p**2 * z3),
        ("pi4_z3",          p**4 * z3),
        ("pi2_z5",          p**2 * z5),
        ("z3_2",            z3**2),
        ("z3_ln2",          z3 * l2),
        ("z3_ln2_2",        z3 * l2**2),
        ("z5_ln2",          z5 * l2),
        ("z3_pi2_ln2",      z3 * p**2 * l2),

        # Polylogarithms at 1/2
        ("Li4_half",        li4_half),
        ("Li5_half",        li5_half),
        ("Li6_half",        li6_half),

        # Polylog cross products
        ("Li4_half_ln2",    li4_half * l2),
        ("Li4_half_pi2",    li4_half * p**2),
        ("Li5_half_ln2",    li5_half * l2),
        ("Li5_half_pi2",    li5_half * p**2),
    ]

    mp.dps = old_dps
    return basis


# ================================================================
# RUN PSLQ ON ONE INTEGRAL
# ================================================================

def run_pslq_scan(label, value_str, basis, dps, maxcoeff):
    """Run PSLQ on one integral against the basis.

    Tries progressively larger subsets of the basis:
    1. Small basis (1, pi2, pi4, z3, z5, ln2, pi2*ln2, pi2*z3)
    2. Medium basis (adds pi6, z7, ln2 powers, polylog)
    3. Full basis (everything)

    Returns dict with results.
    """
    old_dps = mp.dps
    mp.dps = dps + 50

    target = mpf(value_str)

    # Define basis subsets by index ranges
    basis_names = [b[0] for b in basis]
    basis_vals = [b[1] for b in basis]

    # Tier 1: small (2-loop level constants)
    tier1_names = ["1", "pi2", "pi4", "z3", "z5", "ln2",
                   "pi2_ln2", "pi2_z3", "ln2_2"]
    tier1_idx = [i for i, n in enumerate(basis_names) if n in tier1_names]

    # Tier 2: medium (3-loop level)
    tier2_names = tier1_names + ["pi6", "z7", "ln2_3", "ln2_4",
                                  "pi2_ln2_2", "pi4_ln2",
                                  "z3_2", "z3_ln2", "Li4_half"]
    tier2_idx = [i for i, n in enumerate(basis_names) if n in tier2_names]

    # Tier 3: full basis
    tier3_idx = list(range(len(basis)))

    result = {
        "label": label,
        "digits_available": len(value_str.replace("-", "").replace(".", "")),
        "digits_used": dps,
        "tiers": {},
    }

    for tier_name, tier_idx in [("tier1_small", tier1_idx),
                                 ("tier2_medium", tier2_idx),
                                 ("tier3_full", tier3_idx)]:
        tier_basis_names = [basis_names[i] for i in tier_idx]
        tier_basis_vals = [basis_vals[i] for i in tier_idx]

        pslq_input = [target] + tier_basis_vals

        print("  %s: PSLQ with %d basis elements at %d digits..." % (
            tier_name, len(tier_basis_vals), dps))

        tol = mpf(10) ** (-(dps - 50))
        rel = pslq(pslq_input, tol=tol, maxcoeff=maxcoeff)

        if rel is not None:
            # rel[0] is the coefficient of the target
            # rel[1:] are coefficients of basis elements
            target_coeff = rel[0]
            basis_coeffs = rel[1:]

            # Build the expression
            terms = []
            for coeff, name in zip(basis_coeffs, tier_basis_names):
                if coeff != 0:
                    terms.append((coeff, name))

            # Verify
            check = sum(c * v for c, v in zip(rel, pslq_input))

            result["tiers"][tier_name] = {
                "status": "FOUND",
                "target_coeff": target_coeff,
                "terms": terms,
                "verification_residual": float(abs(check)),
                "max_coeff_used": max(abs(c) for c in rel),
            }

            print("    FOUND! target_coeff=%d, %d nonzero terms" % (
                target_coeff, len(terms)))
            for coeff, name in terms:
                print("      %+d * %s" % (coeff, name))
            print("    Verification: %.2e" % float(abs(check)))
            print("    Max coefficient: %d" % max(abs(c) for c in rel))

            # If found at this tier, skip larger tiers
            break
        else:
            result["tiers"][tier_name] = {
                "status": "NULL",
                "basis_size": len(tier_basis_vals),
            }
            print("    NULL (no relation found)")

    mp.dps = old_dps
    return result


# ================================================================
# MAIN
# ================================================================

def main():
    # Parse arguments
    args = sys.argv[1:]
    do_scan = "--scan" in args
    target_label = None
    dps = DEFAULT_DIGITS
    maxcoeff = DEFAULT_MAXCOEFF

    for i, arg in enumerate(args):
        if arg == "--digits" and i + 1 < len(args):
            dps = int(args[i + 1])
        elif arg == "--maxcoeff" and i + 1 < len(args):
            maxcoeff = int(args[i + 1])
        elif arg == "--scan" and i + 1 < len(args) and not args[i + 1].startswith("--"):
            target_label = args[i + 1]

    # Find data file
    filepath = DATA_FILE
    if not os.path.exists(filepath):
        # Try in uploads
        alt = os.path.join("/mnt/user-data/uploads", DATA_FILE)
        if os.path.exists(alt):
            filepath = alt
        else:
            print("ERROR: Cannot find %s" % DATA_FILE)
            sys.exit(1)

    # Parse
    integrals = parse_laporta(filepath)
    summarize(integrals)

    if not do_scan:
        print("Use --scan to run PSLQ analysis.")
        print("Use --scan C81a to scan one integral.")
        print("Use --digits N to set working precision (default %d)." % DEFAULT_DIGITS)
        print("Use --maxcoeff N to set PSLQ coefficient bound (default %d)." % DEFAULT_MAXCOEFF)
        return

    # Set precision
    mp.dps = dps + 50
    print("Working precision: %d digits" % dps)
    print("Max PSLQ coefficient: %d" % maxcoeff)
    print()

    # Build basis
    print("Building transcendental basis...")
    basis = build_basis(dps)
    print("  %d basis constants built." % len(basis))
    print()

    # Determine which integrals to scan
    if target_label:
        if target_label not in integrals:
            print("ERROR: %s not found in data file." % target_label)
            sys.exit(1)
        scan_labels = [target_label]
    else:
        scan_labels = sorted(integrals.keys())

    # Run PSLQ
    all_results = {}
    for label in scan_labels:
        print("=" * 50)
        print("SCANNING: %s" % label)
        print("=" * 50)
        result = run_pslq_scan(label, integrals[label], basis, dps, maxcoeff)
        all_results[label] = result
        print()

    # Save results
    # Convert for JSON serialization
    json_results = {}
    for label, res in all_results.items():
        jr = {
            "label": res["label"],
            "digits_available": res["digits_available"],
            "digits_used": res["digits_used"],
            "tiers": {},
        }
        for tier_name, tier_res in res["tiers"].items():
            jt = {"status": tier_res["status"]}
            if tier_res["status"] == "FOUND":
                jt["target_coeff"] = tier_res["target_coeff"]
                jt["terms"] = [{"coeff": c, "constant": n}
                               for c, n in tier_res["terms"]]
                jt["verification_residual"] = tier_res["verification_residual"]
                jt["max_coeff_used"] = tier_res["max_coeff_used"]
            else:
                jt["basis_size"] = tier_res.get("basis_size", 0)
            jr["tiers"][tier_name] = jt
        json_results[label] = jr

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(json_results, f, indent=2)
    print("Results written to %s" % OUTPUT_FILE)

    # Summary
    print()
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    found = 0
    null = 0
    for label, res in sorted(all_results.items()):
        last_tier = list(res["tiers"].values())[-1]
        status = last_tier["status"]
        if status == "FOUND":
            found += 1
            tier_name = [k for k, v in res["tiers"].items() if v["status"] == "FOUND"][0]
            n_terms = len(last_tier.get("terms", []))
            print("  %-8s  FOUND at %s  (%d terms, max_coeff=%d)" % (
                label, tier_name, n_terms, last_tier.get("max_coeff_used", 0)))
        else:
            null += 1
            print("  %-8s  NULL (no relation in any tier)" % label)

    print()
    print("  FOUND: %d    NULL: %d    TOTAL: %d" % (found, null, len(all_results)))
    print("=" * 50)


if __name__ == "__main__":
    main()
    

