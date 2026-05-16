# VDR NOTEBOOK: Q335 REMAINDER NESTING + FUNCTIONAL COMPOSITIONS — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → q335_multiplication → q335_division → denom_growth → complex → fft → slerp → modular → gym_entries → builtins → dependencies → relationships → section_index → decode_legend

# principles(id|principle|detail)
P1|Remainder nesting preserves frame|p₁·p₂ = q·D + s → [q, D, [s, D, 0]]; denominator stays D=2³³⁵; remainder carries exact overflow; zero information lost
P2|Depth replaces denominator growth|where flat Fraction grows denominators (potentially D^(2^n)), Q335 nesting grows tree depth; same information, manageable structure: prunable, lazily evaluable, bounded by precision policy
P3|Complex as VDR pairs|z = (A, B) where A=Re, B=Im, both VDR triples; not a new type, a convention; arithmetic is 4 real multiplies + 2 add/subs
P4|Functional remainders bridge exact↔Q335|fn remainder computes exact rational at each depth; Q335 projection captures as integer; two mechanisms compose: compute then capture
P5|Modular structure IS remainder structure|CRT residues, RNS channels, VDR remainder children at coprime denominators are the same mathematical object; VDR makes it recursive and first-class
P6|Precision is proportional to depth read|100 digits from top level; 200 from two levels; each Q335 node contributes ~102 digits; depth controls precision without recomputation

# q335_multiplication(id|aspect|detail)
QM1|Frame-preserving multiply|p₁·p₂ = q·D + s → [q, D, [s, D, 0]]; scalar projection Π = (qD+s)/D² = p₁p₂/D²; identical to closed form
QM2|Chain depth|n multiplications → depth ≤ n; denominator always D; squaring [q₁,D,R₁] requires handling cross-terms q₁²·D + 2q₁s₁ + s₁²/D within D-frame
QM3|Precomputed powers preferred|π²·ln(2) cheaper via precomputed p(π²) (one multiply) than from p(π) (three multiplies, deeper tree)

# q335_division(id|aspect|detail)
QD1|Integer division approach|p₁ = q·p₂ + s → [q, 1, [s, p₂, 0]]; rebase to D-frame: [q·D, D, [s, p₂, 0] lifted]; odd denominator p₂ confined to remainder slot
QD2|Frame preservation|top-level stays D; odd factors never infect working frame; VDR native division avoids AA5 compromise when divisor is Q335 constant

# denom_growth(id|aspect|detail)
DG1|Fundamental problem|exact rational arithmetic: every multiply of a/b × c/d produces denominator b·d; after n multiplications potentially D^(2^n)
DG2|VDR response|pick working frame D; overflow → R; denominator fixed, tree grows; transforms "denominators explode" to "trees deepen"
DG3|Logistic map comparison|5 steps at x₀=1/3: flat Fraction denominator 9^(2⁵)=9³² ≈ 10³⁰ digits; Q335 tree: 10 levels × ~102 digits ≈ 1020 digits structured; same exact value, 1000× more compact

# complex_numbers(id|aspect|detail)
CX1|Representation|z = (A, B) where A, B are VDR triples; ordered pair convention on existing types
CX2|Addition|(A₁,B₁) + (A₂,B₂) = (A₁+A₂, B₁+B₂); two VDR additions
CX3|Multiplication|(A₁,B₁)·(A₂,B₂) = (A₁A₂−B₁B₂, A₁B₂+A₂B₁); four VDR multiplies, one sub, one add
CX4|Conjugate|(A,B)* = (A,−B); negate B
CX5|Modulus squared|A² + B²; two multiplies + one add; result is single real VDR
CX6|Inverse|z*/|z|²; conjugate divided by modulus squared

# fft_structure(id|aspect|detail)
FF1|Twiddle factors|ω_N^k = cos(2πk/N) − i·sin(2πk/N); precomputed as Q335 pairs; N=4 exact closed {−1,0,1}; N=8 involves 1/√2 as Q335; general N via Taylor→Q335 projection
FF2|Butterfly|X_even = A + W·B, X_odd = A − W·B; W·B is complex multiply (CX3); per butterfly: 4 Q335 multiplies + 4 add/subs; each multiply nests one remainder level
FF3|Depth bound|N-point FFT has log₂(N) stages; N=1024: 10 stages, depth ≤ 10; denominator always D; entire FFT is integer arithmetic with 10-deep remainder trees
FF4|Precision knob|if 100 digits needed, read top level; full exactness available in tree; float FFT silently accumulates butterfly rounding with no recovery mechanism

