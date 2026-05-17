"""
vdr.export — Lossy export boundary.

This is where exact VDR precision ends and target-format precision begins.
Any loss belongs to the target format, not to VDR.

    from vdr.export import to_decimal, to_float

    x = VDR(1, 7)
    print(to_decimal(x, 50))   # 50 decimal digits, exact from VDR's Fraction
    print(to_float(x))         # lossy 64-bit float
"""

from __future__ import annotations
from fractions import Fraction
from typing import Union

from vdr.vdr import VDR

__all__ = ["to_decimal", "to_float", "to_fraction"]


def to_fraction(x):
    # type: (VDR) -> Fraction
    """
    Exact projection to fractions.Fraction.
    Lossless for closed objects. Legacy-flattened for active objects.
    """
    return x.to_fraction()


def to_float(x):
    # type: (VDR) -> float
    """
    Lossy projection to Python float (64-bit IEEE 754).
    Loss belongs to the float format.
    """
    return float(x.to_fraction())


def to_decimal(x, digits=50):
    # type: (VDR, int) -> str
    """
    Render VDR value as a decimal string with `digits` significant figures.

    Uses mpmath if available for arbitrary precision.
    Falls back to manual long division from Fraction if mpmath is not installed.

    The VDR value is exact. The decimal rendering is the lossy step.
    """
    frac = x.to_fraction()

    try:
        import mpmath
        mpmath.mp.dps = digits + 10  # extra guard digits
        val = mpmath.mpf(frac.numerator) / mpmath.mpf(frac.denominator)
        return mpmath.nstr(val, digits)
    except ImportError:
        pass

    # fallback: manual decimal from Fraction
    return _fraction_to_decimal(frac, digits)


def _fraction_to_decimal(frac, digits):
    # type: (Fraction, int) -> str
    """
    Convert Fraction to decimal string via long division.
    No external dependencies.
    """
    if frac < 0:
        return "-" + _fraction_to_decimal(-frac, digits)

    num = frac.numerator
    den = frac.denominator

    # integer part
    integer_part = num // den
    remainder = num % den

    if remainder == 0:
        s = str(integer_part)
        if digits > len(s):
            return s + "." + "0" * (digits - len(s))
        return s

    # fractional digits
    frac_digits = []
    for _ in range(digits):
        remainder *= 10
        digit = remainder // den
        remainder = remainder % den
        frac_digits.append(str(digit))
        if remainder == 0:
            break

    return "%d.%s" % (integer_part, "".join(frac_digits))
