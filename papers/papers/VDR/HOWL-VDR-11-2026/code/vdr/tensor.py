# code/vdr/tensor.py
from __future__ import annotations

from fractions import Fraction
from typing import Iterable, List, Sequence, Tuple, Union

from .vdr import VDR
from .linalg import Vec, Mat


ScalarLike = Union[VDR, int, Fraction]


def _to_vdr(x: ScalarLike) -> VDR:
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR(int(x))


class Tensor3:
    """
    Minimal 3D tensor for VDR values.
    Shape convention: [B][N][D]
      B = batch
      N = sequence/items
      D = feature dimension
    """
    def __init__(self, data):
        self.data = [
            [Vec([_to_vdr(x) for x in row]) for row in batch]
            for batch in data
        ]
        if len(self.data) == 0:
            self._shape = (0, 0, 0)
        else:
            b = len(self.data)
            n = len(self.data[0])
            d = self.data[0][0].dim if n > 0 else 0
            for batch in self.data:
                if len(batch) != n:
                    raise ValueError("ragged tensor batches")
                for row in batch:
                    if row.dim != d:
                        raise ValueError("ragged tensor rows")
            self._shape = (b, n, d)

    @classmethod
    def zero(cls, b, n, d):
        return cls(
            [[[VDR(0) for _ in range(d)] for _ in range(n)] for _ in range(b)]
        )

    @property
    def shape(self):
        return self._shape

    @property
    def batch(self):
        return self._shape[0]

    @property
    def nrows(self):
        return self._shape[1]

    @property
    def dim(self):
        return self._shape[2]

    def __getitem__(self, idx):
        return self.data[idx]

    def __len__(self):
        return self.batch

    def to_fractions(self):
        return [
            [row.to_fractions() for row in batch]
            for batch in self.data
        ]

    def __repr__(self):
        return "Tensor3(shape=%r)" % (self.shape,)


def batched_matvec(mats: Sequence[Mat], vecs: Sequence[Vec]) -> List[Vec]:
    if len(mats) != len(vecs):
        raise ValueError("batched_matvec requires same batch size")
    return [mats[i].matvec(vecs[i]) for i in range(len(mats))]


def rowwise_add_bias(rows: Sequence[Vec], bias: Vec) -> List[Vec]:
    out = []
    for row in rows:
        if row.dim != bias.dim:
            raise ValueError("row and bias dimension mismatch")
        out.append(row + bias)
    return out


def masked_fill_rows(rows: Sequence[Vec], mask: Sequence[Sequence[bool]], fill) -> List[Vec]:
    fill = _to_vdr(fill)
    if len(rows) != len(mask):
        raise ValueError("mask and rows must have same length")
    out = []
    for i in range(len(rows)):
        row = rows[i]
        mr = mask[i]
        if len(mr) != row.dim:
            raise ValueError("mask width mismatch")
        out.append(Vec([fill if mr[j] else row[j] for j in range(row.dim)]))
    return out


def reduce_sum_rows(rows: Sequence[Vec]) -> Vec:
    if len(rows) == 0:
        raise ValueError("reduce_sum_rows requires nonempty rows")
    d = rows[0].dim
    total = [VDR(0) for _ in range(d)]
    for row in rows:
        if row.dim != d:
            raise ValueError("row dimension mismatch")
        for j in range(d):
            total[j] = total[j] + row[j]
    return Vec(total)
