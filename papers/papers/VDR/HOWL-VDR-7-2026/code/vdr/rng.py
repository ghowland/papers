# code/vdr/rng.py
from __future__ import annotations

from fractions import Fraction
from typing import List

from .vdr import VDR


class VDRRandom:
    """
    Simple deterministic integer PRNG for exact reproducibility.

    Uses a classic LCG:
        state = (a * state + c) mod m

    This is not cryptographic. It is intended for deterministic
    initialization, shuffling, and exact-probability sampling.
    """
    def __init__(self, seed=1):
        self.m = 2 ** 31
        self.a = 1103515245
        self.c = 12345
        self.state = int(seed) % self.m

    def next_int(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def randbelow(self, n):
        if n <= 0:
            raise ValueError("n must be > 0")
        return self.next_int() % n

    def rand_fraction(self):
        """
        Exact rational in [0,1):
            next_int / m
        """
        return VDR(self.next_int(), self.m)

    def randint(self, lo, hi):
        if hi < lo:
            raise ValueError("hi must be >= lo")
        return lo + self.randbelow(hi - lo + 1)

    def shuffle_in_place(self, xs):
        for i in range(len(xs) - 1, 0, -1):
            j = self.randbelow(i + 1)
            xs[i], xs[j] = xs[j], xs[i]

    def permutation(self, n):
        xs = list(range(n))
        self.shuffle_in_place(xs)
        return xs
    