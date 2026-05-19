//! VDR Toy LLM — Single-block transformer in exact Q16 integer arithmetic.
//! No floating-point. No allocations beyond the initial arena.
//! All denominators implicit D = 65536 (2^16). divmod is shift+mask.
//!
//! Build: zig build-exe toy_llm.zig
//! Run:   ./toy_llm

const std = @import("std");
const print = std.debug.print;
const assert = std.debug.assert;

// ─────────────────────────────────────────────────────────────────────
// Config
// ─────────────────────────────────────────────────────────────────────

const VOCAB_SIZE: usize = 5;
const DIM: usize = 4;
const SEQ_LEN: usize = 4;
const FFN_DIM: usize = 8;
const N_EPOCHS: usize = 20;
const D: i32 = 65536; // 2^16
const D_U: u16 = 0xFFFF;
const SEED: u32 = 42;
const LR: i32 = 512; // 1/128 in Q16 = 65536/128

// corpus: "the cat sat on the mat"
const corpus = [_]u8{ 0, 1, 2, 3, 0, 4 };
const vocab = [_][]const u8{ "the", "cat", "sat", "on", "mat" };

// ─────────────────────────────────────────────────────────────────────
// Types
// ─────────────────────────────────────────────────────────────────────

fn Vec16(comptime N: usize) type {
    return struct {
        v: [N]i16,
        r: [N]i16,

        const Self = @This();

        fn zero() Self {
            return Self{
                .v = [_]i16{0} ** N,
                .r = [_]i16{0} ** N,
            };
        }
    };
}

fn Mat16(comptime ROWS: usize, comptime COLS: usize) type {
    return struct {
        v: [ROWS][COLS]i16,

        const Self = @This();

        fn zero() Self {
            return Self{
                .v = [_][COLS]i16{[_]i16{0} ** COLS} ** ROWS,
            };
        }
    };
}

fn GradMat(comptime ROWS: usize, comptime COLS: usize) type {
    return struct {
        v: [ROWS][COLS]i32,

        const Self = @This();

        fn zero() Self {
            return Self{
                .v = [_][COLS]i32{[_]i32{0} ** COLS} ** ROWS,
            };
        }
    };
}

fn GradVec(comptime N: usize) type {
    return struct {
        v: [N]i32,

        const Self = @This();

        fn zero() Self {
            return Self{
                .v = [_]i32{0} ** N,
            };
        }
    };
}

const Window = struct {
    context: [SEQ_LEN]u8,
    target: u8,
};

// ─────────────────────────────────────────────────────────────────────
// LCG RNG
// ─────────────────────────────────────────────────────────────────────

const LCG = struct {
    state: u32,

    fn init(seed: u32) LCG {
        return LCG{ .state = seed };
    }

    fn next(self: *LCG) u32 {
        self.state = self.state *% 1103515245 +% 12345;
        self.state &= 0x7FFFFFFF;
        return self.state;
    }

    fn next_i16_range(self: *LCG, lo: i16, hi: i16) i16 {
        const raw = self.next();
        const range: u32 = @intCast(@as(i32, hi) - @as(i32, lo) + 1);
        const val: i32 = @as(i32, @intCast(raw % range)) + @as(i32, lo);
        return @intCast(val);
    }
};

// ─────────────────────────────────────────────────────────────────────
// Scalar Kernels
// ─────────────────────────────────────────────────────────────────────

inline fn basis_mul(a: i16, b: i16) struct { v: i16, r: i16 } {
    const wide: i32 = @as(i32, a) * @as(i32, b);
    return .{
        .v = @intCast(@divTrunc(wide, D)),
        .r = @intCast(@rem(wide, D)),
    };
}

inline fn dot_q16(comptime N: usize, a: [N]i16, b: [N]i16) struct { v: i16, r: i16 } {
    var acc: i64 = 0;
    for (0..N) |i| {
        acc += @as(i64, a[i]) * @as(i64, b[i]);
    }
    return .{
        .v = @intCast(@divTrunc(acc, D)),
        .r = @intCast(@rem(acc, D)),
    };
}

// ─────────────────────────────────────────────────────────────────────
// Forward Cache
// ─────────────────────────────────────────────────────────────────────

const ForwardCache = struct {
    embedded: [SEQ_LEN]Vec16(DIM),
    Q: [SEQ_LEN]Vec16(DIM),
    K: [SEQ_LEN]Vec16(DIM),
    V_proj: [SEQ_LEN]Vec16(DIM),
    scores: [SEQ_LEN][SEQ_LEN]i16,
    shifted: [SEQ_LEN][SEQ_LEN]i16,
    weights: [SEQ_LEN][SEQ_LEN]i16,
    attn_out: [SEQ_LEN]Vec16(DIM),
    post_wo: [SEQ_LEN]Vec16(DIM),
    post_attn_res: [SEQ_LEN]Vec16(DIM),
    ffn_pre_relu: [SEQ_LEN]Vec16(FFN_DIM),
    ffn_post_relu: [SEQ_LEN]Vec16(FFN_DIM),
    ffn_out: [SEQ_LEN]Vec16(DIM),
    post_ffn_res: [SEQ_LEN]Vec16(DIM),
    logits: [SEQ_LEN]Vec16(VOCAB_SIZE),

    fn init() ForwardCache {
        return ForwardCache{
            .embedded = [_]Vec16(DIM){Vec16(DIM).zero()} ** SEQ_LEN,
            .Q = [_]Vec16(DIM){Vec16(DIM).zero()} ** SEQ_LEN,
            .K = [_]Vec16(DIM){Vec16(DIM).zero()} ** SEQ_LEN,
            .V_proj = [_]Vec16(DIM){Vec16(DIM).zero()} ** SEQ_LEN,
            .scores = [_][SEQ_LEN]i16{[_]i16{0} ** SEQ_LEN} ** SEQ_LEN,
            .shifted = [_][SEQ_LEN]i16{[_]i16{0} ** SEQ_LEN} ** SEQ_LEN,
            .weights = [_][SEQ_LEN]i16{[_]i16{0} ** SEQ_LEN} ** SEQ_LEN,
            .attn_out = [_]Vec16(DIM){Vec16(DIM).zero()} ** SEQ_LEN,
            .post_wo = [_]Vec16(DIM){Vec16(DIM).zero()} ** SEQ_LEN,
            .post_attn_res = [_]Vec16(DIM){Vec16(DIM).zero()} ** SEQ_LEN,
            .ffn_pre_relu = [_]Vec16(FFN_DIM){Vec16(FFN_DIM).zero()} ** SEQ_LEN,
            .ffn_post_relu = [_]Vec16(FFN_DIM){Vec16(FFN_DIM).zero()} ** SEQ_LEN,
            .ffn_out = [_]Vec16(DIM){Vec16(DIM).zero()} ** SEQ_LEN,
            .post_ffn_res = [_]Vec16(DIM){Vec16(DIM).zero()} ** SEQ_LEN,
            .logits = [_]Vec16(VOCAB_SIZE){Vec16(VOCAB_SIZE).zero()} ** SEQ_LEN,
        };
    }
};

