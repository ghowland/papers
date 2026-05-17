# code/test_nn.py
from __future__ import annotations

from fractions import Fraction

from vdr import VDR, Vec, Mat
from vdr.nn import Linear, ReLU, Sequential, MLP
from vdr.losses import mse, l1, hinge_binary, mse_grad
from vdr.optim import SGD, Momentum


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
    show("1. Linear forward")

    lin = Linear.from_ints(
        weight=[[1, 2], [3, 4]],
        bias=[5, 6],
        name="lin",
    )
    x = Vec.from_ints([1, 1])
    y = lin.forward(x)

    print("  y =", y.to_fractions())

    ok = check(y[0] == VDR(8), "row 0: 1*1 + 2*1 + 5 = 8")
    passed += ok
    failed += 1 - ok

    ok = check(y[1] == VDR(13), "row 1: 3*1 + 4*1 + 6 = 13")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("2. Linear backward")

    grad_out = Vec.from_ints([1, 2])
    grad_in = lin.backward(grad_out)

    print("  grad_in =", grad_in.to_fractions())
    print("  W.grad =", lin.W.grad.to_fractions())
    print("  b.grad =", lin.b.grad.to_fractions())

    ok = check(grad_in[0] == VDR(7), "grad_in[0] = 1*1 + 2*3 = 7")
    passed += ok
    failed += 1 - ok

    ok = check(grad_in[1] == VDR(10), "grad_in[1] = 1*2 + 2*4 = 10")
    passed += ok
    failed += 1 - ok

    ok = check(
        lin.W.grad.to_fractions() == [
            [Fraction(1, 1), Fraction(1, 1)],
            [Fraction(2, 1), Fraction(2, 1)],
        ],
        "weight gradient is outer(grad_out, x)",
    )
    passed += ok
    failed += 1 - ok

    ok = check(
        lin.b.grad.to_fractions() == [Fraction(1, 1), Fraction(2, 1)],
        "bias gradient equals grad_out",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("3. ReLU forward/backward")

    relu = ReLU()
    xr = Vec([VDR(-2), VDR(0), VDR(3)])
    yr = relu.forward(xr)
    gr = relu.backward(Vec.from_ints([5, 5, 5]))

    print("  relu(x) =", yr.to_fractions())
    print("  relu grad =", gr.to_fractions())

    ok = check(
        yr.to_fractions() == [Fraction(0, 1), Fraction(0, 1), Fraction(3, 1)],
        "relu forward correct",
    )
    passed += ok
    failed += 1 - ok

    ok = check(
        gr.to_fractions() == [Fraction(0, 1), Fraction(0, 1), Fraction(5, 1)],
        "relu backward mask correct",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("4. Sequential forward/backward")

    seq = Sequential(
        [
            Linear.from_ints([[1, 1], [1, -1]], [0, 0], name="l1"),
            ReLU(),
            Linear.from_ints([[2, 3]], [1], name="l2"),
        ]
    )

    xs = Vec.from_ints([2, 1])
    ys = seq.forward(xs)
    print("  output =", ys.to_fractions())

    ok = check(ys[0] == VDR(8), "seq forward output = 8")
    passed += ok
    failed += 1 - ok

    gback = seq.backward(Vec.from_ints([1]))
    print("  grad to input =", gback.to_fractions())

    ok = check(gback.dim == 2, "seq backward returns input-sized gradient")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("5. MSE loss")

    pred = Vec([VDR(3), VDR(5)])
    target = Vec([VDR(1), VDR(1)])
    loss = mse(pred, target)
    grad = mse_grad(pred, target)

    print("  mse =", loss.to_fraction())
    print("  mse_grad =", grad.to_fractions())

    ok = check(loss == VDR(10), "((3-1)^2 + (5-1)^2)/2 = 10")
    passed += ok
    failed += 1 - ok

    ok = check(
        grad.to_fractions() == [Fraction(2, 1), Fraction(4, 1)],
        "mse grad exact",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("6. L1 loss")

    pred = Vec([VDR(3), VDR(1, 2)])
    target = Vec([VDR(1), VDR(3, 2)])
    loss = l1(pred, target)

    print("  l1 =", loss.to_fraction())

    ok = check(loss == VDR(3, 2), "(|2| + |−1|)/2 = 3/2")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("7. hinge binary loss")

    h1 = hinge_binary(VDR(3, 2), 1)
    h2 = hinge_binary(VDR(-2), 1)
    h3 = hinge_binary(VDR(-3, 2), -1)

    print("  hinge(3/2, +1) =", h1.to_fraction())
    print("  hinge(-2, +1)  =", h2.to_fraction())
    print("  hinge(-3/2,-1) =", h3.to_fraction())

    ok = check(h1 == VDR(0), "positive margin gives zero hinge")
    passed += ok
    failed += 1 - ok

    ok = check(h2 == VDR(3), "hinge(-2,+1) = 1 - (-2) = 3")
    passed += ok
    failed += 1 - ok

    ok = check(h3 == VDR(0), "correct negative classification gives zero hinge")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("8. SGD step")

    lin = Linear.from_ints([[1, 2]], [3], name="sgd_lin")
    _ = lin.forward(Vec.from_ints([4, 5]))
    _ = lin.backward(Vec.from_ints([2]))

    opt = SGD(lin.parameters(), lr=VDR(1, 2))
    opt.step()

    print("  W after step =", lin.W.value.to_fractions())
    print("  b after step =", lin.b.value.to_fractions())

    ok = check(
        lin.W.value.to_fractions() == [[Fraction(-3, 1), Fraction(-3, 1)]],
        "SGD updated weights exactly",
    )
    passed += ok
    failed += 1 - ok

    ok = check(lin.b.value.to_fractions() == [Fraction(2, 1)], "SGD updated bias exactly")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("9. zero_grad")

    lin.zero_grad()

    ok = check(
        lin.W.grad.to_fractions() == [[Fraction(0, 1), Fraction(0, 1)]],
        "weight grad zeroed",
    )
    passed += ok
    failed += 1 - ok

    ok = check(lin.b.grad.to_fractions() == [Fraction(0, 1)], "bias grad zeroed")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("10. Momentum step")

    lin = Linear.from_ints([[2, 0]], [1], name="mom_lin")
    _ = lin.forward(Vec.from_ints([3, 4]))
    _ = lin.backward(Vec.from_ints([1]))

    opt = Momentum(lin.parameters(), lr=VDR(1, 1), beta=VDR(1, 2))
    opt.step()

    print("  W after momentum step 1 =", lin.W.value.to_fractions())
    print("  b after momentum step 1 =", lin.b.value.to_fractions())

    ok = check(
        lin.W.value.to_fractions() == [[Fraction(-1, 1), Fraction(-4, 1)]],
        "momentum step 1 weights exact",
    )
    passed += ok
    failed += 1 - ok

    ok = check(
        lin.b.value.to_fractions() == [Fraction(0, 1)],
        "momentum step 1 bias exact",
    )
    passed += ok
    failed += 1 - ok

    # second step with same gradient shape
    _ = lin.forward(Vec.from_ints([3, 4]))
    _ = lin.backward(Vec.from_ints([1]))
    opt.step()

    print("  W after momentum step 2 =", lin.W.value.to_fractions())
    print("  b after momentum step 2 =", lin.b.value.to_fractions())

    ok = check(
        lin.W.value.to_fractions() == [[Fraction(-11, 2), Fraction(-10, 1)]],
        "momentum accumulates exact velocity",
    )
    passed += ok
    failed += 1 - ok

    ok = check(
        lin.b.value.to_fractions() == [Fraction(-3, 2)],
        "momentum bias accumulates exactly",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("11. Tiny MLP forward")

    mlp = MLP(
        Linear.from_ints([[1, -1], [2, 1]], [0, 1], name="m1"),
        ReLU(),
        Linear.from_ints([[3, 4]], [2], name="m2"),
    )

    y = mlp.forward(Vec.from_ints([2, 1]))
    print("  mlp output =", y.to_fractions())

    ok = check(y[0] == VDR(24), "tiny MLP forward exact")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("12. Tiny MLP backward")

    grad_in = mlp.backward(Vec.from_ints([1]))
    print("  grad_in =", grad_in.to_fractions())

    ok = check(grad_in.dim == 2, "MLP backward returns 2-dim input gradient")
    passed += ok
    failed += 1 - ok

    ok = check(
        mlp.net.layers[2].W.grad.to_fractions() == [[Fraction(1, 1), Fraction(6, 1)]],
        "last layer weight grad exact",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    print("\n" + "=" * 50)
    print("NN batch 1 results: %d passed, %d failed" % (passed, failed))
    if failed == 0:
        print("ALL BATCH 1 TESTS PASSED")
    print("=" * 50)


if __name__ == "__main__":
    main()
    