# code/vdr/nn.py
from __future__ import annotations

from fractions import Fraction
from typing import List, Optional, Sequence, Union

from .vdr import VDR
from .linalg import Mat, Vec


ScalarLike = Union[VDR, int, Fraction]


def _to_vdr(x: ScalarLike) -> VDR:
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR(int(x))


class ParameterVec:
    def __init__(self, value: Vec, name: Optional[str] = None):
        self.value = value
        self.grad = Vec.zero(value.dim)
        self.name = name or "param_vec"

    def zero_grad(self):
        self.grad = Vec.zero(self.value.dim)

    def grad_like(self):
        return self.grad

    def zeros_like(self):
        return Vec.zero(self.value.dim)

    def step(self, lr: VDR):
        self.value = self.value - self.grad.scale(lr)

    def combine_scaled(self, a, a_scale, b, b_scale):
        return a.scale(a_scale) + b.scale(b_scale)

    def apply_update(self, update, lr):
        self.value = self.value - update.scale(lr)


class ParameterMat:
    def __init__(self, value: Mat, name: Optional[str] = None):
        self.value = value
        self.grad = Mat.zero(value.nrows, value.ncols)
        self.name = name or "param_mat"

    def zero_grad(self):
        self.grad = Mat.zero(self.value.nrows, self.value.ncols)

    def grad_like(self):
        return self.grad

    def zeros_like(self):
        return Mat.zero(self.value.nrows, self.value.ncols)

    def step(self, lr: VDR):
        self.value = self.value - self.grad.scale(lr)

    def combine_scaled(self, a, a_scale, b, b_scale):
        return a.scale(a_scale) + b.scale(b_scale)

    def apply_update(self, update, lr):
        self.value = self.value - update.scale(lr)


def _outer(a: Vec, b: Vec) -> Mat:
    rows = []
    for i in range(a.dim):
        row = []
        for j in range(b.dim):
            row.append(a[i] * b[j])
        rows.append(row)
    return Mat(rows)


def _relu_scalar(x: VDR) -> VDR:
    return x if x > VDR(0) else VDR(0)


def _relu_prime_scalar(x: VDR) -> VDR:
    return VDR(1) if x > VDR(0) else VDR(0)


class Module:
    def parameters(self):
        return []

    def zero_grad(self):
        for p in self.parameters():
            p.zero_grad()


class Linear(Module):
    def __init__(self, weight: Mat, bias: Vec, name: Optional[str] = None):
        if weight.nrows != bias.dim:
            raise ValueError("weight rows must equal bias dimension")
        self.W = ParameterMat(weight, name=(name or "linear") + ".W")
        self.b = ParameterVec(bias, name=(name or "linear") + ".b")
        self.name = name or "linear"

        self._last_input = None
        self._last_output = None

    @classmethod
    def from_ints(cls, weight, bias, name: Optional[str] = None):
        return cls(Mat.from_ints(weight), Vec.from_ints(bias), name=name)

    @classmethod
    def from_fracs(cls, weight, bias, name: Optional[str] = None):
        return cls(Mat.from_fracs(weight), Vec.from_fracs(bias), name=name)

    def parameters(self):
        return [self.W, self.b]

    def forward(self, x: Vec) -> Vec:
        if x.dim != self.W.value.ncols:
            raise ValueError("input dimension mismatch")
        self._last_input = x
        y = self.W.value.matvec(x) + self.b.value
        self._last_output = y
        return y

    def backward(self, grad_out: Vec) -> Vec:
        if self._last_input is None:
            raise RuntimeError("forward must be called before backward")
        if grad_out.dim != self.W.value.nrows:
            raise ValueError("grad_out dimension mismatch")

        x = self._last_input
        self.W.grad = _outer(grad_out, x)
        self.b.grad = grad_out
        grad_in = self.W.value.T.matvec(grad_out)
        return grad_in


class ReLU(Module):
    def __init__(self, name: Optional[str] = None):
        self.name = name or "relu"
        self._last_input = None

    def forward(self, x: Vec) -> Vec:
        self._last_input = x
        return Vec([_relu_scalar(x[i]) for i in range(x.dim)])

    def backward(self, grad_out: Vec) -> Vec:
        if self._last_input is None:
            raise RuntimeError("forward must be called before backward")
        x = self._last_input
        if grad_out.dim != x.dim:
            raise ValueError("grad_out dimension mismatch")
        return Vec(
            [(grad_out[i] * _relu_prime_scalar(x[i])).normalize() for i in range(x.dim)]
        )


class Sequential(Module):
    def __init__(self, layers: Sequence[Module]):
        self.layers = list(layers)

    def parameters(self):
        ps = []
        for layer in self.layers:
            ps.extend(layer.parameters())
        return ps

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


class MLP(Module):
    """
    Convenience wrapper:
      input -> Linear -> ReLU -> Linear
    """
    def __init__(self, l1: Linear, act: ReLU, l2: Linear):
        self.net = Sequential([l1, act, l2])

    def parameters(self):
        return self.net.parameters()

    def zero_grad(self):
        self.net.zero_grad()

    def forward(self, x: Vec) -> Vec:
        return self.net.forward(x)

    def backward(self, grad_out: Vec) -> Vec:
        return self.net.backward(grad_out)
    