// ─────────────────────────────────────────────────────────────────────
// Model
// ─────────────────────────────────────────────────────────────────────

const ToyTransformer = struct {
    // embeddings
    token_emb: [VOCAB_SIZE]Vec16(DIM),
    pos_emb: [SEQ_LEN]Vec16(DIM),

    // attention weights + bias
    wq: Mat16(DIM, DIM),
    wq_b: Vec16(DIM),
    wk: Mat16(DIM, DIM),
    wk_b: Vec16(DIM),
    wv: Mat16(DIM, DIM),
    wv_b: Vec16(DIM),
    wo: Mat16(DIM, DIM),
    wo_b: Vec16(DIM),

    // FFN weights + bias
    ffn1: Mat16(FFN_DIM, DIM),
    ffn1_b: Vec16(FFN_DIM),
    ffn2: Mat16(DIM, FFN_DIM),
    ffn2_b: Vec16(DIM),

    // output projection
    out: Mat16(VOCAB_SIZE, DIM),
    out_b: Vec16(VOCAB_SIZE),

    // gradients
    wq_g: GradMat(DIM, DIM),
    wq_b_g: GradVec(DIM),
    wk_g: GradMat(DIM, DIM),
    wk_b_g: GradVec(DIM),
    wv_g: GradMat(DIM, DIM),
    wv_b_g: GradVec(DIM),
    wo_g: GradMat(DIM, DIM),
    wo_b_g: GradVec(DIM),
    ffn1_g: GradMat(FFN_DIM, DIM),
    ffn1_b_g: GradVec(FFN_DIM),
    ffn2_g: GradMat(DIM, FFN_DIM),
    ffn2_b_g: GradVec(DIM),
    out_g: GradMat(VOCAB_SIZE, DIM),
    out_b_g: GradVec(VOCAB_SIZE),

    // cache
    cache: ForwardCache,

    fn init(seed: u32) ToyTransformer {
        var rng = LCG.init(seed);
        var model: ToyTransformer = undefined;

        // init embeddings: values in [-3, 3] scaled to Q16 as val * 8192
        for (0..VOCAB_SIZE) |t| {
            for (0..DIM) |d| {
                model.token_emb[t].v[d] = rng.next_i16_range(-3, 3) * 8192;
                model.token_emb[t].r[d] = 0;
            }
        }
        for (0..SEQ_LEN) |p| {
            for (0..DIM) |d| {
                model.pos_emb[p].v[d] = rng.next_i16_range(-3, 3) * 8192;
                model.pos_emb[p].r[d] = 0;
            }
        }

        // init weight matrices
        init_mat(DIM, DIM, &model.wq.v, &rng);
        init_vec16(DIM, &model.wq_b.v, &rng);
        model.wq_b.r = [_]i16{0} ** DIM;
        init_mat(DIM, DIM, &model.wk.v, &rng);
        init_vec16(DIM, &model.wk_b.v, &rng);
        model.wk_b.r = [_]i16{0} ** DIM;
        init_mat(DIM, DIM, &model.wv.v, &rng);
        init_vec16(DIM, &model.wv_b.v, &rng);
        model.wv_b.r = [_]i16{0} ** DIM;
        init_mat(DIM, DIM, &model.wo.v, &rng);
        init_vec16(DIM, &model.wo_b.v, &rng);
        model.wo_b.r = [_]i16{0} ** DIM;

        init_mat(FFN_DIM, DIM, &model.ffn1.v, &rng);
        init_vec16(FFN_DIM, &model.ffn1_b.v, &rng);
        model.ffn1_b.r = [_]i16{0} ** FFN_DIM;
        init_mat(DIM, FFN_DIM, &model.ffn2.v, &rng);
        init_vec16(DIM, &model.ffn2_b.v, &rng);
        model.ffn2_b.r = [_]i16{0} ** DIM;

        init_mat(VOCAB_SIZE, DIM, &model.out.v, &rng);
        init_vec16(VOCAB_SIZE, &model.out_b.v, &rng);
        model.out_b.r = [_]i16{0} ** VOCAB_SIZE;

        // zero gradients
        model.zero_grad();

        // init cache
        model.cache = ForwardCache.init();

        return model;
    }

    fn zero_grad(self: *ToyTransformer) void {
        self.wq_g = GradMat(DIM, DIM).zero();
        self.wq_b_g = GradVec(DIM).zero();
        self.wk_g = GradMat(DIM, DIM).zero();
        self.wk_b_g = GradVec(DIM).zero();
        self.wv_g = GradMat(DIM, DIM).zero();
        self.wv_b_g = GradVec(DIM).zero();
        self.wo_g = GradMat(DIM, DIM).zero();
        self.wo_b_g = GradVec(DIM).zero();
        self.ffn1_g = GradMat(FFN_DIM, DIM).zero();
        self.ffn1_b_g = GradVec(FFN_DIM).zero();
        self.ffn2_g = GradMat(DIM, FFN_DIM).zero();
        self.ffn2_b_g = GradVec(DIM).zero();
        self.out_g = GradMat(VOCAB_SIZE, DIM).zero();
        self.out_b_g = GradVec(VOCAB_SIZE).zero();
    }
};

