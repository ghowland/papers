# HOWL Series Script Standard
## Operational rules for all computation scripts from PHYS-24 forward.

**Registry:** [@HOWL-SCRIPT-STANDARD-2026]

**Date:** April 2 2026

**Status:** Operational

**Location:** `./supplementary/phys24_script_rules.md` in every paper directory

---

## 1. Purpose

Every script in the HOWL series is a standalone demonstration of one concept. A future session reads the script and immediately understands what it computes, what it checks, and whether it passed. Scripts are the source of truth. Papers report what scripts produce. If a paper and a script disagree, the script wins.

---

## 2. Language and Compatibility

All scripts target Python 3.8+. No language features introduced after 3.8 are permitted. Specifically:

- No walrus operator `:=`
- No `match`/`case`
- No `type | None` union syntax
- No `assert` statements — use `if/else` with printed output. Asserts stop execution. We want all output, including failures.
- No f-strings with `=` (debug format). Use `%` formatting throughout for consistency.

---

## 3. Arithmetic Rule

All computation uses `Fraction` from the `fractions` module. No floating-point value ever enters the computation chain. The computation chain is: Fraction in, Fraction out, convert to `mpf` only at the display boundary.

The display boundary is where a number leaves the computation and enters a print statement or a numerical comparison against an mpf reference. At that boundary, and only there, Fraction converts to mpf via the standard converter `f2m`.

Exact algebraic comparisons (testing whether two Fractions are identical) stay in Fraction. Only approximate numerical comparisons convert through `f2m`. The check functions enforce this: `chk_exact` compares Fractions, `chk` and `chk_precision` compare mpf values.

---

## 4. Precision Rule

All mpmath work uses `mp.dps = 100` as the standing precision, set by `phys24_lib.py` on import. If a specific operation requires higher precision (e.g., mpmath cross-verification at 120 digits), save and restore:

```python
old_dps = mp.dps
mp.dps = 120
ref_value = mpi**2  # need extra headroom
mp.dps = old_dps    # restore immediately
```

The minimum print precision is 11 significant figures via `mp.nstr(value, 11)`. This is the floor. Scripts may print more digits when the source data supports it, but never fewer than 11.

**Never print raw floats or raw mpf values.** The expression `print(some_value)` where `some_value` is a float or mpf is prohibited. Every number in the output goes through `mp.nstr(value, N)` or the `show` helper. No exception.

**Threshold constants in numerical comparisons must be `mpf` strings, not Python float literals:**

```python
# CORRECT
chk_bool("gap in range", mpf("1.2") < f2m(gap) < mpf("1.5"), ..., checks)

# WRONG — bare float literals
chk_bool("gap in range", 1.2 < float(f2m(gap)) < 1.5, ..., checks)
```

---

## 5. The phys24_lib Rule

Every script begins with:

```python
from phys24_lib import *
```

This single import provides all constants, all helpers, all check functions. No script defines its own `f2m`, `chk`, `show`, or any constant. No script hardcodes a Q335 numerator, a measured value, or a beta coefficient. Everything comes from the library.

The library file `phys24_lib.py` lives in `./code/` alongside the scripts. The import is local — no package installation, no `sys.path` manipulation, no `__init__.py`.

If a script needs a value not in the library, the value is added to the library first, the library self-test is updated and re-run, and then the script imports it. No script ever contains a constant that belongs in the library.

**Platform versioning:** `phys24_lib.py` is the Session 4 platform. The name is a platform generation tag, not a PHYS paper number. If a future session needs new data (new PDG values, new constants, new derived quantities), the platform revs to `phys25_lib.py` or `phys36_lib.py`. All scripts in that session import the new platform. The old platform file is never deleted. The import line is the version pin:

```python
from phys24_lib import *   # Session 4 platform
from phys36_lib import *   # hypothetical Session 6 platform
```

To test a script against a new platform, change one line. Every variable name stays the same. The library API only grows — values are added, never removed. If a name collapses (two quantities found to be equal), the alias goes in the NAME MAPPINGS section at the end of the library, and no script code changes.

---

