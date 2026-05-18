#!/bin/bash
# vdr-math repo scaffold
# Run from the repo root

set -e

# Top-level files
touch pyproject.toml README.md LICENSE

# Core package
mkdir -p src/vdr
touch src/vdr/__init__.py
touch src/vdr/core.py
touch src/vdr/active.py
touch src/vdr/fn.py
touch src/vdr/linalg.py
touch src/vdr/export.py
touch src/vdr/basis.py
touch src/vdr/_compat.py

# Math domains
mkdir -p src/vdr/math
touch src/vdr/math/__init__.py
touch src/vdr/math/number_theory.py
touch src/vdr/math/polynomial.py
touch src/vdr/math/continued_fractions.py
touch src/vdr/math/combinatorics.py
touch src/vdr/math/sequences.py
touch src/vdr/math/probability.py
touch src/vdr/math/symbolic.py
touch src/vdr/math/optimization.py
touch src/vdr/math/graph.py
touch src/vdr/math/game_theory.py
touch src/vdr/math/coding_theory.py
touch src/vdr/math/topology.py
touch src/vdr/math/tropical.py
touch src/vdr/math/control.py
touch src/vdr/math/wavelets.py
touch src/vdr/math/transcendental.py
touch src/vdr/math/chaos.py
touch src/vdr/math/geometry.py
touch src/vdr/math/differential_eq.py
touch src/vdr/math/cryptographic.py

# Signal processing
mkdir -p src/vdr/signal
touch src/vdr/signal/__init__.py
touch src/vdr/signal/convolution.py
touch src/vdr/signal/dft.py
touch src/vdr/signal/filters.py
touch src/vdr/signal/schedule.py

# Physics
mkdir -p src/vdr/physics
touch src/vdr/physics/__init__.py
touch src/vdr/physics/qed.py
touch src/vdr/physics/quantum.py
touch src/vdr/physics/orbital.py
touch src/vdr/physics/structural.py
touch src/vdr/physics/thermo.py
touch src/vdr/physics/crystallography.py
touch src/vdr/physics/geodesy.py
touch src/vdr/physics/optics.py

# ML
mkdir -p src/vdr/ml
touch src/vdr/ml/__init__.py
touch src/vdr/ml/softmax.py
touch src/vdr/ml/exp.py
touch src/vdr/ml/logarithm.py
touch src/vdr/ml/attention.py
touch src/vdr/ml/nn.py
touch src/vdr/ml/autodiff.py
touch src/vdr/ml/optim.py
touch src/vdr/ml/losses.py
touch src/vdr/ml/trainer.py
touch src/vdr/ml/transformer.py
touch src/vdr/ml/sampling.py
touch src/vdr/ml/rng.py
touch src/vdr/ml/init.py
touch src/vdr/ml/tensor.py
touch src/vdr/ml/datasets.py
touch src/vdr/ml/checkpoint.py
touch src/vdr/ml/metrics.py

# Diffusion
mkdir -p src/vdr/diffusion
touch src/vdr/diffusion/__init__.py
touch src/vdr/diffusion/schedule.py
touch src/vdr/diffusion/forward.py
touch src/vdr/diffusion/reverse.py
touch src/vdr/diffusion/sampling.py

# Tests
mkdir -p tests/gym
touch tests/__init__.py
touch tests/test_core.py
touch tests/test_active.py
touch tests/test_fn.py
touch tests/test_linalg.py
touch tests/test_export.py
touch tests/test_basis.py
touch tests/test_normalize.py
touch tests/gym/__init__.py
for i in $(seq -w 1 23); do
    touch "tests/gym/test_gym_${i}.py"
done

# Examples
mkdir -p examples
touch examples/quickstart.py
touch examples/hilbert_inverse.py
touch examples/newton_sqrt2.py
touch examples/q335_constants.py

echo "vdr-math scaffold created: $(find src tests examples -type f | wc -l) files"
