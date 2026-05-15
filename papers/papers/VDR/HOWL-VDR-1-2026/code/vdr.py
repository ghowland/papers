"""
VDR — Value Denominator Remainder
Exact finite discrete representation in irreducible triple form.

A VDR object is [V, D, R] where:
    V ∈ ℤ           — value slot (settled numerator)
    D ∈ ℤ \ {0}     — denominator slot (frame)
    R ∈ Residual     — remainder slot (exact unresolved state)

R is either:
    an integer (atomic remainder), or
    an integer base plus a finite list of child VDR objects (composite remainder)

Recursion exists only in R. Every valid object is a finite tree.
No limits, no approximation, no infinity.

Closed object:  [V, D, 0]  — projects to V/D exactly
Active object:  [V, D, R]  with R ≠ 0 — carries exact residual state

    from vdr import VDR
    x = VDR(1, 2)       # 1/2
    y = VDR(1, 3)       # 1/3
    z = x + y           # [5, 6, 0]
    print(z)            # VDR(5, 6, 0)
    print(z.to_fraction())  # 5/6
"""

from __future__ import annotations
from fractions import Fraction
from math import gcd
from typing import List, Optional, Tuple, Union

__all__ = ["VDR", "Residual", "VDRError"]


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------

class VDRError(Exception):
    """Base error for all VDR operations."""
    pass

class ZeroDenominatorError(VDRError):
    pass

class InvalidStructureError(VDRError):
    pass

class RebaseError(VDRError):
    pass

class ArithmeticFailure(VDRError):
    pass


# ---------------------------------------------------------------------------
# Residual
# ---------------------------------------------------------------------------

