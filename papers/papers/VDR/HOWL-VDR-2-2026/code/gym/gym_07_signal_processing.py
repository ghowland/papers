#!/usr/bin/env python3
"""
gym_07_signal_processing.py — VDR exercises in discrete signal processing

DFT on rational signals, convolution, correlation, filtering,
z-transform evaluation. All exact VDR arithmetic.

Note: standard DFT uses complex exponentials (irrational).
We work with the Number Theoretic Transform (NTT) analog
and rational-valued filters instead.
"""

import sys
sys.path.insert(0, '..')
from vdr.vdr import VDR, Remainder
from vdr.linalg import Vec, Mat
from fractions import Fraction

def section(title):
    print("\n=== %s ===" % title)

def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print("  %-55s %s" % (label, status))
    return condition

results = {"pass": 0, "fail": 0}
def record(ok):
    if ok: results["pass"] += 1
    else: results["fail"] += 1

# =========================================================================
section("1. Exact discrete convolution")
# =========================================================================

def convolve(a, b):
    """Exact linear convolution of two VDR sequences."""
    na, nb = len(a), len(b)
    result = [VDR(0)] * (na + nb - 1)
    for i in range(na):
        for j in range(nb):
            result[i + j] = result[i + j] + a[i] * b[j]
    return result

# convolution of [1, 2, 3] with [1, 1]
a = [VDR(1), VDR(2), VDR(3)]
b = [VDR(1), VDR(1)]
c = convolve(a, b)
expected = [VDR(1), VDR(3), VDR(5), VDR(3)]
ok = all(x == y for x, y in zip(c, expected))
record(check("[1,2,3] * [1,1] = [1,3,5,3]", ok))

# convolution with rationals
a2 = [VDR(1, 2), VDR(1, 3), VDR(1, 5)]
b2 = [VDR(1, 7), VDR(1, 11)]
c2 = convolve(a2, b2)
print("  rational conv: %s" % [x.to_fraction() for x in c2])
# verify by manual computation
ok = c2[0] == VDR(1, 2) * VDR(1, 7)
record(check("first element of rational convolution", ok))

# =========================================================================
section("2. Exact cross-correlation")
# =========================================================================

def correlate(a, b):
    """Exact cross-correlation of two sequences."""
    na, nb = len(a), len(b)
    result = []
    for lag in range(-(nb - 1), na):
        total = VDR(0)
        for j in range(nb):
            idx = lag + j
            if 0 <= idx < na:
                total = total + a[idx] * b[j]
        result.append(total)
    return result

# auto-correlation of [1, 2, 1]
signal = [VDR(1), VDR(2), VDR(1)]
acorr = correlate(signal, signal)
print("  auto-correlation of [1,2,1]: %s" % [x.to_fraction() for x in acorr])
# should be symmetric and peak at center
center = len(acorr) // 2
ok = all(acorr[i] == acorr[len(acorr) - 1 - i] for i in range(len(acorr)))
record(check("auto-correlation is symmetric", ok))
ok = all(acorr[center] >= acorr[i] for i in range(len(acorr)))
record(check("auto-correlation peaks at center", ok))

# =========================================================================
section("3. Moving average filter (exact)")
# =========================================================================

def moving_average(signal, window):
    """Exact moving average using VDR arithmetic."""
    n = len(signal)
    w = VDR(1, window)
    result = []
    for i in range(n - window + 1):
        total = VDR(0)
        for j in range(window):
            total = total + signal[i + j]
        result.append(total * w)
    return result

# signal with known pattern
signal = [VDR(i) for i in range(10)]  # 0, 1, 2, ..., 9
ma3 = moving_average(signal, 3)
print("  MA(3) of [0..9]: %s" % [x.to_fraction() for x in ma3])

# verify: MA(3) of [0,1,2,...] should be [1, 2, 3, ..., 8]
expected_ma = [VDR(i, 1) for i in range(1, 9)]
ok = all(ma3[i] == expected_ma[i] for i in range(len(ma3)))
record(check("MA(3) of arithmetic sequence", ok))

# rational signal
rsignal = [VDR(1, k) for k in range(1, 8)]  # 1, 1/2, 1/3, ..., 1/7
rma2 = moving_average(rsignal, 2)
print("  MA(2) of harmonic: %s" % [x.to_fraction() for x in rma2])
# every entry is exact
record(check("rational MA entries are exact",
             all(isinstance(x.to_fraction(), Fraction) for x in rma2)))

