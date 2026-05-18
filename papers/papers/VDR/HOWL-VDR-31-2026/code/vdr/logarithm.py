# code/vdr/logarithm.py
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


def log1p_series(x: ScalarLike, depth: int = 16) -> VDR:
    """
    Exact VDR fraction for truncated log(1+x):

        log(1+x) ~= sum_{k=1..depth} (-1)^(k+1) x^k / k

    Best behaved for |x| < 1, especially -1 < x <= 1.
    """
    x = _to_vdr(x)
    if depth <= 0:
        return VDR(0)

    total = VDR(0)
    power = VDR(1)

    for k in range(1, depth + 1):
        power = (power * x).normalize()
        term = (power / VDR(k)).normalize()
        if k % 2 == 1:
            total = total + term
        else:
            total = total - term

    return total.normalize()


def log_series(x: ScalarLike, depth: int = 16) -> VDR:
    """
    Exact-fraction logarithm approximation for positive x using:

        log(x) = log(1 + (x-1))

    This is exact for the chosen truncation and is best when x is
    reasonably close to 1.
    """
    x = _to_vdr(x)
    if x <= VDR(0):
        raise ValueError("log is defined here only for positive x")

    return log1p_series(x - VDR(1), depth=depth).normalize()


def log_ratio_near_one(num: ScalarLike, den: ScalarLike, depth: int = 16) -> VDR:
    """
    Approximate log(num/den) exactly as a fraction using:

        log(num/den) = log(1 + (num-den)/den)

    Best when num/den is close to 1.
    """
    num = _to_vdr(num)
    den = _to_vdr(den)
    if den == VDR(0):
        raise ZeroDivisionError("denominator is zero")
    ratio = (num / den).normalize()
    return log_series(ratio, depth=depth).normalize()
