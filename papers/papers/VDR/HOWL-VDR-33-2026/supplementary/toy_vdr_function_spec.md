# Toy LLM — Complete Function Specification

## File: `examples/toy_llm/data.py`

```
Module: data preparation for toy LLM.
No VDR needed here — pure Python tokenization.
VDR enters only when we create one-hot vectors.
```

### Globals

```python
CORPUS = "the cat sat on the mat"
```

### Functions

**`build_vocab(corpus: str) -> dict[str, int]`**
- I: text string
- O: dict mapping words to integer ids, ordered by first appearance
- `build_vocab("the cat sat on the mat")` → `{"the": 0, "cat": 1, "sat": 2, "on": 3, "mat": 4}`

**`invert_vocab(vocab: dict) -> dict[int, str]`**
- I: vocab dict
- O: reversed dict {id: word}

**`tokenize(text: str, vocab: dict) -> list[int]`**
- I: text, vocab
- O: list of token ids
- `tokenize("the cat sat", vocab)` → `[0, 1, 2]`

**`detokenize(ids: list[int], inv_vocab: dict) -> str`**
- I: token ids, inverse vocab
- O: space-joined text

**`make_windows(ids: list[int], seq_len: int) -> list[tuple[list[int], int]]`**
- I: full token id sequence, context length
- O: list of (context_ids, target_id) pairs
- `make_windows([0,1,2,3,0,4], 4)` → `[([0,1,2,3], 0), ([1,2,3,0], 4)]`

**`one_hot_target(target_id: int, vocab_size: int) -> Vec`**
- I: target index, vocabulary size
- O: Vec with VDR(1) at target index, VDR(0) elsewhere

**`build_dataset(corpus: str, seq_len: int) -> tuple`**
- I: corpus text, sequence length
- O: (windows, vocab, inv_vocab, vocab_size)
- Convenience function combining all above

---

## File: `examples/toy_llm/config.py`

```
Module: all hyperparameters in one place.
Every numeric value is a VDR or int. No float.
```

### Globals

```python
VOCAB_SIZE = 5        # number of unique tokens
DIM = 4               # embedding and hidden dimension
SEQ_LEN = 4           # context window length
FFN_DIM = 8           # feed-forward hidden dimension
N_HEADS = 1           # attention heads
N_EPOCHS = 20         # training epochs
LR = VDR(1, 100)      # learning rate: exact 1/100
INIT_DENOM = 10       # denominator for weight initialization
SEED = 42             # deterministic seed
EXP_DEPTH = 12        # Taylor depth for softmax exp
```

---

## File: `examples/toy_llm/model.py`

```
Module: ToyTransformer — 1-layer decoder-only transformer.
All components from vdr.ml and vdr.linalg.
```

### Class: `ToyTransformer`

**`__init__(self, config)`**
- I: config object or module with VOCAB_SIZE, DIM, etc.
- S: initializes all parameters with deterministic rational weights
- Components created:
  - `self.token_emb`: list of Vec, one per vocab token (VOCAB_SIZE × DIM)
  - `self.pos_emb`: list of Vec, one per position (SEQ_LEN × DIM)
  - `self.Wq`: Linear(DIM, DIM)
  - `self.Wk`: Linear(DIM, DIM)
  - `self.Wv`: Linear(DIM, DIM)
  - `self.Wo`: Linear(DIM, DIM)
  - `self.ffn_l1`: Linear(FFN_DIM, DIM)
  - `self.ffn_l2`: Linear(DIM, FFN_DIM)
  - `self.relu`: ReLU()
  - `self.output_proj`: Linear(VOCAB_SIZE, DIM)

**`embed(self, token_ids: list[int]) -> list[Vec]`**
- I: list of token ids, length ≤ SEQ_LEN
- O: list of Vec, each token_emb[id] + pos_emb[position]
- Exact addition, no drift

**`attention_block(self, xs: list[Vec]) -> list[Vec]`**
- I: list of hidden state Vec
- O: list of attended Vec (same length)
- Steps:
  1. Q = [Wq.forward(x) for x in xs]
  2. K = [Wk.forward(x) for x in xs]
  3. V = [Wv.forward(x) for x in xs]
  4. attn_out = self_attention(Q, K, V, causal=True, exp_depth=EXP_DEPTH)
  5. projected = [Wo.forward(a) for a in attn_out]
  6. return projected
- Every attention weight row sums to exactly 1

**`ffn_block(self, x: Vec) -> Vec`**
- I: single hidden state Vec
- O: FFN output Vec
- Steps: ffn_l1.forward(x) → relu.forward → ffn_l2.forward
- Per-position, not cross-position

