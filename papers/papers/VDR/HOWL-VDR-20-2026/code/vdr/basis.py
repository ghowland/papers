# code/vdr/basis.py
from __future__ import annotations

from fractions import Fraction
from typing import Sequence, Union

from .vdr import VDR
from .linalg import Vec, Mat


ScalarLike = Union[VDR, int, Fraction]


def _to_vdr(x: ScalarLike) -> VDR:
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR(int(x))


def q_basis_denominator(bits: int) -> int:
    if bits <= 0:
        raise ValueError("bits must be > 0")
    return 1 << bits


def to_qbasis(x: ScalarLike, bits: int) -> VDR:
    """
    Embed x into common denominator 2^bits by exact flooring-free
    nearest rational rounding via Fraction.

    Result is a closed VDR [p, 2^bits, 0].
    """
    x = _to_vdr(x)
    q = q_basis_denominator(bits)
    frac = x.to_fraction()
    p = int(round(frac * q))
    return VDR(p, q).normalize()


def vec_to_qbasis(v: Vec, bits: int) -> Vec:
    return Vec([to_qbasis(v[i], bits) for i in range(v.dim)])


def mat_to_qbasis(m: Mat, bits: int) -> Mat:
    rows = []
    for i in range(m.nrows):
        row = []
        for j in range(m.ncols):
            row.append(to_qbasis(m[i, j], bits))
        rows.append(row)
    return Mat(rows)


def qb_rebase_add(a: VDR, b: VDR, bits: int) -> VDR:
    """
    Convert both to Q-basis and add.
    """
    qa = to_qbasis(a, bits)
    qb = to_qbasis(b, bits)
    return (qa + qb).normalize()


def qb_rebase_mul(a: VDR, b: VDR, bits: int) -> VDR:
    """
    Multiply two values and return result rebased into Q-basis.
    """
    return to_qbasis(_to_vdr(a) * _to_vdr(b), bits)
