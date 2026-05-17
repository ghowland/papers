"""
vdr.linalg — Exact rational linear algebra over VDR objects.

    from vdr.linalg import Vec, Mat

    v = Vec([VDR(1,2), VDR(1,3), VDR(1,7)])
    m = Mat.identity(3)
    det = m.det()

All operations use exact VDR arithmetic. Zero drift.
"""

from __future__ import annotations
from typing import List, Union, Optional
from vdr.vdr import VDR, VDRError, Remainder

__all__ = ["Vec", "Mat", "LinAlgError"]


class LinAlgError(VDRError):
    """Linear algebra specific errors."""
    pass


# ---------------------------------------------------------------------------
# Vec
# ---------------------------------------------------------------------------

class Vec:
    """
    Exact VDR vector — an ordered list of VDR objects.

        v = Vec([VDR(1,2), VDR(1,3)])
        w = Vec.from_ints([1, 2, 3])
        v + w, v - w, v * VDR(2), v.dot(w)
    """

    __slots__ = ("_data",)

    def __init__(self, data):
        # type: (List[Union[VDR, int]]) -> None
        self._data = [_to_vdr(x) for x in data]

    @classmethod
    def from_ints(cls, ns):
        # type: (List[int]) -> Vec
        return cls([VDR(n) for n in ns])

    @classmethod
    def from_fracs(cls, pairs):
        # type: (List[tuple]) -> Vec
        """Vec.from_fracs([(1,2), (3,4)]) → Vec([VDR(1,2), VDR(3,4)])"""
        return cls([VDR(a, b) for a, b in pairs])

    @classmethod
    def zero(cls, n):
        # type: (int) -> Vec
        return cls([VDR(0)] * n)

    # -- access ------------------------------------------------------------

    def __len__(self):
        # type: () -> int
        return len(self._data)

    def __getitem__(self, i):
        # type: (int) -> VDR
        return self._data[i]

    def __iter__(self):
        return iter(self._data)

    @property
    def dim(self):
        # type: () -> int
        return len(self._data)

    # -- arithmetic --------------------------------------------------------

    def __add__(self, other):
        # type: (Vec) -> Vec
        _check_same_dim(self, other, "+")
        return Vec([a + b for a, b in zip(self._data, other._data)])

    def __sub__(self, other):
        # type: (Vec) -> Vec
        _check_same_dim(self, other, "-")
        return Vec([a - b for a, b in zip(self._data, other._data)])

    def __neg__(self):
        # type: () -> Vec
        return Vec([-x for x in self._data])

    def scale(self, s):
        # type: (Union[VDR, int]) -> Vec
        """Scalar multiplication: s · v"""
        s = _to_vdr(s)
        return Vec([x * s for x in self._data])

    def __mul__(self, other):
        # type: (Union[VDR, int]) -> Vec
        return self.scale(other)

    def __rmul__(self, other):
        # type: (Union[VDR, int]) -> Vec
        return self.scale(other)

    def dot(self, other):
        # type: (Vec) -> VDR
        """
        Exact dot product: v · w = Σ vᵢwᵢ
        """
        _check_same_dim(self, other, "dot")
        total = VDR(0)
        for a, b in zip(self._data, other._data):
            total = total + a * b
        return total

    # -- comparison --------------------------------------------------------

    def __eq__(self, other):
        # type: (object) -> bool
        if not isinstance(other, Vec):
            return NotImplemented
        if len(self) != len(other):
            return False
        return all(a == b for a, b in zip(self._data, other._data))

    # -- display -----------------------------------------------------------

    def __repr__(self):
        # type: () -> str
        return "Vec([%s])" % ", ".join(str(x) for x in self._data)

    def to_fractions(self):
        # type: () -> list
        return [x.to_fraction() for x in self._data]


# ---------------------------------------------------------------------------
# Mat
# ---------------------------------------------------------------------------

