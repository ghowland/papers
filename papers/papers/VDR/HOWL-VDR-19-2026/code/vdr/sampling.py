# code/vdr/sampling.py
from __future__ import annotations

from fractions import Fraction
from typing import List, Sequence

from .vdr import VDR
from .linalg import Vec
from .rng import VDRRandom


def _to_vdr(x):
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR(int(x))


def cdf_from_probs(probs: Vec) -> Vec:
    """
    Exact cumulative distribution from exact probability vector.
    """
    total = VDR(0)
    out = []
    for i in range(len(probs)):
        total = total + probs[i]
        out.append(total.normalize())
    return Vec(out)


def categorical_sample(probs: Vec, rng: VDRRandom) -> int:
    """
    Sample exactly from a VDR probability vector.

    Requirements:
      - probs sum exactly to 1
      - all probs >= 0
    """
    total = VDR(0)
    for i in range(len(probs)):
        if probs[i] < VDR(0):
            raise ValueError("probabilities must be nonnegative")
        total = total + probs[i]

    if total != VDR(1):
        raise ValueError("probabilities must sum exactly to 1")

    r = rng.rand_fraction()
    cdf = cdf_from_probs(probs)
    for i in range(len(cdf)):
        if r < cdf[i]:
            return i
    return len(cdf) - 1


def top_k_probs(probs: Vec, k: int) -> Vec:
    if k <= 0:
        raise ValueError("k must be > 0")
    if k > len(probs):
        raise ValueError("k cannot exceed vector length")

    indexed = [(i, probs[i]) for i in range(len(probs))]
    indexed.sort(key=lambda t: t[1].to_fraction(), reverse=True)

    keep = set(i for i, _ in indexed[:k])

    kept_total = VDR(0)
    for i in range(len(probs)):
        if i in keep:
            kept_total = kept_total + probs[i]

    out = []
    for i in range(len(probs)):
        if i in keep:
            out.append((probs[i] / kept_total).normalize())
        else:
            out.append(VDR(0))
    return Vec(out)


def nucleus_probs(probs: Vec, threshold: VDR) -> Vec:
    """
    Keep the smallest set of largest probabilities whose cumulative
    sum is >= threshold, then renormalize exactly.
    """
    threshold = _to_vdr(threshold)
    if threshold <= VDR(0) or threshold > VDR(1):
        raise ValueError("threshold must satisfy 0 < threshold <= 1")

    indexed = [(i, probs[i]) for i in range(len(probs))]
    indexed.sort(key=lambda t: t[1].to_fraction(), reverse=True)

    keep = []
    total = VDR(0)
    for i, p in indexed:
        keep.append(i)
        total = total + p
        if total >= threshold:
            break

    keep_set = set(keep)
    kept_total = VDR(0)
    for i in range(len(probs)):
        if i in keep_set:
            kept_total = kept_total + probs[i]

    out = []
    for i in range(len(probs)):
        if i in keep_set:
            out.append((probs[i] / kept_total).normalize())
        else:
            out.append(VDR(0))
    return Vec(out)