## 6. Standard Helpers

All helpers are defined in `phys24_lib.py` and imported via `from phys24_lib import *`. No script redefines them. The complete set:

| Helper | Purpose |
|---|---|
| `f2m(frac)` | Fraction to mpf at working precision |
| `digits_of(got, expected)` | Digits of numeric agreement (returns mpf) |
| `show(label, value)` | Print labeled mpf at 11+ significant figures |
| `chk(tag, got, expected, need, checks)` | Numerical agreement check (mpf vs mpf) |
| `chk_exact(tag, got, expected, checks)` | Exact Fraction identity check |
| `chk_bool(tag, condition, detail, checks)` | Boolean condition check |
| `chk_precision(tag, frac, pub_str, need, checks)` | Full precision reconstruction (string + numeric + source digit accounting) |
| `precision_report(frac, pub_str)` | Returns dict with complete precision metadata |
| `count_sig_digits(s)` | Count significant digits in a decimal string |
| `print_summary(checks)` | Print TOTAL: N PASS, M FAIL out of K |

`show(label, value)` expects an mpf. Convert Fractions via `f2m` before passing.

`digits_of(got, expected)` returns mpf always. It is designed for comparing quantities with known nonzero expected values. For quantities expected to be exactly zero, use `chk_bool` with an absolute tolerance instead.

`chk_precision` is for measured constants where the reference is a published decimal string. It reports: published string, rendered string, source significant digits, character-level match, numeric agreement, and whether agreement meets or exceeds source precision.

In chk_precision, pass/fail is determined by numeric agreement against the need threshold. String comparison is diagnostic — it reports character-level match or divergence but does not affect pass/fail. For values outside [0.001, 999999], mpmath may render in scientific notation against a plain-decimal published string. This is a display format difference, not a data error.

---

## 7. Check Block Format

The checks block appears at the end of every script, after all computation and display:

```python
# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

chk_exact("SM gap ratio = 218/115",
          gap_ratio_SM, Fraction(218, 115), checks)

chk_precision("alpha_inv reconstruction",
              alpha_inv, "137.035999177", 9, checks)

chk_bool("SM miss exceeds 30%%",
         sm_miss > mpf("30"),
         "miss = %s%%" % mp.nstr(sm_miss, 4), checks)

print_summary(checks)
```

Every script ends with `print_summary(checks)`. The format is always `TOTAL: N PASS, M FAIL out of K`. Check tags must be unique within a script.

---

## 8. Output Structure

Every script prints output in this order:

1. **Header:** `"=" * 70` banner with script title
2. **Inputs:** labeled, with phys24_lib variable names and DATA-4 entry IDs
3. **Computation steps:** numbered or labeled sections separated by `"-" * 70`
4. **Results:** the key finding, stated plainly
5. **Checks:** the standard check block from Section 7
6. **Footer:** `"=" * 70` banner with `[SCRIPT NAME] COMPLETE`

Section separators use two styles only:
- Major sections: `"=" * 70`
- Subsections: `"-" * 70`

---

## 9. Naming

Scripts for PHYS-24 use the prefix `phys24_`. Examples:
- `phys24_gap_ratio.py`
- `phys24_democracy.py`
- `phys24_cabibbo_doublet.py`

Session 3 scripts retain their original names. The prefix prevents confusion about which scripts are the Session 3 verified originals and which are PHYS-24 demonstrations.

---

## 10. Scope

Each script demonstrates ONE concept. If two concepts are independent, they go in separate scripts. The target is 50-100 lines of computation (not counting the standard import and check block). If a script exceeds 150 lines, it is probably doing two things and should be split.

---

## 11. DATA-4 References

Constants come from `phys24_lib.py` by name. Scripts reference library variables, not raw Fraction constructions. Comments in the script identify which library variable is used and its DATA-4 entry:

```python
# uses alpha_inv from phys24_lib (DATA-4 B1, Type M, 12 source digits)
# uses pi_f from phys24_lib (DATA-4 G1, Type A, 100+ digits)
# uses b1_SM from phys24_lib (DATA-4 N1, Type D, exact)
```

