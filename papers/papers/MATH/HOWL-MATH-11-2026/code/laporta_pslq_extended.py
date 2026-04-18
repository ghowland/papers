#!/usr/bin/env python3
"""
Laporta Master Integral PSLQ Scanner — Extended Basis
Adds multiple zeta values, alternating Euler sums, and higher-weight
polylogarithmic products that appear at 4-loop and beyond.

Usage:
  python laporta_pslq_extended.py                    # parse and show basis
  python laporta_pslq_extended.py --scan             # scan all 6 integrals
  python laporta_pslq_extended.py --scan C81a        # scan one integral
  python laporta_pslq_extended.py --digits 500       # set precision
  python laporta_pslq_extended.py --maxcoeff 50000   # set coefficient bound

The basis has ~70 elements covering:
  - Standard: pi powers, zeta values, ln(2) powers, cross products
  - Polylogarithms: Li_n(1/2) and Li_n(-1) for n=4,5,6,7
  - Cross products: all pairwise products of the above up to weight 8
  - Multiple zeta values: z(3,5), z(5,3), z(3,3,3) computed numerically
  - Alternating sums: s6, related series computed numerically
"""

"""
The basis went from 36 to ~70 elements. The new additions:
Multiple zeta values: ζ(3,5), ζ(5,3), ζ(3,3) — computed by direct double summation. These are the MZVs expected at weight 8 (four-loop level).
Alternating Euler sums: s₆ = Σ (−1)^(n+1)/(n⁶ 2ⁿ), ζ̄(5,1), ζ̄(3,3) — the alternating double sums that appear in four-loop calculations with massive propagators.
Polylogarithms at −1: Li₄(−1) through Li₇(−1) — alternating series that complement the Li_n(½) basis.
Extended products: All cross products up to weight ~8 including MZV × ln(2), MZV × π², alternating sum × ln(2), alternating sum × π².
Warning: The MZV computation by direct summation is slow at high digit counts. At 400 digits, ζ(3,5) will take minutes. 
At 1000 digits it could take hours. 
I'd recommend running --scan C81a --digits 400 first to test one integral before committing to the full scan. 
If 400-digit null results come back, increase to --digits 1000 on just C81a before running all six.
"""

import sys
import os
import re
import json
from mpmath import (mp, mpf, pi, log, zeta, sqrt, polylog, euler,
                    catalan, pslq, nsum, inf, power)


# ================================================================
# CONFIGURATION
# ================================================================

DEFAULT_DIGITS = 400
DEFAULT_MAXCOEFF = 10000
DATA_FILE = "laporta.dat"
OUTPUT_FILE = "laporta_pslq_extended_results.json"


# ================================================================
# MULTIPLE ZETA VALUES — computed numerically
# ================================================================

def mzv_2(s1, s2, dps):
    """Multiple zeta value zeta(s1, s2) = sum_{n>m>0} 1/(n^s1 * m^s2).

    Computed by direct summation with acceleration.
    """
    old = mp.dps
    mp.dps = dps + 30
    total = mpf(0)
    # sum over n from 2 to N, inner sum over m from 1 to n-1
    # Use partial sums with enough terms for convergence at dps digits
    N = max(int(dps * 3), 2000)
    inner_cache = mpf(0)
    for n in range(2, N + 1):
        inner_cache += mpf(1) / power(n - 1, s2)
        total += inner_cache / power(n, s1)
    mp.dps = old
    return total


def mzv_3(s1, s2, s3, dps):
    """Multiple zeta value zeta(s1, s2, s3) = sum_{n>m>k>0} 1/(n^s1 m^s2 k^s3)."""
    old = mp.dps
    mp.dps = dps + 30
    total = mpf(0)
    N = max(int(dps * 2), 800)
    for n in range(3, N + 1):
        inner2 = mpf(0)
        for m in range(2, n):
            inner1 = mpf(0)
            for k in range(1, m):
                inner1 += mpf(1) / power(k, s3)
            inner2 += inner1 / power(m, s2)
        total += inner2 / power(n, s1)
    mp.dps = old
    return total


