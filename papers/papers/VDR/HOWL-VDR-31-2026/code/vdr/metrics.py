# code/vdr/metrics.py
from __future__ import annotations

from fractions import Fraction
from typing import Sequence

from .vdr import VDR
from .linalg import Vec, Mat


def exact_accuracy(pred_ids: Sequence[int], target_ids: Sequence[int]) -> VDR:
    if len(pred_ids) != len(target_ids):
        raise ValueError("pred_ids and target_ids must have same length")
    if len(pred_ids) == 0:
        raise ValueError("inputs must be nonempty")
    correct = 0
    for p, t in zip(pred_ids, target_ids):
        if p == t:
            correct += 1
    return VDR(correct, len(pred_ids)).normalize()


def argmax_vec(v: Vec) -> int:
    if len(v) == 0:
        raise ValueError("argmax_vec requires nonempty vector")
    idx = 0
    best = v[0]
    for i in range(1, len(v)):
        if v[i] > best:
            best = v[i]
            idx = i
    return idx


def denominator_complexity_vec(v: Vec):
    denoms = [abs(v[i].d) for i in range(v.dim)]
    return {
        "max_d": max(denoms),
        "sum_d": sum(denoms),
        "count": len(denoms),
    }


def denominator_complexity_mat(m: Mat):
    denoms = []
    for i in range(m.nrows):
        for j in range(m.ncols):
            denoms.append(abs(m[i, j].d))
    return {
        "max_d": max(denoms),
        "sum_d": sum(denoms),
        "count": len(denoms),
    }


def parameter_denominator_complexity(params):
    max_d = 0
    sum_d = 0
    count = 0
    for p in params:
        value = p.value
        if isinstance(value, Vec):
            info = denominator_complexity_vec(value)
        else:
            info = denominator_complexity_mat(value)
        max_d = max(max_d, info["max_d"])
        sum_d += info["sum_d"]
        count += info["count"]
    return {"max_d": max_d, "sum_d": sum_d, "count": count}