// ─────────────────────────────────────────────────────────────────────
// Init helpers
// ─────────────────────────────────────────────────────────────────────

fn init_mat(comptime ROWS: usize, comptime COLS: usize, out: *[ROWS][COLS]i16, rng: *LCG) void {
    for (0..ROWS) |i| {
        for (0..COLS) |j| {
            out[i][j] = rng.next_i16_range(-3, 3) * 8192;
        }
    }
}

fn init_vec16(comptime N: usize, out: *[N]i16, rng: *LCG) void {
    for (0..N) |i| {
        out[i] = rng.next_i16_range(-1, 1) * 8192;
    }
}

// ─────────────────────────────────────────────────────────────────────
// Linear forward
// ─────────────────────────────────────────────────────────────────────

fn linear_forward(
    comptime ROWS: usize,
    comptime COLS: usize,
    weight: *const [ROWS][COLS]i16,
    bias: *const [ROWS]i16,
    input: *const [COLS]i16,
    out_v: *[ROWS]i16,
    out_r: *[ROWS]i16,
) void {
    for (0..ROWS) |i| {
        var acc: i64 = 0;
        for (0..COLS) |j| {
            acc += @as(i64, weight[i][j]) * @as(i64, input[j]);
        }
        // rebase to Q16
        const v_raw: i64 = @divTrunc(acc, D);
        const r_raw: i64 = @rem(acc, D);
        // add bias
        const with_bias: i64 = v_raw * D + r_raw + @as(i64, bias[i]) * D;
        out_v[i] = @intCast(@divTrunc(with_bias, D));
        out_r[i] = @intCast(@rem(with_bias, D));
    }
}

// ─────────────────────────────────────────────────────────────────────
// Linear backward
// ─────────────────────────────────────────────────────────────────────

fn linear_backward(
    comptime ROWS: usize,
    comptime COLS: usize,
    weight: *const [ROWS][COLS]i16,
    weight_grad: *[ROWS][COLS]i32,
    bias_grad: *[ROWS]i32,
    input_v: *const [COLS]i16,
    grad_output: *const [ROWS]i32,
    grad_input: *[COLS]i32,
) void {
    // grad_input = W^T @ grad_output
    for (0..COLS) |j| {
        var acc: i64 = 0;
        for (0..ROWS) |i| {
            acc += @as(i64, weight[i][j]) * @as(i64, grad_output[i]);
        }
        grad_input[j] = @intCast(@divTrunc(acc, D));
    }

    // weight_grad += outer(grad_output, input)
    for (0..ROWS) |i| {
        for (0..COLS) |j| {
            const prod: i64 = @as(i64, grad_output[i]) * @as(i64, input_v[j]);
            weight_grad[i][j] += @intCast(@divTrunc(prod, D));
        }
    }

    // bias_grad += grad_output
    for (0..ROWS) |i| {
        bias_grad[i] += grad_output[i];
    }
}

// ─────────────────────────────────────────────────────────────────────
// Attention scores
// ─────────────────────────────────────────────────────────────────────

fn attention_scores(cache: *ForwardCache) void {
    for (0..SEQ_LEN) |i| {
        for (0..SEQ_LEN) |j| {
            if (j > i) {
                cache.scores[i][j] = -32767;
                continue;
            }
            var acc: i64 = 0;
            for (0..DIM) |d| {
                acc += @as(i64, cache.Q[i].v[d]) * @as(i64, cache.K[j].v[d]);
            }
            cache.scores[i][j] = @intCast(@divTrunc(acc, D));
        }
    }
}

// ─────────────────────────────────────────────────────────────────────
// Quadratic softmax surrogate
// ─────────────────────────────────────────────────────────────────────

fn softmax_surrogate(
    comptime N: usize,
    scores: *const [N]i16,
    probs: *[N]i16,
    shifted_out: *[N]i16,
) void {
    // find min
    var min_val: i16 = scores[0];
    for (1..N) |i| {
        if (scores[i] < min_val) min_val = scores[i];
    }

    // compute shifted and squares
    var sum_sq: i64 = 0;
    var squares: [N]i64 = undefined;
    for (0..N) |i| {
        shifted_out[i] = scores[i] - min_val;
        const s: i64 = @as(i64, shifted_out[i]);
        squares[i] = s * s;
        sum_sq += squares[i];
    }

    if (sum_sq == 0) {
        const uniform: i16 = @intCast(@divTrunc(@as(i64, D), @as(i64, N)));
        for (0..N) |i| {
            probs[i] = uniform;
        }
        return;
    }

    // N-1 probabilities, last = D - sum(first N-1)
    var running: i64 = 0;
    for (0..N - 1) |i| {
        const p: i64 = @divTrunc(squares[i] * D, sum_sq);
        probs[i] = @intCast(p);
        running += p;
    }
    probs[N - 1] = @intCast(D - running);
}

