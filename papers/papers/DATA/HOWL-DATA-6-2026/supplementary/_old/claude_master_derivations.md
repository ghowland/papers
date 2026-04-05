# HOWL SERIES — MASTER DERIVATION TABLES
# ========================================
# Every derivation chain traced step by step.
# All values verified against phys24_lib.py and computation.
# ========================================


## DERIVATION 1: COUPLING EXTRACTION

Three measured quantities → three GUT-normalized inverse couplings.

| Step | Operation | Result |
|------|-----------|--------|
| Input | alpha_inv = 137035999177/10^9 | Level 2 (CODATA) |
| Input | sin2_tW = 23122/100000 | Level 2 (LEP/SLD) |
| Input | alpha_s = 59/500 | Level 2 (PDG) |
| Compute | alpha = 1/alpha_inv | exact Fraction |
| Compute | cos2_tW = 1 - sin2_tW = 38439/50000 | exact Fraction |
| Compute | 1/alpha_1 = (3/5) * alpha_inv * cos2_tW | = 63.2103 |
| Compute | 1/alpha_2 = alpha_inv * sin2_tW | = 31.6855 |
| Compute | 1/alpha_3 = 1/alpha_s = 500/59 | = 8.4746 |

Pitfall: 1/alpha_2 = sin2_tW * alpha_inv, NOT alpha_inv/sin2_tW.
The formula is alpha_2 = alpha_EM/sin2_tW, so 1/alpha_2 = sin2_tW/alpha_EM = sin2_tW * alpha_inv.


## DERIVATION 2: MEASURED GAP RATIO

From three inverse couplings → one ratio.

| Step | Operation | Result |
|------|-----------|--------|
| Input | 1/a1 = 63.2103 | from Derivation 1 |
| Input | 1/a2 = 31.6855 | from Derivation 1 |
| Input | 1/a3 = 8.4746 | from Derivation 1 |
| Compute | numerator = 1/a1 - 1/a2 = 31.5249 | exact Fraction |
| Compute | denominator = 1/a2 - 1/a3 = 23.2109 | exact Fraction |
| Compute | gap = num/den = 1.3582 | exact Fraction |

This is the target. Every model gap ratio is compared to 1.3582.


## DERIVATION 3: SM BETA COEFFICIENTS

From gauge group SU(3)xSU(2)xU(1) + particle content → three exact fractions.

| Step | Operation | b1 (U1) | b2 (SU2) | b3 (SU3) |
|------|-----------|---------|----------|----------|
| Gauge | -(11/3)*C2(adj) | 0 (abelian) | -(11/3)*2 = -22/3 | -(11/3)*3 = -11 |
| Gen 1 | per-gen shift | +4/3 | +4/3 | +4/3 |
| Gen 2 | per-gen shift | +4/3 | +4/3 | +4/3 |
| Gen 3 | per-gen shift | +4/3 | +4/3 | +4/3 |
| Higgs | (1,2,1/2) scalar | +1/10 | +1/6 | 0 |
| Total | sum | 0+4+1/10 = 41/10 | -22/3+4+1/6 = -19/6 | -11+4+0 = -7 |


## DERIVATION 4: SM GAP RATIO

From three SM betas → one exact fraction.

| Step | Operation | Result |
|------|-----------|--------|
| Compute | b1 - b2 = 41/10 - (-19/6) = 123/30 + 95/30 = 218/30 = 109/15 | exact |
| Compute | b2 - b3 = -19/6 - (-7) = -19/6 + 42/6 = 23/6 | exact |
| Compute | gap = (109/15) / (23/6) = (109*6)/(15*23) = 654/345 = 218/115 | exact |
| Value | 218/115 = 1.8957 | 39.6% miss from measured 1.3582 |


## DERIVATION 5: GENERATION DEMOCRACY

Why fermions don't affect the gap ratio.

| Step | Operation | Result |
|------|-----------|--------|
| Input | Per-gen shift = (4/3, 4/3, 4/3) | Level 1 (SU(5) anomaly cancellation) |
| Compute | Fermion gap numerator = 4/3 - 4/3 = 0 | exact zero |
| Compute | Fermion gap denominator = 4/3 - 4/3 = 0 | exact zero |
| Conclusion | Gap ratio is independent of N_gen | Level 1 proof |
| Consequence | Gap ratio = gauge + Higgs only | The boson problem |


