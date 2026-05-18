
# diffusion_forward.py
"""
Exact forward diffusion process over VDR fractions.

The forward process adds noise to data:
    q(xₜ | x₀) = N(√ᾱₜ · x₀, (1-ᾱₜ)·I)

In the reparameterization form:
    xₜ = √ᾱₜ · x₀ + √(1-ᾱₜ) · ε

where ε is sampled noise. For exact arithmetic, ε must be
a rational vector (e.g., from a deterministic rational PRNG
or provided explicitly).

Every operation is exact VDR arithmetic.
"""

from __future__ import annotations
from typing import List

from vdr.vdr import VDR
from vdr.linalg import Vec
from diffusion_schedule import Schedule

__all__ = [
    "forward_sample",
    "forward_sample_step",
    "forward_trajectory",
]


def forward_sample(x0, t, schedule, epsilon):
    # type: (Vec, int, Schedule, Vec) -> Vec
    """
    Sample xₜ directly from x₀ using the closed-form:

        xₜ = √ᾱₜ · x₀ + √(1-ᾱₜ) · ε

    Inputs:
        x0       — clean data as Vec of VDR fractions
        t        — timestep (0-indexed into schedule)
        schedule — precomputed Schedule
        epsilon  — noise vector (rational, same dim as x0)

    Output:
        xₜ as Vec of exact VDR fractions

    No floats. No approximation beyond the Newton sqrt depth
    chosen when building the schedule.
    """
    sqrt_ab = schedule.sqrt_alpha_bars[t]
    sqrt_one_minus = schedule.sqrt_one_minus_ab[t]

    signal = x0.scale(sqrt_ab)
    noise = epsilon.scale(sqrt_one_minus)

    return signal + noise


def forward_sample_step(x_prev, t, schedule, epsilon):
    # type: (Vec, int, Schedule, Vec) -> Vec
    """
    Single forward step from xₜ₋₁ to xₜ:

        xₜ = √αₜ · xₜ₋₁ + √βₜ · ε

    This is the Markov transition, not the closed-form.
    Using it iteratively should give the same result as
    the closed-form (up to different noise draws).

    For deterministic testing with the same ε, the
    closed form and iterated form produce provably
    different results (different noise interpretation),
    but both are exact.
    """
    sqrt_a = schedule.sqrt_alphas[t]
    beta_t = schedule.betas[t]
    sqrt_beta = _exact_sqrt_cached(beta_t, schedule.sqrt_depth)

    signal = x_prev.scale(sqrt_a)
    noise = epsilon.scale(sqrt_beta)

    return signal + noise


def forward_trajectory(x0, schedule, epsilons):
    # type: (Vec, Schedule, List[Vec]) -> List[Vec]
    """
    Compute full forward trajectory x₀, x₁, ..., xₜ using
    closed-form at each step.

    epsilons[t] is the noise vector used at timestep t.

    Returns list of T+1 vectors: [x₀, x₁, ..., xₜ]
    """
    trajectory = [x0]
    for t in range(schedule.T):
        xt = forward_sample(x0, t, schedule, epsilons[t])
        trajectory.append(xt)
    return trajectory


def _exact_sqrt_cached(a, depth):
    # type: (VDR, int) -> VDR
    from diffusion_schedule import exact_sqrt
    return exact_sqrt(a, depth)
