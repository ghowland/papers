# code/test_autodiff.py
from __future__ import annotations

from fractions import Fraction

from vdr import VDR, Vec
from vdr.autodiff import (
    Node,
    dot_nodes,
    grad_of_vec,
    linear_node,
    mean_nodes,
    mse_loss,
    relu,
    sum_nodes,
    value_of_vec,
    zero_grads,
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


def main():
    passed = 0
    failed = 0

    # ------------------------------------------------------------
    show("1. derivative of x^2")

    x = Node(VDR(3), name="x")
    y = x * x
    y.backward()

    print("  y =", y.value, "grad_x =", x.grad)

    ok = check(y.value == VDR(9), "x^2 at x=3 is 9")
    passed += ok
    failed += 1 - ok

    ok = check(x.grad == VDR(6), "d(x^2)/dx at x=3 is 6")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("2. derivative of x^3")

    x = Node(VDR(2), name="x")
    y = x ** 3
    y.backward()

    print("  y =", y.value, "grad_x =", x.grad)

    ok = check(y.value == VDR(8), "x^3 at x=2 is 8")
    passed += ok
    failed += 1 - ok

    ok = check(x.grad == VDR(12), "d(x^3)/dx at x=2 is 12")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("3. affine expression")

    x = Node(VDR(5), name="x")
    y = Node(VDR(3)) * x + Node(VDR(2))
    y.backward()

    print("  y =", y.value, "grad_x =", x.grad)

    ok = check(y.value == VDR(17), "3x+2 at x=5 is 17")
    passed += ok
    failed += 1 - ok

    ok = check(x.grad == VDR(3), "d(3x+2)/dx = 3")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("4. product rule")

    x = Node(VDR(2), name="x")
    y = Node(VDR(7), name="y")
    z = x * y
    z.backward()

    print("  z =", z.value, "grad_x =", x.grad, "grad_y =", y.grad)

    ok = check(z.value == VDR(14), "xy = 14")
    passed += ok
    failed += 1 - ok

    ok = check(x.grad == VDR(7), "d(xy)/dx = y")
    passed += ok
    failed += 1 - ok

    ok = check(y.grad == VDR(2), "d(xy)/dy = x")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("5. quotient rule")

    x = Node(VDR(6), name="x")
    y = Node(VDR(3), name="y")
    z = x / y
    z.backward()

    print("  z =", z.value, "grad_x =", x.grad, "grad_y =", y.grad)

    ok = check(z.value == VDR(2), "x/y = 2")
    passed += ok
    failed += 1 - ok

    ok = check(x.grad == VDR(1, 3), "d(x/y)/dx = 1/y = 1/3")
    passed += ok
    failed += 1 - ok

    ok = check(y.grad == VDR(-2, 3), "d(x/y)/dy = -x/y^2 = -2/3")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("6. relu active branch")

    x = Node(VDR(4), name="x")
    y = relu(x)
    y.backward()

    print("  y =", y.value, "grad_x =", x.grad)

    ok = check(y.value == VDR(4), "relu(4) = 4")
    passed += ok
    failed += 1 - ok

    ok = check(x.grad == VDR(1), "relu'(4) = 1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("7. relu inactive branch")

    x = Node(VDR(-4), name="x")
    y = relu(x)
    y.backward()

    print("  y =", y.value, "grad_x =", x.grad)

    ok = check(y.value == VDR(0), "relu(-4) = 0")
    passed += ok
    failed += 1 - ok

    ok = check(x.grad == VDR(0), "relu'(-4) = 0")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("8. sum and mean")

    a = Node(VDR(1), name="a")
    b = Node(VDR(2), name="b")
    c = Node(VDR(3), name="c")

    s = sum_nodes([a, b, c])
    m = mean_nodes([a, b, c])
    m.backward()

    print("  sum =", s.value, "mean =", m.value)
    print("  grads =", a.grad, b.grad, c.grad)

    ok = check(s.value == VDR(6), "sum = 6")
    passed += ok
    failed += 1 - ok

    ok = check(m.value == VDR(2), "mean = 2")
    passed += ok
    failed += 1 - ok

    ok = check(a.grad == VDR(1, 3), "d mean / da = 1/3")
    passed += ok
    failed += 1 - ok

    ok = check(b.grad == VDR(1, 3), "d mean / db = 1/3")
    passed += ok
    failed += 1 - ok

    ok = check(c.grad == VDR(1, 3), "d mean / dc = 1/3")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("9. dot product")

    x1 = Node(VDR(1), name="x1")
    x2 = Node(VDR(2), name="x2")
    y = dot_nodes([x1, x2], [Node(VDR(3)), Node(VDR(4))])
    y.backward()

    print("  dot =", y.value, "grads =", x1.grad, x2.grad)

    ok = check(y.value == VDR(11), "dot = 1*3 + 2*4 = 11")
    passed += ok
    failed += 1 - ok

    ok = check(x1.grad == VDR(3), "d dot / dx1 = 3")
    passed += ok
    failed += 1 - ok

    ok = check(x2.grad == VDR(4), "d dot / dx2 = 4")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("10. linear node")

    x1 = Node(VDR(2), name="x1")
    x2 = Node(VDR(3), name="x2")
    y = linear_node([VDR(5), VDR(-1)], [x1, x2], VDR(4))
    y.backward()

    print("  y =", y.value, "grads =", x1.grad, x2.grad)

    ok = check(y.value == VDR(11), "5*2 + (-1)*3 + 4 = 11")
    passed += ok
    failed += 1 - ok

    ok = check(x1.grad == VDR(5), "d y / dx1 = 5")
    passed += ok
    failed += 1 - ok

    ok = check(x2.grad == VDR(-1), "d y / dx2 = -1")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("11. mse loss scalar")

    p = Node(VDR(3), name="pred")
    loss = mse_loss([p], [VDR(1)])
    loss.backward()

    print("  loss =", loss.value, "grad_pred =", p.grad)

    ok = check(loss.value == VDR(4), "(3-1)^2 = 4")
    passed += ok
    failed += 1 - ok

    ok = check(p.grad == VDR(4), "d/dp (p-1)^2 at p=3 is 4")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("12. mse loss vector")

    p1 = Node(VDR(2), name="p1")
    p2 = Node(VDR(5), name="p2")
    loss = mse_loss([p1, p2], [VDR(1), VDR(1)])
    loss.backward()

    print("  loss =", loss.value)
    print("  grads =", p1.grad, p2.grad)

    ok = check(loss.value == VDR(17, 2), "((2-1)^2 + (5-1)^2)/2 = 17/2")
    passed += ok
    failed += 1 - ok

    ok = check(p1.grad == VDR(1), "grad p1 = 2*(2-1)/2 = 1")
    passed += ok
    failed += 1 - ok

    ok = check(p2.grad == VDR(4), "grad p2 = 2*(5-1)/2 = 4")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("13. chain rule composite")

    x = Node(VDR(2), name="x")
    y = ((x * x) + VDR(1)) * x
    y.backward()

    print("  y =", y.value, "grad_x =", x.grad)

    ok = check(y.value == VDR(10), "(x^2+1)x at x=2 is 10")
    passed += ok
    failed += 1 - ok

    ok = check(x.grad == VDR(13), "d[(x^2+1)x]/dx at x=2 is 13")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("14. zero_grads")

    x = Node(VDR(2), name="x")
    y = x * x
    y.backward()

    ok = check(x.grad == VDR(4), "grad before zero_grads is 4")
    passed += ok
    failed += 1 - ok

    zero_grads([x, y])

    ok = check(x.grad == VDR(0), "x grad zeroed")
    passed += ok
    failed += 1 - ok

    ok = check(y.grad == VDR(0), "y grad zeroed")
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    show("15. vector extraction helpers")

    a = Node(VDR(1, 2), name="a")
    b = Node(VDR(2, 3), name="b")
    c = a + b
    c.backward()

    vals = value_of_vec([a, b, c])
    grads = grad_of_vec([a, b, c])

    print("  values =", vals.to_fractions())
    print("  grads =", grads.to_fractions())

    ok = check(
        vals.to_fractions() == [Fraction(1, 2), Fraction(2, 3), Fraction(7, 6)],
        "value_of_vec extracts exact values",
    )
    passed += ok
    failed += 1 - ok

    ok = check(
        grads.to_fractions() == [Fraction(1, 1), Fraction(1, 1), Fraction(1, 1)],
        "grad_of_vec extracts exact grads",
    )
    passed += ok
    failed += 1 - ok

    # ------------------------------------------------------------
    print("\n" + "=" * 50)
    print("Autodiff test results: %d passed, %d failed" % (passed, failed))
    if failed == 0:
        print("ALL AUTODIFF TESTS PASSED")
    print("=" * 50)


if __name__ == "__main__":
    main()
