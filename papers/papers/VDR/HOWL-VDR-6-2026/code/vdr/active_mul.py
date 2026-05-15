"""
vdr.active_mul — Active multiplication and division for VDR objects.

Extends VDR arithmetic beyond the closed subclass.

For [V₁,D₁,R₁] × [V₂,D₂,R₂], the product expands as:

    (V₁/D₁ + ρ(R₁)/D₁) × (V₂/D₂ + ρ(R₂)/D₂)

    = V₁V₂/(D₁D₂)                        — closed cross
      + V₁·ρ(R₂)/(D₁D₂)                  — left cross
      + V₂·ρ(R₁)/(D₁D₂)                  — right cross
      + ρ(R₁)·ρ(R₂)/(D₁D₂)               — remainder cross

All cross-terms are captured as exact remainder structure in the result.
No approximation. Explicit failure if exact finite form is impossible.

    import vdr.active_mul
    vdr.active_mul.install()   # patches VDR.__mul__ and __truediv__

This is a separate module so the core vdr.py stays clean and the active
multiplication logic can be iterated independently.
"""

from __future__ import annotations
from fractions import Fraction
from math import gcd
from typing import Union

from vdr.vdr import VDR, Remainder, VDRError, ArithmeticFailure

__all__ = ["active_mul", "active_div", "install"]


def active_mul(a, b):
    # type: (VDR, VDR) -> VDR
    """
    Exact multiplication of two VDR objects, including active.

    Strategy: flatten both to exact Fraction via legacy projection,
    multiply exactly, then construct the result as a VDR object
    that preserves the product's remainder structure.

    For two closed objects, this reduces to standard closed multiplication.

    For active objects, the product is constructed by decomposing the
    exact rational result into a VDR triple that captures the full
    cross-term structure.

    The key insight: since every VDR object (closed or active) projects
    to an exact Fraction via legacy conversion, and Fraction × Fraction
    is exact, the product is always an exact rational. We then construct
    a VDR object from that rational, preserving structural information
    about how the product arose.
    """
    # both closed: use direct formula (no projection needed)
    if a.is_closed and b.is_closed:
        return VDR(a.v * b.v, a.d * b.d).normalize()

    # at least one active: construct product structurally
    #
    # The full expansion of [V₁,D₁,R₁] × [V₂,D₂,R₂]:
    #
    # New denominator frame: D₁·D₂
    #
    # Closed part of numerator: V₁·V₂
    #
    # Cross-term remainder contributions:
    #   V₁ · R₂  (left cross:  V₁ multiplies the second operand's remainder)
    #   V₂ · R₁  (right cross: V₂ multiplies the first operand's remainder)
    #   R₁ · R₂  (remainder cross: both remainders interact)
    #
    # For atomic remainders, each cross-term produces a concrete integer
    # or child VDR contribution.

    new_d = a.d * b.d
    new_v = a.v * b.v

    # Build remainder from cross-terms
    r_parts = _mul_cross_terms(a, b)

    return VDR(new_v, new_d, r_parts).normalize()


def active_div(a, b):
    # type: (VDR, VDR) -> VDR
    """
    Exact division of two VDR objects.

    Division by a closed object with V≠0 is always exact.
    Division by an active object uses the multiplicative inverse
    constructed from the active object's exact projected value.

    If the divisor projects to zero, division fails.
    """
    if b.is_closed:
        if b.v == 0:
            raise ArithmeticFailure("Division by zero")
        if a.is_closed:
            return VDR(a.v * b.d, a.d * b.v).normalize()
        # a is active, b is closed: [V₁,D₁,R₁] / [V₂,D₂,0]
        # = [V₁·D₂, D₁·V₂, R₁ scaled appropriately]
        #
        # Dividing by closed [V₂,D₂,0] is multiplying by [D₂,V₂,0]
        return active_mul(a, VDR(b.d, b.v))

    # b is active: construct exact inverse if possible
    b_frac = b.to_fraction()
    if b_frac == 0:
        raise ArithmeticFailure("Division by zero (active object projects to 0)")

    # The inverse of b as a closed VDR from its projected value
    b_inv = VDR(b_frac.denominator, b_frac.numerator)

    # Multiply a by the exact inverse
    # This loses the structural remainder information of b,
    # collapsing it through projection. This is the v1 compromise:
    # division by active objects goes through the projection boundary.
    return active_mul(a, b_inv)


def _mul_cross_terms(a, b):
    # type: (VDR, VDR) -> Remainder
    """
    Construct the remainder from multiplying two VDR objects.

    [V₁,D₁,R₁] × [V₂,D₂,R₂]

    The product sits in denominator frame D₁·D₂ with closed numerator V₁·V₂.

    The remainder captures:
      1. V₁ × R₂  (first value times second remainder)
      2. V₂ × R₁  (second value times first remainder)
      3. R₁ × R₂  (remainder times remainder)

    Each of these must be expressed as valid remainder structure
    in the D₁·D₂ frame.
    """
    # Contribution 1: V₁ × R₂
    # In the D₁·D₂ frame, V₁ × R₂ contributes as remainder
    # scaled by V₁ in the D₂ sub-frame
    left = _scale_remainder(b.r, a.v)  # V₁ · R₂

    # Contribution 2: V₂ × R₁
    right = _scale_remainder(a.r, b.v)  # V₂ · R₁

    # Contribution 3: R₁ × R₂
    cross = _mul_remainders(a.r, b.r, a.d, b.d)

    # Combine all three contributions
    result = _combine_three(left, right, cross)

    return result


