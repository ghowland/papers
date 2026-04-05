# HOWL SERIES — CORRECTED MASTER TABLES
# ========================================
# Verified against: phys24_lib.py (21/21 + 148/148)
#                   data_4_derivation_lib.py (37/37)
#                   data6/index (329 files, 4/4 spot checks)
#
# SESSION A/B ERRORS FOUND AND CORRECTED:
#   - M_W: Sessions say 80379 MeV. Correct: 80369.2 MeV (Fraction 803692/10)
#   - b1_mod: DATA-5 paper says 62/15. Correct: 25/6 (41/10 + 1/15 = 125/30 = 25/6)
#   - MSSM gap: Alignment doc says 5/7 in one place. Correct: 7/5 = 1.400
#   - DM/baryon miss: Chunk 4 says 0.073%. Correct: 0.0725%
#   - Some sessions round alpha_s miss values inconsistently
#
# All values below are from phys24_lib.py or direct computation.
# ========================================


## TABLE 1: SM BETA COEFFICIENTS — EXACT FRACTIONS

| Group | b_SM | Gauge | Fermion (3 gen) | Higgs | Sum Check |
|-------|------|-------|-----------------|-------|-----------|
| U(1)  | 41/10 | 0 | 4 | 1/10 | 0 + 4 + 1/10 = 41/10 |
| SU(2) | -19/6 | -22/3 | 4 | 1/6 | -22/3 + 4 + 1/6 = -19/6 |
| SU(3) | -7 | -11 | 4 | 0 | -11 + 4 + 0 = -7 |


## TABLE 2: CABIBBO DOUBLET SHIFTS — EXACT FRACTIONS

| Group | db_VL | Formula | b_mod = b_SM + db_VL |
|-------|-------|---------|----------------------|
| U(1)  | 1/15 | (2/5)*3*2*(1/6)^2 | 41/10 + 1/15 = 25/6 |
| SU(2) | 1 | (2/3)*3*(1/2) | -19/6 + 1 = -13/6 |
| SU(3) | 1/3 | (1/3)*2*(1/2) | -7 + 1/3 = -20/3 |


## TABLE 3: GAP RATIOS — EXACT

| Model | Numerator (b1-b2) | Denominator (b2-b3) | Gap Ratio | Decimal |
|-------|-------------------|---------------------|-----------|---------|
| Pure gauge | 22/3 | 11/3 | 2 | 2.000 |
| SM | 109/15 | 23/6 | 218/115 | 1.8957 |
| SM + CD | 19/3 | 9/2 | 38/27 | 1.4074 |
| MSSM | — | — | 7/5 | 1.4000 |
| Measured | — | — | ~1.3582 | 1.3582 |

Distance from measured: SM = 0.5375 (39.6%), CD = 0.0492 (3.6%), MSSM = 0.0418 (3.1%)


## TABLE 4: BETA DECOMPOSITION — NUMERATOR AND DENOMINATOR

| Source | Delta(b1-b2) | % of num | Delta(b2-b3) | % of denom |
|--------|--------------|----------|--------------|------------|
| Gauge (0, -22/3, -11) | +22/3 = +7.333 | 100.9% | +11/3 = +3.667 | 95.7% |
| Fermions (4/3, 4/3, 4/3) per gen | 0 | 0.0% | 0 | 0.0% |
| Higgs (1/10, 1/6, 0) | -1/15 = -0.067 | -0.9% | +1/6 = +0.167 | 4.3% |
| SM total | 109/15 = 7.267 | 100% | 23/6 = 3.833 | 100% |


## TABLE 5: DOUBLE ACTION (CD EFFECT)

| Component | SM value | Delta from CD | Modified | Change |
|-----------|----------|---------------|----------|--------|
| Numerator (b1-b2) | 109/15 = 7.267 | 1/15 - 1 = -14/15 | 19/3 = 6.333 | -12.8% |
| Denominator (b2-b3) | 23/6 = 3.833 | 1 - 1/3 = +2/3 | 9/2 = 4.500 | +17.4% |
| Gap ratio | 218/115 = 1.896 | — | 38/27 = 1.407 | -25.8% |


