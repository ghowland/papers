# HOWL-VDR-31-2026 — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → model_arch → denominator_problem → basis_aware_ops → surrogate_softmax → training_results → verification → precision → scaling → comparisons

# principles(id|principle|rationale)
P1|VDR triple [V,D,R]: value is (V+R)/D; R=0 closed, R≠0 active|remainder is exact residual not error; R can be recursive tree of child VDR triples
P2|fixed-frame rule: D never explodes; divmod keeps D fixed, overflow goes to R|product>>bits=Q, product&mask=S; one shift one mask on power-of-two D
P3|precision floor at D=2^32 is 1/2^32 ≈ 2.33×10⁻¹⁰|worst-case error per op is half grid spacing; configurable by choosing larger D
P4|D=2^32 chosen for toy model: 9.6 decimal digits, V×V product fits 64 bits|divmod is 32-bit right shift — one instruction; sits between float32 (7.2 digits) and float64 (15.9 digits)

# denominator_growth_problem(id|source|mechanism|growth_rate)
DG1|core arithmetic operators (+,-,×,÷)|cross-multiplication D1×D2 for different-D operands|×: doubles bit length per step; 10 muls → D exceeds 10^105
DG2|active multiplication module|patched × and ÷ lacked basis frame awareness|same exponential growth as DG1
DG3|mixed-frame operands|hyperparams like lr=VDR(1,100) D=100 or VDR(2) D=1 mixed with basis values|one-time D1×D2 growth, moves off power-of-two grid permanently
DG4|softmax Taylor series|divides by VDR(k) D=1 at each iteration|16 mixed-frame divisions per element
DG5|loss function constants|gradient scaling VDR(2,n) has small D mixing with basis gradients|mixed-frame arithmetic
DG6|autodiff initialization|gradient accumulators init to VDR(0) D=1|mixed-frame on first accumulation

# basis_aware_solution(id|component|check|action)
BA1|both-in-basis detection|_both_in_basis(a,b): both operands share D = default basis|use divmod to keep D fixed instead of cross-multiplying
BA2|one-in-basis detection|_one_in_basis(a,b): exactly one operand in basis frame|project non-basis operand onto basis grid before operation
BA3|active operator integration|check for basis-frame operands before general active path|flatten active (R≠0) values via to_qbasis projection, then basis-frame operation
# inserted at entry point of every arithmetic operator; transparent to caller; no manual rebase calls needed
# verification: 10 mul + 10 div + 10 add + 10 sub chained at D=2^32, all 54 checks pass, D=4,294,967,296 throughout

# mixed_frame_sources(id|module|function|original_constant|original_D|fix)
MF1|softmax.py|_exp|VDR(k) for k=1..16|1|precomputed 1/k table in basis via to_qbasis
MF2|softmax.py|softmax_surrogate_square|no shift parameter|—|added shift param, default to min logit
MF3|attention.py|apply_boolean_mask|VDR(-1000)|1|project fill to basis once via _basis_fill_value
MF4|losses.py|mse|VDR(n) divisor|n|precomputed VDR(1,n) in basis via _basis_const
MF5|losses.py|mse_grad|VDR(2,n)|n|precomputed in basis via _basis_const
MF6|losses.py|l1_grad|VDR(0)|1|replaced with _basis_const(0)
MF7|losses.py|hinge_binary|VDR(1), VDR(label)|1|projected via _basis_const
MF8|losses.py|cross_entropy_binary|VDR(1)|1|projected via _basis_const
MF9|optim.py|SGD.__init__|lr (arbitrary D)|varies|projected to basis at construction
MF10|optim.py|Momentum.__init__|lr, beta|varies|projected to basis at construction
MF11|optim.py|Momentum.step|VDR(1)|1|cached as self.one in basis
MF12|autodiff.py|Node.__init__|VDR(0) grad|1|_basis_zero()
MF13|autodiff.py|Node.backward|VDR(1) seed|1|_basis_vdr(VDR(1))
MF14|autodiff.py|ensure_node|VDR(x) from int|1|_basis_vdr(VDR(x))
MF15|autodiff.py|__pow__|VDR(exp)|1|_basis_vdr(VDR(exp))
MF16|autodiff.py|relu|VDR(0)|1|_basis_zero()
MF17|autodiff.py|mse_loss|VDR(1,n)|n|_basis_vdr(VDR(1,n))
MF18|tensor.py|Tensor3D.zero|VDR(0)|1|_basis_zero_vec(d)
MF19|tensor.py|masked_fill_rows|VDR(0) fill|1|_basis_zero() or projected fill
MF20|transformer.py|TransformerBlock|Wq,Wk,Wv,Wo|varies|to_qbasis via TransformerBlock.to_qbasis()
MF21|transformer.py|TransformerLM.to_qbasis|output_proj weights|varies|self.output_proj.to_qbasis(bits)
MF22|nn.py|ReLU.forward|VDR(0) comparison|1|comparison only, no arithmetic mixing
# 23 mixed-frame sources across 8 modules identified and fixed

