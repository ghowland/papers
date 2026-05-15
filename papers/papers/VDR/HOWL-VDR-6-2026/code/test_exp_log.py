# code/test_exp_log.py
from __future__ import annotations

from fractions import Fraction

from vdr import VDR
from vdr.exp import exp_series, exp_range_reduced, exp_neg
from vdr.logarithm import log1p_series, log_series, log_ratio_near_one


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


def main():
    passed = 0
    failed = 0

    # ------------------------------------------------------------
    show("1. exp series basics")

    e0 = exp_series(VDR(0), depth=10)
    print("  exp_series(0,10) =", e0.to_fraction())
    ok = check(e0 == VDR(1), "exp_series(0) = 1")
    passed += ok
    failed += 1 - ok

    e1d3 = exp_series(VDR(1), depth=3)
    print("  exp_series(1,3) =", e1d3.to_fraction())
    ok = check(e1d3.to_fraction() == Fraction(8, 3), "exp_series(1,3) = 8/3")
    passed += ok
    failed += 1 - ok

    em1d4 = exp_series(VDR(-1), depth=4)
    print("  exp_series(-1,4) =", em1d4.to_fraction())
    ok = check(
        em1d4.to_fraction() == Fraction(3, 8),
        "exp_series(-1,4) = 1 - 1 + 1/2 - 1/6 + 1/24 = 3/8",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("2. exp monotonicity on small range")

    e0 = exp_series(VDR(0), depth=12)
    e1 = exp_series(VDR(1, 2), depth=12)
    e2 = exp_series(VDR(1), depth=12)

    print("  exp(0)   =", e0.to_fraction())
    print("  exp(1/2) =", e1.to_fraction())
    print("  exp(1)   =", e2.to_fraction())

    ok = check(e2 > e1 > e0, "exp series is monotone on tested range")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("3. exp negative helper")

    eneg = exp_neg(VDR(2), depth=10)
    direct = exp_series(VDR(-2), depth=10)

    print("  exp_neg(2) =", eneg.to_fraction())
    print("  exp_series(-2) =", direct.to_fraction())

    ok = check(eneg == direct, "exp_neg(2) matches exp_series(-2)")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("4. range reduced exp on integers")

    er1 = exp_range_reduced(VDR(1), depth=10)
    es1 = exp_series(VDR(1), depth=10)
    print("  exp_range_reduced(1) =", er1.to_fraction())
    print("  exp_series(1)        =", es1.to_fraction())

    ok = check(er1 == es1, "range reduced exp(1) matches direct")
    passed += ok
    failed += 1 - ok

    er2 = exp_range_reduced(VDR(2), depth=10)
    print("  exp_range_reduced(2) =", er2.to_fraction())
    ok = check(er2 > er1, "exp(2) > exp(1)")
    passed += ok
    failed += 1 - ok

    erm2 = exp_range_reduced(VDR(-2), depth=10)
    print("  exp_range_reduced(-2) =", erm2.to_fraction())
    ok = check(erm2 < VDR(1), "exp(-2) < 1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("5. log1p basics")

    l0 = log1p_series(VDR(0), depth=12)
    print("  log1p_series(0) =", l0.to_fraction())
    ok = check(l0 == VDR(0), "log1p(0) = 0")
    passed += ok
    failed += 1 - ok

    lh = log1p_series(VDR(1, 2), depth=4)
    print("  log1p_series(1/2,4) =", lh.to_fraction())

    expected = (
        Fraction(1, 2)
        - Fraction(1, 8)
        + Fraction(1, 24)
        - Fraction(1, 64)
    )
    ok = check(lh.to_fraction() == expected, "log1p series matches exact truncated sum")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("6. log near one")

    l1 = log_series(VDR(1), depth=12)
    print("  log_series(1) =", l1.to_fraction())
    ok = check(l1 == VDR(0), "log(1) = 0")
    passed += ok
    failed += 1 - ok

    l32 = log_series(VDR(3, 2), depth=10)
    l54 = log_series(VDR(5, 4), depth=10)

    print("  log(3/2) approx =", l32.to_fraction())
    print("  log(5/4) approx =", l54.to_fraction())

    ok = check(l32 > l54 > VDR(0), "log monotonic near one for tested values")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("7. log ratio near one")

    lr = log_ratio_near_one(VDR(3), VDR(2), depth=10)
    l32b = log_series(VDR(3, 2), depth=10)

    print("  log_ratio_near_one(3,2) =", lr.to_fraction())
    print("  log_series(3/2)         =", l32b.to_fraction())

    ok = check(lr == l32b, "log_ratio_near_one matches log_series(num/den)")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("8. exp-log local consistency near zero")

    # log(1+x) with x small, then exp of that approximate value
    x = VDR(1, 10)
    lx = log1p_series(x, depth=12)
    ex = exp_series(lx, depth=12)

    print("  x =", x.to_fraction())
    print("  log1p(x) =", lx.to_fraction())
    print("  exp(log1p(x)) =", ex.to_fraction())

    ok = check(ex > VDR(1), "exp(log1p(x)) > 1 for x > 0")
    passed += ok
    failed += 1 - ok

    ok = check(ex < VDR(6, 5), "exp(log1p(x)) remains in plausible local range")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("9. exact-fraction closure")

    vals = [
        exp_series(VDR(1, 3), depth=8),
        exp_series(VDR(-1, 2), depth=8),
        log1p_series(VDR(1, 4), depth=8),
        log_series(VDR(5, 4), depth=8),
    ]

    closed = True
    for v in vals:
        if not v.is_closed:
            closed = False
            break

    ok = check(closed, "all exp/log outputs are closed VDR fractions")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("10. exact reproducibility")

    a1 = exp_series(VDR(1, 2), depth=12)
    a2 = exp_series(VDR(1, 2), depth=12)
    b1 = log1p_series(VDR(1, 3), depth=12)
    b2 = log1p_series(VDR(1, 3), depth=12)

    ok = check(a1 == a2, "exp reproducible exactly")
    passed += ok
    failed += 1 - ok

    ok = check(b1 == b2, "log reproducible exactly")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    print("\n" + "=" * 50)
    print("Batch 2 results: %d passed, %d failed" % (passed, failed))
    if failed == 0:
        print("ALL BATCH 2 TESTS PASSED")
    print("=" * 50)


if __name__ == "__main__":
    main()
    