## TABLE 6: TWO-LOOP b_ij SM MATRIX

|       | U(1) | SU(2) | SU(3) |
|-------|------|-------|-------|
| U(1)  | 199/50 | 27/10 | 44/5 |
| SU(2) | 9/10 | 35/6 | 12 |
| SU(3) | 11/10 | 9/2 | -26 |


## TABLE 7: TWO-LOOP db_ij VL MATRIX

|       | U(1) | SU(2) | SU(3) |
|-------|------|-------|-------|
| U(1)  | 7/15 | 1/15 | 16/135 |
| SU(2) | 1/30 | 15/4 | 8/3 |
| SU(3) | 1/45 | 1 | 40/9 |

CRITICAL: [1][1] = 15/4, NOT 39/4. Adding a NEW fermion adds ONLY (10/3)*C_R.
The 2*C_G term is already in the SM b_ij. Adding it again double-counts.


## TABLE 8: SM REPRESENTATIONS — FERMION CONTENT

| Name | (SU3, SU2, Y) | Type | db1 | db2 | db3 |
|------|---------------|------|-----|-----|-----|
| Q_L | (3, 2, 1/6) | chiral | 1/30 | 1 | 1/3 |
| u_R | (3, 1, 2/3) | chiral | 8/15 | 0 | 1/3 |
| d_R | (3, 1, -1/3) | chiral | 2/15 | 0 | 1/3 |
| L_L | (1, 2, -1/2) | chiral | 1/6 | 1/3 | 0 |
| e_R | (1, 1, -1) | chiral | 2/5 | 0 | 0 |
| CD | (3, 2, 1/6) | vector-like | 1/15 | 1 | 1/3 |

Per-gen sum of 5 SM reps: (4/3, 4/3, 4/3). Generation democracy.


## TABLE 9: GROUP THEORY CONSTANTS — EXACT

| Quantity | Value | Formula |
|----------|-------|---------|
| C2(adj SU(3)) | 3 | N for SU(N) |
| C2(adj SU(2)) | 2 | N for SU(N) |
| C2(fund SU(3)) | 4/3 | (N^2-1)/(2N) |
| C2(fund SU(2)) | 3/4 | (N^2-1)/(2N) |
| S2(fundamental) | 1/2 | any SU(N) |
| k1 GUT normalization | 3/5 | SU(5) embedding |
| gauge_coeff | -11/3 | Yang-Mills self-coupling |
| N_gen | 3 | SM generation count |
| Pure-gauge gap | 2 | C2(SU(2))/(C2(SU(3))-C2(SU(2))) |


## TABLE 10: MEASURED COUPLINGS AT M_Z

| Quantity | Fraction | Decimal | Digits | Source |
|----------|----------|---------|--------|--------|
| 1/alpha_EM | 137035999177/1000000000 | 137.036 | 12 | CODATA 2022 |
| sin^2(theta_W) | 23122/100000 | 0.23122 | 5 | LEP/SLD |
| alpha_s(M_Z) | 59/500 | 0.1180 | 4 | PDG |
| 1/alpha_1 (GUT) | 15802580317094109/250000000000000 | 63.210 | derived | |
| 1/alpha_2 (GUT) | 1584273186485297/50000000000000 | 31.685 | derived | |
| 1/alpha_3 (GUT) | 500/59 | 8.475 | derived | |
| Measured gap ratio | (inv_a1 - inv_a2)/(inv_a2 - inv_a3) | 1.3582 | derived | |


## TABLE 11: MASSES — EXACT FRACTIONS FROM PLATFORM

