# code/test_sampling_init.py
from __future__ import annotations

from fractions import Fraction

from vdr import VDR, Vec
from vdr.rng import VDRRandom
from vdr.sampling import (
    cdf_from_probs,
    categorical_sample,
    top_k_probs,
    nucleus_probs,
)
from vdr.init import (
    rational_uniform_vec,
    rational_uniform_mat,
    xavier_like_mat,
    zero_bias,
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


def main():
    passed = 0
    failed = 0

    # ------------------------------------------------------------
    show("1. RNG reproducibility")

    r1 = VDRRandom(seed=123)
    r2 = VDRRandom(seed=123)

    seq1 = [r1.next_int() for _ in range(5)]
    seq2 = [r2.next_int() for _ in range(5)]

    print("  seq1 =", seq1)
    print("  seq2 =", seq2)

    ok = check(seq1 == seq2, "same seed gives identical integer stream")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("2. rand_fraction exact range")

    r = VDRRandom(seed=7)
    x = r.rand_fraction()
    print("  rand_fraction =", x.to_fraction())

    ok = check(x >= VDR(0), "rand_fraction >= 0")
    passed += ok
    failed += 1 - ok

    ok = check(x < VDR(1), "rand_fraction < 1")
    passed += ok
    failed += 1 - ok

    ok = check(x.is_closed, "rand_fraction is closed VDR")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("3. shuffle reproducibility")

    xs1 = [0, 1, 2, 3, 4, 5]
    xs2 = [0, 1, 2, 3, 4, 5]
    r1 = VDRRandom(seed=99)
    r2 = VDRRandom(seed=99)

    r1.shuffle_in_place(xs1)
    r2.shuffle_in_place(xs2)

    print("  shuffled1 =", xs1)
    print("  shuffled2 =", xs2)

    ok = check(xs1 == xs2, "shuffle is reproducible")
    passed += ok
    failed += 1 - ok

    ok = check(sorted(xs1) == [0, 1, 2, 3, 4, 5], "shuffle preserves elements")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("4. permutation")

    r = VDRRandom(seed=5)
    p = r.permutation(6)
    print("  permutation =", p)

    ok = check(sorted(p) == [0, 1, 2, 3, 4, 5], "permutation contains all indices")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("5. CDF construction")

    probs = Vec([VDR(1, 4), VDR(1, 2), VDR(1, 4)])
    cdf = cdf_from_probs(probs)
    print("  cdf =", cdf.to_fractions())

    ok = check(
        cdf.to_fractions() == [Fraction(1, 4), Fraction(3, 4), Fraction(1, 1)],
        "CDF exact",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("6. categorical sample exact one-hot cases")

    rng = VDRRandom(seed=1)
    p0 = Vec([VDR(1), VDR(0), VDR(0)])
    p2 = Vec([VDR(0), VDR(0), VDR(1)])

    s0 = categorical_sample(p0, rng)
    s2 = categorical_sample(p2, rng)

    print("  sample from [1,0,0] =", s0)
    print("  sample from [0,0,1] =", s2)

    ok = check(s0 == 0, "categorical one-hot picks 0")
    passed += ok
    failed += 1 - ok

    ok = check(s2 == 2, "categorical one-hot picks 2")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("7. categorical sample reproducibility")

    probs = Vec([VDR(1, 4), VDR(1, 2), VDR(1, 4)])
    r1 = VDRRandom(seed=42)
    r2 = VDRRandom(seed=42)

    seq1 = [categorical_sample(probs, r1) for _ in range(10)]
    seq2 = [categorical_sample(probs, r2) for _ in range(10)]

    print("  seq1 =", seq1)
    print("  seq2 =", seq2)

    ok = check(seq1 == seq2, "categorical sampling reproducible by seed")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("8. top-k probabilities")

    probs = Vec([VDR(1, 10), VDR(2, 10), VDR(3, 10), VDR(4, 10)])
    tk = top_k_probs(probs, 2)
    print("  top-k =", tk.to_fractions())
    print("  sum =", vec_sum(tk).to_fraction())

    ok = check(vec_sum(tk) == VDR(1), "top-k renormalizes to 1")
    passed += ok
    failed += 1 - ok

    ok = check(
        tk.to_fractions() == [Fraction(0, 1), Fraction(0, 1), Fraction(3, 7), Fraction(4, 7)],
        "top-2 keeps largest probabilities exactly",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("9. nucleus probabilities")

    probs = Vec([VDR(1, 2), VDR(1, 5), VDR(1, 5), VDR(1, 10)])
    nuc = nucleus_probs(probs, VDR(3, 5))
    print("  nucleus =", nuc.to_fractions())
    print("  sum =", vec_sum(nuc).to_fraction())

    ok = check(vec_sum(nuc) == VDR(1), "nucleus renormalizes to 1")
    passed += ok
    failed += 1 - ok

    ok = check(
        nuc.to_fractions() == [Fraction(5, 7), Fraction(2, 7), Fraction(0, 1), Fraction(0, 1)],
        "nucleus keeps minimal prefix exceeding threshold",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("10. rational uniform vec reproducibility")

    v1 = rational_uniform_vec(5, denom=20, seed=11, lo=-1, hi=1)
    v2 = rational_uniform_vec(5, denom=20, seed=11, lo=-1, hi=1)

    print("  v1 =", v1.to_fractions())
    print("  v2 =", v2.to_fractions())

    ok = check(v1 == v2, "rational_uniform_vec reproducible")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("11. rational uniform mat reproducibility")

    m1 = rational_uniform_mat(2, 3, denom=20, seed=17, lo=-1, hi=1)
    m2 = rational_uniform_mat(2, 3, denom=20, seed=17, lo=-1, hi=1)

    print("  m1 =", m1.to_fractions())
    print("  m2 =", m2.to_fractions())

    ok = check(m1 == m2, "rational_uniform_mat reproducible")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("12. xavier-like matrix exactness")

    xm = xavier_like_mat(2, 4, denom=20, seed=3)
    print("  xavier-like =", xm.to_fractions())

    all_closed = True
    for i in range(xm.nrows):
        for j in range(xm.ncols):
            if not xm[i, j].is_closed:
                all_closed = False

    ok = check(all_closed, "xavier-like entries are closed VDR fractions")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("13. zero bias")

    zb = zero_bias(4)
    print("  zero_bias =", zb.to_fractions())

    ok = check(
        zb.to_fractions() == [Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)],
        "zero_bias exact",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    print("\n" + "=" * 50)
    print("Batch 4 results: %d passed, %d failed" % (passed, failed))
    if failed == 0:
        print("ALL BATCH 4 TESTS PASSED")
    print("=" * 50)


if __name__ == "__main__":
    main()
    