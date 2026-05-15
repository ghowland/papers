"""
VDR Gym 22: Wavelets and Exact Transforms
Haar wavelet transform, perfect reconstruction, rational filter banks.
"""
from __future__ import annotations
import sys
sys.path.insert(0, '..')
from vdr import VDR

passed = 0
failed = 0
def check(name, condition):
    global passed, failed
    if condition:
        passed += 1
        print("  PASS: %s" % name)
    else:
        failed += 1
        print("  FAIL: %s" % name)

# === 1. Haar wavelet single-level transform ===
print("\n=== 1. Haar single-level transform ===")

def haar_forward(signal):
    """One level of Haar transform. Returns (averages, details)."""
    n = len(signal)
    assert n % 2 == 0
    avgs = []
    dets = []
    for i in range(0, n, 2):
        a = (signal[i] + signal[i + 1]) / VDR(2)
        d = (signal[i] - signal[i + 1]) / VDR(2)
        avgs.append(a)
        dets.append(d)
    return avgs, dets

def haar_inverse(avgs, dets):
    """One level of inverse Haar transform."""
    signal = []
    for a, d in zip(avgs, dets):
        signal.append(a + d)
        signal.append(a - d)
    return signal

# test signal: [1, 3, 5, 7]
sig = [VDR(1), VDR(3), VDR(5), VDR(7)]
avgs, dets = haar_forward(sig)
print("  signal = %s" % [str(x) for x in sig])
print("  averages = %s" % [str(x) for x in avgs])
print("  details = %s" % [str(x) for x in dets])

check("avg[0] = 2", avgs[0] == VDR(2))
check("avg[1] = 6", avgs[1] == VDR(6))
check("det[0] = -1", dets[0] == VDR(-1))
check("det[1] = -1", dets[1] == VDR(-1))

# === 2. Perfect reconstruction ===
print("\n=== 2. Perfect reconstruction ===")

recon = haar_inverse(avgs, dets)
print("  reconstructed = %s" % [str(x) for x in recon])
all_match = all(recon[i] == sig[i] for i in range(4))
check("perfect reconstruction", all_match)

# === 3. Multi-level Haar on 8-sample signal ===
print("\n=== 3. Multi-level Haar (8 samples) ===")

sig8 = [VDR(1), VDR(3), VDR(2), VDR(4), VDR(5), VDR(1), VDR(3), VDR(7)]

# level 1
a1, d1 = haar_forward(sig8)
print("  L1 avgs = %s" % [str(x) for x in a1])
print("  L1 dets = %s" % [str(x) for x in d1])

# level 2
a2, d2 = haar_forward(a1)
print("  L2 avgs = %s" % [str(x) for x in a2])
print("  L2 dets = %s" % [str(x) for x in d2])

# level 3
a3, d3 = haar_forward(a2)
print("  L3 avgs = %s" % [str(x) for x in a3])
print("  L3 dets = %s" % [str(x) for x in d3])

# inverse all levels
r2 = haar_inverse(a3, d3)
r1 = haar_inverse(r2, d2)
r0 = haar_inverse(r1, d1)
print("  reconstructed = %s" % [str(x) for x in r0])
all_match_8 = all(r0[i] == sig8[i] for i in range(8))
check("8-sample 3-level perfect reconstruction", all_match_8)

# === 4. Haar on rational signal ===
print("\n=== 4. Haar on rational signal ===")

sig_rat = [VDR(1, 3), VDR(1, 7), VDR(2, 5), VDR(3, 11)]
a_rat, d_rat = haar_forward(sig_rat)
recon_rat = haar_inverse(a_rat, d_rat)

print("  avg[0] = %s" % a_rat[0].to_fraction())
# (1/3 + 1/7) / 2 = (7+3)/(42) / 2 = 10/42 / 2 = 5/42
check("rational avg[0] = 5/21", a_rat[0] == VDR(5, 21))

all_match_rat = all(recon_rat[i] == sig_rat[i] for i in range(4))
check("rational perfect reconstruction", all_match_rat)

# === 5. Energy preservation (Parseval) ===
print("\n=== 5. Energy preservation ===")

def energy(signal):
    return sum((x * x for x in signal), VDR(0))

# energy of signal = energy of transform coefficients
e_sig = energy(sig8)
e_transform = energy(a3) + energy(d3) + energy(d2) + energy(d1)
# Haar without normalization by sqrt(2) preserves energy/2 at each level
# with our definition (divide by 2), energy splits as:
# E(signal) = 2 * (E(avgs) + E(dets))
# at 3 levels: E = 2^3 * E(a3) + ... it's simpler to check reconstruction

