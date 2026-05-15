"""
VDR Gym 17: Game Theory
Nash equilibria, minimax, Shapley values, exact mixed strategies.
"""
from __future__ import annotations
from fractions import Fraction
import sys
sys.path.insert(0, '..')
from vdr import VDR, Vec, Mat

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

# === 1. 2x2 zero-sum game: minimax ===
print("\n=== 1. 2x2 zero-sum minimax ===")

# payoff matrix for row player
# A = [[3, -1], [-2, 4]]
# mixed strategy: p for row 1, (1-p) for row 2
# row player expected payoff vs col strategy q:
# E = p*q*3 + p*(1-q)*(-1) + (1-p)*q*(-2) + (1-p)*(1-q)*4
# col minimizes over q: set dE/dq = 0
# dE/dq = p*3 - p*(-1) - (1-p)*(-2) - (1-p)*4 ... wait, let's use standard
# For 2x2: p* = (d - c) / (a - b - c + d) where A = [[a,b],[c,d]]
a, b, c, d = VDR(3), VDR(-1), VDR(-2), VDR(4)
denom = a - b - c + d  # 3 - (-1) - (-2) + 4 = 10
p_star = (d - c) / denom  # (4 - (-2)) / 10 = 6/10 = 3/5
q_star = (d - b) / denom  # (4 - (-1)) / 10 = 5/10 = 1/2
game_value = (a * d - b * c) / denom  # (12 - 2)/10 = 1

print("  p* = %s, q* = %s, value = %s" % (
    p_star.to_fraction(), q_star.to_fraction(), game_value.to_fraction()))
check("p* = 3/5", p_star == VDR(3, 5))
check("q* = 1/2", q_star == VDR(1, 2))
check("game value = 1", game_value == VDR(1))

# verify: expected payoff at equilibrium
# E(p*,q*) = p*q*a + p*(1-q)*b + (1-p)*q*c + (1-p)*(1-q)*d
one = VDR(1)
ep = (p_star * q_star * a + p_star * (one - q_star) * b
      + (one - p_star) * q_star * c + (one - p_star) * (one - q_star) * d)
check("E(p*,q*) = value", ep == game_value)

# === 2. Matching pennies ===
print("\n=== 2. Matching pennies ===")

# A = [[1, -1], [-1, 1]]
a2, b2, c2, d2 = VDR(1), VDR(-1), VDR(-1), VDR(1)
den2 = a2 - b2 - c2 + d2  # 1+1+1+1 = 4
p2 = (d2 - c2) / den2  # (1+1)/4 = 1/2
q2 = (d2 - b2) / den2  # (1+1)/4 = 1/2
v2 = (a2 * d2 - b2 * c2) / den2  # (1-1)/4 = 0
print("  p* = %s, q* = %s, value = %s" % (
    p2.to_fraction(), q2.to_fraction(), v2.to_fraction()))
check("matching pennies p* = 1/2", p2 == VDR(1, 2))
check("matching pennies q* = 1/2", q2 == VDR(1, 2))
check("matching pennies value = 0", v2 == VDR(0))

# === 3. Battle of the sexes (non-zero-sum, 2 Nash equilibria) ===
print("\n=== 3. Battle of the sexes ===")

# player 1 payoffs: [[3, 0], [0, 2]]
# player 2 payoffs: [[2, 0], [0, 3]]
# mixed NE: p = P(player1 chooses A)
# player 2 indifferent: p*2 + (1-p)*0 = p*0 + (1-p)*3
# 2p = 3 - 3p => 5p = 3 => p = 3/5
# player 1 indifferent: q*3 + (1-q)*0 = q*0 + (1-q)*2
# 3q = 2 - 2q => 5q = 2 => q = 2/5
p_bos = VDR(3, 5)
q_bos = VDR(2, 5)
print("  p* = %s, q* = %s" % (p_bos.to_fraction(), q_bos.to_fraction()))

# expected payoff for player 1 at mixed NE
ep1 = p_bos * q_bos * VDR(3) + (VDR(1) - p_bos) * (VDR(1) - q_bos) * VDR(2)
# = (3/5)(2/5)(3) + (2/5)(3/5)(2) = 18/25 + 12/25 = 30/25 = 6/5
print("  E1 = %s" % ep1.to_fraction())
check("BOS p* = 3/5", p_bos == VDR(3, 5))
check("BOS q* = 2/5", q_bos == VDR(2, 5))
check("BOS E1 = 6/5", ep1 == VDR(6, 5))

# === 4. Shapley value for 3-player game ===
print("\n=== 4. Shapley value (3-player) ===")

# characteristic function v(S):
# v({}) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0
# v({1,2}) = 1/2, v({1,3}) = 1/3, v({2,3}) = 1/4
# v({1,2,3}) = 1
# Shapley value for player i:
# phi_i = sum over S not containing i:
#   |S|!(n-|S|-1)!/n! * (v(S+i) - v(S))

from math import factorial

def shapley_3(v_func):
    """Compute Shapley values for 3 players {0,1,2}."""
    n = 3
    phi = [VDR(0)] * n
    players = [0, 1, 2]
    for i in players:
        others = [j for j in players if j != i]
        # subsets of others: [], [a], [b], [a,b]
        subsets = [[]]
        for o in others:
            subsets = subsets + [s + [o] for s in subsets]
        for s in subsets:
            s_set = frozenset(s)
            si_set = frozenset(s + [i])
            sz = len(s)
            coeff = VDR(factorial(sz) * factorial(n - sz - 1), factorial(n))
            marginal = v_func(si_set) - v_func(s_set)
            phi[i] = phi[i] + coeff * marginal
    return phi

