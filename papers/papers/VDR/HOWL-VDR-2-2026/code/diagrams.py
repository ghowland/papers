

#!/usr/bin/env python3
"""
HOWL VDR-2-2026 Diagrams — VDR Gym: Exact Arithmetic Across Fifteen Domains
8 figures covering ODE comparison, chaos cost, dynamical divergence,
Picard iteration, computational geometry, cat map, probability, Farey.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os
from fractions import Fraction

# ================================================================
# GLOBAL STYLE
# ================================================================


# Light mode
if True:
    # ── Global palette (Kindle / light mode) ──
    BG      = '#ffffff'
    PAN     = '#f0ede8'
    GOLD    = '#a07820'
    SILVER  = '#505860'
    CYAN    = '#1a8a80'
    MAG     = '#a03058'
    BLUE    = '#2855a0'
    GREEN   = '#2a7a3a'
    RED     = '#b82020'
    ORANGE  = '#c06a18'
    WHITE   = '#1a1a22'
    DIM     = '#908e88'
    PURPLE  = '#6040a0'
else:
    # ── Global palette (D7.2) ──
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
    
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

def style_ax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor(PAN)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=14)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11, labelpad=8)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11, labelpad=8)
    ax.tick_params(colors=DIM, labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)

# ================================================================
# FIG 1: EULER VS RK4 ERROR COMPARISON
# Type: Convergence chart (Type 1)
# Shows: Two error curves with different slopes — the SHAPE reveals
#   method order. Euler O(h), RK4 O(h^4). Both exact VDR at each step.
# ================================================================

import math

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, 'Exact ODE Solvers: Euler vs RK4 for dy/dx = y',
         'Step size h', 'Absolute error at x = 1 vs e')

step_sizes = [Fraction(1, n) for n in [2, 4, 5, 8, 10, 16, 20, 25, 40, 50, 100]]
euler_errors = []
rk4_errors = []

for h in step_sizes:
    n_steps = int(1 / h)
    # Euler: y(1) = (1+h)^n
    y_euler = (1 + h) ** n_steps
    euler_errors.append(abs(float(y_euler) - math.e))

    # RK4: each step exact rational
    y = Fraction(1)
    x = Fraction(0)
    for _ in range(n_steps):
        k1 = y
        k2 = y + h * k1 / 2
        k3 = y + h * k2 / 2
        k4 = y + h * k3
        y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x = x + h
    rk4_errors.append(abs(float(y) - math.e))

h_floats = [float(h) for h in step_sizes]

ax.loglog(h_floats, euler_errors, 'o-', color=RED, linewidth=2.5,
          markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
          label='Euler method — O(h)', zorder=5)

ax.loglog(h_floats, rk4_errors, 's-', color=CYAN, linewidth=2.5,
          markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
          label='RK4 method — O(h' + r'$^4$' + ')', zorder=5)

# reference slopes
h_ref = np.array([0.02, 0.5])
ax.loglog(h_ref, 0.5 * h_ref, '--', color=RED, linewidth=1, alpha=0.4,
          label='slope 1 reference')
ax.loglog(h_ref, 2.0 * h_ref ** 4, '--', color=CYAN, linewidth=1, alpha=0.4,
          label='slope 4 reference')

ax.set_xlim(0.008, 0.7)
ax.set_ylim(min(rk4_errors) * 0.3, max(euler_errors) * 3)

ax.text(0.015, min(rk4_errors) * 1.5,
        'Both methods compute exact VDR rationals at every step.\n'
        'The error is from discretization, not from arithmetic.',
        color=GREEN, fontsize=10, ha='left', va='bottom',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.8))

legend = ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=10, framealpha=0.9)

save(fig, 'vdr2_01_euler_vs_rk4.png')

# ================================================================
# FIG 2: DENOMINATOR EXPLOSION IN CHAOTIC ITERATION
# Type: Convergence/scale chart (Type 1)
# Shows: Exponential growth of fraction size under logistic map r=4.
#   The SHAPE — straight line on log scale — proves exponential cost.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, 'The Cost of Exact Chaos: Denominator Growth in Logistic Map r=4',
         'Iteration Step', 'Denominator Digit Count (log scale)')

# compute denominator digit counts for logistic r=4, x0=1/3
x = Fraction(1, 3)
steps_chaos = list(range(16))
denom_digits = [len(str(x.denominator))]

for i in range(15):
    x = 4 * x * (1 - x)
    denom_digits.append(len(str(x.denominator)))

ax.semilogy(steps_chaos, denom_digits, 'o-', color=MAG, linewidth=2.5,
            markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='logistic r=4, x' + r'$_0$' + ' = 1/3', zorder=5)

# reference: 2^n growth
ref_steps = np.linspace(0, 15, 50)
ref_growth = 1.0 * 2.0 ** ref_steps
ax.semilogy(ref_steps, ref_growth, '--', color=GOLD, linewidth=1.5, alpha=0.6,
            label=r'$2^n$ reference (Lyapunov exponent = ln 2)')

# annotations
for i in [0, 5, 10, 15]:
    if i < len(denom_digits):
        ax.annotate('%d digits' % denom_digits[i],
                    xy=(i, denom_digits[i]),
                    xytext=(i + 0.5, denom_digits[i] * 2.5),
                    color=SILVER, fontsize=9,
                    arrowprops=dict(arrowstyle='->', color=SILVER, linewidth=1))

ax.set_xlim(-0.5, 16)
ax.set_ylim(0.5, max(denom_digits) * 5)

# tent map comparison
tent_digits = [1] * 16  # tent map on 1/7: denominator stays 7 (1 digit)
ax.semilogy(steps_chaos, tent_digits, 'D-', color=GREEN, linewidth=2,
            markersize=8, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='tent map on 1/7 (period 3, constant)', zorder=5)

ax.text(8, 0.8, 'Periodic orbits: zero growth, zero cost',
        color=GREEN, fontsize=10, ha='center', fontstyle='italic')

ax.text(8, max(denom_digits) * 2,
        'Chaotic orbits: exponential representation cost.\n'
        'Float hides this by truncating. VDR exposes it honestly.',
        color=ORANGE, fontsize=10, ha='center', va='bottom',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, alpha=0.8))

legend = ax.legend(loc='center left', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=10, framealpha=0.9)

save(fig, 'vdr2_02_denominator_explosion.png')

# ================================================================
# FIG 3: TENT MAP — VDR VS FLOAT DIVERGENCE
# Type: Convergence/divergence chart (Type 1)
# Shows: Float orbit drifting from exact VDR orbit. The SHAPE of
#   the divergence curve shows when float becomes unreliable.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.30})

# Left: both orbits
n_tent = 35
x_vdr_vals = []
x_float_vals = []

x_v = Fraction(1, 7)
x_f = 1.0 / 7.0

x_vdr_vals.append(float(x_v))
x_float_vals.append(x_f)

for i in range(n_tent):
    if x_v < Fraction(1, 2):
        x_v = 2 * x_v
    else:
        x_v = 2 * (1 - x_v)
    if x_f < 0.5:
        x_f = 2.0 * x_f
    else:
        x_f = 2.0 * (1.0 - x_f)
    x_vdr_vals.append(float(x_v))
    x_float_vals.append(x_f)

steps_tent = list(range(n_tent + 1))

style_ax(ax1, 'Tent Map Orbits: VDR vs Float',
         'Step', 'x value')

ax1.plot(steps_tent, x_vdr_vals, 'o-', color=GREEN, linewidth=1.5,
         markersize=5, markeredgecolor=WHITE, markeredgewidth=1,
         label='VDR (exact)', zorder=5, alpha=0.8)
ax1.plot(steps_tent, x_float_vals, 's-', color=RED, linewidth=1.5,
         markersize=5, markeredgecolor=WHITE, markeredgewidth=1,
         label='float64', zorder=4, alpha=0.8)

ax1.set_xlim(-1, n_tent + 1)
ax1.set_ylim(-0.05, 1.05)
ax1.legend(loc='lower left', facecolor=PAN, edgecolor=DIM,
           labelcolor=WHITE, fontsize=9)

# Right: divergence
diffs = [abs(v - f) for v, f in zip(x_vdr_vals, x_float_vals)]
# replace zeros with tiny value for log
diffs_plot = [max(d, 1e-18) for d in diffs]

style_ax(ax2, 'Float Divergence from Exact',
         'Step', '|VDR - float|')

ax2.semilogy(steps_tent, diffs_plot, 'o-', color=ORANGE, linewidth=2.5,
             markersize=8, markeredgecolor=WHITE, markeredgewidth=1.5,
             zorder=5)

# find where divergence exceeds 0.01
diverge_step = None
for i, d in enumerate(diffs):
    if d > 0.01:
        diverge_step = i
        break

if diverge_step:
    ax2.axvline(x=diverge_step, color=RED, linestyle='--', linewidth=1.5, alpha=0.6)
    ax2.text(diverge_step + 0.5, 1e-1, 'float\nunreliable\nhere',
             color=RED, fontsize=10, va='center')

ax2.axhline(y=1e-15, color=DIM, linestyle=':', linewidth=1, alpha=0.5)
ax2.text(1, 2e-15, 'machine epsilon', color=DIM, fontsize=8)

ax2.set_xlim(-1, n_tent + 1)
ax2.set_ylim(1e-18, 10)

ax2.text(n_tent * 0.5, 1e-16,
         'VDR stays exact forever.\nFloat loses track after ~25 steps.',
         color=GREEN, fontsize=10, ha='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.8))

save(fig, 'vdr2_03_tent_map_divergence.png')

# ================================================================
# FIG 4: PICARD ITERATION CONVERGENCE TO e
# Type: Convergence chart (Type 1)
# Shows: Error dropping as Picard iterations accumulate Taylor terms.
#   The SHAPE shows factorial convergence rate.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.30})

# compute Picard iterations for dy/dx = y
picard_sums = []
factorial = 1
total = Fraction(0)
for k in range(12):
    if k > 0:
        factorial *= k
    total += Fraction(1, factorial)
    picard_sums.append(total)

picard_errors = [abs(float(s) - math.e) for s in picard_sums]
picard_steps = list(range(12))

# Left: partial sums approaching e
style_ax(ax1, 'Picard Iteration: Partial Sums Approaching e',
         'Iteration (Taylor terms)', 'Partial sum value')

ax1.plot(picard_steps, [float(s) for s in picard_sums], 'o-', color=CYAN,
         linewidth=2.5, markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
         label='VDR partial sum', zorder=5)

ax1.axhline(y=math.e, color=GOLD, linestyle='--', linewidth=1.5, alpha=0.7)
ax1.text(11.5, math.e + 0.02, 'e = 2.71828...',
         color=GOLD, fontsize=10, ha='right', va='bottom')

# label some fractions
for i in [1, 3, 5, 8]:
    f = picard_sums[i]
    ax1.annotate('%s' % str(f) if len(str(f)) < 15 else '%.6f' % float(f),
                 xy=(i, float(f)),
                 xytext=(i + 0.4, float(f) - 0.15),
                 color=SILVER, fontsize=8,
                 arrowprops=dict(arrowstyle='->', color=SILVER, linewidth=1))

ax1.set_xlim(-0.5, 12)
ax1.set_ylim(0.5, 3.0)
ax1.legend(loc='lower right', facecolor=PAN, edgecolor=DIM,
           labelcolor=WHITE, fontsize=9)

# Right: error on log scale
style_ax(ax2, 'Error: |partial sum - e|',
         'Iteration', 'Absolute error')

ax2.semilogy(picard_steps, picard_errors, 's-', color=MAG, linewidth=2.5,
             markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
             zorder=5)

# reference: 1/k!
ref_factorial_errors = []
fact = 1
for k in range(12):
    if k > 0:
        fact *= k
    ref_factorial_errors.append(1.0 / fact if fact > 0 else 1.0)

ax2.semilogy(picard_steps, ref_factorial_errors, '--', color=GOLD,
             linewidth=1.5, alpha=0.5, label='1/k! reference')

ax2.set_xlim(-0.5, 12)
ax2.set_ylim(min(picard_errors) * 0.3, max(picard_errors) * 3)

ax2.text(6, picard_errors[4] * 0.3,
         'Every partial sum is an exact\nVDR rational: no float at any step.',
         color=GREEN, fontsize=10, ha='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.8))

ax2.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
           labelcolor=WHITE, fontsize=9)

save(fig, 'vdr2_04_picard_convergence.png')

# ================================================================
# FIG 5: BARYCENTRIC COORDINATES — EXACT GEOMETRY
# Type: Geometric diagram (Type 4)
# Shows: Triangle with exact rational barycentric coordinates at
#   specific points. The GEOMETRY shows spatial relationships that
#   numbers alone cannot convey.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12), facecolor=BG)
style_ax(ax, 'Exact Barycentric Coordinates in VDR', '', '')
ax.set_facecolor(PAN)

# triangle vertices
A = np.array([1.0, 1.0])
B = np.array([14.0, 1.0])
C = np.array([4.0, 12.0])

# draw triangle
tri = plt.Polygon([A, B, C], fill=True, facecolor=PAN, edgecolor=CYAN,
                  linewidth=2.5, zorder=2)
ax.add_patch(tri)

# fill with very light color
tri_fill = plt.Polygon([A, B, C], fill=True, facecolor=CYAN, alpha=0.04, zorder=1)
ax.add_patch(tri_fill)

# vertex labels
offset = 0.6
ax.text(A[0] - offset, A[1] - offset, 'A (0,0)', color=WHITE, fontsize=12,
        fontweight='bold', ha='center', va='top')
ax.text(B[0] + offset, B[1] - offset, 'B (6,0)', color=WHITE, fontsize=12,
        fontweight='bold', ha='center', va='top')
ax.text(C[0] - offset, C[1] + offset, 'C (0,6)', color=WHITE, fontsize=12,
        fontweight='bold', ha='center', va='bottom')

# points with exact barycentric coordinates
# using triangle (0,0),(6,0),(0,6) mapped to display coords
def bary_to_display(u, v, w):
    # barycentric to Cartesian in our display triangle
    return u * A + v * B + w * C

points = [
    ('Centroid', 1.0/3, 1.0/3, 1.0/3, r'$(\frac{1}{3}, \frac{1}{3}, \frac{1}{3})$', GOLD),
    ('Vertex A', 1.0, 0.0, 0.0, '(1, 0, 0)', CYAN),
    ('Vertex B', 0.0, 1.0, 0.0, '(0, 1, 0)', CYAN),
    ('Vertex C', 0.0, 0.0, 1.0, '(0, 0, 1)', CYAN),
    ('Mid BC', 0.0, 0.5, 0.5, r'$(0, \frac{1}{2}, \frac{1}{2})$', GREEN),
    ('Mid AC', 0.5, 0.0, 0.5, r'$(\ \frac{1}{2}, 0, \frac{1}{2})$', GREEN),
    ('Mid AB', 0.5, 0.5, 0.0, r'$(\frac{1}{2}, \frac{1}{2}, 0)$', GREEN),
    (r'$\frac{1}{4}$ point', 0.5, 0.25, 0.25, r'$(\frac{1}{2}, \frac{1}{4}, \frac{1}{4})$', PURPLE),
]

for name, u, v, w, bary_str, color in points:
    pos = bary_to_display(u, v, w)

    ax.scatter([pos[0]], [pos[1]], s=200, color=color, edgecolors=WHITE,
               linewidth=2, zorder=10)

    # text offset to avoid overlap
    tx, ty = pos[0], pos[1]
    if name == 'Centroid':
        tx += 1.8
        ty += 0.5
    elif name == 'Vertex A':
        tx -= 0.5
        ty += 1.0
    elif name == 'Vertex B':
        tx += 0.5
        ty += 1.0
    elif name == 'Vertex C':
        tx += 1.5
        ty -= 0.5
    elif 'Mid BC' in name:
        tx += 1.8
        ty += 0.3
    elif 'Mid AC' in name:
        tx -= 2.0
        ty += 0.3
    elif 'Mid AB' in name:
        tx += 0.5
        ty -= 1.0
    else:
        tx -= 2.5
        ty += 0.3

    ax.annotate('%s\n%s' % (name, bary_str),
                xy=(pos[0], pos[1]),
                xytext=(tx, ty),
                color=color, fontsize=10, ha='center', va='center',
                arrowprops=dict(arrowstyle='->', color=color, linewidth=1.2),
                zorder=11,
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color,
                          alpha=0.85))

# medians (to centroid)
centroid = bary_to_display(1.0/3, 1.0/3, 1.0/3)
for vertex in [A, B, C]:
    ax.plot([vertex[0], centroid[0]], [vertex[1], centroid[1]],
            '--', color=DIM, linewidth=1, alpha=0.4, zorder=3)

ax.text(7.5, -0.8,
        'Every coordinate is an exact VDR rational.\n'
        'Point-in-triangle tests are exact — no epsilon tolerance needed.',
        color=SILVER, fontsize=11, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, alpha=0.8))

ax.set_xlim(-1.5, 16.5)
ax.set_ylim(-2.0, 14.0)
ax.set_aspect('equal')
ax.axis('off')

save(fig, 'vdr2_05_barycentric_exact.png')

# ================================================================
# FIG 6: ARNOLD CAT MAP — EXACT ORBIT ON TORUS
# Type: Geometric diagram (Type 4)
# Shows: 40 exact rational points on the unit square forming a
#   complete orbit. The GEOMETRY of the orbit is impossible to
#   convey without plotting the points.
# ================================================================

fig, ax = plt.subplots(figsize=(14, 14), facecolor=BG)
style_ax(ax, 'Arnold Cat Map: Exact Period-40 Orbit on Rational Torus', '', '')
ax.set_facecolor(PAN)

# compute orbit
x_cat = Fraction(1, 7)
y_cat = Fraction(3, 11)
orbit_x = [float(x_cat)]
orbit_y = [float(y_cat)]

for i in range(39):
    new_x = (2 * x_cat + y_cat)
    new_y = (x_cat + y_cat)
    x_cat = new_x - int(new_x)
    y_cat = new_y - int(new_y)
    if x_cat < 0:
        x_cat += 1
    if y_cat < 0:
        y_cat += 1
    orbit_x.append(float(x_cat))
    orbit_y.append(float(y_cat))

# draw unit square
square = plt.Polygon([(0, 0), (1, 0), (1, 1), (0, 1)], fill=False,
                     edgecolor=DIM, linewidth=2, zorder=2)
ax.add_patch(square)
square_fill = plt.Polygon([(0, 0), (1, 0), (1, 1), (0, 1)], fill=True,
                          facecolor=PAN, alpha=0.5, zorder=1)
ax.add_patch(square_fill)

# plot orbit points with color gradient showing time
colors_cat = plt.cm.plasma(np.linspace(0.1, 0.9, 40))

for i in range(40):
    ax.scatter([orbit_x[i]], [orbit_y[i]], s=120, color=colors_cat[i],
               edgecolors=WHITE, linewidth=1.5, zorder=10)

# connect consecutive points
for i in range(39):
    ax.plot([orbit_x[i], orbit_x[i+1]], [orbit_y[i], orbit_y[i+1]],
            '-', color=DIM, linewidth=0.5, alpha=0.3, zorder=3)

# mark start
ax.scatter([orbit_x[0]], [orbit_y[0]], s=300, color=GREEN,
           edgecolors=WHITE, linewidth=2.5, zorder=11, marker='*')
ax.annotate('start\n(1/7, 3/11)',
            xy=(orbit_x[0], orbit_y[0]),
            xytext=(orbit_x[0] + 0.08, orbit_y[0] + 0.08),
            color=GREEN, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, linewidth=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN, alpha=0.85))

# info box
ax.text(0.5, -0.12,
        'Matrix: [[2,1],[1,1]] mod 1    Period: exactly 40\n'
        'All 40 points are exact rationals with denominator dividing lcm(7,11) = 77\n'
        'Float cannot reliably detect this period due to modular reduction error',
        color=SILVER, fontsize=10, ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, alpha=0.8))

# colorbar-like time indicator
for i in range(40):
    ax.plot([0.02 + i * 0.024, 0.02 + i * 0.024], [-0.04, -0.02],
            '-', color=colors_cat[i], linewidth=3)
ax.text(0.02, -0.06, 'step 0', color=DIM, fontsize=7, ha='left')
ax.text(0.02 + 39 * 0.024, -0.06, 'step 39', color=DIM, fontsize=7, ha='right')
ax.text(0.5, -0.06, 'time', color=DIM, fontsize=8, ha='center')

ax.set_xlim(-0.08, 1.08)
ax.set_ylim(-0.18, 1.08)
ax.set_aspect('equal')
ax.axis('off')

save(fig, 'vdr2_06_arnold_cat_orbit.png')

# ================================================================
# FIG 7: BINOMIAL PMF — EXACT PROBABILITY DISTRIBUTION
# Type: Comparison bar chart (Type 6)
# Shows: B(10, 1/3) with exact rational probabilities. The SHAPE of
#   the distribution is visible. Every bar carries an exact fraction.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, 'Exact Binomial Distribution: B(10, 1/3)',
         'k', 'P(X = k)')

n_binom = 10
p_binom = Fraction(1, 3)
q_binom = 1 - p_binom

pmf = []
for k in range(n_binom + 1):
    # C(n,k) * p^k * q^(n-k)
    coeff = 1
    for i in range(min(k, n_binom - k)):
        coeff = coeff * (n_binom - i) // (i + 1)
    prob = Fraction(coeff) * p_binom ** k * q_binom ** (n_binom - k)
    pmf.append(prob)

ks = list(range(n_binom + 1))
pmf_float = [float(p) for p in pmf]

bars = ax.bar(ks, pmf_float, color=BLUE, alpha=0.7, edgecolor=BLUE,
              linewidth=1.5, width=0.7, zorder=3)

# label each bar with exact fraction
for k, prob in enumerate(pmf):
    y_pos = float(prob) + 0.005
    # shorten fraction display
    frac_str = '%d/%d' % (prob.numerator, prob.denominator)
    if len(frac_str) > 15:
        frac_str = '%.5f' % float(prob)
    ax.text(k, y_pos, frac_str, color=WHITE, fontsize=8,
            ha='center', va='bottom', rotation=45)

# expected value line
ev = float(n_binom * p_binom)
ax.axvline(x=ev, color=GOLD, linestyle='--', linewidth=2, alpha=0.7)
ax.text(ev + 0.15, max(pmf_float) * 0.95,
        r'E[X] = $\frac{10}{3}$ = 3.33...',
        color=GOLD, fontsize=11, va='top')

# sum verification
ax.text(8.5, max(pmf_float) * 0.7,
        r'$\sum$ P(X=k) = $\frac{59049}{59049}$ = 1 exactly',
        color=GREEN, fontsize=12, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.8))

ax.set_xlim(-0.8, 11.3)
ax.set_ylim(0, max(pmf_float) * 1.25)
ax.set_xticks(ks)

save(fig, 'vdr2_07_binomial_pmf.png')

# ================================================================
# FIG 8: FAREY SEQUENCE F5 — EXACT RATIONALS ON THE NUMBER LINE
# Type: Scale/landscape diagram (Type 2)
# Shows: The SPACING of Farey fractions. Equal denominators cluster.
#   The visual spacing reveals mediant structure text cannot show.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8), facecolor=BG)
style_ax(ax, r'Farey Sequence $F_5$: Exact Rationals on [0, 1]', '', '')
ax.set_facecolor(PAN)

# generate F5
from math import gcd as mgcd
farey = []
for q in range(1, 6):
    for p in range(0, q + 1):
        if mgcd(p, q) == 1:
            farey.append(Fraction(p, q))
farey.sort()

# draw number line
y_line = 4.0
ax.plot([0, 1], [y_line, y_line], '-', color=DIM, linewidth=2, zorder=2)

# color by denominator
denom_colors = {1: WHITE, 2: CYAN, 3: GREEN, 4: BLUE, 5: MAG}

# plot fractions
for i, f in enumerate(farey):
    x = float(f)
    d = f.denominator
    color = denom_colors.get(d, SILVER)
    height = 0.6 + (6 - d) * 0.25  # taller ticks for smaller denominators

    # tick mark
    ax.plot([x, x], [y_line - height * 0.3, y_line + height * 0.3],
            '-', color=color, linewidth=2.5, zorder=5)

    # dot
    ax.scatter([x], [y_line], s=100, color=color, edgecolors=WHITE,
               linewidth=1.5, zorder=10)

    # fraction label — stagger vertically to avoid overlap
    if d <= 2:
        y_label = y_line + 1.2
    elif d == 3:
        y_label = y_line - 1.2
    elif d == 4:
        y_label = y_line + 1.8
    else:
        y_label = y_line - 1.8

    frac_str = '%d/%d' % (f.numerator, f.denominator)
    if f == 0:
        frac_str = '0'
    elif f == 1:
        frac_str = '1'

    ax.text(x, y_label, frac_str, color=color, fontsize=11,
            ha='center', va='center', fontweight='bold')

# legend for denominator colors
legend_y = 7.5
legend_items = [(1, WHITE, 'd=1'), (2, CYAN, 'd=2'), (3, GREEN, 'd=3'),
                (4, BLUE, 'd=4'), (5, MAG, 'd=5')]
for i, (d, color, label) in enumerate(legend_items):
    x_leg = 0.1 + i * 0.2
    ax.scatter([x_leg], [legend_y], s=80, color=color, edgecolors=WHITE,
               linewidth=1, zorder=10)
    ax.text(x_leg + 0.03, legend_y, '  ' + label, color=color, fontsize=10,
            va='center')

# mediant property annotation
ax.text(0.5, 1.2,
        r'For every consecutive pair $\frac{a}{b}, \frac{c}{d}$: '
        r'$|ad - bc| = 1$ exactly.'
        '\n11 fractions. Every position is an exact VDR rational.',
        color=SILVER, fontsize=11, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, alpha=0.8))

ax.set_xlim(-0.08, 1.08)
ax.set_ylim(0.2, 8.5)
ax.axis('off')

save(fig, 'vdr2_08_farey_sequence.png')

# ================================================================
# SUMMARY
# ================================================================
print("\nAll figures saved:")
print("  vdr2_01_euler_vs_rk4.png")
print("  vdr2_02_denominator_explosion.png")
print("  vdr2_03_tent_map_divergence.png")
print("  vdr2_04_picard_convergence.png")
print("  vdr2_05_barycentric_exact.png")
print("  vdr2_06_arnold_cat_orbit.png")
print("  vdr2_07_binomial_pmf.png")
print("  vdr2_08_farey_sequence.png")
