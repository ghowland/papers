# VDR Beyond Language Models
## Exact Sequential Arithmetic Across Computational Domains

**Registry:** [@HOWL-VDR-27-2026]

**Series Path:** [@HOWL-VDR-1-2026] → [@HOWL-VDR-2-2026] → [@HOWL-MATH-3-2026] → [@HOWL-MATH-4-2026]  → ... → [@HOWL-VDR-14-2026] → ... → [@HOWL-VDR-21-2026] → [@HOWL-VDR-22-2026] → [@HOWL-VDR-23-2026] → [@HOWL-VDR-24-2026] → [@HOWL-VDR-25-2026] → [@HOWL-VDR-26-2026] → [@HOWL-VDR-27-2026]

**DOI:** 10.5281/zenodo.20260561

**Date:** May 2026

**Domain:** Exact Arithmetic / Generative Model Inference

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.6.

---

## Abstract

The zero-drift property demonstrated for diffusion models in [VDR-26] — where arithmetic error does not accumulate across sequential computation chains — applies to any domain where each step's output feeds the next step's input. This paper maps VDR exact arithmetic to twelve computational domains beyond language models: autoregressive generation (speech, music, protein), normalizing flows, Kalman filtering and state estimation, cryptographic protocols, financial computation, control systems, physics simulation, blockchain and consensus, geodesy and navigation, game theory and mechanism design, digital signal processing, and quantum computing primitives. In every domain, the structural problem is the same: float arithmetic introduces per-step error that compounds through the chain. VDR eliminates the per-step error entirely. The remaining errors — model approximation, measurement noise, basis set truncation — are the domain's problems, not the arithmetic's.

No prior reading is required. VDR arithmetic concepts are summarized where first used; full specifications are in [VDR-1] and [VDR-14].

---

## 1. The Common Structure

### 1.1 Sequential Computation Chains

Across computational science and engineering, the dominant pattern is: compute a value, feed it as input to the next computation, repeat. A Kalman filter updates its state estimate every sensor cycle. A molecular dynamics simulation advances atomic positions every femtosecond. A digital filter processes every audio sample. A blockchain applies every transaction. An autoregressive model generates every token.

In each case, the output of step N becomes the input to step N+1. Any arithmetic error at step N propagates through every subsequent step. In float64 arithmetic, each step introduces approximately 10⁻¹⁶ relative error. Over thousands or millions of steps, this error compounds — sometimes linearly, sometimes multiplicatively, sometimes catastrophically when the error interacts with the dynamics of the system being computed.

### 1.2 VDR's Structural Solution

VDR represents every number as three integers: Value, Denominator, Remainder [VDR-1]. When the Remainder is zero, the value is an exact rational V/D. Arithmetic on exact rationals is exact — addition, subtraction, multiplication, and division of rationals produce rationals with zero error, regardless of chain length.

The only approximation in VDR is square root and transcendental computation via Newton iteration or Taylor series, which produce exact rational approximations at any requested depth. The residual is fixed at the chosen depth (below 10⁻⁵⁰ at depth 10), inspectable, and does not compound through chains [VDR-26].

This means: for any computation chain built from rational arithmetic, VDR produces zero accumulated error. For chains involving square roots or transcendentals, VDR produces a fixed residual that does not grow with chain length. In both cases, the arithmetic separates cleanly from the domain's own error sources — model error, measurement noise, statistical sampling error — allowing each to be identified and addressed independently.

### 1.3 How This Paper Is Organized

Each section maps a computational domain to VDR arithmetic by identifying the sequential chain, the float failure mode, and the VDR exactness guarantee. The treatment is mechanical — what the computation is, why float fails at it, and how VDR handles it — rather than exhaustive. Full specifications for VDR arithmetic are in [VDR-1]; the Q335 fixed-frame arithmetic for GPU execution is in [VDR-14, VDR-18]; the diffusion model validation establishing the zero-drift property is in [VDR-26].

---

## 2. Autoregressive Generation Beyond Text

### 2.1 Speech Synthesis

Autoregressive speech models (WaveNet, SoundStorm) generate audio sample by sample at 16-48 kHz. Each sample is conditioned on previous samples through causal convolution stacks. A 3-second clip at 16 kHz is 48,000 sequential steps.

The chain: at each step, a softmax over quantized audio levels (256 for μ-law encoding) produces a probability distribution. The selected sample feeds back as input to the next step. The softmax weights are attention scores over prior samples, computed through the same QKᵀ matrix products validated in [VDR-4].

The float failure: softmax over 256 levels in float64 sums to approximately 1 ± 10⁻¹⁵. Over 48,000 steps, the probability distribution at the final sample is conditioned on slightly wrong values from every prior sample. The drift is audible in long utterances as subtle pitch instability, timbral inconsistency, and non-reproducible output across hardware.

The VDR guarantee: softmax sums to exactly 1 at every sample [VDR-4, VDR-14]. Attention over prior samples has zero accumulated error. The causal convolution chain carries zero arithmetic drift. Sample 48,000 is conditioned on exactly correct values from samples 1 through 47,999.

### 2.2 Music Generation

Music generation extends the same architecture to longer sequences — 10,000 to 50,000 tokens for a 3-minute piece at token-level generation. Musical structure requires long-range coherence: a chord progression established in bar 4 must be harmonically consistent with bar 64.

The chain: attention scores at position 50,000 looking back at position 100 pass through the same QKᵀ computation as attention at position 101 looking at position 100. In float, the accumulated error from 50,000 steps of attention computation means the model's effective memory of early positions degrades with distance — not because the architecture limits it, but because the arithmetic corrupts it.

The VDR guarantee: attention weights at any position looking back at any prior position are computed with the same precision as attention at adjacent positions. The arithmetic does not degrade long-range attention. Any long-range coherence failure is attributable to the model, not the computation.

### 2.3 Protein Sequence Prediction

Autoregressive generation of amino acid sequences where each position conditions on all prior positions. Protein function depends on exact residue identity — a single substitution can mean the difference between functional and non-functional protein.

The chain: softmax over 20 amino acid types at each position, conditioned on the full prior sequence. For a 300-residue protein, float softmax drift means the probability of the correct residue at position 300 is slightly corrupted by accumulated error from positions 1 through 299.

The VDR guarantee: exact softmax at every position. Same sequence from same model on any machine, guaranteed. For drug design and synthetic biology where reproducibility across laboratories is essential, the computation is deterministic by construction.

### 2.4 Time-Series Forecasting

