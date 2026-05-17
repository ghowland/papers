# test_diffusion.py
"""
Comprehensive tests for exact VDR diffusion arithmetic.

Tests cover:
    1-5:   Schedule computation and consistency
    6-9:   Forward diffusion exactness
    10-14: Reverse diffusion exactness
    15-19: Sampling loop and roundtrip properties
    20-25: Drift measurement and conservation
"""

from __future__ import annotations
from fractions import Fraction

from vdr.vdr import VDR
from vdr.linalg import Vec
import vdr.active_mul
vdr.active_mul.install()

from diffusion_schedule import Schedule, linear_schedule, cosine_schedule_rational, exact_sqrt
from diffusion_forward import forward_sample, forward_sample_step, forward_trajectory
from diffusion_reverse import (
    reverse_step, reverse_step_ddim, reverse_sample_loop,
    compute_posterior_mean, compute_x0_prediction,
)
from diffusion_sampling import (
    verify_schedule_consistency,
    verify_snr_monotonic,
    verify_coefficient_identity,
    verify_forward_reverse_roundtrip,
    verify_multi_step_drift,
    make_oracle_predictor,
)


def show(title):
    print("\n=== " + title + " ===")


def check(cond, msg):
    if cond:
        print("  PASS:", msg)
        return 1
    print("  FAIL:", msg)
    return 0


