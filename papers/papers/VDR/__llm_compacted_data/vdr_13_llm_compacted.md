# VDR-13 PHYSICAL COMPUTATION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → domains → qed → quantum → signal → control → orbital → structural → thermo → crystal → geodesy → optics → gym → float_failures → conservation → convergence → gauss_scaling → denom_comparison → relationships → section_index → decode_legend

# principles(id|principle|detail)
P1|Zero drift|any computation returning to starting point (closed orbits, periodic signals, reversible transforms, group closure) returns exactly
P2|Condition number irrelevance|ill-conditioned systems solved with same arithmetic as well-conditioned; condition number affects float not exact arithmetic
P3|Exact conservation laws|energy, probability, symplecticity, unitarity verified by exact equality not residual tolerance
P4|Reproducibility|same VDR computation on any platform produces identical results; no compiler/FPU/rounding dependence
P5|Honest precision|Q335 has 100 digits and says so; deeper precision via Remainder tree; precision loss (freeze/projection) explicit and quantified
P6|VDR changes arithmetic not physics|does not derive new results; shows routine physical computations produce exact results in VDR

# domains(id|domain|exact|practical_size|advantage|mechanism)
D1|QED coefficients|yes|any loop order with known analytical form|eliminates accumulation in multi-term sums|Q335 add+multiply
D2|Quantum 2×2|yes|unlimited operations|exact unitarity, probability|complex pairs
D3|Quantum n×n|yes|n≤50 with Gaussian|exact eigenvalues, exact evolution|Gaussian+complex
D4|DFT/FFT|yes|N≤2¹⁰ comfortably|exact roundtrip, Parseval, no butterfly rounding|Q335 twiddle+nesting
D5|IIR filters|yes|unlimited steps|drift-free; rational powers collapse|Q335 multiply chain
D6|Transfer functions|yes|any order|exact frequency response|complex Horner
D7|State-space|yes|unlimited steps, n≤50 states|zero drift, exact rank|Gaussian+matrix multiply
D8|Kepler orbits|yes|unlimited orbits|zero closure error|functional remainder Newton
D9|Structural statics|yes|n≤50 DOF|exact equilibrium, no refinement|Gaussian solve
D10|Partition functions|yes|2ⁿ states, n≤20|exact Z, F, S|functional remainder exp/ln
D11|Crystallography|yes|any symmetry group|exact group closure|rational/Q335 matrix multiply
D12|Geodesy|yes|any transform chain|exact roundtrip|rational matrix multiply
D13|Paraxial optics|yes|unlimited elements|exact symplecticity|2×2 matrix power
D14|Resonator stability|yes|any cavity|exact stability boundary|rational comparison

# qed(id|aspect|detail)
QE1|Quantity|a_e=(g−2)/2; perturbation series A₁(α/π)+A₂(α/π)²+A₃(α/π)³+...; each Aₙ from Feynman diagrams at n-loop
QE2|A₂ formula|197/144 + π²/12 + 3ζ(3)/4 − (π²/2)·ln(2); all Q335 basis constants; odd factors confined to R via Q335 division
QE3|A₂ computation|each term: rational coefficient × Q335 integer; divmod for odd denominators; Q335 multiply for π²·ln(2); result matches −0.328478965579... to 100 digits
QE4|A₃|involves ζ(5) and weight-5 products; all in Q335 basis or Borwein; structurally identical to A₂
QE5|A₄ (4-loop wall)|6 master integrals known only numerically to 4800 digits; representable as VDR [p, 10⁴⁸⁰⁰, 0]; analytical forms (if found) involve elliptic integrals computable via hypergeometric
QE6|Fine-structure constant|α measured not computed; Q335 at 100 digits; uncertainty as separate VDR interval; series evaluation exact on exact inputs

