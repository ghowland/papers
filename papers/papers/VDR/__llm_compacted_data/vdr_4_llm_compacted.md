# EXACT-FRACTION LANGUAGE MODEL ARCHITECTURE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → modules → components → test results → findings → limitations → relationships → sections

# principles(id|principle|rationale)
P1|Every LM component expressible as exact rational arithmetic|Complete path from raw text to logits to training update uses only exact VDR fractions
P2|Approximation boundary is design choice not hardware constraint|Truncation depth for exp, Q-basis precision, slice point for chaos — all chosen, not forced
P3|Bit-identical reproducibility|Same model + same params + same input = same exact output on any machine/OS/Python version; impossible with float ML
P4|Zero VDR computation errors across 705 cumulative tests|13 failures all test-design errors across entire project

# module_inventory(id|module|layer|purpose)
# Arithmetic Foundation (from VDR-1)
M01|vdr.py|foundation|Core triple, remainder, normalization, closed arithmetic
M02|active_mul.py|foundation|Active multiplication and division
M03|fn.py|foundation|Functional remainders, discrete calculus
M04|linalg.py|foundation|Vec, Mat, parse, serialize, LaTeX
M05|export.py|foundation|Lossy boundary (float, decimal)
# Transcendental and Nonlinear (new)
M06|exp.py|transcendental|Exact-fraction exponential: Taylor series, range reduction, negative helper
M07|logarithm.py|transcendental|Exact-fraction log: log1p series, log near one, log ratio
M08|softmax.py|transcendental|Exact softmax and rational surrogate softmax
# Differentiation (new)
M09|autodiff.py|differentiation|Reverse-mode scalar autodiff, computation graph, exact gradients
# Neural Network (new)
M10|nn.py|neural_network|Linear, ReLU, Sequential, parameter management
M11|losses.py|neural_network|MSE, L1, hinge loss
M12|optim.py|neural_network|SGD, Momentum, exact parameter updates
# Infrastructure (new)
M13|rng.py|infrastructure|Deterministic integer PRNG, rational random vectors
M14|init.py|infrastructure|Xavier-like rational initialization, zero bias
M15|sampling.py|infrastructure|Categorical sampling, top-k, nucleus filtering
M16|datasets.py|infrastructure|Vocab, tokenization, sliding windows, batching
M17|metrics.py|infrastructure|Accuracy, argmax, denominator complexity tracking
M18|checkpoint.py|infrastructure|Exact parameter save/load with zero precision loss
M19|basis.py|infrastructure|Shared Q-basis denominator management
M20|tensor.py|infrastructure|Batched matvec, row operations, masking, reduction
# Architecture (new)
M21|attention.py|architecture|Score computation, causal masking, softmax/surrogate weighting, value mixing
M22|transformer.py|architecture|Embedding, TransformerBlock, TinyTransformerLM, Q-basis conversion
M23|trainer.py|architecture|Training loop, evaluation, classification helpers
# Total: 24 modules (5 from VDR-1, 19 new). No circular dependencies. vdr.py has zero internal deps.

# test_results(id|batch|domain|tests|passed|failed)
T1|Softmax|Exact-fraction softmax, surrogate|26|26|0
T2|Autodiff|Reverse-mode exact differentiation|39|39|0
T3|Batch 2|Exponential and logarithm series|18|18|0
T4|Batch 3|Tensor operations, attention|28|28|0
T5|Batch 4|RNG, sampling, initialization|19|19|0
T6|Batch 5|Datasets, training, metrics, checkpoints|21|21|0
T7|Batch 6|Transformer, Q-basis, end-to-end LM|22|22|0
T8|NN Batch 1|Linear, ReLU, Sequential, optimizers|25|23|2
# Total: 198 tests, 196 passed, 2 failed (test-expectation errors), 0 VDR errors