# slerp_structure(id|aspect|detail)
SL1|Formula|slerp(q₀,q₁,t) = sin((1−t)θ)/sin(θ)·q₀ + sin(tθ)/sin(θ)·q₁ where θ = arccos(q₀·q₁)
SL2|VDR mechanism|quaternion = four VDR objects; dot product = four multiplies summed; arccos/sin as functional remainders (Taylor, rational coefficients); at any depth all exact rational
SL3|RoPE application|rotary position embeddings: 2D rotations at each dimension pair; angles are rational multiples of base frequency; cos/sin as Q335 projections; exact across all sequence positions, no drift

# modular_connections(id|connection|detail)
MC1|GF(p) operations|already remainder operations; VDR performs natively
MC2|Continued fractions|CF [a₀;a₁,a₂,...] is nested quotient-remainder; specific case of VDR remainder nesting where each denominator frame is CF coefficient
MC3|CRT|reconstructs value from residues mod coprime moduli; VDR composite remainder with children at coprime denominators carries same information; A13 (pairwise distinct) reflects coprimality
MC4|Residue number systems|integers as tuples of residues mod chosen moduli for parallel add/mul; VDR composite remainder at different denominators is same idea lifted to rational arithmetic; same-D children merge (N6)

# gym_entries(id|problem|mechanism|key_result)
G01|π·e in Q335|p(π)·p(e) = q·D + s → [q,D,[s,D,0]]|exact, frame preserved, depth 1
G02|π/e division|p(π) = q·p(e) + s → [q,1,[s,p(e),0]]; rebase to D|odd denominator confined to R
G03|π⁴ from scratch|π·π·π·π tracking depth|depth ≤ 3 after 3 multiplications
G04|A₂ QED coefficient|197/144 + π²/12 + 3ζ(3)/4 − (π²/2)·ln(2)|top-level integer + small structured remainders with odd factors confined to R
G05|Complex multiply with Q335|(π+ei)·(ln2+√2·i)|four G01 operations + two integer add/subs; frame stays D
G06|DFT butterfly with ω₈¹|W=(1/√2)(1−i); exploits common factor|two multiplies instead of four; depth 1
G07|IFFT roundtrip, 4-point|x=[1,2,3,4]; N=4 twiddles all in {−1,0,1}|exact roundtrip, Parseval exact: 120=4·30
G08|2×2 eigenvalues|rational, complex (±i), repeated, irrational (√33)|each case handled: closed, VDR pair, functional remainder
G09|Quaternion rotation 90° around z|q=(1/√2,0,0,1/√2); rotate (1,0,0)|remainder tree must cancel to zero; N7 fires → exact integer result
G10|Slerp at t=1/2|q₀=identity, q₁=180° z-axis; θ=π/2|result (1/√2,0,0,1/√2); sin(π/2)=1 exact closed
G11|RoPE at position 7, d=4|angles 7 and 7/100 radians|cos/sin as Q335 projections; exact across all positions
G12|7¹⁰⁰ mod 13|Fermat little theorem: 7¹² ≡ 1 (mod 13)|VDR [184,1,[9,13,0]]; remainder IS the answer
G13|CRT: x≡2(mod3), x≡3(mod5), x≡2(mod7)|solution x=23 (mod 105)|composite remainder decomposes to children at coprime denominators; A13 holds
G14|Logistic map 5 steps Q335|x₀=1/3, r=4; depth grows 2 per step|depth 10 vs flat denominator 10³⁰ digits; 1000× more compact
G15|Tent map period detection|x₀=1/7; period 3 (cycle 2/7→4/7→6/7)|denominator stays 7; no nesting needed; exact equality detects cycle
G16|Gram-Schmidt complex vectors|v₁=(1+i,2), v₂=(3,1−i)|all exact rational; orthogonality check gives exactly 0
G17|4-point DFT of rational signal|x=(1/3,1/7,1/11,1/13)|all coefficients exact rational; Parseval exact
G18||π+ei|²|p(π)²+p(e)² over D²|frame D with carry arithmetic; depth 1; |z| via Newton functional remainder
G19|Transfer function H(iω)|H(s)=1/(s²+3s+2) at s=i|exact closed (1−3i)/10; at irrational ω: Q335 complex arithmetic
G20|RNS correspondence|1000 mod {7,11,13}|tuple (6,10,12) = three remainder children; parallel add matches VDR same-D merge
G21|√7 as functional remainder|Newton iteration; depth 5→~32 digits|eigenvalue (5+√33)/2: compose fn remainders then freeze to Q335
G22|Twiddle table factory|fn remainder pairs → resolve → freeze to Q335|computed once, stored as integers, used forever
G23|Chained rotations|3 irrational angles composed|fn remainders at same depth; no drift between multiplications
G24|IIR filter y[n]=(1/√2)y[n−1]+x[n]|Q335 coeff multiply chain|(1/√2)²⁰ = 1/1024 exact rational; remainder tree should collapse (N7)
G25|Bayesian update with transcendental prior|P(H)=1/e, P(D|H)=π/4|G01 multiply + G02 divide; posterior exact VDR active object
G26|Horner with functional coefficients|p(x)=πx³−ex²+√2x−ln(3) at x=1/7|resolve coefficients at depth then exact rational Horner
G27|Lazy determinant|det of matrix with √2, π entries|deferred until resolved; Cramer's rule composes
G28|Power series composition|exp(sin(1/5))|nested resolve: sin at depth→exact rational→exp at depth→exact rational→Q335
G29|Convolution Q335 signal×kernel|x=[1/3,1/7,1/11], h=[π/4,√2/2]|G01 per product; depth 1; DFT path gives same exact result
G30|Matrix exponential|diag: Taylor fn remainder; rotation: trig fn remainder|chain 100 rotations still exact at each depth
G31|Logistic map via Q335 frame|each step: G01 multiply, depth +2|5 steps: depth 10, ~1020 digits structured vs 10³⁰ flat
G32|Parseval with mixed types|rational signal + Q335 filter|exact equality after normalization; structural equality of remainder trees
G33|Lazy matrix inverse|deferred adjugate/det via fn remainder|compose with b for lazy solve; depth propagates through
G34|Haar wavelet Q335|/2 via right-shift + 1-bit remainder|perfect reconstruction including remainder structure
G35|4-level fn composition|sin→+1→√→exp at x=1/4|each level exact rational; cubic cost in depth; d=12 sufficient for Q335

