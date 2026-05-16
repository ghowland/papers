# MATH-3 TRANSCENDENTAL HIERARCHY — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → basis_constants → elliptic → acceleration → hierarchy → pslq → extended_basis → falsification → limitations → relationships → section_index → decode_legend

# principles(id|principle|rationale)
P1|Integer pair = exact Fraction p/q from truncated convergent rational series|truncation error bounded by next term; not floating-point approximation but exact rational differing from true value by known bounded amount
P2|Elliptic integrals are integer pairs|K(k) at rational k = (π/2) × hypergeometric rational series; product of two integer pairs is an integer pair
P3|Borwein acceleration replaces linear convergence with geometric|ζ(5) goes from 10k terms for 20 digits to 210 terms for 100 digits; all rational coefficients; applies to all odd ζ values uniformly
P4|Transcendental hierarchy maps loop order to constant class|maximal weight conjecture: max transcendental weight at L-loop = 2L−1; topology determines transcendental content
P5|Both success and failure of PSLQ identification are contributions|success closes 4-loop basis; failure precisely characterizes new irreducible transcendental constants

# math2_basis(id|constant|series|convergence|digits_at_terms|appears_at)
MB1|π|Machin (arctan)|geometric ~1.4 bits/term|999 at 160 terms|2-loop (as π²)
MB2|ln(2)|2·arctanh(1/3)|geometric ~1.6 bits/term|999 at 160 terms|2-loop
MB3|ζ(3)|central binomial|geometric ~1.0 bit/term|114 at 180 terms|2-loop
MB4|ζ(5)|alternating eta|linear 1/N⁵|20 at 10000 terms|3-loop
MB5|Li₄(1/2)|direct sum 1/(2ⁿn⁴)|geometric ~1 bit/term|100 at 300 terms|3-loop
# These 5 are the constants appearing in QED a_e through 3-loop
# MATH-2 total: 17 constants as integer pairs at 100-999 digits

# constant_origins(id|constant|physical_origin)
CO1|π|Dirac trace and angular integrals
CO2|ln(2)|threshold integrals where virtual particle goes on-shell at halfway point of Feynman parameter range
CO3|ζ(3)|three-fold nested integration of 1/n-type denominators
CO4|ζ(5), Li₄(1/2)|higher-fold nestings at 3-loop

# four_loop_classes(id|class|description|status)
CL1|Harmonic polylogarithms at roots of unity|Li_n(z) at z=e^(iπ/3), e^(2iπ/3), e^(iπ/2); reduce to rational combos of π, ζ, Clausen functions|within MATH-2 framework
CL2|Integrals of products of complete elliptic integrals|∫₀¹ f(x)K(g(x))dx where K is complete elliptic integral first kind; algebraic integrands|requires MATH-3 elliptic extension
CL3|Six finite parts of master integrals (numerical only)|Laporta computed to 4800 digits; cannot express analytically|target for PSLQ identification

# elliptic_integrals(id|constant|series|convergence_ratio|digits_at_500_terms|notes)
EI1|K(1/√2)|π/2 · ₂F₁(1/2,1/2;1;1/2)|k²=1/2|~150|singular value k₁; equals Γ(1/4)²/(4√π)
EI2|K(√3/2)|π/2 · ₂F₁(1/2,1/2;1;3/4)|k²=3/4|~60|equianharmonic lattice period; relates to Γ(1/3)
EI3|K(1/2)|π/2 · ₂F₁(1/2,1/2;1;1/4)|k²=1/4|~300|fastest convergence; no simple gamma relation
EI4|E(1/√2)|π/2 · ₂F₁(-1/2,1/2;1;1/2)|k²=1/2|~150|
EI5|E(√3/2)|π/2 · ₂F₁(-1/2,1/2;1;3/4)|k²=3/4|~60|
EI6|E(1/2)|π/2 · ₂F₁(-1/2,1/2;1;1/4)|k²=1/4|~300|
# K(k) = (π/2) · Σ_{n=0}^N [C(2n,n)]² k^{2n} / 4^n — all rational coefficients
# Recurrence: t_{n+1}/t_n = [(2n+1)/(2n+2)]² × k² — avoids factorial computation
# Truncation error: < (π/2) × t_{N+1} / (1 − k²)
# AGM alternative: quadratic convergence but requires √ at each step (nested series in Fraction); hypergeometric preferred for integer pairs

