"""
VDR Gym 18: Coding Theory and Finite Fields
Hamming codes, parity checks, syndrome decoding, GF(p) arithmetic.
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

# === 1. GF(p) arithmetic ===
print("\n=== 1. GF(7) arithmetic ===")

def gf_add(a, b, p):
    return VDR((a.v + b.v) % p)

def gf_mul(a, b, p):
    return VDR((a.v * b.v) % p)

def gf_inv(a, p):
    """Modular inverse via Fermat's little theorem: a^(p-2) mod p."""
    result = VDR(1)
    base = VDR(a.v % p)
    exp = p - 2
    while exp > 0:
        if exp % 2 == 1:
            result = gf_mul(result, base, p)
        base = gf_mul(base, base, p)
        exp //= 2
    return result

# GF(7) tests
check("3+5 mod 7 = 1", gf_add(VDR(3), VDR(5), 7) == VDR(1))
check("3*5 mod 7 = 1", gf_mul(VDR(3), VDR(5), 7) == VDR(1))
check("inv(3) mod 7 = 5", gf_inv(VDR(3), 7) == VDR(5))
check("inv(2) mod 7 = 4", gf_inv(VDR(2), 7) == VDR(4))
# verify: 2*4 = 8 mod 7 = 1
check("2*4 mod 7 = 1", gf_mul(VDR(2), VDR(4), 7) == VDR(1))

# all nonzero elements have inverses
for a in range(1, 7):
    inv_a = gf_inv(VDR(a), 7)
    prod = gf_mul(VDR(a), inv_a, 7)
    check("GF(7): %d * %d^-1 = 1" % (a, a), prod == VDR(1))

# === 2. Hamming(7,4) encoding ===
print("\n=== 2. Hamming(7,4) encode ===")

# generator matrix G (4x7) for systematic Hamming(7,4)
# data bits d1..d4, parity bits p1..p3
# p1 = d1+d2+d4, p2 = d1+d3+d4, p3 = d2+d3+d4 (mod 2)
def hamming74_encode(data):
    """data = [d1,d2,d3,d4] as ints 0/1. Returns 7-bit codeword."""
    d1, d2, d3, d4 = data
    p1 = (d1 + d2 + d4) % 2
    p2 = (d1 + d3 + d4) % 2
    p3 = (d2 + d3 + d4) % 2
    return [p1, p2, d1, p3, d2, d3, d4]

# parity check matrix H (3x7)
H = [
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
]

def syndrome(codeword):
    """Compute syndrome = H * c^T mod 2. Returns 3-bit list."""
    s = []
    for row in H:
        val = 0
        for j in range(7):
            val += row[j] * codeword[j]
        s.append(val % 2)
    return s

# encode all 16 possible data words
all_valid = True
for i in range(16):
    data = [(i >> 3) & 1, (i >> 2) & 1, (i >> 1) & 1, i & 1]
    cw = hamming74_encode(data)
    syn = syndrome(cw)
    if syn != [0, 0, 0]:
        all_valid = False
        break
check("all 16 codewords have zero syndrome", all_valid)

# specific encode test
cw_1011 = hamming74_encode([1, 0, 1, 1])
print("  encode(1011) = %s" % cw_1011)
check("encode(1011) syndrome = 0", syndrome(cw_1011) == [0, 0, 0])

# === 3. Hamming(7,4) single-error correction ===
print("\n=== 3. Hamming(7,4) error correction ===")

def hamming74_correct(received):
    """Correct single-bit error. Returns corrected codeword."""
    syn = syndrome(received)
    error_pos = syn[0] * 1 + syn[1] * 2 + syn[2] * 4  # 1-indexed
    corrected = list(received)
    if error_pos > 0:
        corrected[error_pos - 1] ^= 1  # flip the error bit
    return corrected

# introduce single-bit errors at every position
cw = hamming74_encode([1, 1, 0, 1])
all_corrected = True
for err_pos in range(7):
    corrupted = list(cw)
    corrupted[err_pos] ^= 1
    fixed = hamming74_correct(corrupted)
    if fixed != cw:
        all_corrected = False
        print("  failed at position %d" % err_pos)
check("all 7 single-bit errors corrected", all_corrected)

# === 4. Hamming distance and weight ===
print("\n=== 4. Hamming distance ===")

