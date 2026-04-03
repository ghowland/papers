# HOWL API-Driven Diagram Script Rules

**Document:** api_diagram_rules.md

**Version:** 2.0

**Date:** April 3, 2026

**Supersedes:** diagram_script_rules.md v1.0 (D1-D17)

**Scope:** All diagram-producing Python scripts in the HOWL series from Session 4 forward

**Companion document:** api_demo_script_rules.md (forthcoming — governs demo/experiment scripts)

---

## What Changed and Why

The v1.0 rules assumed every diagram script was self-contained: it defined its own colors, its own helpers, its own data, and its own style functions. This produced 600+ line scripts for 8 figures, with hardcoded physics values that had to be manually verified against papers.

The v2.0 rules assume every diagram script imports data_5_diagram_lib.py and the platform libraries. The diagram library provides colors, helpers, figure creation, and provenance tracking. The platform libraries provide every physics value. The diagram script contains only figure-specific layout logic — typically 10-20 lines per figure instead of 50-80.

The v1.0 rules (D1-D17) are inherited where they apply. The new rules add the library-driven workflow, provenance requirements, and the structural upgrade protocol. No v1.0 rule is removed — they are superseded where the new rules are more specific.

---

## A. ARCHITECTURE

### A1. The Library Stack

Every diagram script imports from this stack. No exceptions.

```python
# Required: diagram helpers
from data_5_diagram_lib import *

# Required: platform constants
from phys24_lib import *

# As needed: computation functions
from data_4_derivation_lib import *

# As needed: structured data
from phys24_structure_lib import *

# As needed: boundary traversal
from phys24_boundary_map_lib import *

# As needed: domain data and cross-domain functions
from phys24_domain_lib import *

# As needed: hypothesis libraries
from phys24_hubble_lib import *
```

### A2. What Lives Where

| Content | Location | Example |
|---|---|---|
| Colors, fonts, DPI, background | data_5_diagram_lib.py | `BG`, `GOLD`, `GAUGE_COLORS` |
| Figure creation and save | data_5_diagram_lib.py | `dark_fig()`, `save_fig()` |
| Plot primitives | data_5_diagram_lib.py | `measurement_band()`, `data_point()`, `threshold_line()` |
| Composite figures | data_5_diagram_lib.py | `convergence_bar_figure()`, `running_figure()` |
| Provenance logging | data_5_diagram_lib.py | `prov()`, `print_provenance()` |
| Physics constants | phys24_lib.py | `alpha_inv`, `b1_SM`, `gap_VL` |
| Derivation functions | data_4_derivation_lib.py | `predict_alpha_s_two_loop()` |
| Representations and census | phys24_structure_lib.py | `make_rep()`, `generation_betas()` |
| Boundary data and traversal | phys24_boundary_map_lib.py | `traverse()`, `BOUNDARY_STACK` |
| Domain equations and helpers | phys24_domain_lib.py | `disc_spot_size()`, `wire_resistance()` |
| Figure-specific layout | The diagram script itself | Axis limits, label positions, annotation offsets |

### A3. What the Diagram Script Contains

The diagram script itself contains ONLY:

1. Imports from the stack
2. `set_outdir()` call
3. Per-figure blocks: library calls → `prov()` → plot calls → `save_fig()`
4. `print_provenance()` at the end

It does NOT contain:

- Color definitions (use library)
- Style functions (use library)
- Matplotlib boilerplate (use library)
- Physics constants (use platform)
- Computation logic (use derivation library)
- Helper function definitions (use library)

---

## B. PROVENANCE

### B1. The Provenance Rule

Every physics value plotted in a diagram MUST be logged with `prov(name, value, source)` where source is the function call or variable name that produced it. This is mandatory, not optional.

```python
# CORRECT: value from library, logged
as_pred = predict_alpha_s_two_loop(inv_a1, inv_a2, inv_a3, ...)
prov("alpha_s_2L", as_pred["alpha_s_pred"], "predict_alpha_s_two_loop(b_ij_full)")

# WRONG: value typed by hand, not logged
as_pred = 0.11838  # DO NOT DO THIS
```

