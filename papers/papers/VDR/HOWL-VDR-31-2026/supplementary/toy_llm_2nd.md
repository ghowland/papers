# Small-Integer VDR Toy LLM — Function Specs and Turn Plan

## File 1: `config.py`

```python
"""All hyperparameters and frame constants."""

# D-frames (power-of-two denominators)
D_WEIGHT = 128        # weight storage: i8-scale
D_ACT = 128           # activations: i8-scale
D_SCORE = 256         # attention scores: i8×i8
D_PROB = 256          # softmax output: probability resolution
D_ACC = 32768         # accumulator: i16-scale dot product sums
D_GRAD = 32768        # gradients: i16-scale
D_OPT = 32768         # optimizer state: i16-scale

# Model shape
VOCAB_SIZE = 5
DIM = 4
SEQ_LEN = 4
FFN_DIM = 8
N_HEADS = 1

# Training
N_EPOCHS = 20
LR = VDR(1, 128)      # learning rate in weight frame
INIT_DENOM = 128       # weight init denominator = D_WEIGHT
SEED = 42

CORPUS = "the cat sat on the mat"
```

## File 2: `data.py`

No changes from current. Same 7 functions:

```
build_vocab(corpus) -> dict
    I: text string
    O: {token: id} ordered by first appearance

invert_vocab(vocab) -> dict
    I: vocab dict
    O: {id: token}

tokenize(text, vocab) -> list[int]
    I: text string, vocab dict
    O: token id list

detokenize(ids, inv_vocab) -> str
    I: id list, inverse vocab
    O: space-joined text

make_windows(ids, seq_len) -> list[(list[int], int)]
    I: full token sequence, context length
    O: list of (context_ids, target_id)

one_hot_target(target_id, vocab_size) -> Vec
    I: target index, vocab size
    O: Vec with VDR(1) at target, VDR(0) elsewhere

build_dataset(corpus, seq_len) -> (windows, vocab, inv_vocab, vocab_size)
    I: corpus string, sequence length
    O: complete dataset tuple
```

## File 3: `frames.py` (NEW)

Central rebase utilities. Every layer boundary calls these.

```
rebase_value(x, target_d) -> VDR
    I: VDR value, target denominator (int, power of two)
    O: VDR rebased to target_d frame
    divmod keeps D fixed, overflow to R

rebase_vec(v, target_d) -> Vec
    I: Vec of VDR values, target denominator
    O: new Vec with every element rebased

rebase_mat(m, target_d) -> Mat
    I: Mat of VDR values, target denominator
    O: new Mat with every element rebased

rebase_params(params, target_d) -> None
    I: list of parameter objects, target denominator
    O: None
    S: mutates each param.value in place via rebase

rebase_grads(params, target_d) -> None
    I: list of parameter objects, target denominator
    O: None
    S: mutates each param.grad in place via rebase

init_weight_vec(dim, denom, seed, idx) -> Vec
    I: dimension, denominator (D_WEIGHT), rng seed, index offset
    O: Vec with small-integer numerators in D_WEIGHT frame
    values are VDR(k, denom) where k from deterministic RNG in [-denom+1, denom-1]

init_weight_mat(rows, cols, denom, seed, idx) -> Mat
    I: matrix shape, denominator, seed, index offset
    O: Mat with small-integer numerators in D_WEIGHT frame

zero_vec(dim) -> Vec
    I: dimension
    O: Vec of VDR(0) values

frame_check(x, expected_d) -> bool
    I: VDR value, expected denominator
    O: True if x.d == expected_d (for closed) or x is zero
    diagnostic helper — asserts frame discipline is maintained

frame_check_vec(v, expected_d) -> bool
    I: Vec, expected denominator
    O: True if all elements pass frame_check
```

## File 4: `model.py`