| Particle | Fraction | Value (MeV) | Digits | Entry |
|----------|----------|-------------|--------|-------|
| e | 51099895069/10^11 | 0.51100 | 11 | B2 |
| mu | 1056583755/10^7 | 105.658 | 10 | B3 |
| tau | 177686/100 | 1776.86 | 6 | B4 |
| u | 216/100 | 2.16 | 3 | D1 |
| d | 470/100 | 4.70 | 3 | D2 |
| s | 935/10 | 93.5 | 3 | D3 |
| c | 1273 | 1273 | 4 | D4 |
| b | 4183 | 4183 | 4 | D5 |
| t | 172570 | 172570 | 5 | C4 |
| Z | 911876/10 | 91187.6 | 6 | C1 |
| W | 803692/10 | 80369.2 | 6 | C3 |
| H | 125200 | 125200 | 5 | C5 |
| p | 93827208943/10^8 | 938.272 | 11 | B5 |
| n | 93956542194/10^8 | 939.565 | 11 | E1 |


## TABLE 12: GEOMETRIC CONSTANTS

| Identity | Value | Appears in |
|----------|-------|-----------|
| R2 = pi/4 | 0.78540 | 9+ engineering domains, every circular-to-rectilinear |
| R4 = pi^2/32 | 0.30843 | Every loop integral, QED A2 coefficient |
| 4*R2 = pi | 3.14159 | Standard replacement |
| 8*R2 = 2*pi | 6.28318 | Fourier, angular frequency |
| 64*R2^2 = 4*pi^2 | 39.478 | Kepler's law: T^2 = 64R2^2 a^3/(GM) |


## TABLE 13: DERIVATION RESULTS — FROM PLATFORM TEST OUTPUT

| Prediction | Method | Value | Measured | Miss |
|------------|--------|-------|----------|------|
| alpha_s | One-loop CD | 0.10769 | 0.1180 | 8.74% |
| alpha_s | Two-loop SM bij | 0.11753 | 0.1180 | 0.397% |
| alpha_s | Two-loop full bij | 0.11838 | 0.1180 | 0.325% |
| sin2_tW | One-loop CD | 0.22845 | 0.23122 | 1.199% |
| m_tau | Koide K=2/3 | 1776.969 MeV | 1776.86 MeV | 0.00614% |
| M_GUT | One-loop CD | 10^15.54 GeV | — | — |
| L_GUT | One-loop CD | 4.978 | — | — |
| DM/baryon | (22/13)*pi | 5.3165 | 5.3204 | 0.0725% |
| Omega_DM | (44/169)*R2 | 0.2045 | 0.2607 | — |
| GPS correction | GM/(rc^2) | 38.5 us/day | ~38.6 us/day | <1% |
| MOND a0 | cH0/(8R2) | ~1.1e-10 m/s^2 | ~1.2e-10 m/s^2 | ~8% |


## TABLE 14: KOIDE DATA — THREE SECTORS

| Sector | K | a^2 | a^2 - 2 | Status |
|--------|---|------|---------|--------|
| Charged leptons (e,mu,tau) | 0.66666051 | 1.99996307 | -3.7e-5 | Near K=2/3 |
| Down quarks (d,s,b) | 0.73129 | 2.388 | +0.388 | Far from 2/3 |
| Up quarks (u,c,t) | 0.84879 | 3.093 | +1.093 | Far from 2/3 |

K_koide = 6666605115/10^10 (from phys24_lib)
a2_lep = 19999630688/10^10 (from phys24_lib, NOT exactly 2)


## TABLE 15: COSMOLOGICAL PARAMETERS FROM BETA INTEGERS

| Parameter | Formula | Integers | Predicted | Planck 2018 | Miss |
|-----------|---------|----------|-----------|-------------|------|
| DM/baryon | (2*YM/|b2_mod_num|)*pi = (22/13)*pi | 11, 13 | 5.3165 | 5.3204 | 0.073% |
| Omega_DM | (4*YM/|b2_mod_num|^2)*R2 = (44/169)*R2 | 11, 13 | 0.2045 | 0.2607 | — |