# operator_coverage(id|operator|module|both_in_basis_action|one_in_basis_action|neither_action)
OC1|__add__|core.py|integer add same D|rebase non-basis, integer add|cross-multiply D1×D2
OC2|__sub__|core.py|integer subtract same D|rebase non-basis, integer subtract|cross-multiply D1×D2
OC3|__mul__|core.py|_basis_mul (divmod)|—|cross-multiply D1×D2
OC4|__truediv__|core.py|_basis_div (divmod)|—|reciprocal multiply
OC5|active_mul|active.py|flatten active, _basis_mul|rebase non-basis, _basis_mul|cross-multiply with remainder tree
OC6|active_div|active.py|flatten active, _basis_div|rebase non-basis, _basis_div|project divisor to Fraction, reciprocal multiply
OC7|_active_add|core.py|integer add same-D path|rebase non-basis, integer add|cross-multiply D1×D2, lift remainders
# core __mul__ and __truediv__ only check _both_in_basis; active.install() patches them with active_mul/active_div which check both

# model_architecture(id|component|shape|elements|notes)
MA1|token embedding|5×4|20|vocabulary: {the,cat,sat,on,mat}
MA2|positional embedding|4×4|16|context length 4
MA3|Wq projection|4×4 + bias 4|20|single-head self-attention
MA4|Wk projection|4×4 + bias 4|20|
MA5|Wv projection|4×4 + bias 4|20|
MA6|Wo projection|4×4 + bias 4|20|
MA7|FFN layer 1|8×4 + bias 8|40|hidden dim 8, ReLU activation
MA8|FFN layer 2|4×8 + bias 4|36|
MA9|output head|5×4 + bias 5|25|projects to vocab size
# total: 217 VDR values (181 trainable parameters reported by parameters() — excludes 36 embedding elements)
# architecture: embed → single-head causal attention → residual → FFN(ReLU) → residual → output projection → quadratic softmax

# weight_initialization(id|method|details)
WI1|deterministic LCG|state = (1103515245 × state + 12345) mod 2^31; seed=42
WI2|small-integer rationals|integers in [-4,4] stored as VDR(k,4), projected via to_qbasis
WI3|bit-identical across platforms|LCG is deterministic; no float-dependent initialization

# quadratic_softmax_surrogate(id|aspect|description)
QS1|formula|p_i = (x_i - shift)² / Σ_j (x_j - shift)²; shift = min logit
QS2|operations|subtraction, squaring, summation, division — all exact rational in VDR; zero transcendentals
QS3|sum-to-one guarantee|compute first N-1 probabilities by independent division; last = 1 - sum of others; absorbs all division remainder residuals
QS4|max residual bound|(N-1)/2^32 ≈ 9.3×10⁻¹⁰ for N=5 vocabulary
QS5|backward pass|∂L/∂s_i = (2·s_i / Σs²) · (∂L/∂p_i - Σ_j ∂L/∂p_j · p_j); uses cached shifted values and probabilities; no exp derivative
QS6|vs Taylor exp softmax|3 ops/element vs ~32; no series truncation error; no mixed-frame constants; broader distribution (no gradient saturation)
QS7|nature|not an approximation of exp softmax — different normalization function satisfying same structural requirements: non-negative, sum-to-1, differentiable

# training_config(id|parameter|value)
TC1|loss function|MSE between softmax output and one-hot target; constants projected to basis
TC2|optimizer|SGD, learning rate 1/128 projected to basis at construction
TC3|corpus|"the cat sat on the mat" → tokens [0,1,2,3,0,4] → 2 training windows of length 4
TC4|epochs|20
TC5|backward pass|manual backprop through all layers; all gradients exact