### B2. Provenance Report

Every diagram script ends with `print_provenance()`. The output lists every value with its figure number and source. The report is the audit trail — a reviewer can verify that every plotted number traces to a library function.

### B3. Zero Hardcoded Physics

The provenance report must show "0 hardcoded physics values." Visual parameters (axis limits, label positions, font sizes, annotation offsets) are not physics and do not need provenance. But any number that represents a measurement, prediction, coupling, mass, ratio, threshold, or physical constant MUST come from a library import or function call.

### B4. Provenance Survives Refactoring

If a library function is renamed or restructured, the diagram script updates its import and its `prov()` source string. The provenance chain is maintained across library versions.

---

## C. FIGURE CREATION

### C1. Figure Types (from data_5_diagram_lib.py)

| Function | Returns | Use for |
|---|---|---|
| `dark_fig(title, size, xlabel, ylabel)` | `(fig, ax)` | Standard single-panel figure |
| `dark_fig_dual(title_l, title_r, size, wspace)` | `(fig, ax1, ax2)` | Side-by-side comparison |
| `dark_canvas(title, size)` | `(fig, ax)` | Freeform drawing (axis off) |

All three set dark background, styled spines, grid, and tick colors automatically.

### C2. Plot Primitives

| Function | What it does | Lines saved vs raw matplotlib |
|---|---|---|
| `measurement_band(ax, val, unc, label)` | 1σ+3σ shaded band + center line + label | 5 lines → 1 |
| `measurement_band_v(ax, val, unc, label)` | Vertical measurement band | 5 → 1 |
| `threshold_line(ax, x, label)` | Labeled dashed line | 3 → 1 |
| `data_point(ax, x, y, label, color)` | Scatter with white edge + label | 3 → 1 |
| `data_point_err(ax, x, y, yerr, label)` | Point + error bar | 5 → 1 |
| `measured_diamond(ax, x, y, label)` | Diamond marker for measured values | 3 → 1 |
| `curve(ax, x, y, label, color)` | Styled line plot | 2 → 1 |
| `shaded_region(ax, x0, x1, color, label)` | Vertical shaded zone | 3 → 1 |
| `shaded_region_h(ax, y0, y1, color, label)` | Horizontal shaded zone | 3 → 1 |
| `result_box(ax, x, y, text)` | Highlighted result label | 4 → 1 |
| `note(ax, x, y, text)` | Small annotation | 2 → 1 |
| `arrow_label(ax, xd, yd, xt, yt, text)` | Annotation with arrow | 4 → 1 |
| `legend(ax)` | Styled legend | 2 → 1 |

### C3. Bar and Grouped Bar Charts

```python
bar_chart(ax, labels, values, colors)
grouped_bars(ax, categories, groups, group_colors, group_labels)
```

Both handle xtick labeling, value display, and styling automatically.

### C4. Physics-Specific Helpers

```python
plot_gauge_running(ax, log_mu, inv_a_MZ, betas)      # Three coupling curves
plot_H0_running(ax, N_array, H0_0, r)                 # Hubble running curve
plot_H0_data(ax, measurements, N_assignments)          # H0 data with errors
one_loop_run(inv_a0, b, log_mu0, log_mu_array)        # Numpy array of running
```

### C5. Composite Helpers (complete figures in one call)

```python
convergence_bar_figure(title, scenarios, meas_val, meas_unc, meas_label, filename)
running_figure(title, log_mu, inv_a_MZ, betas_SM, betas_CD, log_MVL, log_MGUT, filename)
```

These create, populate, and save a complete figure. Use when the figure type is standard. Use individual primitives when custom layout is needed.

### C6. Landscape and Geometry Helpers

```python
log_landscape(ax, boundaries)                # Vertical scale diagram
concentric_shells(ax, shells)                # Nested boundary shells
```

---

## D. SCRIPT STRUCTURE

### D1. Standard Header