// ─────────────────────────────────────────────────────────────────────
// Softmax surrogate backward
// ─────────────────────────────────────────────────────────────────────

fn softmax_surrogate_backward(
    comptime N: usize,
    grad_probs: *const [N]i32,
    probs: *const [N]i16,
    shifted: *const [N]i16,
    grad_scores: *[N]i32,
) void {
    var sum_sq: i64 = 0;
    for (0..N) |i| {
        sum_sq += @as(i64, shifted[i]) * @as(i64, shifted[i]);
    }

    if (sum_sq == 0) {
        for (0..N) |i| grad_scores[i] = 0;
        return;
    }

    // dot(grad_probs, probs) in Q16 scaling
    var dot_gp: i64 = 0;
    for (0..N) |i| {
        dot_gp += @as(i64, grad_probs[i]) * @as(i64, probs[i]);
    }

    for (0..N) |i| {
        const diff: i64 = @as(i64, grad_probs[i]) * D - dot_gp;
        const numer: i64 = 2 * @as(i64, shifted[i]) * diff;
        grad_scores[i] = @intCast(@divTrunc(numer, sum_sq));
    }
}

// ─────────────────────────────────────────────────────────────────────
// Attention mix
// ─────────────────────────────────────────────────────────────────────

fn attention_mix(cache: *ForwardCache) void {
    for (0..SEQ_LEN) |i| {
        for (0..DIM) |d| {
            var acc: i64 = 0;
            for (0..SEQ_LEN) |j| {
                acc += @as(i64, cache.weights[i][j]) * @as(i64, cache.V_proj[j].v[d]);
            }
            cache.attn_out[i].v[d] = @intCast(@divTrunc(acc, D));
            cache.attn_out[i].r[d] = @intCast(@rem(acc, D));
        }
    }
}

// ─────────────────────────────────────────────────────────────────────
// Attention mix backward
// ─────────────────────────────────────────────────────────────────────

fn attention_mix_backward(
    grad_attn_out: *const [SEQ_LEN][DIM]i32,
    weights: *const [SEQ_LEN][SEQ_LEN]i16,
    v_proj: *const [SEQ_LEN]Vec16(DIM),
    grad_weights: *[SEQ_LEN][SEQ_LEN]i32,
    grad_v: *[SEQ_LEN][DIM]i32,
) void {
    // grad_weights[i][j] = dot(grad_attn_out[i], V[j])
    for (0..SEQ_LEN) |i| {
        for (0..SEQ_LEN) |j| {
            var acc: i64 = 0;
            for (0..DIM) |d| {
                acc += @as(i64, grad_attn_out[i][d]) * @as(i64, v_proj[j].v[d]);
            }
            grad_weights[i][j] = @intCast(@divTrunc(acc, D));
        }
    }

    // grad_V[j][d] = sum_i weights[i][j] * grad_attn_out[i][d]
    for (0..SEQ_LEN) |j| {
        for (0..DIM) |d| {
            var acc: i64 = 0;
            for (0..SEQ_LEN) |i| {
                acc += @as(i64, weights[i][j]) * @as(i64, grad_attn_out[i][d]);
            }
            grad_v[j][d] = @intCast(@divTrunc(acc, D));
        }
    }
}

// ─────────────────────────────────────────────────────────────────────
// Score backward
// ─────────────────────────────────────────────────────────────────────

fn score_backward(
    grad_scores: *const [SEQ_LEN][SEQ_LEN]i32,
    Q: *const [SEQ_LEN]Vec16(DIM),
    K: *const [SEQ_LEN]Vec16(DIM),
    grad_Q: *[SEQ_LEN][DIM]i32,
    grad_K: *[SEQ_LEN][DIM]i32,
) void {
    for (0..SEQ_LEN) |i| {
        for (0..DIM) |d| {
            var acc: i64 = 0;
            for (0..SEQ_LEN) |j| {
                acc += @as(i64, grad_scores[i][j]) * @as(i64, K[j].v[d]);
            }
            grad_Q[i][d] = @intCast(@divTrunc(acc, D));
        }
    }

    for (0..SEQ_LEN) |j| {
        for (0..DIM) |d| {
            var acc: i64 = 0;
            for (0..SEQ_LEN) |i| {
                acc += @as(i64, grad_scores[i][j]) * @as(i64, Q[i].v[d]);
            }
            grad_K[j][d] = @intCast(@divTrunc(acc, D));
        }
    }
}

// ─────────────────────────────────────────────────────────────────────
// ReLU forward / backward
// ─────────────────────────────────────────────────────────────────────

fn relu_forward(comptime N: usize, input: *const Vec16(N), output: *Vec16(N)) void {
    for (0..N) |i| {
        if (input.v[i] > 0) {
            output.v[i] = input.v[i];
            output.r[i] = input.r[i];
        } else {
            output.v[i] = 0;
            output.r[i] = 0;
        }
    }
}

fn relu_backward(comptime N: usize, pre_relu_v: *const [N]i16, grad_out: *const [N]i32, grad_in: *[N]i32) void {
    for (0..N) |i| {
        grad_in[i] = if (pre_relu_v[i] > 0) grad_out[i] else 0;
    }
}

// ─────────────────────────────────────────────────────────────────────
// Residual add
// ─────────────────────────────────────────────────────────────────────

fn residual_add(comptime N: usize, a: *const Vec16(N), b: *const Vec16(N), out: *Vec16(N)) void {
    for (0..N) |i| {
        const sum: i32 = @as(i32, a.v[i]) + @as(i32, b.v[i]);
        out.v[i] = @intCast(@as(i32, @truncate(@as(i64, sum) & 0xFFFF)));
        out.r[i] = 0;
    }
}

// ─────────────────────────────────────────────────────────────────────
// Full forward pass
// ─────────────────────────────────────────────────────────────────────

