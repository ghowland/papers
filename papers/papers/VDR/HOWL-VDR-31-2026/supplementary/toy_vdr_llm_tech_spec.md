# VDR Toy LLM — Technical Specification

## Goal

Build the smallest possible language model that actually trains and generates text, using only VDR exact arithmetic. No float anywhere. Every weight, every gradient, every attention score, every softmax probability is an exact rational.

This proves the complete pipeline works end-to-end and serves as exact ground truth for verifying float implementations.

---

## Architecture

**Model:** 1-layer transformer decoder (GPT-style), causal attention.

**Dimensions:**
- Vocabulary: 16 tokens (single characters from a tiny corpus)
- Embedding dimension: 4
- Sequence length: 4 tokens
- Attention heads: 1
- FFN hidden dimension: 8
- Total parameters: ~200 scalars

This is deliberately tiny. The point is not performance — it's proving the pipeline is exact.

---

## Data

A single sentence repeated:

```
"the cat sat on the mat"
```

Tokenized character-by-character or word-by-word. Word-level is simpler:

```python
vocab = {"the": 0, "cat": 1, "sat": 2, "on": 3, "mat": 4, "<pad>": 5}
# 6 tokens, embedding dim 4, seq_len 4
```

Training windows:
```
["the", "cat", "sat", "on"]  -> target: "the"
["cat", "sat", "on", "the"]  -> target: "mat"
```

---

## Components (all from vdr-math library)

### 1. Embedding Table

```python
from vdr.ml.transformer import Embedding
from vdr.ml.init import rational_uniform_mat

# 6 tokens x 4 dimensions
emb_table = rational_uniform_mat(6, 4, denom=10, seed=42)
embedding = Embedding([Vec([emb_table[i, j] for j in range(4)]) for i in range(6)])
```

### 2. Positional Encoding

Fixed rational positional encoding. No sin/cos needed for 4 positions — just learnable or fixed rational vectors.

```python
pos_table = rational_uniform_mat(4, 4, denom=10, seed=43)
```

Add position to embedding: `x[i] = embedding[token_id] + pos[i]`

### 3. Self-Attention (Single Head)

```python
from vdr.ml.nn import Linear
from vdr.ml.attention import self_attention

# Q, K, V projections: 4 -> 4
Wq = Linear(xavier_like_mat(4, 4, denom=10, seed=44), zero_bias(4))
Wk = Linear(xavier_like_mat(4, 4, denom=10, seed=45), zero_bias(4))
Wv = Linear(xavier_like_mat(4, 4, denom=10, seed=46), zero_bias(4))
Wo = Linear(xavier_like_mat(4, 4, denom=10, seed=47), zero_bias(4))
```

Forward:
```
Q = [Wq(x_i) for each position i]
K = [Wk(x_i) for each position i]
V = [Wv(x_i) for each position i]
attn_out = self_attention(Q, K, V, causal=True)
projected = [Wo(a_i) for each position i]
```

Every attention weight row sums to exactly 1 via exact softmax.

### 4. Residual Connection

```python
h = [projected[i] + x[i] for i in range(seq_len)]
```

Exact addition. No drift.

### 5. Feed-Forward Network

```python
from vdr.ml.nn import Linear, ReLU

ffn_l1 = Linear(xavier_like_mat(8, 4, denom=10, seed=48), zero_bias(8))
ffn_l2 = Linear(xavier_like_mat(4, 8, denom=10, seed=49), zero_bias(4))
relu = ReLU()

# Forward per position:
# h_i -> ffn_l1 -> relu -> ffn_l2 -> + h_i (residual)
```

### 6. Output Projection

```python
# Project from dim 4 to vocab size 6
output_proj = Linear(xavier_like_mat(6, 4, denom=10, seed=50), zero_bias(6))
```

### 7. Softmax + Loss

```python
from vdr.ml.softmax import softmax
from vdr.ml.losses import mse, mse_grad

logits = output_proj.forward(h[-1])  # last position predicts next token
probs = softmax(logits)              # sums to exactly 1
target = one_hot(target_id, 6)       # exact: 1 at target, 0 elsewhere
loss = mse(probs, target)            # exact rational loss
```