# builtins(id|name|inputs|output|mechanism|edge_cases)
B01|sqrt(n)|VDR int n≥0|√n fn remainder|Newton x_{k+1}=(x_k+n/x_k)/2|n=0→[0,1,0]; perfect squares collapse to closed
B02|exp(x)|VDR rational x|eˣ fn remainder|Taylor Σxⁿ/n!|x=0→[1,1,0]; large |x| needs more depth
B03|sin(x)|VDR rational x|sin(x) fn remainder|Taylor odd series|x=0→[0,1,0]
B04|cos(x)|VDR rational x|cos(x) fn remainder|Taylor even series|x=0→[1,1,0]
B05|ln(x)|VDR rational x>0|ln(x) fn remainder|near 1: ln(1+t) series; general: reduce via ln(a·2^k)|x≤0→error; x=1→[0,1,0]
B06|arctan(x)|VDR rational x|arctan(x) fn remainder|Taylor |x|≤1; identity reduction |x|>1|x=0→[0,1,0]; x=1→π/4
B07|arcsin(x)|VDR rational x, |x|≤1|arcsin(x) fn remainder|Taylor with central binomial coefficients|x=0→[0,1,0]; |x|>1→error
B08|arccos(x)|VDR rational x, |x|≤1|π/2−arcsin(x)|composes B11+B07|x=1→[0,1,0]; x=0→π/2
B09|power(base,n)|VDR base, int n|base^n|repeated squaring|base=0,n<0→error; n=0→[1,1,0]
B10|nth_root(x,q)|VDR x>0, int q>0|x^(1/q) fn remainder|generalized Newton|q=1→identity; q=2→B01
B11|const_pi()|none|π fn remainder|Machin-type arctangent identity|—
B12|const_e()|none|e fn remainder|Σ 1/n!|—
B13|zeta(s)|int s≥2|ζ(s) fn remainder|Borwein acceleration (odd s); closed-form (even s)|s=1→error(pole)
B14|polylog(n,x)|int n≥1, VDR |x|≤1|Li_n(x) fn remainder|direct sum Σxᵏ/kⁿ|x=1→ζ(n); x=0→[0,1,0]
B15|elliptic_k(k)|VDR 0≤k²<1|K(k) fn remainder|(π/2)·₂F₁(1/2,1/2;1;k²)|k=0→π/2; k²≥1→error
B16|elliptic_e(k)|VDR 0≤k²<1|E(k) fn remainder|(π/2)·₂F₁(−1/2,1/2;1;k²)|k=0→π/2
B17|hypergeometric_2f1(a,b,c,x)|VDR rationals, |x|<1|₂F₁ fn remainder|term recurrence|c∈{0,−1,...}→error
B18|taylor(coeff_fn,x)|callable+VDR x|Σcoeff_fn(n)·xⁿ fn remainder|general Taylor evaluator|convergence depends on series
B19|compose(f,g)|two FnRemainders|f(g(x)) fn remainder|resolves g at depth, passes to f|type mismatch if g output outside f domain
B20|freeze(fn,depth)|FnRemainder+int|Q335 closed [round(val·D),D,0]|resolve then project|lossy below 100-digit floor by design; one-way
B21|complex_pair(re,im)|two VDR objects|VDR complex pair|convention wrapping|components independently closed/active/functional
B22|complex_mul(z1,z2)|two complex pairs|(a₁a₂−b₁b₂, a₁b₂+a₂b₁)|four real multiplies|both closed→result closed
B23|complex_inv(z)|complex pair z|z*/|z|² as complex pair|conjugate/modulus²|z=0→error
B24|twiddle(k,N)|int k,N|complex pair (cos,−sin)|B04+B03+B11 composed|N=0→error; k=0→(1,0); N=4→closed
B25|dft(signal,N)|list VDR+int N|list of N complex pairs|twiddle multiply+sum|N=1→identity; pad if short
B26|slerp(q0,q1,t)|two unit quaternions+VDR t∈[0,1]|interpolated quaternion|sin/arccos via B03,B08|q0=q1→q0; q0=−q1→undefined
B27|quaternion_mul(q1,q2)|two 4-tuples VDR|Hamilton product 4-tuple|16→standard formula|all closed→closed output
B28|mod(a,m)|VDR ints a, m>0|[0,1,[r,m,0]] carrying quotient+remainder|integer division|m=0→error
B29|crt(residues,moduli)|lists VDR ints, coprime|composite remainder children at each modulus|CRT reconstruction|non-coprime→error
B30|logistic_step(x,r)|Q335 x, VDR r|r·x·(1−x) in Q335 frame|G01 multiply, depth +2|x outside [0,1]→valid but may escape
B31|iterate(step_fn,x0,n)|callable+VDR+int|n-fold application in Q335 frame|remainder nesting per step|n=0→x0
B32|detect_period(step_fn,x0,max)|callable+VDR+int|period length or 0|Floyd/Brent on exact VDR equality|aperiodic within max→0
B33|horner(coeffs,x)|list VDR+VDR x|polynomial evaluation|Horner's method, exact|empty→[0,1,0]
B34|haar_forward(signal)|list VDR, len=2^k|wavelet coefficients|avg via add+shift, diff via sub+shift|len≠2^k→error
B35|haar_inverse(coeffs)|list VDR|reconstructed signal|exact inverse of B34|perfect reconstruction
B36|convolve(x,h)|two lists VDR|list len(x)+len(h)−1|direct summation of products|either empty→empty
B37|mat_fn(entry_fn,r,c)|callable+ints|lazy matrix|entries computed on resolve; supports det/inv/mul|r,c≤0→error
B38|transfer_fn(num,den,s)|VDR lists+complex pair|H(s)=N(s)/D(s) complex pair|B33 eval+B23 divide|D(s)=0→error(pole)
B39|borwein_eta(s,n)|int s≥2, int n|η(s) exact rational|weighted sum with rational d_k; error 3^(−n)|s=1→slow convergence
B40|resolve_to_depth(fn,d)|FnRemainder+int|concrete VDR|evaluates fn(depth)|d<0→error