**`forward(self, token_ids: list[int]) -> list[Vec]`**
- I: token ids
- O: list of logit Vec, one per position
- Steps:
  1. xs = self.embed(token_ids)
  2. attn = self.attention_block(xs)
  3. xs = [attn[i] + xs[i] for i in range(len(xs))]  # residual
  4. ffn_out = [self.ffn_block(x) for x in xs]
  5. xs = [ffn_out[i] + xs[i] for i in range(len(xs))]  # residual
  6. logits = [self.output_proj.forward(x) for x in xs]
  7. return logits

**`forward_last_logits(self, token_ids: list[int]) -> Vec`**
- I: token ids
- O: logit Vec for last position only
- Calls forward, returns logits[-1]

**`parameters(self) -> list`**
- O: flat list of all VecParam and MatParam from all layers

**`zero_grad(self)`**
- S: zeros all parameter gradients

**`backward_from_output(self, grad_output: list[Vec]) -> None`**
- I: gradient of loss w.r.t. each position's logits
- S: backpropagates through entire model, accumulates into parameter grads
- Steps (reverse of forward):
  1. grad through output_proj.backward for each position
  2. split residual gradient (additive: grad passes to both branches)
  3. grad through ffn_l2.backward, relu.backward, ffn_l1.backward per position
  4. split residual gradient
  5. grad through attention backward (Wo, then attention weights, then Wq/Wk/Wv)
  6. grad to embedding (not updated in v1 — fixed embeddings)

**`backward_from_last(self, grad: Vec) -> None`**
- I: gradient of loss w.r.t. last position logits only
- S: wraps grad in a list with zeros for other positions, calls backward_from_output
- Simpler interface for next-token prediction training

---

## File: `examples/toy_llm/attention_backward.py`

```
Module: backward pass through self-attention.
Separated because attention backward is the most complex component.
```

### Functions

**`attention_backward(grad_out: list[Vec], Q: list[Vec], K: list[Vec], V: list[Vec], weights: list[Vec], Wq: Linear, Wk: Linear, Wv: Linear, Wo: Linear) -> list[Vec]`**
- I: gradient from above (list of Vec, one per position), cached forward values (Q, K, V, attention weights), projection layers
- O: gradient w.r.t. input hidden states (list of Vec)
- S: accumulates gradients into Wq, Wk, Wv, Wo parameters
- Steps:
  1. Backprop through Wo: grad_attn = [Wo.backward(g) for g in grad_out]
  2. Backprop through weighted sum: grad_weights, grad_V from attention_mix_backward
  3. Backprop through softmax: grad_scores from softmax_backward
  4. Backprop through score computation: grad_Q, grad_K
  5. Backprop through projections: Wq.backward, Wk.backward, Wv.backward
  6. Sum gradients to get grad w.r.t. input

**`softmax_backward(grad_probs: Vec, probs: Vec) -> Vec`**
- I: gradient w.r.t. softmax output, softmax output (probabilities)
- O: gradient w.r.t. softmax input (scores)
- Formula: `grad_score[j] = probs[j] * (grad_probs[j] - sum_k(grad_probs[k] * probs[k]))`
- All exact VDR arithmetic

**`attention_mix_backward(grad_out: list[Vec], weights: list[Vec], V: list[Vec]) -> tuple[list[Vec], list[Vec]]`**
- I: gradient from above, attention weights, value vectors
- O: (grad_weights, grad_V) — gradients w.r.t. weights and values
- grad_weights[i][j] = grad_out[i] . V[j]
- grad_V[j] = sum_i weights[i][j] * grad_out[i]

**`score_backward(grad_scores: list[Vec], Q: list[Vec], K: list[Vec]) -> tuple[list[Vec], list[Vec]]`**
- I: gradient w.r.t. scores, query and key vectors
- O: (grad_Q, grad_K)
- grad_Q[i] = sum_j grad_scores[i][j] * K[j]
- grad_K[j] = sum_i grad_scores[i][j] * Q[i]

---

## File: `examples/toy_llm/train.py`

```
Module: training loop.
```

### Functions

**`compute_loss(model, context_ids: list[int], target_id: int, vocab_size: int) -> tuple[VDR, Vec]`**
- I: model, context token ids, target token id, vocab size
- O: (loss, grad) — MSE loss as VDR, gradient w.r.t. logits as Vec
- Steps:
  1. logits = model.forward_last_logits(context_ids)
  2. probs = softmax(logits, exp_depth=EXP_DEPTH)
  3. target = one_hot_target(target_id, vocab_size)
  4. loss = mse(probs, target)
  5. grad = mse_grad(probs, target)
  6. return (loss, grad)

