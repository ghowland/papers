# code/vdr/exp.py
from __future__ import annotations

from fractions import Fraction
from typing import Union

from .vdr import VDR


ScalarLike = Union[VDR, int, Fraction]


def _to_vdr(x: ScalarLike) -> VDR:
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR(int(x))


def exp_series(x: ScalarLike, depth: int = 16) -> VDR:
    """
    Exact VDR fraction for the truncated series:

        exp(x) ~= sum_{k=0..depth} x^k / k!
    """
    x = _to_vdr(x)
    if depth < 0:
        raise ValueError("depth must be >= 0")

    total = VDR(1)
    term = VDR(1)

    for k in range(1, depth + 1):
        term = (term * x) / VDR(k)
        total = total + term

    return total.normalize()


def exp_range_reduced(x: ScalarLike, depth: int = 16) -> VDR:
    """
    Simple exact range reduction for integer arguments.

    If x is an integer n:
      - for n >= 0: exp(n) = exp(1)^n, approximated as [exp_series(1,depth)]^n
      - for n < 0:  exp(n) = 1 / exp(-n)

    Otherwise falls back to exp_series(x, depth).

    This is not the most numerically efficient method, but it gives a
    stronger exact-fraction path for larger integer magnitudes than a
    single Taylor expansion around zero.
    """
    x = _to_vdr(x)

    if x.is_closed and x.d == 1:
        n = x.v
        if n == 0:
            return VDR(1)
        e1 = exp_series(VDR(1), depth=depth)
        if n > 0:
            out = VDR(1)
            for _ in range(n):
                out = (out * e1).normalize()
            return out
        out = VDR(1)
        for _ in range(-n):
            out = (out * e1).normalize()
        return (VDR(1) / out).normalize()

    return exp_series(x, depth=depth)


def exp_neg(x: ScalarLike, depth: int = 16) -> VDR:
    """
    Convenience helper for exp(-x) using exact-fraction series.
    """
    return exp_series(-_to_vdr(x), depth=depth).normalize()
