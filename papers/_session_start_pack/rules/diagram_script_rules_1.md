# HOWL Diagram Script Operational Rules

**Document:** diagram_script_rules.md
**Version:** 2.0
**Date:** April 4, 2026
**Scope:** All diagram-producing Python scripts in the HOWL series
**Supersedes:** v1.0 (April 3, 2026)

---

## D1. DELIVERY

D1.1. All diagram scripts are written IN CHAT. Never as file attachments.

D1.2. One script per paper. Exactly 8 PNG figures.

D1.3. Script is written AFTER the paper is complete. Process: human provides finished paper → Claude enumerates 20 candidates → scores and selects top 8 → presents selections for agreement → writes script.

---

## D2. PYTHON SPEC

D2.1. **Python 3.8 compatible.** No f-strings with `=`, no walrus operator, no `match` statements. Use `%` formatting or `.format()`.

D2.2. **Always import the diagram library:**
```python
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))
```

D2.3. **Use library helpers for all boilerplate.** The mapping:

| Task | Helper |
|------|--------|
| Figure with axes | `dark_fig(title, xlabel, ylabel, size)` |
| Freeform canvas | `dark_canvas(title, size)` |
| Dual panel | `dark_fig_dual(title_l, title_r, size, wspace)` |
| Save | `save_fig(fig, filename)` |
| Data point | `data_point(ax, x, y, label, color, size)` |
| Data point + error | `data_point_err(ax, x, y, yerr, label, color, size)` |
| Measured value | `measured_diamond(ax, x, y, label, color, size)` |
| Measurement band (H) | `measurement_band(ax, value, unc, label, color)` |
| Measurement band (V) | `measurement_band_v(ax, value, unc, label, color)` |
| Threshold line | `threshold_line(ax, x, label, color, vertical)` |
| Curve | `curve(ax, x, y, label, color, width, style, alpha)` |
| Shaded region (H) | `shaded_region_h(ax, y0, y1, color, alpha, label)` |
| Shaded region (V) | `shaded_region(ax, x0, x1, color, alpha, label)` |
| Result box | `result_box(ax, x, y, text, color, fontsize)` |
| Note | `note(ax, x, y, text, color, fontsize)` |
| Arrow annotation | `arrow_label(ax, x_data, y_data, x_text, y_text, text, color)` |
| Concentric shells | `concentric_shells(ax, shells, center)` |
| Bar chart | `bar_chart(ax, labels, values, colors, width)` |
| Running couplings | `running_curves(ax, log_mu, inv_alphas, labels, colors)` |
| Legend | `legend(ax, loc)` |
| Provenance | `prov(name, value, source)` |

D2.4. **Colors are provided by the library.** Never redefine BG, PAN, GOLD, SILVER, CYAN, MAG, BLUE, GREEN, RED, ORANGE, WHITE, DIM, PURPLE.

D2.5. **Manual matplotlib only for custom geometry** — radial gradients, orbit ellipses, circulation arrows, boundary walls. Everything else goes through the library.

---

## D3. PROHIBITED PATTERNS

D3.1. **Never use `transform=ax.transAxes` on `axvline`, `axhline`, or `axhspan`.** These generate their own transforms and raise `ValueError`.

D3.2. **Never use `transform=ax.get_xaxis_transform()` with negative y-values.** Causes PNG size explosion via `bbox_inches='tight'`.

D3.3. **Never place text or annotations outside axis limits.** All content must be inside `ax.set_xlim` / `ax.set_ylim` bounds.

D3.4. **Never set `clip_on=False`.** Defeats bounding box control.

D3.5. **For freeform geometric diagrams:** use `dark_canvas`, then immediately set `ax.set_xlim`, `ax.set_ylim`, and `ax.set_aspect('equal')` where needed. All drawing uses data coordinates within these bounds.

D3.6. **Never redefine library colors or manually style spines/ticks/grid.** The library handles all of this.

D3.7. **Never call `fig.savefig` directly.** Use `save_fig(fig, filename)`.

D3.8. **When indexing in a loop over dictionary keys, use the loop index `i`, not the key value.** `counts[i]` not `counts[s]`.

---

## D4. WHAT DIAGRAMS ARE FOR

D4.1. A diagram earns its place when it shows a curve, a scale, a nesting, a convergence, a geometry, a threshold, or a region that text cannot convey.