```python
#!/usr/bin/env python3
"""
HOWL {Paper} Diagrams — {Title}
{N} figures from platform library APIs.
Every value from phys24_lib + extension libraries.
Output: PNG files to ../figures/
"""

from data_5_diagram_lib import *
from phys24_lib import *
# ... additional imports as needed

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '..', 'figures'))
```

### D2. Per-Figure Block

```python
# ---- Fig N: TITLE ----
# Type: {D5 type from v1.0 rules}
# Shows: {what physics this communicates that text cannot}
# API calls: {which library functions produce the data}

fig, ax = dark_fig("Title", xlabel="...", ylabel="...")

# Get data from libraries
result = library_function(library_constant, ...)
prov("name", result, "library_function()")

# Plot using primitives
measurement_band(ax, measured_value, uncertainty, "label")
data_point(ax, x, y, "prediction", GREEN)
result_box(ax, x, y, "key finding")

ax.set_xlim(...)
ax.set_ylim(...)
save_fig(fig, "paper_NN_description.png")
```

### D3. Footer

```python
print_provenance()
print("=" * 70)
print("  {PAPER} DIAGRAMS COMPLETE — {N} figures")
print("=" * 70)
```

### D4. Lines Per Figure Target

| Complexity | Target | Example |
|---|---|---|
| Simple (bar chart, single curve) | 5-10 lines | α_s convergence bars |
| Medium (multi-curve, annotations) | 10-20 lines | Coupling running with thresholds |
| Complex (dual panel, many elements) | 20-30 lines | Structural parallel comparison |
| Composite (use composite helper) | 1-3 lines | `convergence_bar_figure(...)` |

With these targets, 40 figures in a single script is 400-800 lines — feasible for one prompt.

---

## E. FIGURE COUNT AND SELECTION

### E1. No Fixed Limit

The v1.0 rule "exactly 8 PNG figures per script" is relaxed. The diagram library makes additional figures cheap. A script may produce 8, 16, 24, or 40 figures depending on the paper's visual needs. The enumeration process (D14 from v1.0) scales accordingly: enumerate more candidates, select more winners.

### E2. The Coffee Table Test

For papers intended for a wide audience, apply the coffee table test: could someone learn the key findings by looking only at the figures with captions, without reading the body text? If yes, the figure set is complete. If not, add figures until the visual narrative is self-contained.

### E3. Minimum Type Diversity

At least 4 different diagram types (from D5 in v1.0) per 8 figures. For 16 figures, at least 5 types. For 24+, at least 6 types.

---

## F. STRUCTURAL UPGRADE PROTOCOL

### F1. No Removal, No Rename

The diagram library (data_5_diagram_lib.py) and all platform libraries follow the structural upgrade protocol:

- **Functions are never removed.** A deprecated function stays with a deprecation note.
- **Functions are never renamed.** If a better name is found, add an alias. The old name stays.
- **Parameters are never removed from function signatures.** New parameters are added with defaults.
- **Dict keys in data objects are never removed.** New keys are added.
- **Color names are never changed.** New colors are added alongside existing ones.

This ensures that every diagram script ever written continues to work after library upgrades. A script from Session 4 runs without modification in Session 10.

### F2. Version Tracking

The diagram library has a version string:

```python
DIAGRAM_LIB_VERSION = "2.0"  # data_5_diagram_lib.py
```

Diagram scripts do not need to check the version. The structural upgrade protocol guarantees backward compatibility.

### F3. New Helper Addition Process

When a new diagram pattern is identified (e.g., a new composite helper):

1. Write the helper in data_5_diagram_lib.py
2. Add a test case to the self-test
3. Use it in one diagram script to verify
4. Document it in this rules file under the appropriate section
5. The helper is now available to all future scripts

---

## G. COMPATIBILITY

### G1. Python 3.8+

All scripts and libraries are Python 3.8 compatible. No f-strings with `=`, no walrus operators in comprehensions, no `match` statements, no `%` formatting with positional-only parameters. Use `%` string formatting throughout.

### G2. Matplotlib Backend

Always `matplotlib.use('Agg')` before any plt import. This is handled by data_5_diagram_lib.py — the diagram script does not need to set it.

