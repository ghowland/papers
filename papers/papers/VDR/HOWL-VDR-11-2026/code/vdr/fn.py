"""
vdr.fn — Functional remainder for VDR objects.

Extends the remainder slot to hold a callable that produces VDR structure
on demand. This is how VDR replaces limits with recursion.

A functional remainder is:
    - a Python callable that takes a depth integer and returns a VDR object
    - a name string for inspectability
    - an optional metadata dict

The function is finite (it has finite source). The structure it produces
at any depth is finite and exact. Expansion is on demand via .resolve(depth).

    from vdr.fn import FnRemainder, vdr_fn

    @vdr_fn("sqrt2_step")
    def sqrt2_step(depth):
        '''Newton-Raphson for x^2 = 2, each step exact VDR rational.'''
        x = VDR(1)
        for _ in range(depth):
            x = (x + VDR(2) / x) / VDR(2)
        return x

    obj = VDR(1, 1, FnRemainder(sqrt2_step))
    print(obj.resolve(5))   # 5 Newton steps, exact rational

Completion semantics: a functional remainder is exact at every finite
depth of expansion. It is not an approximation — it is a recursive
specification that produces exact structure on demand.

The modulus: the parent denominator D constrains interpretation.
When resolved, the function's output is placed in the remainder slot
and the parent VDR is re-normalized. The depth parameter controls
how many recursive expansion steps are taken.
"""

from __future__ import annotations
from fractions import Fraction
from typing import Callable, Optional, Dict, Any, Union

from vdr.vdr import VDR, Remainder, VDRError, InvalidStructureError

__all__ = [
    "FnRemainder", "vdr_fn", "resolve", "is_functional",
    "make_constant_fn", "make_series_fn", "make_newton_fn",
    "install",
]


# ---------------------------------------------------------------------------
# FnRemainder
# ---------------------------------------------------------------------------

class FnRemainder(Remainder):
    """
    A remainder slot holding a callable instead of (or in addition to)
    concrete integer/child structure.

    The callable signature is:  f(depth: int) -> VDR

    At any given depth, the function produces an exact finite VDR object.
    There is no limit process. Each depth is a complete exact answer.

        fr = FnRemainder(my_func, name="sqrt2")
        result = fr.expand(5)   # calls my_func(5), returns VDR
    """

    __slots__ = ("func", "name", "meta")

    def __init__(self, func, name=None, meta=None):
        # type: (Callable[[int], VDR], Optional[str], Optional[Dict[str, Any]]) -> None
        super(FnRemainder, self).__init__(0, [])
        if not callable(func):
            raise InvalidStructureError(
                "FnRemainder requires a callable, got %s" % type(func).__name__
            )
        self.func = func
        self.name = name or getattr(func, "__name__", "<fn>")
        self.meta = meta or {}

    @property
    def is_zero(self):
        # type: () -> bool
        return False  # functional remainder is never zero

    @property
    def is_atomic(self):
        # type: () -> bool
        return False

    @property
    def is_functional(self):
        # type: () -> bool
        return True

    @property
    def is_globally_zero(self):
        # type: () -> bool
        return False

    def expand(self, depth):
        # type: (int) -> VDR
        """
        Expand the function at the given depth.
        Returns an exact finite VDR object.
        """
        if depth < 0:
            raise VDRError("Expansion depth must be non-negative")
        result = self.func(depth)
        if not isinstance(result, VDR):
            raise VDRError(
                "FnRemainder '%s' returned %s, expected VDR" % (
                    self.name, type(result).__name__
                )
            )
        return result

    def legacy_value(self):
        # type: () -> Fraction
        """
        Functional remainder has no default scalar projection.
        Expand first, then project.
        """
        raise VDRError(
            "Cannot project functional remainder '%s' without expansion. "
            "Call .resolve(depth) first." % self.name
        )

    def negate(self):
        # type: () -> FnRemainder
        def negated(depth):
            return -self.func(depth)
        return FnRemainder(negated, name="-%s" % self.name, meta=self.meta)

    def lift(self, k):
        # type: (int) -> FnRemainder
        def lifted(depth):
            result = self.func(depth)
            return result._lift_vdr(k)
        return FnRemainder(lifted, name="lift(%s,%d)" % (self.name, k), meta=self.meta)

    def structural_eq(self, other):
        # type: (Remainder) -> bool
        if not isinstance(other, FnRemainder):
            return False
        # function identity: same callable object and same name
        return self.func is other.func and self.name == other.name

    def normalize(self):
        # type: () -> FnRemainder
        # functional remainders don't normalize — expand first
        return self

    def combine(self, other, sign=1):
        # type: (Remainder, int) -> Remainder
        """
        Combining a functional remainder with another remainder.
        If both are functional, compose them.
        If one is concrete, wrap in a hybrid.
        """
        if isinstance(other, FnRemainder):
            fn_a = self.func
            fn_b = other.func
            s = sign
            name_b = other.name
            def combined(depth):
                a_val = fn_a(depth)
                b_val = fn_b(depth)
                if s == 1:
                    return a_val + b_val
                else:
                    return a_val - b_val
            op = "+" if sign == 1 else "-"
            return FnRemainder(
                combined,
                name="(%s %s %s)" % (self.name, op, name_b),
            )
        # other is concrete Remainder — expand self at depth 0 and combine
        # This is the conservative path: we don't lose the function,
        # we wrap it
        fn_a = self.func
        concrete = other
        s = sign
        def hybrid(depth):
            a_val = fn_a(depth)
            # convert concrete remainder to a VDR for combination
            concrete_vdr = VDR(0, 1, concrete)
            if s == 1:
                return a_val + concrete_vdr
            else:
                return a_val - concrete_vdr
        return FnRemainder(
            hybrid,
            name="(%s + concrete)" % self.name,
        )

    def __repr__(self):
        # type: () -> str
        return "fn:%s" % self.name