class Residual:
    """
    The remainder slot of a VDR triple.

    Atomic form:   Residual(base=r, children=[])
                   — a single integer r

    Composite form: Residual(base=r, children=[X1, X2, ...])
                    — integer base plus finite child VDR list

    Formally: R = r + X₁ + X₂ + … + Xₙ
    where r ∈ ℤ and each Xᵢ is a valid VDR object.
    """

    __slots__ = ("base", "children")

    def __init__(self, base=0, children=None):
        # type: (int, Optional[List[VDR]]) -> None
        if not isinstance(base, int):
            raise InvalidStructureError(
                "Residual base must be int, got %s" % type(base).__name__
            )
        self.base = base
        self.children = list(children) if children else []
        for c in self.children:
            if not isinstance(c, VDR):
                raise InvalidStructureError(
                    "Residual child must be VDR, got %s" % type(c).__name__
                )

    # -- predicates --------------------------------------------------------

    @property
    def is_zero(self):
        # type: () -> bool
        """True when this residual contributes nothing: base 0, no children."""
        return self.base == 0 and len(self.children) == 0

    @property
    def is_atomic(self):
        # type: () -> bool
        return len(self.children) == 0

    @property
    def is_globally_zero(self):
        # type: () -> bool
        """True when base is 0, no children, recursively."""
        if self.base != 0:
            return False
        return all(c.is_globally_closed for c in self.children)

    # -- equality ----------------------------------------------------------

    def structural_eq(self, other):
        # type: (Residual) -> bool
        if not isinstance(other, Residual):
            return False
        if self.base != other.base:
            return False
        if len(self.children) != len(other.children):
            return False
        return all(
            a.structural_eq(b)
            for a, b in zip(self.children, other.children)
        )

    # -- operations --------------------------------------------------------

    def negate(self):
        # type: () -> Residual
        """
        -(r + X₁ + … + Xₙ) = -r + (-X₁) + … + (-Xₙ)
        """
        return Residual(
            -self.base,
            [c.negate() for c in self.children],
        )

    def combine(self, other, sign=1):
        # type: (Residual, int) -> Residual
        """
        Same-frame residual combination.
        sign=1  for addition:    R₁ ⊕ R₂
        sign=-1 for subtraction: R₁ ⊖ R₂
        """
        if sign == 1:
            new_base = self.base + other.base
            new_children = list(self.children) + list(other.children)
        else:
            new_base = self.base - other.base
            new_children = list(self.children) + [
                c.negate() for c in other.children
            ]
        return Residual(new_base, new_children)

    def lift(self, k):
        # type: (int) -> Residual
        """
        Transport remainder into a scaled denominator frame.

        lift(r, k) = k·r
        lift(r + X₁+…+Xₙ, k) = k·r + lift(X₁,k) + … + lift(Xₙ,k)

        Child VDR lift:
            lift([V, D, R], k) = [k·V, D, lift(R, k)]
        — scales V and R, preserves child D.
        """
        if k == 0:
            raise VDRError("lift by zero is invalid")
        return Residual(
            self.base * k,
            [c._lift_vdr(k) for c in self.children],
        )

    # -- projection --------------------------------------------------------

    def legacy_value(self):
        # type: () -> Fraction
        """
        Additive flattening for external scalar comparison.

        legacy(r) = r
        legacy(r + X₁+…+Xₙ) = r + legacy(X₁) + … + legacy(Xₙ)
        """
        total = Fraction(self.base)
        for c in self.children:
            total += c.to_fraction()
        return total

    # -- normalization -----------------------------------------------------

    def normalize(self):
        # type: () -> Residual
        """
        Normalize residual structure:
        1. Normalize all children recursively
        2. Absorb closed children with matching parent-frame denominator
           (deferred — requires parent context)
        3. Consolidate atomic base (already single int by construction)
        4. Sort children canonically
        5. Merge same-denominator closed children
        """
        # normalize children first
        normed = [c.normalize() for c in self.children]

        # separate children that collapsed to zero
        live = []
        absorbed_base = self.base
        for c in normed:
            if c.is_globally_closed and c.v == 0:
                # zero-value closed child contributes nothing
                continue
            live.append(c)

        # merge closed children sharing a denominator
        merged = _merge_same_denom_children(live)

        # absorb any child that is globally closed with value that
        # can fold into atomic base... only if child D == 1
        final_children = []
        for c in merged:
            if c.is_globally_closed and c.d == 1:
                absorbed_base += c.v
            else:
                final_children.append(c)

        # sort children canonically: by |D| asc, then V asc, then residual
        final_children.sort(key=_child_sort_key)

        return Residual(absorbed_base, final_children)

    # -- display -----------------------------------------------------------

    def __repr__(self):
        # type: () -> str
        if self.is_atomic:
            return str(self.base)
        parts = [str(self.base)]
        for c in self.children:
            parts.append(repr(c))
        return " + ".join(parts)

    def __eq__(self, other):
        # type: (object) -> bool
        if isinstance(other, int) and self.is_atomic:
            return self.base == other
        if isinstance(other, Residual):
            return self.structural_eq(other)
        return NotImplemented

    def __hash__(self):
        # type: () -> int
        return hash((self.base, tuple(self.children)))


# ---------------------------------------------------------------------------
# VDR
# ---------------------------------------------------------------------------