# quantum(id|aspect|detail)
QM1|Pauli matrices|σ_x,σ_y,σ_z: 2×2 with entries from {0,±1,±i}; all exact VDR closed or complex pairs
QM2|Pauli algebra|σ_x²=σ_y²=σ_z²=I and σ_x·σ_y=iσ_z verified as structural identity not approximate equality
QM3|Spin rotation|U=cos(θ/2)I−i·sin(θ/2)(n̂·σ⃗); for rational θ=pπ/q, trig as functional remainders→Q335; U†U=I exact
QM4|Rotation periodicity|U(π/2 about z) applied four times returns to initial state exactly; float gives I±~10⁻¹⁵
QM5|Measurement probabilities||a|²+|b|²=1 verified exactly; matters for sequential measurements where tiny errors compound
QM6|Hydrogen truncated|n×n Hermitian with rational entries (atomic units); eigenvalues via Gaussian; 2×2 exact closed or √ functional remainder

# signal_processing(id|aspect|detail)
SP1|Exact DFT|rational samples (all digital signals: ADC outputs are integers/2^bits) have exact DFT in VDR; every frequency bin exact complex value
SP2|DFT roundtrip|IDFT(DFT(x))=x exactly; Parseval Σ|x[n]|²=(1/N)Σ|X[k]|² exactly
SP3|IIR filter chains|y[n]=a·y[n−1]+x[n] with Q335 coefficient; each step nests one R level; (1/√2)²⁰=1/1024 collapses via N7
SP4|Convolution identity|direct convolution = DFT convolution exactly; float can only approximate this

# control(id|aspect|detail)
CT1|Transfer function|H(s)=N(s)/D(s) evaluated at s=iω exactly; H(i)=(1−3i)/10 for 1/(s²+3s+2) as exact closed
CT2|State-space evolution|x[n+1]=Ax[n]+Bu[n] with rational A,B,u; exact after 100+ steps; no drift, no Kalman filter needed
CT3|Controllability/observability|rank via Gaussian gives exact rank; no numerical rank thresholding, no SVD tolerance
CT4|Cayley-Hamilton|A²+bA+cI=0 verified as exact zero matrix; float gives ~10⁻¹⁵ per entry

# orbital(id|aspect|detail)
OR1|Kepler equation|M=E−e·sin(E); Newton iteration as functional remainder; 20 steps gives ~100 digits; verify residual at working precision
OR2|Orbit closure|two-body propagation with exact arithmetic; orbit closes exactly after one period
OR3|Patched conics|each conic segment exact; patch point matching with exact comparison; no tolerance/residual management

# structural(id|aspect|detail)
ST1|Direct stiffness method|assemble K, solve Ku=F via Gaussian; rational entries in consistent units; displacements and stresses exact
ST2|Equilibrium verification|K@u==F as exact structural equality; no iterative refinement
ST3|Ill-conditioned structures|vastly different stiffnesses produce ill-conditioned K; VDR solves exactly regardless; condition number irrelevant

# thermodynamics(id|aspect|detail)
TH1|Discrete partition function|Z=Σexp(−βEᵢ); each exp as functional remainder (Taylor); Z exact at each depth; F,S,C via exact discrete calculus
TH2|Ising small lattices|1D: transfer matrix method, 2×2 matrix power exact; small 2D (4×4, 5×5): exact enumeration of all 2ⁿ² states; no Monte Carlo, no sign problems

# crystallography(id|aspect|detail)
CR1|Point group operations|3×3 matrices with entries from {0,±1} (cubic) or {1/2,√3/2} (hexagonal); composition exact; group closure verified by exact comparison
CR2|Structure factor|F(hkl)=Σfⱼexp(2πi(hxⱼ+kyⱼ+lzⱼ)); complex exponentials of rational arguments as VDR complex pairs; |F|² exact

# geodesy(id|aspect|detail)
GE1|Helmert transformation|7-parameter (3 translations, 3 rotations, 1 scale); forward then inverse recovers original coordinates identically; zero residual
GE2|Vincenty formula|geodesic on ellipsoid via iterative convergence; each iteration functional remainder; terminates by exact equality not tolerance
GE3|Coordinate precision|Q335 resolution = 10⁶⁶ × below Planck length

# optics(id|aspect|detail)
OP1|ABCD matrices|2×2 with rational entries; system matrix = product of element matrices, exact; det(M)=1 (symplecticity) exact
OP2|Matrix powers|M¹⁰⁰⁰ via repeated squaring (10 multiplies); exact; float accumulates 1000 butterfly-equivalent roundings
OP3|Resonator stability||A+D|/2<1 as exact rational comparison; no borderline float ambiguity