# ---------------------------------------------------------------------------
# Decorator for creating named VDR functions
# ---------------------------------------------------------------------------

def vdr_fn(name=None):
    # type: (Optional[str]) -> Callable
    """
    Decorator for creating named VDR remainder functions.

        @vdr_fn("sqrt2")
        def sqrt2(depth):
            x = VDR(1)
            for _ in range(depth):
                x = (x + VDR(2) / x) / VDR(2)
            return x
    """
    def decorator(func):
        func._vdr_fn_name = name or func.__name__
        return func
    return decorator


# ---------------------------------------------------------------------------
# resolve: expand a VDR with functional remainder
# ---------------------------------------------------------------------------

def resolve(x, depth=1):
    # type: (VDR, int) -> VDR
    """
    Resolve a VDR object by expanding any functional remainder.

    If the remainder is functional, expand it at the given depth
    and construct a concrete VDR result.

    If the remainder is already concrete, return the object unchanged.

        resolved = resolve(obj, depth=10)
    """
    if not is_functional(x):
        return x

    fn_r = x.r  # type: FnRemainder
    expanded = fn_r.expand(depth)

    # The expanded VDR replaces the functional remainder.
    # The parent frame [V, D, _] wraps the expanded result.
    #
    # Interpretation: the functional remainder produces a VDR
    # whose value completes the parent. Under completion semantics:
    #
    #   [V, D, fn] resolved at depth N →
    #   [V, D, expanded_as_remainder]
    #
    # where expanded_as_remainder is the expansion placed in R.

    if x.v == 0 and x.d == 1:
        # trivial frame: the function IS the value
        return expanded

    # non-trivial frame: expanded value goes into remainder
    # The expanded VDR becomes a child in the remainder
    if expanded.is_closed and expanded.v == 0:
        # expansion produced zero — close the parent
        return VDR(x.v, x.d).normalize()

    new_r = Remainder(0, [expanded])
    return VDR(x.v, x.d, new_r).normalize()


def is_functional(x):
    # type: (VDR) -> bool
    """Check if a VDR object has a functional remainder."""
    return isinstance(x.r, FnRemainder)


def resolve_recursive(x, depth=1):
    # type: (VDR, int) -> VDR
    """
    Resolve all functional remainders in a VDR tree, recursively.
    """
    if is_functional(x):
        x = resolve(x, depth)

    if x.r.is_zero or x.r.is_atomic:
        return x

    # resolve children
    new_children = []
    for c in x.r.children:
        new_children.append(resolve_recursive(c, depth))

    return VDR(x.v, x.d, Remainder(x.r.base, new_children)).normalize()


# ---------------------------------------------------------------------------
# Factory functions for common patterns
# ---------------------------------------------------------------------------

def make_constant_fn(name, value_func):
    # type: (str, Callable[[], VDR]) -> FnRemainder
    """
    Create a functional remainder that always returns the same value
    regardless of depth. Useful for named constants.

        pi_approx = make_constant_fn("pi_22_7", lambda: VDR(22, 7))
    """
    def const(depth):
        return value_func()
    return FnRemainder(const, name=name)


def make_series_fn(name, term_func, initial=None):
    # type: (str, Callable[[int], VDR], Optional[VDR]) -> FnRemainder
    """
    Create a functional remainder from a series.

    term_func(n) returns the nth exact rational term.
    At depth N, the result is the sum of terms 0..N.

        # Leibniz series for pi/4: 1 - 1/3 + 1/5 - 1/7 + ...
        def leibniz_term(n):
            sign = 1 if n % 2 == 0 else -1
            return VDR(sign, 2*n + 1)

        pi_fn = make_series_fn("leibniz_pi4", leibniz_term)
    """
    start = initial if initial is not None else VDR(0)
    init = start

    def series(depth):
        total = init
        for n in range(depth + 1):
            total = total + term_func(n)
        return total

    return FnRemainder(series, name=name)