```
class ToyTransformer:

    __init__(self, seed=None)
        I: optional seed (default from config)
        S: initializes all 226 parameters in D_WEIGHT=128 frame
           token_emb: list of 5 Vec in D_WEIGHT
           pos_emb: list of 4 Vec in D_WEIGHT
           Wq, Wk, Wv, Wo: Linear layers, weights in D_WEIGHT
           ffn_l1, ffn_l2: Linear layers, weights in D_WEIGHT
           output_proj: Linear layer, weights in D_WEIGHT
           relu: ReLU
           _cache: dict for backward

    embed(self, token_ids) -> list[Vec]
        I: list of token ids
        O: list of Vec in D_ACT frame
        lookup token_emb + pos_emb, rebase sum to D_ACT

    attention_block(self, xs) -> list[Vec]
        I: list of Vec in D_ACT frame
        O: list of Vec in D_ACT frame
        Wq/Wk/Wv project -> rebase to D_SCORE
        scores = Q dot K -> in D_ACC, rebase to D_SCORE
        softmax_surrogate -> D_PROB, sums to exactly 1
        value mix -> D_ACC, rebase to D_ACT
        Wo project -> rebase to D_ACT

    attention_block_with_cache(self, xs) -> (list[Vec], dict)
        I: list of Vec in D_ACT frame
        O: (output in D_ACT, cache dict with all intermediates)
        same as attention_block but caches Q, K, V, scores, weights, attn_out

    ffn_block(self, x) -> Vec
        I: Vec in D_ACT frame
        O: Vec in D_ACT frame
        ffn_l1 -> D_ACC, rebase to D_ACT
        relu (no frame change)
        ffn_l2 -> D_ACC, rebase to D_ACT

    forward(self, token_ids) -> list[Vec]
        I: list of token ids
        O: list of logit Vec in D_ACT frame
        embed -> attention + residual -> FFN + residual -> output_proj

    forward_with_cache(self, token_ids) -> (list[Vec], dict)
        I: token ids
        O: (logits, full cache dict)

    forward_last_logits(self, token_ids) -> Vec
        I: token ids
        O: last position logits Vec

    forward_last_logits_with_cache(self, token_ids) -> (Vec, dict)
        I: token ids
        O: (last logits, cache)

    parameters(self) -> list
        O: flat list of all trainable parameter objects

    zero_grad(self) -> None
        S: zeros all parameter gradients

    backward_from_output(self, grad_logits) -> None
        I: list of Vec — gradient per position logits
        S: accumulates gradients into all parameters
        requires forward_with_cache called first

    backward_from_last(self, grad) -> None
        I: Vec — gradient for last position only
        S: wraps backward_from_output with zeros for other positions
```

## File 5: `attention_backward.py`

Same 4 functions, no changes to signatures or logic. Gradients emerge in whatever frame the cached values are in. Rebase happens in train.py after full backward.

```
softmax_surrogate_backward(grad_probs, probs, shifted) -> Vec
    I: grad w.r.t. surrogate output, output probs, shifted input values
    O: grad w.r.t. surrogate input scores
    backward through (z-m+c)^2 / sum((z-m+c)^2)

attention_mix_backward(grad_out, weights, V) -> (list[Vec], list[Vec])
    I: grad w.r.t. mix output, cached weights, cached V
    O: (grad_weights, grad_V)

score_backward(grad_scores, Q, K) -> (list[Vec], list[Vec])
    I: grad w.r.t. scores, cached Q, cached K
    O: (grad_Q, grad_K)

attention_backward(grad_projected, Q, K, V, weights, shifted,
                   Wq, Wk, Wv, Wo, xs_input) -> list[Vec]
    I: all cached attention intermediates + layer references
    O: grad w.r.t. attention block input
    S: accumulates into Wq, Wk, Wv, Wo parameter gradients
```

Note: `softmax_backward` becomes `softmax_surrogate_backward` — different math. Surrogate is `s_i = (z_i - m + c)^2 / sum((z_j - m + c)^2)`. Backward is chain rule through square and normalization. Simpler than Taylor exp backward. The `shifted` values (z - m + c) are cached during forward for use here.

## File 6: `train.py`

```
mse_loss(pred, target) -> VDR
    I: pred Vec, target Vec
    O: exact MSE as VDR scalar

mse_loss_grad(pred, target) -> Vec
    I: pred Vec, target Vec
    O: gradient of MSE w.r.t. pred

surrogate_softmax_then_mse(logits, target_vec) -> (probs, loss, grad_logits)
    I: logits Vec in D_ACT, target one-hot Vec
    O: probs in D_PROB (sums to exactly 1), loss as VDR, grad w.r.t. logits
    uses surrogate softmax, not Taylor exp

train_step(model, context_ids, target_id, optimizer) -> (loss, probs)
    I: model, context, target, optimizer
    O: (exact loss, exact probs)
    S: forward_with_cache -> loss -> backward -> rebase_grads to D_GRAD -> step -> rebase_params to D_WEIGHT

train_epoch(model, windows, optimizer) -> list[(loss, probs)]
    I: model, window list, optimizer
    O: per-window results

average_loss(results) -> VDR
    I: list of (loss, probs)
    O: exact average

train(n_epochs, model, verbose) -> (model, loss_history)
    I: epochs, optional model, verbose flag
    O: trained model + list of exact loss per epoch
    creates optimizer, runs epochs, verifies softmax sum each epoch

quick_train(n_epochs) -> (model, losses)
    convenience: fewer epochs, verbose

train_silent(n_epochs, model) -> (model, losses)
    convenience: no printing
```

## File 7: `generate.py`

Minimal changes — surrogate softmax instead of Taylor, rebase at output.