# builtin_dependencies(id|builtin|depends_on)
BD1|B08(arccos)|B11(const_pi), B07(arcsin)
BD2|B13(zeta)|B39(borwein_eta), B11(const_pi) for even s
BD3|B15(elliptic_k)|B17(hypergeometric_2f1), B11(const_pi)
BD4|B16(elliptic_e)|B17(hypergeometric_2f1), B11(const_pi)
BD5|B14(polylog)|B13(zeta) at x=1
BD6|B24(twiddle)|B04(cos), B03(sin), B11(const_pi)
BD7|B25(dft)|B24(twiddle), B22(complex_mul)
BD8|B26(slerp)|B03(sin), B08(arccos), B27(quaternion_mul)
BD9|B38(transfer_fn)|B33(horner), B23(complex_inv)
BD10|B19(compose)|B40(resolve_to_depth)
BD11|B20(freeze)|B40(resolve_to_depth)
BD12|B32(detect_period)|B31(iterate)
# Leaf builtins (no dependencies): B01-B05, B09, B28 — depend only on VDR core arithmetic

# relationships(from|rel|to)
P1|enables|QM1,QD1,DG2
P2|transforms|DG1
P3|defines|CX1-CX6
P4|bridges|B01-B18(fn remainders) and QM1(Q335 frame)
P5|unifies|MC1-MC4
P6|enables|FF4
QM1|used_in|G01,G05,G06,G29
QD1|used_in|G02,G04
DG2|demonstrated_by|G14,G31
CX3|used_in|FF2,G05,G06
FF1|prereq_of|FF2
FF2|composes_into|FF3
FF3|bounded_by|P6
SL1|uses|CX1,B03,B08
SL3|applies|SL1(to LLM position embeddings)
MC2|instance_of|P1(nested quotient-remainder = VDR tree)
MC3|reflected_by|A13(pairwise distinct denominators)
MC4|reflected_by|N6(same-D children merge)
G07|verifies|FF3(exact roundtrip)
G09|tests|N7(closed-form preference fires when remainder cancels)
G15|confirms|P2(periodic orbits free; no nesting needed)
G24|tests|N7(irrational^integer_power → rational should collapse)
G31|demonstrates|DG3(1000× compression vs flat Fraction)
G32|verifies|FF4(DFT convolution = direct convolution exactly)
B20|composes|B40+QM1(resolve then project)
B19|chains|B40(nested resolve at same depth)

