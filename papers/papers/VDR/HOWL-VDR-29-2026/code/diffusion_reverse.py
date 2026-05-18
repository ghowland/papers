# diffusion_reverse.py
"""
Exact reverse diffusion process over VDR fractions.

The reverse process denoises:
    p(xₜ₋₁ | xₜ) = N(μₜ, β̃ₜ·I)

where:
    μₜ = (1/√αₜ) · (xₜ - βₜ/√(1-ᾱₜ) · ε_pred)

    β̃ₜ = βₜ · (1-ᾱₜ₋₁) / (1-ᾱₜ)

ε_pred comes from a neural network (or for testing, is provided
directly as an exact rational vector).

Every operation is exact VDR arithmetic.
"""

from __future__ import annotations
from typing import List, Optional, Callable

from vdr.vdr import VDR, VDRError
from vdr.linalg import Vec
from diffusion_schedule import Schedule, exact_sqrt

__all__ = [
    "reverse_step",
    "reverse_step_ddim",
    "reverse_sample_loop",
    "compute_posterior_mean",
    "compute_x0_prediction",
]


def compute_x0_prediction(xt, t, schedule, eps_pred):
    # type: (Vec, int, Schedule, Vec) -> Vec
    """
    Predict x₀ from xₜ and predicted noise:

        x̂₀ = (xₜ - √(1-ᾱₜ) · ε_pred) / √ᾱₜ

    Exact VDR arithmetic. The division by √ᾱₜ is division
    by an exact rational (the Newton iterate).
    """
    sqrt_ab = schedule.sqrt_alpha_bars[t]
    sqrt_one_minus = schedule.sqrt_one_minus_ab[t]

    # xₜ - √(1-ᾱₜ)·ε_pred
    noise_component = eps_pred.scale(sqrt_one_minus)
    signal = xt - noise_component

    # divide by √ᾱₜ
    recip_sqrt_ab = VDR(1) / sqrt_ab
    return signal.scale(recip_sqrt_ab)


def compute_posterior_mean(xt, t, schedule, eps_pred):
    # type: (Vec, int, Schedule, Vec) -> Vec
    """
    Posterior mean for reverse step:

        μₜ = (1/√αₜ) · (xₜ - βₜ/√(1-ᾱₜ) · ε_pred)

    Exact VDR. All coefficients are exact rationals.
    """
    sqrt_recip_alpha = schedule.sqrt_recip_alphas[t]
    beta = schedule.betas[t]
    sqrt_one_minus_ab = schedule.sqrt_one_minus_ab[t]

    # βₜ / √(1-ᾱₜ)
    noise_coeff = beta / sqrt_one_minus_ab

    # xₜ - noise_coeff · ε_pred
    adjusted = xt - eps_pred.scale(noise_coeff)

    # (1/√αₜ) · adjusted
    return adjusted.scale(sqrt_recip_alpha)


def reverse_step(xt, t, schedule, eps_pred, z=None):
    # type: (Vec, int, Schedule, Vec, Optional[Vec]) -> Vec
    """
    Single reverse diffusion step from xₜ to xₜ₋₁:

        xₜ₋₁ = μₜ + √β̃ₜ · z

    where z is optional noise (zero for deterministic sampling,
    rational vector for stochastic).

    For t=0 (final step), no noise is added regardless of z.

    Exact VDR arithmetic throughout.
    """
    mu = compute_posterior_mean(xt, t, schedule, eps_pred)

    if t == 0:
        return mu

    if z is None:
        return mu

    # posterior variance
    post_var = schedule.posterior_variance(t)
    sqrt_post_var = exact_sqrt(post_var, schedule.sqrt_depth)

    noise_term = z.scale(sqrt_post_var)
    return mu + noise_term


def reverse_step_ddim(xt, t, t_prev, schedule, eps_pred, eta=VDR(0)):
    # type: (Vec, int, int, Schedule, Vec, VDR) -> Vec
    """
    DDIM reverse step (deterministic when eta=0):

        x̂₀ = (xₜ - √(1-ᾱₜ)·ε_pred) / √ᾱₜ

        xₜ₋₁ = √ᾱₜ₋₁ · x̂₀ + √(1-ᾱₜ₋₁ - σ²) · ε_pred + σ·z

    where σ = η · √((1-ᾱₜ₋₁)/(1-ᾱₜ)) · √βₜ

    When η=0 this is fully deterministic — same inputs always
    produce same outputs. Exact VDR throughout.
    """
    # predict x0
    x0_pred = compute_x0_prediction(xt, t, schedule, eps_pred)

    if t_prev < 0:
        return x0_pred

    ab_t = schedule.alpha_bars[t]
    ab_prev = schedule.alpha_bars[t_prev]

    sqrt_ab_prev = schedule.sqrt_alpha_bars[t_prev]

    one = VDR(1)
    one_minus_ab_prev = one - ab_prev

    # direction pointing to xt
    if eta == VDR(0):
        # deterministic: no sigma term
        dir_coeff = exact_sqrt(one_minus_ab_prev, schedule.sqrt_depth)
        x_prev = x0_pred.scale(sqrt_ab_prev) + eps_pred.scale(dir_coeff)
        return x_prev

    # stochastic DDIM with eta > 0
    one_minus_ab_t = one - ab_t
    sigma_sq = eta * eta * (one_minus_ab_prev / one_minus_ab_t) * schedule.betas[t]
    sigma = exact_sqrt(sigma_sq, schedule.sqrt_depth)

    dir_coeff = exact_sqrt(one_minus_ab_prev - sigma_sq, schedule.sqrt_depth)

    x_prev = x0_pred.scale(sqrt_ab_prev) + eps_pred.scale(dir_coeff)
    # noise term omitted when z not provided (deterministic path)
    return x_prev


def reverse_sample_loop(xT, schedule, predict_noise, noise_vectors=None):
    # type: (Vec, Schedule, Callable[[Vec, int], Vec], Optional[List[Vec]]) -> List[Vec]
    """
    Full reverse sampling loop from xₜ to x₀.

    predict_noise(xt, t) returns ε_pred as exact Vec.
    noise_vectors[t] provides z for stochastic sampling (None for deterministic).

    Returns trajectory [xₜ, xₜ₋₁, ..., x₀].
    """
    trajectory = [xT]
    xt = xT
    for t in range(schedule.T - 1, -1, -1):
        eps_pred = predict_noise(xt, t)
        z = None
        if noise_vectors is not None and t > 0:
            z = noise_vectors[t]
        xt = reverse_step(xt, t, schedule, eps_pred, z)
        trajectory.append(xt)
    return trajectory