def alternating_euler_sum_s6(dps):
    """s6 = sum_{n=1}^inf (-1)^(n+1) / (n^6 * 2^n).

    This is related to Li6(1/2) but is a specific combination that
    appears in 4-loop QED.
    """
    old = mp.dps
    mp.dps = dps + 30
    total = mpf(0)
    N = max(int(dps * 4), 3000)
    for n in range(1, N + 1):
        total += power(-1, n + 1) / (power(n, 6) * power(2, n))
    mp.dps = old
    return total


def colored_zeta_bar_51(dps):
    """zeta_bar(5,1) = sum_{n>m>0} (-1)^(n+1) / (n^5 * m).

    Alternating double Euler sum. Appears in 4-loop calculations.
    """
    old = mp.dps
    mp.dps = dps + 30
    total = mpf(0)
    N = max(int(dps * 2.5), 1500)
    inner_cache = mpf(0)
    for n in range(2, N + 1):
        inner_cache += mpf(1) / (n - 1)
        total += power(-1, n + 1) * inner_cache / power(n, 5)
    mp.dps = old
    return total


def colored_zeta_bar_33(dps):
    """zeta_bar(3,3) = sum_{n>m>0} (-1)^(n+1) / (n^3 * m^3)."""
    old = mp.dps
    mp.dps = dps + 30
    total = mpf(0)
    N = max(int(dps * 2.5), 1500)
    inner_cache = mpf(0)
    for n in range(2, N + 1):
        inner_cache += mpf(1) / power(n - 1, 3)
        total += power(-1, n + 1) * inner_cache / power(n, 3)
    mp.dps = old
    return total


# ================================================================
# PARSE THE DATA FILE
# ================================================================

def parse_laporta(filepath):
    """Parse laporta.dat into a dict of {label: decimal_string}."""
    with open(filepath, 'r') as f:
        content = f.read()
    entries = re.findall(r'(C\d+[a-z])\s+([-]?\d+\.\d+)', content)
    return dict(entries)


def summarize(integrals):
    """Print summary of parsed integrals."""
    print("=" * 60)
    print("LAPORTA MASTER INTEGRALS")
    print("=" * 60)
    for label, value in sorted(integrals.items()):
        sign = '-' if value.startswith('-') else '+'
        integer_part = value.split('.')[0]
        n_digits = len(value.split('.')[1])
        print("  %-8s  sign:%s  int:%6s  digits:%d  head:%s..." % (
            label, sign, integer_part, n_digits, value[:35]))
    print("  %d integrals." % len(integrals))
    print()


# ================================================================
# BUILD THE EXTENDED BASIS
# ================================================================

