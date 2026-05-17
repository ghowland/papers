# code/test_softmax.py
from __future__ import annotations

from fractions import Fraction

from vdr import VDR, Vec
from vdr.softmax import (
    exp_series,
    logsumexp,
    softmax,
    softmax_matrix_rows,
    softmax_surrogate_square,
)


def show(title):
    print("\n=== " + title + " ===")


def pass_msg(msg):
    print("  PASS:", msg)


def fail_msg(msg):
    print("  FAIL:", msg)


def check(cond, msg):
    if cond:
        pass_msg(msg)
        return 1
    fail_msg(msg)
    return 0


def vec_sum(v):
    total = VDR(0)
    for i in range(len(v)):
        total = total + v[i]
    return total


def all_positive(v):
    for i in range(len(v)):
        if not (v[i] > VDR(0)):
            return False
    return True


def all_nonnegative(v):
    for i in range(len(v)):
        if v[i] < VDR(0):
            return False
    return True


def fractions_of(v):
    return [v[i].to_fraction() for i in range(len(v))]


def main():
    passed = 0
    failed = 0

    # ------------------------------------------------------------
    show("1. exp series basics")

    e0 = exp_series(VDR(0), depth=10)
    print("  exp_series(0,10) =", e0)
    ok = check(e0 == VDR(1), "exp_series(0) = 1 exactly")
    passed += ok
    failed += 1 - ok

    e1d0 = exp_series(VDR(1), depth=0)
    print("  exp_series(1,0) =", e1d0)
    ok = check(e1d0 == VDR(1), "depth 0 returns 1")
    passed += ok
    failed += 1 - ok

    e1d3 = exp_series(VDR(1), depth=3)
    print("  exp_series(1,3) =", e1d3, "=", e1d3.to_fraction())
    ok = check(
        e1d3.to_fraction() == Fraction(8, 3),
        "exp_series(1,3) = 8/3",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("2. softmax sums to one")

    xs = Vec([VDR(1), VDR(2), VDR(3)])
    s = softmax(xs, depth=12)
    total = vec_sum(s)

    print("  softmax([1,2,3]) =", fractions_of(s))
    print("  sum =", total.to_fraction())

    ok = check(total == VDR(1), "softmax probabilities sum exactly to 1")
    passed += ok
    failed += 1 - ok

    ok = check(all_positive(s), "all softmax outputs are positive")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("3. equal logits give equal probabilities")

    eq = Vec([VDR(5), VDR(5), VDR(5), VDR(5)])
    se = softmax(eq, depth=10)
    print("  softmax([5,5,5,5]) =", fractions_of(se))

    ok = check(se[0] == se[1] == se[2] == se[3], "equal logits -> equal outputs")
    passed += ok
    failed += 1 - ok

    ok = check(se[0].to_fraction() == Fraction(1, 4), "equal logits -> 1/4 each")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("4. monotonic ordering")

    mono = Vec([VDR(-1), VDR(0), VDR(2)])
    sm = softmax(mono, depth=14)
    print("  softmax([-1,0,2]) =", fractions_of(sm))

    ok = check(sm[2] > sm[1] > sm[0], "larger logits produce larger probabilities")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("5. stabilization invariance")

    base = Vec([VDR(1), VDR(2), VDR(3)])
    shifted = Vec([VDR(11), VDR(12), VDR(13)])

    sb = softmax(base, depth=14, stabilize=True)
    ss = softmax(shifted, depth=14, stabilize=True)

    print("  softmax([1,2,3])      =", fractions_of(sb))
    print("  softmax([11,12,13])   =", fractions_of(ss))

    same = True
    for i in range(len(sb)):
        if sb[i] != ss[i]:
            same = False
            break

    ok = check(same, "softmax invariant under adding constant shift")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("6. unstabilized vs stabilized")

    s_stab = softmax(base, depth=14, stabilize=True)
    s_raw = softmax(base, depth=14, stabilize=False)

    print("  stabilized   =", fractions_of(s_stab))
    print("  unstabilized =", fractions_of(s_raw))

    ok = check(vec_sum(s_raw) == VDR(1), "unstabilized softmax still sums to 1")
    passed += ok
    failed += 1 - ok

    ok = check(all_positive(s_raw), "unstabilized softmax outputs are positive")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("7. logsumexp helper")

    shift, denom = logsumexp(xs, depth=12, stabilize=True)
    print("  shift =", shift)
    print("  denom =", denom, "=", denom.to_fraction())

    ok = check(shift == VDR(3), "logsumexp shift is max(logits)")
    passed += ok
    failed += 1 - ok

    ok = check(denom > VDR(0), "logsumexp denominator is positive")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("8. rational logits")

    xr = Vec([VDR(1, 2), VDR(1, 3), VDR(1, 4)])
    sr = softmax(xr, depth=16)
    print("  softmax([1/2,1/3,1/4]) =", fractions_of(sr))
    print("  sum =", vec_sum(sr).to_fraction())

    ok = check(vec_sum(sr) == VDR(1), "rational-logit softmax sums to 1")
    passed += ok
    failed += 1 - ok

    ok = check(all_positive(sr), "rational-logit softmax positive")
    passed += ok
    failed += 1 - ok

    ok = check(sr[0] > sr[1] > sr[2], "ordering preserved for rational logits")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("9. row-wise matrix softmax")

    rows = [
        Vec([VDR(1), VDR(2), VDR(3)]),
        Vec([VDR(0), VDR(0), VDR(0)]),
        Vec([VDR(2), VDR(1), VDR(0)]),
    ]
    out_rows = softmax_matrix_rows(rows, depth=12)

    for i, row in enumerate(out_rows):
        row_sum = vec_sum(row)
        print("  row", i, "=", fractions_of(row), "sum =", row_sum.to_fraction())
        ok = check(row_sum == VDR(1), "row %d sums to 1" % i)
        passed += ok
        failed += 1 - ok

    # ------------------------------------------------------------
    show("10. surrogate softmax")

    ssq = softmax_surrogate_square(xs)
    print("  surrogate softmax([1,2,3]) =", fractions_of(ssq))
    print("  sum =", vec_sum(ssq).to_fraction())

    ok = check(vec_sum(ssq) == VDR(1), "surrogate softmax sums exactly to 1")
    passed += ok
    failed += 1 - ok

    ok = check(all_nonnegative(ssq), "surrogate softmax outputs are nonnegative")
    passed += ok
    failed += 1 - ok

    ok = check(ssq[2] > ssq[1] > ssq[0], "surrogate ordering preserved")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("11. equal logits in surrogate softmax")

    seq2 = softmax_surrogate_square(eq)
    print("  surrogate softmax([5,5,5,5]) =", fractions_of(seq2))

    ok = check(
        seq2[0] == seq2[1] == seq2[2] == seq2[3],
        "surrogate equal logits -> equal outputs",
    )
    passed += ok
    failed += 1 - ok

    ok = check(seq2[0].to_fraction() == Fraction(1, 4), "surrogate equal logits -> 1/4 each")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("12. peakedness")

    xp = Vec([VDR(0), VDR(0), VDR(3)])
    sp = softmax(xp, depth=18)
    print("  softmax([0,0,10]) =", fractions_of(sp))

    ok = check(sp[2] > sp[1], "dominant logit has dominant probability (moderate gap)")
    passed += ok
    failed += 1 - ok

    ok = check(sp[2] > sp[0], "dominant logit beats first component (moderate gap)")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    print("\n" + "=" * 50)
    print("Softmax test results: %d passed, %d failed" % (passed, failed))
    if failed == 0:
        print("ALL SOFTMAX TESTS PASSED")
    print("=" * 50)


if __name__ == "__main__":
    main()
