# code/vdr/losses.py
from __future__ import annotations

from fractions import Fraction
from typing import Sequence, Union

from .vdr import VDR
from .linalg import Vec


ScalarLike = Union[VDR, int, Fraction]


def _to_vdr(x: ScalarLike) -> VDR:
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR(int(x))


def mse(pred: Vec, target: Vec) -> VDR:
    if pred.dim != target.dim:
        raise ValueError("pred and target must have same dimension")
    total = VDR(0)
    for i in range(pred.dim):
        d = pred[i] - target[i]
        total = total + d * d
    return (total / VDR(pred.dim)).normalize()


def l1(pred: Vec, target: Vec) -> VDR:
    if pred.dim != target.dim:
        raise ValueError("pred and target must have same dimension")
    total = VDR(0)
    for i in range(pred.dim):
        d = pred[i] - target[i]
        total = total + abs(d)
    return (total / VDR(pred.dim)).normalize()


def hinge_binary(score: VDR, label: int) -> VDR:
    """
    Binary hinge with labels in {-1, +1}:

        max(0, 1 - y * s)
    """
    if label not in (-1, 1):
        raise ValueError("label must be -1 or +1")
    y = VDR(label)
    margin = VDR(1) - y * score
    if margin > VDR(0):
        return margin.normalize()
    return VDR(0)


def mse_grad(pred: Vec, target: Vec) -> Vec:
    if pred.dim != target.dim:
        raise ValueError("pred and target must have same dimension")
    two = VDR(2)
    n = VDR(pred.dim)
    return Vec([((two * (pred[i] - target[i])) / n).normalize() for i in range(pred.dim)])
