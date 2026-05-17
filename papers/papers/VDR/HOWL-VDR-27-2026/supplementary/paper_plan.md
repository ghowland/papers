### Autoregressive Models Beyond LLMs

**Speech synthesis (WaveNet, SoundStorm):** Generate audio sample-by-sample at 16-48kHz. Each sample conditions on previous samples through causal convolution stacks. A 3-second clip at 16kHz is 48,000 sequential steps. Float softmax over quantized audio levels (256 for μ-law) drifts across samples — the probability distribution at sample 48,000 is conditioned on slightly-wrong values from every prior sample. VDR: exact softmax sums to exactly 1 at every sample, attention over prior samples has zero accumulated error, the causal convolution chain carries zero arithmetic drift. Audible artifacts from float: subtle pitch drift, timbral inconsistency across long utterances, non-reproducible output across hardware. VDR eliminates all three.

**Music generation:** Same architecture, longer sequences. A 3-minute piece at token-level generation might be 10,000-50,000 tokens. Musical structure requires long-range coherence — a chord progression established in bar 4 must be harmonically consistent with bar 64. Float drift in the attention scores means the model's memory of bar 4 degrades as context grows. VDR: attention weights at position 50,000 looking back at position 100 are computed with the same precision as attention at position 101 looking at position 100.

**Protein sequence prediction:** Autoregressive generation of amino acid sequences where each position conditions on all prior positions. Protein function depends on exact residue identity — a single substitution can be the difference between functional and non-functional. Float softmax drift means the probability of the correct residue at position 300 is slightly corrupted by accumulated error from positions 1-299. For drug design and synthetic biology, reproducibility across labs and hardware is essential. VDR: same sequence from same model on any machine, guaranteed.

**Time-series forecasting:** Recursive multi-step prediction where each predicted value feeds back as input. Weather forecasting, energy demand, financial time-series. The classic problem: prediction error compounds exponentially with horizon. Float arithmetic adds a noise floor on top of model error. VDR separates the two — model error is the model's problem, arithmetic error is zero. You can finally measure pure model error without a float noise floor contaminating the signal.

### Normalizing Flows

**The exact invertibility problem:** Normalizing flows transform a simple distribution (Gaussian) into a complex one through a chain of invertible transformations. The key property: forward(inverse(x)) = x exactly. Each transformation is typically an affine coupling layer — multiply by a scale factor, add a shift. Float: after 10 coupling layers, forward-inverse roundtrip error is ~10⁻¹⁴. After 50 layers (common in modern flows): ~10⁻¹². This means log-likelihood computation is wrong by a small but non-zero amount, and generated samples don't exactly invert to their latent codes.

VDR: affine coupling is multiply and add on exact rationals. 50 layers, 100 layers, 1000 layers — roundtrip error is zero. Log-likelihood computation is exact. Every generated sample maps to exactly one latent code and back. This matters for density estimation in scientific applications (particle physics, astrophysics) where the log-likelihood value itself is the measurement.

**Real NVP, Glow, Neural Spline Flows:** All built on invertible transformations. Spline flows use rational quadratic splines — already rational functions, natural fit for VDR. The spline knots and derivatives are exact rationals, the forward and inverse evaluations are exact rational arithmetic, the log-determinant of the Jacobian is exact.

### Kalman Filters and State Estimation

**The covariance accumulation problem:** A Kalman filter maintains a state estimate x̂ and covariance matrix P. Each update cycle: predict (P = FPFᵀ + Q), then correct (P = (I-KH)P). The covariance matrix must remain symmetric and positive definite. Float arithmetic breaks symmetry by ~10⁻¹⁶ per step. After 10,000 steps: P is noticeably asymmetric, eigenvalues can go negative, filter diverges. Practitioners add symmetrization hacks (P = (P+Pᵀ)/2) and positive-definite enforcement. These are bandages on a float wound.

VDR: matrix multiply is exact. FPFᵀ is exactly symmetric because the multiplication is exact. P never loses positive definiteness from arithmetic error. The Kalman gain K = PHᵀ(HPHᵀ+R)⁻¹ is computed via exact matrix inversion. No symmetrization needed. No positive-definite enforcement. The filter tracks the true covariance of the estimation error, not the true covariance plus accumulated float noise.

**Spacecraft navigation:** Deep space missions run Kalman filters for months or years. Voyager, New Horizons, Mars rovers — continuous state estimation with no opportunity to reset. Float drift in the covariance matrix means the filter's confidence in its position estimate slowly decorrelates from reality. VDR: covariance at month 36 has the same arithmetic precision as covariance at minute 1.