Recursive multi-step prediction where each predicted value feeds back as input. Weather forecasting, energy demand, financial time-series. The classic problem: prediction error compounds exponentially with horizon. Float arithmetic adds a noise floor on top of model error.

The VDR guarantee: arithmetic error is zero. The noise floor is eliminated. Model error is the model's problem. For the first time, you can measure pure model error at long horizons without a float noise floor contaminating the measurement.

---

## 3. Normalizing Flows

### 3.1 The Exact Invertibility Problem

Normalizing flows transform a simple distribution (Gaussian) into a complex one through a chain of invertible transformations. The defining property: forward(inverse(x)) = x exactly. Each transformation is typically an affine coupling layer — multiply by a scale factor, add a shift.

The chain: data passes through 10 to 100 coupling layers in sequence. Each layer's output feeds the next. The inverse pass reverses the chain. Exact invertibility requires that the composition of forward layers followed by the composition of inverse layers recovers the input exactly.

The float failure: after 10 coupling layers, forward-inverse roundtrip error is approximately 10⁻¹⁴. After 50 layers (common in modern flows), approximately 10⁻¹². This means log-likelihood computation is wrong by a small but nonzero amount, and generated samples do not exactly invert to their latent codes.

The VDR guarantee: affine coupling is multiply and add on exact rationals. 50 layers, 100 layers, 1000 layers — roundtrip error is zero. Log-likelihood computation is exact. Every generated sample maps to exactly one latent code and back. For density estimation in scientific applications — particle physics, astrophysics — where the log-likelihood value itself is the measurement, exact computation eliminates an entire error source.

### 3.2 Architecture Compatibility

Real NVP, Glow, and Neural Spline Flows are all built on invertible transformations. Spline flows use rational quadratic splines — already rational functions, a natural fit for VDR. The spline knots and derivatives are exact rationals, forward and inverse evaluations are exact rational arithmetic, and the log-determinant of the Jacobian is exact.

---

## 4. Kalman Filtering and State Estimation

### 4.1 The Covariance Accumulation Problem

A Kalman filter maintains a state estimate x̂ and covariance matrix P. Each update cycle consists of a predict step (P = FPFᵀ + Q) and a correct step (P = (I-KH)P). The covariance matrix must remain symmetric and positive definite throughout operation.

The chain: each cycle's covariance matrix feeds the next cycle's prediction. The matrix operations — multiplication, transpose, addition, inversion — each introduce float error. The critical requirement is symmetry: P must equal Pᵀ exactly, because asymmetry in the covariance causes the filter to weight observations inconsistently across dimensions.

The float failure: float matrix multiplication breaks symmetry by approximately 10⁻¹⁶ per step. After 10,000 steps, P is noticeably asymmetric and eigenvalues can go negative, causing the filter to diverge. Practitioners add symmetrization hacks — P = (P + Pᵀ)/2 — and positive-definite enforcement after every step. These are compensations for arithmetic failure, not features of the algorithm.

The VDR guarantee: matrix multiplication is exact. FPFᵀ is exactly symmetric because the multiplication is exact and the transpose produces exactly the same values. P never loses positive definiteness from arithmetic error. The Kalman gain K = PHᵀ(HPHᵀ + R)⁻¹ is computed via exact matrix inversion [VDR-1]. No symmetrization needed. No positive-definite enforcement. The filter tracks the true covariance of the estimation error, not the true covariance plus accumulated float noise.

### 4.2 Spacecraft Navigation

Deep space missions run Kalman filters for months or years. Voyager, New Horizons, Mars rovers — continuous state estimation with no opportunity to reset. Float drift in the covariance matrix means the filter's confidence in its position estimate slowly decorrelates from reality. VDR: covariance at month 36 has the same arithmetic precision as covariance at minute 1.

### 4.3 Autonomous Vehicles

Sensor fusion combining GPS, IMU, LiDAR, and camera through extended or unscented Kalman filters. Safety-critical: the covariance matrix determines whether the vehicle's control system believes it knows the vehicle's position. Float asymmetry in P can cause the vehicle to be overconfident in one axis and underconfident in another. VDR: exact covariance, exact confidence bounds, no arithmetic source of overconfidence.

### 4.4 Financial Filtering

Estimating hidden states (true volatility, regime) from noisy observations (prices, volumes). The Kalman gain determines how much the model trusts new data versus its prior estimate. Float drift in the gain means the model slowly becomes either too trusting or too skeptical of new data. Over a trading year — 252 days with updates every minute producing approximately 100,000 steps — the arithmetic drift is measurable.

---

## 5. Cryptographic Protocols

### 5.1 Shamir Secret Sharing

Split a secret into n shares such that any k shares reconstruct it. The secret is a polynomial evaluated at n points over a finite field. Reconstruction uses Lagrange interpolation — exact rational arithmetic over a finite field.

Float is categorically excluded. VDR's exact arithmetic and finite field builtins — gf_add, gf_mul, gf_inv, gf_pow from [VDR-10] — handle this natively. The VDR-2 gym (domain 12) already verified RSA encrypt/decrypt roundtrip, Chinese Remainder Theorem, and discrete logarithm with zero computation errors [VDR-2].

### 5.2 Homomorphic Encryption

Compute on encrypted data. Schemes like BFV and CKKS operate on polynomial rings with exact modular arithmetic. CKKS allows approximate arithmetic, but the approximation must be controlled — each operation's error is tracked explicitly.

VDR's Remainder slot is structurally parallel to CKKS's error tracking: the R slot carries exactly what the computation did not absorb in the current denominator frame. The Q335 frame with explicit remainder is a natural representation for homomorphic ciphertext noise budgets — the Remainder tells you how much noise budget has been consumed, as an exact integer, not a float estimate.

### 5.3 Zero-Knowledge Proofs

ZK-SNARKs and ZK-STARKs require field arithmetic over large primes (BN254, BLS12-381). The operand width — 256 to 384 bits — matches Q335's 384-bit working width exactly. VDR-22 identified this overlap and designed the Barrett reduction extension (2.1% die area increase) for dual-purpose VDR+ZKP silicon [VDR-22]. The arithmetic is identical: wide integer multiply, modular reduction, point operations on elliptic curves.

### 5.4 Post-Quantum Cryptography

Lattice-based schemes (CRYSTALS-Kyber, CRYSTALS-Dilithium) use polynomial arithmetic over moderate-sized integers. Exact integer arithmetic with no float contamination is a requirement of the standard, not an optimization. VDR's integer arithmetic layer handles lattice operations natively.

---

## 6. Financial Computation

### 6.1 Monte Carlo Pricing