# section_index(section|title|ids)
1|Q335 Multiplication Problem|P1,QM1-QM3
2|Q335 Division|QD1-QD2
3|Denominator Growth|P2,DG1-DG3
4|Complex Numbers as VDR Pairs|P3,CX1-CX6
5|Roots of Unity and Twiddle Tables|FF1
6|FFT as Integer Butterflies|FF2-FF4
7|Slerp via Functional Remainders|SL1-SL3
8|Modular Structure|P5,MC1-MC4
9|What This Solves|P1-P6(synthesis)
gym_part1|G01-G20|G01-G20
gym_part2|G21-G35|G21-G35
builtins|B01-B40|B01-B40
dependencies|Builtin Dependency Graph|BD1-BD12

# decode_legend
id_prefixes: P=principle, QM=q335_multiplication, QD=q335_division, DG=denom_growth, CX=complex, FF=fft, SL=slerp, MC=modular_connection, G=gym_entry, B=builtin, BD=builtin_dependency
D: 2³³⁵ throughout (shared Q335 denominator)
frame_preservation: top-level denominator stays D; overflow nests into remainder slot
depth: number of remainder nesting levels; cost currency replacing denominator growth
fn_remainder: callable f(depth)→VDR producing exact rational at each depth; deferred computation
freeze: resolve fn remainder then project to Q335 via round(val·D); one-way, lossy below 100-digit floor
rel_types: enables|transforms|defines|bridges|unifies|used_in|demonstrated_by|composes_into|bounded_by|uses|applies|instance_of|reflected_by|verifies|tests|confirms|demonstrates|composes|chains|prereq_of
VDR_axioms_referenced: A13(pairwise distinct denominators), N6(same-D merge), N7(closed-form preference), AA3(active multiply), AA5(divisor projection compromise)
gym_count: 35 entries (G01-G35)
builtin_count: 40 functions (B01-B40)
all_builtins_pure: yes; all are factories returning FnRemainder or performing exact integer/rational operations