class Mat:
    """
    Exact VDR matrix — list of row Vecs, all same dimension.

        m = Mat([[VDR(1), VDR(2)], [VDR(3), VDR(4)]])
        m = Mat.from_ints([[1,2],[3,4]])
        m + n, m - n, m * n, m.det(), m.inv(), m.T
    """

    __slots__ = ("_rows",)

    def __init__(self, rows):
        # type: (List[Union[List[Union[VDR, int]], Vec]]) -> None
        if not rows:
            raise LinAlgError("Matrix must have at least one row")
        parsed = []
        for row in rows:
            if isinstance(row, Vec):
                parsed.append(row)
            else:
                parsed.append(Vec(row))
        ncols = len(parsed[0])
        for i, row in enumerate(parsed):
            if len(row) != ncols:
                raise LinAlgError(
                    "Row %d has %d cols, expected %d" % (i, len(row), ncols)
                )
        self._rows = parsed

    @classmethod
    def from_ints(cls, data):
        # type: (List[List[int]]) -> Mat
        return cls([[VDR(x) for x in row] for row in data])

    @classmethod
    def from_fracs(cls, data):
        # type: (List[List[tuple]]) -> Mat
        """Mat.from_fracs([[(1,2),(3,4)],[(5,6),(7,8)]])"""
        return cls([[VDR(a, b) for a, b in row] for row in data])

    @classmethod
    def identity(cls, n):
        # type: (int) -> Mat
        rows = []
        for i in range(n):
            row = [VDR(0)] * n
            row[i] = VDR(1)
            rows.append(row)
        return cls(rows)

    @classmethod
    def zero(cls, nrows, ncols):
        # type: (int, int) -> Mat
        return cls([[VDR(0)] * ncols for _ in range(nrows)])

    # -- access ------------------------------------------------------------

    @property
    def nrows(self):
        # type: () -> int
        return len(self._rows)

    @property
    def ncols(self):
        # type: () -> int
        return len(self._rows[0])

    @property
    def shape(self):
        # type: () -> tuple
        return (self.nrows, self.ncols)

    @property
    def is_square(self):
        # type: () -> bool
        return self.nrows == self.ncols

    def __getitem__(self, idx):
        # type: (tuple) -> VDR
        if isinstance(idx, tuple):
            r, c = idx
            return self._rows[r][c]
        return self._rows[idx]  # returns Vec (row)

    def row(self, i):
        # type: (int) -> Vec
        return self._rows[i]

    def col(self, j):
        # type: (int) -> Vec
        return Vec([self._rows[i][j] for i in range(self.nrows)])

    # -- arithmetic --------------------------------------------------------

    def __add__(self, other):
        # type: (Mat) -> Mat
        _check_same_shape(self, other, "+")
        return Mat([a + b for a, b in zip(self._rows, other._rows)])

    def __sub__(self, other):
        # type: (Mat) -> Mat
        _check_same_shape(self, other, "-")
        return Mat([a - b for a, b in zip(self._rows, other._rows)])

    def __neg__(self):
        # type: () -> Mat
        return Mat([-r for r in self._rows])

    def scale(self, s):
        # type: (Union[VDR, int]) -> Mat
        """Scalar multiplication."""
        return Mat([r.scale(s) for r in self._rows])

    def __mul__(self, other):
        # type: (Union[Mat, Vec, VDR, int]) -> Union[Mat, Vec]
        if isinstance(other, Mat):
            return self.matmul(other)
        if isinstance(other, Vec):
            return self.matvec(other)
        return self.scale(other)

    def __rmul__(self, other):
        # type: (Union[VDR, int]) -> Mat
        return self.scale(other)

    def matmul(self, other):
        # type: (Mat) -> Mat
        """
        Exact matrix multiplication: C[i,j] = Σ A[i,k]·B[k,j]
        """
        if self.ncols != other.nrows:
            raise LinAlgError(
                "Cannot multiply %dx%d by %dx%d" % (
                    self.nrows, self.ncols, other.nrows, other.ncols
                )
            )
        result = []
        for i in range(self.nrows):
            row = []
            for j in range(other.ncols):
                total = VDR(0)
                for k in range(self.ncols):
                    total = total + self[i, k] * other[k, j]
                row.append(total)
            result.append(row)
        return Mat(result)

    def matvec(self, v):
        # type: (Vec) -> Vec
        """Matrix-vector product: Ax"""
        if self.ncols != len(v):
            raise LinAlgError(
                "Cannot multiply %dx%d matrix by %d-vector" % (
                    self.nrows, self.ncols, len(v)
                )
            )
        return Vec([self.row(i).dot(v) for i in range(self.nrows)])

    # -- transpose ---------------------------------------------------------

    @property
    def T(self):
        # type: () -> Mat
        return Mat([
            [self[i, j] for i in range(self.nrows)]
            for j in range(self.ncols)
        ])

    # -- determinant -------------------------------------------------------

    def det(self):
        # type: () -> VDR
        """
        Exact determinant by cofactor expansion.

        For n×n:
            det(A) = Σ (-1)^j · A[0,j] · det(minor(0,j))

        Uses exact VDR arithmetic throughout. No floats.
        """
        if not self.is_square:
            raise LinAlgError("Determinant requires square matrix")
        n = self.nrows
        if n == 1:
            return self[0, 0]
        if n == 2:
            return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]
        total = VDR(0)
        for j in range(n):
            cofactor = self._minor(0, j).det()
            term = self[0, j] * cofactor
            if j % 2 == 0:
                total = total + term
            else:
                total = total - term
        return total

    def _minor(self, row_skip, col_skip):
        # type: (int, int) -> Mat
        """Matrix with row row_skip and column col_skip removed."""
        rows = []
        for i in range(self.nrows):
            if i == row_skip:
                continue
            row = []
            for j in range(self.ncols):
                if j == col_skip:
                    continue
                row.append(self[i, j])
            rows.append(row)
        return Mat(rows)

    # -- trace -------------------------------------------------------------

    def trace(self):
        # type: () -> VDR
        """Sum of diagonal elements."""
        if not self.is_square:
            raise LinAlgError("Trace requires square matrix")
        total = VDR(0)
        for i in range(self.nrows):
            total = total + self[i, i]
        return total

    # -- inverse -----------------------------------------------------------

    def inv(self):
        # type: () -> Mat
        """
        Exact matrix inverse via adjugate method:

            A⁻¹ = adj(A) / det(A)

        Fails if det(A) = 0. Uses exact VDR division.
        """
        if not self.is_square:
            raise LinAlgError("Inverse requires square matrix")
        d = self.det()
        if d == VDR(0):
            raise LinAlgError("Matrix is singular (det = 0)")
        adj = self._adjugate()
        return adj.scale(VDR(1) / d)

    def _adjugate(self):
        # type: () -> Mat
        """Transpose of cofactor matrix."""
        n = self.nrows
        cof = []
        for i in range(n):
            row = []
            for j in range(n):
                minor_det = self._minor(i, j).det()
                if (i + j) % 2 == 1:
                    minor_det = -minor_det
                row.append(minor_det)
            cof.append(row)
        return Mat(cof).T

    # -- solve -------------------------------------------------------------

    def solve(self, b):
        # type: (Vec) -> Vec
        """
        Solve Ax = b by Cramer's rule (exact for small systems).

        For large systems, Gaussian elimination would be more efficient
        but Cramer's rule is exact and simple for v1.
        """
        if not self.is_square:
            raise LinAlgError("Solve requires square matrix")
        if self.nrows != len(b):
            raise LinAlgError("Dimension mismatch")
        d = self.det()
        if d == VDR(0):
            raise LinAlgError("System is singular")
        n = self.nrows
        result = []
        for j in range(n):
            # replace column j with b
            cols = []
            for jj in range(n):
                if jj == j:
                    cols.append([b[i] for i in range(n)])
                else:
                    cols.append([self[i, jj] for i in range(n)])
            # build matrix from columns
            replaced = Mat([
                [cols[jj][i] for jj in range(n)]
                for i in range(n)
            ])
            result.append(replaced.det() / d)
        return Vec(result)

    # -- rank (via row echelon) --------------------------------------------

    def rank(self):
        # type: () -> int
        """
        Exact rank via Gaussian elimination over VDR rationals.
        """
        rows = [list(r) for r in self._rows]
        m, n = self.nrows, self.ncols
        pivot_row = 0
        for col in range(n):
            # find nonzero entry in this column at or below pivot_row
            found = None
            for row in range(pivot_row, m):
                if rows[row][col] != VDR(0):
                    found = row
                    break
            if found is None:
                continue
            # swap
            rows[pivot_row], rows[found] = rows[found], rows[pivot_row]
            # eliminate below
            pivot_val = rows[pivot_row][col]
            for row in range(pivot_row + 1, m):
                if rows[row][col] != VDR(0):
                    factor = rows[row][col] / pivot_val
                    for k in range(n):
                        rows[row][k] = rows[row][k] - factor * rows[pivot_row][k]
            pivot_row += 1
        return pivot_row

    # -- comparison --------------------------------------------------------

    def __eq__(self, other):
        # type: (object) -> bool
        if not isinstance(other, Mat):
            return NotImplemented
        if self.shape != other.shape:
            return False
        return all(a == b for a, b in zip(self._rows, other._rows))

    # -- display -----------------------------------------------------------

    def __repr__(self):
        # type: () -> str
        row_strs = []
        for r in self._rows:
            row_strs.append("[%s]" % ", ".join(str(x) for x in r))
        return "Mat([%s])" % ", ".join(row_strs)

    def pretty(self):
        # type: () -> str
        """Human-readable matrix display."""
        lines = []
        # compute column widths
        strs = [[str(self[i, j]) for j in range(self.ncols)]
                for i in range(self.nrows)]
        widths = [max(len(strs[i][j]) for i in range(self.nrows))
                  for j in range(self.ncols)]
        for i in range(self.nrows):
            cells = [strs[i][j].rjust(widths[j]) for j in range(self.ncols)]
            lines.append("| %s |" % "  ".join(cells))
        return "\n".join(lines)

    def to_fractions(self):
        # type: () -> list
        """Export as list of lists of Fraction."""
        return [[self[i, j].to_fraction()
                 for j in range(self.ncols)]
                for i in range(self.nrows)]