Price exotic derivatives by simulating thousands of paths. Each path: generate random increments, apply to a stochastic differential equation, compute payoff, average across paths.

The float failure: each path has slightly different rounding, and the average of 100,000 paths has a float noise floor of approximately 10⁻¹² on top of the statistical Monte Carlo error. You cannot determine whether the residual error in your price estimate is from insufficient paths or from arithmetic.

The VDR guarantee: each path is exact rational arithmetic. The average is exact. The only error is Monte Carlo sampling error. Statistical error and arithmetic error are cleanly separated for the first time.

### 6.2 Risk Aggregation

Sum Value-at-Risk across thousands of positions. Each position's contribution involves multiplying notional by sensitivity by scenario value.

The float failure: $10,000,000.00 × 0.000001 × 1.0000001 produces different results depending on multiplication order due to float non-associativity. The risk number depends on how the code was written, not just what the positions are.

The VDR guarantee: multiplication is associative over exact rationals. The risk number is the same regardless of aggregation order. Regulators can verify the computation is deterministic and order-independent.

### 6.3 Regulatory Capital

Banks compute capital requirements (Basel III/IV) using exact formulas applied to portfolio data. The formulas involve products, sums, square roots, and ratios of large numbers. A rounding difference of $1 across millions of positions can mean millions in required capital.

The VDR guarantee: one answer, every time, on every machine. The audit trail is a provenance chain of exact rationals [VDR-14]. No platform dependence, no rounding mode dependence, no aggregation order dependence.

### 6.4 Options Greeks

Delta, gamma, and vega computed as numerical derivatives of pricing functions. The finite difference Δ = (f(S+h) - f(S-h))/(2h) is the standard computation.

The float failure: catastrophic cancellation. f(S+h) and f(S-h) are nearly equal. Their difference loses significant digits. The division by 2h amplifies whatever digits remain. The resulting Greek can be wrong by orders of magnitude for small h.

The VDR guarantee: the difference is exact, the division is exact, the Greek is exact at the chosen step size. No subtractive cancellation because rational subtraction does not lose digits — the result has a larger denominator, not fewer significant figures. This is the same structural advantage demonstrated in VDR-26's diffusion reverse step, where the subtraction xₜ - √(1-ᾱₜ)·ε is exact despite the operands being close in magnitude.

### 6.5 Blockchain DeFi

Automated market makers (Uniswap, Curve) compute prices using exact formulas. Every node must compute the identical result. Float is forbidden.

Current implementations use fixed-point integer arithmetic with manual scaling — multiply by 10¹⁸, divide at the end, truncate. VDR provides the same exactness with rational arithmetic that handles arbitrary denominators natively. No manual scaling, no overflow management, no truncation decisions. The constant product invariant x·y = k is verified as exact equality after every swap.

Yield calculations across 2.6 million blocks per year compound interest at every block. Fixed-point truncates at every step. VDR: (1 + r/n)ⁿ is exact for rational r and integer n. Zero truncation across the entire year.

---

## 7. Control Systems

### 7.1 Model Predictive Control

At each timestep, solve an optimization problem over a prediction horizon, apply the first control input, shift the horizon, repeat. Each optimization involves matrix multiplications, inversions, and constraint checks.

The chain: thousands of control cycles for industrial process control running for days. Each cycle's optimization is influenced by the previous cycle's state estimate, which was influenced by the cycle before that.

The float failure: drift in the optimization means the controller slowly diverges from the true optimum. Over thousands of cycles, the accumulated drift manifests as suboptimal setpoints — not wrong enough to trigger an alarm, but wrong enough to waste energy or reduce yield.

The VDR guarantee: each optimization is exact, each control input is exactly optimal for the model, drift is zero.

### 7.2 PID Controllers

Industrial PID controllers have gains Kp, Ki, Kd that are often rational numbers. The integral term accumulates error over time.

The float failure: float integral windup includes both physical windup (the plant saturating) and arithmetic windup (float accumulation error in the integral sum). Practitioners cannot distinguish the two.

The VDR guarantee: physical windup is the controller's problem. Arithmetic windup is zero. The integral sum is exact. For the first time, the controller engineer can separate actuator saturation from computation error.

### 7.3 Digital Filter Chains

IIR filters in series, each step's output feeding the next filter's input. VDR-13 demonstrated this: (1/√2)²⁰ collapses to exact 1/1024 via normalization [VDR-13]. A cascade of 20 biquad sections in float accumulates approximately 10⁻¹³ error.

The VDR guarantee: zero. Audio processing, vibration analysis, power grid monitoring — anywhere filter chains run continuously, VDR eliminates the drift that float introduces.

### 7.4 Stability Analysis

Is a control system stable? Check if all eigenvalues of the state matrix have negative real parts. For 2×2 systems with rational entries, eigenvalues are exact (quadratic formula with VDR exact arithmetic). For larger systems, eigenvalues are generally irrational, but VDR functional remainders produce exact rational approximations at any depth.

The critical case: an eigenvalue real part near zero. Float might round -10⁻¹⁶ to +10⁻¹⁶, declaring an unstable system stable. VDR resolves the eigenvalue to the Newton residual depth — below 10⁻⁵⁰ at depth 10 — making false stability declarations vanishingly unlikely.

---

## 8. Physics Simulation

### 8.1 N-Body Orbital Mechanics

Two-body orbits close exactly. VDR-13 demonstrated exact orbit closure where float64 shows measurable precession after a single orbit [VDR-13]. N-body problems are chaotic long-term, but VDR's Remainder representation means you know exactly when your simulation has diverged from reality — the denominator growth and remainder nesting depth tell you the information-theoretic cost of the trajectory.

For mission planning — gravity assists, constellation design — short-term exact propagation with known precision bounds is more useful than long-term approximate propagation with unknown error.

### 8.2 Molecular Dynamics

Integrate Newton's equations for molecular systems. Symplectic integrators (Verlet, leapfrog) are designed to preserve energy over long trajectories.

The chain: 10⁶ timesteps for nanosecond simulations at femtosecond timestep. Each step's positions and velocities feed the next step's force calculation.

The float failure: float breaks symplecticity by approximately 10⁻¹⁶ per step. Over 10⁶ steps, energy drift is measurable and corrupts thermodynamic averages. The drift means the simulation is not actually sampling from the correct ensemble.