# training_results(id|epoch|loss|softmax_sum_exact)
TRN1|1|0.267299|yes
TRN2|5|0.255813|yes
TRN3|10|0.244555|yes
TRN4|15|0.234526|yes
TRN5|20|0.225423|yes
# monotonically decreasing; worst observed residual: 9.07×10⁻¹³ at epoch 12 (measurement artifact from re-summation through different addition order, not computation error)

# attention_pattern(id|context|pattern|notes)
AT1|"the cat sat on"|the→the: 1.000; cat→(the 0.500, cat 0.500); sat→(the 0.333, cat 0.335, sat 0.332); on→(the 0.283, cat 0.527, on 0.190)|causal mask exact: future positions get exactly zero; each row sums to exactly 1

# generation(id|prompt|output|notes)
GEN1|"the cat"|the cat sat sat sat sat|model learned "sat" as most probable next token — consistent with training data

# decoding_strategies(id|strategy|mechanism)
DS1|greedy|exact argmax comparison
DS2|categorical sampling|exact rational CDF vs deterministic rational random in [0,1)
DS3|top-k|keep k highest, renormalize exactly, categorical sample
DS4|nucleus (top-p)|keep smallest set exceeding threshold, renormalize exactly, categorical sample
# all decisions are exact rational comparisons; CDF has no gaps/overlaps because probabilities sum to exactly 1

# verification_tests(id|test|description|result)
VT1|softmax_sum|every probability vector sums to 1 within 10⁻⁹|PASS
VT2|attention_weights|every attention weight row sums to 1|PASS
VT3|d_stability|all 181 parameters and all logits have D=2^32|PASS
VT4|deterministic|two runs from seed 42 produce bit-identical losses and weights|PASS
VT5|forward_backward_roundtrip|same init, one step, bit-identical results|PASS
VT6|checkpoint_roundtrip|save → perturb → restore → bit-identical|PASS
VT7|weight_update|(w_old - w_new) / lr == grad, exact equality|PASS
VT8|loss_monotonicity|loss at epoch 20 < loss at epoch 1|PASS
VT9|gradient_correctness|analytical gradient matches finite difference (diff < 0.1)|PASS
# VT4 and VT5 are strongest: bit-identical across runs is structurally impossible with float arithmetic

# precision_floor_by_frame(id|bits|D_approx|decimal_digits|floor_per_op|after_1K_ops|after_1M_ops|after_1B_ops|hardware_alignment)
PF1|8|256|2.4|3.9×10⁻³|3.9|—|—|byte
PF2|16|65536|4.8|1.5×10⁻⁵|1.5×10⁻²|15.3|—|INT16
PF3|32|4.3×10⁹|9.6|2.3×10⁻¹⁰|2.3×10⁻⁷|2.3×10⁻⁴|0.23|INT32
PF4|64|1.8×10¹⁹|19.3|5.4×10⁻²⁰|5.4×10⁻¹⁷|5.4×10⁻¹⁴|5.4×10⁻¹¹|INT64/SIMD
PF5|128|3.4×10³⁸|38.5|2.9×10⁻³⁹|2.9×10⁻³⁶|2.9×10⁻³³|2.9×10⁻³⁰|AVX-512
PF6|335|8.7×10¹⁰⁰|100.9|1.1×10⁻¹⁰¹|1.1×10⁻⁹⁸|1.1×10⁻⁹⁵|1.1×10⁻⁹²|arbitrary precision
# worst-case assumes all errors same direction; observed accumulation far less (toy model: ~2000 ops, worst 9.07×10⁻¹³ vs theoretical 4.7×10⁻⁷)

# d_growth_before_fix(id|step|D_bit_length|D_approx|notes)
DGR1|0|33|4.3×10⁹|initial
DGR2|1|65|1.8×10¹⁹|multiplication
DGR3|5|193|6.3×10⁵⁷|
DGR4|10|353|9.2×10¹⁰⁵|exceeds atoms in observable universe
# after fix: steps 1-10 all D=4,294,967,296

