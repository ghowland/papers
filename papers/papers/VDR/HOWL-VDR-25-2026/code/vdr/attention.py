# code/vdr/attention.py
from __future__ import annotations

from fractions import Fraction
from typing import List, Optional, Sequence, Union

from .vdr import VDR
from .linalg import Vec, Mat
from .softmax import softmax, softmax_surrogate_square


ScalarLike = Union[VDR, int, Fraction]


def _to_vdr(x: ScalarLike) -> VDR:
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR(int(x))


def attention_scores(Q: Sequence[Vec], K: Sequence[Vec]) -> List[Vec]:
    """
    Compute score matrix rows:
        scores[i][j] = Q_i dot K_j
    """
    if len(Q) == 0 or len(K) == 0:
        raise ValueError("Q and K must be nonempty")
    d = Q[0].dim
    for q in Q:
        if q.dim != d:
            raise ValueError("Q rows must have same dimension")
    for k in K:
        if k.dim != d:
            raise ValueError("K rows must have same dimension as Q rows")

    rows = []
    for i in range(len(Q)):
        row = []
        for j in range(len(K)):
            row.append(Q[i].dot(K[j]))
        rows.append(Vec(row))
    return rows


def causal_mask(n: int) -> List[List[bool]]:
    """
    True means masked.
    For row i, positions j > i are masked.
    """
    out = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(j > i)
        out.append(row)
    return out


def apply_boolean_mask(
    score_rows: Sequence[Vec],
    mask: Sequence[Sequence[bool]],
    masked_value: ScalarLike,
) -> List[Vec]:
    masked_value = _to_vdr(masked_value)
    if len(score_rows) != len(mask):
        raise ValueError("mask row count mismatch")
    out = []
    for i in range(len(score_rows)):
        row = score_rows[i]
        mr = mask[i]
        if len(mr) != row.dim:
            raise ValueError("mask width mismatch")
        out.append(Vec([masked_value if mr[j] else row[j] for j in range(row.dim)]))
    return out


def attention_weights(
    score_rows: Sequence[Vec],
    mode: str = "softmax",
    depth: int = 12,
) -> List[Vec]:
    out = []
    for row in score_rows:
        if mode == "softmax":
            out.append(softmax(row, depth=depth, stabilize=True))
        elif mode == "surrogate":
            out.append(softmax_surrogate_square(row))
        else:
            raise ValueError("unknown attention weight mode: %r" % mode)
    return out


def weighted_sum(weights: Vec, values: Sequence[Vec]) -> Vec:
    if len(values) == 0:
        raise ValueError("values must be nonempty")
    if weights.dim != len(values):
        raise ValueError("weights length must equal number of value vectors")
    d = values[0].dim
    for v in values:
        if v.dim != d:
            raise ValueError("value vectors must share dimension")

    total = [VDR(0) for _ in range(d)]
    for i in range(len(values)):
        for j in range(d):
            total[j] = total[j] + weights[i] * values[i][j]
    return Vec(total)


def attention_mix(weight_rows: Sequence[Vec], V: Sequence[Vec]) -> List[Vec]:
    return [weighted_sum(weight_rows[i], V) for i in range(len(weight_rows))]


def self_attention(
    X: Sequence[Vec],
    mode: str = "softmax",
    depth: int = 12,
    causal: bool = False,
    masked_value: ScalarLike = None,
):
    """
    Simple self-attention with Q=K=V=X.

    Returns:
      {
        "scores": score_rows,
        "weights": weight_rows,
        "output": mixed_rows,
      }
    """
    if len(X) == 0:
        raise ValueError("X must be nonempty")

    scores = attention_scores(X, X)

    if causal:
        if masked_value is None:
            masked_value = VDR(-3)
        scores_used = apply_boolean_mask(scores, causal_mask(len(X)), masked_value)
    else:
        scores_used = scores

    weights = attention_weights(scores_used, mode=mode, depth=depth)
    output = attention_mix(weights, X)

    return {
        "scores": scores_used,
        "weights": weights,
        "output": output,
    }
