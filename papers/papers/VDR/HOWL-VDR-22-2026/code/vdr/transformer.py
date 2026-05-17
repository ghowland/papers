# code/vdr/transformer.py
from __future__ import annotations

from fractions import Fraction
from typing import List, Optional, Sequence, Union

from .vdr import VDR
from .linalg import Vec, Mat
from .nn import Linear, ReLU, Sequential
from .attention import self_attention
from .basis import vec_to_qbasis, mat_to_qbasis, to_qbasis


ScalarLike = Union[VDR, int, Fraction]


def _to_vdr(x: ScalarLike) -> VDR:
    if isinstance(x, VDR):
        return x
    if isinstance(x, Fraction):
        return VDR.from_fraction(x)
    return VDR(int(x))


class Embedding:
    def __init__(self, table: Sequence[Vec], name: Optional[str] = None):
        if len(table) == 0:
            raise ValueError("embedding table must be nonempty")
        d = table[0].dim
        for row in table:
            if row.dim != d:
                raise ValueError("embedding rows must have same dimension")
        self.table = list(table)
        self.name = name or "embedding"

    @classmethod
    def from_ints(cls, rows, name: Optional[str] = None):
        return cls([Vec.from_ints(row) for row in rows], name=name)

    @classmethod
    def from_fracs(cls, rows, name: Optional[str] = None):
        return cls([Vec.from_fracs(row) for row in rows], name=name)

    @property
    def vocab_size(self):
        return len(self.table)

    @property
    def dim(self):
        return self.table[0].dim

    def lookup(self, idx: int) -> Vec:
        return self.table[idx]

    def lookup_many(self, ids: Sequence[int]) -> List[Vec]:
        return [self.lookup(i) for i in ids]

    def to_qbasis(self, bits: int):
        return Embedding([vec_to_qbasis(v, bits) for v in self.table], name=self.name)


class FeedForwardBlock:
    """
    Minimal transformer feedforward:
      Linear -> ReLU -> Linear
    """
    def __init__(self, l1: Linear, l2: Linear):
        self.net = Sequential([l1, ReLU(), l2])

    def parameters(self):
        return self.net.parameters()

    def zero_grad(self):
        self.net.zero_grad()

    def forward(self, x: Vec) -> Vec:
        return self.net.forward(x)

    def backward(self, grad_out: Vec) -> Vec:
        return self.net.backward(grad_out)


class TransformerBlock:
    """
    Minimal single-head transformer-like block:
      self-attention + residual + feedforward + residual

    This is not a full industrial transformer. It is a VDR-native
    prototype block using existing exact primitives.
    """
    def __init__(
        self,
        ff: FeedForwardBlock,
        attention_mode: str = "softmax",
        attention_depth: int = 12,
        causal: bool = False,
    ):
        self.ff = ff
        self.attention_mode = attention_mode
        self.attention_depth = attention_depth
        self.causal = causal

    def parameters(self):
        return self.ff.parameters()

    def zero_grad(self):
        self.ff.zero_grad()

    def forward(self, xs: Sequence[Vec]) -> List[Vec]:
        attn = self_attention(
            xs,
            mode=self.attention_mode,
            depth=self.attention_depth,
            causal=self.causal,
        )
        attn_out = attn["output"]

        # residual after attention
        res1 = [attn_out[i] + xs[i] for i in range(len(xs))]

        # feedforward positionwise
        ff_out = [self.ff.forward(v) for v in res1]

        # second residual
        out = [ff_out[i] + res1[i] for i in range(len(xs))]
        return out

    def forward_with_cache(self, xs: Sequence[Vec]):
        attn = self_attention(
            xs,
            mode=self.attention_mode,
            depth=self.attention_depth,
            causal=self.causal,
        )
        attn_out = attn["output"]
        res1 = [attn_out[i] + xs[i] for i in range(len(xs))]
        ff_out = [self.ff.forward(v) for v in res1]
        out = [ff_out[i] + res1[i] for i in range(len(xs))]
        return {
            "scores": attn["scores"],
            "weights": attn["weights"],
            "attn_out": attn_out,
            "res1": res1,
            "ff_out": ff_out,
            "out": out,
        }


class TinyTransformerLM:
    """
    Tiny exact-fraction transformer-like language model:

      token ids
        -> embedding lookup
        -> transformer block
        -> output projection (Linear applied tokenwise)

    Output:
      one logit vector per token position
    """
    def __init__(
        self,
        embedding: Embedding,
        block: TransformerBlock,
        out_proj: Linear,
        name: Optional[str] = None,
    ):
        if embedding.dim != out_proj.W.value.ncols:
            raise ValueError("embedding dim must match output projection input dim")
        self.embedding = embedding
        self.block = block
        self.out_proj = out_proj
        self.name = name or "tiny_transformer_lm"

    def parameters(self):
        return self.block.parameters() + self.out_proj.parameters()

    def zero_grad(self):
        self.block.zero_grad()
        self.out_proj.zero_grad()

    def embed(self, token_ids: Sequence[int]) -> List[Vec]:
        return self.embedding.lookup_many(token_ids)

    def forward_hidden(self, token_ids: Sequence[int]) -> List[Vec]:
        xs = self.embed(token_ids)
        return self.block.forward(xs)

    def forward_logits(self, token_ids: Sequence[int]) -> List[Vec]:
        hs = self.forward_hidden(token_ids)
        return [self.out_proj.forward(h) for h in hs]

    def forward_logits_with_cache(self, token_ids: Sequence[int]):
        xs = self.embed(token_ids)
        block_cache = self.block.forward_with_cache(xs)
        logits = [self.out_proj.forward(h) for h in block_cache["out"]]
        block_cache["logits"] = logits
        return block_cache

    def to_qbasis(self, bits: int):
        emb = self.embedding.to_qbasis(bits)

        ff_params = self.block.ff.parameters()
        for p in ff_params:
            if isinstance(p.value, Vec):
                p.value = vec_to_qbasis(p.value, bits)
            else:
                p.value = mat_to_qbasis(p.value, bits)

        for p in self.out_proj.parameters():
            if isinstance(p.value, Vec):
                p.value = vec_to_qbasis(p.value, bits)
            else:
                p.value = mat_to_qbasis(p.value, bits)

        return self
    