# ---------------------------------------------------------------------------
# vdr/parse.py functionality inlined here for now
# ---------------------------------------------------------------------------

def parse_vdr(text):
    # type: (str) -> VDR
    """
    Parse bracket notation into a VDR object.

        parse_vdr("[1, 2, 0]")       → VDR(1, 2)
        parse_vdr("[1, 3, [1, 6, 0]]") → VDR(1, 3, Remainder(0, [VDR(1, 6)]))

    Grammar:
        vdr     := '[' int ',' int ',' remainder ']'
        remainder := int | int '+' vdr ('+' vdr)*
        int     := optional sign + digits
    """
    text = text.strip()
    result, pos = _parse_vdr(text, 0)
    if pos != len(text):
        raise InvalidStructureError(
            "Unexpected trailing content at position %d" % pos
        )
    return result


from vdr.vdr import InvalidStructureError


def _parse_vdr(text, pos):
    # type: (str, int) -> tuple
    pos = _skip_ws(text, pos)
    if pos >= len(text) or text[pos] != '[':
        raise InvalidStructureError("Expected '[' at position %d" % pos)
    pos += 1

    # V
    pos = _skip_ws(text, pos)
    v, pos = _parse_int(text, pos)

    pos = _skip_ws(text, pos)
    if pos >= len(text) or text[pos] != ',':
        raise InvalidStructureError("Expected ',' after V at position %d" % pos)
    pos += 1

    # D
    pos = _skip_ws(text, pos)
    d, pos = _parse_int(text, pos)

    pos = _skip_ws(text, pos)
    if pos >= len(text) or text[pos] != ',':
        raise InvalidStructureError("Expected ',' after D at position %d" % pos)
    pos += 1

    # R
    pos = _skip_ws(text, pos)
    r, pos = _parse_remainder(text, pos)

    pos = _skip_ws(text, pos)
    if pos >= len(text) or text[pos] != ']':
        raise InvalidStructureError("Expected ']' at position %d" % pos)
    pos += 1

    return VDR(v, d, r), pos


