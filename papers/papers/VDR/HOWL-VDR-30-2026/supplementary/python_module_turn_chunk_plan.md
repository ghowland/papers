# Turn Chunk Plan

## Estimating Capacity

My output limit is roughly 16K tokens per turn. Python source is dense — roughly 1 token per 3-4 characters. A typical module with docstrings, type hints, and functions runs 200-600 lines. The core modules (core.py, active.py, fn.py) are each 300-500 lines. Smaller math modules are 80-200 lines.

**Rule:** pack as much as possible per turn to maintain alignment. Never split a single file across turns.

---

## Turn Plan

### Turn 1 — Core Package (5 files)
- `src/vdr/__init__.py`
- `src/vdr/_compat.py`
- `src/vdr/core.py` (the big one — VDR, Remainder, normalization with fix, closed arithmetic, rebase, lift)
- `src/vdr/active.py`
- `src/vdr/export.py`

**Rationale:** core.py is ~500 lines, active.py ~250, export.py ~80, init ~30, compat ~30. Total ~890 lines. Tight but fits. These 5 files must align perfectly — one turn.

### Turn 2 — Core Package Continued (2 files)
- `src/vdr/fn.py` (~400 lines — FnRemainder, resolve, factories, discrete calculus, install)
- `src/vdr/basis.py` (~150 lines — D-frame management, Q335, qb operations)

**Rationale:** fn.py is complex with FnRemainder class, multiple factories, discrete calculus. basis.py is smaller but depends on core. Both together ~550 lines.

### Turn 3 — Linear Algebra (1 file)
- `src/vdr/linalg.py` (~600 lines — Vec, Mat, Gaussian elimination added, cofactor, parse, serialize, LaTeX)

**Rationale:** This is a big file. Vec + Mat with all methods, plus Gaussian det/inv/solve, plus parser and serialization. Needs its own turn.

### Turn 4 — Math: Number Theory + Continued Fractions + Combinatorics + Sequences (4 files)
- `src/vdr/math/__init__.py`
- `src/vdr/math/number_theory.py` (~200 lines)
- `src/vdr/math/continued_fractions.py` (~150 lines)
- `src/vdr/math/combinatorics.py` (~150 lines)
- `src/vdr/math/sequences.py` (~150 lines)

**Rationale:** all pure integer/rational arithmetic, no dependencies beyond core. ~650 lines total.

### Turn 5 — Math: Polynomial + Symbolic + Probability (3 files)
- `src/vdr/math/polynomial.py` (~250 lines)
- `src/vdr/math/symbolic.py` (~150 lines)
- `src/vdr/math/probability.py` (~200 lines)

**Rationale:** polynomial is medium-large (many operations). Symbolic builds on polynomial. Probability is self-contained. ~600 lines.

### Turn 6 — Math: Geometry + Optimization + Differential Eq (3 files)
- `src/vdr/math/geometry.py` (~150 lines)
- `src/vdr/math/optimization.py` (~150 lines)
- `src/vdr/math/differential_eq.py` (~200 lines)

**Rationale:** geometry is compact. Optimization is compact. Diff eq has Euler, RK4, Picard, Lotka-Volterra. ~500 lines.

### Turn 7 — Math: Graph + Game Theory + Cryptographic (3 files)
- `src/vdr/math/graph.py` (~250 lines — Dijkstra, Bellman-Ford, Floyd-Warshall, PageRank, max-flow)
- `src/vdr/math/game_theory.py` (~200 lines)
- `src/vdr/math/cryptographic.py` (~150 lines)

**Rationale:** graph is medium (multiple algorithms). Game theory has several equilibrium computations. Crypto is compact (modular arithmetic). ~600 lines.

### Turn 8 — Math: Coding Theory + Topology + Tropical + Control (4 files)
- `src/vdr/math/coding_theory.py` (~150 lines)
- `src/vdr/math/topology.py` (~120 lines)
- `src/vdr/math/tropical.py` (~200 lines — includes LLL)
- `src/vdr/math/control.py` (~200 lines)

**Rationale:** coding theory is compact. Topology is compact. Tropical includes Gram-Schmidt and LLL which add bulk. Control has state-space, Cayley-Hamilton. ~670 lines.

### Turn 9 — Math: Wavelets + Chaos + Transcendental (3 files)
- `src/vdr/math/wavelets.py` (~150 lines)
- `src/vdr/math/chaos.py` (~120 lines)
- `src/vdr/math/transcendental.py` (~400 lines — the big one: all Q335 constants as globals, Borwein, elliptic, trig series, sqrt_newton)

**Rationale:** transcendental.py is large because it has 22 Q335 globals plus many series functions plus Borwein acceleration. Wavelets and chaos are compact. ~670 lines.

### Turn 10 — Signal Processing (4 files)
- `src/vdr/signal/__init__.py`
- `src/vdr/signal/convolution.py` (~80 lines)
- `src/vdr/signal/dft.py` (~150 lines)
- `src/vdr/signal/filters.py` (~100 lines)
- `src/vdr/signal/schedule.py` (~100 lines)

**Rationale:** all signal modules are compact. ~430 lines total. Could potentially combine with a physics module but signal is a clean category.

### Turn 11 — Physics: QED + Quantum + Orbital + Optics (4 files)
- `src/vdr/physics/__init__.py`
- `src/vdr/physics/qed.py` (~120 lines)
- `src/vdr/physics/quantum.py` (~200 lines)
- `src/vdr/physics/orbital.py` (~120 lines)
- `src/vdr/physics/optics.py` (~120 lines)

