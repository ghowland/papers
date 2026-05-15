from __future__ import annotations

from fractions import Fraction
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union

from vdr import Mat, VDR, Vec


ScalarLike = Union[VDR, int, Fraction]


def _to_vdr(x: ScalarLike) -> VDR:
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR.from_int(int(x))


def _zero() -> VDR:
    return VDR(0)


def _one() -> VDR:
    return VDR(1)


def _relu(x: VDR) -> VDR:
    return x if x >= VDR(0) else VDR(0)


def _relu_prime(x: VDR) -> VDR:
    return VDR(1) if x > VDR(0) else VDR(0)


def _mse_loss(pred: Vec, target: Vec) -> VDR:
    if pred.dim != target.dim:
        raise ValueError("pred and target must have same dimension")
    total = VDR(0)
    for i in range(pred.dim):
        d = pred[i] - target[i]
        total = total + d * d
    return total / VDR(pred.dim)


def _outer(a: Vec, b: Vec) -> Mat:
    rows = []
    for i in range(a.dim):
        row = []
        for j in range(b.dim):
            row.append(a[i] * b[j])
        rows.append(row)
    return Mat(rows)


def _vec_add(a: Vec, b: Vec) -> Vec:
    return a + b


def _vec_sub(a: Vec, b: Vec) -> Vec:
    return a - b


def _vec_hadamard(a: Vec, b: Vec) -> Vec:
    if a.dim != b.dim:
        raise ValueError("hadamard vectors must have same dimension")
    return Vec([a[i] * b[i] for i in range(a.dim)])


def _mat_sub(a: Mat, b: Mat) -> Mat:
    return a - b


def _scalar_vec_mul(s: ScalarLike, v: Vec) -> Vec:
    return v.scale(_to_vdr(s))


def _scalar_mat_mul(s: ScalarLike, m: Mat) -> Mat:
    return m.scale(_to_vdr(s))


class Linear:
    def __init__(self, weight: Mat, bias: Vec, name: Optional[str] = None):
        if weight.nrows != bias.dim:
            raise ValueError("weight rows must equal bias dimension")
        self.weight = weight
        self.bias = bias
        self.name = name or "linear"

        self._last_input: Optional[Vec] = None
        self._last_output: Optional[Vec] = None

        self.grad_w = Mat.zero(weight.nrows, weight.ncols)
        self.grad_b = Vec.zero(bias.dim)

    @classmethod
    def from_fracs(
        cls,
        weight: Sequence[Sequence[Tuple[int, int]]],
        bias: Sequence[Tuple[int, int]],
        name: Optional[str] = None,
    ) -> "Linear":
        return cls(Mat.from_fracs(weight), Vec.from_fracs(bias), name=name)

    @classmethod
    def from_ints(
        cls,
        weight: Sequence[Sequence[int]],
        bias: Sequence[int],
        name: Optional[str] = None,
    ) -> "Linear":
        return cls(Mat.from_ints(weight), Vec.from_ints(bias), name=name)

    def forward(self, x: Vec) -> Vec:
        if x.dim != self.weight.ncols:
            raise ValueError("input dimension mismatch")
        self._last_input = x
        y = self.weight.matvec(x) + self.bias
        self._last_output = y
        return y

    def backward(self, grad_out: Vec) -> Vec:
        if self._last_input is None:
            raise RuntimeError("forward must be called before backward")
        if grad_out.dim != self.weight.nrows:
            raise ValueError("grad_out dimension mismatch")

        x = self._last_input

        self.grad_w = _outer(grad_out, x)
        self.grad_b = grad_out

        grad_in = self.weight.T.matvec(grad_out)
        return grad_in

    def step(self, lr: ScalarLike) -> None:
        eta = _to_vdr(lr)
        self.weight = self.weight - self.grad_w.scale(eta)
        self.bias = self.bias - self.grad_b.scale(eta)

    def zero_grad(self) -> None:
        self.grad_w = Mat.zero(self.weight.nrows, self.weight.ncols)
        self.grad_b = Vec.zero(self.bias.dim)


