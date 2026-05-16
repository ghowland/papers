# code/vdr/optim.py
from __future__ import annotations

from fractions import Fraction
from typing import Dict, Iterable, List, Union

from .vdr import VDR


ScalarLike = Union[VDR, int, Fraction]


def _to_vdr(x: ScalarLike) -> VDR:
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR(int(x))


class SGD:
    def __init__(self, params, lr):
        self.params = list(params)
        self.lr = _to_vdr(lr)

    def zero_grad(self):
        for p in self.params:
            p.zero_grad()

    def step(self):
        for p in self.params:
            p.step(self.lr)


class Momentum:
    """
    Exact momentum optimizer:

        v <- beta * v + grad
        w <- w - lr * v

    with rational beta and lr.
    """
    def __init__(self, params, lr, beta=VDR(9, 10)):
        self.params = list(params)
        self.lr = _to_vdr(lr)
        self.beta = _to_vdr(beta)
        self.velocity = {}
        for p in self.params:
            self.velocity[id(p)] = p.zeros_like()

    def zero_grad(self):
        for p in self.params:
            p.zero_grad()

    def step(self):
        for p in self.params:
            key = id(p)
            v = self.velocity[key]
            v = p.combine_scaled(v, self.beta, p.grad_like(), VDR(1))
            self.velocity[key] = v
            p.apply_update(v, self.lr)
            