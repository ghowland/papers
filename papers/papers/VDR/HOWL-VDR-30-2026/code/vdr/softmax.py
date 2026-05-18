# code/vdr/softmax.py
from __future__ import annotations

from fractions import Fraction
from typing import Iterable, List, Sequence, Union

from .vdr import VDR
from .linalg import Vec


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

    The result is exact as a fraction for the chosen truncation depth.
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


def _vec_max(v: Vec) -> VDR:
    if len(v) == 0:
        raise ValueError("vector must be nonempty")
    m = v[0]
    for i in range(1, len(v)):
        if v[i] > m:
            m = v[i]
    return m


def softmax(
    logits: Union[Vec, Sequence[ScalarLike]],
    depth: int = 16,
    stabilize: bool = True,
) -> Vec:
    """
    VDR softmax using exact-fraction truncated exp series.

    Steps:
      1. optional max-shift stabilization
      2. exact fractional exp partial sums
      3. exact normalization

    Returns a Vec of closed VDR objects summing exactly to 1
    in the implemented truncated-exp representation.
    """
    if not isinstance(logits, Vec):
        logits = Vec([_to_vdr(x) for x in logits])

    if len(logits) == 0:
        raise ValueError("softmax requires nonempty vector")

    if stabilize:
        shift = _vec_max(logits)
        shifted = Vec([logits[i] - shift for i in range(len(logits))])
    else:
        shifted = logits

    exps = Vec([exp_series(shifted[i], depth=depth) for i in range(len(shifted))])

    denom = VDR(0)
    for i in range(len(exps)):
        denom = denom + exps[i]

    if denom == VDR(0):
        raise ZeroDivisionError("softmax denominator is zero")

    return Vec([(exps[i] / denom).normalize() for i in range(len(exps))])


def logsumexp(
    logits: Union[Vec, Sequence[ScalarLike]],
    depth: int = 16,
    stabilize: bool = True,
):
    """
    VDR helper returning exp-space logsumexp components.

    If stabilize=True, returns:
        (shift, denom)

    meaning:
        sum_j exp(logits_j) ~= exp(shift) * denom

    where denom is the exact VDR fraction from the chosen truncation.
    """
    if not isinstance(logits, Vec):
        logits = Vec([_to_vdr(x) for x in logits])

    if len(logits) == 0:
        raise ValueError("logsumexp requires nonempty vector")

    if stabilize:
        shift = _vec_max(logits)
        shifted = Vec([logits[i] - shift for i in range(len(logits))])
    else:
        shift = VDR(0)
        shifted = logits

    denom = VDR(0)
    for i in range(len(shifted)):
        denom = denom + exp_series(shifted[i], depth=depth)

    return shift, denom.normalize()


def softmax_matrix_rows(
    rows: Sequence[Union[Vec, Sequence[ScalarLike]]],
    depth: int = 16,
    stabilize: bool = True,
) -> List[Vec]:
    """
    Apply softmax row-wise to a list of rows.
    """
    return [softmax(row, depth=depth, stabilize=stabilize) for row in rows]


def softmax_surrogate_square(
    logits: Union[Vec, Sequence[ScalarLike]],
    c: ScalarLike = None,
) -> Vec:
    """
    Fully rational surrogate softmax:

        s_i = (z_i - m + c)^2 / sum_j (z_j - m + c)^2

    Default c = 4.
    """
    if not isinstance(logits, Vec):
        logits = Vec([_to_vdr(x) for x in logits])

    if len(logits) == 0:
        raise ValueError("softmax requires nonempty vector")

    if c is None:
        c = VDR(4)
    else:
        c = _to_vdr(c)

    m = _vec_max(logits)

    vals = []
    for i in range(len(logits)):
        t = logits[i] - m + c
        vals.append((t * t).normalize())

    denom = VDR(0)
    for v in vals:
        denom = denom + v

    if denom == VDR(0):
        raise ZeroDivisionError("surrogate softmax denominator is zero")

    return Vec([(v / denom).normalize() for v in vals])


if __name__ == "__main__":
    xs = Vec([VDR(1), VDR(2), VDR(3)])

    s = softmax(xs, depth=12)
    print("softmax([1,2,3]) =", s.to_fractions())

    total = VDR(0)
    for i in range(len(s)):
        total = total + s[i]
    print("sum =", total.to_fraction())

    ss = softmax_surrogate_square(xs)
    print("surrogate softmax([1,2,3]) =", ss.to_fractions())

    total2 = VDR(0)
    for i in range(len(ss)):
        total2 = total2 + ss[i]
    print("surrogate sum =", total2.to_fraction())
    