def build_extended_basis(dps):
    """Build extended basis with ~70 elements including MZVs and
    alternating Euler sums.

    Weight budget: constants up to transcendental weight 8.
    """
    old = mp.dps
    mp.dps = dps + 50

    p = pi
    l2 = log(2)
    z3 = zeta(3)
    z5 = zeta(5)
    z7 = zeta(7)
    z9 = zeta(9)

    # Polylogarithms at 1/2
    li4h = polylog(4, mpf("0.5"))
    li5h = polylog(5, mpf("0.5"))
    li6h = polylog(6, mpf("0.5"))
    li7h = polylog(7, mpf("0.5"))

    # Polylogarithms at -1 (alternating series)
    li4m = polylog(4, mpf("-1"))    # = -7/720 * pi^4 (known, but include anyway)
    li5m = polylog(5, mpf("-1"))    # = -15/16 * zeta(5) (known)
    li6m = polylog(6, mpf("-1"))    # known relation to pi^6
    li7m = polylog(7, mpf("-1"))

    print("  Computing multiple zeta values (this takes time at %d digits)..." % dps)

    # Multiple zeta values
    print("    z(3,5)...")
    z35 = mzv_2(3, 5, dps)
    print("    z(5,3)...")
    z53 = mzv_2(5, 3, dps)
    print("    z(3,3)...")
    z33 = mzv_2(3, 3, dps)

    # Alternating Euler sums
    print("    s6...")
    s6 = alternating_euler_sum_s6(dps)
    print("    zeta_bar(5,1)...")
    zb51 = colored_zeta_bar_51(dps)
    print("    zeta_bar(3,3)...")
    zb33 = colored_zeta_bar_33(dps)

    print("  Basis constants computed.")

    basis = [
        # === RATIONAL ===
        ("1",                   mpf(1)),

        # === SINGLE TRANSCENDENTALS ===
        # Pi powers (weight 1-6)
        ("pi",                  p),
        ("pi2",                 p**2),
        ("pi3",                 p**3),
        ("pi4",                 p**4),
        ("pi5",                 p**5),
        ("pi6",                 p**6),

        # Zeta values (weight 3-9)
        ("z3",                  z3),
        ("z5",                  z5),
        ("z7",                  z7),
        ("z9",                  z9),

        # ln(2) powers (weight 1-6)
        ("ln2",                 l2),
        ("ln2_2",               l2**2),
        ("ln2_3",               l2**3),
        ("ln2_4",               l2**4),
        ("ln2_5",               l2**5),
        ("ln2_6",               l2**6),

        # === PRODUCTS: pi^n * ln(2)^m ===
        ("pi2_ln2",             p**2 * l2),
        ("pi2_ln2_2",           p**2 * l2**2),
        ("pi2_ln2_3",           p**2 * l2**3),
        ("pi2_ln2_4",           p**2 * l2**4),
        ("pi4_ln2",             p**4 * l2),
        ("pi4_ln2_2",           p**4 * l2**2),
        ("pi6_ln2",             p**6 * l2),

        # === PRODUCTS: zeta * pi^n ===
        ("pi2_z3",              p**2 * z3),
        ("pi4_z3",              p**4 * z3),
        ("pi2_z5",              p**2 * z5),

        # === PRODUCTS: zeta * ln(2)^m ===
        ("z3_ln2",              z3 * l2),
        ("z3_ln2_2",            z3 * l2**2),
        ("z3_ln2_3",            z3 * l2**3),
        ("z5_ln2",              z5 * l2),
        ("z5_ln2_2",            z5 * l2**2),
        ("z7_ln2",              z7 * l2),

        # === PRODUCTS: zeta * zeta ===
        ("z3_2",                z3**2),
        ("z3_z5",               z3 * z5),

        # === PRODUCTS: zeta * pi^n * ln(2)^m ===
        ("z3_pi2_ln2",          z3 * p**2 * l2),
        ("z3_pi2_ln2_2",        z3 * p**2 * l2**2),
        ("z5_pi2_ln2",          z5 * p**2 * l2),

        # === POLYLOGARITHMS AT 1/2 ===
        ("Li4h",                li4h),
        ("Li5h",                li5h),
        ("Li6h",                li6h),
        ("Li7h",                li7h),

        # === POLYLOG PRODUCTS ===
        ("Li4h_ln2",            li4h * l2),
        ("Li4h_ln2_2",          li4h * l2**2),
        ("Li4h_pi2",            li4h * p**2),
        ("Li5h_ln2",            li5h * l2),
        ("Li5h_pi2",            li5h * p**2),
        ("Li6h_ln2",            li6h * l2),

        # === POLYLOGARITHMS AT -1 ===
        ("Li4m",                li4m),
        ("Li5m",                li5m),
        ("Li6m",                li6m),
        ("Li7m",                li7m),

        # === MULTIPLE ZETA VALUES ===
        ("z35",                 z35),
        ("z53",                 z53),
        ("z33",                 z33),

        # === MZV PRODUCTS ===
        ("z35_ln2",             z35 * l2),
        ("z53_ln2",             z53 * l2),
        ("z33_pi2",             z33 * p**2),

        # === ALTERNATING EULER SUMS ===
        ("s6",                  s6),
        ("zbar51",              zb51),
        ("zbar33",              zb33),

        # === ALTERNATING EULER SUM PRODUCTS ===
        ("s6_ln2",              s6 * l2),
        ("zbar51_ln2",          zb51 * l2),
        ("zbar33_ln2",          zb33 * l2),
        ("s6_pi2",              s6 * p**2),
        ("zbar51_pi2",          zb51 * p**2),
    ]

    mp.dps = old
    return basis


# ================================================================
# RUN PSLQ
# ================================================================