**Autonomous vehicles:** Sensor fusion combining GPS, IMU, LiDAR, camera through extended Kalman filter or unscented Kalman filter. Safety-critical: the covariance matrix determines whether the vehicle thinks it knows where it is. Float asymmetry in P can cause the vehicle to be overconfident in one direction and underconfident in another. VDR: exact covariance, exact confidence bounds.

**Financial filtering:** Estimating hidden states (true volatility, regime) from noisy observations (prices, volumes). The Kalman gain determines how much the model trusts new data versus its prior. Float drift in the gain means the model slowly becomes either too trusting or too skeptical of new data. Over a trading year (252 days, updates every minute = ~100,000 steps), this matters.

### Cryptographic Protocols

**Shamir secret sharing:** Split a secret into n shares such that any k shares reconstruct it. The secret is a polynomial evaluated at n points over a finite field. Reconstruction uses Lagrange interpolation — exact rational arithmetic over a finite field. Float is categorically excluded. VDR's exact arithmetic and finite field builtins (gf_add, gf_mul, gf_inv, gf_pow from VDR-10) handle this natively. The tested gym (VDR-2 gym 12) already verified RSA encrypt/decrypt roundtrip, CRT, and discrete logarithm.

**Homomorphic encryption:** Compute on encrypted data. Schemes like BFV and CKKS operate on polynomial rings with exact modular arithmetic. CKKS allows approximate arithmetic but the approximation must be controlled — each operation's error is tracked. VDR's remainder slot is structurally identical to CKKS's error tracking: the R slot carries exactly what the computation didn't absorb. The Q335 frame with explicit remainder is a natural representation for homomorphic ciphertext noise budgets.

**Zero-knowledge proofs:** Prove you know a value without revealing it. ZK-SNARKs and ZK-STARKs require field arithmetic over large primes (BN254, BLS12-381). The operand width (256-384 bits) matches Q335's 384-bit working width exactly. VDR-22 identified this overlap and designed the Barrett reduction extension (2.1% area increase) for dual-purpose VDR+ZKP silicon. The arithmetic is identical: wide integer multiply, modular reduction, point operations on elliptic curves.

**Post-quantum cryptography:** Lattice-based schemes (CRYSTALS-Kyber, CRYSTALS-Dilithium) use polynomial arithmetic over moderate-sized integers. Exact integer arithmetic with no float contamination is a requirement, not an optimization.

### Financial Computation

**Monte Carlo pricing:** Price exotic derivatives by simulating thousands of paths. Each path: generate random increments, apply to stochastic differential equation, compute payoff, average. Float arithmetic means each path has slightly different rounding, and the average of 100,000 paths has a float noise floor of ~10⁻¹² on top of the statistical Monte Carlo error. VDR: each path is exact rational arithmetic, the average is exact, the only error is Monte Carlo sampling error. You can finally separate statistical error from arithmetic error.

**Risk aggregation:** Sum Value-at-Risk across thousands of positions. Each position's contribution involves multiplying notional by sensitivity by scenario value. Float: $10,000,000.00 × 0.000001 × 1.0000001 produces different results depending on multiplication order due to float non-associativity. VDR: multiplication is associative over exact rationals. The risk number is the same regardless of aggregation order. Regulators can verify the computation is deterministic.

**Regulatory capital (Basel III/IV):** Banks compute capital requirements using exact formulas applied to portfolio data. The formulas involve products, sums, square roots, and ratios of large numbers. A rounding difference of $1 across millions of positions can mean millions in required capital. Float makes the computation order-dependent and platform-dependent. VDR: one answer, every time, on every machine. Audit trail is a provenance chain of exact rationals.

**Options Greeks:** Delta, gamma, vega computed as numerical derivatives of pricing functions. The finite difference Δ = (f(S+h) - f(S-h))/(2h) is exact in VDR for any rational h. No subtractive cancellation (the classic float problem where f(S+h) and f(S-h) are nearly equal and their difference loses significant digits). VDR: the difference is exact, the division is exact, the Greek is exact at the chosen step size.

**Blockchain DeFi:** Automated market makers (Uniswap, Curve) compute prices using exact formulas (constant product x·y=k, or StableSwap invariant). Every node must compute the identical result. Float is forbidden. Current implementations use fixed-point integer arithmetic with manual scaling. VDR provides the same exactness with rational arithmetic that handles arbitrary denominators natively — no manual scaling, no overflow management.

### Control Systems

**Model predictive control (MPC):** At each timestep, solve an optimization problem over a prediction horizon, apply the first control input, shift the horizon, repeat. Each optimization involves matrix multiplications, inversions, and constraint checks. Float drift in the optimization means the controller slowly diverges from the true optimum. Over thousands of control cycles (industrial process control running for days), the accumulated drift manifests as suboptimal setpoints. VDR: each optimization is exact, each control input is exactly optimal for the model, drift is zero.

