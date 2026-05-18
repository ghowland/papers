You're right. If D is fixed per domain, it's not a runtime field — it's a domain constant. The Basis struct disappears. The shift and mask become module-level constants. Every struct gets leaner.

```zig
// ============================================================
// vdr_types.zig — VDR structs for LLM and Diffusion
// Fixed-basis, no runtime D. Domain constants only.
// ============================================================

// --- Domain Bases ---
// Fixed at the values that fit SIMD for each domain.
// These are the only place basis is defined.

const LLM_WEIGHT_BITS: u6 = 16;
const LLM_ACTIVATION_BITS: u6 = 32;
const LLM_GRAD_BITS: u6 = 64;
const DIFFUSION_BITS: u6 = 32;

// --- Element Types ---
// No basis field. The type itself implies the basis.
// V and R pack adjacent for SIMD.

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

// --- Dense Containers ---
// No basis field. The element type carries the contract.

const WeightVec = struct {
    len: i32,
    data: [*]Vdr16,
};

const WeightMat = struct {
    rows: i32,
    cols: i32,
    stride: i32,
    data: [*]Vdr16,
};

const ActivationVec = struct {
    len: i32,
    data: [*]Vdr32,
};

const ActivationMat = struct {
    rows: i32,
    cols: i32,
    stride: i32,
    data: [*]Vdr32,
};

const GradVec = struct {
    len: i32,
    data: [*]Vdr64,
};

const GradMat = struct {
    rows: i32,
    cols: i32,
    stride: i32,
    data: [*]Vdr64,
};

// --- LLM Layer Types ---

const LinearLayer = struct {
    weight: WeightMat,
    bias: ActivationVec,
};

const AttentionHead = struct {
    wq: WeightMat,
    wk: WeightMat,
    wv: WeightMat,
    wo: WeightMat,
    head_dim: i32,
};

const MultiHeadAttention = struct {
    heads: [*]AttentionHead,
    num_heads: i32,
    embed_dim: i32,
};

const LayerNorm = struct {
    gamma: ActivationVec,
    beta: ActivationVec,
    eps_v: i32,
};

const FeedForward = struct {
    up: LinearLayer,
    down: LinearLayer,
    gate: LinearLayer,
};

const TransformerBlock = struct {
    attn: MultiHeadAttention,
    ffn: FeedForward,
    norm1: LayerNorm,
    norm2: LayerNorm,
};

const TransformerModel = struct {
    embedding: WeightMat,
    blocks: [*]TransformerBlock,
    num_blocks: i32,
    final_norm: LayerNorm,
    lm_head: LinearLayer,
    vocab_size: i32,
    max_seq_len: i32,
};

// --- Activation Buffers ---

const ActivationBuffer = struct {
    seq_len: i32,
    embed_dim: i32,
    data: [*]Vdr32,
};

const AttentionScores = struct {
    seq_len: i32,
    num_heads: i32,
    data: [*]Vdr32,
};

const SoftmaxOutput = struct {
    len: i32,
    data: [*]Vdr32,
    sum_v: i32,     // must equal 1 << LLM_ACTIVATION_BITS exactly
};

// --- KV Cache ---

const KvEntry = struct {
    k: WeightVec,
    v: WeightVec,
};

const KvCache = struct {
    entries: [*]KvEntry,
    capacity: i32,
    len: i32,
    head_dim: i32,
    num_heads: i32,
};

// --- Diffusion Types ---

const DiffusionSchedule = struct {
    timesteps: i32,
    betas: ActivationVec,
    alphas: ActivationVec,
    alpha_bars: ActivationVec,
    sqrt_alpha_bars: ActivationVec,
    sqrt_one_minus_alpha_bars: ActivationVec,
    posterior_variance: ActivationVec,
};

const DiffusionLatent = struct {
    channels: i32,
    height: i32,
    width: i32,
    data: [*]Vdr32,
};

const DiffusionTrajectory = struct {
    num_frames: i32,
    latent_size: i32,
    data: [*]Vdr32,
};

const NoisePredictor = struct {
    backbone: TransformerModel,
    schedule: *DiffusionSchedule,
};

const DenoisingStep = struct {
    t: i32,
    xt: DiffusionLatent,
    eps_pred: DiffusionLatent,
    x_prev: DiffusionLatent,
};

// --- Gradient / Training ---

const OptimizerState = struct {
    lr_v: i64,
    lr_r: i64,
    momentum: [*]Vdr64,
    variance: [*]Vdr64,
    param_count: i32,
    step: i64,
};

// --- Rebase ---
// Only needed at boundaries between domains.
// src and dst bits are known constants, so the shift
// difference is computable at the call site.

const RebaseResult = struct {
    v: i64,
    r: i64,
};
```

Every struct got smaller. No basis pointer, no basis indirection, no runtime branching on bit width. The type system itself encodes which domain you're in — `WeightMat` is Q16, `ActivationMat` is Q32, `GradMat` is Q64. If you're holding a `WeightMat` you already know the shift is 16 and the mask is 0xFFFF. The compiler knows it too.

Rebase only happens at explicit domain boundaries — weight × activation produces an accumulation that needs widening from Q16 into Q32 space. That's a known fixed shift, not a runtime decision.