### G3. Human Runs All Scripts

All diagram scripts are written IN CHAT. The human copies, runs, and verifies. The provenance report is the verification — if it shows 0 hardcoded physics and all sources trace to library functions, the figures are trustworthy.

---

## H. INHERITED RULES (from v1.0)

The following v1.0 sections are inherited without change:

- **D4: What Diagrams Are For** — diagrams show curves, scales, geometry, comparisons, connections that text cannot
- **D5: Approved Diagram Types** — Types 1-8 unchanged
- **D6: Prohibited Diagram Types** — program flowcharts, text-in-boxes, verification ledgers still prohibited
- **D7.1-D7.4: Colors and fonts** — now defined in data_5_diagram_lib.py, same values
- **D7.5: Figure sizes** — unchanged, defaults in `dark_fig(size=(16, 10))`
- **D8: Spacing and Layout** — all spacing rules unchanged
- **D9: Chart-Specific Rules** — log scales, curves, scatter, shading rules unchanged
- **D10: Geometric Diagram Rules** — patches, nesting, paths, labels unchanged
- **D11: Naming Convention** — `{paper_short}_{nn}_{description}.png` unchanged
- **D13: Content Integrity** — now enforced by provenance system rather than manual review
- **D14: Enumeration Process** — scoring system unchanged, figure count relaxed (E1)
- **D15: Paper Integration** — placement tables and markdown unchanged
- **D16: Bounding Box Safety** — all elements inside axis limits, unchanged
- **D17: Lessons Learned** — all design lessons inherited

### What v1.0 Rules Are Superseded

| v1.0 Rule | Superseded By | Reason |
|---|---|---|
| D1.2 (exactly 8 figures) | E1 (no fixed limit) | Library makes more figures cheap |
| D2.2 (required imports) | A1 (library stack) | Imports are from libraries, not raw matplotlib |
| D2.4 (outdir setup) | `set_outdir()` in library | One-liner replaces boilerplate |
| D2.5 (savefig call) | `save_fig()` in library | One-liner replaces boilerplate |
| D7.2 (color definitions) | Library constants | Colors defined once in data_5_diagram_lib.py |
| D12.2 (global style block) | Library handles styling | `dark_fig()` does all styling |
| D12.4 (save pattern) | `save_fig()` | Library function |
| D13.1 (values from backing script) | B1-B3 (provenance rule) | Stronger: logged provenance, not just "from script" |

---

## I. QUICK REFERENCE

### Minimal 1-Figure Script

```python
from data_5_diagram_lib import *
from phys24_lib import *
set_outdir("../figures")

fig, ax = dark_fig("My Title", ylabel="Value")
val = f2m(alpha_s)
prov("alpha_s", alpha_s, "phys24_lib.alpha_s")
measurement_band(ax, alpha_s, Fraction(9, 10000), "$\\alpha_s$")
data_point(ax, 1, val, "prediction", GREEN)
ax.set_xlim(0, 2)
ax.set_ylim(0.11, 0.12)
save_fig(fig, "example_01_test.png")
print_provenance()
```

That is 12 lines for a complete, publication-quality, provenance-tracked figure.

### 8-Figure Script Template

```python
from data_5_diagram_lib import *
from phys24_lib import *
from data_4_derivation_lib import *
set_outdir("../figures")

# Fig 1
fig, ax = dark_fig("...")
# ... 10 lines ...
save_fig(fig, "paper_01_desc.png")

# Fig 2
fig, ax = dark_fig("...")
# ... 10 lines ...
save_fig(fig, "paper_02_desc.png")

# ... Figs 3-8 ...

print_provenance()
```

Approximately 100-160 lines for 8 figures. Compare to 600+ lines in v1.0.

---

*api_diagram_rules.md v2.0. Supersedes diagram_script_rules.md v1.0 (D1-D17) for all scripts using data_5_diagram_lib.py. No v1.0 rule is removed — they are inherited or superseded. The structural upgrade protocol ensures all scripts work across library versions. April 3, 2026.*