**PID loops with exact coefficients:** Industrial PID controllers have gains Kp, Ki, Kd that are often rational numbers (tuned as fractions). The integral term accumulates error over time — float integral windup includes both physical windup and arithmetic windup. VDR separates the two: physical windup is the controller's problem, arithmetic windup is zero.

**Digital filter chains:** IIR filters in series, each step's output feeding the next filter's input. VDR-13 demonstrated this: (1/√2)²⁰ collapses to exact 1/1024 via normalization. A cascade of 20 biquad sections in float accumulates ~10⁻¹³ error. VDR: zero. Audio processing, vibration analysis, power grid monitoring — anywhere filter chains run continuously.

**Stability analysis:** Is a control system stable? Check if all eigenvalues of the state matrix have negative real parts. For 2×2 systems with rational entries, eigenvalues are exact (quadratic formula). For larger systems, eigenvalues are generally irrational — but VDR functional remainders produce exact rational approximations at any depth, and the stability boundary (eigenvalue real part = 0) can be checked to arbitrary precision. No false stability declarations from float rounding an eigenvalue from -10⁻¹⁶ to +10⁻¹⁶.

### Physics Simulation

**N-body orbital mechanics:** Two-body orbits close exactly (VDR-13 demonstrated this). N-body problems are chaotic long-term, but VDR's honest representation means you know exactly when your simulation has diverged from reality — the denominator growth tells you the information-theoretic cost of the trajectory. For mission planning (gravity assists, constellation design), short-term exact propagation with known precision bounds is more useful than long-term approximate propagation with unknown error.

**Molecular dynamics:** Integrate Newton's equations for molecular systems. Symplectic integrators (Verlet, leapfrog) are designed to preserve energy over long trajectories. Float breaks symplecticity by ~10⁻¹⁶ per step. Over 10⁶ steps (nanosecond simulations at femtosecond timestep), energy drift is measurable and corrupts thermodynamic averages. VDR: symplectic integrator with exact arithmetic preserves energy exactly. The Hamiltonian at step 10⁶ equals the Hamiltonian at step 0. Thermodynamic averages have zero arithmetic contamination.

**Quantum chemistry:** Hartree-Fock and post-HF methods involve diagonalizing the Fock matrix, computing two-electron integrals, and iterating to self-consistency. The SCF cycle is a fixed-point iteration where each cycle's output (density matrix) becomes the next cycle's input (Fock matrix construction). Float drift in the density matrix means the SCF converges to a slightly wrong fixed point. VDR: convergence to the exact fixed point of the discretized equations. The only error is basis set truncation and correlation approximation — the arithmetic is not a source of error.

**Lattice QCD:** Compute quark propagators on a discretized spacetime lattice. The propagator is the inverse of the Dirac operator — a large sparse matrix. Conjugate gradient solvers on float accumulate error proportional to the condition number times machine epsilon. Lattice QCD matrices are notoriously ill-conditioned. VDR with Gaussian elimination (when implemented for large sparse systems) would give exact propagators. Currently limited by matrix size (practical up to ~50×50), but for toy lattices and verification of float results, this is immediately applicable.

**Fluid dynamics (CFD):** Solve Navier-Stokes on a mesh. Each timestep involves matrix assembly and linear system solve. Float drift across thousands of timesteps manifests as non-physical mass or energy creation/destruction. Conservation law verification in VDR is exact equality, not residual tolerance. For benchmark problems where the exact solution is known, VDR computes it exactly.

### Blockchain and Consensus

**Deterministic state transitions:** Every node in a blockchain network must compute the identical state after applying each transaction. Ethereum's EVM uses 256-bit integers specifically to avoid float non-determinism. Solidity has no float type. Current approach: manual fixed-point with explicit scaling (multiply by 10¹⁸, divide at the end, truncate). VDR provides exact rational arithmetic natively — no manual scaling, no truncation decisions, no rounding mode selection. The result is the result, on every node, always.

**Automated market makers:** Uniswap v2: x·y = k after each swap. Uniswap v3: concentrated liquidity with tick math involving square roots and logarithms of price ratios. Current implementation approximates with fixed-point. VDR: the invariant x·y = k is verified as exact equality after every swap. Square roots of price ratios use Newton iteration with exact rational convergence. No tick boundary rounding errors.