Every constant has two names in the library: `foo` (working value) and `foo_full` (maximum available precision). For most constants these are identical. When a higher-precision value becomes available, `foo_full` gets the new value while `foo` stays unchanged until all scripts are verified. Scripts use `foo` for normal work and `foo_full` when precision-critical.

If a script uses a _full value, state that choice in the Inputs section with a comment explaining why.

---

## 12. Cross-Verification Rule

After writing a script, the author must verify that every key output matches the corresponding Session 3 script output. The verification is:

- Run the new script
- Compare each key number to the Session 3 script output
- If they agree to the expected digit count: proceed
- If they disagree: stop and investigate before writing the paper

The Session 3 scripts remain the verified source of truth. The PHYS-24 scripts are demonstrations that must reproduce the same numbers. A "key output" is any number that appears in the paper's source-of-truth table or in the results section.

---

## 13. What Scripts Do Not Do

- Scripts do not create files
- Scripts do not import `math` (see Section 16)
- Scripts do not import libraries beyond `fractions`, `mpmath`, `sys`, and `phys24_lib`
- Scripts do not use `assert`
- Scripts do not use `float()` anywhere in the computation chain
- Scripts do not use bare `print(value)` — all values go through `mp.nstr` or `show`
- Scripts do not suppress errors — if something fails, it prints FAIL and continues
- Scripts do not use `try/except` around computation (only the `sys.set_int_max_str_digits` guard in phys24_lib.py)
- Scripts do not define constants that belong in the library
- Scripts do not redefine helper functions from the library
- Scripts do not print raw floats or mpf values without `mp.nstr` formatting
- Scripts do not use scientific notation in published reference strings passed to `chk_precision`

---

## 14. Scripts In Chat

The author writes scripts in chat as code blocks. The human operator runs them and sends back the output. The author never creates files directly during the script-writing phase. Scripts go to `./code/` only as final deliverables after all checks pass and the paper is complete.

This rule exists so the human operator is never out of the loop. Every script is reviewed before execution. Every output is reviewed before proceeding to the next script.

**One script per prompt.** The author writes one complete script per message. Do not combine two scripts into one message to save tokens — low tokens mean bad choices. If two scripts are needed, they are written in two separate messages. The human runs each one and sends back the output before the next script is written. The only exception is when the human explicitly requests multiple scripts in one message.

---

## 15. Error Recovery

If a script produces a FAIL:

1. Report the FAIL with full output
2. Diagnose: is it a script bug or a genuine discrepancy with Session 3?
3. If script bug: fix the script and rerun
4. If genuine discrepancy: stop all work and investigate before proceeding. Do not write the paper. Do not write the next script. Find the source of the discrepancy first.

Never paper over a FAIL. Never comment out a failing check. Never weaken a check threshold to make it pass. If a check fails, the check is telling you something. Listen to it.

**Crash semantics:** Check failures print FAIL and continue — the script runs to completion so all checks are reported. Invalid computation states (division by zero, missing assumptions, corrupted data) may hard-crash the script before the checks block. Hard crashes are acceptable diagnostic output and must not be hidden with `try/except`. A crash that prevents the TOTAL line from printing is itself a diagnostic: something is wrong before the checks.

---

## 16. The math Ban

The `math` module is banned from all HOWL scripts. It is float-based. Every numeric function in it (`math.log`, `math.sqrt`, `math.pi`, `math.exp`) returns a Python float. If any of those values touch the computation chain, the Fraction discipline is silently broken.

If you need `log` for display: use `mpmath.log`.
If you need `sqrt` for display: use `mpmath.sqrt`.
If you need `gcd`: use `Fraction`, which handles it internally.
If you need `pi`: use `pi_f` from phys24_lib (Fraction) or `mpmath.pi` (mpf at display boundary).

There is no legitimate use of `math` in a HOWL script.

---

## 17. Determinism

Scripts must be deterministic. They must not depend on:
- Current time or date
- Random number generation
- Locale or encoding settings
- Network access
- Filesystem state (except importing phys24_lib.py from `./code/`)
- Environment variables
- Platform-specific behavior