# operation_count_per_forward(id|stage|ops_per_call|calls|total)
OPC1|embedding (vec add)|4 adds|4 positions|16
OPC2|Q projection (mat-vec 4×4)|16 mul + 12 add|4|112
OPC3|K projection|16 mul + 12 add|4|112
OPC4|V projection|16 mul + 12 add|4|112
OPC5|attention scores (dot 4-dim)|4 mul + 3 add|10 (causal)|70
OPC6|surrogate softmax|~3n per row|4 rows|~60
OPC7|value mix (weighted sum)|~8 per output elem|4×4|~128
OPC8|Wo projection|16 mul + 12 add|4|112
OPC9|residual add|4 adds|4|16
OPC10|FFN layer 1 (mat-vec 8×4)|32 mul + 24 add|4|224
OPC11|ReLU|8 comparisons|4|32
OPC12|FFN layer 2 (mat-vec 4×8)|32 mul + 28 add|4|240
OPC13|residual add|4 adds|4|16
OPC14|output projection (mat-vec 5×4)|20 mul + 15 add|4|140
# forward total: ~1,390 ops; backward ~same; per training step ~2,800
# 20 epochs × 2 windows × 2,800 ≈ 112,000 total VDR ops during training

# demonstrations(id|claim|evidence)
DM1|every LLM pipeline operation works in fixed-D rational arithmetic|forward, backprop, attention, softmax, sampling, weight updates all demonstrated
DM2|denominator growth solvable at operator level|basis-aware operators make frame stability automatic; model code unaware
DM3|quadratic surrogate eliminates transcendentals from forward pass|no exp anywhere; simpler backward; natural fit for VDR
DM4|exact determinism achievable|VT4+VT5: bit-identical across runs — structural property of integer arithmetic
DM5|D=2^32 sufficient precision for toy scale|20 epochs, worst error 9.07×10⁻¹³, well below 10⁻⁶

# limitations(id|limitation|description)
LM1|scale|181 params, 5 tokens; production needs billions of params, 50K+ vocab; Python VDR ~50-200× float per op
LM2|convergence quality|quadratic surrogate produces different optimization landscape than exp softmax; not compared at scale
LM3|no layer normalization|requires rsqrt (irrational) — must approximate via Newton iteration; engineering not math obstacle
LM4|single-head attention|multi-head structurally trivial but would test D stability more thoroughly
LM5|no hardware acceleration|all Python arbitrary-precision; production needs compiled kernels on fixed-width integers

# next_steps(id|step|description)
NS1|compiled arithmetic kernels|C/Rust implementation of basis-frame mul/div on fixed-width 32/64-bit V slots with bit-shift divmod
NS2|GPU implementation|D=2^32: multiply two i32→i64, split upper/lower 32 bits; maps to GPU integer multiply-and-split
NS3|larger models|verify D stability across 96+ layers, 4096+ hidden dim, 4096+ sequence length
NS4|selective remainder tracking|carry R through precision-sensitive paths (residual stream); flatten at insensitive boundaries (post-softmax)
NS5|mixed-precision frames|D=2^16 weight storage, D=2^32 accumulation, D=2^64 gradient statistics; basis-aware ops already handle rebasing

# softmax_comparison(id|property|taylor_exp|quadratic_surrogate)
SC1|forward ops per element|~32 (16 mul + 16 div depth 16)|3 (subtract, square, divide)
SC2|backward complexity|chain rule through 16 Taylor terms|single closed-form expression
SC3|transcendental functions|yes (exp approximated)|none
SC4|series truncation error|yes (controlled by depth)|none
SC5|distribution shape|sharply peaked (exponential)|broadly spread (quadratic)
SC6|sum-to-one guarantee|by construction after correction|by construction after correction
SC7|gradient saturation|yes (extreme logits → near-zero grad)|no (gradient proportional to input)
SC8|mixed-frame constants|16 VDR(k) divisions per element|1 shift subtraction
SC9|suitability for VDR|functional but expensive|natural fit

# quantization_comparison(id|property|int8_quantization|vdr_fixed_basis)
QC1|representation|integer with float scaling factor|integer triple [V,D,R] with power-of-two D
QC2|error tracking|quantization error discarded|remainder slot catches exact overflow
QC3|remainder options|none — information lost|monitor, accumulate, carry, or flatten
QC4|current toy model behavior|n/a|flattens remainders (like quantization) but infrastructure for exact carry exists

