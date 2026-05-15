# code/vdr/datasets.py
from __future__ import annotations

from typing import Dict, List, Sequence, Tuple

from .vdr import VDR
from .linalg import Vec


def build_vocab(tokens: Sequence[str]) -> Dict[str, int]:
    vocab = {}
    for tok in tokens:
        if tok not in vocab:
            vocab[tok] = len(vocab)
    return vocab


def encode_tokens(tokens: Sequence[str], vocab: Dict[str, int]) -> List[int]:
    return [vocab[t] for t in tokens]


def decode_tokens(ids: Sequence[int], inv_vocab: Dict[int, str]) -> List[str]:
    return [inv_vocab[i] for i in ids]


def invert_vocab(vocab: Dict[str, int]) -> Dict[int, str]:
    return {i: t for t, i in vocab.items()}


def sliding_windows(ids: Sequence[int], seq_len: int) -> List[Tuple[List[int], int]]:
    """
    For language-model style next-token prediction:
      input = ids[i:i+seq_len]
      target = ids[i+seq_len]
    """
    if seq_len <= 0:
        raise ValueError("seq_len must be > 0")
    out = []
    for i in range(len(ids) - seq_len):
        out.append((list(ids[i:i + seq_len]), ids[i + seq_len]))
    return out


def one_hot(index: int, size: int) -> Vec:
    vals = [VDR(0) for _ in range(size)]
    vals[index] = VDR(1)
    return Vec(vals)


def batchify_windows(
    windows: Sequence[Tuple[List[int], int]],
    batch_size: int,
) -> List[List[Tuple[List[int], int]]]:
    if batch_size <= 0:
        raise ValueError("batch_size must be > 0")
    out = []
    cur = []
    for item in windows:
        cur.append(item)
        if len(cur) == batch_size:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def tiny_text_dataset(text: str, seq_len: int):
    toks = text.split()
    vocab = build_vocab(toks)
    ids = encode_tokens(toks, vocab)
    windows = sliding_windows(ids, seq_len)
    return {
        "tokens": toks,
        "vocab": vocab,
        "inv_vocab": invert_vocab(vocab),
        "ids": ids,
        "windows": windows,
    }
