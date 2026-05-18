# code/test_training_stack.py
from __future__ import annotations

from fractions import Fraction

from vdr import VDR, Vec
from vdr.nn import Linear, ReLU, Sequential
from vdr.optim import SGD
from vdr.datasets import (
    build_vocab,
    encode_tokens,
    decode_tokens,
    invert_vocab,
    sliding_windows,
    one_hot,
    batchify_windows,
    tiny_text_dataset,
)
from vdr.metrics import (
    exact_accuracy,
    argmax_vec,
    denominator_complexity_vec,
    denominator_complexity_mat,
    parameter_denominator_complexity,
)
from vdr.checkpoint import save_parameters, load_parameters, save_model
from vdr.trainer import train_step, train_epoch, evaluate_epoch, predict_class, evaluate_classification


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


def make_toy_regression_model():
    return Sequential(
        [
            Linear.from_fracs(
                weight=[[(1, 2), (1, 3)], [(-1, 4), (2, 5)]],
                bias=[(0, 1), (1, 10)],
                name="l1",
            ),
            ReLU(),
            Linear.from_fracs(
                weight=[[(3, 4), (1, 2)]],
                bias=[(0, 1)],
                name="l2",
            ),
        ]
    )


def make_toy_regression_dataset():
    return [
        (Vec.from_fracs([(1, 1), (0, 1)]), Vec.from_fracs([(1, 2)])),
        (Vec.from_fracs([(0, 1), (1, 1)]), Vec.from_fracs([(2, 5)])),
        (Vec.from_fracs([(1, 1), (1, 1)]), Vec.from_fracs([(3, 5)])),
    ]


def make_toy_class_model():
    return Sequential(
        [
            Linear.from_ints([[2, -1], [-1, 2]], [0, 0], name="clf"),
        ]
    )


def make_toy_class_dataset():
    return [
        (Vec.from_ints([1, 0]), 0),
        (Vec.from_ints([0, 1]), 1),
        (Vec.from_ints([2, 0]), 0),
        (Vec.from_ints([0, 2]), 1),
    ]


