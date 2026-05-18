# diffusion_sampling.py
"""
Exact diffusion sampling demonstrations over VDR fractions.

This module provides self-contained demonstrations of key diffusion
properties that VDR makes exactly verifiable:

1. Forward-reverse roundtrip (deterministic, known noise)
2. Schedule conservation (cumulative products exact)
3. Signal-to-noise monotonicity
4. Multi-step drift measurement (zero by construction)
5. Coefficient consistency checks
"""

from __future__ import annotations
from typing import List, Tuple

from vdr.vdr import VDR, VDRError
from vdr.linalg import Vec
from diffusion_schedule import Schedule, linear_schedule, exact_sqrt

__all__ = [
    "verify_schedule_consistency",
    "verify_snr_monotonic",
    "verify_coefficient_identity",
    "verify_forward_reverse_roundtrip",
    "verify_multi_step_drift",
    "make_oracle_predictor",
]


def verify_schedule_consistency(schedule):
    # type: (Schedule) -> List[Tuple[str, bool, str]]
    """
    Verify exact internal consistency of a noise schedule.

    Checks:
    1. αₜ = 1 - βₜ for all t
    2. ᾱₜ = ᾱₜ₋₁ · αₜ for all t > 0
    3. (√ᾱₜ)² ≈ ᾱₜ (within Newton residual)
    4. √ᾱₜ² + √(1-ᾱₜ)² = 1 (not exact due to Newton, but close)
    5. All βₜ in (0, 1)

    Returns list of (name, passed, detail) tuples.
    """
    results = []

    # check 1: α = 1 - β
    all_ok = True
    for t in range(schedule.T):
        expected = VDR(1) - schedule.betas[t]
        if schedule.alphas[t] != expected:
            all_ok = False
            break
    results.append(("alpha_equals_1_minus_beta", all_ok, "all t"))

    # check 2: cumulative product consistency
    all_ok = True
    cumulative = VDR(1)
    for t in range(schedule.T):
        cumulative = cumulative * schedule.alphas[t]
        if schedule.alpha_bars[t] != cumulative:
            all_ok = False
            break
    results.append(("alpha_bar_cumulative", all_ok, "all t"))

    # check 3: sqrt squared close to original
    all_ok = True
    for t in range(schedule.T):
        sq = schedule.sqrt_alpha_bars[t] * schedule.sqrt_alpha_bars[t]
        diff = sq - schedule.alpha_bars[t]
        diff_frac = diff.to_fraction()
        if abs(diff_frac) > 0:
            # Newton residual exists but should be tiny
            if abs(diff_frac) > __import__('fractions').Fraction(1, 10**15):
                all_ok = False
                break
    results.append(("sqrt_squared_consistency", all_ok, "residual < 10^-15"))

    # check 4: betas in (0, 1)
    all_ok = True
    for t in range(schedule.T):
        b = schedule.betas[t]
        if b <= VDR(0) or b >= VDR(1):
            all_ok = False
            break
    results.append(("betas_in_range", all_ok, "0 < β < 1"))

    # check 5: alpha_bars monotonically decreasing
    all_ok = True
    for t in range(1, schedule.T):
        if schedule.alpha_bars[t] >= schedule.alpha_bars[t - 1]:
            all_ok = False
            break
    results.append(("alpha_bar_decreasing", all_ok, "ᾱₜ < ᾱₜ₋₁"))

    return results


def verify_snr_monotonic(schedule):
    # type: (Schedule) -> Tuple[bool, List[VDR]]
    """
    Verify signal-to-noise ratio is monotonically decreasing.

    SNRₜ = ᾱₜ / (1 - ᾱₜ)

    Returns (is_monotonic, snr_values).
    """
    snrs = []
    one = VDR(1)
    for t in range(schedule.T):
        ab = schedule.alpha_bars[t]
        snr = ab / (one - ab)
        snrs.append(snr)

    is_mono = True
    for t in range(1, len(snrs)):
        if snrs[t] >= snrs[t - 1]:
            is_mono = False
            break

    return is_mono, snrs