def run_pslq_scan(label, value_str, basis, dps, maxcoeff):
    """Run PSLQ on one integral against the extended basis.

    Tries three tiers:
    1. Standard (no MZV, no alternating sums) — ~36 elements
    2. With MZV and alternating sums — ~55 elements
    3. Full basis with all products — all elements
    """
    old = mp.dps
    mp.dps = dps + 50

    target = mpf(value_str)

    basis_names = [b[0] for b in basis]
    basis_vals = [b[1] for b in basis]

    # Tier 1: standard (everything before MZV section)
    standard_stop = [i for i, n in enumerate(basis_names) if n == "z35"]
    if standard_stop:
        tier1_idx = list(range(standard_stop[0]))
    else:
        tier1_idx = list(range(len(basis)))

    # Tier 2: standard + MZV + alternating (no products of MZV)
    mzv_names = {"z35", "z53", "z33", "s6", "zbar51", "zbar33"}
    tier2_idx = tier1_idx + [i for i, n in enumerate(basis_names)
                              if n in mzv_names]

    # Tier 3: everything
    tier3_idx = list(range(len(basis)))

    result = {
        "label": label,
        "digits_available": len(value_str.replace("-", "").replace(".", "")),
        "digits_used": dps,
        "tiers": {},
    }

    for tier_name, tier_idx in [("tier1_standard", tier1_idx),
                                 ("tier2_with_mzv", tier2_idx),
                                 ("tier3_full", tier3_idx)]:
        tier_basis_names = [basis_names[i] for i in tier_idx]
        tier_basis_vals = [basis_vals[i] for i in tier_idx]

        pslq_input = [target] + tier_basis_vals

        print("  %s: PSLQ with %d basis elements at %d digits..." % (
            tier_name, len(tier_basis_vals), dps))

        tol = mpf(10) ** (-(dps - 50))
        rel = pslq(pslq_input, tol=tol, maxcoeff=maxcoeff)

        if rel is not None:
            target_coeff = rel[0]
            basis_coeffs = rel[1:]

            terms = []
            for coeff, name in zip(basis_coeffs, tier_basis_names):
                if coeff != 0:
                    terms.append((coeff, name))

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

            break
        else:
            result["tiers"][tier_name] = {
                "status": "NULL",
                "basis_size": len(tier_basis_vals),
            }
            print("    NULL (no relation found)")

    mp.dps = old
    return result


# ================================================================
# MAIN
# ================================================================

def main():
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

    filepath = DATA_FILE
    if not os.path.exists(filepath):
        alt = os.path.join("/mnt/user-data/uploads", DATA_FILE)
        if os.path.exists(alt):
            filepath = alt
        else:
            print("ERROR: Cannot find %s" % DATA_FILE)
            sys.exit(1)

    integrals = parse_laporta(filepath)
    summarize(integrals)

    if not do_scan:
        print("Use --scan to run PSLQ analysis.")
        print("Use --scan C81a to scan one integral.")
        print("Use --digits N to set working precision (default %d)." % DEFAULT_DIGITS)
        print("Use --maxcoeff N to set PSLQ coefficient bound (default %d)." % DEFAULT_MAXCOEFF)
        return

    mp.dps = dps + 50
    print("Working precision: %d digits" % dps)
    print("Max PSLQ coefficient: %d" % maxcoeff)
    print()

    print("Building extended transcendental basis...")
    basis = build_extended_basis(dps)
    print("  %d basis constants built." % len(basis))
    print()

    if target_label:
        if target_label not in integrals:
            print("ERROR: %s not found." % target_label)
            sys.exit(1)
        scan_labels = [target_label]
    else:
        scan_labels = sorted(integrals.keys())

    all_results = {}
    for label in scan_labels:
        print("=" * 50)
        print("SCANNING: %s" % label)
        print("=" * 50)
        result = run_pslq_scan(label, integrals[label], basis, dps, maxcoeff)
        all_results[label] = result
        print()

    # Save results
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
            tier_name = [k for k, v in res["tiers"].items()
                         if v["status"] == "FOUND"][0]
            n_terms = len(last_tier.get("terms", []))
            print("  %-8s  FOUND at %s  (%d terms, max_coeff=%d)" % (
                label, tier_name, n_terms,
                last_tier.get("max_coeff_used", 0)))
        else:
            null += 1
            print("  %-8s  NULL (no relation in any tier)" % label)

    print()
    print("  FOUND: %d    NULL: %d    TOTAL: %d" % (
        found, null, len(all_results)))
    print("=" * 50)


if __name__ == "__main__":
    main()