def main():
    passed = 0
    failed = 0

    # ------------------------------------------------------------
    show("1. vocab and encoding")

    toks = ["a", "b", "a", "c"]
    vocab = build_vocab(toks)
    ids = encode_tokens(toks, vocab)
    inv = invert_vocab(vocab)
    dec = decode_tokens(ids, inv)

    print("  vocab =", vocab)
    print("  ids =", ids)
    print("  decoded =", dec)

    ok = check(len(vocab) == 3, "vocab size = 3")
    passed += ok
    failed += 1 - ok

    ok = check(dec == toks, "decode(encode(tokens)) = tokens")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("2. sliding windows")

    windows = sliding_windows([0, 1, 2, 3, 4], seq_len=2)
    print("  windows =", windows)

    ok = check(
        windows == [([0, 1], 2), ([1, 2], 3), ([2, 3], 4)],
        "sliding windows exact",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("3. one-hot and batching")

    oh = one_hot(2, 5)
    batches = batchify_windows(windows, batch_size=2)

    print("  one_hot =", oh.to_fractions())
    print("  batches =", batches)

    ok = check(
        oh.to_fractions() == [Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)],
        "one_hot exact",
    )
    passed += ok
    failed += 1 - ok

    ok = check(len(batches) == 2, "batchify produces 2 batches")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("4. tiny text dataset")

    ds = tiny_text_dataset("a b a c a", seq_len=2)
    print("  ids =", ds["ids"])
    print("  windows =", ds["windows"])

    ok = check(len(ds["windows"]) == 3, "tiny_text_dataset windows count = 3")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("5. metrics basics")

    acc = exact_accuracy([0, 1, 1, 0], [0, 1, 0, 0])
    av = argmax_vec(Vec.from_fracs([(1, 3), (2, 3), (1, 2)]))

    print("  accuracy =", acc.to_fraction())
    print("  argmax =", av)

    ok = check(acc == VDR(3, 4), "exact_accuracy = 3/4")
    passed += ok
    failed += 1 - ok

    ok = check(av == 1, "argmax = index 1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("6. denominator complexity")

    v = Vec.from_fracs([(1, 2), (1, 3), (1, 4)])
    info_v = denominator_complexity_vec(v)

    model = make_toy_regression_model()
    info_p = parameter_denominator_complexity(model.parameters())

    print("  vec complexity =", info_v)
    print("  param complexity =", info_p)

    ok = check(info_v["max_d"] == 4, "vec max denominator = 4")
    passed += ok
    failed += 1 - ok

    ok = check(info_p["count"] > 0, "parameter complexity counts entries")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("7. single train step")

    model = make_toy_regression_model()
    opt = SGD(model.parameters(), lr=VDR(1, 10))
    x, y = make_toy_regression_dataset()[0]

    loss, pred = train_step(model, x, y, opt)

    print("  pred =", pred.to_fractions())
    print("  loss =", loss.to_fraction())

    ok = check(loss.is_closed, "train_step loss is closed")
    passed += ok
    failed += 1 - ok

    ok = check(pred.dim == 1, "prediction has dimension 1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("8. train epoch")

    model = make_toy_regression_model()
    opt = SGD(model.parameters(), lr=VDR(1, 20))
    data = make_toy_regression_dataset()

    before = evaluate_epoch(model, data)
    after = train_epoch(model, data, opt)

    print("  before avg_loss =", before["avg_loss"].to_fraction())
    print("  after avg_loss =", after["avg_loss"].to_fraction())

    ok = check(before["avg_loss"].is_closed, "before avg_loss closed")
    passed += ok
    failed += 1 - ok

    ok = check(after["avg_loss"].is_closed, "after avg_loss closed")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("9. evaluate epoch")

    model = make_toy_regression_model()
    data = make_toy_regression_dataset()
    ev = evaluate_epoch(model, data)

    print("  eval avg_loss =", ev["avg_loss"].to_fraction())
    print("  preds len =", len(ev["preds"]))

    ok = check(len(ev["preds"]) == len(data), "evaluate returns one pred per sample")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("10. classification helpers")

    clf = make_toy_class_model()
    class_data = make_toy_class_dataset()

    pred0 = predict_class(clf, class_data[0][0])
    evc = evaluate_classification(clf, class_data)

    print("  pred0 =", pred0)
    print("  pred_ids =", evc["pred_ids"])
    print("  accuracy =", evc["accuracy"].to_fraction())

    ok = check(pred0 == 0, "predict_class first sample = 0")
    passed += ok
    failed += 1 - ok

    ok = check(evc["accuracy"] == VDR(1), "toy classifier has exact accuracy 1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("11. checkpoint save/load parameters")

    model = make_toy_regression_model()
    saved = save_parameters(model.parameters())
    loaded = load_parameters(saved)

    print("  saved entries =", len(saved))
    print("  loaded entries =", len(loaded))

    ok = check(len(saved) == len(model.parameters()), "save_parameters count matches")
    passed += ok
    failed += 1 - ok

    ok = check(len(loaded) == len(saved), "load_parameters count matches")
    passed += ok
    failed += 1 - ok

    ok = check(
        loaded[0].value == model.parameters()[0].value,
        "loaded first parameter value matches original",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("12. checkpoint save model")

    model = make_toy_regression_model()
    sm = save_model(model)

    print("  save_model entries =", len(sm))

    ok = check(len(sm) == len(model.parameters()), "save_model serializes all params")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    print("\n" + "=" * 50)
    print("Batch 5 results: %d passed, %d failed" % (passed, failed))
    if failed == 0:
        print("ALL BATCH 5 TESTS PASSED")
    print("=" * 50)


if __name__ == "__main__":
    main()
    