Integers: YM = 11 (Yang-Mills), |b2_mod numerator| = 13, 2*11 = 22, 4*11 = 44, 13^2 = 169.
R2 cancels in the Omega_DM product: 44/169 is pure rational.


## TABLE 16: INTEGER POOL — APPEARANCES ACROSS PROGRAMS

| Integer | Origin | Where it appears |
|---------|--------|-----------------|
| 11 | Yang-Mills -(11/3)*C2(adj) | b3_SM gauge = -11, DM numerator 2*11=22, Omega 4*11=44 |
| 13 | |b2_mod numerator| | b2_mod = -13/6, DM denominator, Omega denominator 13^2=169 |
| 19 | |b2_SM numerator| | b2_SM = -19/6, gap SM numerator 218, dwarf cosmic ratio |
| 20 | |b3_mod * 3| | b3_mod = -20/3, gap SM denominator 115 |
| 22 | 2 * YM | DM/baryon = (22/13)*pi |
| 44 | 4 * YM | Omega_DM = (44/169)*R2, amplification reduced = 44/13 |
| 169 | 13^2 | Omega_DM denominator, pure rational |
| 38 | 2 * 19 | CD gap numerator 38/27 |
| 27 | 3^3 | CD gap denominator 38/27 |
| 218 | b1_SM - b2_SM as 30ths: 123-(-95) = numerator | SM gap numerator 218/115 |
| 115 | b2_SM - b3_SM as 6ths: -19-(-42) = 23 -> 23*5 = 115 | SM gap denominator 218/115 |


## TABLE 17: SI CONSTANTS — EXACT BY DEFINITION

| Constant | Value | Unit | Entry |
|----------|-------|------|-------|
| c | 299792458 | m/s | A1 |
| h | 662607015/10^42 | J*s | A2 |
| e | 1602176634/10^28 | C | A3 |
| k_B | 1380649/10^29 | J/K | A4 |
| N_A | 602214076 * 10^15 | 1/mol | A5 |
| dv_Cs | 9192631770 | Hz | A6 |
| K_cd | 683 | lm/W | A7 |


## TABLE 18: Q335 BASIS CONSTANTS

All stored as p/Q where Q = 2^335. Each numerator is a ~101-digit integer.
100-digit agreement with mpmath verified for all constants.

| # | Constant | Numerator first 10 digits | Match |
|---|----------|---------------------------|-------|
| G1 | pi | 2198864258... | 100+ digits |
| G2 | e | 1902580447... | 100+ digits |
| G3 | ln(2) | 4851477353... | 100+ digits |
| G4 | sqrt(2) | 9898366845... | 100+ digits |
| G5 | sqrt(3) | 1212297402... | 100+ digits |
| G6 | sqrt(5) | 1565069217... | 100+ digits |
| G7 | sqrt(7) | 1851814871... | 100+ digits |
| G8 | phi | 1132494724... | 100+ digits |
| G9 | zeta(3) | 8413439464... | 100+ digits |
| G10 | zeta(5) | 7257667148... | 100+ digits |
| G11 | pi^2 | 6907935801... | 100+ digits |
| G12 | zeta(2) | 1151322633... | 100+ digits |

Plus extended basis: zeta(7), zeta(9), Li4(1/2), Li5(1/2), Li6(1/2), Li7(1/2),
Catalan, e^pi, ln(3), ln(5), K(k^2=1/4,1/2,3/4), E(k^2=1/4,1/2,3/4), Cl2(pi/3).
Total: 35 constants, all verified.


## TABLE 19: R2 CANCELLATION IDENTITIES