# borwein_acceleration(id|aspect|detail)
BA1|Method|weighted sum with Chebyshev-like coefficients d_k; achieves geometric convergence 3^(-n) for Dirichlet eta η(s)
BA2|Coefficients|d_k = n · Σ_{i=0}^k (n+i−1)! · 4^i / ((n−i)! · (2i)!); each d_k is finite sum of rational terms; all rational
BA3|Accelerated sum|η(s) ≈ −(1/d_n) · Σ_{k=0}^{n−1} (−1)^k · (d_k − d_n) / (k+1)^s
BA4|Error bound|C · 3^(-n); at n=210: 3^(-210) ≈ 10^(-100.2); 100 correct digits guaranteed for any s
BA5|Operation count|computing d_k for k=0..210 requires ~22000 Fraction ops; accelerated sum requires 210 Fraction divisions; total ~22000 ops on numbers with up to ~500-digit numerators; feasible in minutes
BA6|Universality|applies to ζ(s) for any s with same convergence rate 3^(-n); ζ(7), ζ(9), ζ(11) etc. all at 100 digits with n=210

# accelerated_zeta(id|constant|method|convergence|digits_at_param)
AZ1|ζ(5)|Borwein n=210|3^(-n)|~100 at n=210 (replaces MB4: 10000 terms for 20 digits)
AZ2|ζ(7)|Borwein n=210|3^(-n)|~100 at n=210 (appears in 4-loop mass-dependent terms)
AZ3|ζ(9)|Borwein n=210|3^(-n)|~100 at n=210 (may appear at 5-loop)

# clausen_functions(id|constant|series|convergence|notes)
CF1|Cl₂(π/3)|Σ sin(nπ/3)/n²|linear|reducible to ζ(2) and L-functions
CF2|Cl₃(π/3)|Σ cos(nπ/3)/n³|linear|related to ζ(3) by known identity
CF3|Cl₂(π/2)|Catalan's constant G|Borwein acceleration|~100 digits at n=210

# transcendental_weights(id|constant|weight)
TW1|rational number|0
TW2|π|1
TW3|ln(2)|1
TW4|ζ(n)|n
TW5|Li_n(1/2)|n
TW6|K(k) at rational k|1 (same as π: K = π/2 × rational series)

# hierarchy_by_loop(id|loop_order|max_weight|examples)
HL1|1 (A₁=1/2)|0|rational only
HL2|2 (A₂)|3|ζ(3), π² (weight 2), π²·ln(2) (weight 3)
HL3|3 (A₃)|5|ζ(5), π²·ζ(3) (weight 5)
HL4|4 (A₄)|7 (expected)|ζ(7), products to weight 7, elliptic contributions
HL5|5 (predicted)|9|everything from 4-loop; no new transcendental class expected
HL6|6 (predicted)|11|possible first occurrence beyond elliptic: K3 surfaces or hyperelliptic integrals

# topology_classification(id|topology|transcendental_class|description)
TC1|Factorizable|ζ/ln/Li (MATH-2)|diagram cut into two pieces by cutting single propagator; integral factors into product of lower-loop integrals
TC2|2-loop sunrise (equal mass)|ζ(2), ζ(3)|simplest irreducible self-energy diagram
TC3|3-loop banana|ζ(5), higher weight|double sunrise produces higher-weight constants
TC4|4-loop sunrise (4 propagators)|complete elliptic integrals|topology forces genuinely new transcendental class; periods of elliptic curve from momentum-space geometry
# Factorization boundary: if one cut separates graph → ζ/ln/Li; if no cut exists → elliptic integrals appear