# actually with our normalization: a = (x+y)/2, d = (x-y)/2
# x^2 + y^2 = (a+d)^2 + (a-d)^2 = 2a^2 + 2d^2
# so E(signal) = 2 * E(transform at each level)
e_l1 = VDR(2) * (energy(a1) + energy(d1))
print("  E(signal) = %s, 2*(E(a1)+E(d1)) = %s" % (
    e_sig.to_fraction(), e_l1.to_fraction()))
check("Parseval (level 1): E = 2*(Ea+Ed)", e_sig == e_l1)

# === 6. Haar as matrix multiplication ===
print("\n=== 6. Haar as matrix ===")

from vdr import Mat

# 4-point Haar matrix (unnormalized by sqrt(2), using 1/2 scaling)
H4 = Mat([
    [VDR(1, 2), VDR(1, 2), VDR(0), VDR(0)],
    [VDR(0), VDR(0), VDR(1, 2), VDR(1, 2)],
    [VDR(1, 2), VDR(-1, 2), VDR(0), VDR(0)],
    [VDR(0), VDR(0), VDR(1, 2), VDR(-1, 2)],
])

from vdr import Vec
sig_vec = Vec(sig)
transformed = H4.matvec(sig_vec)
print("  H4 * signal = %s" % [str(x) for x in transformed.data])

# first 2 are averages, last 2 are details
check("matrix avg[0] matches", transformed.data[0] == avgs[0])
check("matrix avg[1] matches", transformed.data[1] == avgs[1])
check("matrix det[0] matches", transformed.data[2] == dets[0])
check("matrix det[1] matches", transformed.data[3] == dets[1])

# inverse matrix
H4_inv = H4.inv()
recon_vec = H4_inv.matvec(transformed)
all_match_mat = all(recon_vec.data[i] == sig[i] for i in range(4))
check("matrix inverse reconstruction", all_match_mat)

# === 7. Haar denoising (thresholding) ===
print("\n=== 7. Haar denoising ===")

# signal + noise
sig_noisy = [VDR(10), VDR(11), VDR(10), VDR(9),
             VDR(20), VDR(21), VDR(19), VDR(20)]

a_n1, d_n1 = haar_forward(sig_noisy)
a_n2, d_n2 = haar_forward(a_n1)
a_n3, d_n3 = haar_forward(a_n2)

# hard threshold: zero out small details (|d| < 1)
def threshold(dets, thresh):
    return [d if (d > thresh or d < -thresh) else VDR(0) for d in dets]

thresh = VDR(1)
d_n1_t = threshold(d_n1, thresh)
d_n2_t = threshold(d_n2, thresh)
d_n3_t = threshold(d_n3, thresh)

# reconstruct
r_n2 = haar_inverse(a_n3, d_n3_t)
r_n1 = haar_inverse(r_n2, d_n2_t)
r_n0 = haar_inverse(r_n1, d_n1_t)

print("  denoised = %s" % [str(x) for x in r_n0])
# all values should be exact rationals
all_closed = all(x.is_closed for x in r_n0)
check("denoised values are exact rationals", all_closed)

# denoised should be smoother (closer to [10,10,10,10,20,20,20,20])
# check that large-scale structure preserved
avg_first = (r_n0[0] + r_n0[1] + r_n0[2] + r_n0[3]) / VDR(4)
avg_second = (r_n0[4] + r_n0[5] + r_n0[6] + r_n0[7]) / VDR(4)
print("  avg first half = %s, avg second half = %s" % (
    avg_first.to_fraction(), avg_second.to_fraction()))
check("first half avg = 10", avg_first == VDR(10))
check("second half avg = 20", avg_second == VDR(20))

# === 8. 64-sample Haar roundtrip ===
print("\n=== 8. 64-sample roundtrip ===")

# signal: x[n] = n/64 (ramp)
sig64 = [VDR(n, 64) for n in range(64)]

# 6 levels of decomposition
coeffs = []
current = sig64
for level in range(6):
    a, d = haar_forward(current)
    coeffs.append(d)
    current = a
coeffs.append(current)  # final averages

# reconstruct
current = coeffs[-1]
for level in range(5, -1, -1):
    current = haar_inverse(current, coeffs[level])

all_match_64 = all(current[i] == sig64[i] for i in range(64))
check("64-sample 6-level perfect reconstruction", all_match_64)


print("\n" + "=" * 50)
print("Gym 22 results: %d passed, %d failed" % (passed, failed))
if failed == 0:
    print("ALL GYM 22 TESTS PASSED")
print("=" * 50)

