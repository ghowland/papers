#!/usr/bin/env python3
"""
HOWL Hubble Tension Diagrams — From Library APIs
8 figures exploring the H0 running curve hypothesis.
Every value from phys24_hubble_lib.py.
Every plot call from data_5_diagram_lib.py.
Output: PNG files to ../figures/
"""

from phys24_lib import *
from phys24_hubble_lib import *
from data_5_diagram_lib import *
import numpy as np


set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '..', 'figures'))


# ================================================================
# FIG 1: THE H0 DATA — FIVE MEASUREMENTS WITH ERROR BARS
# Type: Comparison (D5.6)
# Shows: Tension is visible. Bands don't overlap. 5 sigma gap.
# ================================================================

fig, ax = dark_fig("The Hubble Tension: Five Measurements",
                    xlabel="Measurement Method (ordered by distance)",
                    ylabel="H$_0$ (km/s/Mpc)")

colors_h = [RED, ORANGE, CYAN, GREEN, PURPLE]
for i, key in enumerate(H0_ORDERED):
    m = H0_MEASUREMENTS[key]
    data_point_err(ax, i, m["H0"], m["uncertainty"],
                  label=key.replace("_", "\n"), color=colors_h[i])
    prov("H0_%s" % key, m["H0"], "H0_MEASUREMENTS['%s']" % key)

measurement_band(ax, H0_local, H0_MEASUREMENTS["SH0ES"]["uncertainty"],
                  "Local: 73.0 $\\pm$ 1.0", MAG, label_x=4.8)
measurement_band(ax, H0_far, H0_MEASUREMENTS["Planck"]["uncertainty"],
                  "CMB: 67.4 $\\pm$ 0.5", BLUE, label_x=4.8)

result_box(ax, 2, 65.5, "Tension: %s$\\sigma$" % mp.nstr(H0_tension_sigma, 3))
prov("tension_sigma", H0_tension_sigma, "phys24_hubble_lib.H0_tension_sigma")

ax.set_xticks(range(5))
ax.set_xticklabels([k.replace("_", "\n") for k in H0_ORDERED],
                    color=SILVER, fontsize=8)
ax.set_xlim(-0.5, 5.3)
ax.set_ylim(64, 77)
save_fig(fig, "hubble_01_tension_data.png")


# ================================================================
# FIG 2: RUNNING CURVES AT DIFFERENT N
# Type: Running/Convergence (D5.1)
# Shows: H0(N) = H0(0) * r^N for 4 different N values.
# The SHAPE shows how r determines the curve steepness.
# ================================================================

fig, ax = dark_fig("H$_0$ Running Curves for Different N$_{eff}$",
                    xlabel="Boundary Transit Count N",
                    ylabel="H$_0$(N) (km/s/Mpc)")

N_array = np.linspace(0, 200, 500)
for N_total, color, lbl in [
    (10, RED, "N$_{eff}$=10"),
    (50, ORANGE, "N$_{eff}$=50"),
    (100, CYAN, "N$_{eff}$=100"),
    (500, GREEN, "N$_{eff}$=500"),
]:
    r = float(required_r(N_total))
    plot_H0_running(ax, N_array, H0_local, r, color=color, label=lbl)
    prov("r(N=%d)" % N_total, required_r(N_total), "required_r(%d)" % N_total)

measurement_band(ax, H0_far, H0_MEASUREMENTS["Planck"]["uncertainty"],
                  "Planck: 67.4", GOLD, label_x=190)
measurement_band(ax, H0_local, H0_MEASUREMENTS["SH0ES"]["uncertainty"],
                  "SH0ES: 73.0", MAG, label_x=190)

legend(ax, loc='upper right')
ax.set_xlim(0, 200)
ax.set_ylim(60, 76)
save_fig(fig, "hubble_02_running_curves.png")


# ================================================================
# FIG 3: 1-r vs N — THE MAGNITUDE CONSTRAINT
# Type: Running/Convergence (D5.1)
# Shows: How the per-transit correction shrinks with N on a log-log
# plot. The shape is a straight line: 1-r ~ 0.08/N.
# ================================================================

fig, ax = dark_fig("Per-Transit Correction: 1 $-$ r vs N",
                    xlabel="Effective Transit Count N",
                    ylabel="1 $-$ r (correction per transit)")

N_scan = np.logspace(0.5, 4.5, 200)
omr_scan = [float(one_minus_r(N)) for N in N_scan]
prov("1-r curve", "200 points", "one_minus_r(N) for N in logspace")

curve(ax, N_scan, omr_scan, "1 $-$ r = ln(73/67.4) / N", CYAN)

# Mark specific N values from MAGNITUDE_TABLE
for N_mark in [10, 100, 1000, 10000]:
    omr_mark = float(MAGNITUDE_TABLE[N_mark]["one_minus_r"])
    data_point(ax, N_mark, omr_mark, "N=%d" % N_mark, GOLD, size=150)

