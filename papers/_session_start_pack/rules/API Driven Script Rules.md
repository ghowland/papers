# HOWL API-Driven Demo and Experiment Script Rules

**Document:** api_demo_script_rules.md

**Version:** 1.0

**Date:** April 3, 2026

**Scope:** All demo scripts, experiment scripts, and platform library files in the HOWL series

**Companion document:** api_diagram_rules.md v2.0 (governs diagram scripts using the same libraries)

**Supersedes:** phys24_script_rules.md (for scripts using the expanded library system)

---

## 1. Purpose

This document governs how to write Python scripts that use the HOWL platform libraries to run experiments, produce demos, make predictions, and generate results with full provenance. It also governs how the libraries themselves are structured, versioned, and upgraded.

The goal: any script written today runs unchanged in Session 100. Any result produced today traces to the library function that produced it. Any library upgraded tomorrow does not break any script written yesterday.

---

## 2. The Platform Pack

### 2.1 Definition

A platform pack is a specific set of library files at specific versions that work together. A script declares which pack it uses. The pack is the unit of reproducibility.

### 2.2 Current Pack: HOWL-PLATFORM-v1

| Library | File | Checks | Content |
|---|---|---|---|
| Foundation | phys24_lib.py | 21/21 + 148/148 | Constants, helpers, check functions |
| Derivations | data_4_derivation_lib.py | 37/37 | Coupling extraction, running, predictions |
| Structures | phys24_structure_lib.py | 46/46 | Representations, census, catalog, cross-refs |
| Boundaries | phys24_boundary_map_lib.py | 14/14 | 19 boundaries, forces, traversal |
| Domains | phys24_domain_lib.py | 40/40 | 17 domains, 22 R₂ equations, helpers |
| Hubble | phys24_hubble_lib.py | 16/17 | Running curve hypothesis, falsification |
| Diagrams | data_5_diagram_lib.py | 7 test figs | Plot helpers, provenance tracking |
| **Total** | **7 files** | **322/323** | **1 physically meaningful FAIL** |

### 2.3 Pack Declaration

Every script begins with a pack declaration comment:

```python
# Platform: HOWL-PLATFORM-v1
```

This tells any future session exactly which library versions the script was written against.

### 2.4 Pack Versioning

When a library is added or upgraded, the pack version increments:

```
HOWL-PLATFORM-v1  — Session 4 (April 3 2026), 7 libraries
HOWL-PLATFORM-v2  — (future) adds new library or upgrades existing
```

Old pack versions are never deleted. A script declaring v1 runs against v1 libraries. A script declaring v2 runs against v2 libraries. The structural upgrade protocol (Section 6) ensures v1 scripts also run against v2 libraries.

---

## 3. Script Categories

### 3.1 Demo Scripts

Demonstrate what the libraries can do. Import multiple libraries, call functions, print results with checks. Used to verify the platform works and to show future sessions how to use it.

Examples: `phys24_demo.py`, `demo_cross_domain.py`, `demo_platform_diagrams.py`

### 3.2 Experiment Scripts

Test a specific hypothesis or compute a specific prediction. Import the needed libraries, run the computation, report results with provenance. These are the scripts that papers cite.

Examples: `hubble_diagrams.py`, future scripts testing α_s at two-loop, sin²θ_W predictions, boundary-law calibrations

### 3.3 Library Files

The platform libraries themselves. Each is both a library (importable) and a demo (runnable with self-test). Every library ends with `if __name__ == "__main__":` that runs all its checks.

### 3.4 Diagram Scripts

Governed by api_diagram_rules.md v2.0. Import data_5_diagram_lib.py and the platform. Produce PNG figures with provenance.

---

## 4. Writing Scripts

### 4.1 Always in Chat

All scripts are written IN CHAT. Never as file attachments. The human must be able to read, verify, and run the script themselves. This is the fundamental delivery rule — it applies to libraries, demos, experiments, and diagram scripts.

### 4.2 Python 3.8 Compatible

All code is Python 3.8 compatible:

- No f-strings with `=` (3.8 does not support)
- No walrus operator in comprehensions
- No `match` statements
- No positional-only parameters
- Use `%` string formatting: `"value = %s" % mp.nstr(x, 4)`
- Use `os.path.join()` not pathlib

### 4.3 Fraction Arithmetic Throughout

All computation uses Fraction arithmetic from phys24_lib.py. No `math` module. No `float()` conversions in the derivation chain. No `assert` statements.

- Constants as Fraction: `alpha_inv = Fraction(137035999177, 1000000000)`
- Conversion to mpf at display boundary only: `f2m(alpha_inv)`
- Threshold values as mpf from string: `mpf("91187.6")` not `mpf(91187.6)`
- Standing precision: `mp.dps = 100` (set by phys24_lib.py)

### 4.4 All Constants from Libraries

Every physics constant comes from a library import. Never hardcode a mass, coupling, beta coefficient, or measured value in a script.

```python
# CORRECT
from phys24_lib import *
show("alpha_s", f2m(alpha_s))

# WRONG
alpha_s = 0.1180  # NEVER DO THIS
```

### 4.5 All Computation from Library Functions

Every computation calls a library function. If a computation is done more than once across scripts, it belongs in a library, not in the script.

```python
# CORRECT: library function computes, script reports
result = predict_alpha_s_two_loop(inv_a1, inv_a2, inv_a3,
                                   [b1_mod, b2_mod, b3_mod], b_ij_full)
show("alpha_s prediction", result["alpha_s_pred"])

# WRONG: script reimplements the computation
L = mlog(f2m(M_GUT) / f2m(M_Z)) / (mpf("2") * mpi)
# ... 20 lines of running code ...
```

### 4.6 Check Functions for Every Claim

Every numerical result is verified with `chk()`, `chk_exact()`, `chk_bool()`, or `chk_precision()` from phys24_lib.py. Every script ends with `print_summary(checks)`.

```python
checks = []
# ... computation ...
chk("alpha_s 2-loop", result["alpha_s_pred"], mpf("0.1184"), 3, checks)
chk_bool("tension > 4 sigma", H0_tension > mpf("4"), "...", checks)
# ... more checks ...
print_summary(checks)
```

### 4.7 Display via show() and mp.nstr()

All printed numbers use `show(label, value)` or `mp.nstr(value, N)` with N >= 11 significant figures. Never `print(float(x))`.

```python
# CORRECT
show("M_GUT", f2m(M_GUT_MeV))
print("  miss = %s%%" % mp.nstr(miss_pct, 4))

# WRONG
print(float(M_GUT_MeV))
print("miss = %.2f%%" % float(miss_pct))
```

---

## 5. Script Structure

### 5.1 Standard Header

```python
#!/usr/bin/env python3
"""
HOWL {Category}: {Title}
{Description of what this script demonstrates or tests.}

Platform: HOWL-PLATFORM-v1
Libraries: phys24_lib, data_4_derivation_lib, [others as needed]
Output: terminal (demo/experiment) or PNG (diagram)
"""

# Platform: HOWL-PLATFORM-v1

from phys24_lib import *
from data_4_derivation_lib import *
# ... additional imports ...
```

### 5.2 Section Structure

Each logical section is clearly delineated:

```python
# ================================================================
# SECTION N: TITLE IN CAPS
# What this section computes and why
# ================================================================
```

### 5.3 Check Collection

```python
checks = []

# Section 1
# ... computation and chk() calls ...

# Section 2
# ... computation and chk() calls ...

# Final
print_summary(checks)
```

### 5.4 Standard Footer

```python
n_fail = sum(1 for _, s in checks if s == "FAIL")
if n_fail == 0:
    print("  ALL PASS")
else:
    print("  %d FAILURES" % n_fail)
    for tag, status in checks:
        if status == "FAIL":
            print("    - %s" % tag)

print()
print("=" * 70)
print("{SCRIPT NAME} COMPLETE")
print("=" * 70)
```

---

## 6. The Structural Upgrade Protocol

This is the most important section in this document. It governs how libraries evolve without breaking scripts.