### 8. Backward Pass

Manual backprop through the chain. Each layer's `backward()` returns exact gradients.

```python
grad = mse_grad(probs, target)
grad = output_proj.backward(grad)
# ... back through FFN, residual, attention, embedding
```

### 9. Optimizer

```python
from vdr.ml.optim import SGD

all_params = (
    Wq.parameters() + Wk.parameters() + Wv.parameters() + Wo.parameters() +
    ffn_l1.parameters() + ffn_l2.parameters() +
    output_proj.parameters()
)
optimizer = SGD(all_params, lr=VDR(1, 100))
```

### 10. Generation

```python
from vdr.ml.sampling import categorical_sample, top_k_probs
from vdr.ml.rng import VDRRandom

rng = VDRRandom(seed=1)

def generate(model, prompt_ids, max_len=10):
    ids = list(prompt_ids)
    for _ in range(max_len):
        logits = model.forward_logits(ids[-seq_len:])
        probs = softmax(logits[-1])
        next_id = categorical_sample(probs, rng)
        ids.append(next_id)
    return ids
```

---

## File Structure

```
examples/toy_llm/
├── model.py          # ToyTransformer class wrapping all components
├── data.py           # corpus, tokenization, windows
├── train.py          # training loop
├── generate.py       # text generation
├── verify.py         # exact verification tests
└── README.md         # explanation
```

---

## model.py — Specification

```python
class ToyTransformer:
    """
    1-layer transformer decoder with exact VDR arithmetic.
    
    Config:
        vocab_size: 6
        dim: 4
        seq_len: 4
        n_heads: 1
        ffn_dim: 8
    """
    
    def __init__(self, vocab_size=6, dim=4, seq_len=4, ffn_dim=8, seed=42):
        # Embedding + positional
        self.embedding  # Embedding(vocab_size, dim)
        self.pos_table  # Mat(seq_len, dim)
        
        # Attention projections
        self.Wq, self.Wk, self.Wv, self.Wo  # Linear(dim, dim) each
        
        # FFN
        self.ffn_l1  # Linear(ffn_dim, dim)
        self.ffn_l2  # Linear(dim, ffn_dim)
        self.relu    # ReLU()
        
        # Output
        self.output_proj  # Linear(vocab_size, dim)
    
    def forward(self, token_ids):
        """
        Full forward pass.
        
        I: list of token ids (ints), length <= seq_len
        O: list of logit Vec (one per position)
        
        Pipeline:
            1. Embed tokens + add position
            2. Self-attention (causal) + residual
            3. FFN + residual
            4. Output projection
        """
    
    def forward_last_logits(self, token_ids):
        """Forward pass, return only last position logits."""
    
    def parameters(self):
        """All trainable parameters."""
    
    def zero_grad(self):
        """Zero all gradients."""
    
    def backward_from_last(self, grad):
        """Backprop from output through entire model."""
```

---

## data.py — Specification

```python
CORPUS = "the cat sat on the mat"

def build_data():
    """
    Returns:
        vocab: dict str -> int
        inv_vocab: dict int -> str  
        windows: list of (context_ids, target_id)
    """

def one_hot_target(target_id, vocab_size):
    """Exact one-hot Vec."""
```

---

## train.py — Specification

```python
def train(n_epochs=20):
    """
    Training loop:
    
    For each epoch:
        For each (context, target) in windows:
            1. Forward: logits = model.forward_last_logits(context)
            2. Softmax: probs = softmax(logits)  # sums to exactly 1
            3. Loss: mse(probs, one_hot(target))  # exact rational
            4. Backward: exact gradients through entire model
            5. Step: SGD update, exact
            6. Zero grad
        Print epoch loss (exact rational)
    
    Properties verified each epoch:
        - softmax sums to exactly 1
        - loss is exact rational (never NaN, never negative)
        - all parameters are exact rationals
    """
```

