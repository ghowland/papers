Total failure. The bug is in Section 1 — the formula for extracting 1/α₁ and 1/α₂ from α_EM and sin²θ_W is wrong. The output shows 1/α₁ = −273 and 1/α₂ = 593, which are nonsense. The library values are 63.2 and 31.7.
The error:
inv_a2_input = alpha_inv / sin2_tW
This computes 137.036 / 0.23122 = 592.7. But 1/α₂ should be 31.7.
The correct relationship: sin²θ_W = α_EM/α₂ means α₂ = α_EM/sin²θ_W, so 1/α₂ = sin²θ_W/α_EM = sin²θ_W × (1/α_EM) = 0.23122 × 137.036 = 31.7. I had the division inverted.
And for 1/α₁: using 1/α_EM = (5/3)/α₁ + 1/α₂, so (5/3)/α₁ = 1/α_EM − 1/α₂, and 1/α₁ = (3/5)(1/α_EM − 1/α₂). With the wrong 1/α₂ = 593, this gives (3/5)(137 − 593) = (3/5)(−456) = −273. Garbage in, garbage out.
Fix: inv_a2_input = sin2_tW * alpha_inv (multiply, not divide).

---