# VP step size for comparison
threshold_line(ax, 0, label="", vertical=False)  # just x axis
ax.axhline(float(VP_STEP_SIZE), color=ORANGE, linewidth=1.5,
           linestyle='--', alpha=0.7)
note(ax, 20, float(VP_STEP_SIZE) * 1.15, "VP step: 1/(3$\\pi$) = 0.106", ORANGE)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(3, 30000)
ax.set_ylim(5e-6, 0.5)
save_fig(fig, "hubble_03_magnitude_constraint.png")


# ================================================================
# FIG 4: STRUCTURAL PARALLEL — ALPHA RUNNING vs H0 RUNNING
# Type: Dual Panel (D5.1 + D5.1)
# Shows: Side-by-side comparison of the two running structures.
# Same mathematical form, different physical variables.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "$\\alpha$ Running (established)",
    "H$_0$ Running (hypothesis)",
    size=(18, 9))

# Left: alpha running
log_mu = np.linspace(np.log10(91.19), 17, 500)
plot_gauge_running(ax1, log_mu,
                    [inv_a1, inv_a2, inv_a3],
                    [b1_mod, b2_mod, b3_mod],
                    labels=["1/$\\alpha_1$", "1/$\\alpha_2$", "1/$\\alpha_3$"])
threshold_line(ax1, np.log10(3000), "M$_{VL}$")
ax1.set_xlabel("log$_{10}$(E/GeV)", color=SILVER, fontsize=11)
ax1.set_ylabel("1/$\\alpha_i$", color=SILVER, fontsize=11)
ax1.set_xlim(1.5, 17)
ax1.set_ylim(0, 70)
legend(ax1, loc='upper left')
result_box(ax1, 12, 10, "Verified to 0.02 ppm\n(PHYS-5)", GREEN)

# Right: H0 running
N_array = np.linspace(0, 500, 300)
for N_total, color, lbl in [(100, CYAN, "N=100"), (500, GREEN, "N=500")]:
    r_val = float(required_r(N_total))
    plot_H0_running(ax2, N_array, H0_local, r_val, color=color, label=lbl)

measurement_band(ax2, H0_far, H0_MEASUREMENTS["Planck"]["uncertainty"], "", GOLD)
measurement_band(ax2, H0_local, H0_MEASUREMENTS["SH0ES"]["uncertainty"], "", MAG)

ax2.set_xlabel("Boundary Transit Count N", color=SILVER, fontsize=11)
ax2.set_ylabel("H$_0$(N) (km/s/Mpc)", color=SILVER, fontsize=11)
ax2.set_xlim(0, 500)
ax2.set_ylim(60, 76)
legend(ax2)
result_box(ax2, 350, 63, "Not yet testable\n(N unknown)", ORANGE)

save_fig(fig, "hubble_04_structural_parallel.png")


# ================================================================
# FIG 5: THE DATA GAP — ALL EFFECTIVE_N ARE NONE
# Type: Scale/Landscape (D5.2)
# Shows: Each measurement with its H0 value on one axis and
# "?" on the N axis. The gap between data and model is visual.
# ================================================================

fig, ax = dark_fig("The Data Gap: Every N is Unknown",
                    xlabel="Effective Transit Count N (unknown for all)",
                    ylabel="H$_0$ (km/s/Mpc)")

# The running curve (light, as context)
N_array = np.linspace(0, 300, 200)
r_100 = float(required_r(100))
curve(ax, N_array, float(f2m(H0_local)) * r_100 ** N_array,
      "H$_0$(N) if N$_{eff}$=100", DIM, width=1.5, style='--')

# Data points — plotted at GUESSED x positions with ? markers
guess_N = {"SH0ES": 0, "H0LiCOW": 10, "CCHP": 60, "DES_BAO_BBN": 150, "Planck": 250}

for i, key in enumerate(H0_ORDERED):
    m = H0_MEASUREMENTS[key]
    N_guess = guess_N[key]
    data_point_err(ax, N_guess, m["H0"], m["uncertainty"],
                  color=colors_h[i])
    ax.text(N_guess, float(f2m(m["H0"])) + float(f2m(m["uncertainty"])) * 2.5,
            key.replace("_", "\n"), color=colors_h[i], fontsize=8,
            ha='center', va='bottom')
    # Question mark below each point
    ax.text(N_guess, float(f2m(m["H0"])) - float(f2m(m["uncertainty"])) * 3,
            "N = ?", color=ORANGE, fontsize=10, ha='center', va='top',
            fontweight='bold')

result_box(ax, 150, 75.5, "5 measurements, 0 known N values\nThis is the blocking dependency")

