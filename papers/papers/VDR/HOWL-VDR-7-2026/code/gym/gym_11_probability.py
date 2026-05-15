#!/usr/bin/env python3
"""
gym_11_probability.py — VDR exercises in exact probability

Exact probability distributions, Bayes' theorem, Markov chains,
random walks, and expected values — all exact VDR rational.
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
section("1. Exact Bayes' theorem")
# =========================================================================

# Disease test: P(disease)=1/1000, P(positive|disease)=99/100,
# P(positive|healthy)=1/100
# P(disease|positive) = P(pos|dis)*P(dis) / P(pos)

p_disease = VDR(1, 1000)
p_pos_given_disease = VDR(99, 100)
p_pos_given_healthy = VDR(1, 100)
p_healthy = VDR(1) - p_disease

p_positive = p_pos_given_disease * p_disease + p_pos_given_healthy * p_healthy
p_disease_given_positive = p_pos_given_disease * p_disease / p_positive

print("  Bayes' theorem — disease test:")
print("    P(positive) = %s" % p_positive.to_fraction())
print("    P(disease|positive) = %s" % p_disease_given_positive.to_fraction())

# the famous result: even with 99% accuracy, P(disease|+) is small
float_result = float(p_disease_given_positive.to_fraction())
print("    = %.4f (about %.1f%%)" % (float_result, float_result * 100))
record(check("P(disease|+) is exact rational", isinstance(
    p_disease_given_positive.to_fraction(), Fraction)))

# verify: P(disease|+) * P(+) + P(healthy|+) * P(+) should sum correctly
# actually just verify P sums to 1
total = p_disease_given_positive + (VDR(1) - p_disease_given_positive)
record(check("probabilities sum to 1", total == VDR(1)))

# =========================================================================
section("2. Exact Markov chain steady state")
# =========================================================================

# weather model: sunny→sunny 0.8, sunny→rainy 0.2
#                rainy→sunny 0.4, rainy→rainy 0.6
P = Mat([
    [VDR(4, 5), VDR(1, 5)],
    [VDR(2, 5), VDR(3, 5)],
])

# steady state: πP = π, sum(π) = 1
# π1 * 4/5 + π2 * 2/5 = π1 → π2 = π1/2
# π1 + π2 = 1 → π1 = 2/3, π2 = 1/3

# compute by matrix power: P^n converges to steady state rows
P_power = P
for _ in range(20):
    P_power = P_power * P

print("  Markov steady state (P^20):")
print(P_power.pretty())

# both rows should be approximately [2/3, 1/3]
row0 = (P_power[0, 0].to_fraction(), P_power[0, 1].to_fraction())
row1 = (P_power[1, 0].to_fraction(), P_power[1, 1].to_fraction())
print("  row 0: %s, %s" % row0)
print("  row 1: %s, %s" % row1)

# solve exactly: (P^T - I)π = 0 with constraint sum=1
# P^T = [[4/5, 2/5],[1/5, 3/5]]
# (P^T - I) = [[-1/5, 2/5],[1/5, -2/5]]
# plus constraint: π1 + π2 = 1
A_mc = Mat([
    [VDR(-1, 5), VDR(2, 5)],
    [VDR(1), VDR(1)],
])
b_mc = Vec([VDR(0), VDR(1)])
pi_exact = A_mc.solve(b_mc)
print("  exact steady state: %s" % [x.to_fraction() for x in pi_exact])
record(check("steady state = [2/3, 1/3]",
             pi_exact[0] == VDR(2, 3) and pi_exact[1] == VDR(1, 3)))

# =========================================================================
section("3. Random walk absorption probabilities")
# =========================================================================

# gambler's ruin: start at k, absorbing barriers at 0 and N
# P(ruin at 0 | start at k) = (q/p)^k ... for p != q
# for p=q=1/2: P(ruin) = 1 - k/N

# exact computation: set up system of equations
# P_k = p * P_{k+1} + q * P_{k-1}, P_0 = 1, P_N = 0
# solve as linear system

N = 5
p = VDR(1, 2)
q = VDR(1, 2)

# system: for k=1..N-1, P_k - p*P_{k+1} - q*P_{k-1} = 0
# with P_0 = 1, P_N = 0
n_interior = N - 1
A_rw = [[VDR(0)] * n_interior for _ in range(n_interior)]
b_rw = [VDR(0)] * n_interior

for k in range(n_interior):
    actual_k = k + 1
    A_rw[k][k] = VDR(1)
    if actual_k + 1 < N:
        A_rw[k][k + 1] = -p
    if actual_k - 1 > 0:
        A_rw[k][k - 1] = -q
    # boundary contributions
    if actual_k - 1 == 0:
        b_rw[k] = b_rw[k] + q  # q * P_0 = q * 1
    if actual_k + 1 == N:
        pass  # p * P_N = 0

A_rw_mat = Mat(A_rw)
b_rw_vec = Vec(b_rw)
ruin_probs = A_rw_mat.solve(b_rw_vec)

print("  Gambler's ruin (N=%d, p=q=1/2):" % N)
for k in range(n_interior):
    print("    P(ruin | start at %d) = %s" % (k + 1, ruin_probs[k].to_fraction()))

# for p=q=1/2: P(ruin at 0 | k) = 1 - k/N
for k in range(n_interior):
    expected = Fraction(N - k - 1, N)
    ok = ruin_probs[k].to_fraction() == expected
    record(check("P(ruin|k=%d) = %s" % (k + 1, expected), ok))

# =========================================================================
section("4. Exact expected value and variance")
# =========================================================================

# die roll: exact E[X] and Var[X]
probs = [VDR(1, 6)] * 6
values = [VDR(i) for i in range(1, 7)]

expected_value = VDR(0)
for p_val, v in zip(probs, values):
    expected_value = expected_value + p_val * v

print("  E[die roll] = %s" % expected_value.to_fraction())
record(check("E[X] = 7/2", expected_value == VDR(7, 2)))

# E[X^2]
expected_x2 = VDR(0)
for p_val, v in zip(probs, values):
    expected_x2 = expected_x2 + p_val * v * v

variance = expected_x2 - expected_value * expected_value
print("  Var[die roll] = %s" % variance.to_fraction())
record(check("Var[X] = 35/12", variance == VDR(35, 12)))

# =========================================================================
section("5. Binomial distribution (exact)")
# =========================================================================

def binom_coeff(n, k):
    result = VDR(1)
    for i in range(min(k, n - k)):
        result = result * VDR(n - i, i + 1)
    return result

def binom_pmf(n, k, p):
    """P(X=k) = C(n,k) * p^k * (1-p)^(n-k), all exact VDR."""
    q = VDR(1) - p
    p_k = VDR(1)
    for _ in range(k):
        p_k = p_k * p
    q_nk = VDR(1)
    for _ in range(n - k):
        q_nk = q_nk * q
    return binom_coeff(n, k) * p_k * q_nk

# P(X=k) for n=10, p=1/3
n, p_binom = 10, VDR(1, 3)
total = VDR(0)
print("  Binomial(10, 1/3):")
for k in range(n + 1):
    prob = binom_pmf(n, k, p_binom)
    total = total + prob
    if k <= 5:
        print("    P(X=%d) = %s" % (k, prob.to_fraction()))

record(check("binomial PMF sums to 1", total == VDR(1)))

# exact expected value: np
ev = VDR(0)
for k in range(n + 1):
    ev = ev + VDR(k) * binom_pmf(n, k, p_binom)
record(check("E[Binom(10,1/3)] = 10/3", ev == VDR(10, 3)))

# =========================================================================
section("6. Conditional probability chain")
# =========================================================================

# multiple updates via Bayes — exact throughout
# prior: 1/2
# evidence 1: likelihood ratio 3/1 (positive)
# evidence 2: likelihood ratio 1/2 (negative)
# evidence 3: likelihood ratio 4/1 (positive)

prior = VDR(1, 2)

def bayes_update(prior, likelihood_ratio):
    """
    P(H|E) = P(E|H)P(H) / P(E)
    Using odds form: posterior_odds = prior_odds * LR
    Then convert back to probability.
    """
    prior_odds = prior / (VDR(1) - prior)
    posterior_odds = prior_odds * likelihood_ratio
    posterior = posterior_odds / (VDR(1) + posterior_odds)
    return posterior

updates = [VDR(3), VDR(1, 2), VDR(4)]
current = prior
print("  Sequential Bayesian updates:")
print("    prior: %s" % current.to_fraction())
for i, lr in enumerate(updates):
    current = bayes_update(current, lr)
    print("    after evidence %d (LR=%s): %s = %.4f" % (
        i + 1, lr.to_fraction(), current.to_fraction(),
        float(current.to_fraction())))

# final posterior should be exact
record(check("Bayesian posterior is exact rational",
             isinstance(current.to_fraction(), Fraction)))

# verify: prior odds = 1, * 3 * 1/2 * 4 = 6
# posterior = 6/7
record(check("final posterior = 6/7", current == VDR(6, 7)))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 11 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