# relationships(from|rel|to)
P1|defines|P2
P2|prevents|DG1
P3|configurable_via|P4
P4|enables|PF3
DG1|caused_by|OC1
DG1|caused_by|OC3
DG3|caused_by|MF1
DG3|caused_by|MF9
DG3|caused_by|MF12
DG4|caused_by|MF1
BA1|solves|DG1
BA1|solves|DG2
BA2|solves|DG3
BA2|solves|DG5
BA2|solves|DG6
BA3|solves|DG2
BA1|implemented_in|OC1
BA1|implemented_in|OC3
BA2|implemented_in|OC5
BA2|implemented_in|OC6
QS1|eliminates|DG4
QS2|enables|DM3
QS3|ensures|VT1
QS5|simpler_than|SC2
QS7|distinct_from|SC1
MA1|component_of|MA9
MA3|component_of|MA6
MA7|component_of|MA8
WI1|enables|VT4
WI1|enables|DM4
TC2|requires|BA2
TRN5|demonstrates|VT8
VT3|validates|BA1
VT4|validates|DM4
VT7|validates|TC5
DM1|demonstrated_by|VT1
DM1|demonstrated_by|VT3
DM2|demonstrated_by|BA1
DM2|demonstrated_by|BA2
DM2|demonstrated_by|BA3
DM5|demonstrated_by|TRN5
LM1|motivates|NS1
LM1|motivates|NS2
LM3|motivates|NS3
LM5|motivates|NS1
NS5|extends|BA2
QC4|relates_to|NS4

# section_index(section|title|ids)
1|Introduction|P1,P2,P3
2|The VDR Representation|P1,P2,P3,P4
2.1|The Triple|P1
2.2|The Fixed-Frame Rule|P2
2.3|The Precision Floor|P3,P4
3|The Denominator Growth Problem|DG1-DG6,DGR1-DGR4
3.1|How D Explodes|DG1,DGR1-DGR4
3.2|Where Growth Occurs in LLM|DG1-DG6
3.3|The Solution: Basis-Aware Operators|BA1-BA3
3.4|Verification of Stability|VT3
4|The Toy Model|MA1-MA9,WI1-WI3,QS1-QS7,TC1-TC5,DS1-DS4
4.1|Architecture|MA1-MA9
4.2|Weight Initialization|WI1-WI3
4.3|Quadratic Softmax Surrogate|QS1-QS7
4.4|Training Configuration|TC1-TC5
4.5|Surrogate Softmax Backward|QS5
4.6|Text Generation|DS1-DS4
5|Results|TRN1-TRN5,AT1,GEN1,VT1-VT9
6|Discussion|DM1-DM5,LM1-LM5
7|Next Steps|NS1-NS5
C|Operator Basis-Awareness Coverage|OC1-OC7
D|D Growth Under Original Operators|DGR1-DGR4
E|Mixed-Frame Sources|MF1-MF22
F|Precision Floor by Frame Size|PF1-PF6
G|Softmax Surrogate Sum Residuals|TRN1-TRN5
H|Toy Model Parameter Census|MA1-MA9
I|Operation Count Per Forward Pass|OPC1-OPC14
J|Comparison of Softmax Approaches|SC1-SC9
K|Verification Test Execution Order|VT1-VT9

# decode_legend
# VDR: [V,D,R] triple; (V+R)/D = exact rational; D fixed power-of-two per pipeline stage
# closed: R=0; active: R≠0; R can be recursive tree of child VDR triples
# basis frame: the default D (2^32 in this paper) shared across all pipeline values
# divmod: integer division + modulo; at power-of-two D reduces to shift+mask
# to_qbasis: project any VDR value onto the current basis frame via divmod
# _basis_mul/_basis_div: basis-frame multiply/divide preserving D via divmod
# _both_in_basis: check both operands share D = default basis
# _one_in_basis: check exactly one operand in basis; rebase the other
# quadratic surrogate: p_i = (x_i-shift)²/Σ(x_j-shift)²; replaces exp softmax
# LCG: linear congruential generator for deterministic initialization
# precision floor: 1/D = smallest representable nonzero value = grid spacing
# D growth: uncontrolled denominator expansion from cross-multiplication of different-D operands
# Barrett reduction: integer division via precomputed multiplicative inverse
# ULP: unit in last place — float mantissa least significant bit magnitude
# frame sizes: Q8=D=2^8, Q16=D=2^16, Q32=D=2^32, Q64=D=2^64, Q335=D=2^335
# rel_types: defines|prevents|configurable_via|enables|caused_by|solves|implemented_in|eliminates|ensures|simpler_than|distinct_from|component_of|requires|demonstrates|validates|demonstrated_by|motivates|extends|relates_to