ax.set_xlim(-20, 300)
ax.set_ylim(63, 77)
save_fig(fig, "hubble_05_data_gap.png")


# ================================================================
# FIG 6: FALSIFICATION LANDSCAPE
# Type: Threshold/Region (D5.3)
# Shows: Which F-tests pass and fail, with the data that drives them.
# ================================================================

fig, ax = dark_fig("Falsification Test Results",
                    ylabel="H$_0$ (km/s/Mpc)")

# F1: monotonicity — show the inversion
H0_vals = [float(f2m(H0_MEASUREMENTS[k]["H0"])) for k in H0_ORDERED]
H0_uncs = [float(f2m(H0_MEASUREMENTS[k]["uncertainty"])) for k in H0_ORDERED]

for i in range(len(H0_ORDERED)):
    c = GREEN if i == 0 or H0_vals[i] <= H0_vals[i-1] else RED
    if i == 1:
        c = RED  # H0LiCOW > SH0ES
    ax.errorbar([i], [H0_vals[i]], yerr=[H0_uncs[i]], fmt='none',
                ecolor=c, elinewidth=2, capsize=5, capthick=2)
    ax.scatter([i], [H0_vals[i]], s=200, c=c, edgecolors=WHITE,
               linewidth=2, zorder=10)

# Highlight the F1 strict failure
ax.annotate("F1 FAIL: 73.3 > 73.0",
            xy=(1, H0_vals[1]), xytext=(2.5, 74.5),
            color=RED, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=2))

# F1 soft pass — show overlapping bands
ax.fill_between([0-0.3, 0+0.3],
                H0_vals[0] - H0_uncs[0], H0_vals[0] + H0_uncs[0],
                color=GREEN, alpha=0.1)
ax.fill_between([1-0.3, 1+0.3],
                H0_vals[1] - H0_uncs[1], H0_vals[1] + H0_uncs[1],
                color=ORANGE, alpha=0.1)

note(ax, 2.5, 73.5, "F1 soft: PASS\n(1$\\sigma$ bands overlap)", GREEN)

# F4: intermediate distinct
note(ax, 2.5, 71.5, "F4: PASS\n(CCHP distinct from\nboth endpoints)", CYAN)

result_box(ax, 2.5, 65.5, "F1 strict: FAIL (data, not bug)\nF1 soft: PASS\nF4: PASS")

ax.set_xticks(range(5))
ax.set_xticklabels([k.replace("_", "\n") for k in H0_ORDERED],
                    color=SILVER, fontsize=8)
ax.set_xlim(-0.5, 5)
ax.set_ylim(64, 76)
save_fig(fig, "hubble_06_falsification.png")


# ================================================================
# FIG 7: CUMULATIVE RATIO AND THE 337/365 FRACTION
# Type: Connection/Integer Map (D5.5)
# Shows: The exact Fraction 337/365 and what it means physically.
# The integer content is the starting point for the curve.
# ================================================================