**Yield calculation:** DeFi protocols compute interest rates, yield farming rewards, liquidation thresholds using compound interest formulas applied every block (~12 seconds). Over a year: ~2.6 million blocks. Float compound interest drift: significant. Fixed-point compound interest: truncation at every step. VDR: exact rational compound interest with zero truncation. (1 + r/n)^n is exact for rational r and integer n.

**Cross-chain bridges:** Assets moving between chains require exact balance accounting. A rounding discrepancy of 1 wei ($0.000000000000000001) between two chains means the bridge is either creating or destroying value. VDR: exact balance, zero discrepancy, mathematically provable conservation.

### Geodesy and Navigation

**Coordinate transformation chains:** Convert from GPS (WGS84) to local projection (UTM) to site coordinates to building coordinates. Each transformation is a matrix multiplication or polynomial evaluation. A survey traverse might chain 20 transformations. Float: ~10⁻¹² position error after 20 transforms. VDR-13 demonstrated exact Helmert roundtrip with zero residual. For legal survey work where millimeter precision has property-line implications, exact arithmetic eliminates the "which rounding produced this boundary?" question.

**GPS correction chains:** Differential GPS applies corrections from reference stations. Each correction is a small additive adjustment. Chaining corrections from multiple stations involves weighted averages where the weights must sum to exactly 1. Float: weights sum to 1 ± 10⁻¹⁶. VDR: weights sum to exactly 1. The correction is exactly what the mathematics says, not approximately.

**Inertial navigation:** Dead reckoning from accelerometer and gyroscope data. Each step integrates acceleration to get velocity, velocity to get position. Double integration of noisy data with float arithmetic means position error grows as t² from integration plus accumulated float drift. VDR: the integration is exact, so position error growth is purely from sensor noise, not arithmetic. You can separate sensor quality from computation quality.

**Cadastral surveying:** Property boundaries defined by chains of bearings and distances. "From the iron pin, N45°00'00"E for 100.00 feet" — each leg is a trigonometric computation whose endpoint is the start of the next leg. Float: after 20 legs, the traverse misclosure includes both measurement error and arithmetic error, and you can't tell which is which. VDR: arithmetic error is zero, misclosure is pure measurement error.

### Game Theory and Mechanism Design

**Auction clearing:** Vickrey-Clarke-Groves mechanism computes each bidder's payment as the externality they impose on others. This requires computing the optimal allocation with and without each bidder — combinatorial optimization producing exact rational payments. Float: payments may not sum to the correct total due to rounding. VDR: payments are exact rationals, budget balance is verifiable as exact equality.

**Matching markets:** Deferred acceptance algorithm (Gale-Shapley) for school choice, residency matching. The algorithm itself is combinatorial, but extensions with priorities and quotas involve tie-breaking with numerical scores. Float tie-breaking is platform-dependent — the same student might be assigned to different schools on different hardware. VDR: deterministic, reproducible, litigable.

**Shapley values:** The Shapley value of player i is a weighted average over all coalitions. For n players, this is a sum over 2ⁿ terms, each involving factorial weights. VDR-2 gym 17 verified exact Shapley values summing to v(N)=1 exactly. Float: Shapley values sum to 1 ± 10⁻¹⁵. For cost allocation in shared infrastructure (airports, utilities), the rounding determines who pays what.

**Mechanism design with money:** Designing incentive-compatible mechanisms requires verifying that no agent benefits from misreporting. The verification involves comparing utilities under truthful vs. strategic reporting — differences that may be small rational numbers. Float: a mechanism declared incentive-compatible might not be due to rounding. VDR: the comparison is exact, the mechanism either is or isn't incentive-compatible.

**Cournot/Bertrand equilibrium:** Firms compute optimal quantities or prices by solving systems of equations (reaction functions). The equilibrium is typically a rational function of the model parameters. VDR-2 gym 17 computed Cournot duopoly equilibrium q₁*=20/3, q₂*=14/3, profit₁=200/9 exactly. Float: equilibrium quantities are approximately right, profit calculations accumulate rounding through multiplication. VDR: exact equilibrium, exact profits.

**Voting theory:** Computing voting power indices (Banzhaf, Shapley-Shubik) requires summing over all winning coalitions. The indices are rational numbers that must sum to 1. Float: they don't quite. For constitutional analysis and corporate governance where voting power has legal significance, "approximately 1" is not acceptable.

### Common Thread

Every domain above shares the same structural problem: computation chains where each step's output feeds the next step's input, and the arithmetic error from each step compounds into the final result. VDR eliminates the compounding mechanism by eliminating the per-step error. The remaining errors — model approximation, measurement noise, truncation of infinite series — are the domain's problems, not the arithmetic's. VDR separates "is my model wrong?" from "is my arithmetic wrong?" and guarantees the answer to the second question is always no.