class VDR:
    """
    Exact finite discrete triple: [V, D, R]

    Construction:
        VDR(3)              → [3, 1, 0]   integer
        VDR(1, 2)           → [1, 2, 0]   rational 1/2
        VDR(1, 3, Residual(1))  → [1, 3, 1]   active
        VDR.from_fraction(Fraction(5, 6))  → [5, 6, 0]

    Arithmetic uses Python operators:
        x + y,  x - y,  x * y,  x / y,  -x

    Projection:
        x.to_fraction()  → Fraction (exact for closed, legacy flatten for active)
        float(x)         → lossy float export
    """

    __slots__ = ("v", "d", "r")

    def __init__(self, v, d=1, r=None):
        # type: (int, int, Union[None, int, Residual]) -> None
        if not isinstance(v, int):
            raise InvalidStructureError(
                "V must be int, got %s" % type(v).__name__
            )
        if not isinstance(d, int):
            raise InvalidStructureError(
                "D must be int, got %s" % type(d).__name__
            )
        if d == 0:
            raise ZeroDenominatorError("D must not be zero")

        self.v = v
        self.d = d

        if r is None:
            self.r = Residual(0)
        elif isinstance(r, int):
            self.r = Residual(r)
        elif isinstance(r, Residual):
            self.r = r
        else:
            raise InvalidStructureError(
                "R must be int, Residual, or None, got %s" % type(r).__name__
            )

    # -- class constructors ------------------------------------------------

    @classmethod
    def from_fraction(cls, frac):
        # type: (Fraction) -> VDR
        """Exact inbound construction from fractions.Fraction."""
        return cls(frac.numerator, frac.denominator)

    @classmethod
    def from_int(cls, n):
        # type: (int) -> VDR
        """Exact inbound construction from integer."""
        return cls(n, 1)

    # -- predicates --------------------------------------------------------

    @property
    def is_closed(self):
        # type: () -> bool
        """Top-level remainder is zero."""
        return self.r.is_zero

    @property
    def is_globally_closed(self):
        # type: () -> bool
        """All remainders in the entire tree are zero."""
        if not self.r.is_zero:
            return False
        return self.r.is_globally_zero

    @property
    def is_active(self):
        # type: () -> bool
        return not self.is_closed

    # -- equality ----------------------------------------------------------

    def structural_eq(self, other):
        # type: (VDR) -> bool
        """
        X ≡ₛ Y  iff every slot matches exactly, recursively.
        """
        if not isinstance(other, VDR):
            return False
        return (
            self.v == other.v
            and self.d == other.d
            and self.r.structural_eq(other.r)
        )

    def value_eq(self, other):
        # type: (VDR) -> bool
        """
        X ≡ₙ Y  iff  norm(X) ≡ₛ norm(Y)

        Normalized value equality.
        """
        if not isinstance(other, VDR):
            return False
        return self.normalize().structural_eq(other.normalize())

    def __eq__(self, other):
        # type: (object) -> bool
        """Python == uses value equality."""
        if isinstance(other, VDR):
            return self.value_eq(other)
        if isinstance(other, int):
            return self.value_eq(VDR(other))
        if isinstance(other, Fraction):
            return self.value_eq(VDR.from_fraction(other))
        return NotImplemented

    def __hash__(self):
        # type: () -> int
        n = self.normalize()
        return hash((n.v, n.d, n.r))

    # -- normalization -----------------------------------------------------

    def normalize(self):
        # type: () -> VDR
        """
        Produce canonical form:
        1. Normalize remainder recursively
        2. Sign convention: D > 0
        3. GCD reduce (V, D) for closed nodes
        4. Absorb same-denominator children where possible
        5. Closed-form preference: if remainder settles to zero, close it

        norm(X) is always value-equal to X.
        """
        # normalize remainder first
        nr = self.r.normalize()
        v, d = self.v, self.d

        # sign convention: positive denominator
        if d < 0:
            v, d = -v, -d

        # if remainder is globally zero, reduce as closed fraction
        if nr.is_zero:
            g = gcd(abs(v), abs(d))
            if g > 0:
                v, d = v // g, d // g
            return VDR(v, d, Residual(0))

        # for active nodes, still enforce positive D
        # but only reduce V,D if compatible with remainder
        # (first pass: reduce V,D by gcd always, scale remainder)
        g = gcd(abs(v), abs(d))
        if g > 1:
            # to reduce [V,D,R] to [V/g, D/g, R']:
            # this changes the denominator frame, so R must be
            # adjusted. For now, only reduce if g divides the
            # remainder base and all child numerators cleanly.
            if _remainder_divisible_by(nr, g):
                v, d = v // g, d // g
                nr = _remainder_divide(nr, g)
            # else keep unreduced

        return VDR(v, d, nr)

    # -- projection --------------------------------------------------------

    def to_fraction(self):
        # type: () -> Fraction
        """
        Exact projection to fractions.Fraction.

        Closed:  V/D
        Active:  (V + ρ_D(R)) / D  via legacy flattening

        For closed objects this is exact and lossless.
        For active objects this uses additive flattening (legacy conversion).
        The result is exact rational but leaves native VDR semantics.
        """
        return Fraction(self.v, self.d) + Fraction(
            self.r.legacy_value(), self.d
        )

    def to_float(self):
        # type: () -> float
        """
        Lossy export to float.
        Loss belongs to the target format, not to VDR.
        """
        return float(self.to_fraction())

    def __float__(self):
        # type: () -> float
        return self.to_float()

    # -- closed arithmetic -------------------------------------------------
    #
    #  [V₁,D₁,0] + [V₂,D₂,0] = [V₁D₂+V₂D₁, D₁D₂, 0]
    #  [V₁,D₁,0] - [V₂,D₂,0] = [V₁D₂-V₂D₁, D₁D₂, 0]
    #  [V₁,D₁,0] × [V₂,D₂,0] = [V₁V₂, D₁D₂, 0]
    #  [V₁,D₁,0] ÷ [V₂,D₂,0] = [V₁D₂, D₁V₂, 0]   (V₂≠0)
    #

    def __add__(self, other):
        # type: (Union[VDR, int, Fraction]) -> VDR
        other = _coerce(other)
        if self.is_closed and other.is_closed:
            return VDR(
                self.v * other.d + other.v * self.d,
                self.d * other.d,
            ).normalize()
        # active addition
        return _active_add(self, other, sign=1)

    def __radd__(self, other):
        # type: (Union[int, Fraction]) -> VDR
        return self.__add__(other)

    def __sub__(self, other):
        # type: (Union[VDR, int, Fraction]) -> VDR
        other = _coerce(other)
        if self.is_closed and other.is_closed:
            return VDR(
                self.v * other.d - other.v * self.d,
                self.d * other.d,
            ).normalize()
        return _active_add(self, other, sign=-1)

    def __rsub__(self, other):
        # type: (Union[int, Fraction]) -> VDR
        return _coerce(other).__sub__(self)

    def __mul__(self, other):
        # type: (Union[VDR, int, Fraction]) -> VDR
        other = _coerce(other)
        if self.is_closed and other.is_closed:
            return VDR(
                self.v * other.v,
                self.d * other.d,
            ).normalize()
        raise ArithmeticFailure(
            "Active multiplication not yet constructively defined in v1"
        )

    def __rmul__(self, other):
        # type: (Union[int, Fraction]) -> VDR
        return self.__mul__(other)

    def __truediv__(self, other):
        # type: (Union[VDR, int, Fraction]) -> VDR
        other = _coerce(other)
        if other.is_closed and other.v == 0:
            raise ArithmeticFailure("Division by zero")
        if self.is_closed and other.is_closed:
            return VDR(
                self.v * other.d,
                self.d * other.v,
            ).normalize()
        raise ArithmeticFailure(
            "Active division not yet constructively defined in v1"
        )

    def __rtruediv__(self, other):
        # type: (Union[int, Fraction]) -> VDR
        return _coerce(other).__truediv__(self)

    def __neg__(self):
        # type: () -> VDR
        """
        -[V, D, R] = [-V, D, -R]
        """
        return VDR(-self.v, self.d, self.r.negate())

    def __pos__(self):
        # type: () -> VDR
        return self

    def __abs__(self):
        # type: () -> VDR
        if self.to_fraction() < 0:
            return -self
        return VDR(self.v, self.d, self.r)

    # -- rebase ------------------------------------------------------------

    def rebase(self, target_d):
        # type: (int) -> VDR
        """
        Change top-level denominator to target_d, preserving exact value.

        Closed rebase:  succeeds when V·B/D is integer
        Active rebase:  [Q, B, [S,D,0] + lift(R, B)]
            where V·B = Q·D + S

        rebase([V,D,R], B) = [Q, B, [S,D,0] + lift(R,B)]

        Projects correctly under completion semantics:
            Π([Q,B,[S,D,0]]) = (Q + S/D) / B = (QD+S)/(BD) = V/D
        """
        if not isinstance(target_d, int) or target_d == 0:
            raise RebaseError("Target denominator must be nonzero integer")

        if target_d == self.d:
            return VDR(self.v, self.d, self.r)

        # try closed rebase first
        n = self.v * target_d
        q, s = divmod(n, self.d)

        # handle Python's floor division for negative cases
        # we want truncation toward zero for consistent remainder sign
        if self.d > 0:
            q, s = divmod(n, self.d)
        else:
            q, s = divmod(n, self.d)

        if s == 0 and self.r.is_zero:
            # clean closed rebase
            return VDR(q, target_d).normalize()

        # active rebase
        # mismatch witness: [S, D, 0]
        mismatch = VDR(s, self.d)

        # lift existing remainder into new frame
        lifted_r = self.r.lift(target_d)

        # combine: [S,D,0] + lift(R, B)
        new_children = [mismatch] + lifted_r.children if not lifted_r.is_zero else [mismatch]
        new_base = lifted_r.base

        # if mismatch is zero, skip it
        if mismatch.v == 0:
            new_r = lifted_r
        else:
            new_r = Residual(new_base, new_children)

        return VDR(q, target_d, new_r).normalize()

    # -- lift (on VDR object) ----------------------------------------------

    def _lift_vdr(self, k):
        # type: (int) -> VDR
        """
        lift([V, D, R], k) = [k·V, D, lift(R, k)]

        Scales V and R by k, preserves child D.
        """
        return VDR(k * self.v, self.d, self.r.lift(k))

    # -- negation helper ---------------------------------------------------

    def negate(self):
        # type: () -> VDR
        return self.__neg__()

    # -- structural metrics ------------------------------------------------

    def depth(self):
        # type: () -> int
        """
        Recursive depth of the VDR tree.

        depth([V,D,0]) = 0
        depth([V,D,R]) = max(depth of children) + 1  if R has children
        """
        if self.r.is_zero:
            return 0
        if not self.r.children:
            return 0  # atomic nonzero remainder, no nesting
        return 1 + max(c.depth() for c in self.r.children)

    def size(self):
        # type: () -> int
        """
        Structural size: 1 per VDR node + 1 per atomic remainder base.

        size(r) = 1
        size([V,D,R]) = 1 + size(R)
        size(r + X₁+…+Xₙ) = 1 + Σsize(Xᵢ)
        """
        return 1 + _residual_size(self.r)

    def den_complexity(self):
        # type: () -> Tuple[int, int, int]
        """
        Denominator complexity: (distinct_count, magnitude_sum, node_count)
        Compared lexicographically. Lower is simpler.
        """
        denoms = []  # type: List[int]
        _collect_denoms(self, denoms)
        abs_denoms = [abs(dd) for dd in denoms]
        unique = len(set(abs_denoms))
        total = sum(abs_denoms)
        count = len(abs_denoms)
        return (unique, total, count)

    # -- display -----------------------------------------------------------

    def __repr__(self):
        # type: () -> str
        return "VDR(%s, %s, %s)" % (self.v, self.d, repr(self.r))

    def __str__(self):
        # type: () -> str
        return "[%s, %s, %s]" % (self.v, self.d, self.r)

    def bracket(self):
        # type: () -> str
        """Native bracket notation."""
        return str(self)

    # -- comparison (ordering via projection) ------------------------------

    def __lt__(self, other):
        # type: (Union[VDR, int, Fraction]) -> bool
        other = _coerce(other)
        return self.to_fraction() < other.to_fraction()

    def __le__(self, other):
        # type: (Union[VDR, int, Fraction]) -> bool
        other = _coerce(other)
        return self.to_fraction() <= other.to_fraction()

    def __gt__(self, other):
        # type: (Union[VDR, int, Fraction]) -> bool
        other = _coerce(other)
        return self.to_fraction() > other.to_fraction()

    def __ge__(self, other):
        # type: (Union[VDR, int, Fraction]) -> bool
        other = _coerce(other)
        return self.to_fraction() >= other.to_fraction()


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _coerce(other):
    # type: (Union[VDR, int, Fraction]) -> VDR
    """Coerce int or Fraction into VDR for arithmetic."""
    if isinstance(other, VDR):
        return other
    if isinstance(other, int):
        return VDR(other)
    if isinstance(other, Fraction):
        return VDR.from_fraction(other)
    raise TypeError("Cannot coerce %s to VDR" % type(other).__name__)


