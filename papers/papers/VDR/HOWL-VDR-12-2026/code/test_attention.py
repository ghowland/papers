# code/test_attention.py
from __future__ import annotations

from fractions import Fraction

from vdr import VDR, Vec
from vdr.tensor import (
    Tensor3,
    batched_matvec,
    masked_fill_rows,
    reduce_sum_rows,
    rowwise_add_bias,
)
from vdr.linalg import Mat
from vdr.attention import (
    apply_boolean_mask,
    attention_mix,
    attention_scores,
    attention_weights,
    causal_mask,
    self_attention,
    weighted_sum,
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
    show("1. Tensor3 construction")

    t = Tensor3(
        [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ]
    )
    print("  shape =", t.shape)
    print("  data =", t.to_fractions())

    ok = check(t.shape == (2, 2, 2), "Tensor3 shape = (2,2,2)")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("2. batched matvec")

    mats = [
        Mat.from_ints([[1, 2], [3, 4]]),
        Mat.from_ints([[2, 0], [0, 2]]),
    ]
    vecs = [
        Vec.from_ints([1, 1]),
        Vec.from_ints([3, 4]),
    ]
    out = batched_matvec(mats, vecs)
    print("  out[0] =", out[0].to_fractions())
    print("  out[1] =", out[1].to_fractions())

    ok = check(out[0].to_fractions() == [Fraction(3, 1), Fraction(7, 1)], "batched matvec row 0")
    passed += ok
    failed += 1 - ok

    ok = check(out[1].to_fractions() == [Fraction(6, 1), Fraction(8, 1)], "batched matvec row 1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("3. rowwise add bias")

    rows = [Vec.from_ints([1, 2]), Vec.from_ints([3, 4])]
    bias = Vec.from_ints([10, 20])
    rb = rowwise_add_bias(rows, bias)

    print("  row 0 =", rb[0].to_fractions())
    print("  row 1 =", rb[1].to_fractions())

    ok = check(rb[0].to_fractions() == [Fraction(11, 1), Fraction(22, 1)], "bias row 0")
    passed += ok
    failed += 1 - ok

    ok = check(rb[1].to_fractions() == [Fraction(13, 1), Fraction(24, 1)], "bias row 1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("4. masked fill rows")

    rows = [Vec.from_ints([1, 2, 3]), Vec.from_ints([4, 5, 6])]
    mask = [[False, True, False], [True, False, True]]
    mf = masked_fill_rows(rows, mask, VDR(-9))

    print("  masked row 0 =", mf[0].to_fractions())
    print("  masked row 1 =", mf[1].to_fractions())

    ok = check(
        mf[0].to_fractions() == [Fraction(1, 1), Fraction(-9, 1), Fraction(3, 1)],
        "masked fill row 0",
    )
    passed += ok
    failed += 1 - ok

    ok = check(
        mf[1].to_fractions() == [Fraction(-9, 1), Fraction(5, 1), Fraction(-9, 1)],
        "masked fill row 1",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("5. reduce sum rows")

    rs = reduce_sum_rows([Vec.from_ints([1, 2]), Vec.from_ints([3, 4]), Vec.from_ints([5, 6])])
    print("  reduced sum =", rs.to_fractions())

    ok = check(rs.to_fractions() == [Fraction(9, 1), Fraction(12, 1)], "row reduction exact")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("6. attention scores")

    Q = [Vec.from_ints([1, 0]), Vec.from_ints([0, 1])]
    K = [Vec.from_ints([1, 1]), Vec.from_ints([2, 0])]
    scores = attention_scores(Q, K)

    print("  score row 0 =", scores[0].to_fractions())
    print("  score row 1 =", scores[1].to_fractions())

    ok = check(scores[0].to_fractions() == [Fraction(1, 1), Fraction(2, 1)], "score row 0 exact")
    passed += ok
    failed += 1 - ok

    ok = check(scores[1].to_fractions() == [Fraction(1, 1), Fraction(0, 1)], "score row 1 exact")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("7. causal mask")

    cm = causal_mask(4)
    print("  causal mask =", cm)

    ok = check(cm[0] == [False, True, True, True], "causal row 0")
    passed += ok
    failed += 1 - ok

    ok = check(cm[2] == [False, False, False, True], "causal row 2")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("8. apply boolean mask")

    rows = [Vec.from_ints([1, 2, 3]), Vec.from_ints([4, 5, 6])]
    mask = [[False, True, True], [False, False, True]]
    am = apply_boolean_mask(rows, mask, VDR(-5))

    print("  masked row 0 =", am[0].to_fractions())
    print("  masked row 1 =", am[1].to_fractions())

    ok = check(
        am[0].to_fractions() == [Fraction(1, 1), Fraction(-5, 1), Fraction(-5, 1)],
        "boolean mask row 0",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("9. attention weights softmax")

    sw = attention_weights([Vec.from_ints([1, 2, 3])], mode="softmax", depth=12)[0]
    print("  softmax weights =", sw.to_fractions(), "sum =", vec_sum(sw).to_fraction())

    ok = check(vec_sum(sw) == VDR(1), "softmax attention weights sum to 1")
    passed += ok
    failed += 1 - ok

    ok = check(sw[2] > sw[1] > sw[0], "softmax attention weights preserve order")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("10. attention weights surrogate")

    rw = attention_weights([Vec.from_ints([1, 2, 3])], mode="surrogate")[0]
    print("  surrogate weights =", rw.to_fractions(), "sum =", vec_sum(rw).to_fraction())

    ok = check(vec_sum(rw) == VDR(1), "surrogate attention weights sum to 1")
    passed += ok
    failed += 1 - ok

    ok = check(rw[2] > rw[1] > rw[0], "surrogate attention weights preserve order")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("11. weighted sum")

    weights = Vec([VDR(1, 4), VDR(3, 4)])
    values = [Vec.from_ints([2, 0]), Vec.from_ints([6, 8])]
    ws = weighted_sum(weights, values)

    print("  weighted sum =", ws.to_fractions())

    ok = check(
        ws.to_fractions() == [Fraction(5, 1), Fraction(6, 1)],
        "weighted sum exact",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("12. attention mix")

    wrows = [
        Vec([VDR(1, 2), VDR(1, 2)]),
        Vec([VDR(1, 4), VDR(3, 4)]),
    ]
    Vrows = [Vec.from_ints([2, 0]), Vec.from_ints([6, 8])]
    mixed = attention_mix(wrows, Vrows)

    print("  mixed row 0 =", mixed[0].to_fractions())
    print("  mixed row 1 =", mixed[1].to_fractions())

    ok = check(
        mixed[0].to_fractions() == [Fraction(4, 1), Fraction(4, 1)],
        "attention mix row 0 exact",
    )
    passed += ok
    failed += 1 - ok

    ok = check(
        mixed[1].to_fractions() == [Fraction(5, 1), Fraction(6, 1)],
        "attention mix row 1 exact",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("13. self attention softmax")

    X = [
        Vec.from_ints([1, 0]),
        Vec.from_ints([0, 1]),
    ]
    attn = self_attention(X, mode="softmax", depth=12, causal=False)

    print("  scores row 0 =", attn["scores"][0].to_fractions())
    print("  weights row 0 =", attn["weights"][0].to_fractions())
    print("  output row 0 =", attn["output"][0].to_fractions())

    ok = check(len(attn["output"]) == 2, "self attention returns 2 output rows")
    passed += ok
    failed += 1 - ok

    ok = check(vec_sum(attn["weights"][0]) == VDR(1), "row 0 weights sum to 1")
    passed += ok
    failed += 1 - ok

    ok = check(vec_sum(attn["weights"][1]) == VDR(1), "row 1 weights sum to 1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("14. self attention surrogate")

    attn2 = self_attention(X, mode="surrogate", causal=False)

    print("  surrogate weights row 0 =", attn2["weights"][0].to_fractions())
    print("  surrogate weights row 1 =", attn2["weights"][1].to_fractions())

    ok = check(vec_sum(attn2["weights"][0]) == VDR(1), "surrogate row 0 weights sum to 1")
    passed += ok
    failed += 1 - ok

    ok = check(vec_sum(attn2["weights"][1]) == VDR(1), "surrogate row 1 weights sum to 1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("15. causal self attention")

    Xc = [
        Vec.from_ints([1, 0]),
        Vec.from_ints([0, 1]),
        Vec.from_ints([1, 1]),
    ]
    attnc = self_attention(Xc, mode="softmax", depth=12, causal=True, masked_value=VDR(-4))

    print("  causal scores row 0 =", attnc["scores"][0].to_fractions())
    print("  causal scores row 1 =", attnc["scores"][1].to_fractions())
    print("  causal scores row 2 =", attnc["scores"][2].to_fractions())

    ok = check(
        attnc["scores"][0].to_fractions() == [Fraction(1, 1), Fraction(-4, 1), Fraction(-4, 1)],
        "causal row 0 masking exact",
    )
    passed += ok
    failed += 1 - ok

    ok = check(
        attnc["scores"][1].to_fractions() == [Fraction(0, 1), Fraction(1, 1), Fraction(-4, 1)],
        "causal row 1 masking exact",
    )
    passed += ok
    failed += 1 - ok

    ok = check(vec_sum(attnc["weights"][0]) == VDR(1), "causal row 0 weights sum to 1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    print("\n" + "=" * 50)
    print("Batch 3 results: %d passed, %d failed" % (passed, failed))
    if failed == 0:
        print("ALL BATCH 3 TESTS PASSED")
    print("=" * 50)


if __name__ == "__main__":
    main()
    