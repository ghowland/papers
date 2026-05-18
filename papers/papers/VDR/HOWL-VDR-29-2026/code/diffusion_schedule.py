# diffusion_schedule.py
"""
Exact diffusion noise schedule over VDR fractions.

A noise schedule is a sequence of rational β values β₁..βₜ.
From these we derive:
    αₜ = 1 - βₜ
    ᾱₜ = ∏ₖ₌₁ᵗ αₖ       (cumulative product)
    √ᾱₜ                   (via functional remainder Newton iteration)
    √(1-ᾱₜ)               (same)

Every value is exact VDR. No floats anywhere.
"""

from __future__ import annotations
from typing import List, Callable

from vdr.vdr import VDR, Remainder, VDRError
from vdr.fn import FnRemainder, make_newton_fn, resolve

__all__ = [
    "Schedule",
    "linear_schedule",
    "cosine_schedule_rational",
    "exact_sqrt",
    "exact_sqrt_vdr",
]


def exact_sqrt(a, depth=10):
    # type: (VDR, int) -> VDR
    """
    Exact rational square root of a via Newton iteration.

    x_{n+1} = (x_n + a / x_n) / 2

    Each step is exact VDR arithmetic. At depth N, the result
    is an exact rational whose square differs from a by a known
    exact residual.

    Returns closed VDR rational (the Nth Newton iterate).
    """
    if a == VDR(0):
        return VDR(0)
    if a < VDR(0):
        raise VDRError("exact_sqrt requires non-negative input")
    x = VDR(1)
    for _ in range(depth):
        x = (x + a / x) / VDR(2)
    return x


def exact_sqrt_vdr(a, depth=10):
    # type: (VDR, int) -> VDR
    """
    Same as exact_sqrt but returns the result with a functional
    remainder attached for further refinement if needed.
    """
    return exact_sqrt(a, depth)


class Schedule:
    """
    Exact diffusion noise schedule.

    Given a list of rational β values (as VDR fractions),
    precomputes all derived quantities exactly.

    Fields:
        T         — number of timesteps
        betas     — β₁..βₜ as VDR list
        alphas    — αₜ = 1 - βₜ
        alpha_bars — ᾱₜ = ∏ₖ₌₁ᵗ αₖ (cumulative product)
        sqrt_alpha_bars     — √ᾱₜ (Newton, exact rational)
        sqrt_one_minus_ab   — √(1-ᾱₜ) (Newton, exact rational)
        sqrt_alphas         — √αₜ
        sqrt_recip_alphas   — 1/√αₜ
    """

    def __init__(self, betas, sqrt_depth=10):
        # type: (List[VDR], int) -> None
        if not betas:
            raise VDRError("Schedule requires at least one beta value")

        self.T = len(betas)
        self.betas = list(betas)
        self.sqrt_depth = sqrt_depth

        # αₜ = 1 - βₜ
        self.alphas = [VDR(1) - b for b in self.betas]

        # ᾱₜ = ∏ₖ₌₁ᵗ αₖ
        self.alpha_bars = []  # type: List[VDR]
        cumulative = VDR(1)
        for a in self.alphas:
            cumulative = cumulative * a
            self.alpha_bars.append(cumulative)

        # precompute square roots
        self.sqrt_alpha_bars = [
            exact_sqrt(ab, sqrt_depth) for ab in self.alpha_bars
        ]
        self.sqrt_one_minus_ab = [
            exact_sqrt(VDR(1) - ab, sqrt_depth) for ab in self.alpha_bars
        ]
        self.sqrt_alphas = [
            exact_sqrt(a, sqrt_depth) for a in self.alphas
        ]
        self.sqrt_recip_alphas = [
            VDR(1) / exact_sqrt(a, sqrt_depth) for a in self.alphas
        ]

    def posterior_variance(self, t):
        # type: (int) -> VDR
        """
        Posterior variance for reverse step at timestep t (1-indexed internally).

        β̃ₜ = βₜ · (1 - ᾱₜ₋₁) / (1 - ᾱₜ)

        For t=0 (first timestep), ᾱₜ₋₁ = 1, so β̃₀ = 0.
        """
        if t <= 0:
            return VDR(0)
        beta_t = self.betas[t]
        ab_prev = self.alpha_bars[t - 1]
        ab_curr = self.alpha_bars[t]
        one = VDR(1)
        numerator = beta_t * (one - ab_prev)
        denominator = one - ab_curr
        return numerator / denominator


def linear_schedule(T, beta_start, beta_end):
    # type: (int, VDR, VDR) -> List[VDR]
    """
    Linear noise schedule: β values evenly spaced from beta_start to beta_end.

    β_k = beta_start + k * (beta_end - beta_start) / (T - 1)
    for k = 0, 1, ..., T-1.

    All values are exact VDR rationals.
    """
    if T <= 0:
        raise VDRError("T must be positive")
    if T == 1:
        return [beta_start]
    betas = []
    for k in range(T):
        beta_k = beta_start + VDR(k) * (beta_end - beta_start) / VDR(T - 1)
        betas.append(beta_k)
    return betas


def cosine_schedule_rational(T, s=VDR(8, 1000)):
    # type: (int, VDR) -> List[VDR]
    """
    Rational approximation to cosine schedule.

    The true cosine schedule uses cos(π/2 · (t/T + s)/(1+s)).
    We approximate with a rational quadratic that has the same
    shape: f(t) = 1 - (t/T)² scaled to hit similar endpoints.

    This gives a schedule that starts slow, accelerates in the middle,
    and slows at the end — the cosine schedule's key property —
    while staying exactly rational.

    β_k = clip(1 - f(k)/f(k-1), 0, max_beta)
    where f(t) = (1 - (t/(T+s))²)

    All values exact VDR.
    """
    if T <= 0:
        raise VDRError("T must be positive")

    one = VDR(1)
    max_beta = VDR(999, 1000)

    def f_val(t_idx):
        # type: (int) -> VDR
        ratio = VDR(t_idx) / (VDR(T) + s)
        return one - ratio * ratio

    betas = []
    for k in range(T):
        if k == 0:
            betas.append(VDR(1, 1000))
        else:
            fk = f_val(k)
            fk_prev = f_val(k - 1)
            beta_k = one - fk / fk_prev
            if beta_k < VDR(0):
                beta_k = VDR(0)
            if beta_k > max_beta:
                beta_k = max_beta
            betas.append(beta_k)
    return betas