Expected output:
```
Epoch  1: loss = 1439/8640  (exact)
Epoch  2: loss = 1203/8640  (decreasing)
...
Epoch 20: loss = 89/8640    (converged)
```

Every loss value is an exact fraction. No float anywhere.

---

## verify.py — Specification

```python
def verify_all():
    """
    Exact verification suite:
    
    1. Softmax sum-to-one:
       For every forward pass, sum of softmax output == VDR(1) exactly.
    
    2. Gradient correctness:
       Compare autodiff gradients against numerical gradients
       (discrete derivative with small h). Both exact.
    
    3. Weight update exactness:
       w_new = w_old - lr * grad. Verify by reconstructing:
       (w_old - w_new) / lr == grad exactly.
    
    4. Deterministic reproducibility:
       Same seed, same data, same result. Run twice, compare bit-identical.
    
    5. Loss monotonicity:
       With small enough lr, loss decreases (verify via exact comparison).
    
    6. Attention weight rows sum to 1:
       Every row of attention weights == VDR(1) exactly.
    
    7. Forward-backward roundtrip:
       Train one step, save parameters, load parameters,
       train same step again. Results bit-identical.
    
    8. Parameter checkpoint roundtrip:
       save_model -> load_model_parameters -> all parameters identical.
    """
```

---

## generate.py — Specification

```python
def generate_text(model, prompt="the cat", max_tokens=10):
    """
    Autoregressive generation:
    
    1. Tokenize prompt
    2. Forward pass on prompt
    3. Softmax last position -> exact probability distribution
    4. Sample from distribution (exact CDF comparison)
    5. Append token, repeat
    
    Every sampling decision is exact. Same seed = same output on any platform.
    """
```

---

## Build Order

**Phase 1: data.py** — corpus, vocab, tokenization, windows. Pure Python + VDR one_hot. Test: windows are correct.

**Phase 2: model.py** — ToyTransformer construction and forward pass. Test: forward produces logits of correct shape, softmax sums to 1.

**Phase 3: train.py** — single training step. Test: loss decreases, gradients are nonzero, parameters change.

**Phase 4: verify.py** — full verification suite. Test: all 8 properties hold.

**Phase 5: generate.py** — text generation. Test: produces valid token ids, deterministic with seed.

**Phase 6: end-to-end** — train 20 epochs, generate, verify everything exact.

---

## Expected Results

| Property | Float | VDR |
|---|---|---|
| Softmax sum | 0.9999999999999998 | exactly 1 |
| Loss value | 0.16655... | 1439/8640 (exact fraction) |
| Gradient | 0.0234375... | 3/128 (exact) |
| Weight after update | 0.0898437... | 1151/12800 (exact) |
| Same seed different platform | different last digits | bit-identical |
| 20-epoch loss trajectory | float noise in last digits | exact rational sequence |

---

## Parameter Count

| Component | Shape | Scalars |
|---|---|---|
| Embedding | 6 × 4 | 24 |
| Positional | 4 × 4 | 16 |
| Wq | 4 × 4 + 4 | 20 |
| Wk | 4 × 4 + 4 | 20 |
| Wv | 4 × 4 + 4 | 20 |
| Wo | 4 × 4 + 4 | 20 |
| FFN L1 | 8 × 4 + 8 | 40 |
| FFN L2 | 4 × 8 + 4 | 36 |
| Output proj | 6 × 4 + 6 | 30 |
| **Total** | | **226** |

226 exact rational parameters. Every one inspectable, serializable, reproducible.

---

## What This Proves

1. **Complete LLM pipeline in exact arithmetic works.** Embedding, attention, softmax, FFN, loss, backprop, optimizer — all exact.

2. **Softmax sums to exactly 1 at every step.** Not approximately. Exactly.

3. **Gradients are exact.** No numerical differentiation, no float accumulation in the backward pass.

4. **Training is deterministic.** Same input, same output, any platform, any time.

5. **Every intermediate is inspectable.** You can print any attention weight, any gradient, any parameter as an exact fraction.

6. **Ground truth for float verification.** Train the same model in float, compare against VDR's exact results, measure exactly how much error float introduces at each layer.