# gym_exercises(id|exercise|verification)
PH01|A₂ QED coefficient via Q335|verify against known value to 100 digits
PH02|Pauli algebra identities|σ_x²=I, σ_x·σ_y=iσ_z; exact structural equality
PH03|Spin rotation π/2 about z, ×4|returns to initial state exactly
PH04|Measurement probabilities after unitary|sum to exactly 1
PH05|8-point DFT exact roundtrip|Parseval exact
PH06|IIR (1/√2)²⁰ collapses to 1/1024|N7 fires
PH07|Direct convolution = DFT convolution|exact equality
PH08|H(i)=(1−3i)/10 for 1/(s²+3s+2)|exact closed
PH09|100-step state-space Ax+Bu|exact at every step
PH10|Cayley-Hamilton A²+bA+cI=0|exact zero matrix
PH11|Kepler Newton 20 steps|verify M=E−e·sin(E)
PH12|Truss Ku=F exact solve|K@u==F verified
PH13|ABCD product det=1|symplecticity exact
PH14|Helmert forward-inverse roundtrip|exact coordinate recovery
PH15|Two-level partition function Z,F,S|exact discrete calculus

# float_failures(id|domain|computation|float64_error|vdr_error)
FF1|Linear algebra|H₅ inverse residual|~10⁻⁹|0
FF2|Linear algebra|H₁₀ inverse residual|catastrophic (~10⁻²)|0
FF3|Signal processing|200-op return-to-origin|2.78×10⁻¹⁶|0
FF4|Signal processing|IIR (1/√2)²⁰|~10⁻¹⁶|0 (exact 1/1024)
FF5|Quantum|U⁴=I for π/2 rotation|~10⁻¹⁵ per entry|0
FF6|Probability|Binomial PMF sum n=10|~2×10⁻¹⁶|0 (exact 1)
FF7|Orbital|Kepler orbit closure|~10⁻¹² position|0
FF8|Control|Cayley-Hamilton residual|~10⁻¹⁵ per entry|0
FF9|Optics|det(M) after 1000 elements|~10⁻¹²|0 (exact 1)
FF10|Geodesy|Helmert roundtrip|~1 nm|0
FF11|Chaos|Tent map 1/7, 25 steps|diverged (total loss)|0 (period 3 forever)
FF12|Chaos|Logistic map r=4, 15 steps|noise (total loss)|0 (exact rational)

# conservation_laws(id|law|system|float_verify|vdr_verify)
CV1|Probability=1|quantum ⟨ψ|ψ⟩|1.0±~10⁻¹⁵|1 exactly
CV2|Unitarity U†U=I|time evolution|I±~10⁻¹⁵|I exactly
CV3|Symplecticity det(M)=1|paraxial optics|1.0±~10⁻¹² after 1000|1 exactly
CV4|Energy conservation|Hamiltonian evolution|E±~10⁻¹² per step|E exactly
CV5|Parseval energy|DFT/IDFT|equal±~10⁻¹⁴|equal exactly
CV6|Equilibrium Ku=F|structural statics|residual~10⁻¹⁰|residual=0
CV7|Group closure|crystallographic symmetry|within tolerance|structural equality
CV8|Orbit closure|Kepler 2-body|position~10⁻¹²|position=0
CV9|Partition function ratio|thermodynamic identity|ratio±~10⁻¹⁴|ratio exact
CV10|Coordinate roundtrip|Helmert|~1 nm|0

# convergence_rates(id|function|series|convergence|depth_100dig_x_half|depth_100dig_x_1|notes)
FN1|exp(x)|Σxⁿ/n!|super-geometric|~35|~45|fastest builtin
FN2|sin(x)|odd Taylor|super-geometric|~35|~45|same as exp
FN3|cos(x)|even Taylor|super-geometric|~35|~45|same as exp
FN4|ln(1+x)|Σ(−1)ⁿ⁺¹xⁿ/n|geometric ratio x|~340 at x=1|~340|slow near x=1; reduce via ln(a·2ᵏ)
FN5|arctan(x)|odd Taylor|geometric ratio x²|~170|Borwein needed|Machin identity preferred for π
FN6|arcsin(x)|central binomial|geometric ratio x²|~170|diverges|requires |x|<1
FN7|√n Newton|quadratic|digits double/step|~8|~8|1,3,6,12,24,48,>100 digits
FN8|₂F₁(1/2,1/2;1;k²)|hypergeometric|geometric ratio k²|~170 at k²=1/4|N/A (k²<1)|for elliptic K(k)
FN9|ζ(s) Borwein|accelerated eta|3⁻ⁿ|210 for any s|210|universal rate
FN10|Kepler Newton|quadratic|digits double/step|~8|~8|same as √n