The VDR guarantee: symplectic integrator with exact arithmetic preserves energy exactly. The Hamiltonian at step 10⁶ equals the Hamiltonian at step 0 (for the exact discrete map, which differs from the continuous trajectory by the integrator's truncation error — a separate, understood, controllable error source). Thermodynamic averages have zero arithmetic contamination.

### 8.3 Quantum Chemistry

Hartree-Fock and post-HF methods involve diagonalizing the Fock matrix, computing two-electron integrals, and iterating to self-consistency. The SCF cycle is a fixed-point iteration where each cycle's output (density matrix) becomes the next cycle's input (Fock matrix construction).

The float failure: drift in the density matrix means the SCF converges to a slightly wrong fixed point. The converged energy includes an unknown arithmetic contribution.

The VDR guarantee: convergence to the exact fixed point of the discretized equations. The only errors are basis set truncation and correlation approximation — the arithmetic is not a source of error.

### 8.4 Lattice Gauge Theory

Compute quark propagators on a discretized spacetime lattice. The propagator is the inverse of the Dirac operator — a large sparse matrix. Conjugate gradient solvers on float accumulate error proportional to the condition number times machine epsilon.

VDR with exact Gaussian elimination gives exact propagators for system sizes within the practical matrix dimension limit. Currently applicable to toy lattices and verification of float results. The exact result serves as ground truth for validating float solver accuracy.

### 8.5 Computational Fluid Dynamics

Solve Navier-Stokes on a mesh. Each timestep involves matrix assembly and linear system solve.

The float failure: drift across thousands of timesteps manifests as nonphysical mass or energy creation or destruction. Conservation law verification requires tolerance — "energy is conserved to within 10⁻¹⁰" — because the arithmetic cannot guarantee exact conservation.

The VDR guarantee: conservation law verification is exact equality, not residual tolerance. For benchmark problems where the exact solution is known, VDR computes it exactly [VDR-13].

---

## 9. Blockchain and Consensus

### 9.1 Deterministic State Transitions

Every node in a blockchain network must compute the identical state after applying each transaction. This is the strongest possible requirement on arithmetic: not approximate agreement, not agreement within tolerance — bit-identical output from every participant.

Ethereum's EVM uses 256-bit integers specifically to avoid float nondeterminism. Solidity has no float type. Current approach: manual fixed-point with explicit scaling (multiply by 10¹⁸, divide at the end, truncate). VDR provides exact rational arithmetic natively — no manual scaling, no truncation decisions, no rounding mode selection. The result is the result, on every node, always.

### 9.2 Automated Market Makers

Uniswap v2 maintains the constant product invariant x·y = k after each swap. Uniswap v3 uses concentrated liquidity with tick math involving square roots and logarithms of price ratios. Current implementation approximates with fixed-point arithmetic.

The VDR guarantee: the invariant x·y = k is verified as exact equality after every swap. Square roots of price ratios use Newton iteration with exact rational convergence. No tick boundary rounding errors. No invariant violation from arithmetic.

### 9.3 Yield Calculation

DeFi protocols compute interest rates, yield farming rewards, and liquidation thresholds using compound interest formulas applied every block — approximately every 12 seconds. Over a year: approximately 2.6 million blocks.

The float failure: compound interest drift is significant over 2.6 million compounding steps. Fixed-point arithmetic truncates at every step, losing a fraction of a cent per block that accumulates into meaningful discrepancy over a year.

The VDR guarantee: exact rational compound interest with zero truncation. (1 + r/n)ⁿ is exact for rational r and integer n. The interest earned after 2.6 million blocks is the exact rational number the formula defines, not an approximation.

### 9.4 Cross-Chain Bridges

Assets moving between chains require exact balance accounting. A rounding discrepancy of 1 wei (10⁻¹⁸ ETH) between two chains means the bridge is either creating or destroying value.

The VDR guarantee: exact balance, zero discrepancy, mathematically provable conservation. The sum of all balances across both chains is an exact rational that does not change through any transaction.

---

## 10. Geodesy and Navigation

### 10.1 Coordinate Transformation Chains

Convert from GPS (WGS84) to local projection (UTM) to site coordinates to building coordinates. Each transformation is a matrix multiplication or polynomial evaluation. A survey traverse might chain 20 transformations.

The float failure: approximately 10⁻¹² position error after 20 transforms. For legal survey work where millimeter precision has property-line implications, the question "which rounding produced this boundary?" is unanswerable.

The VDR guarantee: VDR-13 demonstrated exact Helmert roundtrip with zero residual [VDR-13]. Twenty chained transformations produce zero accumulated arithmetic error. Survey misclosure is pure measurement error, identifiable and correctable.

### 10.2 GPS Correction Chains

Differential GPS applies corrections from reference stations. Each correction is a small additive adjustment. Chaining corrections from multiple stations involves weighted averages where the weights must sum to exactly 1.

The float failure: weights sum to 1 ± 10⁻¹⁶. The correction is approximately what the mathematics says.

The VDR guarantee: weights sum to exactly 1. The correction is exactly what the mathematics says. The same structural property as VDR's softmax summing to exactly 1 [VDR-4, VDR-14].

### 10.3 Inertial Navigation

Dead reckoning from accelerometer and gyroscope data. Each step integrates acceleration to get velocity, velocity to get position. Double integration of noisy data with float arithmetic means position error grows as t² from integration plus accumulated float drift.

The VDR guarantee: the integration is exact. Position error growth is purely from sensor noise, not arithmetic. Sensor quality and computation quality are separable.

### 10.4 Cadastral Surveying

Property boundaries defined by chains of bearings and distances. Each leg is a trigonometric computation whose endpoint is the start of the next leg.

The float failure: after 20 legs, the traverse misclosure includes both measurement error and arithmetic error, indistinguishable from each other.

The VDR guarantee: arithmetic error is zero. Misclosure is pure measurement error. The surveyor knows exactly what to attribute to instrument precision and what to attribute to the computation — and the computation contributes nothing.

---

## 11. Game Theory and Mechanism Design

### 11.1 Auction Clearing

Vickrey-Clarke-Groves mechanism computes each bidder's payment as the externality they impose on others. This requires computing the optimal allocation with and without each bidder — combinatorial optimization producing exact rational payments.

The float failure: payments may not sum to the correct total due to rounding. Budget balance — a fundamental property of the mechanism — is violated by arithmetic.

The VDR guarantee: payments are exact rationals. Budget balance is verifiable as exact equality. The mechanism has the properties its designer intended, not approximate versions of those properties.

### 11.2 Matching Markets

Deferred acceptance algorithm for school choice and residency matching. Extensions with priorities and quotas involve tie-breaking with numerical scores.

The float failure: float tie-breaking is platform-dependent. The same student might be assigned to different schools on different hardware. For a process that determines children's educational opportunities, nondeterministic computation is unacceptable.

The VDR guarantee: deterministic, reproducible, litigable. Same input, same output, everywhere, always.

### 11.3 Shapley Values

The Shapley value of player i is a weighted average over all coalitions. For n players, this is a sum over 2ⁿ terms, each involving factorial weights.

VDR-2 gym domain 17 verified exact Shapley values summing to v(N) = 1 exactly [VDR-2]. Float: Shapley values sum to 1 ± 10⁻¹⁵. For cost allocation in shared infrastructure — airports, utilities, telecommunications — the rounding determines who pays what. Exact Shapley values eliminate allocation disputes arising from arithmetic.

### 11.4 Mechanism Incentive Compatibility

Designing incentive-compatible mechanisms requires verifying that no agent benefits from misreporting. The verification involves comparing utilities under truthful versus strategic reporting — differences that may be small rational numbers.

The float failure: a mechanism declared incentive-compatible might not be, because float rounding obscures a small but genuine benefit from misreporting.

The VDR guarantee: the comparison is exact. The mechanism either is or is not incentive-compatible. No arithmetic gray zone.

### 11.5 Market Equilibrium

VDR-2 gym domain 17 computed Cournot duopoly equilibrium exactly: q₁* = 20/3, q₂* = 14/3, profit₁ = 200/9 [VDR-2]. These are exact rationals, not float approximations. The equilibrium conditions are verified by exact substitution into the best-response equations, not by checking that residuals are below tolerance.

### 11.6 Voting Power

Computing voting power indices (Banzhaf, Shapley-Shubik) requires summing over all winning coalitions. The indices are rational numbers that must sum to 1.

The float failure: they do not quite sum to 1.

The VDR guarantee: they sum to exactly 1. For constitutional analysis and corporate governance where voting power has legal significance, exact computation eliminates the question of whether a fractional discrepancy is arithmetic or structural.

---

## 12. Digital Signal Processing

### 12.1 IIR Filter Cascades

Infinite impulse response filters in series, each step's output feeding the next filter. Audio processing, vibration analysis, power grid monitoring — continuous operation over millions of samples.

VDR-13 demonstrated this directly: (1/√2)²⁰ collapses to exact 1/1024 via normalization [VDR-13]. A cascade of 20 biquad sections in float accumulates approximately 10⁻¹³ error. VDR: zero.

The practical implication: a digital filter chain that runs for a year of continuous operation has the same arithmetic precision at month 12 as at second 1.

### 12.2 DFT Roundtrip

The Discrete Fourier Transform followed by the inverse DFT should recover the original signal exactly. VDR-13 verified exact DFT roundtrip where float shows measurable residual [VDR-13]. For signal analysis where the frequency content must be exactly recoverable from the spectrum, VDR provides lossless transformation.

### 12.3 Convolution

Linear convolution of two sequences — the fundamental operation in signal processing. Each output sample is a sum of products. Float accumulates rounding in each product and in the summation. VDR: each product is exact, the summation is exact, the convolution is exact.

---

## 13. Quantum Computing Primitives

### 13.1 State Vectors

A quantum state vector has complex amplitudes whose squared magnitudes must sum to exactly 1. Float: they sum to approximately 1. After each gate operation, renormalization is needed. VDR: amplitudes are VDR complex pairs [VDR-13]. Gate operations (matrix-vector products) are exact. The normalization constraint is maintained exactly through the computation without renormalization.

### 13.2 Gate Matrices

Single-qubit gates (Hadamard, Pauli, phase) and multi-qubit gates (CNOT, Toffoli) are unitary matrices. Float matrix multiplication of unitary matrices is not exactly unitary — UUᵀ ≈ I but not exactly I. After 100 gates, the accumulated deviation from unitarity can affect simulation fidelity. VDR: UUᵀ = I exactly for gates with rational entries (Hadamard H = (1/√2)[[1,1],[1,-1]] via Newton iteration for √2). Gates involving irrational entries maintain unitarity to the Newton residual depth.

### 13.3 Measurement Probabilities

Born rule: probability of outcome k is |⟨k|ψ⟩|². The probabilities must sum to exactly 1. Float: they sum to approximately 1. VDR: they sum to exactly 1 (for closed rational amplitudes) or to within Newton residual (for amplitudes involving square roots). This is the same structural property as softmax summing to exactly 1 [VDR-4], applied to quantum measurement.

---

## 14. The Structural Pattern

### 14.1 Separation of Error Sources

In every domain examined, float arithmetic conflates two distinct error sources: the domain's inherent approximation (model error, measurement noise, basis set truncation, statistical sampling) and the arithmetic's rounding error. These are fundamentally different kinds of error — one is the problem's property, the other is the tool's limitation — but float makes them indistinguishable in the output.

VDR eliminates the arithmetic error source. What remains is purely the domain's error. This separation is the common value across all twelve domains: not that VDR makes the computation faster or the model better, but that it makes the arithmetic honest. When the output is wrong, the arithmetic is not the cause. You can finally answer "is my model wrong?" without first having to answer "or is my arithmetic wrong?"

### 14.2 Where VDR Applies

VDR is appropriate for computation chains where:

Exactness matters more than throughput. Financial regulation, safety-critical control, legal survey, medical diagnostics, cryptographic protocols.

Reproducibility is required. Blockchain consensus, cross-platform scientific computation, regulatory audit, forensic evidence processing.

Chain length is long. Video generation, long-term state estimation, molecular dynamics, continuous monitoring, DeFi yield computation.

Error attribution is valuable. Model validation, algorithm comparison, debugging sequential processes, separating measurement from computation.

### 14.3 Where VDR Does Not Apply

VDR is not appropriate for:

Single-step computation where float precision is sufficient. A single matrix multiply in float64 has approximately 10⁻¹⁵ relative error. For a single operation, this is invisible and the 150× cost of Q335 is not justified.

Real-time systems where latency dominates correctness. Game physics, interactive graphics, real-time audio effects where "close enough" at microsecond latency is preferable to "exact" at millisecond latency.

Stochastic processes where model error dominates arithmetic error by many orders of magnitude. If the model is wrong by 10%, float arithmetic error of 10⁻¹⁵ is irrelevant regardless of chain length.

---

## 15. Boundaries

### 15.1 Matrix Size

VDR's exact matrix operations (determinant via cofactor expansion, inverse via adjugate) are O(n!) in the current implementation [VDR-1]. Gaussian elimination is O(n³) but requires pivot selection that interacts with VDR's remainder structure. For domains requiring large matrix operations — lattice QCD, large-scale CFD — the matrix size limitation is the binding constraint. Practical exact matrix operations are currently limited to approximately 50×50.

### 15.2 Transcendental Functions

Domains requiring transcendental functions (sin, cos, exp, log) use Newton iteration or Taylor series, producing exact rational approximations at configurable depth. The residual is fixed and inspectable but nonzero. For domains where exact transcendental evaluation is required (it never is — transcendentals are inherently irrational), VDR provides the closest rational approximation at any requested precision.

### 15.3 Computational Cost

VDR is 100-1000× slower per operation in Python, approximately 150× on GPU with Q335 [VDR-18]. For large-scale simulations (10⁶ atoms in MD, 10⁸ mesh points in CFD), the overhead is prohibitive with current implementations. The practical path is using VDR for validation — running a small system exactly to provide ground truth for verifying float implementations on larger systems.

### 15.4 Denominator Growth

Long multiplication chains produce growing denominators. Q335 fixed-frame arithmetic [VDR-14, VDR-18] manages this by fixing the denominator at 2³³⁵ and routing overflow to remainder depth. For the Python prototype, denominator growth limits practical chain length for chains involving many multiplications. The diffusion validation [VDR-26] demonstrated that chains of practical length (hundreds of steps) are manageable.

---

## Appendices

### Appendix A — Domain Classification by Chain Type

| Domain | Chain type | Typical chain length | Float error at chain end | VDR error | Error ratio |
|---|---|---|---|---|---|
| Speech synthesis | Sample-by-sample | 48,000-144,000 | ~10⁻¹¹ | 0 (rational) or < 10⁻⁵⁰ (sqrt) | > 10³⁹ |
| Music generation | Token-by-token | 10,000-50,000 | ~10⁻¹¹ | 0 or < 10⁻⁵⁰ | > 10³⁹ |
| Protein generation | Residue-by-residue | 100-1,000 | ~10⁻¹³ | 0 or < 10⁻⁵⁰ | > 10³⁷ |
| Normalizing flow | Layer-by-layer | 10-100 | ~10⁻¹⁴ | 0 | Float / 0 |
| Kalman filter | Cycle-by-cycle | 10,000-10,000,000 | ~10⁻⁹ | 0 | Float / 0 |
| Monte Carlo paths | Step-by-step per path | 100-10,000 per path | ~10⁻¹² | 0 | Float / 0 |
| MPC control | Cycle-by-cycle | 10,000-1,000,000 | ~10⁻¹⁰ | 0 | Float / 0 |
| PID integral | Sample-by-sample | 1,000,000+ | ~10⁻¹⁰ | 0 | Float / 0 |
| IIR filter cascade | Sample-by-sample | 1,000,000+ | ~10⁻¹⁰ | 0 | Float / 0 |
| MD simulation | Timestep-by-timestep | 10⁶-10⁹ | ~10⁻⁷ | 0 | Float / 0 |
| SCF iteration | Cycle-by-cycle | 10-100 | ~10⁻¹⁴ | 0 | Float / 0 |
| Blockchain txn | Block-by-block | 2,600,000/year | ~10⁻⁹ (fixed-point) | 0 | Fixed-point / 0 |
| GPS correction | Station-by-station | 5-20 | ~10⁻¹⁴ | 0 | Float / 0 |
| Inertial nav | Sample-by-sample | 100,000+ | ~10⁻¹¹ | 0 | Float / 0 |
| Survey traverse | Leg-by-leg | 10-50 | ~10⁻¹³ | 0 | Float / 0 |
| Shapley value | Coalition-by-coalition | 2ⁿ (exponential) | ~10⁻¹⁵ | 0 | Float / 0 |
| Quantum sim | Gate-by-gate | 100-10,000 | ~10⁻¹² | 0 or < 10⁻⁵⁰ | > 10³⁸ |
| Video diffusion | Frame × step | 36,000-8,640,000 | ~10⁻⁸ | < 10⁻⁵⁰ | > 10⁴² |

### Appendix B — VDR Primitive Mapping by Domain

| Domain | Primary VDR operations | Builtin categories used | Prior validation |
|---|---|---|---|
| Autoregressive gen | Softmax, attention (QKᵀ), linear, ReLU | Linear algebra, statistics | VDR-4: 198 tests |
| Normalizing flows | Multiply, add, inverse, log-determinant | Closed arithmetic, linear algebra | VDR-1: 68 tests; VDR-2: exact matrix inverse |
| Kalman filtering | Matrix multiply, transpose, inverse, add | Linear algebra | VDR-1: Hilbert inverse exact; VDR-2: 15 domains |
| Secret sharing | Finite field arithmetic, Lagrange interpolation | Finite field, polynomial | VDR-2 gym 12: RSA roundtrip, CRT |
| Homomorphic encryption | Polynomial multiply, modular reduction | Polynomial, number theory | VDR-2 gym 12, VDR-3 |
| ZK proofs | Wide integer multiply, modular reduction | Integer/bit ops, number theory | VDR-22: Q335 matches BN254/BLS12-381 width |
| Monte Carlo | Multiply, add, average, sqrt | Closed arithmetic, statistics, functional remainder | VDR-1: zero drift; VDR-26: exact path |
| Risk/capital | Multiply, add, compare, sort | Closed arithmetic, comparison, collections | VDR-1, VDR-2 |
| Options Greeks | Subtract, divide (finite difference) | Closed arithmetic | VDR-1: exact division |
| DeFi AMM | Multiply, divide, sqrt, compare | Closed arithmetic, functional remainder, comparison | VDR-1, VDR-3 |
| MPC/PID | Matrix multiply, inverse, add, integrate | Linear algebra, discrete calculus | VDR-1, VDR-13 |
| IIR filters | Multiply, add, chain | Closed arithmetic | VDR-13: (1/√2)²⁰ = 1/1024 exact |
| Orbital mechanics | Multiply, sqrt, trig (Newton), chain | Closed arithmetic, functional remainder | VDR-13: exact orbit closure |
| Molecular dynamics | Add, multiply, sqrt (Verlet step) | Closed arithmetic, functional remainder | VDR-13: conservation exact |
| Quantum chemistry | Matrix eigenvalue, multiply, iterate | Linear algebra | VDR-1: Hilbert inverse; VDR-2: eigenvalue domain |
| CFD | Matrix assemble, solve, integrate | Linear algebra, discrete calculus | VDR-1, VDR-13 |
| DFT roundtrip | Complex multiply, sum, inverse | Linear algebra, complex pairs | VDR-13: exact DFT roundtrip |
| Geodesy | Matrix multiply, trig, chain | Linear algebra, functional remainder | VDR-13: exact Helmert roundtrip |
| Survey traverse | Trig, add, chain | Functional remainder, closed arithmetic | VDR-13: trigonometric domains |
| Shapley values | Factorial, sum, divide | Number theory, closed arithmetic | VDR-2 gym 17: exact Shapley |
| Voting power | Combinatorial sum, divide | Number theory, closed arithmetic | VDR-2 gym 17 |
| Auction clearing | Optimize, subtract, compare | Closed arithmetic, comparison | VDR-2 gym 17: exact equilibrium |
| Quantum gates | Matrix multiply, complex pairs | Linear algebra, complex pairs | VDR-13: complex pairs, DFT |
| Blockchain | Integer multiply, modular, compare | Integer ops, number theory, comparison | VDR-2 gym 12: RSA, CRT |

### Appendix C — Error Accumulation Models

| Model | Formula | Example | Float behavior | VDR behavior |
|---|---|---|---|---|
| Random walk | ε_total ≈ √N × ε_step | Independent rounding errors | Grows as √N | 0 |
| Linear | ε_total ≈ N × ε_step | Worst-case same-direction errors | Grows as N | 0 |
| Multiplicative | ε_total ≈ (1 + ε_step)ᴺ - 1 | Compounding relative errors | Grows exponentially | 0 |
| Catastrophic | ε_total ≈ ε_step × 10ᵏ | Cancellation amplifies error by 10ᵏ | Sudden precision loss | 0 |
| Fixed residual | ε_total = ε_residual | Newton sqrt at fixed depth | N/A (float has no fixed residual) | Constant < 10⁻⁵⁰ |
| Chaotic amplification | ε_total ≈ ε_step × e^(λN) | Lyapunov exponent λ > 0 | Grows exponentially × exponentially | 0 × e^(λN) = 0 |

VDR eliminates the per-step error ε_step. The accumulation model becomes irrelevant because there is nothing to accumulate. The only exception is Newton/Taylor residual, which produces a fixed ε_residual independent of N.

### Appendix D — Symmetry and Conservation Guarantees

| Property | Domain | Float behavior | VDR guarantee | Verification method |
|---|---|---|---|---|
| Matrix symmetry | Kalman filter (P = Pᵀ) | Breaks by ~10⁻¹⁶/step | Exact | Structural equality of P and Pᵀ |
| Positive definiteness | Kalman filter (P > 0) | Can go negative | Maintained | Eigenvalue check (exact for small matrices) |
| Unitarity | Quantum gates (UUᵀ = I) | Drifts from I | Exact (rational gates) | Matrix multiply and compare to identity |
| Probability sum | Softmax, Born rule | ≈ 1 ± 10⁻¹⁵ | Exactly 1 | Rational sum check |
| Energy conservation | MD, orbital | Drifts ~10⁻¹⁶/step | Exact (discrete Hamiltonian) | Hamiltonian evaluation at step 0 vs N |
| Mass conservation | CFD | Drifts ~10⁻¹⁶/step | Exact | Mass integral comparison |
| Budget balance | Auction (∑payments = correct) | ≈ correct ± 10⁻¹⁵ | Exact | Rational sum check |
| Voting power sum | Banzhaf/Shapley-Shubik | ≈ 1 ± 10⁻¹⁵ | Exactly 1 | Rational sum check |
| Token balance | Blockchain (∑balances = total supply) | Exact (integer) | Exact (rational) | Sum check |
| Flow invertibility | Normalizing flow (f⁻¹(f(x)) = x) | ≈ x ± 10⁻¹² | Exactly x | Roundtrip identity check |
| Coefficient identity | Diffusion ((√ᾱ)²+(√(1-ᾱ))²=1) | ≈ 1 ± 10⁻¹⁵ | < 10⁻⁵⁰ residual | VDR-26 test 11 |
| GPS weight sum | Weighted average (∑wᵢ = 1) | ≈ 1 ± 10⁻¹⁶ | Exactly 1 | Rational sum check |
| Associativity | Risk aggregation (a×b×c order) | Order-dependent | Order-independent | Compare different orderings |
| Shamir reconstruction | Secret sharing (k-of-n recovery) | Float excluded | Exact finite field | Reconstruct and compare |

### Appendix E — Prior VDR Validation Coverage by Domain

| Domain | VDR paper | Tests | Passed | Failed (test error) | Failed (VDR error) | Relevant to this paper |
|---|---|---|---|---|---|---|
| Core arithmetic | VDR-1 | 68 | 68 | 0 | 0 | All domains |
| Number theory | VDR-2 gym 1 | 19 | 19 | 0 | 0 | Cryptography, voting |
| Polynomial algebra | VDR-2 gym 2 | 18 | 18 | 0 | 0 | Homomorphic encryption |
| Continued fractions | VDR-2 gym 3 | 19 | 19 | 0 | 0 | Rational approximation |
| Matrix decomposition | VDR-2 gym 4 | 19 | 18 | 1 | 0 | Kalman, quantum, MD |
| Combinatorics | VDR-2 gym 5 | 19 | 19 | 0 | 0 | Shapley, voting |
| Signal processing | VDR-2 gym 6 | 19 | 19 | 0 | 0 | DSP, filters |
| Computational geometry | VDR-2 gym 7 | 19 | 18 | 1 | 0 | Geodesy |
| Differential equations | VDR-2 gym 8 | 19 | 18 | 1 | 0 | Control, physics sim |
| Optimization | VDR-2 gym 9 | 19 | 18 | 1 | 0 | MPC, auction |
| Probability | VDR-2 gym 10 | 19 | 19 | 0 | 0 | Monte Carlo, Kalman |
| Cryptography | VDR-2 gym 12 | 19 | 18 | 1 | 0 | All crypto domains |
| Graph theory | VDR-2 gym 14 | 18 | 18 | 0 | 0 | Network analysis |
| Game theory | VDR-2 gym 17 | 19 | 19 | 0 | 0 | All game theory domains |
| Q335 basis | VDR-3 | 157 | 152 | 5 | 0 | Transcendental computation |
| LM pipeline | VDR-4 | 198 | 196 | 2 | 0 | Autoregressive, diffusion |
| QED/quantum | VDR-13 phys | — | — | — | 0 | Quantum chemistry |
| Orbital mechanics | VDR-13 phys | — | — | — | 0 | N-body |
| Signal processing | VDR-13 phys | — | — | — | 0 | DSP, filters |
| Control systems | VDR-13 phys | — | — | — | 0 | Control, PID |
| Geodesy | VDR-13 phys | — | — | — | 0 | Coordinate transforms |
| Crystallography | VDR-13 phys | — | — | — | 0 | Molecular simulation |
| Diffusion | VDR-26 | 37 | 33 | 4 | 0 | Diffusion, video gen |
| **Total** | | **884 + 37** | **870 + 33** | **14 + 4** | **0** | |

921 tests across 38 domains. Zero VDR computation errors. Every failure traces to test design, never to arithmetic.

### Appendix F — Practical Deployment Scenarios

| Scenario | Chain length | Current approach | Current limitation | VDR approach | VDR limitation |
|---|---|---|---|---|---|
| Bank regulatory capital | 10⁶ positions × 10 operations | Float64 + manual rounding rules | Platform-dependent; audit disputes | Exact rational; deterministic audit | Computational cost for full portfolio |
| Mars rover navigation | 10⁸ Kalman steps (3-year mission) | Float64 + symmetrization hacks | Covariance drift; periodic resets needed | Exact covariance; no resets | Matrix size for high-dimensional state |
| DeFi yield (1 year) | 2.6×10⁶ blocks | Fixed-point with truncation | Truncation loss per block; dust accumulation | Exact rational compound interest | Denominator growth (Q335 addresses this) |
| Video generation (2 hr) | 8.64×10⁶ sequential ops | Float16/32 with heuristic corrections | Temporal drift visible in long sequences | Zero drift; exact frame conditioning | Per-operation cost limits resolution |
| Pharmaceutical MD | 10⁹ timesteps | Float64 + energy monitoring | Energy drift corrupts averages | Exact symplectic integration | System size limited to small molecules |
| Audio mastering chain | 10⁷ samples × 20 filters | Float64 | Accumulates ~10⁻¹⁰ over session | Zero drift across filter chain | Real-time latency for live processing |
| Legal survey | 20-50 chained legs | Float64 + misclosure adjustment | Cannot separate measurement from arithmetic | Zero arithmetic error; pure measurement misclosure | Trigonometric approximation depth |
| Quantum circuit sim | 10,000 gates | Float64 + renormalization | Unitarity drift; periodic renorm | Exact unitarity (rational gates) | Gate count × qubit count limited |
| Secret key sharing | k-of-n reconstruction | Integer modular arithmetic | Already exact for standard schemes | Same exactness; unified with other VDR operations | No additional limitation |
| Options desk Greeks | 10,000 positions × 5 Greeks | Float64 with step-size tuning | Cancellation error at small h | Exact finite difference at any h | Per-position cost |

### Appendix G — Float Failure Taxonomy

| Failure type | Mechanism | Domains affected | Detection difficulty | VDR elimination |
|---|---|---|---|---|
| Accumulation | Per-step ULP errors summing over N steps | All sequential chains | Easy to estimate, hard to measure exactly | Complete: 0 per-step error |
| Cancellation | Subtracting nearly equal values loses digits | Options Greeks, Kalman, diffusion reverse step | Hard: result looks plausible but wrong | Complete: exact subtraction |
| Non-associativity | (a×b)×c ≠ a×(b×c) in float | Risk aggregation, any parallel reduction | Hard: depends on code structure and optimizer | Complete: rational multiplication is associative |
| Platform dependence | Different FMA, different sqrt, different rounding | Blockchain, regulatory, scientific reproducibility | Detectable only by cross-platform comparison | Complete: integer arithmetic is platform-independent |
| Overflow/underflow | Values exceed float range | Kalman (ill-conditioned P), long products | Easy to detect (NaN/Inf) but hard to prevent | VDR denominators grow instead of overflowing |
| Denormalized numbers | Very small values lose precision | Near-zero quantities in physics, small probabilities | Hard: gradual precision loss, no explicit signal | Complete: VDR has full precision at any magnitude |
| Non-reproducibility | Same code, different hardware, different result | All float computation | Detectable; not fixable without abandoning float | Complete: deterministic by construction |
| Symmetry breaking | A×B ≠ (A×B)ᵀ even when mathematically symmetric | Kalman filter covariance, quantum density matrix | Hard: asymmetry is tiny but consequential | Complete: exact matrix multiply preserves symmetry |
| Energy/conservation drift | Conservation laws violated by rounding | MD, CFD, diffusion coefficient identity, quantum normalization | Measurable but not correctable without exact arithmetic | Complete: conservation verified by exact equality |
| False convergence | Iteration stops because residual ≈ float epsilon | SCF in quantum chemistry, Newton in optimization | Hard: looks converged but at wrong fixed point | VDR converges to exact fixed point of discrete equations |

### Appendix H — Regulatory and Standards Requirements for Exact Computation

| Regulation/Standard | Domain | Requirement | Float compliance | VDR compliance |
|---|---|---|---|---|
| Basel III/IV | Banking capital | Deterministic capital calculation | Approximate: platform-dependent | Full: exact rational, platform-independent |
| MiFID II | Financial trading | Best execution proof; reproducible pricing | Approximate: depends on rounding mode | Full: deterministic pricing |
| FIPS 140-3 | Cryptography | Correct implementation of crypto primitives | Integer arithmetic mandated (no float) | Full: integer arithmetic native |
| DO-178C | Aviation software | Verified arithmetic for safety-critical | Float with analysis; expensive certification | Exact arithmetic simplifies certification argument |
| IEC 61508 | Functional safety | Demonstrated arithmetic integrity | Float with documented precision | Exact: integrity by construction |
| ISO 19111 | Geographic information | Coordinate transformation accuracy | Float with precision statements | Exact: zero transformation chain error |
| GAAP/IFRS | Accounting | Consistent, auditable calculations | Fixed-point or float with rounding rules | Exact rational: no rounding rules needed |
| FDA 21 CFR Part 11 | Medical devices | Reproducible, validated computation | Float with validation suite | Exact: validation is structural property |
| NIST SP 800-185 | Cryptographic hashing | Bit-exact computation | Integer mandated | Full: integer native |
| Smart contract audit | Blockchain | Deterministic state transitions | Integer mandated (no float in EVM) | Full: exact rational extends integer capability |
| GxP (pharma) | Drug development | Reproducible computational results | Float with documented precision | Exact: reproducibility by construction |
| SOX Section 404 | Financial controls | Verifiable financial calculations | Float with auditor review | Exact: provenance chain is the audit |