# zeta5_question(id|aspect|detail)
ZQ1|Central binomial series for ζ(5)|whether identity ζ(5) = c · Σ f(k)/[k⁵ C(2k,k)^a] exists with simple rational f(k) is open question
ZQ2|Zudilin (2001)|showed at least one of ζ(5),ζ(7),ζ(9),ζ(11) is irrational; construction related to Apéry but no clean central-binomial form
ZQ3|Practical resolution|Borwein acceleration solves the computational problem; existence of central binomial series remains theoretical question

# pslq_identification(id|aspect|detail)
PQ1|Target|Laporta's 6 finite 4-loop master integrals, each known to 4800 digits
PQ2|Candidate pool|~80 constants organized by weight 0-7: rational, π/ln(2) products, ζ values, Li values, elliptic K/E values, Clausen functions; after removing algebraic dependencies ~50-100 candidates
PQ3|Precision requirement|all candidates to 5000+ digits in Fraction arithmetic (4800 target + 100+ margin)
PQ4|Feasibility|π/ln(2) trivial at high terms; ζ(3)/ζ(5) via Borwein at n≈10500; Li₄(1/2) at 16600 terms; K(k) via hypergeometric; dominated by Fraction arithmetic on 5000-digit numbers; hours per constant
PQ5|Success outcome|A₄ fully analytical; 4-loop a_e computable in Fraction arithmetic; transcendental basis closed through 4-loop; wall falls
PQ6|Failure outcome|resistant integrals define genuinely new transcendental constants; hierarchy has gap; A₄ remains semi-analytical; wall stands but structure precisely characterized
PQ7|Current status|computation NOT performed; method and feasibility established; infrastructure exists in PARI/GP, Mathematica, Sage; deferred to follow-up

# extended_basis_summary(id|category|count|items)
EB1|MATH-2 original|17|π, e, ln(2), ζ(2-5), Li_n(1/2) for small n, etc.
EB2|Elliptic integrals (new)|6|K and E at k²=1/2, 3/4, 1/4
EB3|Accelerated odd zeta (replacing slow versions)|3|ζ(5), ζ(7), ζ(9) via Borwein
EB4|Clausen functions (new)|3|Cl₂(π/3), Cl₃(π/3), Cl₂(π/2)
# Total extended basis: ~29 constants, all computable in Fraction arithmetic to 100+ digits with geometric convergence

# falsification(id|criterion)
F1|Fraction computation of K(k) at rational k must agree with published special values (AGM to thousands of digits) to all computed digits; K(1/√2) must match Γ(1/4)²/(4√π)
F2|Accelerated ζ(5) must agree with known value to 100+ digits; Borwein d_k coefficients must be rational by construction
F3|Stated convergence rates (geometric ratio k² for K(k), 3^(-n) for Borwein) must be verified numerically at multiple term counts
F4|Any PSLQ integer relation must hold to all 4800 available digits; relation holding to 1000 but failing at 2000 is false positive
F5|If transcendental class beyond elliptic (hyperelliptic, K3 periods) demonstrated at 5-loop, hierarchy prediction of HL5 is wrong

# limitations(id|limitation|detail)
LM1|PSLQ not performed|method and extended basis established; computation deferred to follow-up
LM2|Borwein not implemented|companion scripts use direct alternating series (10k terms/20 digits); Borwein implementation (210 terms/100 digits) awaits execution
LM3|Elliptic integrals not computed to high precision|integer pair status established by hypergeometric argument; high-precision Fraction computation awaits execution
LM4|Hierarchy is observational|maximal weight conjecture 2L−1 stated as pattern, not theorem; factorization boundary described qualitatively, not rigorously graph-theoretic
LM5|Topology-transcendental correspondence incomplete|some reducible diagrams produce same constants as irreducible via IBP identities; topology gives upper bound on transcendental content, not exact content