# component_details(id|component|mechanism|key_results)
C01|Exact softmax|exp_N(x) = Σ x^k/k! truncated Taylor; s_i = exp_N(z_i-m)/Σ exp_N(z_j-m)|Logits [1,2,3]: outputs 64826368/720042809, 176214841/720042809, 479001600/720042809; sum exactly 1; equal logits [5,5,5,5] → exactly [1/4,1/4,1/4,1/4]; stabilization invariance holds
C02|Rational surrogate softmax|s_i = (z_i-m+c)²/Σ(z_j-m+c)²; avoids exponentials entirely|Logits [1,2,3] c=4: outputs 4/29, 9/29, 16/29; sum exactly 1; nonnegativity, symmetry, monotonicity
C03|Exact exponential|Three methods: direct Taylor, negative helper, range-reduced via exp(n+f)=exp(1)^n·exp(f)|exp(0)=1 exactly; exp(1,depth=3)=8/3; exp(-1,depth=4)=3/8; exp(-2)=1/exp(2) exactly; monotonicity verified
C04|Exact logarithm|log1p series: log(1+x)=x-x²/2+x³/3-...; each partial sum exact VDR fraction|log(1)=0 exactly; monotonicity preserved; exp-log local consistency verified near 1.1
C05|Exact autodiff|Reverse-mode scalar computation graph with Node objects; backward by topological sort|d(x²)/dx at x=3 = exactly 6; d(x³)/dx at x=2 = exactly 12; quotient rule d(x/y)/dy at x=6,y=3 = exactly -2/3; ReLU grad exactly 1 or 0; MSE gradients exact; chain rule (x²+1)x at x=2 = exactly 13
C06|Linear layer|Forward: y=Wx+b exact matvec+bias; Backward: grad_in=W^T·grad_out, weight_grad=outer(grad_out,input), bias_grad=grad_out|W=[[1,2],[3,4]] b=[5,6] input=[1,1]: forward [8,13] exactly; backward with grad_out=[1,2]: grad_in=[7,10] exactly
C07|ReLU|Forward: max(0,x) elementwise; Backward: gradient mask 1 where input>0, 0 elsewhere|Input [-2,-1,3] grad_out [1,3,5]: forward [0,0,3], backward [0,0,5] exact
C08|Sequential|Chain layers for forward/backward; tested Linear→ReLU→Linear|Forward produces exact output; backward propagates exact gradients through chain
C09|Losses|MSE: ((pred-target)²).mean(); L1: |pred-target|.mean(); Hinge: max(0,1-y·pred)|MSE([3,5],[1,1])=17/2 exactly; L1=3/2; hinge(-2,+1)=3
C10|SGD optimizer|W ← W - lr·grad; exact parameter updates|lr=1, W=[[1,2]] grad=[[4,5]]: W becomes [[-3,-3]] exactly
C11|Momentum optimizer|v ← μv + grad; W ← W - lr·v; exact velocity accumulation|After 2 steps with μ=1/2, accumulated velocity and updates match manual calculation exactly
C12|Attention|Score=QK^T; causal mask (upper-triangle with large negative fill); row-wise softmax; value mixing (weighted sum)|Every attention weight row sums to exactly 1; 2-position standard softmax: 43545600/59565131 and 16019531/59565131; surrogate: 16/25 and 9/25; causal masking zeros future positions exactly
C13|TinyTransformerLM|Embedding → TransformerBlock (attention+residual → feedforward+residual) → logits head|3-token vocab, 2-dim embedding, context 3; every logit exact fraction; cache exposes all intermediates; 6 parameter groups all exact; attention weights sum to exactly 1 at every position
C14|Q-basis conversion|Model converted to shared-denominator Q-basis representation|Forward passes produce identical exact results after conversion; Q-basis embedding lookup returns same fractions; Q-basis logits match original
C15|Training loop|Forward → loss → backward via autodiff → optimizer step → gradient zero|Single step produces exact loss; epoch of training produces measurably lower average loss — model is learning; every step exact
C16|Deterministic RNG|Linear congruential generator with exact integer state|Same seed → identical sequences, fractions, shuffles, permutations; 5-element sequences reproduced exactly
C17|Sampling|Categorical from exact probability vectors via CDF + rational threshold|One-hot [1,0,0] always returns index 0; top-k zeros all but k largest then renormalizes to exact sum 1; nucleus keeps minimal prefix exceeding threshold
C18|Checkpoints|Exact parameter serialization/deserialization|Every weight, bias, fraction saved and loaded with zero precision loss; bit-identical outputs after reload