**`train_step(model, context_ids: list[int], target_id: int, vocab_size: int, optimizer) -> VDR`**
- I: model, data, optimizer
- O: loss value as VDR
- S: forward, loss, backward, optimizer step, zero grad
- Steps:
  1. loss, grad = compute_loss(model, context_ids, target_id, vocab_size)
  2. model.backward_from_last(grad)
  3. optimizer.step()
  4. model.zero_grad()
  5. return loss

**`train_epoch(model, dataset: list[tuple], vocab_size: int, optimizer) -> list[VDR]`**
- I: model, list of (context_ids, target_id) windows, vocab size, optimizer
- O: list of per-sample losses
- Iterates train_step over all windows

**`train(n_epochs: int = 20) -> tuple`**
- I: number of epochs
- O: (model, epoch_losses) where epoch_losses is list of list of VDR
- Steps:
  1. Build dataset from CORPUS
  2. Initialize model with SEED
  3. Create SGD optimizer
  4. For each epoch: train_epoch, print total loss as fraction
  5. Return trained model and loss history

---

## File: `examples/toy_llm/generate.py`

```
Module: autoregressive text generation.
```

### Functions

**`generate_ids(model, prompt_ids: list[int], max_tokens: int, vocab_size: int, seed: int = 1, temperature: VDR = None) -> list[int]`**
- I: trained model, prompt token ids, max new tokens, vocab size, RNG seed, optional temperature
- O: list of all token ids (prompt + generated)
- Steps:
  1. Create VDRRandom(seed)
  2. ids = list(prompt_ids)
  3. For each new token:
     a. context = ids[-SEQ_LEN:]
     b. logits = model.forward_last_logits(context)
     c. if temperature: logits = temperature_scale(logits, temperature)
     d. probs = softmax(logits, exp_depth=EXP_DEPTH)
     e. next_id = categorical_sample(probs, rng)
     f. ids.append(next_id)
  4. return ids

**`generate_text(model, prompt: str, max_tokens: int, vocab: dict, inv_vocab: dict, seed: int = 1) -> str`**
- I: model, prompt text, max tokens, vocab, inverse vocab, seed
- O: generated text string
- Tokenizes prompt, calls generate_ids, detokenizes result

**`generate_greedy(model, prompt_ids: list[int], max_tokens: int, vocab_size: int) -> list[int]`**
- I: model, prompt, max tokens, vocab size
- O: token ids using argmax (no randomness)
- Deterministic decoding — always picks highest probability token

**`generate_top_k(model, prompt_ids: list[int], max_tokens: int, vocab_size: int, k: int = 3, seed: int = 1) -> list[int]`**
- I: model, prompt, max tokens, vocab size, k, seed
- O: token ids sampled from top-k filtered distribution
- Each filtered distribution sums to exactly 1

---

## File: `examples/toy_llm/verify.py`

```
Module: exact verification of every pipeline property.
```

### Functions

**`verify_softmax_sum(model, dataset: list[tuple], vocab_size: int) -> bool`**
- I: model, dataset, vocab size
- O: True if softmax output sums to exactly VDR(1) for every sample
- For each (context, target): forward, softmax, assert sum == VDR(1)

**`verify_attention_weights_sum(model, dataset: list[tuple]) -> bool`**
- I: model, dataset
- O: True if every attention weight row sums to exactly VDR(1)
- Requires forward_with_cache to capture intermediate attention weights

**`verify_gradient_correctness(model, context_ids: list[int], target_id: int, vocab_size: int, h: VDR = None) -> list[tuple[str, VDR]]`**
- I: model, single sample, vocab size, finite difference step h
- O: list of (param_name, max_discrepancy) tuples
- For each parameter scalar:
  1. Compute autodiff gradient (from backward pass)
  2. Compute numerical gradient: (loss(w+h) - loss(w-h)) / (2h)
  3. Compare — both are exact rationals
- With small enough h, should agree closely. Discrepancy is exact.

**`verify_weight_update(model, context_ids: list[int], target_id: int, vocab_size: int, lr: VDR) -> bool`**
- I: model, single sample, vocab size, learning rate
- O: True if w_new == w_old - lr * grad exactly
- Steps:
  1. Save all parameter values
  2. Forward, backward, step
  3. For each parameter: verify (w_old - w_new) / lr == grad

**`verify_deterministic(corpus: str, seq_len: int, seed: int, n_epochs: int = 3) -> bool`**
- I: corpus, seq_len, seed, epochs
- O: True if two independent runs produce identical loss sequences
- Run train twice from scratch with same seed, compare every loss value with ==