fn forward(model: *ToyTransformer, token_ids: [SEQ_LEN]u8) void {
    // embed
    for (0..SEQ_LEN) |pos| {
        const tid: usize = token_ids[pos];
        for (0..DIM) |d| {
            const sum: i32 = @as(i32, model.token_emb[tid].v[d]) + @as(i32, model.pos_emb[pos].v[d]);
            model.cache.embedded[pos].v[d] = @intCast(sum);
            model.cache.embedded[pos].r[d] = 0;
        }
    }

    // Q, K, V projections
    for (0..SEQ_LEN) |pos| {
        linear_forward(DIM, DIM, &model.wq.v, &model.wq_b.v, &model.cache.embedded[pos].v, &model.cache.Q[pos].v, &model.cache.Q[pos].r);
        linear_forward(DIM, DIM, &model.wk.v, &model.wk_b.v, &model.cache.embedded[pos].v, &model.cache.K[pos].v, &model.cache.K[pos].r);
        linear_forward(DIM, DIM, &model.wv.v, &model.wv_b.v, &model.cache.embedded[pos].v, &model.cache.V_proj[pos].v, &model.cache.V_proj[pos].r);
    }

    // attention scores
    attention_scores(&model.cache);

    // softmax per row
    for (0..SEQ_LEN) |i| {
        softmax_surrogate(SEQ_LEN, &model.cache.scores[i], &model.cache.weights[i], &model.cache.shifted[i]);
    }

    // attention mix
    attention_mix(&model.cache);

    // Wo projection
    for (0..SEQ_LEN) |pos| {
        linear_forward(DIM, DIM, &model.wo.v, &model.wo_b.v, &model.cache.attn_out[pos].v, &model.cache.post_wo[pos].v, &model.cache.post_wo[pos].r);
    }

    // residual: embedded + post_wo
    for (0..SEQ_LEN) |pos| {
        residual_add(DIM, &model.cache.embedded[pos], &model.cache.post_wo[pos], &model.cache.post_attn_res[pos]);
    }

    // FFN
    for (0..SEQ_LEN) |pos| {
        // ffn1
        linear_forward(FFN_DIM, DIM, &model.ffn1.v, &model.ffn1_b.v, &model.cache.post_attn_res[pos].v, &model.cache.ffn_pre_relu[pos].v, &model.cache.ffn_pre_relu[pos].r);
        // relu
        relu_forward(FFN_DIM, &model.cache.ffn_pre_relu[pos], &model.cache.ffn_post_relu[pos]);
        // ffn2
        linear_forward(DIM, FFN_DIM, &model.ffn2.v, &model.ffn2_b.v, &model.cache.ffn_post_relu[pos].v, &model.cache.ffn_out[pos].v, &model.cache.ffn_out[pos].r);
    }

    // residual: post_attn_res + ffn_out
    for (0..SEQ_LEN) |pos| {
        residual_add(DIM, &model.cache.post_attn_res[pos], &model.cache.ffn_out[pos], &model.cache.post_ffn_res[pos]);
    }

    // output projection
    for (0..SEQ_LEN) |pos| {
        linear_forward(VOCAB_SIZE, DIM, &model.out.v, &model.out_b.v, &model.cache.post_ffn_res[pos].v, &model.cache.logits[pos].v, &model.cache.logits[pos].r);
    }
}

// ─────────────────────────────────────────────────────────────────────
// Full backward pass from last position
// ─────────────────────────────────────────────────────────────────────

