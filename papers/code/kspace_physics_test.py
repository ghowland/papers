from mpmath import mp, mpf
mp.dps = 50
import kspace_physics as ksp

M = ksp.M_now()
print("M =", M)
print("N =", ksp.N(M))
print("α⁻¹ =", ksp.alpha_inv(M))
print("α =", ksp.alpha(M))
print("α_s =", ksp.alpha_s(M))
print("sin²θ_W =", ksp.sin2_theta_W())
print("μ/e =", ksp.muon_to_electron(M))
print("τ/e =", ksp.tau_to_electron(M))
print("p/e =", ksp.proton_to_electron(M))
print("Ω_Λ =", ksp.Omega_Lambda(M))
print("g_e =", ksp.g_electron(M))
print("Δf =", ksp.Delta_f())