def _parse_remainder(text, pos):
    # type: (str, int) -> tuple
    pos = _skip_ws(text, pos)

    # check if it starts with '[' (a child VDR in remainder)
    if pos < len(text) and text[pos] == '[':
        child, pos = _parse_vdr(text, pos)
        children = [child]
        # check for more '+' children
        while pos < len(text):
            pos = _skip_ws(text, pos)
            if pos < len(text) and text[pos] == '+':
                pos += 1
                pos = _skip_ws(text, pos)
                if pos < len(text) and text[pos] == '[':
                    child, pos = _parse_vdr(text, pos)
                    children.append(child)
                else:
                    # integer after +
                    n, pos = _parse_int(text, pos)
                    # this is base, swap: put base first
                    return Remainder(n, children), pos
            else:
                break
        return Remainder(0, children), pos

    # starts with int
    base, pos = _parse_int(text, pos)

    # check for '+' followed by children
    children = []
    while pos < len(text):
        pos = _skip_ws(text, pos)
        if pos < len(text) and text[pos] == '+':
            saved = pos
            pos += 1
            pos = _skip_ws(text, pos)
            if pos < len(text) and text[pos] == '[':
                child, pos = _parse_vdr(text, pos)
                children.append(child)
            elif pos < len(text) and (text[pos].isdigit() or text[pos] == '-'):
                # could be next int being added to base... but our grammar
                # treats remainder base as single int. This would be like "1 + 2"
                # which should consolidate. For now, fail cleanly.
                pos = saved
                break
            else:
                pos = saved
                break
        else:
            break

    return Remainder(base, children), pos