### 6.1 The Five Rules

**Rule 1: Functions are never removed.** If a function is superseded by a better version, the old function stays. Add a comment: `# Superseded by new_function() in v2, kept for backward compatibility`.

**Rule 2: Functions are never renamed.** If a better name is found, add an alias:

```python
def old_name(...):
    """Original function. See also: new_name()."""
    ...

def new_name(...):
    """Improved version. Alias for old_name where compatible."""
    ...
```

**Rule 3: Parameters are never removed from function signatures.** New parameters are added with defaults that preserve old behavior:

```python
# v1
def predict_alpha_s(inv_a1, inv_a2, inv_a3, betas, bij):
    ...

# v2: added threshold_corrections parameter
def predict_alpha_s(inv_a1, inv_a2, inv_a3, betas, bij,
                     threshold_corrections=None):
    # If threshold_corrections is None, behaves exactly like v1
    ...
```

**Rule 4: Dict keys in data objects are never removed.** New keys are added:

```python
# v1
H0_MEASUREMENTS["SH0ES"] = {
    "H0": Fraction(730, 10),
    "uncertainty": Fraction(10, 10),
    "effective_N": None,
}

# v2: added new key, old keys unchanged
H0_MEASUREMENTS["SH0ES"] = {
    "H0": Fraction(730, 10),
    "uncertainty": Fraction(10, 10),
    "effective_N": None,
    "systematic_correction": None,  # NEW in v2
}
```

**Rule 5: Constants are never changed.** If a measurement is updated, the old value stays with a version suffix and the new value gets a new name:

```python
# v1
alpha_s = Fraction(59, 500)          # 0.1180, PDG 2022

# v2: updated measurement, old preserved
alpha_s = Fraction(59, 500)          # 0.1180, PDG 2022 (original)
alpha_s_v2 = Fraction(1181, 10000)   # 0.1181, PDG 2024 (updated)
```

The base name (`alpha_s`) always keeps its original value. Upgraded values get version suffixes. Every script that used `alpha_s` continues to get 0.1180.

### 6.2 Version Tracking in Libraries

Every library has a version block at the top:

```python
_LIB_VERSION = "1"
_LIB_VERSION_1 = "Session 4, April 3 2026. Initial release. 40/40 checks."
# Future:
# _LIB_VERSION_2 = "Session N, date. Added X. N/N checks."
# _LIB_VERSION_3 = "Session M, date. Added Y. N/N checks."
```

The version history is cumulative. Each entry says what was added and the check count at that version. The `_LIB_VERSION` variable always points to the latest version number.

### 6.3 What Upgrading Looks Like

A future session upgrades phys24_domain_lib.py:

```python
_LIB_VERSION = "2"
_LIB_VERSION_1 = "Session 4, April 3 2026. Initial release. 40/40 checks."
_LIB_VERSION_2 = "Session 7, April 10 2026. Added NAND data. 45/45 checks."

# NEW in v2: NAND flash data
NAND_DATA = {
    "SLC": {"bits_per_cell": 1, "endurance_cycles": 100000},
    "MLC": {"bits_per_cell": 2, "endurance_cycles": 10000},
    "TLC": {"bits_per_cell": 3, "endurance_cycles": 3000},
    "QLC": {"bits_per_cell": 4, "endurance_cycles": 1000},
}
```

Every script written against v1 continues to work because nothing was removed, renamed, or changed. The new data is simply available for new scripts.

---

## 7. Paper Integration

### 7.1 Paper Pack

Each paper has a `./code/` directory containing copies of the platform libraries it uses. This is the paper's pack — frozen at the version used when the paper was written.

```
HOWL-PHYS-30/
  paper.md
  code/
    phys24_lib.py           # copied from platform
    data_4_derivation_lib.py
    phys24_structure_lib.py
    data_5_diagram_lib.py
    phys30_backing_script.py
    phys30_diagrams.py
  figures/
    phys30_01_alpha_s.png
    phys30_02_running.png
    ...
```

### 7.2 Library Provenance

