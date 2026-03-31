import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 120

# e from Taylor series — exact Fraction, 100+ correct digits
def compute_e(n_terms=80):
    total = Fraction(0)
    factorial = 1
    for i in range(n_terms):
        total += Fraction(1, factorial)
        factorial *= (i + 1)
    return total

e_rat = compute_e(80)

print("=" * 70)
print("e AS p/2^n AT 100-DIGIT PRECISION")
print("=" * 70)
print()

# We need 2^{-(n+1)} < 10^{-100}
# n+1 > 100 * log2(10) = 332.19
# n >= 333

# But we have e_rat which is already exact to 100+ digits.
# p = round(e_rat * 2^n) = nearest integer to e * 2^n
# The error is |e - p/2^n| <= 1/(2 * 2^n) = 2^{-(n+1)}

# For 100-digit match: n = 333 gives 2^{-334} ~ 10^{-100.6}
# Let's use n = 340 for margin

for n in [333, 340, 400, 500]:
    q = 2**n
    # e_rat is a Fraction. Multiply by q, round to nearest integer.
    e_times_q = e_rat * q
    # Round: check floor and floor+1
    p_floor = e_times_q.numerator // e_times_q.denominator
    remainder = e_times_q - p_floor
    if remainder >= Fraction(1, 2):
        p = p_floor + 1
    else:
        p = p_floor
    
    # Now p/q is our approximation
    approx = Fraction(p, q)
    
    # Verify at 100 digits using mpmath
    mp.dps = 120
    our_val = mpf(p) / mpf(q)
    e_ref = mp.e
    
    our_str = mp.nstr(our_val, 100)
    ref_str = mp.nstr(e_ref, 100)
    
    match = (our_str == ref_str)
    
    # Count matching digits
    match_count = 0
    for a, b in zip(our_str, ref_str):
        if a == b:
            match_count += 1
        else:
            break
    
    print(f"n = {n} (2^{n}):")
    print(f"  p has {p.bit_length()} bits ({len(str(p))} decimal digits)")
    print(f"  q = 2^{n} ({n} bits)")
    print(f"  100-digit string match: {'YES' if match else 'NO'}")
    if not match:
        print(f"  Matching chars: {match_count}")
        # Find first divergence
        for i, (a, b) in enumerate(zip(our_str, ref_str)):
            if a != b:
                print(f"  First divergence at position {i}")
                print(f"    ours: ...{our_str[max(0,i-3):i+5]}...")
                print(f"    ref:  ...{ref_str[max(0,i-3):i+5]}...")
                break
    else:
        print(f"  ours: {our_str}")
        print(f"  ref:  {ref_str}")
    
    print(f"  p = {p}")
    print(f"  p is Fraction: {isinstance(approx, Fraction)}")
    print(f"  GCD(p, 2^{n}) = {Fraction(p, q).denominator == q}")
    
    # Check if p is odd (meaning the fraction is already in lowest terms with 2^n denom)
    print(f"  p is odd: {p % 2 == 1}")
    if p % 2 == 1:
        print(f"  Fraction is irreducible: p/2^{n} is already lowest terms")
    else:
        # Find actual power of 2 in denominator after reduction
        reduced = Fraction(p, q)
        actual_q = reduced.denominator
        actual_n = actual_q.bit_length() - 1
        print(f"  Reduced denominator: 2^{actual_n}")
    print()

# Now: the minimal n for 100-digit match
print("=" * 70)
print("FINDING MINIMAL n FOR 100-DIGIT MATCH")
print("=" * 70)
print()

# Binary search
lo, hi = 300, 400
while lo < hi:
    mid = (lo + hi) // 2
    q = 2**mid
    e_times_q = e_rat * q
    p_floor = e_times_q.numerator // e_times_q.denominator
    remainder = e_times_q - p_floor
    p = p_floor + 1 if remainder >= Fraction(1, 2) else p_floor
    
    our_val = mpf(p) / mpf(q)
    our_str = mp.nstr(our_val, 100)
    ref_str = mp.nstr(mp.e, 100)
    
    if our_str == ref_str:
        hi = mid
    else:
        lo = mid + 1

n_min = lo
q_min = 2**n_min
e_times_q = e_rat * q_min
p_floor = (e_times_q).numerator // (e_times_q).denominator
remainder = e_times_q - p_floor
p_min = p_floor + 1 if remainder >= Fraction(1, 2) else p_floor

print(f"Minimal n for 100-digit match: {n_min}")
print(f"  p = {p_min}")
print(f"  p has {len(str(p_min))} decimal digits")
print(f"  p is odd: {p_min % 2 == 1}")
print()

# Verify
our_val = mpf(p_min) / mpf(2**n_min)
our_str = mp.nstr(our_val, 100)
ref_str = mp.nstr(mp.e, 100)
print(f"  Verification: {our_str == ref_str}")
print(f"  {our_str}")
print(f"  {ref_str}")
print()

# Also check n_min - 1
n_test = n_min - 1
q_test = 2**n_test
e_times_q = e_rat * q_test
p_floor = (e_times_q).numerator // (e_times_q).denominator
remainder = e_times_q - p_floor
p_test = p_floor + 1 if remainder >= Fraction(1, 2) else p_floor
our_val = mpf(p_test) / mpf(q_test)
our_str_prev = mp.nstr(our_val, 100)
print(f"  n = {n_test}: match = {our_str_prev == ref_str}")
if our_str_prev != ref_str:
    for i, (a, b) in enumerate(zip(our_str_prev, ref_str)):
        if a != b:
            print(f"  Fails at position {i} ({i-2} digits after decimal)")
            break

        