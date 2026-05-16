Alright, enumerating the open problems from the papers:

1. **Complex number extension** — No native complex type. Blocks eigenvalues for n≥3, DFT on complex signals, complex polynomial roots. Design is understood per VDR-3 (UI1), described as engineering work not mathematical obstacle.

2. **Gaussian elimination** — Currently using cofactor expansion which is O(n!). Blocks practical matrix computation beyond ~15×15. Gaussian elimination would give O(n³) with exact rational pivots. Top priority on the development roadmap (FW1, UI2).

3. **Max-flow BFS fix** — Ford-Fulkerson augmenting-path loop termination bug (F1 in VDR-3). VDR arithmetic is correct, the graph traversal logic is wrong. Straightforward algorithm fix.

4. **Denominator growth compression** — Chaotic iteration produces denominators growing exponentially (~2^n digits after n steps). FW2 proposes functional remainders representing "n logistic steps" without materializing intermediate fractions. Completely untested — no passes, no failures, just an open design space.

Four problems. Different sizes. How do you want to sequence these — hardest first, quickest win first, or by dependency?

---

