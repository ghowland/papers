```zig
// ============================================================
// vdr_types.zig — VDR structs for LLM and Diffusion workloads
// ============================================================

// --- Element Types ---
// D is implicit (owned by container). V and R pack adjacent for SIMD.
// Atomic remainder only — no tree. Sufficient for bounded ML domains.

const Vdr16 = struct {
    v: i16,
    r: i16,
};

const Vdr32 = struct {
    v: i32,
    r: i32,
};

const Vdr64 = struct {
    v: i64,
    r: i64,
};

// --- Basis ---
// Runtime basis descriptor. Power-of-two D means divmod is shift+mask.
// bits = 16 means D = 2^16 = 65536.
// shift and mask are precomputed from bits for fast divmod.

const Basis = struct {
    bits: i32,
    shift: u6,      // for right-shift (divmod quotient)
    mask: i64,       // for bitwise AND (divmod remainder)
};

// --- Dense Containers ---
// Vectors and matrices own their basis and hold flat arrays of elements.
// Single allocation, SIMD-friendly layout.

const VdrVec16 = struct {
    basis: Basis,
    len: i32,
    data: [*]Vdr16,   // packed V,R,V,R,V,R...
};

const VdrVec32 = struct {
    basis: Basis,
    len: i32,
    data: [*]Vdr32,
};

const VdrMat32 = struct {
    basis: Basis,
    rows: i32,
    cols: i32,
    stride: i32,      // for row-major packing / alignment
    data: [*]Vdr32,
};

const VdrMat16 = struct {
    basis: Basis,
    rows: i32,
    cols: i32,
    stride: i32,
    data: [*]Vdr16,
};

// --- LLM Layer Types ---

const LinearLayer = struct {
    weight: VdrMat16,    // quantized weights, 16-bit basis typical
    bias: VdrVec32,      // bias at higher precision than weights
};

const AttentionHead = struct {
    wq: VdrMat16,
    wk: VdrMat16,
    wv: VdrMat16,
    wo: VdrMat16,
    head_dim: i32,
};

const MultiHeadAttention = struct {
    heads: [*]AttentionHead,
    num_heads: i32,
    embed_dim: i32,
};

const LayerNorm = struct {
    gamma: VdrVec32,     // scale, 32-bit for normalization precision
    beta: VdrVec32,      // offset
    eps_v: i32,          // epsilon numerator as VDR element
    eps_basis: Basis,    // epsilon can have its own basis
};

const FeedForward = struct {
    up: LinearLayer,
    down: LinearLayer,
    gate: LinearLayer,   // for gated architectures (LLaMA-style)
};

const TransformerBlock = struct {
    attn: MultiHeadAttention,
    ffn: FeedForward,
    norm1: LayerNorm,
    norm2: LayerNorm,
};

const TransformerModel = struct {
    embedding: VdrMat16,
    blocks: [*]TransformerBlock,
    num_blocks: i32,
    final_norm: LayerNorm,
    lm_head: LinearLayer,
    vocab_size: i32,
    max_seq_len: i32,
};

// --- Activation Buffers ---
// Intermediate values during forward pass.
// 32-bit for accumulation even when weights are 16-bit.

const ActivationBuffer = struct {
    basis: Basis,
    seq_len: i32,
    embed_dim: i32,
    data: [*]Vdr32,
};

const AttentionScores = struct {
    basis: Basis,
    seq_len: i32,
    num_heads: i32,
    data: [*]Vdr32,      // softmax outputs: sum to exact 1 in this basis
};

const SoftmaxOutput = struct {
    basis: Basis,
    len: i32,
    data: [*]Vdr32,
    sum_v: i32,          // cached: should equal basis.mask + 1 (exact 1)
};

// --- KV Cache ---

const KvEntry = struct {
    k: VdrVec16,
    v: VdrVec16,
};

const KvCache = struct {
    entries: [*]KvEntry,
    capacity: i32,
    len: i32,
    head_dim: i32,
    num_heads: i32,
};

// --- Diffusion Types ---

// Precomputed schedule. All values exact in their basis.
// No sqrt drift over long chains.

const DiffusionSchedule = struct {
    basis: Basis,
    timesteps: i32,
    betas: VdrVec32,
    alphas: VdrVec32,
    alpha_bars: VdrVec32,
    sqrt_alpha_bars: VdrVec32,           // Newton-derived, exact in basis
    sqrt_one_minus_alpha_bars: VdrVec32, // same
    posterior_variance: VdrVec32,
};

// Single spatial position in the diffusion latent.
// For image/video: one element per channel per pixel.

const DiffusionLatent = struct {
    basis: Basis,
    channels: i32,
    height: i32,
    width: i32,
    data: [*]Vdr32,
};

// For video: latents over time. The chaining dimension.
const DiffusionTrajectory = struct {
    basis: Basis,
    num_frames: i32,
    latent_size: i32,    // channels * height * width
    data: [*]Vdr32,      // num_frames * latent_size elements
};

// The denoising network predicts noise as VDR.
// No arithmetic error between prediction and schedule application.

const NoisePredictor = struct {
    backbone: TransformerModel,    // or UNet — same VDR types either way
    schedule: *DiffusionSchedule,
};

const DenoisingStep = struct {
    t: i32,                        // current timestep
    xt: DiffusionLatent,           // noisy input
    eps_pred: DiffusionLatent,     // predicted noise
    x_prev: DiffusionLatent,       // output: one step cleaner
};

// --- Gradient / Training Types ---

const GradBuffer = struct {
    basis: Basis,
    len: i32,
    data: [*]Vdr64,     // 64-bit for gradient accumulation
};

const OptimizerState = struct {
    lr: Vdr64,
    lr_basis: Basis,
    momentum: [*]Vdr64,
    variance: [*]Vdr64,  // for Adam-style
    param_count: i32,
    step: i64,
};

// --- Basis Conversion ---
// When moving between layers at different bit widths,
// rebase explicitly. The remainder catches the mismatch exactly.

const RebaseOp = struct {
    src_basis: Basis,
    dst_basis: Basis,
};
```

Key structural decisions:

**D is never stored per-element.** It lives on the container. Every element in a vector or matrix shares the same basis, which is what makes SIMD uniform.

**Mixed precision via mixed basis.** Weights at Q16, activations at Q32, gradients at Q64. Rebase between them explicitly — the remainder catches the mismatch, nothing is silently truncated.

**Softmax carries a sum witness.** `sum_v` should equal D exactly. If it doesn't, something is wrong. Not approximately wrong — wrong. Binary check.

**Diffusion trajectory is flat.** Frames × latent size, single allocation, sequential access along the chaining dimension. The whole point is that stepping through this array for a million frames doesn't accumulate error.