## DERIVATION 6: PURE-GAUGE GAP

The baseline before Higgs correction.

| Step | Operation | Result |
|------|-----------|--------|
| Gauge b1 | 0 (U(1) abelian) | Level 1 |
| Gauge b2 | -(11/3)*2 = -22/3 | C2(adj SU(2)) = 2 |
| Gauge b3 | -(11/3)*3 = -11 | C2(adj SU(3)) = 3 |
| Numerator | 0 - (-22/3) = 22/3 | exact |
| Denominator | -22/3 - (-11) = 11/3 | exact |
| Gap | (22/3)/(11/3) = 22/11 = 2 | the 11 cancels |
| Casimir form | C2(SU(2)) / (C2(SU(3)) - C2(SU(2))) = 2/(3-2) = 2 | independent of YM integer |


## DERIVATION 7: CABIBBO DOUBLET SHIFTS

From representation (3,2,1/6) → three exact fractions.

| Step | Operation | Result |
|------|-----------|--------|
| Input | (d3, d2, Y) = (3, 2, 1/6), vector-like | Level 1 |
| db1 formula | (2/5) * d3 * d2 * Y^2 | exact |
| db1 | (2/5) * 3 * 2 * (1/36) = (2/5)*(1/6) = 1/15 | exact |
| db2 formula | (2/3) * d3 * S2(fund SU(2)) | S2 = 1/2 |
| db2 | (2/3) * 3 * (1/2) = 1 | exact |
| db3 formula | (1/3) * d2 * S2(fund SU(3)) | S2 = 1/2 |
| db3 | (1/3) * 2 * (1/2) = 1/3 | exact |


## DERIVATION 8: MODIFIED BETAS AND CD GAP RATIO

SM betas + CD shifts → modified betas → new gap ratio.

| Step | Operation | Result |
|------|-----------|--------|
| b1_mod | 41/10 + 1/15 = 123/30 + 2/30 = 125/30 = 25/6 | exact |
| b2_mod | -19/6 + 1 = -19/6 + 6/6 = -13/6 | exact |
| b3_mod | -7 + 1/3 = -21/3 + 1/3 = -20/3 | exact |
| Numerator | 25/6 - (-13/6) = 38/6 = 19/3 | exact |
| Denominator | -13/6 - (-20/3) = -13/6 + 40/6 = 27/6 = 9/2 | exact |
| Gap | (19/3) / (9/2) = (19*2)/(3*9) = 38/27 | exact |
| Value | 38/27 = 1.4074 | 3.6% miss from measured 1.3582 |


## DERIVATION 9: DOUBLE ACTION MECHANISM

Why the CD correction is so effective.

| Step | Operation | Result |
|------|-----------|--------|
| Numerator change | db1 - db2 = 1/15 - 1 = -14/15 | DECREASES numerator |
| Denominator change | db2 - db3 = 1 - 1/3 = +2/3 | INCREASES denominator |
| Combined | Numerator shrinks 12.8%, denominator grows 17.4% | Double action |
| Key ratio | db2/db1 = 1/(1/15) = 15 | Asymmetry = 15 |
| Source | Y = 1/6 → Y^2 = 1/36 → db1 tiny | Y = 1/6 is the mechanism |
| Scaling | db2/db1 = constant/(12Y^2/5) ∝ 1/Y^2 | Smaller Y → larger asymmetry |


## DERIVATION 10: Y-DEPENDENCE FOR (3,2,Y) FAMILY

Analytical gap ratio as function of hypercharge.

| Step | Operation | Result |
|------|-----------|--------|
| Fixed | db2 = 1, db3 = 1/3 for all (3,2,Y) | independent of Y |
| Variable | db1 = (2/5)*3*2*Y^2 = (12/5)*Y^2 | varies as Y^2 |
| Modified numerator | 109/15 + (12/5)*Y^2 - 1 = 94/15 + (12/5)*Y^2 | |
| Modified denominator | 23/6 + 1 - 1/3 = 9/2 | constant for all Y |
| Gap(Y) | [94/15 + (12/5)*Y^2] / (9/2) | |
| Simplified | (188 + 72*Y^2) / 135 | analytical formula |
| At Y=1/6 | (188 + 2) / 135 = 190/135 = 38/27 | confirms |
| Crossover | Gap(Y) = 218/115 when Y ~ 0.97 | larger Y → worse than SM |