class ReLU:
    def __init__(self, name: Optional[str] = None):
        self.name = name or "relu"
        self._last_input: Optional[Vec] = None

    def forward(self, x: Vec) -> Vec:
        self._last_input = x
        return Vec([_relu(x[i]) for i in range(x.dim)])

    def backward(self, grad_out: Vec) -> Vec:
        if self._last_input is None:
            raise RuntimeError("forward must be called before backward")
        x = self._last_input
        if grad_out.dim != x.dim:
            raise ValueError("grad_out dimension mismatch")
        mask = Vec([_relu_prime(x[i]) for i in range(x.dim)])
        return _vec_hadamard(grad_out, mask)

    def step(self, lr: ScalarLike) -> None:
        return None

    def zero_grad(self) -> None:
        return None


class Sequential:
    def __init__(self, layers: Sequence[object]):
        self.layers = list(layers)

    def forward(self, x: Vec) -> Vec:
        out = x
        for layer in self.layers:
            out = layer.forward(out)
        return out

    def backward(self, grad_out: Vec) -> Vec:
        grad = grad_out
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
        return grad

    def zero_grad(self) -> None:
        for layer in self.layers:
            if hasattr(layer, "zero_grad"):
                layer.zero_grad()

    def step(self, lr: ScalarLike) -> None:
        for layer in self.layers:
            if hasattr(layer, "step"):
                layer.step(lr)


def mse_grad(pred: Vec, target: Vec) -> Vec:
    if pred.dim != target.dim:
        raise ValueError("pred and target must have same dimension")
    n = VDR(pred.dim)
    two = VDR(2)
    return Vec([(two * (pred[i] - target[i])) / n for i in range(pred.dim)])


class SGD:
    def __init__(self, model: Sequential, lr: ScalarLike):
        self.model = model
        self.lr = _to_vdr(lr)

    def step(self) -> None:
        self.model.step(self.lr)

    def zero_grad(self) -> None:
        self.model.zero_grad()


def train_step(model: Sequential, x: Vec, y: Vec, opt: SGD) -> VDR:
    opt.zero_grad()
    pred = model.forward(x)
    loss = _mse_loss(pred, y)
    grad_loss = mse_grad(pred, y)
    model.backward(grad_loss)
    opt.step()
    return loss


def train_epoch(
    model: Sequential,
    dataset: Sequence[Tuple[Vec, Vec]],
    opt: SGD,
) -> VDR:
    total = VDR(0)
    for x, y in dataset:
        total = total + train_step(model, x, y, opt)
    return total / VDR(len(dataset))


def make_toy_regression_model() -> Sequential:
    # 2 -> 2 -> 1 exact network
    l1 = Linear.from_fracs(
        weight=[
            [(1, 2), (-1, 3)],
            [(2, 5), (1, 4)],
        ],
        bias=[(0, 1), (1, 10)],
        name="layer1",
    )
    a1 = ReLU()
    l2 = Linear.from_fracs(
        weight=[
            [(3, 4), (-2, 5)],
        ],
        bias=[(0, 1)],
        name="layer2",
    )
    return Sequential([l1, a1, l2])


def make_toy_dataset() -> List[Tuple[Vec, Vec]]:
    return [
        (
            Vec.from_fracs([(1, 1), (0, 1)]),
            Vec.from_fracs([(1, 2)]),
        ),
        (
            Vec.from_fracs([(0, 1), (1, 1)]),
            Vec.from_fracs([(1, 5)]),
        ),
        (
            Vec.from_fracs([(1, 1), (1, 1)]),
            Vec.from_fracs([(3, 5)]),
        ),
        (
            Vec.from_fracs([(2, 1), (1, 1)]),
            Vec.from_fracs([(4, 5)]),
        ),
    ]


def demo_train() -> None:
    model = make_toy_regression_model()
    data = make_toy_dataset()
    opt = SGD(model, lr=VDR(1, 20))

    print("Initial training:")
    for i, (x, y) in enumerate(data):
        pred = model.forward(x)
        loss = _mse_loss(pred, y)
        print(
            "sample",
            i,
            "pred=",
            pred.to_fractions(),
            "target=",
            y.to_fractions(),
            "loss=",
            loss.to_fraction(),
        )

    for epoch in range(5):
        avg_loss = train_epoch(model, data, opt)
        print("epoch", epoch + 1, "avg_loss =", avg_loss.to_fraction())

    print("\nFinal predictions:")
    for i, (x, y) in enumerate(data):
        pred = model.forward(x)
        loss = _mse_loss(pred, y)
        print(
            "sample",
            i,
            "pred=",
            pred.to_fractions(),
            "target=",
            y.to_fractions(),
            "loss=",
            loss.to_fraction(),
        )


if __name__ == "__main__":
    demo_train()