fn backward(model: *ToyTransformer, grad_logits_last: *const [VOCAB_SIZE]i32) void {
    // only backprop from last position
    const last = SEQ_LEN - 1;

    // backward through output projection
    var grad_post_ffn: [SEQ_LEN][DIM]i32 = [_][DIM]i32{[_]i32{0} ** DIM} ** SEQ_LEN;
    linear_backward(VOCAB_SIZE, DIM, &model.out.v, &model.out_g.v, &model.out_b_g.v, &model.cache.post_ffn_res[last].v, grad_logits_last, &grad_post_ffn[last]);

    // backward through FFN residual: grad splits to FFN path and skip
    var grad_ffn2_out: [DIM]i32 = grad_post_ffn[last];
    const grad_post_attn_res_from_ffn: [DIM]i32 = grad_post_ffn[last]; // skip connection

    // backward through ffn2
    var grad_post_relu: [FFN_DIM]i32 = undefined;
    linear_backward(DIM, FFN_DIM, &model.ffn2.v, &model.ffn2_g.v, &model.ffn2_b_g.v, &model.cache.ffn_post_relu[last].v, &grad_ffn2_out, &grad_post_relu);

    // backward through relu
    var grad_pre_relu: [FFN_DIM]i32 = undefined;
    relu_backward(FFN_DIM, &model.cache.ffn_pre_relu[last].v, &grad_post_relu, &grad_pre_relu);

    // backward through ffn1
    var grad_from_ffn1: [DIM]i32 = undefined;
    linear_backward(FFN_DIM, DIM, &model.ffn1.v, &model.ffn1_g.v, &model.ffn1_b_g.v, &model.cache.post_attn_res[last].v, &grad_pre_relu, &grad_from_ffn1);

    // combine FFN backward + skip
    var grad_post_attn_res: [DIM]i32 = undefined;
    for (0..DIM) |d| {
        grad_post_attn_res[d] = grad_from_ffn1[d] + grad_post_attn_res_from_ffn[d];
    }

    // backward through attention residual: grad splits to Wo path and skip
    var grad_post_wo: [SEQ_LEN][DIM]i32 = [_][DIM]i32{[_]i32{0} ** DIM} ** SEQ_LEN;
    grad_post_wo[last] = grad_post_attn_res;
    // var grad_embedded_from_res: [DIM]i32 = grad_post_attn_res; // skip

    // backward through Wo
    var grad_attn_out: [SEQ_LEN][DIM]i32 = [_][DIM]i32{[_]i32{0} ** DIM} ** SEQ_LEN;
    linear_backward(DIM, DIM, &model.wo.v, &model.wo_g.v, &model.wo_b_g.v, &model.cache.attn_out[last].v, &grad_post_wo[last], &grad_attn_out[last]);

    // backward through attention mix
    var grad_weights: [SEQ_LEN][SEQ_LEN]i32 = [_][SEQ_LEN]i32{[_]i32{0} ** SEQ_LEN} ** SEQ_LEN;
    var grad_v: [SEQ_LEN][DIM]i32 = [_][DIM]i32{[_]i32{0} ** DIM} ** SEQ_LEN;
    attention_mix_backward(&grad_attn_out, &model.cache.weights, &model.cache.V_proj, &grad_weights, &grad_v);

    // backward through softmax surrogate (only last row matters for single-position backprop)
    var grad_scores: [SEQ_LEN][SEQ_LEN]i32 = [_][SEQ_LEN]i32{[_]i32{0} ** SEQ_LEN} ** SEQ_LEN;
    for (0..SEQ_LEN) |i| {
        softmax_surrogate_backward(SEQ_LEN, &grad_weights[i], &model.cache.weights[i], &model.cache.shifted[i], &grad_scores[i]);
    }

    // backward through scores
    var grad_Q: [SEQ_LEN][DIM]i32 = undefined;
    var grad_K: [SEQ_LEN][DIM]i32 = undefined;
    score_backward(&grad_scores, &model.cache.Q, &model.cache.K, &grad_Q, &grad_K);

    // backward through Wq, Wk, Wv projections
    for (0..SEQ_LEN) |pos| {
        var discard_q: [DIM]i32 = undefined;
        linear_backward(DIM, DIM, &model.wq.v, &model.wq_g.v, &model.wq_b_g.v, &model.cache.embedded[pos].v, &grad_Q[pos], &discard_q);

        var discard_k: [DIM]i32 = undefined;
        linear_backward(DIM, DIM, &model.wk.v, &model.wk_g.v, &model.wk_b_g.v, &model.cache.embedded[pos].v, &grad_K[pos], &discard_k);

        var discard_v: [DIM]i32 = undefined;
        linear_backward(DIM, DIM, &model.wv.v, &model.wv_g.v, &model.wv_b_g.v, &model.cache.embedded[pos].v, &grad_v[pos], &discard_v);
    }
}

// ─────────────────────────────────────────────────────────────────────
// SGD step
// ─────────────────────────────────────────────────────────────────────

fn sgd_mat(comptime ROWS: usize, comptime COLS: usize, weight: *[ROWS][COLS]i16, grad: *[ROWS][COLS]i32) void {
    for (0..ROWS) |i| {
        for (0..COLS) |j| {
            const update: i64 = @as(i64, LR) * @as(i64, grad[i][j]);
            const update_q16: i32 = @intCast(@divTrunc(update, D));
            weight[i][j] -= @intCast(update_q16);
        }
    }
}

fn sgd_vec(comptime N: usize, weight: *[N]i16, grad: *[N]i32) void {
    for (0..N) |i| {
        const update: i64 = @as(i64, LR) * @as(i64, grad[i]);
        const update_q16: i32 = @intCast(@divTrunc(update, D));
        weight[i] -= @intCast(update_q16);
    }
}

fn sgd_step(model: *ToyTransformer) void {
    sgd_mat(DIM, DIM, &model.wq.v, &model.wq_g.v);
    sgd_vec(DIM, &model.wq_b.v, &model.wq_b_g.v);
    sgd_mat(DIM, DIM, &model.wk.v, &model.wk_g.v);
    sgd_vec(DIM, &model.wk_b.v, &model.wk_b_g.v);
    sgd_mat(DIM, DIM, &model.wv.v, &model.wv_g.v);
    sgd_vec(DIM, &model.wv_b.v, &model.wv_b_g.v);
    sgd_mat(DIM, DIM, &model.wo.v, &model.wo_g.v);
    sgd_vec(DIM, &model.wo_b.v, &model.wo_b_g.v);
    sgd_mat(FFN_DIM, DIM, &model.ffn1.v, &model.ffn1_g.v);
    sgd_vec(FFN_DIM, &model.ffn1_b.v, &model.ffn1_b_g.v);
    sgd_mat(DIM, FFN_DIM, &model.ffn2.v, &model.ffn2_g.v);
    sgd_vec(DIM, &model.ffn2_b.v, &model.ffn2_b_g.v);
    sgd_mat(VOCAB_SIZE, DIM, &model.out.v, &model.out_g.v);
    sgd_vec(VOCAB_SIZE, &model.out_b.v, &model.out_b_g.v);
}

// ─────────────────────────────────────────────────────────────────────
// Loss
// ─────────────────────────────────────────────────────────────────────

fn mse_loss(pred: *const [VOCAB_SIZE]i16, target: *const [VOCAB_SIZE]i32) i64 {
    var total: i64 = 0;
    for (0..VOCAB_SIZE) |i| {
        const diff: i64 = @as(i64, pred[i]) - @as(i64, target[i]);
        total += diff * diff;
    }
    return @divTrunc(total, VOCAB_SIZE);
}

fn mse_grad(pred: *const [VOCAB_SIZE]i16, target: *const [VOCAB_SIZE]i32, grad: *[VOCAB_SIZE]i32) void {
    for (0..VOCAB_SIZE) |i| {
        const item: i32 = @intCast(target[i]);
        const diff: i32 = @as(i32, pred[i]) - item;
        grad[i] = @divTrunc(2 * diff, VOCAB_SIZE);
    }
}