## DERIVATION 11: ONE-LOOP CROSSING SCALE

Finding where 1/alpha_1 and 1/alpha_2 cross.

| Step | Operation | Result |
|------|-----------|--------|
| RG equation | 1/alpha_i(mu) = 1/alpha_i(M_Z) - b_i/(2*pi) * ln(mu/M_Z) | one-loop |
| Define | L = ln(mu/M_Z) / (2*pi) | dimensionless scale |
| Crossing | 1/a1 - b1*L = 1/a2 - b2*L | set alpha_1 = alpha_2 |
| Solve | L = (1/a1 - 1/a2) / (b1 - b2) | exact Fraction |
| SM betas | L_SM = 31.525 / (109/15) = 4.338 | |
| CD betas | L_CD = 31.525 / (19/3) = 4.978 | |
| Scale | M_GUT = M_Z * exp(2*pi*L_CD) | |
| log10 | log10(M_GUT/GeV) = 15.54 | one-loop CD prediction |


## DERIVATION 12: ONE-LOOP ALPHA_S PREDICTION

From unification scale → predicted alpha_s at M_Z.

| Step | Operation | Result |
|------|-----------|--------|
| Input | L_GUT = 4.978 from Derivation 11 | |
| Compute | 1/alpha_GUT = 1/a1 - b1_mod*L = 1/a2 - b2_mod*L | crossing value |
| Run back | 1/alpha_3(M_Z) = 1/alpha_GUT + b3_mod*L | run SU(3) down |
| Predict | alpha_s = 1/(1/alpha_3) = 0.10769 | |
| Miss | vs measured 0.1180 = 8.74% | one-loop insufficient |


## DERIVATION 13: ONE-LOOP SIN2_THETA_W PREDICTION

From SU(5) value 3/8 → run to M_Z.

| Step | Operation | Result |
|------|-----------|--------|
| GUT value | sin2_tW(GUT) = 3/8 = 0.375 | SU(5) prediction |
| RG running | sin2(M_Z) depends on (b1-b2) running | one-loop |
| b_EM | b_EM = (5/3)*b1_mod + b2_mod = (5/3)*(25/6) + (-13/6) = 125/18 - 13/6 = 43/9 | |
| Predict | sin2_tW = 0.22845 | |
| Miss | vs measured 0.23122 = 1.199% | |


## DERIVATION 14: TWO-LOOP ALPHA_S (EULER INTEGRATION)

Full two-loop running with binary search for exact crossing.

| Step | Operation | Result |
|------|-----------|--------|
| Input | SM bij matrix (9 Fractions, Table 6 of master tables) | Level 1 |
| Input | VL dbij matrix (9 Fractions, Table 7 of master tables) | Level 1 |
| Compute | bij_full = bij_SM + dbij_VL (element-wise) | 9 exact Fractions |
| Method | Euler integration of d(1/alpha_i)/dL = -b_i - sum_j b_ij*alpha_j/(2pi) | numerical |
| Search | Binary search over L_GUT to find crossing 1/a1 = 1/a2 | 60 bisections |
| Run back | Euler integrate from L_GUT to 0 with bij_full | |
| SM bij only | alpha_s predicted = 0.11753, miss = 0.397% | |
| Full bij | alpha_s predicted = 0.11838, miss = 0.325% | |
| Improvement | Full bij improves over SM bij | full b_ij adds VL threshold effects |

Critical: bij_VL[1][1] = 15/4, NOT 39/4. Fermion only. Adding gauge double-counts.


## DERIVATION 15: KOIDE RATIO

From three lepton masses → K and a^2.

