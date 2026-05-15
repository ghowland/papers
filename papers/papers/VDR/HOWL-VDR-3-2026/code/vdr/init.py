# code/vdr/init.py
from __future__ import annotations

from fractions import Fraction

from .vdr import VDR
from .linalg import Vec, Mat
from .rng import VDRRandom


def rational_uniform_vec(dim, denom=100, seed=1, lo=-1, hi=1):
    rng = VDRRandom(seed)
    vals = []
    for _ in range(dim):
        n = rng.randint(lo * denom, hi * denom)
        vals.append(VDR(n, denom).normalize())
    return Vec(vals)


def rational_uniform_mat(nrows, ncols, denom=100, seed=1, lo=-1, hi=1):
    rng = VDRRandom(seed)
    rows = []
    for _ in range(nrows):
        row = []
        for _ in range(ncols):
            n = rng.randint(lo * denom, hi * denom)
            row.append(VDR(n, denom).normalize())
        rows.append(row)
    return Mat(rows)


def xavier_like_mat(nrows, ncols, denom=100, seed=1):
    """
    Very simple exact rational Xavier-like initialization:

      values drawn uniformly from approximately
      [-1/sqrt(fan_in), +1/sqrt(fan_in)]

    Since sqrt is not native here, use the rational surrogate:
      bound = 1 / fan_in

    This is conservative and exact.
    """
    fan_in = max(1, ncols)
    lo = -1
    hi = 1
    rng = VDRRandom(seed)
    rows = []
    for _ in range(nrows):
        row = []
        for _ in range(ncols):
            n = rng.randint(lo * denom, hi * denom)
            row.append(VDR(n, denom * fan_in).normalize())
        rows.append(row)
    return Mat(rows)


def zero_bias(dim):
    return Vec([VDR(0) for _ in range(dim)])