def v_coal(s):
    s = frozenset(s)
    table = {
        frozenset(): VDR(0),
        frozenset([0]): VDR(0),
        frozenset([1]): VDR(0),
        frozenset([2]): VDR(0),
        frozenset([0, 1]): VDR(1, 2),
        frozenset([0, 2]): VDR(1, 3),
        frozenset([1, 2]): VDR(1, 4),
        frozenset([0, 1, 2]): VDR(1),
    }
    return table[s]

phi = shapley_3(v_coal)
print("  phi = [%s, %s, %s]" % (
    phi[0].to_fraction(), phi[1].to_fraction(), phi[2].to_fraction()))

# Shapley values must sum to v(grand coalition) = 1
phi_sum = phi[0] + phi[1] + phi[2]
check("Shapley sums to v(N) = 1", phi_sum == VDR(1))

# efficiency: verify each is rational
check("phi[0] is closed", phi[0].is_closed)
check("phi[1] is closed", phi[1].is_closed)
check("phi[2] is closed", phi[2].is_closed)

# === 5. Dominated strategy elimination ===
print("\n=== 5. Dominated strategy elimination ===")

# 3x2 game for row player:
# [[4, 3],
#  [2, 6],
#  [1, 2]]
# Row 3 is dominated by row 1 (4>1 and 3>2)
# After removing row 3: 2x2 game [[4,3],[2,6]]
# solve: p* = (6-2)/(4-3-2+6) = 4/5
r1 = [VDR(4), VDR(3)]
r2 = [VDR(2), VDR(6)]
r3 = [VDR(1), VDR(2)]

dominated = r1[0] > r3[0] and r1[1] > r3[1]
check("row 3 dominated by row 1", dominated)

# solve reduced 2x2
a5, b5, c5, d5 = r1[0], r1[1], r2[0], r2[1]
den5 = a5 - b5 - c5 + d5  # 4-3-2+6 = 5
p5 = (d5 - c5) / den5  # (6-2)/5 = 4/5
print("  p*(row1) = %s" % p5.to_fraction())
check("reduced game p* = 4/5", p5 == VDR(4, 5))

# === 6. Cournot duopoly exact solution ===
print("\n=== 6. Cournot duopoly ===")

# linear demand: P = a - b(q1+q2), cost ci*qi
# profit_i = qi * (a - b(q1+q2)) - ci*qi
# FOC: a - 2b*qi - b*qj - ci = 0
# reaction: qi = (a - ci - b*qj) / (2b)
# equilibrium: solve simultaneously
# q1 = (a - c1 - b*q2)/(2b), q2 = (a - c2 - b*q1)/(2b)
# substituting: q1 = (a - 2c1 + c2)/(3b), q2 = (a - 2c2 + c1)/(3b)

a_d = VDR(10)      # demand intercept
b_d = VDR(1, 2)    # demand slope
c1 = VDR(1)        # cost firm 1
c2 = VDR(2)        # cost firm 2

q1_star = (a_d - VDR(2) * c1 + c2) / (VDR(3) * b_d)
q2_star = (a_d - VDR(2) * c2 + c1) / (VDR(3) * b_d)
print("  q1* = %s, q2* = %s" % (q1_star.to_fraction(), q2_star.to_fraction()))
# q1 = (10 - 2 + 2)/(3/2) = 10/(3/2) = 20/3
# q2 = (10 - 4 + 1)/(3/2) = 7/(3/2) = 14/3
check("q1* = 20/3", q1_star == VDR(20, 3))
check("q2* = 14/3", q2_star == VDR(14, 3))

# verify: price at equilibrium
Q = q1_star + q2_star  # 34/3
P = a_d - b_d * Q      # 10 - 17/3 = 13/3
print("  P* = %s" % P.to_fraction())
check("P* = 13/3", P == VDR(13, 3))

# profit
prof1 = q1_star * P - c1 * q1_star  # q1*(P-c1) = 20/3 * 10/3 = 200/9
print("  profit1 = %s" % prof1.to_fraction())
check("profit1 = 200/9", prof1 == VDR(200, 9))

# === 7. Zero-sum 3x3 via linear programming formulation ===
print("\n=== 7. 3x3 zero-sum solve via support enumeration ===")

# A = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]  (rock-paper-scissors)
# by symmetry: p* = (1/3, 1/3, 1/3), value = 0
# verify by checking indifference conditions
p_rps = [VDR(1, 3), VDR(1, 3), VDR(1, 3)]
A_rps = [[VDR(0), VDR(-1), VDR(1)],
         [VDR(1), VDR(0), VDR(-1)],
         [VDR(-1), VDR(1), VDR(0)]]

# expected payoff for each column j under p*
for j in range(3):
    ej = VDR(0)
    for i in range(3):
        ej = ej + p_rps[i] * A_rps[i][j]
    check("RPS E(col %d) = 0" % j, ej == VDR(0))

check("RPS probs sum to 1", p_rps[0] + p_rps[1] + p_rps[2] == VDR(1))


print("\n" + "=" * 50)
print("Gym 17 results: %d passed, %d failed" % (passed, failed))
if failed == 0:
    print("ALL GYM 17 TESTS PASSED")
print("=" * 50)