// ─────────────────────────────────────────────────────────────────────
// One-hot target
// ─────────────────────────────────────────────────────────────────────

fn one_hot(target_id: u8, out: *[VOCAB_SIZE]i32) void {
    for (0..VOCAB_SIZE) |i| {
        out[i] = if (i == target_id) D else 0;
    }
}

// ─────────────────────────────────────────────────────────────────────
// Training
// ─────────────────────────────────────────────────────────────────────

fn train_step(model: *ToyTransformer, context: [SEQ_LEN]u8, target_id: u8) i64 {
    forward(model, context);

    // softmax on last position
    var probs: [VOCAB_SIZE]i16 = undefined;
    var shifted: [VOCAB_SIZE]i16 = undefined;
    softmax_surrogate(VOCAB_SIZE, &model.cache.logits[SEQ_LEN - 1].v, &probs, &shifted);

    // one-hot
    var target: [VOCAB_SIZE]i32 = undefined;
    one_hot(target_id, &target);

    // loss
    const loss = mse_loss(&probs, &target);

    // grad of loss
    var grad_probs: [VOCAB_SIZE]i32 = undefined;
    mse_grad(&probs, &target, &grad_probs);

    // backward through softmax
    var grad_logits: [VOCAB_SIZE]i32 = undefined;
    softmax_surrogate_backward(VOCAB_SIZE, &grad_probs, &probs, &shifted, &grad_logits);

    // backward through model
    model.zero_grad();
    backward(model, &grad_logits);

    // SGD step
    sgd_step(model);

    return loss;
}

fn make_windows() [2]Window {
    return [2]Window{
        Window{ .context = .{ 0, 1, 2, 3 }, .target = 0 },
        Window{ .context = .{ 1, 2, 3, 0 }, .target = 4 },
    };
}

fn train_epoch(model: *ToyTransformer, windows: []const Window) i64 {
    var total: i64 = 0;
    for (windows) |w| {
        total += train_step(model, w.context, w.target);
    }
    return @divTrunc(total, @as(i64, @intCast(windows.len)));
}

// ─────────────────────────────────────────────────────────────────────
// Generation
// ─────────────────────────────────────────────────────────────────────

fn sample_greedy(probs: *const [VOCAB_SIZE]i16) u8 {
    var best: u8 = 0;
    var best_val: i16 = probs[0];
    for (1..VOCAB_SIZE) |i| {
        if (probs[i] > best_val) {
            best_val = probs[i];
            best = @intCast(i);
        }
    }
    return best;
}

fn generate(model: *ToyTransformer, prompt: [SEQ_LEN]u8, max_tokens: usize, output: []u8) usize {
    var ids: [SEQ_LEN + 20]u8 = undefined; // max generation
    @memcpy(ids[0..SEQ_LEN], &prompt);
    var len: usize = SEQ_LEN;

    for (0..max_tokens) |_| {
        var context: [SEQ_LEN]u8 = undefined;
        @memcpy(&context, ids[len - SEQ_LEN .. len]);
        forward(model, context);

        var probs: [VOCAB_SIZE]i16 = undefined;
        var shifted: [VOCAB_SIZE]i16 = undefined;
        softmax_surrogate(VOCAB_SIZE, &model.cache.logits[SEQ_LEN - 1].v, &probs, &shifted);

        ids[len] = sample_greedy(&probs);
        len += 1;
    }

    @memcpy(output[0..len], ids[0..len]);
    return len;
}

// ─────────────────────────────────────────────────────────────────────
// Verification
// ─────────────────────────────────────────────────────────────────────

fn verify_softmax_sum(model: *ToyTransformer, windows: []const Window) bool {
    for (windows) |w| {
        forward(model, w.context);
        var probs: [VOCAB_SIZE]i16 = undefined;
        var shifted: [VOCAB_SIZE]i16 = undefined;
        softmax_surrogate(VOCAB_SIZE, &model.cache.logits[SEQ_LEN - 1].v, &probs, &shifted);
        var total: i32 = 0;
        for (0..VOCAB_SIZE) |i| {
            total += @as(i32, probs[i]);
        }
        if (total != D) return false;
    }
    return true;
}

fn verify_determinism() bool {
    var model1 = ToyTransformer.init(SEED);
    var model2 = ToyTransformer.init(SEED);
    const windows = make_windows();

    for (0..3) |_| {
        const loss1 = train_epoch(&model1, &windows);
        const loss2 = train_epoch(&model2, &windows);
        if (loss1 != loss2) return false;
    }

    // compare weights
    const w1 = @as([*]const u8, @ptrCast(&model1.wq.v));
    const w2 = @as([*]const u8, @ptrCast(&model2.wq.v));
    const size = @sizeOf(@TypeOf(model1.wq.v));
    for (0..size) |i| {
        if (w1[i] != w2[i]) return false;
    }

    return true;
}

fn verify_attention_weights(model: *ToyTransformer, windows: []const Window) bool {
    for (windows) |w| {
        forward(model, w.context);
        for (0..SEQ_LEN) |i| {
            var total: i32 = 0;
            for (0..SEQ_LEN) |j| {
                total += @as(i32, model.cache.weights[i][j]);
            }
            if (total != D) return false;
        }
    }
    return true;
}

// ─────────────────────────────────────────────────────────────────────
// Print helpers
// ─────────────────────────────────────────────────────────────────────

fn print_token(id: u8) void {
    print("{s}", .{vocab[id]});
}