**Rationale:** QED depends on transcendental constants. Quantum has Pauli globals and spin rotation. Orbital has Kepler. Optics has ABCD matrices. ~560 lines.

### Turn 12 — Physics: Structural + Thermo + Crystallography + Geodesy (4 files)
- `src/vdr/physics/structural.py` (~100 lines)
- `src/vdr/physics/thermo.py` (~150 lines)
- `src/vdr/physics/crystallography.py` (~150 lines)
- `src/vdr/physics/geodesy.py` (~100 lines)

**Rationale:** all compact physics modules. ~500 lines.

### Turn 13 — ML Core: softmax + exp + logarithm + losses + rng + init (6 files)
- `src/vdr/ml/__init__.py`
- `src/vdr/ml/softmax.py` (~150 lines)
- `src/vdr/ml/exp.py` (~100 lines)
- `src/vdr/ml/logarithm.py` (~100 lines)
- `src/vdr/ml/losses.py` (~80 lines)
- `src/vdr/ml/rng.py` (~80 lines)
- `src/vdr/ml/init.py` (~80 lines)

**Rationale:** these are the ML primitives everything else builds on. All compact. ~590 lines.

### Turn 14 — ML: nn + autodiff + optim (3 files)
- `src/vdr/ml/nn.py` (~350 lines — VecParam, MatParam, Linear, ReLU, Sequential, FFN)
- `src/vdr/ml/autodiff.py` (~250 lines — Node, backward, operators)
- `src/vdr/ml/optim.py` (~80 lines — SGD, Momentum)

**Rationale:** nn.py is the largest ML file. Autodiff is medium. These three form the training stack. ~680 lines.

### Turn 15 — ML: attention + transformer + sampling (3 files)
- `src/vdr/ml/attention.py` (~200 lines)
- `src/vdr/ml/transformer.py` (~300 lines — Embedding, FFN, TransformerBlock, TransformerLM)
- `src/vdr/ml/sampling.py` (~100 lines)

**Rationale:** transformer.py is medium-large. Attention feeds into it. Sampling is compact. ~600 lines.

### Turn 16 — ML: trainer + tensor + datasets + checkpoint + metrics (5 files)
- `src/vdr/ml/trainer.py` (~100 lines)
- `src/vdr/ml/tensor.py` (~120 lines)
- `src/vdr/ml/datasets.py` (~100 lines)
- `src/vdr/ml/checkpoint.py` (~60 lines)
- `src/vdr/ml/metrics.py` (~80 lines)

**Rationale:** all compact support modules. ~460 lines.

### Turn 17 — Diffusion (4 files)
- `src/vdr/diffusion/__init__.py`
- `src/vdr/diffusion/schedule.py` (~150 lines)
- `src/vdr/diffusion/forward.py` (~100 lines)
- `src/vdr/diffusion/reverse.py` (~150 lines)
- `src/vdr/diffusion/sampling.py` (~150 lines)

**Rationale:** diffusion is a self-contained domain. ~550 lines.

### Turn 18 — pyproject.toml + README.md
- `pyproject.toml` (complete, with all metadata)
- `README.md` (comprehensive, with examples for each domain category)

**Rationale:** README needs to be substantial to represent the library properly. Combined ~400 lines.

### Turn 19-22 — Tests (4 turns)
- **Turn 19:** `tests/test_core.py`, `tests/test_active.py`, `tests/test_normalize.py`
- **Turn 20:** `tests/test_fn.py`, `tests/test_linalg.py`, `tests/test_export.py`, `tests/test_basis.py`
- **Turn 21:** `tests/gym/test_gym_01.py` through `tests/gym/test_gym_12.py`
- **Turn 22:** `tests/gym/test_gym_13.py` through `tests/gym/test_gym_23.py`

### Turn 23 — Examples (1 turn)
- `examples/quickstart.py`
- `examples/hilbert_inverse.py`
- `examples/newton_sqrt2.py`
- `examples/q335_constants.py`

---

## Summary

| Turn | Content | Est. Lines | Files |
|---|---|---|---|
| 1 | Core: init, compat, core, active, export | ~890 | 5 |
| 2 | Core: fn, basis | ~550 | 2 |
| 3 | linalg | ~600 | 1 |
| 4 | Math: number_theory, continued_fractions, combinatorics, sequences | ~650 | 5 |
| 5 | Math: polynomial, symbolic, probability | ~600 | 3 |
| 6 | Math: geometry, optimization, differential_eq | ~500 | 3 |
| 7 | Math: graph, game_theory, cryptographic | ~600 | 3 |
| 8 | Math: coding_theory, topology, tropical, control | ~670 | 4 |
| 9 | Math: wavelets, chaos, transcendental | ~670 | 3 |
| 10 | Signal: all 4 modules | ~430 | 5 |
| 11 | Physics: qed, quantum, orbital, optics | ~560 | 5 |
| 12 | Physics: structural, thermo, crystallography, geodesy | ~500 | 4 |
| 13 | ML: softmax, exp, log, losses, rng, init | ~590 | 7 |
| 14 | ML: nn, autodiff, optim | ~680 | 3 |
| 15 | ML: attention, transformer, sampling | ~600 | 3 |
| 16 | ML: trainer, tensor, datasets, checkpoint, metrics | ~460 | 5 |
| 17 | Diffusion: all 4 modules | ~550 | 5 |
| 18 | pyproject.toml, README | ~400 | 2 |
| 19-22 | Tests (4 turns) | ~2400 | ~30 |
| 23 | Examples | ~300 | 4 |
| **Total** | | **~12,200** | **~102 files** |

**23 turns to complete the entire library.** After turn 23 you test, I fix.