D4.2. A diagram must communicate something a table or paragraph CANNOT:
- The SHAPE of a curve (convergence, divergence, crossing)
- The SCALE of a hierarchy (orders of magnitude, log spacing)
- The GEOMETRY of a structure (nesting, cross-section, path)
- The RELATIVE SIZE of quantities (bars against a criterion)
- The CONNECTIONS between numbers across domains (with actual formulas)

D4.3. If the same information is equally clear as a sentence or a table row, it is NOT a diagram candidate.

D4.4. **The "could I get this from a table?" test is the primary filter.** If deleting the diagram and replacing it with two sentences loses nothing, it's not a diagram.

D4.5. **The best diagrams show a CURVE whose SHAPE is the finding.** Prioritize candidates where the shape carries meaning independent of the numbers.

D4.6. **Comparison diagrams earn their slot only when the comparison is VISUAL.** The reader must SEE which bars reach the band, or SEE the target sitting in the distribution. If all items are close together and you must read numbers anyway, it's a weak candidate.

D4.7. **Connection maps work only when they carry FORMULAS AND NUMBERS.** Each box must contain a specific Fraction or value. Arrows must mean "this number flows into this computation." Labels without numbers are flowcharts in disguise.

D4.8. **When in doubt between two candidates, pick the one with more data on it.**

---

## D5. PROHIBITED DIAGRAM TYPES

D5.1. **Program flowcharts.** Boxes saying "PHYS-26 → PHYS-27" connected by arrows.

D5.2. **Survival/failure box lists.** Two columns of text labeled "Survives" and "Disfavored."

D5.3. **Verification ledgers.** Bars showing check counts (47/47, 11/11).

D5.4. **Text-in-boxes.** If removing the boxes and arrows leaves readable prose, it was never a diagram.

D5.5. **Success/failure bar charts about scripts.** QA data belongs in appendix tables.

D5.6. **Generic motivational graphics.** Abstract shapes or decorative borders with no data.

---

## D6. COMMON DIAGRAM FORMS (Reference, Not Exhaustive)

These are forms that have worked well. They are a vocabulary, not a constraint. Any visual form that shows physics and passes the D4 filters is eligible. Novel forms not on this list are welcome if they earn their slot by score.

**Running/Convergence Chart.** Curves evolving with energy, scale, distance, or parameter. Shows crossing points, convergence, divergence, asymptotes.

**Scale/Landscape Diagram.** Log-scale axis spanning many orders of magnitude with labeled landmarks.

**Threshold/Region Chart.** Curves with shaded regions showing regime changes. Labeled boundaries separate physics.

**Geometric Cross-Section.** Nesting, boundaries, shapes, paths through structure. Uses `dark_canvas`.

**Connection/Integer Map.** Specific numbers linking across domains. Contains Fractions and formulas, not program labels.

**Comparison Bar Chart.** Quantitative bars against a physical criterion with threshold lines.

**Progression/Sequence Diagram.** Physical stages left-to-right with data at each stage. Not a program flowchart.

**Identity Card.** ONE per paper maximum. Visual anchor combining key data with geometry.

**Density/Distribution Histogram.** Powerful for "is this coincidence?" questions. Shows alternatives with targets marked.

**Phase/Parameter Space.** 2D space with regions, boundaries, and specific points marked. Shows where candidates sit relative to constraints.

---

## D7. SPACING AND LAYOUT

D7.1. **2× default margins on ALL text.** Every label, annotation, result box, and note must have visible breathing room from every other element and from geometry. No overlapping text. No touching boxes. If in doubt, add more space.

D7.2. **Minimum gaps:**
- Between annotation text and labeled element: at least 4% of axis range
- Between separate text labels: at least 6% of axis range vertically
- Between boxes in geometric diagrams: at least 10% of axis range
- Between legend and plot area: at least 5% of figure width
- Between subplots: `wspace=0.30` minimum

D7.3. **Axis padding:** Extend `xlim` and `ylim` at least 8% beyond data range on each side. Data points never touch axis boundary.

D7.4. **Text never overlaps data.** Offset labels and use `arrow_label` or `ax.annotate` with `arrowprops` to connect back.

D7.5. **Annotation arrows point FROM text TO data point.** `xytext` = label position (clear space), `xy` = data point.

