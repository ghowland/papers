## HOWL Diagram Script Operational Rules

**Document:** diagram_script_rules.md
**Version:** 1.0
**Date:** April 3, 2026
**Scope:** All diagram-producing Python scripts in the HOWL series

---

### D1. DELIVERY

D1.1. All diagram scripts are written IN CHAT. Never as file attachments. The human must be able to read, verify, and run the script themselves.

D1.2. One script per paper. Each script produces exactly 8 PNG figures.

D1.3. The script is written AFTER the paper is complete. The human provides the finished paper, Claude enumerates 20 candidate diagrams, selects the top 8, and writes the script.

---

### D2. PYTHON SPEC

D2.1. Python 3.8 compatible. No f-strings with `=` (3.8 doesn't support), no walrus operator in comprehensions, no `match` statements.

D2.2. Required imports only:
```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os
```

D2.3. Optional imports from the paper's backing script and phys24_lib:
```python
from phys24_lib import *
```
Only when computed values from the library are needed in the figure. Do not import the library just to show you have it.

D2.4. Output directory: `../figures/` relative to the script location in `./code/`. The script creates the directory if it does not exist:
```python
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)
```

D2.5. Output format: PNG at 180 DPI with dark background, tight bounding box:
```python
fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
```

---

### D3. SELECTION PROCESS

D3.1. After the paper is written, enumerate 20 things from the paper that COULD be diagrammed.

D3.2. Filter each candidate: does it need a curve, a geometry, a scale, a nesting, or a spatial relationship? If the candidate is just a list of facts, a comparison of text items, or a program sequence, it belongs in a TABLE in the paper, not a PNG.

D3.3. Select the top 8 that span DIFFERENT diagram types. Do not produce 8 bar charts or 8 flowcharts. Use at least 4 different types from the approved list (D5).

D3.4. For each selected diagram, state in a comment what TYPE it is (from D5) and what PHYSICS it shows that the paper text cannot.

---

### D4. WHAT DIAGRAMS ARE FOR

D4.1. Diagrams exist to give humans spatial, geometric, and relational understanding that text cannot provide. A diagram earns its place when it shows a curve, a scale, a nesting, a convergence, a geometry, a threshold, or a region.

D4.2. A diagram must communicate something a table or paragraph CANNOT:
- The SHAPE of a curve (convergence, divergence, crossing)
- The SCALE of a hierarchy (orders of magnitude, log spacing)
- The GEOMETRY of a structure (nesting, cross-section, path)
- The RELATIVE SIZE of quantities (bars against a criterion)
- The CONNECTIONS between numbers across domains (with actual formulas)

D4.3. If the same information is equally clear as a sentence or a table row, it is NOT a diagram candidate.

---

### D5. APPROVED DIAGRAM TYPES

**Type 1: Running/Convergence Chart.** Curves showing how quantities evolve with energy, scale, distance, or parameter. X-axis is physical (energy, log(E/GeV), transit count). Y-axis is a measurable quantity (coupling, mass, correction factor). Shows crossing points, convergence, divergence, asymptotes. Examples: coupling unification, sin²θ_W evolution, α_s convergence.

**Type 2: Scale/Landscape Diagram.** Log-scale axis spanning many orders of magnitude with labeled landmarks. Shows WHERE things sit. The spacing communicates proximity and separation that numbers alone cannot. Examples: energy landscape from m_e to M_GUT, mass hierarchy, proton lifetime scale.

**Type 3: Threshold/Region Chart.** Curves with shaded regions showing where physics changes character. Labeled boundaries separate regimes. Shows: "above this line is excluded," "in this band is natural," "this region is fine-tuned." Examples: proton decay bounds, naturalness windows, experimental sensitivity bands.

**Type 4: Geometric Cross-Section.** Shows nesting, boundaries, shapes, paths through structure. Spheres inside tori inside spheres, light rays crossing boundaries, field configurations. Communicates structure that is impossible in prose. Examples: soliton nesting, galaxy crossing shells, field boundary topology.

**Type 5: Connection/Integer Map.** Shows how specific numbers link across physics domains. Contains actual Fractions and formulas, not program labels. Arrows carry mathematical meaning: "this integer appears in both this formula and that formula." Examples: 13 appearing in b₂' and in DM/baryon and in sin²θ_W.

**Type 6: Comparison Bar Chart.** Quantitative bars against a physical criterion. Shows elimination, ranking, or relative magnitude. Each bar carries a number. Threshold lines show pass/fail criteria. The eye sees immediately which candidates survive. Examples: gap ratio comparison, mass splitting requirements, coupling predictions vs measured.

**Type 7: Progression/Sequence Diagram.** Left-to-right showing sequential physical stages with data at each stage. Not a program flowchart — a physical sequence (light ray traversing boundaries, correction accumulating through stages, coupling evolving through thresholds). Each stage has computed values.

**Type 8: Identity Card.** ONE per paper maximum. A visual reference combining key data with a schematic of the main object. Contains quantum numbers, key Fractions, a geometric representation. Serves as a visual anchor for the paper. Not a box of text — includes actual geometry (representations, symmetry diagrams, particle content).

---

### D6. PROHIBITED DIAGRAM TYPES

D6.1. **Program flowcharts.** Boxes saying "PHYS-26 → PHYS-27 → PHYS-28" connected by arrows. This is a table of contents, not a diagram. The numbering already tells the sequence.

D6.2. **Survival/failure box lists.** Two columns of text items labeled "Survives" and "Disfavored" with colored borders. This is a table pretending to be a diagram. Use an actual table in the paper.

D6.3. **Verification ledgers.** Horizontal bars showing check counts (47/47, 11/11). This is metadata about scripts, not physics. It belongs in an appendix table.

D6.4. **Text-in-boxes.** Any diagram where the primary content is paragraphs of text inside rectangular boxes connected by arrows. If removing the boxes and arrows leaves readable prose, it was never a diagram.

D6.5. **Success/failure bar charts about scripts.** Bar charts showing how many tests passed. This is QA data. Readers care about what α_s equals, not how many checks confirmed it.

D6.6. **Generic motivational graphics.** Abstract shapes, decorative borders, or "artistic" representations that carry no quantitative data.

---

### D7. VISUAL STYLE

D7.1. **Background:** Dark (#0a0a12 or #12121f). All elements drawn on dark.

D7.2. **Color palette:** Consistent across all papers:
```python
BG      = '#0a0a12'
PAN     = '#12121f'
GOLD    = '#d4a843'   # Key results, highlights
SILVER  = '#a0a8b8'   # Secondary text, annotations
CYAN    = '#4ecdc4'   # Intermediate results, SU(2)
MAG     = '#c74b7a'   # Measured values, experimental
BLUE    = '#5b8def'   # U(1), theoretical curves
GREEN   = '#6bcf7f'   # Passing, natural, SU(3) low energy
RED     = '#e05555'   # Failures, excluded, boundaries
ORANGE  = '#e8944a'   # Thresholds, warnings, gates
WHITE   = '#e8e8f0'   # Primary text, labels
DIM     = '#555570'   # Subdued elements, grid lines
PURPLE  = '#9b7bd4'   # Cosmological, special quantities
```

D7.3. **Gauge group colors** (when showing coupling-specific data): Blue = U(1)/α₁, Green = SU(2)/α₂, Red = SU(3)/α₃. Consistent with the energy landscape convention.

D7.4. **Font sizes:**
- Figure title: 14–17pt, bold, GOLD or WHITE
- Axis labels: 11–12pt, SILVER
- Tick labels: 9–10pt, DIM
- Annotations and data labels: 9–10pt, color-matched to the element
- Small notes: 7–8pt, DIM or SILVER

D7.5. **Figure size:** Default (16, 10) for charts, (18, 12) for complex diagrams with many elements, (18, 8) for wide panoramic layouts. Never smaller than (14, 8).

---

### D8. SPACING AND LAYOUT

D8.1. **2× default margins.** Every element (box, label, annotation, legend, axis) must have visible breathing room from every other element. No overlapping text. No touching boxes. If in doubt, add more space.

D8.2. **Minimum gaps:**
- Between boxes in a diagram: at least 8% of the axis range
- Between text labels and the elements they label: at least 2% of axis range
- Between legend and plot area: at least 5% of figure width
- Between subplots: at least 15% of figure height

D8.3. **Axis padding:** `ax.set_xlim` and `ax.set_ylim` should extend at least 5% beyond the data range on each side. Data points should never touch the axis boundary.

D8.4. **Text never overlaps data.** If an annotation would overlap a curve or bar, offset it with an arrow (use `ax.annotate` with `arrowprops`).

D8.5. **Spine styling:** All spines set to DIM color, linewidth 0.5. For diagrams using `ax.axis('off')`, no spines.

---

### D9. CHART-SPECIFIC RULES

D9.1. **Log scales** whenever the physics spans more than 2 orders of magnitude. Label with physical landmarks (M_Z, M_VL, M_GUT, Λ_QCD) not just raw numbers.

D9.2. **Curves:** linewidth 2–2.5 for primary curves, 1–1.5 for secondary/reference. Dashed for theoretical/estimated, solid for computed/measured.

D9.3. **Scatter points:** size 150–250 for key data points. Edgecolor WHITE with linewidth 1.5–2 for emphasis on dark backgrounds.

D9.4. **Shaded regions:** alpha 0.05–0.15 for background regions. Never so dark they obscure curves or labels.

D9.5. **Horizontal/vertical reference lines:** linewidth 1–1.5, linestyle '--' or '-.', alpha 0.5–0.7. Labeled at the edge of the plot area.

D9.6. **Bar charts:** bars with alpha 0.6–0.8, edgecolor matching the fill at full opacity, linewidth 1.5–2. Numeric labels on each bar.

D9.7. **Legends:** facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize 9. Position: lower-right or upper-left, whichever avoids data.

---

### D10. GEOMETRIC DIAGRAM RULES

D10.1. For cross-sections and nesting diagrams, use `matplotlib.patches` (Circle, FancyBboxPatch, Wedge, Arc, Ellipse). Do not attempt 3D rendering.

D10.2. Nesting: larger structures drawn first (lower z-order), smaller structures on top. Alpha decreases with nesting level (outermost 0.3, innermost 0.7) to show depth.

D10.3. Paths (light rays, particle trajectories): draw as colored lines with arrows. Use `ax.annotate` for arrowheads or `ax.plot` with arrow markers.

D10.4. Labels for geometric features go OUTSIDE the feature with a thin leader line, not on top of the feature where they obscure the geometry.

D10.5. Physical scales noted on the diagram (e.g., "10^21 m" next to the halo, "10^13 m" next to the disk) so the reader can connect the geometry to physical reality.

---

### D11. NAMING CONVENTION

D11.1. File names: `{paper_short}_{nn}_{description}.png`

Examples:
```
phys28_01_bij_heatmap.png
phys28_02_coupling_running.png
phys28_03_delta_convergence.png
phys30_01_alpha_s_convergence.png
phys30_02_six_scenarios.png
```

D11.2. The nn index (01–08) matches the order in the script.

D11.3. The description is 2–4 words, lowercase, underscores, describing the PHYSICS content, not the diagram type.

---

### D12. SCRIPT STRUCTURE

D12.1. Standard header:
```python
#!/usr/bin/env python3
"""
HOWL PHYS-NN Diagrams — {paper_title}
{N} figures covering {brief description}.
Output: PNG files to ../figures/
"""
```

D12.2. Global style block with all colors and helper functions defined once at the top.

D12.3. Each figure in a clearly labeled section:
```python
# ================================================================
# FIG N: TITLE IN CAPS
# Type: {from D5 list}
# Shows: {what physics this communicates that text cannot}
# ================================================================
```

D12.4. Each figure block ends with `save(fig, filename)` and `print("  Saved: %s" % filename)`.

D12.5. Final summary block prints all 8 filenames.

---

### D13. CONTENT INTEGRITY

D13.1. All numerical values in diagrams must come from the backing script output or the phys24_lib. No hand-typed numbers that bypass the source of truth.

D13.2. If a value is computed in the diagram script (e.g., running a coupling), the computation must use the same formulas and conventions as the backing script.

D13.3. Annotations and labels must match the paper's terminology exactly. If the paper says "Delta" the diagram says "Delta", not "unification miss" or "gap."

D13.4. Measured values carry uncertainty bars or bands when shown alongside predictions. Do not plot a measured point without its error.

---

### D14. THE ENUMERATION PROCESS

D14.1. After receiving the completed paper, enumerate 20 diagram candidates. For each candidate, state:
- What it would show
- Which type from D5 it would use
- What physics it communicates that text cannot
- One sentence explaining why it earns a PNG slot

D14.2. Score each candidate:
- +2 if it shows a curve or geometric structure
- +2 if it shows something impossible to convey in text
- +1 if it shows quantitative comparison with data
- +1 if it connects quantities across different sections of the paper
- −2 if it is essentially a table rendered as an image
- −2 if it is a program flowchart or text-in-boxes
- −1 if a similar diagram already appears in a prior paper's atlas

D14.3. Select the top 8 by score. Enforce: at least 4 different types from D5. If the top 8 are all the same type, replace the lowest-scoring duplicates with the highest-scoring candidates of different types.

D14.4. Present the 8 selections to the human with one-line descriptions before writing the script. Wait for agreement. Then write the script in chat.

---

*End of diagram_script_rules.md. These rules govern all figure-producing scripts in the HOWL series. Every figure must show physics that text cannot. Every PNG must earn its slot.*

---

## Addendum D15: Paper Integration

**Added to:** diagram_script_rules.md
**Section:** D15

---

### D15. PAPER INTEGRATION

D15.1. After the diagram script is written, provide a **placement table** listing all 8 figures with:
- Figure number (Fig. 1–8)
- Filename
- Title (as it appears in the figure)
- Target section in the paper (by section number and name)
- The exact markdown to paste into that section

D15.2. The markdown uses relative path from the paper root directory (paper is in `./`, figures are in `./figures/`):

```markdown
![Fig. N: Title](./figures/physNN_0N_description.png)
```

D15.3. The placement table format:

```
| Fig | Filename | Title | Section | Markdown |
|-----|----------|-------|---------|----------|
| 1 | phys30_01_alpha_s_convergence.png | ... | §4 | `![Fig. 1: ...](./figures/phys30_01_...)` |
```

D15.4. Each markdown line includes the figure number and a short caption after the title, matching the paper's terminology:

```markdown
![Fig. 3: The VL b_ij Heatmap — Nine Fractions from one representation.](./figures/phys28_03_bij_heatmap.png)
```

D15.5. The caption in the markdown must be self-contained — a reader seeing only the figure and caption understands what is shown without reading the surrounding text.

D15.6. Figures are placed AFTER the first paragraph that references them in each section, not collected at the end.

---

*End of addendum D15. Every diagram has a home in the paper and a one-line paste command to put it there.*

---

### D16. BOUNDING BOX SAFETY

D16.1. Never place text or annotations outside the axis limits. The `bbox_inches='tight'` option expands the figure to include ALL drawn elements, including those beyond the axis range. Text at negative y-values or with `clip_on=False` and `transform=ax.get_xaxis_transform()` will balloon the output PNG to thousands of pixels of blank space.

D16.2. All annotations, labels, and result text must be placed INSIDE the axis limits using data coordinates. If a label needs to go below a chart, place it at the bottom of the y-range (e.g., `y = ylim_min + 0.05 * range`), not below the axis.

D16.3. Never use `transform=ax.get_xaxis_transform()` with negative y-values. This places elements in figure-fraction coordinates below the axis, which `tight` layout interprets as content requiring space.

---