| Step | Operation | Result |
|------|-----------|--------|
| Input | m_e, m_mu, m_tau (Level 2 masses) | |
| Compute | K = (m_e + m_mu + m_tau) / (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2 | |
| Result | K = 0.66666051 | within 6e-6 of 2/3 |
| Amplitude | a^2 = 2*(3K - 1) = 1.999963 | within 4e-5 of 2 |
| Identity | K = (1 + a^2/2) / 3 | algebraic identity for N=3 |


## DERIVATION 16: KOIDE M_TAU PREDICTION

Set K = 2/3 exactly, predict m_tau from m_e and m_mu.

| Step | Operation | Result |
|------|-----------|--------|
| Hypothesis | K = 2/3 exactly → a^2 = 2 exactly | Level 1 hypothesis |
| Setup | (sqrt(m_e) + sqrt(m_mu) + x)^2 = (3/2)*(m_e + m_mu + x^2) | x = sqrt(m_tau) |
| Let | S = sqrt(m_e) + sqrt(m_mu), M = m_e + m_mu | |
| Quadratic | x^2 - 4Sx + (3M - 2S^2) = 0 | |
| Solve | x = 2S + sqrt(4S^2 - 3M + 2S^2) = 2S + sqrt(6S^2 - 3M) | take + root |
| Square | m_tau = x^2 = 1776.969 MeV | |
| Measured | m_tau = 1776.86 MeV | |
| Miss | 0.00614% | 0.91 sigma |
| Other root | x^2 = 3.317 MeV | not physical |


## DERIVATION 17: DM/BARYON RATIO

From beta integers → cosmological prediction.

| Step | Operation | Result |
|------|-----------|--------|
| Extract | YM = 11 from gauge coefficient -(11/3)*C2(adj) | Level 1 |
| Extract | |b2_mod numerator| = 13 from b2_mod = -13/6 | Level 1 |
| Formula | DM/baryon = (2*YM / |b2_mod_num|) * pi | |
| Compute | = (22/13) * pi = (22/13) * 4*R2 | |
| Value | = 5.3165 | |
| Planck 2018 | 5.3204 | |
| Miss | 0.0725% | |


## DERIVATION 18: OMEGA_DM

From same beta integers → dark matter density fraction.

| Step | Operation | Result |
|------|-----------|--------|
| Formula | Omega_DM = (4*YM / |b2_mod_num|^2) * R2 | |
| Compute | = (44/169) * R2 | |
| Key point | R2 cancels in the product derivation | |
| Result | 44/169 is a PURE RATIONAL — no irrational factors | |
| Value | = 0.2045 | |
| Integers | 44 = 4*11, 169 = 13^2 | same two integers |


## DERIVATION 19: AMPLIFICATION FACTOR DECOMPOSITION

From DM/baryon → boundary amplification → integer decomposition.

| Step | Operation | Result |
|------|-----------|--------|
| Formula | A = (DM/baryon) * 2c^2 / v^2 | amplification at rotation velocity v |
| Expand | A = (22/13)*pi * 2c^2/v^2 | |
| Factor | A = (22/13) * 2 * pi * (c/v)^2 | |
| Simplify | A = (44/13) * pi * (c/v)^2 | |
| R2 form | A = (44/13) * 4R2 * (c/v)^2 | |
| Reduced | A / [pi*(c/v)^2] = 44/13 = 4*YM / |b2_mod_num| | same integers |


## DERIVATION 20: KEPLER VIA R2

The orbital period in R2 form.

| Step | Operation | Result |
|------|-----------|--------|
| Standard | T^2 = 4*pi^2 * a^3 / (GM) | Kepler's third law |
| Substitute | 4*pi^2 = 4*(4R2)^2 = 64*R2^2 | R2 = pi/4 |
| R2 form | T^2 = 64*R2^2 * a^3 / (GM) | same R2 as pipes, wires, discs |
| Identity | 64*R2^2 = 64*(pi/4)^2 = 64*pi^2/16 = 4*pi^2 | verified to 20 digits |
| Earth check | T = 365.26 days vs 365.25 | <0.01% |


## DERIVATION 21: GPS CLOCK CORRECTION

From soliton coupling → time dilation components.

| Step | Operation | Result |
|------|-----------|--------|
| Gravitational | df/f = GM/(c^2) * (1/R_earth - 1/R_GPS) | higher = faster |
| Value | = +5.291e-10 | positive |
| Velocity | df/f = -v_GPS^2 / (2c^2) | moving = slower |
| Value | = -8.349e-11 | negative |
| Total | df/f = +4.456e-10 | gravity dominates |
| Per day | total * 86400 * 10^6 = +38.5 us/day | |
| Meaning | GPS clocks gain 38.5 microseconds/day | must be corrected |


## DERIVATION 22: MOND a0

From R2 and Hubble → MOND acceleration scale.

| Step | Operation | Result |
|------|-----------|--------|
| Formula | a0 = c * H0 / (8*R2) = c * H0 / (2*pi) | |
| H0 | 67.4 km/s/Mpc in SI = 2.184e-18 s^-1 | Planck value |
| Compute | a0 = 299792458 * 2.184e-18 / (2*pi) | |
| Value | = 1.042e-10 m/s^2 | |
| Published | MOND a0 ~ 1.2e-10 m/s^2 | |
| Match | within factor ~1.15 | ~8% miss |


## DERIVATION 23: PROCESS RATE (GRAVITATIONAL DILATION)

From GM/(rc^2) → time dilation factor.

| Step | Operation | Result |
|------|-----------|--------|
| Coupling | phi = GM/(rc^2) | dimensionless soliton coupling |
| Rate | sqrt(1 - 2*phi) | process rate relative to infinity |
| Earth | phi = 6.96e-10 | GM_E/(R_E*c^2) |
| Rate | 1 - 6.96e-10 | clocks tick slower at surface |
| GPS orbit | phi = 1.67e-10 | GM_E/(R_GPS*c^2) |
| Rate | 1 - 1.67e-10 | closer to infinity → faster |
| Difference | GPS rate > surface rate | the 38.5 us/day correction |


## DERIVATION 24: MUON LIFETIME

Reading across velocity boundary.

| Step | Operation | Result |
|------|-----------|--------|
| Rest lifetime | tau_rest = 2.1970e-6 s | Level 2 (PDG) |
| Lorentz factor | gamma = 1/sqrt(1 - v^2/c^2) | |
| At v = 0.99c | gamma = 1/sqrt(1 - 0.9801) = 1/sqrt(0.0199) = 7.089 | |
| Observed | tau_obs = gamma * tau_rest = 15.57e-6 s | |
| Interpretation | Muon internal rate is FIXED. Observer reads across velocity boundary. | |


## DERIVATION 25: HILL SPHERE

Soliton dominance boundary.

| Step | Operation | Result |
|------|-----------|--------|
| Formula | R_Hill = a * (m/(3M))^(1/3) | |
| Earth | a = 1 AU, m = M_earth, M = M_sun | |
| Value | R_Hill = 1.496e11 * (5.972e24/(3*1.989e30))^(1/3) | |
| Result | ~ 1.50e9 m = 1.50e6 km | |
| Meaning | Inside: Earth's gravity dominates. Outside: Sun's. | |


## DERIVATION 26: R2 CANCELLATION IN K_J * R_K

How R2 enters and exits the metrological product.

| Step | Operation | Result |
|------|-----------|--------|
| K_J | = 2e/h = 2e/(8R2*hbar) | Josephson constant |
| R_K | = h/e^2 = 8R2*hbar/e^2 | von Klitzing constant |
| Product | K_J * R_K = [2e/(8R2*hbar)] * [8R2*hbar/e^2] | |
| Cancel | 8R2*hbar divides out | |
| Result | = 2/e | R2-free. Measurable to 10^-8 |


## DERIVATION 27: R2 CANCELLATION IN WIRE R * CAP C

Cross-domain cancellation.

| Step | Operation | Result |
|------|-----------|--------|
| Wire R | R = rho*L / (R2*d^2) | resistance, R2 in denominator |
| Cap C | C = eps0 * R2*d^2 / t | capacitance, R2 in numerator |
| Product | R*C = [rho*L/(R2*d^2)] * [eps0*R2*d^2/t] | |
| Cancel | R2*d^2 divides out | |
| Result | = rho*eps0*L/t | R2-free. Verified to 30 digits |


## DERIVATION 28: FERMION VS SCALAR — MAGNITUDE DOUBLING

Why VL fermion beats scalar with same quantum numbers.

| Step | Operation | Fermion | Scalar | Ratio |
|------|-----------|---------|--------|-------|
| db1 | from formula | 1/15 | 1/30 | 2:1 |
| db2 | from formula | 1 | 1/2 | 2:1 |
| db3 | from formula | 1/3 | 1/6 | 2:1 |
| db2/db1 | asymmetry | 15 | 15 | same |
| Gap ratio | result | 38/27 = 1.407 | ~1.632 | — |
| Distance | from measured | 0.049 | 0.274 | 5.6x worse |

Fermion has 2x the shift at fixed asymmetry → 5.6x better gap ratio correction.


## DERIVATION 29: SM PARAMETER REDUCTION — THETA_QCD

| Step | Operation | Result |
|------|-----------|--------|
| SM count | 19 parameters | standard |
| theta_QCD | can be rotated away by quark mass rephasing | |
| Method | energy minimization of QCD vacuum | |
| Result | theta_QCD = 0 is the minimum | |
| Count | 19 → 18 | unconditional reduction |


## DERIVATION 30: KOIDE C3 CLOSURE

Why Koide's K = 2/3 is not a discovery.

| Step | Operation | Result |
|------|-----------|--------|
| Data | 3 positive masses (m_e, m_mu, m_tau) | 3 numbers |
| Parameters | M (scale), a (amplitude), theta_0 (phase) | 3 parameters |
| DOF | 3 data - 3 parameters = 0 constraints | tautology |
| Any 3 masses | K = (1+a^2/2)/3 always has a solution | mathematical identity |
| Saddle | K = 2/3 is a saddle point on C3 landscape | not a minimum |
| Conclusion | K ~ 2/3 is not selected by symmetry | tautology + saddle = closure |
| Open | derive a^2 = 2 from physics | no known attack |


## SUMMARY: DERIVATION CHAIN DEPENDENCIES

| Derivation | Depends on | Produces | Type |
|------------|-----------|----------|------|
| D1: Coupling extraction | 3 L2 measurements | inv_a1, inv_a2, inv_a3 | L1 on L2 |
| D2: Measured gap | D1 output | gap_measured = 1.3582 | derived |
| D3: SM betas | Gauge group + SM content | b1=41/10, b2=-19/6, b3=-7 | L1 |
| D4: SM gap | D3 output | 218/115 | L1 |
| D5: Gen democracy | D3 decomposition | fermion contribution = 0 | L1 proof |
| D6: Pure-gauge gap | D3 gauge parts | 2 | L1 |
| D7: CD shifts | (3,2,1/6) + Dynkin | db=(1/15, 1, 1/3) | L1 |
| D8: CD gap | D3 + D7 | 38/27 | L1 |
| D9: Double action | D7 analysis | db2/db1 = 15 | L1 |
| D10: Y-dependence | D9 generalized | Gap(Y) = (188+72Y^2)/135 | L1 |
| D11: Crossing scale | D1 + D8 | L_GUT = 4.978 | derived |
| D12: 1L alpha_s | D11 | alpha_s = 0.10769, miss 8.74% | derived |
| D13: 1L sin2_tW | D8 + D11 | sin2 = 0.22845, miss 1.199% | derived |
| D14: 2L alpha_s | D1 + D8 + bij matrices | alpha_s = 0.11838, miss 0.325% | derived |
| D15: Koide ratio | 3 L2 masses | K = 0.66666, a^2 = 1.99996 | derived |
| D16: Koide m_tau | D15 + hypothesis a^2=2 | m_tau = 1776.969 MeV | conditional |
| D17: DM/baryon | D8 integers (11, 13) | (22/13)*pi = 5.3165 | derived |
| D18: Omega_DM | D17 integers | (44/169)*R2 | derived |
| D19: Amplification | D17 decomposition | A = (44/13)*pi*(c/v)^2 | derived |
| D20: Kepler R2 | R2 = pi/4 | T^2 = 64R2^2*a^3/(GM) | L1 identity |
| D21: GPS | GM/(rc^2) | 38.5 us/day | derived |
| D22: MOND a0 | R2 + H0 | cH0/(8R2) = 1.04e-10 | derived |
| D23: Process rate | GM/(rc^2) | sqrt(1-2phi) | L1 formula |
| D24: Muon | SR gamma | tau_obs = gamma*tau_rest | L1 formula |
| D25: Hill sphere | Gravity | R = a*(m/3M)^(1/3) | L1 formula |
| D26: KJ*RK cancel | h = 8R2*hbar | 2/e (R2-free) | L1 identity |
| D27: RC cancel | R2 in R and C | rho*eps0*L/t (R2-free) | L1 identity |
| D28: Fermion vs scalar | Dynkin coefficient ratio | 2:1 magnitude, same asymmetry | L1 |
| D29: theta_QCD | Energy minimization | 19 → 18 parameters | L1 derivation |
| D30: Koide closure | DOF counting + saddle | tautology, not discovery | L1 proof |