**`verify_loss_decrease(losses: list[list[VDR]]) -> bool`**
- I: epoch losses from training
- O: True if total loss per epoch is non-increasing (via exact comparison)
- Note: with small enough lr and enough data, loss should decrease. May not be monotone per sample.

**`verify_checkpoint_roundtrip(model) -> bool`**
- I: trained model
- O: True if save_model → load_model_parameters produces identical parameters
- Steps:
  1. Save model state
  2. Create fresh model
  3. Load saved state
  4. Compare every parameter with ==

**`verify_generation_deterministic(model, prompt_ids: list[int], vocab_size: int, seed: int) -> bool`**
- I: model, prompt, vocab size, seed
- O: True if two calls to generate_ids with same seed produce identical output

**`verify_all(model, dataset, vocab_size) -> dict[str, bool]`**
- I: trained model, dataset, vocab size
- O: dict of test names to pass/fail booleans
- Runs all verification functions, prints summary table

---

## File: `examples/toy_llm/inspect.py`

```
Module: tools for inspecting exact model internals.
```

### Functions

**`print_parameters(model) -> None`**
- S: prints every parameter name, shape, and sample values as fractions

**`print_attention_map(model, token_ids: list[int], vocab: dict) -> None`**
- S: forward pass, capture attention weights, print as fraction grid
- Shows exactly which tokens attend to which, with exact rational weights

**`print_logits_and_probs(model, token_ids: list[int], vocab: dict) -> None`**
- S: forward pass, softmax, print logits and probabilities per position
- Each probability is an exact fraction

**`print_gradient_magnitudes(model) -> None`**
- S: after backward pass, print gradient norms per parameter

**`print_loss_trajectory(losses: list[list[VDR]]) -> None`**
- S: prints each epoch's total loss as exact fraction and approximate decimal

**`denominator_report(model) -> None`**
- S: prints denominator complexity statistics for all parameters
- Shows how denominators grow during training

---

## File: `examples/toy_llm/run.py`

```
Module: main entry point that ties everything together.
```

### Functions

**`main() -> None`**
- Steps:
  1. Print config
  2. Build dataset
  3. Initialize model
  4. Train for N_EPOCHS
  5. Print loss trajectory
  6. Run verify_all
  7. Generate text from prompt
  8. Print attention map for a sample
  9. Print denominator report
  10. Save checkpoint

**Expected output:**
```
=== VDR Toy LLM ===
Config: vocab=5, dim=4, seq_len=4, ffn_dim=8, lr=1/100

Training:
  Epoch  1: loss = 347/2160
  Epoch  2: loss = 291/2160
  ...
  Epoch 20: loss = 43/2160

Verification:
  softmax_sum:           PASS (all exactly 1)
  attention_weights_sum: PASS (all exactly 1)
  weight_update:         PASS (exact)
  deterministic:         PASS (bit-identical)
  checkpoint_roundtrip:  PASS (exact)
  generation_deterministic: PASS (same output)
  6/6 passed

Generation (prompt="the cat"):
  the cat sat on the cat sat on the cat

Attention map at "the cat sat on":
       the   cat   sat    on
  the  1/1   0/1   0/1   0/1
  cat  3/7   4/7   0/1   0/1
  sat  1/5   2/5   2/5   0/1
  on   1/9   2/9   3/9   3/9

Denominator complexity after 20 epochs:
  Wq: max denom 1200 digits
  Wk: max denom 1180 digits
  ...
```

---

## Build Order

| Phase | Files | Tests | Depends On |
|---|---|---|---|
| 1 | config.py, data.py | vocab, windows correct | nothing |
| 2 | model.py (forward only) | shapes correct, softmax sums to 1 | vdr.ml.* |
| 3 | attention_backward.py | gradient shapes correct | model.py |
| 4 | model.py (add backward) | full backward works | attention_backward.py |
| 5 | train.py | loss decreases over epochs | model.py |
| 6 | generate.py | produces valid ids, deterministic | model.py |
| 7 | verify.py | all 6 checks pass | train.py, generate.py |
| 8 | inspect.py | prints without error | model.py |
| 9 | run.py | end-to-end | everything |

---

## Key Invariants to Maintain

1. **No float anywhere.** Every number is VDR. LR is VDR(1, 100), not 0.01.

2. **Softmax sums to exactly 1.** Verified at every forward pass.

3. **Attention weight rows sum to exactly 1.** Verified at every forward pass.

4. **Loss is an exact fraction.** Printable as numerator/denominator.

5. **Same seed = same result.** On any platform, any Python version.

6. **All parameters inspectable.** Every weight is an exact fraction you can print.

7. **Gradients are exact.** No numerical differentiation in the backward pass.

8. **Checkpoint roundtrip is exact.** Save → load → identical parameters.