# gauss_vs_cofactor(id|size|gauss_det|cofactor_det|gauss_inv|gauss_solve)
GS1|3×3|17|15|39|26
GS2|4×4|40|64|88|56
GS3|5×5|75|325|155|100
GS4|10×10|550|~3.6×10⁶|1100|700
GS5|20×20|4200|~2.4×10¹⁸|8400|5400
GS6|30×30|13950|impossible|27900|18000
GS7|50×50|63750|impossible|127500|82500
# Cofactor impractical at n=10, impossible at n=20. Gaussian handles n=50 routinely.

# hilbert_pivot_growth(id|matrix|max_pivot_num_digits|max_pivot_den_digits|det_den_approx|float_det_error)
HB1|H₃|3|3|2160|~10⁻¹⁶
HB2|H₄|5|7|6048000|~10⁻¹³
HB3|H₅|8|11|~2.7×10¹⁰|~10⁻⁹
HB4|H₆|11|16|~1.9×10¹⁵|~10⁻⁴
HB5|H₈|18|27|~3.6×10²⁶|~10⁴ (wrong sign possible)
HB6|H₁₀|26|40|~4.6×10⁴¹|meaningless
HB7|H₂₀|70|110|~10¹⁷⁰|impossible
HB8|H₃₀|120|185|~10⁴⁰⁰|impossible
# Hilbert determinant numerator always 1. VDR computes H₃₀ routinely.

# denom_comparison_logistic(id|step|flat_denom_digits|q335_tree_digits|compression)
DC1|0|1|102|0.01× (Q335 larger)
DC2|5|31|1020|0.03×
DC3|10|~980|2040|0.5×
DC4|15|~31000|3060|10×
DC5|20|~990000|4080|243×
DC6|25|~31000000|5100|6078×
DC7|30|~10⁹|6120|~163000×
# Crossover at ~step 10. Below: flat more compact. Above: Q335 exponentially better.

# transcendental_weights(id|weight|constants|physical_origin|first_appearance|vdr_mechanism)
TW1|0|rationals (197/144 etc.)|combinatorial factors from diagram counting|1-loop A₁|closed arithmetic
TW2|1|π, ln(2)|Dirac traces, angular integrals, threshold integrals|2-loop A₂|Q335 basis
TW3|2|π², ζ(2)|two-fold nested parameter integrals|2-loop A₂|Q335 basis
TW4|3|ζ(3)|three-fold nested 1/n-type denominators|2-loop A₂|Q335 basis
TW5|4|Li₄(1/2)|four-fold nested integrals with half-range boundary|3-loop A₃|Q335 basis
TW6|5|ζ(5), π²ζ(3)|five-fold nesting; products of lower-weight|3-loop A₃|Borwein n=210; Q335 multiply
TW7|6|K(k), E(k) at rational k|elliptic curve periods from sunrise topology|4-loop A₄|hypergeometric ₂F₁
TW8|7|ζ(7), products to weight 7|expected maximal weight at 4-loop|4-loop A₄|Borwein n=210

# q335_operation_costs(id|operation|int_ops|depth_change|precision_impact|example)
OC1|Add two Q335|1 add|0|±1 ULP|π+e
OC2|Subtract two Q335|1 sub|0|±1 ULP|π−e
OC3|Multiply by integer k|1 mul|0|exact|3·ζ(3)
OC4|Multiply by 1/2ᵐ|1 shift|0|exact|π/2
OC5|Multiply two Q335|1 mul+1 divmod|+1|zero (overflow in R)|π·e
OC6|Divide by integer k|1 divmod|+1 if remainder|odd factor in R|π²/12
OC7|Divide two Q335|1 divmod|+1|odd denominator in R|π/e
OC8|Chain n multiplies|n mul+n divmod|≤n|zero (each level exact)|π⁴: depth≤3
OC9|Freeze fn remainder|resolve+1 divmod|resets to 0|lossy below 100-digit floor|freeze(sin(1/7),50)
OC10|Complex multiply|4 mul+1 add+1 sub|+1 per multiply|same as real multiply|(π+ei)·(ln2+√2i)
OC11|FFT butterfly|4 mul+4 add/sub|+1|per stage|N=1024: depth≤10

