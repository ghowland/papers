"""
VDR — Value Denominator Remainder
Exact finite discrete representation.

    from vdr import VDR, Vec, Mat

    x = VDR(1, 2) + VDR(1, 3)  # exact rational arithmetic
    m = Mat.identity(3)          # exact linear algebra
"""

from vdr.vdr import VDR, Remainder, VDRError
from vdr.linalg import Vec, Mat, LinAlgError, parse_vdr, vdr_to_dict, vdr_from_dict, vdr_to_latex
from vdr.export import to_decimal, to_float, to_fraction

# Auto-install active multiplication/division
import vdr.active_mul
vdr.active_mul.install()

# Auto-install Functions
from vdr.fn import (
    FnRemainder, vdr_fn, resolve, is_functional,
    make_constant_fn, make_series_fn, make_newton_fn, make_iterative_fn,
    discrete_derivative, discrete_integral, discrete_integral_trapz,
    discrete_derivative_nth, resolve_recursive,
)
import vdr.fn
vdr.fn.install()