def _active_add(a, b, sign=1):
    # type: (VDR, VDR, int) -> VDR
    """
    General addition (sign=1) or subtraction (sign=-1).

    Same denominator:
        [V₁,D,R₁] + [V₂,D,R₂] = [V₁+V₂, D, R₁⊕R₂]

    Different denominator:
        cross-scale to D₁·D₂, lift remainders
        [V₁D₂+V₂D₁, D₁D₂, lift(R₁,D₂) + lift(R₂,D₁)]
    """
    if a.d == b.d:
        # same frame
        if sign == 1:
            new_v = a.v + b.v
        else:
            new_v = a.v - b.v
        new_r = a.r.combine(b.r, sign=sign)
        return VDR(new_v, a.d, new_r).normalize()

    # different denominators: cross-scale
    # a becomes [a.v * b.d, a.d * b.d, lift(a.r, b.d)]
    # b becomes [b.v * a.d, a.d * b.d, lift(b.r, a.d)]
    new_d = a.d * b.d
    a_lifted_r = a.r.lift(b.d)
    b_lifted_r = b.r.lift(a.d)

    if sign == 1:
        new_v = a.v * b.d + b.v * a.d
    else:
        new_v = a.v * b.d - b.v * a.d

    new_r = a_lifted_r.combine(b_lifted_r, sign=sign)
    return VDR(new_v, new_d, new_r).normalize()