```
sample_categorical(probs, rng) -> int
    I: probs Vec (sums to exactly 1), deterministic RNG
    O: sampled index via exact CDF comparison

sample_greedy(probs) -> int
    I: probs Vec
    O: argmax index (exact comparison, ties to lowest index)

sample_top_k(probs, k, rng) -> int
    I: probs Vec, k, RNG
    O: sampled from top-k with exact renormalization summing to 1

sample_nucleus(probs, p_threshold, rng) -> int
    I: probs Vec, threshold VDR, RNG
    O: sampled from nucleus set with exact renormalization

generate_ids(model, prompt_ids, max_tokens, strategy, seed, top_k, top_p) -> list[int]
    I: model, prompt, generation config
    O: prompt_ids + generated ids

generate_text(model, prompt, max_tokens, strategy, ...) -> str
    I: model, text prompt, config
    O: full generated text

tokenize_safe(text, vocab) -> list[int]
    I: text, vocab
    O: ids or ValueError

generate_greedy(model, prompt, max_tokens) -> str
generate_sampled(model, prompt, max_tokens, seed) -> str
generate_top_k_text(model, prompt, max_tokens, k, seed) -> str
generate_nucleus_text(model, prompt, max_tokens, p, seed) -> str
    convenience wrappers

show_generation(model, prompt, max_tokens, strategy, ...) -> str
    I: model, prompt, config
    O: generated text
    S: prints each step with exact probabilities
```

## File 8: `verify.py`

Same 8 tests plus verify_all. One addition: frame discipline check.

```
verify_softmax_sum(model, windows) -> (bool, str)
    every softmax output sums to exactly VDR(1)

verify_gradient_correctness(model) -> (bool, str)
    autodiff vs numerical discrete derivative, both exact

verify_weight_update(model) -> (bool, str)
    (w_old - w_new) / lr == grad exactly

verify_deterministic(n_epochs) -> (bool, str)
    two runs from same seed produce bit-identical results

verify_loss_monotonicity(n_epochs, model) -> (bool, str)
    final loss < initial loss

verify_attention_weights(model) -> (bool, str)
    every attention weight row sums to exactly 1

verify_forward_backward_roundtrip() -> (bool, str)
    train one step twice from same init, bit-identical

verify_checkpoint_roundtrip(model) -> (bool, str)
    save -> perturb -> load -> bit-identical

verify_frame_discipline(model) -> (bool, str)        # NEW
    after forward pass, check all intermediates are in expected D-frames
    weights in D_WEIGHT, activations in D_ACT, scores in D_SCORE, etc.

verify_all(model, verbose) -> (bool, results)
    runs all 9 tests, prints summary
```

## File 9: `inspect.py`

Same functions. `denominator_report` becomes more useful — should confirm all denominators are 128/256/32768, not growing.

```
print_parameters(model, max_per_layer) -> None
print_embeddings(model) -> None
print_attention_map(model, context_ids) -> None
print_logits_and_probs(model, context_ids) -> None
print_gradient_magnitudes(model, context_ids, target_id) -> None
print_loss_trajectory(losses) -> None
denominator_report(model) -> None
    confirms all parameter denominators are D_WEIGHT=128
full_inspection(model, losses) -> None
```

## File 10: `run.py`

Same structure, same 5 modes.

```
run_train(verbose) -> (model, losses)
run_generate(model) -> None
run_verify(model) -> bool
run_inspect(model, losses) -> None
main() -> None
    argv dispatch: train | generate | verify | inspect | all
```

---

# Turn Plan

## Turn 1 — Foundation: config.py + data.py + frames.py + model.py

- `config.py` (~25 lines) — frame constants, model shape, training config
- `data.py` (~80 lines) — unchanged from current, copy with minor cleanup
- `frames.py` (~120 lines) — rebase_value, rebase_vec, rebase_mat, rebase_params, rebase_grads, init_weight_vec, init_weight_mat, zero_vec, frame_check, frame_check_vec
- `model.py` (~450 lines) — ToyTransformer with init in D_WEIGHT frame, embed with rebase to D_ACT, attention_block with frame transitions at every boundary, ffn_block with frame transitions, forward, forward_with_cache, forward_last_logits, parameters, zero_grad, backward_from_output, backward_from_last

~675 lines.

## Turn 2 — Backward + Training + Generation: attention_backward.py + train.py + generate.py

- `attention_backward.py` (~220 lines) — softmax_surrogate_backward, attention_mix_backward, score_backward, attention_backward (passes `shifted` values through for surrogate backward)
- `train.py` (~200 lines) — mse_loss, mse_loss_grad, surrogate_softmax_then_mse, train_step with rebase_grads and rebase_params calls, train_epoch, average_loss, train, quick_train, train_silent
- `generate.py` (~250 lines) — all sampling functions, generate_ids, generate_text, tokenize_safe, 4 convenience wrappers, show_generation

~670 lines.

## Turn 3 — Verification + Inspection + Entry: verify.py + inspect.py + run.py

- `verify.py` (~350 lines) — all 9 tests including new verify_frame_discipline, verify_all
- `inspect.py` (~180 lines) — all inspection functions, denominator_report now confirms small fixed frames
- `run.py` (~80 lines) — main entry point with 5 modes

~610 lines.

## Summary

| Turn | Files | Est. Lines |
|---|---|---|
| 1 | config.py, data.py, frames.py, model.py | ~675 |
| 2 | attention_backward.py, train.py, generate.py | ~670 |
| 3 | verify.py, inspect.py, run.py | ~610 |
| **Total** | **10 files** | **~1955** |

3 turns. Expected runtime after rewrite: under 10 seconds for full `run.py all` on a 2019 laptop.

---