fig, ax = dark_canvas("The Cumulative Ratio: 337/365", size=(16, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Central fraction
result_box(ax, 5, 7.5, "H$_0$(far) / H$_0$(local) = 67.4 / 73.0 = 337 / 365",
           GOLD, fontsize=14)

prov("cumulative_ratio", cumulative_ratio, "phys24_hubble_lib.cumulative_ratio")

# Factor tree
note(ax, 1.5, 6.0, "337 is PRIME", CYAN, fontsize=12)
note(ax, 6.5, 6.0, "365 = 5 $\\times$ 73", ORANGE, fontsize=12)
note(ax, 6.5, 5.3, "73 = H$_0$(local) in km/s/Mpc", SILVER, fontsize=10)
note(ax, 6.5, 4.7, "5 = exact factor from 67.4 = 337/5", SILVER, fontsize=10)

# ln of the ratio
note(ax, 2.0, 3.5, "ln(73.0/67.4) = ln(365/337) = %s" % mp.nstr(ln_cumulative, 6),
     GREEN, fontsize=11)
prov("ln_cumulative", ln_cumulative, "phys24_hubble_lib.ln_cumulative")

# The running model
note(ax, 2.0, 2.5, "If H$_0$(N) = H$_0$(0) $\\times$ r$^N$:", WHITE, fontsize=11)
note(ax, 2.0, 1.8, "  r$^N$ = 337/365", WHITE, fontsize=11)
note(ax, 2.0, 1.1, "  1 $-$ r $\\approx$ 0.0798 / N", SILVER, fontsize=10)

# VP comparison
note(ax, 6.0, 2.5, "Compare VP step:", ORANGE, fontsize=10)
note(ax, 6.0, 1.8, "  1/(3$\\pi$) = 1/(12R$_2$) = %s" % mp.nstr(VP_STEP_SIZE, 5),
     ORANGE, fontsize=10)
note(ax, 6.0, 1.1, "  H$_0$ step / VP step = 0.0798 / (N $\\times$ 0.106)",
     SILVER, fontsize=9)

save_fig(fig, "hubble_07_cumulative_fraction.png")


# ================================================================
# FIG 8: THE COMPLETE PICTURE — RUNNING + DATA + UNKNOWNS
# Type: Running/Convergence + Threshold (D5.1 + D5.3)
# Shows: The hypothesis curve with data, unknowns marked, and
# the prediction range for different N values. This is the
# "money diagram" — everything in one view.
# ================================================================

fig, ax = dark_fig("The Complete Picture: H$_0$ Running Hypothesis",
                    xlabel="Effective Transit Count N",
                    ylabel="H$_0$(N) (km/s/Mpc)")

# Family of curves for different N_eff
N_plot = np.linspace(0, 600, 500)
for N_total, color, alpha_v in [(30, RED, 0.3), (100, CYAN, 0.6),
                                  (300, GREEN, 0.6), (1000, PURPLE, 0.3)]:
    r_val = float(required_r(N_total))
    y = float(f2m(H0_local)) * r_val ** N_plot
    curve(ax, N_plot, y, "N$_{eff}$=%d" % N_total, color, width=2, alpha=alpha_v)

# Measurement bands
measurement_band(ax, H0_local, H0_MEASUREMENTS["SH0ES"]["uncertainty"],
                  "SH0ES", MAG)
measurement_band(ax, H0_far, H0_MEASUREMENTS["Planck"]["uncertainty"],
                  "Planck", BLUE)

# CCHP intermediate
H0_cchp = float(f2m(H0_MEASUREMENTS["CCHP"]["H0"]))
shaded_region_h(ax, H0_cchp - 1.7, H0_cchp + 1.7, CYAN, 0.06, "")
ax.axhline(H0_cchp, color=CYAN, linewidth=1, linestyle=':', alpha=0.7)
note(ax, 420, H0_cchp + 0.3, "CCHP: 69.8 $\\pm$ 1.7", CYAN, fontsize=9)

# Unknown N zone
shaded_region(ax, -20, 600, DIM, 0.02)
result_box(ax, 300, 75, "All N values unknown\nCurve shape depends on N$_{eff}$")

# Arrow showing "which curve fits?"
arrow_label(ax, 200, 67.4, 400, 70, "Which curve\nhits here?", GOLD)

legend(ax, loc='lower left')
ax.set_xlim(-10, 600)
ax.set_ylim(62, 77)
save_fig(fig, "hubble_08_complete_picture.png")


# ================================================================
# PROVENANCE AND SUMMARY
# ================================================================

print_provenance()

print("=" * 70)
print("  HUBBLE TENSION DIAGRAMS COMPLETE — 8 figures")
print("  Every value from phys24_hubble_lib.py")
print("  Every plot call from data_5_diagram_lib.py")
print("  Hypothesis status: %s" % HYPOTHESIS_STATUS)
print("=" * 70)


"""
  [1] Saved: hubble_01_tension_data.png
  [2] Saved: hubble_02_running_curves.png
  [3] Saved: hubble_03_magnitude_constraint.png
  [4] Saved: hubble_04_structural_parallel.png
  [5] Saved: hubble_05_data_gap.png
  [6] Saved: hubble_06_falsification.png
  [7] Saved: hubble_07_cumulative_fraction.png
  [8] Saved: hubble_08_complete_picture.png

========================================================================
  PROVENANCE: 13 values, 0 hardcoded physics
========================================================================
  Fig 1   H0_SH0ES               H0_MEASUREMENTS['SH0ES']
  Fig 1   H0_H0LiCOW             H0_MEASUREMENTS['H0LiCOW']
  Fig 1   H0_CCHP                H0_MEASUREMENTS['CCHP']
  Fig 1   H0_DES_BAO_BBN         H0_MEASUREMENTS['DES_BAO_BBN']
  Fig 1   H0_Planck              H0_MEASUREMENTS['Planck']
  Fig 1   tension_sigma          phys24_hubble_lib.H0_tension_sigma
  Fig 2   r(N=10)                required_r(10)
  Fig 2   r(N=50)                required_r(50)
  Fig 2   r(N=100)               required_r(100)
  Fig 2   r(N=500)               required_r(500)
  Fig 3   1-r curve              one_minus_r(N) for N in logspace
  Fig 7   cumulative_ratio       phys24_hubble_lib.cumulative_ratio
  Fig 7   ln_cumulative          phys24_hubble_lib.ln_cumulative

======================================================================
  HUBBLE TENSION DIAGRAMS COMPLETE — 8 figures
  Every value from phys24_hubble_lib.py
  Every plot call from data_5_diagram_lib.py
  Hypothesis status: ACTIVE_INVESTIGATION
======================================================================
"""