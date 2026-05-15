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