def make_newton_fn(name, f_step):
    # type: (str, Callable[[VDR], VDR]) -> FnRemainder
    """
    Create a functional remainder from Newton-Raphson iteration.

    f_step(x) takes current VDR approximation and returns next one.
    Each step is exact rational arithmetic.

        # sqrt(2): x_{n+1} = (x + 2/x) / 2
        sqrt2_fn = make_newton_fn("sqrt2", lambda x: (x + VDR(2)/x) / VDR(2))

    The initial value is determined by depth=0 expansion of the function.
    At depth 0, returns f_step applied to VDR(1).
    At depth N, applies f_step N times starting from VDR(1).
    """
    def newton(depth):
        x = VDR(1)
        for _ in range(depth):
            x = f_step(x)
        return x

    return FnRemainder(newton, name=name)


def make_iterative_fn(name, step, start):
    # type: (str, Callable[[VDR], VDR], VDR) -> FnRemainder
    """
    General iterative function: apply step N times to start.

        fn = make_iterative_fn("collatz", collatz_step, VDR(27))
    """
    init = start
    def iterate(depth):
        x = init
        for _ in range(depth):
            x = step(x)
        return x

    return FnRemainder(iterate, name=name, meta={"start": str(start)})


# ---------------------------------------------------------------------------
# Discrete calculus operators
# ---------------------------------------------------------------------------

def discrete_derivative(f, h):
    # type: (Callable[[VDR], VDR], VDR) -> Callable[[VDR], VDR]
    """
    Discrete derivative operator.

    Given f: VDR → VDR and step size h (VDR rational),
    returns Df where:

        Df(x) = (f(x + h) - f(x)) / h

    Every evaluation is exact VDR arithmetic. No limits.

        f = lambda x: x * x
        df = discrete_derivative(f, VDR(1, 1000))
        print(df(VDR(3)))  # ≈ 6, exact at step size 1/1000
    """
    step = h
    def deriv(x):
        return (f(x + step) - f(x)) / step
    return deriv


def discrete_integral(f, a, b, n):
    # type: (Callable[[VDR], VDR], VDR, VDR, int) -> VDR
    """
    Discrete integral (left Riemann sum).

    Computes the exact sum:
        Σ f(a + k·h) · h   for k = 0, 1, ..., n-1

    where h = (b - a) / n.

    Every term is exact VDR arithmetic. No limits.
    Increasing n gives finer resolution. Each n gives an exact answer.

        # integral of x^2 from 0 to 1 with 100 steps
        result = discrete_integral(lambda x: x*x, VDR(0), VDR(1), 100)
    """
    if n <= 0:
        raise VDRError("Number of steps must be positive")
    h = (b - a) / VDR(n)
    total = VDR(0)
    for k in range(n):
        x_k = a + VDR(k) * h
        total = total + f(x_k) * h
    return total


def discrete_integral_trapz(f, a, b, n):
    # type: (Callable[[VDR], VDR], VDR, VDR, int) -> VDR
    """
    Discrete integral (trapezoidal rule).

    Computes:
        h/2 · (f(a) + 2·f(a+h) + 2·f(a+2h) + ... + 2·f(a+(n-1)h) + f(b))

    where h = (b - a) / n.

    More accurate than left Riemann for the same n.
    Still exact VDR arithmetic at every step.
    """
    if n <= 0:
        raise VDRError("Number of steps must be positive")
    h = (b - a) / VDR(n)
    total = f(a) + f(b)
    for k in range(1, n):
        x_k = a + VDR(k) * h
        total = total + VDR(2) * f(x_k)
    return total * h / VDR(2)


def discrete_derivative_nth(f, h, order=1):
    # type: (Callable[[VDR], VDR], VDR, int) -> Callable[[VDR], VDR]
    """
    Nth-order discrete derivative by repeated application.

    D^n f = D(D^(n-1) f)

    Each application is exact.
    """
    result = f
    for _ in range(order):
        result = discrete_derivative(result, h)
    return result


# ---------------------------------------------------------------------------
# Installation: make VDR aware of FnRemainder
# ---------------------------------------------------------------------------

_original_to_fraction = VDR.to_fraction
_original_is_closed = VDR.is_closed.fget
_original_is_active = VDR.is_active.fget


def _patched_to_fraction(self):
    # type: (VDR) -> Fraction
    if isinstance(self.r, FnRemainder):
        raise VDRError(
            "Cannot project VDR with functional remainder '%s'. "
            "Call resolve(obj, depth) first." % self.r.name
        )
    return _original_to_fraction(self)


def _patched_is_closed(self):
    # type: (VDR) -> bool
    if isinstance(self.r, FnRemainder):
        return False
    return _original_is_closed(self)


def _patched_is_active(self):
    # type: (VDR) -> bool
    if isinstance(self.r, FnRemainder):
        return True
    return _original_is_active(self)


def install():
    """
    Patch VDR to be aware of functional remainders.

        import vdr.fn
        vdr.fn.install()

    After this, VDR.to_fraction() will raise on functional remainders
    (forcing explicit resolve), and is_closed/is_active work correctly.
    """
    VDR.to_fraction = _patched_to_fraction
    VDR.is_closed = property(_patched_is_closed)
    VDR.is_active = property(_patched_is_active)


def uninstall():
    """Restore original VDR behavior."""
    VDR.to_fraction = _original_to_fraction
    VDR.is_closed = property(_original_is_closed)
    VDR.is_active = property(_original_is_active)
    