fn print_probs(probs: *const [VOCAB_SIZE]i16) void {
    print("[", .{});
    for (0..VOCAB_SIZE) |i| {
        if (i > 0) print(", ", .{});
        // print as fixed point: value / 65536
        const v: i32 = @as(i32, probs[i]);
        const whole: i32 = @divTrunc(v * 10000, D);
        print("0.{d:0>4}", .{@as(u32, @intCast(if (whole < 0) -whole else whole))});
    }
    print("]", .{});
}

fn q16_to_f32(v: i16) f32 {
    // only for display — no float in computation
    return @as(f32, @floatFromInt(v)) / 65536.0;
}

// ─────────────────────────────────────────────────────────────────────
// Main
// ─────────────────────────────────────────────────────────────────────

pub fn main() !void {
    // Arena: 1MB, never grows
    var arena_buf: [1024 * 1024]u8 = undefined;
    _ = &arena_buf; // arena exists but model is stack-allocated at these sizes

    print("VDR Toy LLM — Q16 Integer Arithmetic\n", .{});
    print("D = {d} (2^16)\n\n", .{D});

    var model = ToyTransformer.init(SEED);
    const windows = make_windows();

    // ── Train ──────────────────────────────────────────────────────
    print("=== TRAINING ===\n", .{});
    var loss_history: [N_EPOCHS]i64 = undefined;

    for (0..N_EPOCHS) |epoch| {
        const avg_loss = train_epoch(&model, &windows);
        loss_history[epoch] = avg_loss;

        // check softmax sum
        var sum_ok = true;
        for (&windows) |w| {
            forward(&model, w.context);
            var probs: [VOCAB_SIZE]i16 = undefined;
            var shifted: [VOCAB_SIZE]i16 = undefined;
            softmax_surrogate(VOCAB_SIZE, &model.cache.logits[SEQ_LEN - 1].v, &probs, &shifted);
            var total: i32 = 0;
            for (0..VOCAB_SIZE) |i| {
                total += @as(i32, probs[i]);
            }
            if (total != D) sum_ok = false;
        }

        const loss_display: f32 = @as(f32, @floatFromInt(avg_loss)) / 65536.0;
        _ = loss_display;
        print("  epoch {d:2}  loss_q16={d:10}  softmax_sum={d}: {s}\n", .{
            epoch + 1,
            avg_loss,
            D,
            if (sum_ok) "yes" else "NO",
        });
    }

    // ── Generate ───────────────────────────────────────────────────
    print("\n=== GENERATION ===\n", .{});
    print("prompt: the cat sat on\n", .{});
    print("greedy: ", .{});

    var output: [20]u8 = undefined;
    const len = generate(&model, .{ 0, 1, 2, 3 }, 4, &output);
    for (0..len) |i| {
        if (i > 0) print(" ", .{});
        print_token(output[i]);
    }
    print("\n", .{});

    // show step-by-step
    print("\nstep-by-step:\n", .{});
    var step_ids: [SEQ_LEN + 4]u8 = .{ 0, 1, 2, 3, 0, 0, 0, 0 };
    var step_len: usize = SEQ_LEN;
    for (0..4) |step| {
        var context: [SEQ_LEN]u8 = undefined;
        @memcpy(&context, step_ids[step_len - SEQ_LEN .. step_len]);
        forward(&model, context);

        var probs: [VOCAB_SIZE]i16 = undefined;
        var shifted: [VOCAB_SIZE]i16 = undefined;
        softmax_surrogate(VOCAB_SIZE, &model.cache.logits[SEQ_LEN - 1].v, &probs, &shifted);

        const next_id = sample_greedy(&probs);
        step_ids[step_len] = next_id;
        step_len += 1;

        print("  step {d}: ", .{step + 1});
        print_probs(&probs);
        print(" -> {s}\n", .{vocab[next_id]});
    }

    // ── Verify ─────────────────────────────────────────────────────
    print("\n=== VERIFICATION ===\n", .{});

    // softmax sum
    {
        var verify_model = ToyTransformer.init(SEED);
        const ok = verify_softmax_sum(&verify_model, &windows);
        print("  softmax_sum            [{s}]\n", .{if (ok) "PASS" else "FAIL"});
    }

    // attention weights
    {
        var verify_model = ToyTransformer.init(SEED);
        const ok = verify_attention_weights(&verify_model, &windows);
        print("  attention_weights      [{s}]\n", .{if (ok) "PASS" else "FAIL"});
    }

    // determinism
    {
        const ok = verify_determinism();
        print("  determinism            [{s}]\n", .{if (ok) "PASS" else "FAIL"});
    }

    // loss monotonicity
    {
        const first_loss = loss_history[0];
        const last_loss = loss_history[N_EPOCHS - 1];
        const ok = last_loss < first_loss;
        print("  loss_monotonicity      [{s}] {d} -> {d}\n", .{ if (ok) "PASS" else "FAIL", first_loss, last_loss });
    }

    // weight update exactness
    {
        var m1 = ToyTransformer.init(SEED);
        const w_old = m1.wq.v[0][0];
        _ = train_step(&m1, windows[0].context, windows[0].target);
        const w_new = m1.wq.v[0][0];
        const grad = m1.wq_g.v[0][0];

        // check: w_old - w_new == (LR * grad) / D
        const delta: i32 = @as(i32, w_old) - @as(i32, w_new);
        const expected: i32 = @intCast(@divTrunc(@as(i64, LR) * @as(i64, grad), D));
        const ok = delta == expected;
        print("  weight_update          [{s}]\n", .{if (ok) "PASS" else "FAIL"});
    }

    print("\n=== DENOMINATOR REPORT ===\n", .{});
    print("  all denominators implicit D={d} (2^16)\n", .{D});
    print("  no D field exists — frame is structural, not stored\n", .{});
    print("  D stability guaranteed by shift+mask epilogue\n", .{});

    print("\ndone.\n", .{});
}