def verify_coefficient_identity(schedule):
    # type: (Schedule) -> List[Tuple[int, VDR]]
    """
    Verify the coefficient identity at each timestep:

        (√ᾱₜ)² + (√(1-ᾱₜ))² should equal 1

    This won't be exact because √ is Newton-approximated,
    but the residual should be extremely small.

    Returns list of (t, residual) where residual = sum - 1.
    """
    results = []
    one = VDR(1)
    for t in range(schedule.T):
        s1 = schedule.sqrt_alpha_bars[t]
        s2 = schedule.sqrt_one_minus_ab[t]
        total = s1 * s1 + s2 * s2
        residual = total - one
        results.append((t, residual))
    return results


def make_oracle_predictor(x0, schedule):
    # type: (Vec, Schedule) -> callable
    """
    Create a perfect noise predictor for testing.

    Given that xₜ = √ᾱₜ·x₀ + √(1-ᾱₜ)·ε, the oracle knows
    x₀ and can compute the exact ε that was used:

        ε = (xₜ - √ᾱₜ·x₀) / √(1-ᾱₜ)

    This creates a predictor that, given xₜ and t, returns
    the exact noise. Used for roundtrip verification.
    """
    def predict(xt, t):
        # type: (Vec, int) -> Vec
        sqrt_ab = schedule.sqrt_alpha_bars[t]
        sqrt_one_minus = schedule.sqrt_one_minus_ab[t]
        recip = VDR(1) / sqrt_one_minus
        signal = x0.scale(sqrt_ab)
        noise = (xt - signal).scale(recip)
        return noise
    return predict


def verify_forward_reverse_roundtrip(x0, schedule, epsilon):
    # type: (Vec, Schedule, Vec) -> Tuple[bool, Vec, Vec, VDR]
    """
    Forward diffuse x₀ to xₜ, then reverse back to x₀ using
    an oracle noise predictor.

    With perfect noise prediction and deterministic sampling
    (no added noise in reverse), the roundtrip should recover
    x₀ exactly (within Newton sqrt residual).

    Returns (is_exact, recovered_x0, x0_original, max_elementwise_error).
    """
    from diffusion_forward import forward_sample
    from diffusion_reverse import reverse_step, compute_posterior_mean

    T = schedule.T

    # forward: jump directly to xₜ
    xT = forward_sample(x0, T - 1, schedule, epsilon)

    # build oracle
    oracle = make_oracle_predictor(x0, schedule)

    # reverse: deterministic (no noise)
    xt = xT
    for t in range(T - 1, -1, -1):
        eps_pred = oracle(xt, t)
        xt = reverse_step(xt, t, schedule, eps_pred, z=None)

    recovered = xt

    # measure error
    max_err = VDR(0)
    for i in range(len(x0)):
        diff = recovered[i] - x0[i]
        err = abs(diff)
        if err > max_err:
            max_err = err

    is_exact = (max_err == VDR(0))
    return is_exact, recovered, x0, max_err


def verify_multi_step_drift(x0, schedule, epsilon, num_cycles=3):
    # type: (Vec, Schedule, Vec, int) -> List[VDR]
    """
    Run forward-reverse cycles multiple times and measure drift.

    Each cycle: x₀ → xₜ → x₀'
    Next cycle uses x₀' as starting point.

    Float arithmetic would accumulate drift across cycles.
    VDR should show zero or near-zero drift at every cycle.

    Returns list of max errors per cycle.
    """
    from diffusion_forward import forward_sample
    from diffusion_reverse import reverse_step

    errors = []
    x_current = x0

    for cycle in range(num_cycles):
        # forward
        xT = forward_sample(x_current, schedule.T - 1, schedule, epsilon)

        # oracle for current x
        oracle = make_oracle_predictor(x_current, schedule)

        # reverse
        xt = xT
        for t in range(schedule.T - 1, -1, -1):
            eps_pred = oracle(xt, t)
            xt = reverse_step(xt, t, schedule, eps_pred, z=None)

        recovered = xt

        # measure error vs original x0 (not x_current)
        max_err = VDR(0)
        for i in range(len(x0)):
            diff = recovered[i] - x0[i]
            err = abs(diff)
            if err > max_err:
                max_err = err

        errors.append(max_err)
        x_current = recovered

    return errors

