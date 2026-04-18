#!/usr/bin/env python3
"""
HOWL Video 1 — Physics as Function Calls
3 figures showing the Standard Model as a call graph.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

BG      = '#0a0a12'
PAN     = '#12121f'
GOLD    = '#d4a843'
SILVER  = '#a0a8b8'
CYAN    = '#4ecdc4'
MAG     = '#c74b7a'
BLUE    = '#5b8def'
GREEN   = '#6bcf7f'
RED     = '#e05555'
ORANGE  = '#e8944a'
WHITE   = '#e8e8f0'
DIM     = '#555570'
PURPLE  = '#9b7bd4'

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)


def render_code(ax, title, lines, colors):
    """Render colored code lines on a dark axis.
    lines: list of strings (the code)
    colors: list of (line_index, start_col, end_col, color) tuples for highlighting.
    Everything not highlighted is rendered in DIM.
    """
    ax.set_facecolor(BG)
    ax.axis('off')

    ax.text(0.50, 0.98, title,
            transform=ax.transAxes, ha='center', va='top',
            fontsize=18, fontweight='bold', color=GOLD)

    n_lines = len(lines)
    line_height = 0.88 / max(n_lines, 1)
    y_top = 0.92

    # Build a color map: (line, col) -> color
    cmap = {}
    for li, c_start, c_end, color in colors:
        for c in range(c_start, c_end):
            cmap[(li, c)] = color

    for i, line in enumerate(lines):
        y = y_top - i * line_height
        # Render line number
        ax.text(0.03, y, '%2d' % (i + 1),
                transform=ax.transAxes, ha='right', va='top',
                fontsize=9, color=DIM, family='monospace')

        # Render each character or contiguous segment
        # Group by color for efficiency
        segments = []
        current_color = cmap.get((i, 0), DIM)
        current_start = 0
        for j in range(len(line)):
            char_color = cmap.get((i, j), DIM)
            if char_color != current_color:
                segments.append((current_start, j, current_color))
                current_color = char_color
                current_start = j
        segments.append((current_start, len(line), current_color))

        for seg_start, seg_end, seg_color in segments:
            # Calculate x position based on character offset
            # Monospace: each char ~ 0.0065 of axis width at fontsize 10
            x = 0.05 + seg_start * 0.0068
            text = line[seg_start:seg_end]
            ax.text(x, y, text,
                    transform=ax.transAxes, ha='left', va='top',
                    fontsize=10, color=seg_color, family='monospace')


def color_range(line_idx, text, full_line, color):
    """Helper: find text in full_line and return color tuple."""
    start = full_line.find(text)
    if start == -1:
        return None
    return (line_idx, start, start + len(text), color)


# ================================================================
# FIG 1: SIMPLE CALL GRAPH
# Type: Connection/Integer Map (D5.5)
# Shows: The basic dependency structure of physics as function calls.
# Vacuum calls gauge_setup, which spawns particles, which compose
# into atoms. The hierarchy IS the physics.
# ================================================================

lines_1 = [
    "main()                          // void - vacuum",
    "  |",
    "  +-- gauge_setup()             // GUT scale, CD level",
    "  |     |",
    "  |     +-- CD()                // long-lived thread, never returns",
    "  |     +-- strong()            // SU(3) setup",
    "  |     +-- weak()              // SU(2) setup",
    "  |     +-- higgs()             // called by CD and others",
    "  |           |                 // NOT main, it is a function",
    "  |           |                 // returns inertia scale",
    "  |           |",
    "  |           +-- quark()       // receives return value",
    "  |           +-- electron()    // receives return value",
    "  |           +-- nucleon()     // composite, from quark threads",
    "  |                 |",
    "  |                 +-- atom()  // composite, nucleon + electron",
]

colors_1 = []
for i, line in enumerate(lines_1):
    # Function names in cyan
    for fn in ['main()', 'gauge_setup()', 'CD()', 'strong()', 'weak()',
               'higgs()', 'quark()', 'electron()', 'nucleon()', 'atom()']:
        r = color_range(i, fn, line, CYAN)
        if r:
            colors_1.append(r)
    # Comments in green
    ci = line.find('//')
    if ci >= 0:
        colors_1.append((i, ci, len(line), GREEN))
    # Tree characters in dim (already default)

fig, ax = plt.subplots(figsize=(20, 12), facecolor=BG)
render_code(ax, 'Physics as a Function Call Graph: Basic Structure', lines_1, colors_1)
save(fig, 'vid1_fn_01_simple.png')


# ================================================================
# FIG 2: FORCE CARRIERS ADDED
# Type: Connection/Integer Map (D5.5)
# Shows: Strong and electroweak branches with force carriers.
# Lifetime expressed as return behavior: returns = short-lived,
# never returns = stable. Higgs returns vev=246GeV.
# ================================================================

lines_2 = [
    "main()                          // void - vacuum",
    "  |",
    "  +-- gauge_setup()             // GUT scale",
    "        |",
    "        +-- CD()                // long-lived, Dirac mass local",
    "        +-- strong()            // SU(3)",
    "        |     +-- gluon()       // long-lived, confined threads",
    "        |",
    "        +-- electroweak()       // SU(2) x U(1)",
    "              +-- higgs()       // symmetry breaking call",
    "                    |           // returns vev = 246 GeV",
    "                    |           // inertia begins here",
    "                    |",
    "                    +-- W+()    // short-lived, returns",
    "                    +-- W-()    // short-lived, returns",
    "                    +-- Z()     // short-lived, returns",
    "                    +-- photon()// massless, never returns",
    "                    |    +-- EM()  // persistent channel",
    "                    |",
    "                    +-- quark()    // long-lived, confined",
    "                    |    +-- nucleon()",
    "                    |          +-- atom()",
    "                    |",
    "                    +-- electron() // long-lived, never returns",
    "                          +-- atom()  // shares scope w/ nucleon",
]

colors_2 = []
for i, line in enumerate(lines_2):
    for fn in ['main()', 'gauge_setup()', 'CD()', 'strong()', 'gluon()',
               'electroweak()', 'higgs()', 'W+()', 'W-()', 'Z()',
               'photon()', 'EM()', 'quark()', 'nucleon()', 'atom()',
               'electron()']:
        r = color_range(i, fn, line, CYAN)
        if r:
            colors_2.append(r)
    # Highlight return behavior keywords
    for kw in ['never returns', 'short-lived, returns', 'long-lived',
               'persistent channel', 'confined', 'massless']:
        r = color_range(i, kw, line, ORANGE)
        if r:
            colors_2.append(r)
    # Highlight the vev
    r = color_range(i, 'vev = 246 GeV', line, GOLD)
    if r:
        colors_2.append(r)
    r = color_range(i, 'inertia begins here', line, GOLD)
    if r:
        colors_2.append(r)
    # Comments in green (but after keyword overrides)
    ci = line.find('//')
    if ci >= 0:
        # Only color comment chars that aren't already colored
        for j in range(ci, len(line)):
            if (i, j) not in dict(((c[0], c[1] + k), c[3])
                                   for c in colors_2
                                   for k in range(c[2] - c[1])):
                pass  # Will fall through to DIM

fig, ax = plt.subplots(figsize=(20, 16), facecolor=BG)
render_code(ax, 'Physics as Function Calls: Force Carriers and Lifetimes', lines_2, colors_2)
save(fig, 'vid1_fn_02_carriers.png')


# ================================================================
# FIG 3: FULL STANDARD MODEL
# Type: Connection/Integer Map (D5.5)
# Shows: Complete particle content with neutrinos, pions, hadrons.
# Kill test annotations, open questions marked explicitly.
# The viewer sees where the model is complete and where it is open.
# ================================================================

lines_3 = [
    "main()                              // void - vacuum",
    "  |",
    "  +-- gauge_setup()                 // GUT scale",
    "        |",
    "        +-- CD()                    // long-lived, Dirac mass local",
    "        |                           // precedes inertia",
    "        |                           // feeds electroweak() conditions",
    "        |                           // KILL: p -> e+ pi0 at 10^34 yr",
    "        |",
    "        +-- strong()                // SU(3)",
    "        |     +-- gluon()           // long-lived, confined threads",
    "        |           +-- pion()      // short-lived, returns",
    "        |           |               // pi0, pi+, pi-",
    "        |           |               // KILL channel: p -> e+ pi0",
    "        |           +-- hadron()    // composite patterns",
    "        |                 +-- nucleon()",
    "        |                       +-- proton()   // long-lived",
    "        |                       +-- neutron()   // long-lived",
    "        |",
    "        +-- electroweak()           // SU(2) x U(1)",
    "              +-- higgs()           // symmetry breaking call",
    "                    |               // returns vev = 246 GeV",
    "                    |               // inertia begins here",
    "                    |",
    "                    +-- W+()        // short-lived, returns",
    "                    +-- W-()        // short-lived, returns",
    "                    +-- Z()         // short-lived, returns",
    "                    +-- photon()    // massless, never returns",
    "                    |     +-- EM()  // persistent channel",
    "                    |",
    "                    +-- quark()     // long-lived, confined",
    "                    |     +-- nucleon()  // shares w/ strong()",
    "                    |           +-- atom()",
    "                    |",
    "                    +-- electron()  // long-lived, never returns",
    "                    |     +-- atom()     // shared scope",
    "                    |",
    "                    +-- neutrino()  // long-lived, near-massless",
    "                          +-- v_e()     // electron neutrino",
    "                          +-- v_u()     // muon neutrino",
    "                          +-- v_t()     // tau neutrino",
    "                          +-- oscillation()  // threads mix scope",
    "                                        // v_e <-> v_u <-> v_t",
    "                                        // mass mechanism OPEN",
    "                                        // seesaw? Majorana?",
    "                                        // not in RUM yet",
]

colors_3 = []
for i, line in enumerate(lines_3):
    # Function names
    for fn in ['main()', 'gauge_setup()', 'CD()', 'strong()', 'gluon()',
               'pion()', 'hadron()', 'nucleon()', 'proton()', 'neutron()',
               'electroweak()', 'higgs()', 'W+()', 'W-()', 'Z()',
               'photon()', 'EM()', 'quark()', 'atom()',
               'electron()', 'neutrino()', 'v_e()', 'v_u()', 'v_t()',
               'oscillation()']:
        r = color_range(i, fn, line, CYAN)
        if r:
            colors_3.append(r)
    # Kill tests in red
    for kw in ['KILL:', 'KILL channel:', 'p -> e+ pi0']:
        r = color_range(i, kw, line, RED)
        if r:
            colors_3.append(r)
    # Open questions in orange
    for kw in ['OPEN', 'seesaw? Majorana?', 'not in RUM yet']:
        r = color_range(i, kw, line, ORANGE)
        if r:
            colors_3.append(r)
    # Lifetime keywords in purple
    for kw in ['never returns', 'short-lived, returns', 'long-lived',
               'persistent channel', 'confined', 'massless', 'near-massless']:
        r = color_range(i, kw, line, PURPLE)
        if r:
            colors_3.append(r)
    # Key physics in gold
    for kw in ['vev = 246 GeV', 'inertia begins here', 'precedes inertia',
               'threads mix scope', 'Dirac mass local',
               'feeds electroweak() conditions']:
        r = color_range(i, kw, line, GOLD)
        if r:
            colors_3.append(r)
    # 10^34 in gold
    r = color_range(i, '10^34', line, GOLD)
    if r:
        colors_3.append(r)
    # Comments base color (will be overridden by above where applicable)
    ci = line.find('//')
    if ci >= 0:
        colors_3.append((i, ci, ci + 2, GREEN))

fig, ax = plt.subplots(figsize=(22, 22), facecolor=BG)
render_code(ax, 'The Standard Model as a Call Graph: Complete', lines_3, colors_3)

# Legend at bottom
legend_items = [
    ('Function names', CYAN),
    ('Lifetime / behavior', PURPLE),
    ('Key physics', GOLD),
    ('Kill tests', RED),
    ('Open questions', ORANGE),
    ('Comments', GREEN),
]
for j, (label, color) in enumerate(legend_items):
    x = 0.05 + j * 0.16
    ax.add_patch(mpatches.FancyBboxPatch(
        (x, 0.01), 0.012, 0.018,
        transform=ax.transAxes,
        boxstyle='round,pad=0.002',
        facecolor=color, edgecolor=color,
        alpha=0.7, clip_on=True))
    ax.text(x + 0.018, 0.019, label,
            transform=ax.transAxes, ha='left', va='center',
            fontsize=9, color=color)

save(fig, 'vid1_fn_03_full.png')

print("\n  All 3 function graph diagrams saved to %s" % outdir)
print("  vid1_fn_01_simple.png")
print("  vid1_fn_02_carriers.png")
print("  vid1_fn_03_full.png")