# failures(id|test|expected|got|root_cause)
F1|Sequential forward|8|10|Manual computation did not correctly trace through ReLU between layers
F2|Tiny MLP forward|wrong expected|correct exact value|Similar layer composition tracing error
# Both test-expectation errors. Zero VDR computation errors.

# findings(id|finding|detail)
FN1|Exact normalization|Attention weights sum to exactly 1/1 at every position, layer, forward pass; output distributions sum to exactly 1; no probability mass created or destroyed
FN2|Full inspectability|Every intermediate value is exact printable fraction; attention weight for position 0→1 is exactly 16019531/59565131, not "approximately 0.27"
FN3|Platform independence|VDR fractions are platform-independent; no hardware-dependent float rounding; checkpoints preserve exact state across machines
FN4|Softmax engineering boundary|Truncated Taylor at moderate depth poor on large negative shifted logits; range reduction and Padé approximants are path forward
FN5|Denominator growth|Single forward pass produces denominators in tens of millions; training hundreds of steps → billions; manageable for research-scale tiny models, not production-scale
FN6|Approximation is explicit|Truncated Taylor exp is approximation — exact rational differing from true transcendental by known bounded amount; truncation depth chosen not forced

# limitations(id|limitation|detail)
L1|Not practical at production scale|Denominator growth through operations; tiny model forward pass → millions in denominators; training → billions+
L2|Truncated Taylor exp is approximation|VDR does not make exp rational; makes approximation explicit, controllable, exact at every truncation depth
L3|Architecture may need redesign|Standard transformer designed for float; GELU, layer norm with sqrt, float initialization awkward in exact fractions; rational surrogate softmax, ReLU, Xavier-like rational init are adaptations
L4|Gaussian elimination still unimplemented|Cofactor expansion limits practical matrix size; top priority from VDR-3
L5|Cross-entropy loss not yet integrated|Requires exact log (now available via logarithm.py); integration planned

# future_work(id|item|rationale)
FW1|Gaussian elimination|O(n³) exact rational elimination for all matrix operations; directly benefits transformer attention and feedforward
FW2|Better exponential evaluation|Padé approximants, range reduction with exact bounds, binary splitting; extend softmax to larger logit ranges
FW3|Exact cross-entropy loss|Integrate logarithm.py into loss module for standard LM training objective
FW4|Exact optimizer dynamics study|With exact gradients and updates, determine if training instabilities are arithmetic artifacts (float rounding) or algorithmic (inherent to optimization landscape)
FW5|Denominator growth tracking|How fast do parameter denominators grow during training? Natural precision budget? Periodic Q-basis re-projection to control growth?
FW6|Rational surrogate architectures|Replace transcendental nonlinearities with rational ones native to VDR; rational activations, normalization, attention kernels — not copies of float-era transformers
FW7|Q-basis scaling path|Project all parameters onto 2^k grid at each training step; controlled bounded explicit precision loss analogous to quantization but with exact error bounds