When a library is copied into a paper's `./code/`, its version history travels with it. A reader can see `_LIB_VERSION = "1"` and know exactly which version of the library produced the paper's results.

### 7.3 Result Provenance Chain

The full chain for any plotted or printed number:

```
Diagram/Demo script
  ↓ calls
Library function (logged with prov())
  ↓ uses
Platform constant (from phys24_lib.py)
  ↓ traced to
DATA-4 entry (measured value with source)
```

Every link in this chain is recorded: the script's `prov()` call logs the function, the function's docstring names its inputs, phys24_lib.py maps each constant to its DATA-4 entry.

---

## 8. Experiment Design

### 8.1 Hypothesis Scripts

For scripts testing a hypothesis (like phys24_hubble_lib.py):

1. Mark the hypothesis status clearly: `HYPOTHESIS_STATUS = "ACTIVE_INVESTIGATION"`
2. Separate measured data (Level 2, verified) from hypothesis components (unverified)
3. Encode falsification tests as callable functions
4. Mark every unknown as `None`, never as a guess presented as fact
5. Include a reminder in the self-test output that the library encodes a hypothesis

### 8.2 Null Results

Null results are results. When a falsification test fails or a prediction misses:

1. Keep the FAIL in the self-test — do not suppress it
2. Write a null report explaining what the FAIL means
3. Add the null to the library's documentation
4. Future sessions see the FAIL and understand its meaning

```python
# The F1 strict FAIL is kept — it tells us SH0ES and H0LiCOW
# are in the same distance class, not strictly ordered.
```

### 8.3 Updated Results

When new data changes a result:

1. Keep the old result with a version suffix
2. Add the new result with the updated data
3. Both are accessible — the old for reproducibility, the new for current work

```python
alpha_s_prediction_v1 = mpf("0.11838")  # Session 4, two-loop full b_ij
# Future:
# alpha_s_prediction_v2 = mpf("...")    # Session N, with threshold corrections
```

---

## 9. Library Self-Test Requirements

### 9.1 Every Library is Runnable

Every library file works as both an importable module and a standalone test:

```bash
python phys24_lib.py              # 21/21
python data_4_derivation_lib.py   # 37/37
python phys24_structure_lib.py    # 46/46
python phys24_boundary_map_lib.py # 14/14
python phys24_domain_lib.py       # 40/40
python phys24_hubble_lib.py       # 16/17
python data_5_diagram_lib.py      # 7 test figures
```

### 9.2 Self-Test Coverage

The self-test must cover:

- Every exported function (at least one call with known output)
- Every data object (count check: "3 optical disc formats")
- Every cross-reference (if function A uses constant B, test that A(B) gives the expected result)
- Every known edge case or pitfall (documented in the function's docstring)

### 9.3 Self-Test Output Format

```
======================================================================
{LIBRARY_NAME} SELF-TEST
======================================================================

{SECTION NAME}
----------------------------------------------------------------------

  [PASS] {test description}
        {details}
  [FAIL] {test description}
        {details}

  TOTAL: N PASS, M FAIL out of K

  {LIBRARY_NAME}: OPERATIONAL (or: N FAILURES)
  
======================================================================
{LIBRARY_NAME} SELF-TEST COMPLETE
======================================================================
```

---

## 10. Import Patterns

### 10.1 Minimal (constants only)

```python
from phys24_lib import *
```

### 10.2 Computation (constants + derivations)

```python
from phys24_lib import *
from data_4_derivation_lib import *
```

### 10.3 Full Platform

```python
from phys24_lib import *
from data_4_derivation_lib import *
from phys24_structure_lib import *
from phys24_boundary_map_lib import *
from phys24_domain_lib import *
```

### 10.4 Full Platform + Hypothesis

```python
from phys24_lib import *
from data_4_derivation_lib import *
from phys24_structure_lib import *
from phys24_boundary_map_lib import *
from phys24_domain_lib import *
from phys24_hubble_lib import *
```

### 10.5 Diagram Script

```python
from data_5_diagram_lib import *
from phys24_lib import *
# ... additional computation libraries as needed
```

---

## 11. Prohibited Patterns

### 11.1 No `math` Module

```python
import math  # NEVER
```

Use mpmath via phys24_lib.py: `from mpmath import pi as mpi, log as mlog, sqrt as msqrt`

### 11.2 No `float()` in Derivation Chain

```python
x = float(some_fraction)  # NEVER in computation
y = x * 2.5              # NEVER — loses precision

# CORRECT
x = f2m(some_fraction)    # Fraction → mpf at full precision
y = x * mpf("2.5")
```

### 11.3 No `assert`

```python
assert result > 0  # NEVER
```

Use `chk_bool("result positive", result > mpf("0"), "...", checks)` instead.

### 11.4 No Hardcoded Physics

```python
M_Z = 91.1876  # NEVER
```

Use `from phys24_lib import M_Z` instead.

### 11.5 No `print(float(...))`

```python
print(float(value))           # NEVER
print("%.4f" % float(value))  # NEVER
```

Use `show("label", value)` or `mp.nstr(value, N)` instead.

### 11.6 No Raw Matplotlib in Diagram Scripts

```python
fig, ax = plt.subplots(...)           # NEVER in diagram scripts
fig.patch.set_facecolor('#0a0a12')    # NEVER — use dark_fig()
```

Use `fig, ax = dark_fig("Title")` from data_5_diagram_lib.py.

---

## 12. Inherited Rules from phys24_script_rules.md

The following rules from the original phys24_script_rules.md are inherited without change:

- Fraction arithmetic throughout
- `mpf` at display boundary only via `f2m()`
- `mp.dps = 100` standing precision (set by phys24_lib.py)
- All printed numbers via `mp.nstr(value, N)` with N >= 11
- Threshold constants as `mpf("string")`, never Python float literals
- Every constant from phys24_lib, never hardcoded
- Every script ends with `print_summary(checks)`

### What Is Superseded

| Old Rule | Superseded By | Reason |
|---|---|---|
| "Import only phys24_lib" | Section 10 (import patterns) | Multiple libraries now available |
| "One backing script per paper" | Section 7 (paper pack) | Paper uses a pack of libraries |
| "Self-contained computation" | Section 4.5 (library functions) | Computation lives in libraries, scripts call functions |
| "Manual value verification" | Section 7.3 (provenance chain) | Provenance system replaces manual checking |

---

## 13. Quick Reference Card

### New Library

```python
_LIB_VERSION = "1"
_LIB_VERSION_1 = "Session N, date. Purpose. Checks."

from phys24_lib import *
# ... data objects and functions ...

if __name__ == "__main__":
    checks = []
    # ... self-test ...
    print_summary(checks)
```

### New Demo Script

```python
# Platform: HOWL-PLATFORM-v1
from phys24_lib import *
from data_4_derivation_lib import *

checks = []
# ... sections with computation and chk() calls ...
print_summary(checks)
```

### New Diagram Script

```python
# Platform: HOWL-PLATFORM-v1
from data_5_diagram_lib import *
from phys24_lib import *
set_outdir("../figures")

fig, ax = dark_fig("Title")
val = library_function(library_constant)
prov("name", val, "library_function()")
data_point(ax, x, val, "label", GREEN)
save_fig(fig, "paper_01_desc.png")

print_provenance()
```

### Upgrade a Library

```python
# Change _LIB_VERSION
_LIB_VERSION = "2"
# Add version history line
_LIB_VERSION_2 = "Session M, date. Added X. N/N checks."
# Add new data/functions (never remove or rename old ones)
NEW_DATA = { ... }
def new_function(...): ...
# Add new self-test checks
chk_bool("new data loaded", len(NEW_DATA) == 4, "...", checks)
```

---

*api_demo_script_rules.md v1.0. Governs all demo scripts, experiment scripts, and platform libraries in the HOWL series. Companion to api_diagram_rules.md v2.0. Supersedes phys24_script_rules.md for scripts using the expanded library system. The structural upgrade protocol ensures every script written today runs unchanged in every future session. April 3, 2026.*
