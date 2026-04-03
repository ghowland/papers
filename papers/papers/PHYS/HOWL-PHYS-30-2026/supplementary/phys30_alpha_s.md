Total failure. The bug is in Section 1 — the formula for extracting 1/α₁ and 1/α₂ from α_EM and sin²θ_W is wrong. The output shows 1/α₁ = −273 and 1/α₂ = 593, which are nonsense. The library values are 63.2 and 31.7.
The error:
inv_a2_input = alpha_inv / sin2_tW
This computes 137.036 / 0.23122 = 592.7. But 1/α₂ should be 31.7.
The correct relationship: sin²θ_W = α_EM/α₂ means α₂ = α_EM/sin²θ_W, so 1/α₂ = sin²θ_W/α_EM = sin²θ_W × (1/α_EM) = 0.23122 × 137.036 = 31.7. I had the division inverted.
And for 1/α₁: using 1/α_EM = (5/3)/α₁ + 1/α₂, so (5/3)/α₁ = 1/α_EM − 1/α₂, and 1/α₁ = (3/5)(1/α_EM − 1/α₂). With the wrong 1/α₂ = 593, this gives (3/5)(137 − 593) = (3/5)(−456) = −273. Garbage in, garbage out.
Fix: inv_a2_input = sin2_tW * alpha_inv (multiply, not divide).

---

The input derivation is now correct (S1 PASS EXACT). The structural problem is physics: the one-loop α_s prediction misses by 12%, not 1-2%.This is NOT symmetric with the PHYS-27 sin²θ_W prediction (1.2% miss). The asymmetry: sin²θ_W is a RATIO of couplings (α₁/α₂), so the one-loop errors partially cancel. But α_s is the ABSOLUTE value of the third coupling, so the full one-loop Delta = −1.17 translates directly into a 12% miss in α_s.The 12% miss IS the Delta = −1.17 seen from below. Delta = −1.17 means 1/α₃ at M_GUT is 1.17 below 1/α_GUT. Running this deficit back down to M_Z: 1/α₃ is predicted too high (9.65 vs measured 8.47), so α_s is predicted too low (0.104 vs 0.118).At two loops, Delta improves to −0.40, which would give a much better α_s prediction. The two-loop α_s miss should be ~4% (proportional to 0.40/1.17 × 12% ≈ 4.1%). This is still outside 3σ but much closer.The script is correct. The checks need to reflect the ACTUAL physics: one-loop α_s prediction has a 12% miss, the abort test should use a 15% threshold (not 3σ), and the two-loop estimate should be computed.

---