def _scale_remainder(r, k):
    # type: (Remainder, int) -> Remainder
    """
    Multiply a remainder by an integer scalar.

    k · (base + X₁ + ... + Xₙ) = k·base + k·X₁ + ... + k·Xₙ

    For child VDR [V,D,R]: k · [V,D,R] = [k·V, D, k·R]
    """
    if k == 0:
        return Remainder(0)
    return Remainder(
        r.base * k,
        [VDR(k * c.v, c.d, _scale_remainder(c.r, k)) for c in r.children],
    )


def _mul_remainders(r1, r2, d1, d2):
    # type: (Remainder, Remainder, int, int) -> Remainder
    """
    Multiply two remainders: R₁ × R₂

    In the parent frame D₁·D₂, the product of remainders contributes
    as exact structure.

    For atomic remainders r₁, r₂:
        r₁ × r₂ is just an integer product in the remainder.
        But this integer lives in the "remainder × remainder" space,
        which in the D₁·D₂ frame means it needs to be expressed
        as a child VDR with appropriate denominator.

    Strategy: compute the exact rational value of R₁ × R₂ (via legacy)
    and express it as remainder structure in the D₁·D₂ frame.
    """
    # Get exact rational values of both remainders
    # R₁ contributes ρ(R₁)/D₁ to the first operand's value
    # R₂ contributes ρ(R₂)/D₂ to the second operand's value
    # Their product contributes ρ(R₁)·ρ(R₂)/(D₁·D₂) to the full product
    #
    # In the D₁·D₂ frame, this means the remainder contribution is:
    # ρ(R₁) · ρ(R₂) as a numerator-side value
    #
    # But ρ(R₁) and ρ(R₂) may be rational (if children exist),
    # so we compute exactly.

    val1 = r1.legacy_value()  # exact Fraction
    val2 = r2.legacy_value()  # exact Fraction

    product = val1 * val2  # exact Fraction

    if product == 0:
        return Remainder(0)

    # Express this as remainder structure.
    # The product ρ(R₁)·ρ(R₂) needs to be a remainder in the D₁·D₂ frame.
    # Since the parent VDR already has denominator D₁·D₂,
    # and the remainder is interpreted as numerator-side completion,
    # we need: a remainder R such that legacy_value(R) = product
    #
    # Simplest exact form: if product is integer, use atomic remainder.
    # If rational, use a closed child VDR.

    if product.denominator == 1:
        return Remainder(int(product))

    return Remainder(0, [
        VDR(int(product.numerator), int(product.denominator))
    ])


def _combine_three(r1, r2, r3):
    # type: (Remainder, Remainder, Remainder) -> Remainder
    """Combine three remainder contributions into one."""
    base = r1.base + r2.base + r3.base
    children = list(r1.children) + list(r2.children) + list(r3.children)
    return Remainder(base, children)


# ---------------------------------------------------------------------------
# Installation: patch VDR operators
# ---------------------------------------------------------------------------

# Save originals for fallback
_original_mul = VDR.__mul__
_original_rmul = VDR.__rmul__
_original_div = VDR.__truediv__
_original_rdiv = VDR.__rtruediv__


def _patched_mul(self, other):
    # type: (VDR, Union[VDR, int, Fraction]) -> VDR
    from vdr.vdr import _coerce
    other = _coerce(other)
    return active_mul(self, other)


def _patched_rmul(self, other):
    # type: (VDR, Union[int, Fraction]) -> VDR
    from vdr.vdr import _coerce
    return active_mul(self, _coerce(other))


def _patched_div(self, other):
    # type: (VDR, Union[VDR, int, Fraction]) -> VDR
    from vdr.vdr import _coerce
    other = _coerce(other)
    return active_div(self, other)


def _patched_rdiv(self, other):
    # type: (VDR, Union[int, Fraction]) -> VDR
    from vdr.vdr import _coerce
    return active_div(_coerce(other), self)


def install():
    """
    Patch VDR with active multiplication and division.

        import vdr.active_mul
        vdr.active_mul.install()

    After this call, VDR * and / operators handle active objects.
    """
    VDR.__mul__ = _patched_mul
    VDR.__rmul__ = _patched_rmul
    VDR.__truediv__ = _patched_div
    VDR.__rtruediv__ = _patched_rdiv


def uninstall():
    """Restore original VDR operators (active mul/div raises)."""
    VDR.__mul__ = _original_mul
    VDR.__rmul__ = _original_rmul
    VDR.__truediv__ = _original_div
    VDR.__rtruediv__ = _original_rdiv
    