def _parse_int(text, pos):
    # type: (str, int) -> tuple
    pos = _skip_ws(text, pos)
    start = pos
    if pos < len(text) and text[pos] in '+-':
        pos += 1
    if pos >= len(text) or not text[pos].isdigit():
        raise InvalidStructureError(
            "Expected integer at position %d" % start
        )
    while pos < len(text) and text[pos].isdigit():
        pos += 1
    return int(text[start:pos]), pos


def _skip_ws(text, pos):
    # type: (str, int) -> int
    while pos < len(text) and text[pos] in ' \t\n\r':
        pos += 1
    return pos


# ---------------------------------------------------------------------------
# Serialization helpers
# ---------------------------------------------------------------------------

def vdr_to_dict(x):
    # type: (VDR) -> dict
    """Serialize VDR to a JSON-compatible dict."""
    return {
        "v": x.v,
        "d": x.d,
        "r": _remainder_to_dict(x.r),
    }


def vdr_from_dict(d):
    # type: (dict) -> VDR
    """Deserialize VDR from a JSON-compatible dict."""
    return VDR(d["v"], d["d"], _remainder_from_dict(d["r"]))


def _remainder_to_dict(r):
    # type: (Remainder) -> dict
    return {
        "base": r.base,
        "children": [vdr_to_dict(c) for c in r.children],
    }


def _remainder_from_dict(d):
    # type: (dict) -> Remainder
    children = [vdr_from_dict(c) for c in d.get("children", [])]
    return Remainder(d["base"], children)


def vdr_to_latex(x):
    # type: (VDR) -> str
    """
    Export VDR to LaTeX notation.

        [1, 2, 0]          → \\frac{1}{2}
        [1, 3, [1, 6, 0]]  → \\frac{1}{3}\\left\\{\\frac{1}{6}\\right\\}
    """
    if x.is_closed:
        if x.d == 1:
            return str(x.v)
        return "\\frac{%d}{%d}" % (x.v, x.d)
    # active: show remainder in braces
    base = "\\frac{%d}{%d}" % (x.v, x.d) if x.d != 1 else str(x.v)
    rem = _remainder_to_latex(x.r)
    return "%s\\left\\{%s\\right\\}" % (base, rem)


def _remainder_to_latex(r):
    # type: (Remainder) -> str
    parts = []
    if r.base != 0 or not r.children:
        parts.append(str(r.base))
    for c in r.children:
        parts.append(vdr_to_latex(c))
    return " + ".join(parts)


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _to_vdr(x):
    # type: (Union[VDR, int]) -> VDR
    if isinstance(x, VDR):
        return x
    if isinstance(x, int):
        return VDR(x)
    raise TypeError("Expected VDR or int, got %s" % type(x).__name__)


def _check_same_dim(a, b, op):
    # type: (Vec, Vec, str) -> None
    if len(a) != len(b):
        raise LinAlgError(
            "Vec %s requires same dimension: %d vs %d" % (op, len(a), len(b))
        )


def _check_same_shape(a, b, op):
    # type: (Mat, Mat, str) -> None
    if a.shape != b.shape:
        raise LinAlgError(
            "Mat %s requires same shape: %s vs %s" % (op, a.shape, b.shape)
        )
    