# relationships(from|rel|to)
P1|grounds|EI1-EI6,MB1-MB5,AZ1-AZ3
P2|established_by|EI1-EI6
P3|enables|AZ1-AZ3
P4|governs|HL1-HL6,TC1-TC4
P5|governs|PQ5,PQ6
MB1|used_in|EI1-EI6(as π/2 factor)
MB4|superseded_by|AZ1
CL1|within|MB1-MB5(MATH-2 framework)
CL2|requires|EI1-EI6
CL3|target_of|PQ1-PQ7
EI1-EI6|enables|CL2
AZ1|replaces|MB4
BA1|implements|P3
BA6|enables|AZ1,AZ2,AZ3
TC1|produces|MB1-MB5(ζ/ln/Li family)
TC4|produces|EI1-EI6
HL1|prereq_of|HL2
HL2|prereq_of|HL3
HL3|prereq_of|HL4
HL4|prereq_of|HL5
HL5|prereq_of|HL6
PQ2|draws_from|EB1,EB2,EB3,EB4
PQ3|requires|BA1(for 5000-digit ζ values)
PQ5|validates|P4
PQ6|falsifies_partially|P4
F1|validates|P2,EI1-EI6
F2|validates|P3,AZ1
F5|tests|HL5
ZQ3|resolves_via|BA1
LM1|limits|PQ1-PQ7
LM4|limits|P4

# section_index(section|title|ids)
I|Abstract|(overview only)
II.1|MATH-2 Basis|MB1-MB5,P1
II.2|Five Constants in QED 3-loop|MB1-MB5,CO1-CO4
II.3|The 4-Loop Wall|CL1-CL3
III.1|Hypergeometric Representation|P2,EI1-EI6
III.2|Convergence Rate|EI1-EI6
III.3|E(k) Second Kind|EI4-EI6
III.4|Specific Values for A₄|EI1-EI3
III.5|AGM Alternative|EI1(verification method)
IV.1|ζ(5) Bottleneck|MB4
IV.2|Known Accelerated Series|BA1
IV.3|Borwein Method Detail|BA1-BA5
IV.4|Higher Odd Zeta|BA6,AZ1-AZ3
IV.5|Central Binomial Question|ZQ1-ZQ3
V.1|Loop Order and Weight|TW1-TW6,HL1-HL4
V.2|Topology and Class|TC1-TC4
V.3|Factorization Boundary|TC1,TC4
V.4|5-Loop Prediction|HL5,HL6
VI|PSLQ Identification|PQ1-PQ7
VII|Extended Basis|EB1-EB4
VIII|Falsification|F1-F5
IX|Limitations|LM1-LM5
AppA|Hypergeometric Computation|EI1-EI6(recurrence, truncation error)
AppB|Borwein Acceleration|BA1-BA5(coefficients, error bound, operation count)

# decode_legend
id_prefixes: P=principle, MB=math2_basis, CO=constant_origin, CL=four_loop_class, EI=elliptic_integral, BA=borwein_acceleration, AZ=accelerated_zeta, CF=clausen_function, TW=transcendental_weight, HL=hierarchy_by_loop, TC=topology_classification, ZQ=zeta5_question, PQ=pslq_identification, EB=extended_basis, F=falsification, LM=limitation
rel_types: grounds|established_by|enables|governs|used_in|superseded_by|within|requires|target_of|implements|replaces|produces|prereq_of|draws_from|validates|falsifies_partially|tests|resolves_via|limits
convergence_types: geometric(ratio per term), linear(1/N^s)
integer_pair: exact Fraction p/q from truncated convergent rational series with bounded error
transcendental_weight: rational=0, π=ln(2)=1, ζ(n)=n, Li_n(1/2)=n, K(k)=1
maximal_weight_conjecture: at L-loop, max weight = 2L−1
status: PSLQ not performed; Borwein not implemented; elliptic not computed to high precision; hierarchy observational not proven