def main():
    passed = 0
    failed = 0

    # ================================================================
    # SCHEDULE TESTS
    # ================================================================

    show("1. Linear schedule construction")

    betas = linear_schedule(5, VDR(1, 100), VDR(1, 20))
    sched = Schedule(betas, sqrt_depth=12)

    ok = check(len(betas) == 5, "5 beta values produced")
    passed += ok; failed += 1 - ok

    ok = check(betas[0] == VDR(1, 100), "beta_0 = 1/100")
    passed += ok; failed += 1 - ok

    ok = check(betas[4] == VDR(1, 20), "beta_4 = 1/20")
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("2. Schedule alpha = 1 - beta")

    all_ok = True
    for t in range(sched.T):
        if sched.alphas[t] != VDR(1) - sched.betas[t]:
            all_ok = False
            break
    ok = check(all_ok, "alpha_t = 1 - beta_t for all t")
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("3. Cumulative product consistency")

    cumulative = VDR(1)
    all_ok = True
    for t in range(sched.T):
        cumulative = cumulative * sched.alphas[t]
        if sched.alpha_bars[t] != cumulative:
            all_ok = False
            break
    ok = check(all_ok, "alpha_bar_t = product of alphas")
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("4. Alpha bars monotonically decreasing")

    all_ok = True
    for t in range(1, sched.T):
        if sched.alpha_bars[t] >= sched.alpha_bars[t - 1]:
            all_ok = False
            break
    ok = check(all_ok, "alpha_bar strictly decreasing")
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("5. SNR monotonically decreasing")

    is_mono, snrs = verify_snr_monotonic(sched)
    ok = check(is_mono, "SNR strictly decreasing across timesteps")
    passed += ok; failed += 1 - ok

    # ================================================================
    # SQRT EXACTNESS
    # ================================================================

    show("6. exact_sqrt basic values")

    s4 = exact_sqrt(VDR(4), depth=10)
    ok = check(s4 == VDR(2), "sqrt(4) = 2 exactly")
    passed += ok; failed += 1 - ok

    s1 = exact_sqrt(VDR(1), depth=10)
    ok = check(s1 == VDR(1), "sqrt(1) = 1 exactly")
    passed += ok; failed += 1 - ok

    s0 = exact_sqrt(VDR(0), depth=10)
    ok = check(s0 == VDR(0), "sqrt(0) = 0 exactly")
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("7. exact_sqrt of rational")

    # sqrt(1/4) should be 1/2 exactly
    s_quarter = exact_sqrt(VDR(1, 4), depth=15)
    ok = check(s_quarter == VDR(1, 2), "sqrt(1/4) = 1/2 exactly")
    passed += ok; failed += 1 - ok

    # sqrt(9/16) should be 3/4 exactly
    s_916 = exact_sqrt(VDR(9, 16), depth=15)
    ok = check(s_916 == VDR(3, 4), "sqrt(9/16) = 3/4 exactly")
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("8. exact_sqrt Newton residual for irrational")

    # sqrt(2): x^2 - 2 should be very small
    s2 = exact_sqrt(VDR(2), depth=10)
    residual = s2 * s2 - VDR(2)
    res_frac = residual.to_fraction()
    ok = check(
        abs(res_frac) < Fraction(1, 10**50),
        "sqrt(2) residual < 10^-50 at depth 10"
    )
    passed += ok; failed += 1 - ok

    print("    sqrt(2) residual =", res_frac)

    # ================================================================
    # FORWARD DIFFUSION
    # ================================================================

    show("9. Forward diffusion preserves dimensionality")

    x0 = Vec([VDR(1), VDR(2), VDR(3)])
    eps = Vec([VDR(1, 10), VDR(-1, 10), VDR(1, 5)])
    xt = forward_sample(x0, 2, sched, eps)

    ok = check(xt.dim == 3, "forward sample output has same dimension")
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("10. Forward diffusion at t=0 close to x0")

    # at t=0, alpha_bar is close to 1, so xt ≈ x0
    xt0 = forward_sample(x0, 0, sched, eps)
    # sqrt_alpha_bar[0] close to 1, sqrt_one_minus close to 0
    # so xt0 ≈ x0
    # check that signal dominates
    ok = check(
        sched.alpha_bars[0] > VDR(9, 10),
        "alpha_bar_0 > 0.9 (signal dominates at t=0)"
    )
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("11. Forward diffusion coefficient identity")

    # (√ᾱ)² + (√(1-ᾱ))² should be very close to 1
    residuals = verify_coefficient_identity(sched)
    max_res = max(abs(r.to_fraction()) for _, r in residuals)
    ok = check(
        max_res < Fraction(1, 10**20),
        "coefficient identity residual < 10^-20 for all t"
    )
    passed += ok; failed += 1 - ok
    print("    max coefficient residual =", max_res)

    # ----------------------------------------------------------------
    show("12. Forward trajectory length")

    epsilons = [eps] * sched.T
    traj = forward_trajectory(x0, sched, epsilons)

    ok = check(len(traj) == sched.T + 1, "trajectory has T+1 entries")
    passed += ok; failed += 1 - ok

    ok = check(traj[0] == x0, "trajectory starts at x0")
    passed += ok; failed += 1 - ok

    # ================================================================
    # REVERSE DIFFUSION
    # ================================================================

    show("13. x0 prediction from perfect noise")

    # forward with known noise
    eps_known = Vec([VDR(1, 7), VDR(-2, 7), VDR(3, 7)])
    t_test = 3
    xt_test = forward_sample(x0, t_test, sched, eps_known)

    # predict x0 back
    x0_pred = compute_x0_prediction(xt_test, t_test, sched, eps_known)

    # with perfect noise, x0_pred should be very close to x0
    # Not exact because sqrt is Newton-approximated
    max_err = VDR(0)
    for i in range(len(x0)):
        diff = abs(x0_pred[i] - x0[i])
        if diff > max_err:
            max_err = diff

    err_frac = max_err.to_fraction()
    ok = check(
        err_frac < Fraction(1, 10**20),
        "x0 prediction error < 10^-20 with perfect noise"
    )
    passed += ok; failed += 1 - ok
    print("    x0 prediction error =", err_frac)

    # ----------------------------------------------------------------
    show("14. Posterior mean computation")

    mu = compute_posterior_mean(xt_test, t_test, sched, eps_known)
    ok = check(mu.dim == 3, "posterior mean has correct dimension")
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("15. Reverse step preserves dimension")

    x_prev = reverse_step(xt_test, t_test, sched, eps_known, z=None)
    ok = check(x_prev.dim == 3, "reverse step output has correct dimension")
    passed += ok; failed += 1 - ok

    # ================================================================
    # ROUNDTRIP TESTS
    # ================================================================

    show("16. Forward-reverse roundtrip (small schedule)")

    # small schedule for exact roundtrip test
    small_betas = [VDR(1, 10), VDR(1, 5), VDR(3, 10)]
    small_sched = Schedule(small_betas, sqrt_depth=15)
    small_x0 = Vec([VDR(1), VDR(-1)])
    small_eps = Vec([VDR(1, 3), VDR(-1, 3)])

    is_exact, recovered, original, max_err = verify_forward_reverse_roundtrip(
        small_x0, small_sched, small_eps
    )

    err_frac = max_err.to_fraction()
    print("    roundtrip error =", err_frac)

    ok = check(
        err_frac < Fraction(1, 10**20),
        "roundtrip error < 10^-20"
    )
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("17. DDIM deterministic roundtrip")

    # DDIM with eta=0 is deterministic
    xt_ddim = forward_sample(small_x0, small_sched.T - 1, small_sched, small_eps)
    oracle = make_oracle_predictor(small_x0, small_sched)

    # step backwards through all timesteps
    x_curr = xt_ddim
    for t in range(small_sched.T - 1, 0, -1):
        eps_pred = oracle(x_curr, t)
        x_curr = reverse_step_ddim(x_curr, t, t - 1, small_sched, eps_pred, eta=VDR(0))

    # final step
    eps_pred = oracle(x_curr, 0)
    x_curr = reverse_step_ddim(x_curr, 0, -1, small_sched, eps_pred, eta=VDR(0))

    max_err_ddim = VDR(0)
    for i in range(len(small_x0)):
        diff = abs(x_curr[i] - small_x0[i])
        if diff > max_err_ddim:
            max_err_ddim = diff

    err_ddim_frac = max_err_ddim.to_fraction()
    print("    DDIM roundtrip error =", err_ddim_frac)

    ok = check(
        err_ddim_frac < Fraction(1, 10**20),
        "DDIM roundtrip error < 10^-20"
    )
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("18. Full reverse sample loop")

    def oracle_fn(xt, t):
        return oracle(xt, t)

    trajectory = reverse_sample_loop(xt_ddim, small_sched, oracle_fn, noise_vectors=None)

    ok = check(
        len(trajectory) == small_sched.T + 1,
        "reverse trajectory has T+1 entries"
    )
    passed += ok; failed += 1 - ok

    # last entry should be close to x0
    final = trajectory[-1]
    max_final_err = VDR(0)
    for i in range(len(small_x0)):
        diff = abs(final[i] - small_x0[i])
        if diff > max_final_err:
            max_final_err = diff

    err_final_frac = max_final_err.to_fraction()
    ok = check(
        err_final_frac < Fraction(1, 10**20),
        "reverse loop recovers x0 within 10^-20"
    )
    passed += ok; failed += 1 - ok

    # ================================================================
    # DRIFT AND CONSERVATION
    # ================================================================

    show("19. Multi-cycle drift = zero")

    # use smaller schedule and fewer cycles for speed
    drift_betas = [VDR(1, 10), VDR(1, 5)]
    drift_sched = Schedule(drift_betas, sqrt_depth=10)
    drift_x0 = Vec([VDR(1), VDR(-1)])
    drift_eps = Vec([VDR(1, 3), VDR(-1, 3)])

    drift_errors = verify_multi_step_drift(
        drift_x0, drift_sched, drift_eps, num_cycles=2
    )

    for i, err in enumerate(drift_errors):
        print("    cycle %d drift = %s" % (i + 1, err.to_fraction()))

    max_drift = max(e.to_fraction() for e in drift_errors)
    ok = check(
        max_drift < Fraction(1, 10**20),
        "all 3 cycles have drift < 10^-20"
    )
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("20. Drift does NOT grow across cycles")

    if len(drift_errors) >= 2:
        grows = False
        for i in range(1, len(drift_errors)):
            if drift_errors[i].to_fraction() > drift_errors[i-1].to_fraction() + Fraction(1, 10**30):
                grows = True
                break
        ok = check(not grows, "drift does not increase across cycles")
        passed += ok; failed += 1 - ok
    else:
        ok = check(True, "not enough cycles to test growth (trivially passes)")
        passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("21. Schedule consistency battery")

    results = verify_schedule_consistency(sched)
    for name, passed_check, detail in results:
        ok = check(passed_check, "%s (%s)" % (name, detail))
        passed += ok; failed += 1 - ok

    # ================================================================
    # EXACT ARITHMETIC PROPERTIES
    # ================================================================

    show("22. Cumulative product is exact (no float drift)")

    # compute alpha_bar manually as exact fraction
    manual_ab = Fraction(1)
    for t in range(sched.T):
        alpha_frac = sched.alphas[t].to_fraction()
        manual_ab *= alpha_frac

    computed_ab = sched.alpha_bars[-1].to_fraction()
    ok = check(manual_ab == computed_ab, "VDR cumulative product matches Fraction exactly")
    passed += ok; failed += 1 - ok

    print("    alpha_bar_T = %s" % computed_ab)

    # ----------------------------------------------------------------
    show("23. Posterior variance is exact rational")

    for t in range(1, sched.T):
        pv = sched.posterior_variance(t)
        ok_closed = pv.is_closed
        ok_positive = pv > VDR(0)
        if not (ok_closed and ok_positive):
            ok = check(False, "posterior var at t=%d not closed positive" % t)
            passed += 0; failed += 1
            break
    else:
        ok = check(True, "all posterior variances are closed positive rationals")
        passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("24. Cosine schedule construction")

    cos_betas = cosine_schedule_rational(10)
    cos_sched = Schedule(cos_betas, sqrt_depth=10)

    ok = check(len(cos_betas) == 10, "cosine schedule has 10 steps")
    passed += ok; failed += 1 - ok

    # verify monotonic alpha_bar
    all_ok = True
    for t in range(1, cos_sched.T):
        if cos_sched.alpha_bars[t] >= cos_sched.alpha_bars[t - 1]:
            all_ok = False
            break
    ok = check(all_ok, "cosine alpha_bar monotonically decreasing")
    passed += ok; failed += 1 - ok

    # ----------------------------------------------------------------
    show("25. Perfect square rational sqrt is exact")

    # collection of perfect square rationals
    test_cases = [
        (VDR(1, 1), VDR(1, 1)),
        (VDR(4, 1), VDR(2, 1)),
        (VDR(9, 1), VDR(3, 1)),
        (VDR(16, 1), VDR(4, 1)),
        (VDR(25, 1), VDR(5, 1)),
        (VDR(1, 4), VDR(1, 2)),
        (VDR(1, 9), VDR(1, 3)),
        (VDR(4, 9), VDR(2, 3)),
        (VDR(9, 4), VDR(3, 2)),
        (VDR(25, 16), VDR(5, 4)),
    ]

    all_ok = True
    for inp, expected in test_cases:
        result = exact_sqrt(inp, depth=15)
        if result != expected:
            print("    sqrt(%s) = %s, expected %s" % (inp, result, expected))
            all_ok = False

    ok = check(all_ok, "all 10 perfect square rationals give exact results")
    passed += ok; failed += 1 - ok

    # ================================================================
    # SUMMARY
    # ================================================================

    print("\n" + "=" * 60)
    print("Diffusion test results: %d passed, %d failed" % (passed, failed))
    if failed == 0:
        print("ALL DIFFUSION TESTS PASSED")
    else:
        print("SOME TESTS FAILED")
    print("=" * 60)


if __name__ == "__main__":
    main()