def _remainder_divisible_by(r, g):
    # type: (Residual, int) -> bool
    """Check if a remainder can be cleanly divided by g."""
    if r.base % g != 0:
        return False
    for c in r.children:
        if c.v % g != 0:
            return False
        if not _remainder_divisible_by(c.r, g):
            return False
    return True


def _remainder_divide(r, g):
    # type: (Residual, int) -> Residual
    """Divide remainder structure by g (must be pre-checked)."""
    new_children = []
    for c in r.children:
        new_children.append(VDR(c.v // g, c.d, _remainder_divide(c.r, g)))
    return Residual(r.base // g, new_children)


def _merge_same_denom_children(children):
    # type: (List[VDR]) -> List[VDR]
    """Merge closed children sharing a denominator."""
    if not children:
        return []

    by_denom = {}  # type: dict
    non_closed = []
    for c in children:
        if c.is_globally_closed:
            key = abs(c.d)
            if key not in by_denom:
                by_denom[key] = []
            by_denom[key].append(c)
        else:
            non_closed.append(c)

    merged = []
    for key in sorted(by_denom.keys()):
        group = by_denom[key]
        if len(group) == 1:
            merged.append(group[0])
        else:
            # add them: all share same |D|, but signs may differ
            total = group[0]
            for g in group[1:]:
                total = total + g  # uses closed addition
            if total.v != 0 or not total.is_globally_closed:
                merged.append(total.normalize())
            # else it cancelled to zero, drop it

    return merged + non_closed


def _child_sort_key(c):
    # type: (VDR) -> tuple
    """Canonical sort key for remainder children."""
    return (abs(c.d), c.d, c.v, c.r.base)


def _residual_size(r):
    # type: (Residual) -> int
    """size(R): 1 for atomic base + sum of child sizes."""
    total = 1  # the atomic base
    for c in r.children:
        total += c.size()
    return total


def _collect_denoms(x, acc):
    # type: (VDR, List[int]) -> None
    """Collect all denominators in the tree."""
    acc.append(x.d)
    for c in x.r.children:
        _collect_denoms(c, acc)
        