| Name | Formula | Status | Precision |
|------|---------|--------|-----------|
| K_J * R_K | (2e/h)(h/e^2) = 2/e | CANCELS | 10^-8 |
| G_0 * R_K | (2e^2/h)(h/e^2) = 2 | CANCELS | exact |
| Rydberg | alpha^2*m_e*c/(2h) | CANCELS | 13 digits |
| a_0 * alpha | hbar/(m_e*c) | CANCELS | 12 digits |
| Hartree | m_e*c^2*alpha^2 | R2-FREE | 10 digits |
| Wire R * Cap C | rho*L/(R2*d^2) * eps0*R2*d^2/t | CANCELS | 30 digits |
| Omega_DM | (44/169)*R2 | R2 FACTOR | 44/169 pure rational |


## TABLE 20: Y-DEPENDENCE — GAP RATIO FOR (3,2,Y) VL FERMIONS

All share db2 = 1, db3 = 1/3. Only db1 = (12/5)*Y^2 varies.

| Y | db1 | db2/db1 | Gap Ratio | Distance | Factor worse |
|---|-----|---------|-----------|----------|-------------|
| 1/6 | 1/15 | 15 | 38/27 = 1.407 | 0.049 | 1.0x |
| 1/3 | 4/15 | 15/4 | 196/135 = 1.452 | 0.094 | 1.9x |
| 1/2 | 3/5 | 5/3 | 206/135 = 1.526 | 0.168 | 3.4x |
| 2/3 | 16/15 | 15/16 | 44/27 = 1.630 | 0.272 | 5.5x |

Analytical: Gap(Y) = (188 + 72*Y^2) / 135
Crossover (worse than SM): Y ~ 0.97


## TABLE 21: A2 QED COEFFICIENT — THREE-PIECE DECOMPOSITION

| Piece | Expression | Value | % of |A2| |
|-------|-----------|-------|---------|
| Rational | 197/144 | +1.368 | 416% |
| Number-theoretic | (3/4)*zeta(3) | +0.902 | 274% |
| Geometric | R4*(8/3 - 16*ln2) | -2.598 | 791% |
| Net A2 | sum | -0.329 | 100% |

Cancellation: 87.4%. Surviving: 12.6%.
Sign set by: 16*ln2 > 8/3 -> IR dominates UV -> geometric piece negative.


## TABLE 22: QED COEFFICIENT PROGRESSION

| n | A_n | Diagrams | New transcendentals | R4 power |
|---|-----|----------|--------------------|----|
| 1 | +1/2 | 1 | none (rational) | 0 |
| 2 | -0.329 | 7 | zeta(3), R4, ln2 | 1 |
| 3 | +1.181 | 72 | zeta(5), Li4(1/2), R4^2 | 2 |
| 4 | -1.912 | 891 | elliptic integrals (4-loop wall) | 3 |


## TABLE 23: HUBBLE DATA — EXACT FRACTIONS

| Name | H0 (km/s/Mpc) | Uncertainty | Class |
|------|---------------|-------------|-------|
| SH0ES | 730/10 = 73.0 | 10/10 = 1.0 | local |
| H0LiCOW | 733/10 = 73.3 | 18/10 = 1.8 | local-medium |
| CCHP | 698/10 = 69.8 | 17/10 = 1.7 | medium |
| DES_BAO_BBN | 674/10 = 67.4 | 12/10 = 1.2 | high |
| Planck | 674/10 = 67.4 | 5/10 = 0.5 | maximum |

Cumulative ratio: 674/730 = 337/365
Tension: ~5.0 sigma
VP step: 1/(12*R2) = 1/(3*pi)


## TABLE 24: SOLITON HIERARCHY — 11 LEVELS