# =========================================================================
section("4. Z-transform evaluation at rational points")
# =========================================================================

# H(z) = sum_{n=0}^{N-1} h[n] * z^{-n}
def z_transform(h, z):
    """Evaluate z-transform at a VDR rational point."""
    result = VDR(0)
    z_inv_n = VDR(1)
    z_inv = VDR(1) / z
    for n in range(len(h)):
        result = result + h[n] * z_inv_n
        z_inv_n = z_inv_n * z_inv
    return result

# simple FIR filter: h = [1/3, 1/3, 1/3]
h = [VDR(1, 3), VDR(1, 3), VDR(1, 3)]

# evaluate at z = 2
hz2 = z_transform(h, VDR(2))
print("  H(2) = %s" % hz2.to_fraction())
# = 1/3 + 1/3 * 1/2 + 1/3 * 1/4 = 1/3 + 1/6 + 1/12 = 7/12
record(check("H(2) = 7/12", hz2 == VDR(7, 12)))

# evaluate at z = 1 (DC gain)
hz1 = z_transform(h, VDR(1))
print("  H(1) = %s (DC gain)" % hz1.to_fraction())
record(check("H(1) = 1 (unity DC gain)", hz1 == VDR(1)))

# =========================================================================
section("5. Toeplitz matrix from filter coefficients")
# =========================================================================

# convolution can be expressed as Toeplitz matrix multiplication
def toeplitz_mat(h, n):
    """Build Toeplitz matrix for convolution of h with n-length signal."""
    nh = len(h)
    m = n + nh - 1
    rows = []
    for i in range(m):
        row = [VDR(0)] * n
        for j in range(n):
            k = i - j
            if 0 <= k < nh:
                row[j] = h[k]
        rows.append(row)
    return Mat(rows)

h = [VDR(1), VDR(2), VDR(1)]
T = toeplitz_mat(h, 4)
print("  Toeplitz matrix for [1,2,1]:")
print(T.pretty())

# multiply by signal
signal = Vec([VDR(1), VDR(0), VDR(1), VDR(0)])
result = T * signal
conv_direct = convolve([VDR(1), VDR(0), VDR(1), VDR(0)], h)
ok = all(result[i] == conv_direct[i] for i in range(len(conv_direct)))
record(check("Toeplitz*signal = convolution", ok))

# =========================================================================
section("6. Difference equation (IIR filter)")
# =========================================================================

# y[n] = (1/2)*y[n-1] + x[n]
# impulse response: x = [1, 0, 0, 0, ...]
# y = [1, 1/2, 1/4, 1/8, ...]
def iir_filter(x, a_coeff):
    """First-order IIR: y[n] = a*y[n-1] + x[n]"""
    y = []
    for n in range(len(x)):
        prev = y[-1] if y else VDR(0)
        y.append(a_coeff * prev + x[n])
    return y

impulse = [VDR(1)] + [VDR(0)] * 9
response = iir_filter(impulse, VDR(1, 2))
print("  IIR impulse response (a=1/2):")
print("    %s" % [r.to_fraction() for r in response])

# verify: y[n] = (1/2)^n
for n in range(10):
    expected = Fraction(1, 2 ** n)
    ok = response[n].to_fraction() == expected
    if not ok:
        print("  y[%d] = %s, expected %s" % (n, response[n].to_fraction(), expected))
record(check("IIR impulse response = (1/2)^n", all(
    response[n].to_fraction() == Fraction(1, 2 ** n) for n in range(10)
)))

# rational coefficient: a = 2/3
response2 = iir_filter(impulse, VDR(2, 3))
print("  IIR impulse response (a=2/3):")
print("    %s" % [r.to_fraction() for r in response2[:6]])

for n in range(8):
    expected = Fraction(2, 3) ** n
    ok = response2[n].to_fraction() == expected
    if not ok:
        print("  y[%d] = %s, expected %s" % (n, response2[n].to_fraction(), expected))
record(check("IIR impulse response = (2/3)^n", all(
    response2[n].to_fraction() == Fraction(2, 3) ** n for n in range(8)
)))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 07 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