Given the same `phys24_lib.py`, the same script produces the same output every time on every machine running Python 3.8+ with mpmath installed.

---

## 18. Units

Every physical input and result label must include units or state "dimensionless." A number without a unit is ambiguous. The library comments already do this (MeV, m, Hz, GeV^-2, etc.). Scripts must continue the practice:

```python
# CORRECT
show("M_Z (MeV)", f2m(M_Z))
show("gap ratio (dimensionless)", f2m(gap_SM))

# WRONG — no units
show("M_Z", f2m(M_Z))
```

---

## 19. Output Medium Rules

These rules apply to all HOWL production, not just scripts:

- **Scripts:** Written in chat as code blocks. Never as file attachments. Never created directly in `./code/` during drafting. The human runs them, not the Claude.
- **Papers:** Written in chat as markdown. Never as docx. Never as file attachments during drafting.
- **Diagrams:** If a diagram is needed, write it as a Python script in chat that produces the diagram. The human runs it. No JavaScript. No interactive widgets. No browser-rendered visualizations. Python only.
- **Feedback:** The human runs the script, pastes the output back in chat. The Claude reviews the output and proceeds or diagnoses failures. This is the feedback loop. It is never bypassed.
- **Polls and widgets:** Never. The human types responses directly. No interactive UI elements.

---

## 20. Directory Structure

Every paper has this structure:

```
paper_name/
  ./code/
    phys24_lib.py          # platform library (copied into every paper)
    phys24_lib_test.py     # platform test (copied into every paper)
    phys24_scriptname.py   # paper-specific demonstration scripts
  ./supplementary/
    phys24_script_rules.md # this document
  paper_name.md            # the paper itself
```

The `./code/` directory contains the platform library and all scripts. Every script imports from the local copy: `from phys24_lib import *`. This means each paper is self-contained — copy the directory and it runs.

The `./supplementary/` directory contains this rules document and any other supporting material that is not a script or a paper.

When the platform revs (e.g., `phys36_lib.py`), the new library goes into `./code/` of every paper that uses it. Old papers keep their original `phys24_lib.py`. Each paper directory is a frozen snapshot of the platform it was written on.

---

## 21. The Docstring Standard

Every script begins with a docstring that includes:

```python
#!/usr/bin/env python3
"""
HOWL PHYS-NN DEMONSTRATION: [Title]
Filename: [script_name.py]
====================================
[One-line description of what this script demonstrates.]

Backed by: [Session 3 script name] ([N/N] checks)
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""
```

The `Backed by:` line identifies the Session 3 verified script this demonstration derives from. The `Platform:` line identifies the library version. Both are mandatory.


---

## 22. Summary

The standard is:

**Computation rules:**
- Fraction in, mpf at the display boundary, `mp.nstr` for all printed numbers
- 100 dps standing, 120 for headroom, save/restore for local changes
- No `math`, no `float()`, no `assert`, no raw prints
- One concept per script, 50-100 lines target
- Python 3.8 compatible

**Platform rules:**
- `from phys24_lib import *` — one import, all constants from library
- No hardcoded constants in scripts — everything from the library
- Platform versions by import line — change one line to test new data
- Library API only grows — values added, never removed

**Workflow rules:**
- Scripts written in chat, human runs and returns output
- One script per prompt unless human specifies otherwise
- Papers written in chat as markdown, never docx
- Diagrams as Python scripts, never JavaScript
- FAILs are investigated, never papered over
- Hard crashes are diagnostic, never hidden

**Check rules:**
- Four check types: `chk` (numeric), `chk_exact` (Fraction identity), `chk_bool` (condition), `chk_precision` (string + numeric reconstruction)
- Every script ends with `TOTAL: N PASS, M FAIL out of K`
- Check tags unique within a script
- Every key output cross-verified against Session 3 scripts

This standard applies to every script from PHYS-24 forward. Earlier scripts are not retroactively changed but new scripts must conform.

---

*These rules are operational from this point forward. They are not style preferences. They are the computational standard of the series.*