D7.6. **For geometric diagrams:** place labels at edges or corners, connected to features by thin leader arrows. Never on top of geometry.

---

## D8. VISUAL STYLE

D8.1. Colors, background, and palette are defined by the library and must not be overridden.

D8.2. **Gauge group convention:** Blue = U(1)/α₁, Green = SU(2)/α₂, Red = SU(3)/α₃.

D8.3. **Font sizes:**
- Title: 14–17pt, bold, GOLD or WHITE
- Axis labels: 11–12pt, SILVER
- Tick labels: 9–10pt, DIM
- Annotations: 9–10pt, color-matched
- Small notes: 7–8pt, DIM or SILVER

D8.4. **Figure size:** Default (16, 10) for charts, (16, 14) or (18, 12) for complex geometric, (18, 8) or (18, 9) for wide/dual layouts. Never smaller than (14, 8).

---

## D9. CHART-SPECIFIC RULES

D9.1. **Log scales** whenever physics spans more than 2 orders of magnitude. Label with physical landmarks, not just numbers.

D9.2. **Curves:** Use `curve()`. Width 2.5 primary, 1.5 secondary. Dashed = theoretical, solid = computed/measured.

D9.3. **Scatter points:** Use `data_point()` or `data_point_err()`. Size 200–250. White edge automatic.

D9.4. **Shaded regions:** Use `shaded_region()` / `shaded_region_h()`. Alpha 0.03–0.08 large regions, 0.10–0.15 narrow bands. Test: can you read labels through the shading?

D9.5. **Measurement bands:** Use `measurement_band()`. Automatic 1σ and 3σ.

D9.6. **Distinct markers for computed vs measured.** Circles (`data_point`) = predictions, diamonds (`measured_diamond`) = measured values, dashed lines (`threshold_line`) = bounds.

D9.7. **Dual panels:** identical axis limits on both. `dark_fig_dual` with `wspace=0.30`.

D9.8. **Text boxes for results:** `result_box()`. Background matches BG, edgecolor draws attention.

---

## D10. GEOMETRIC DIAGRAM RULES

D10.1. Use `dark_canvas` for all geometric diagrams. Set `xlim`, `ylim`, `aspect` immediately.

D10.2. Use `matplotlib.patches` for shapes. No 3D rendering.

D10.3. Use `concentric_shells()` when possible. For custom nesting: larger first (lower z-order), alpha decreases outward.

D10.4. Paths as colored lines with arrows via `ax.annotate`.

D10.5. Physical scales noted on diagram to connect geometry to reality.

---

## D11. NAMING AND STRUCTURE

D11.1. Filenames: `{paper_short}_{nn}_{description}.png`. Example: `phys1_03_proton_radius_depth.png`.

D11.2. Index 01–08 matches script order.

D11.3. Header:
```python
#!/usr/bin/env python3
"""
HOWL PHYS-NN Diagrams — {paper_title}
8 figures covering {brief description}.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""
```

D11.4. Each figure section:
```python
# ================================================================
# FIG N: TITLE IN CAPS
# Type: {description of visual form}
# Shows: {what physics this communicates that text cannot}
# ================================================================
```

D11.5. Each block ends with `save_fig(fig, filename)`.

D11.6. Final summary prints all 8 filenames and placement table.

---

## D12. CONTENT INTEGRITY

D12.1. All values come from backing script output, phys24_lib, or paper appendices. Use `prov()` to log sources.

D12.2. Computations use the same formulas and conventions as backing scripts.

D12.3. Labels match paper terminology exactly.

D12.4. Measured values always carry uncertainty bars or bands.

---

## D13. THE TWO-STAGE SELECTION PROCESS

### Stage 1: Unconstrained Enumeration

D13.1. Enumerate 20 diagram candidates from the paper. For each state:
- What it would show
- What visual form it would take (any form, not restricted to D6)
- What physics it communicates that text cannot
- One sentence on why it earns a PNG slot

D13.2. Score each candidate independently of the D6 reference list:
- +2 if it shows a curve or geometric structure
- +2 if it shows something impossible to convey in text
- +1 if it shows quantitative comparison with data
- +1 if it connects quantities across different sections
- −2 if it is essentially a table rendered as an image
- −2 if it is a program flowchart or text-in-boxes (D5 prohibited)
- −1 if a similar diagram already exists in a prior paper's atlas