def hamming_distance(a, b):
    return sum(VDR(1) if a[i] != b[i] else VDR(0) for i in range(len(a)))

def hamming_weight(a):
    return sum(VDR(1) if x != 0 else VDR(0) for x in a)

# minimum distance of Hamming(7,4) code
min_dist = VDR(7)  # start high
codewords = []
for i in range(16):
    data = [(i >> 3) & 1, (i >> 2) & 1, (i >> 1) & 1, i & 1]
    codewords.append(hamming74_encode(data))

for i in range(16):
    for j in range(i + 1, 16):
        d_ij = hamming_distance(codewords[i], codewords[j])
        if d_ij < min_dist:
            min_dist = d_ij

print("  minimum distance = %s" % min_dist)
check("Hamming(7,4) min distance = 3", min_dist == VDR(3))

# minimum weight of nonzero codewords
min_wt = VDR(7)
for i in range(1, 16):
    w = hamming_weight(codewords[i])
    if w < min_wt:
        min_wt = w
check("min weight = 3 (equals min distance)", min_wt == VDR(3))

# === 5. Repetition code ===
print("\n=== 5. Repetition code (3,1) ===")

# encode: 0 -> 000, 1 -> 111
# decode by majority vote
def rep3_decode(bits):
    s = bits[0] + bits[1] + bits[2]
    return VDR(1) if s >= VDR(2) else VDR(0)

check("rep3 decode 000 = 0", rep3_decode([VDR(0), VDR(0), VDR(0)]) == VDR(0))
check("rep3 decode 111 = 1", rep3_decode([VDR(1), VDR(1), VDR(1)]) == VDR(1))
check("rep3 decode 110 = 1", rep3_decode([VDR(1), VDR(1), VDR(0)]) == VDR(1))
check("rep3 decode 001 = 0", rep3_decode([VDR(0), VDR(0), VDR(1)]) == VDR(0))
check("rep3 decode 101 = 1", rep3_decode([VDR(1), VDR(0), VDR(1)]) == VDR(1))

# === 6. GF(11) polynomial evaluation ===
print("\n=== 6. GF(11) polynomial evaluation ===")

def gf_poly_eval(coeffs, x, p):
    """Evaluate polynomial at x in GF(p). coeffs[i] = coeff of x^i."""
    result = VDR(0)
    x_pow = VDR(1)
    for c in coeffs:
        result = gf_add(result, gf_mul(c, x_pow, p), p)
        x_pow = gf_mul(x_pow, VDR(x.v), p)
    return result

# p(x) = x^2 + 3x + 5 in GF(11)
coeffs = [VDR(5), VDR(3), VDR(1)]
# p(0) = 5
check("p(0) = 5 in GF(11)", gf_poly_eval(coeffs, VDR(0), 11) == VDR(5))
# p(1) = 1+3+5 = 9
check("p(1) = 9 in GF(11)", gf_poly_eval(coeffs, VDR(1), 11) == VDR(9))
# p(2) = 4+6+5 = 15 mod 11 = 4
check("p(2) = 4 in GF(11)", gf_poly_eval(coeffs, VDR(2), 11) == VDR(4))
# p(10) = 100+30+5 = 135 mod 11 = 135 - 12*11 = 135-132 = 3
check("p(10) = 3 in GF(11)", gf_poly_eval(coeffs, VDR(10), 11) == VDR(3))

# === 7. CRC-like checksum ===
print("\n=== 7. Simple checksum ===")

# sum of data words mod p = checksum
def compute_checksum(data, p):
    total = VDR(0)
    for d in data:
        total = gf_add(total, d, p)
    return total

data_7 = [VDR(3), VDR(5), VDR(2), VDR(6)]
cksum = compute_checksum(data_7, 7)
# 3+5+2+6 = 16 mod 7 = 2
print("  checksum = %s" % cksum)
check("checksum = 2 mod 7", cksum == VDR(2))

# verify: data + checksum sums to 0
extended = data_7 + [VDR((7 - cksum.v) % 7)]
total_check = compute_checksum(extended, 7)
check("extended checksum = 0", total_check == VDR(0))


print("\n" + "=" * 50)
print("Gym 18 results: %d passed, %d failed" % (passed, failed))
if failed == 0:
    print("ALL GYM 18 TESTS PASSED")
print("=" * 50)