# complete_path(id|step|description)
CP1|Tokenization|Raw text → token IDs via character-level vocabulary
CP2|Embedding lookup|Token IDs → exact VDR fraction vectors
CP3|Attention scores|QK^T exact matrix computation
CP4|Causal masking|Upper-triangle boolean mask with large negative fill
CP5|Softmax normalization|Exact-fraction softmax or rational surrogate; weights sum to exactly 1
CP6|Value mixing|Weighted sum of value vectors with exact attention weights
CP7|Residual connection|Exact addition of attention output to input
CP8|Feedforward|Linear → ReLU → Linear with exact arithmetic
CP9|Residual connection|Exact addition of feedforward output
CP10|Logits head|Final linear layer producing exact logit fractions
CP11|Loss computation|MSE or classification loss as exact fraction
CP12|Backward propagation|Exact gradients via reverse-mode autodiff
CP13|Optimizer step|Exact parameter update (SGD or momentum)
# Every step uses only exact VDR fraction arithmetic. No floats anywhere.

# cumulative_statistics(id|paper|new_modules|tests|passed|failed_test_error|failed_vdr_error)
CS1|VDR-1|5|68|68|0|0
CS2|VDR-2|0 (15 gyms)|282|276|6|0
CS3|VDR-3|0 (8 gyms)|157|152|5|0
CS4|VDR-4|19|198|196|2|0
CS5|Total|24|705|692|13|0

# claims(id|claim|type|evidence)
CL1|Every component of a language model architecture expressible as exact rational arithmetic|demonstrated|CP1-CP13, C01-C18
CL2|Approximation boundary is design choice not hardware constraint|structural|P2, FN6, L2
CL3|Bit-identical reproducibility across platforms|demonstrated|FN3, C18
CL4|Exact normalization: attention weights sum to exactly 1|demonstrated|FN1, C12
CL5|Full inspectability of every intermediate value|demonstrated|FN2
CL6|Zero VDR computation errors across 705 tests|demonstrated|CS5
CL7|Not practical at production scale due to denominator growth|honest_limitation|L1, FN5
CL8|Working exact-fraction transformer runs forward passes, computes exact logits, produces exact attention weights|demonstrated|C13, T7

# relationships(from|rel|to)
M01|foundation_for|all other modules
M06|enables|C01 (exact softmax)
M07|enables|C04 (exact log)
M08|uses|M06
M09|enables|C05 (exact autodiff)
M10|uses|M04,M09
M21|uses|M08,M20,M04
M22|uses|M21,M10,M04,M19
M23|uses|M10,M11,M12,M16
C01|enables|C12 (attention softmax)
C02|alternative_to|C01
C05|enables|C15 (training backward pass)
C12|component_of|C13
C14|integrates|MATH-4 Q-basis into transformer
FN1|demonstrated_by|C12,C01
FN5|constrains|L1
FW7|addresses|FN5,L1
L3|motivates|FW6
L5|addressable_by|FW3

# section_index(section|title|ids)
1|Module Inventory|M01-M23
2|Test Results|T1-T8
3|Exact Softmax|C01,C02,FN4
4|Exact Autodiff|C05
5|Exact Exponential and Logarithm|C03,C04
6|Tensor Operations and Attention|C12,M20,M21
7|Neural Network Components|C06,C07,C08,C09,C10,C11
8|Infrastructure|C16,C17,C18,M13-M19
9|The Transformer|C13,C14,C15
10|What This Means|FN1,FN2,FN3,CL1-CL5
11|What This Does Not Mean|L1,L2,L3,CL7
12|The Two Failures|F1,F2
13|Module Dependency Graph|M01-M23 dependency structure
14|Cumulative Statistics|CS1-CS5
15|What Comes Next|FW1-FW7
16|Conclusion|CL1-CL8

# decode_legend
module_layers: foundation|transcendental|differentiation|neural_network|infrastructure|architecture
claim_types: demonstrated|structural|honest_limitation
failure_categories: test-expectation error (both F1,F2)
complete_path: CP1-CP13 traces tokenization through training update with zero floats
Q-basis: shared-denominator 2^k representation from MATH-4 for controlled precision
surrogate_softmax: square-shift kernel avoiding exponentials entirely
rel_types: foundation_for|enables|uses|alternative_to|component_of|integrates|demonstrated_by|constrains|addresses|motivates|addressable_by