D13.3. A candidate that shows physics in a novel visual form not listed in D6 scores normally. The D6 list does not constrain enumeration — only the D5 prohibited list eliminates candidates by type.

### Stage 2: Selection and Diversity Check

D13.4. Sort all 20 candidates by score. Select the top 8.

D13.5. Check visual diversity: at least 4 different visual forms among the 8. If the top 8 are all the same form, swap the lowest-scoring duplicates for the highest-scoring candidates of different forms.

D13.6. Present the 8 selections to the human with one-line descriptions. Wait for agreement. Then write the script.

---

## D14. PAPER INTEGRATION

D14.1. After the script is written, provide a placement table:

```
| Fig | Filename | Title | Section | Markdown |
|-----|----------|-------|---------|----------|
| 1 | phys1_01_h0_transit.png | ... | §VI.1 | `![Fig. 1: ...](./figures/phys1_01_...)` |
```

D14.2. Markdown uses relative path `./figures/` from paper root.

D14.3. Captions are self-contained — a reader seeing only figure and caption understands what is shown.

D14.4. Figures placed AFTER the first paragraph that references them, not collected at the end.

---

## D15. LESSONS FROM PRACTICE

D15.1. **Side-by-side panels** need explicit `figsize` width. Use (18, 9) not (18, 10). Use `wspace=0.30` minimum.

D15.2. **Measurement bands** as two nested spans — 1σ (alpha 0.15) and 3σ (alpha 0.05). `measurement_band()` does this automatically.

D15.3. **Log scales need labeled landmarks.** M_Z, M_VL, M_GUT with vertical lines and text. Landmarks turn a number line into a map.

D15.4. **For scatter on dark backgrounds:** white edge mandatory. `data_point()` handles this automatically.

D15.5. **Shaded regions:** test alpha by checking if labels remain readable through the shading.

D15.6. **Density histograms** are powerful for "is this coincidence?" questions. Mark targets on the histogram. Dense region = expected. Sparse region = meaningful.

D15.7. **Cross-paper comparison diagrams** are strong when they reveal the SAME number arising from DIFFERENT mechanisms.

D15.8. **`transform=ax.transAxes` is forbidden on axis-bindable methods** (`axvline`, `axhline`, `axhspan`, `axvspan`). These generate their own transforms. Use data coordinates only.

---

*End of diagram_script_rules.md v2.0. Two-stage process: enumerate unconstrained, then select with diversity. Every PNG must show physics that text cannot. The library handles boilerplate. Manual code handles custom geometry only.*

---


## Addendum D16: Placement Table Is Mandatory Output

**Added to:** diagram_script_rules.md v2.0
**Section:** D16

---

### D16. PLACEMENT TABLE IS A REQUIRED DELIVERABLE

D16.1. The placement table is produced TWICE in the diagram workflow — once as part of the script output, and once as a separate formatted table delivered in chat immediately after the script.

D16.2. The in-chat placement table is the PRIMARY deliverable for the human. It contains everything needed to integrate figures into the paper without re-reading the script. The script's print block is a backup.

D16.3. **The placement table is NOT optional.** If the script is delivered without the placement table in chat, the deliverable is incomplete. Claude must produce both the script AND the table in the same response, or the table in the immediately following response if the script fills the response.

D16.4. The table has exactly 5 columns:

| Column | Content | Example |
|--------|---------|---------|
| Fig | Figure number 1–8 | 3 |
| Filename | Full filename with extension | math1_03_isomorphism_grid.png |
| Title | Title as rendered in the figure | The Isomorphism: Nine Domains, One Skeleton |
| Section | Target section number and name | §V.2 Nine Instances |
| Markdown | Complete paste-ready markdown line | `![Fig. 3: Caption.](./figures/math1_03_isomorphism_grid.png)` |

D16.5. **The Markdown column caption must be self-contained.** A reader seeing only the figure and caption understands what is shown without reading the paper. The caption is NOT the title — it is a one-sentence description of what the figure shows and why it matters.

D16.6. **Checklist before submitting:** Count the rows. There must be exactly 8. Count the columns. There must be exactly 5. Every Markdown entry must have the correct relative path `./figures/`. Every caption must be a complete sentence or phrase, not just the filename repeated.

---

*End of addendum D16. The placement table is a required deliverable, produced in chat alongside or immediately after the script. Eight rows, five columns, no exceptions.*