# relationships(from|rel|to)
P1|demonstrated_by|QM4,OR2,SP2,GE1,OP2,PH03,PH14
P2|demonstrated_by|ST3,HB1-HB8,FF2
P3|demonstrated_by|CV1-CV10
P4|demonstrated_by|FF1-FF12
P5|demonstrated_by|OC1-OC11,DC1-DC7
P6|governs|D1-D14
QE2|uses|OC1,OC5,OC6
QE5|requires|TW7(elliptic integrals)
QM3|uses|FN2,FN3(trig functional remainders)
SP1|enables|SP2,SP4
SP3|demonstrates|P1(N7 collapse)
CT2|demonstrates|P1(zero drift)
OR1|uses|FN2,FN3,FN10
ST1|uses|GS1-GS7(Gaussian)
TH1|uses|FN1(exp),FN4(ln)(functional remainders)
CR1|uses|OC5(Q335 matrix multiply)
OP1|demonstrates|P3(symplecticity)
TW1-TW8|maps|QE1-QE5(weight→loop order)
FF1-FF12|contrasts|CV1-CV10(float failure vs exact conservation)
GS1-GS7|enables|D3,D7,D9(n×n capability)
HB1-HB8|demonstrates|P2(float fails, VDR succeeds)
DC1-DC7|demonstrates|P5(tree depth vs denominator explosion)

# section_index(section|title|ids)
1|What This Paper Is|P6
2|QED Electron g−2|QE1-QE6,TW1-TW8
3|Quantum Mechanics|QM1-QM6
4|Signal Processing|SP1-SP4
5|Control Systems|CT1-CT4
6|Orbital Mechanics|OR1-OR3
7|Structural Mechanics|ST1-ST3
8|Thermodynamics|TH1-TH2
9|Crystallography|CR1-CR2
10|Geodesy and Navigation|GE1-GE3
11|Optics|OP1-OP3
12|What VDR Provides|P1-P5
AppA|Physical Constants in Q335|QE6
AppB|Gym Exercises|PH01-PH15
AppC|Transcendental Weights|TW1-TW8
AppD|Q335 Operation Costs|OC1-OC11
AppE|Float Failure Points|FF1-FF12
AppF|Convergence Rates|FN1-FN10
AppG|Gaussian Scaling|GS1-GS7
AppH|Complex Identities Verified|QM1-QM2,CV1-CV10
AppI|Denominator Comparison|DC1-DC7
AppJ|CRT Correspondence|(structural, refs P5)
AppK|Hilbert Pivot Growth|HB1-HB8
AppL|Quaternion Operations|(structural, refs QM3)
AppM|Conservation Laws|CV1-CV10
AppN|Domain Suitability|D1-D14

# decode_legend
id_prefixes: P=principle, D=domain, QE=qed, QM=quantum, SP=signal_processing, CT=control, OR=orbital, ST=structural, TH=thermodynamics, CR=crystallography, GE=geodesy, OP=optics, PH=gym_exercise, FF=float_failure, CV=conservation_law, FN=convergence_rate, GS=gauss_scaling, HB=hilbert_pivot, DC=denom_comparison, TW=transcendental_weight, OC=operation_cost
rel_types: demonstrated_by|governs|uses|requires|enables|demonstrates|maps|contrasts|enables
vdr_error_column: 0 means exact structural equality (not approximately zero)
float_error: representative float64 values; actual may vary by platform/compiler
practical_size: limited by Gaussian O(n³) for matrix domains; unlimited for scalar/2×2 domains
Q335: D=2³³⁵ shared denominator; 100 decimal digits; ~102-digit integer numerators
depth: remainder nesting levels; cost currency; each level ~102 additional digits of precision