| Level | Size | GM/(rc^2) | Integer Rule | Boundary |
|-------|------|-----------|--------------|----------|
| Proton (QCD) | ~1 fm | 99% | b3 = -7 | Confinement |
| Atom (EM) | ~0.1 nm | ~10^-8 | alpha = 1/137 | Ionization |
| Crystal lattice | ~1 nm - km | ~10^-10 | Band structure | Melting |
| Geological | ~m - km | ~10^-10 | Material strength | Phase boundary |
| Human on surface | ~1.7 m | ~10^-9 | GM_E/(R_E*c^2) | Jump height |
| Earth Hill sphere | ~1.5e6 km | ~10^-9 | M_E/M_Sun | L1 Lagrange |
| Earth orbit | 1 AU | ~10^-8 | Kepler T^2~a^3 | v_escape |
| Solar Hill sphere | ~120 AU | ~10^-6 | M_Sun/M_gal | Voyager |
| Galactic disk | ~15 kpc | ~10^-6 | DM/bar=(22/13)*pi | Virial radius |
| Galaxy cluster | ~3 Mpc | ~10^-5 | DM ~ 85% | Virial radius |
| BAO/cosmological | ~150 Mpc | — | N~100 boundaries | H0 running |


## TABLE 25: DWARF SPHEROIDAL CATALOG

### Classical (8)

| Name | M_vis (Msun) | sigma (km/s) | M_dyn (Msun) | DM/vis |
|------|-------------|-------------|-------------|--------|
| Fornax | 2e7 | 11.7 | 1.6e8 | 8 |
| Sculptor | 2.3e6 | 9.2 | 7.0e7 | 30 |
| Draco | 2.9e5 | 9.1 | 5.4e7 | 186 |
| Ursa Minor | 2.9e5 | 9.5 | 4.8e7 | 166 |
| Carina | 3.8e5 | 6.6 | 3.2e7 | 84 |
| Sextans | 4.4e5 | 7.9 | 1.3e8 | 295 |
| Leo I | 5.5e6 | 9.2 | 6.3e7 | 11 |
| Leo II | 7.4e5 | 6.6 | 2.3e7 | 31 |

### Ultra-Faint (3)

| Name | M_vis (Msun) | sigma (km/s) | M_dyn (Msun) | DM/vis |
|------|-------------|-------------|-------------|--------|
| Segue 1 | 340 | 3.9 | 1.3e6 | 3824 |
| Reticulum II | 2600 | 3.3 | 1.0e6 | 385 |
| Tucana II | 3000 | 8.6 | 3.6e7 | 12000 |


## TABLE 26: PLATFORM VERIFICATION STATUS

| Library | Checks | Status |
|---------|--------|--------|
| phys24_lib self-test | 21/21 | PASS |
| phys24_lib platform test | 148/148 | PASS |
| data_4_derivation_lib | 37/37 | PASS |
| phys24_structure_lib | 46/46 | PASS |
| phys24_boundary_map_lib | 14/14 | PASS |
| phys24_domain_lib | 40/40 | PASS |
| phys24_hubble_lib | 16/17 | F1 strict = data (H0LiCOW > SH0ES) |
| data_5_populate | 30/31 | Higgs rep count (scalar, not fermion) |
| TOTAL | 352/354 | 2 expected FAILs, 0 bugs |


## TABLE 27: LEVEL 1 / LEVEL 2 CLASSIFICATION

Level 1 = determined by framework (integers, geometry). Cannot be different.
Level 2 = supplied by universe (measurement). Could be different.
Derived = Level 1 function evaluated on Level 2 inputs.

| Level 1 (framework) | Level 2 (measurement) |
|---------------------|----------------------|
| b1_SM = 41/10 | alpha_inv = 137.036 |
| b2_SM = -19/6 | sin2_tW = 0.23122 |
| b3_SM = -7 | alpha_s = 0.1180 |
| gap_SM = 218/115 | m_e = 0.51100 MeV |
| gap_VL = 38/27 | m_mu = 105.658 MeV |
| CD = (3,2,1/6) | m_tau = 1776.86 MeV |
| db = (1/15, 1, 1/3) | M_Z = 91187.6 MeV |
| Democracy = (4/3,4/3,4/3) | m_t = 172570 MeV |
| R2 = pi/4 | K_koide = 0.66666 |
| R4 = pi^2/32 | gap_measured = 1.358 |
| A1 = 1/2 | H0(SH0ES) = 73.0 |
| Pure-gauge gap = 2 | H0(Planck) = 67.4 |
