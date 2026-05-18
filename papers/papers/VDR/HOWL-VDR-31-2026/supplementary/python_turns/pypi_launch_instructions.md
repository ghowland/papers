# PyPI Launch Instructions

## Overview

You have all the source files. This document gets you from files on disk to a published PyPI package with auto-generated API docs, CI, and utility scripts.

---

## 1. Repository Setup

### 1.1 Initialize Git

```bash
cd vdr-math
git init
git add .
git commit -m "Initial commit: vdr-math 0.1.0"
```

### 1.2 Create `.gitignore`

```
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
.eggs/
*.egg
.pytest_cache/
.mypy_cache/
.tox/
htmlcov/
.coverage
site/
.venv/
venv/
env/
```

### 1.3 Create `LICENSE`

```
MIT License

Copyright (c) 2025 VDR Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 2. Requirements Files

### 2.1 `requirements.txt` (runtime — empty, no required deps)

```
# vdr-math has no required dependencies.
# Optional: mpmath for arbitrary-precision decimal export.
```

### 2.2 `requirements-dev.txt`

```
pytest>=7.0
pytest-cov>=4.0
mpmath>=1.3
build>=1.0
twine>=4.0
mkdocs>=1.5
mkdocstrings[python]>=0.24
mkdocs-material>=9.0
ruff>=0.3
mypy>=1.8
```

### 2.3 `requirements-docs.txt`

```
mkdocs>=1.5
mkdocstrings[python]>=0.24
mkdocs-material>=9.0
```

---

## 3. Utility Scripts

Create a `scripts/` directory:

```bash
mkdir -p scripts
```

### 3.1 `scripts/test.sh` — Run tests

```bash
#!/bin/bash
# Run all tests
set -e
python -m pytest tests/ -v "$@"
```

### 3.2 `scripts/test-fast.sh` — Run core tests only

```bash
#!/bin/bash
# Run core tests (skip gym)
set -e
python -m pytest tests/ -v --ignore=tests/gym "$@"
```

### 3.3 `scripts/test-gym.sh` — Run gym tests only

```bash
#!/bin/bash
# Run gym integration tests
set -e
python -m pytest tests/gym/ -v "$@"
```

### 3.4 `scripts/test-cov.sh` — Coverage report

```bash
#!/bin/bash
# Run tests with coverage
set -e
python -m pytest tests/ --cov=vdr --cov-report=html --cov-report=term-missing "$@"
echo ""
echo "HTML report: htmlcov/index.html"
```

### 3.5 `scripts/build.sh` — Build package

```bash
#!/bin/bash
# Build sdist and wheel
set -e
rm -rf dist/ build/ src/*.egg-info
python -m build
echo ""
echo "Built:"
ls -la dist/
```

### 3.6 `scripts/publish-test.sh` — Upload to Test PyPI

```bash
#!/bin/bash
# Upload to Test PyPI (test before real publish)
set -e
./scripts/build.sh
python -m twine upload --repository testpypi dist/*
echo ""
echo "Published to Test PyPI."
echo "Install with: pip install --index-url https://test.pypi.org/simple/ vdr-math"
```

### 3.7 `scripts/publish.sh` — Upload to real PyPI

```bash
#!/bin/bash
# Upload to real PyPI
set -e
read -p "Publishing to REAL PyPI. Are you sure? (y/N) " confirm
if [ "$confirm" != "y" ]; then
    echo "Aborted."
    exit 1
fi
./scripts/build.sh
python -m twine upload dist/*
echo ""
echo "Published to PyPI."
echo "Install with: pip install vdr-math"
```

### 3.8 `scripts/lint.sh` — Lint and type check

```bash
#!/bin/bash
# Lint with ruff, type check with mypy
set -e
echo "=== Ruff ==="
python -m ruff check src/vdr/
echo ""
echo "=== Mypy ==="
python -m mypy src/vdr/ --ignore-missing-imports
```

### 3.9 `scripts/docs-build.sh` — Build documentation

```bash
#!/bin/bash
# Build mkdocs documentation
set -e
python -m mkdocs build
echo ""
echo "Docs built: site/index.html"
```

### 3.10 `scripts/docs-serve.sh` — Serve docs locally

```bash
#!/bin/bash
# Serve docs locally for preview
set -e
python -m mkdocs serve
```

### 3.11 `scripts/clean.sh` — Clean build artifacts

```bash
#!/bin/bash
# Clean all build artifacts
rm -rf dist/ build/ src/*.egg-info
rm -rf .pytest_cache/ htmlcov/ .coverage
rm -rf site/
rm -rf .mypy_cache/
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null
echo "Cleaned."
```

### 3.12 `scripts/install-dev.sh` — Set up dev environment

```bash
#!/bin/bash
# Set up development environment
set -e
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
pip install -e .
echo ""
echo "Dev environment ready. Run ./scripts/test.sh to verify."
```

### Make all scripts executable:

```bash
chmod +x scripts/*.sh
```

---

## 4. Auto-Generated API Documentation

### 4.1 `mkdocs.yml`

```yaml
site_name: vdr-math
site_description: Exact arithmetic with Value, Denominator, Remainder triples
repo_url: https://github.com/vdr-project/vdr-math
repo_name: vdr-project/vdr-math

theme:
  name: material
  palette:
    scheme: default
    primary: indigo
  features:
    - navigation.sections
    - navigation.expand
    - content.code.copy
    - search.suggest

plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            show_source: false
            show_root_heading: true
            show_root_full_path: false
            heading_level: 3
            docstring_style: google
            show_signature_annotations: true
            separate_signature: true
            merge_init_into_class: true

nav:
  - Home: index.md
  - Understanding VDR: understanding.md
  - Cookbook: cookbook.md
  - Migration Guide: migration.md
  - Domain Extension Guide: extension.md
  - API Reference:
    - Core:
      - vdr.core: api/core.md
      - vdr.active: api/active.md
      - vdr.fn: api/fn.md
      - vdr.linalg: api/linalg.md
      - vdr.export: api/export.md
      - vdr.basis: api/basis.md
    - Math Domains:
      - Number Theory: api/math/number_theory.md
      - Continued Fractions: api/math/continued_fractions.md
      - Combinatorics: api/math/combinatorics.md
      - Sequences: api/math/sequences.md
      - Polynomial: api/math/polynomial.md
      - Symbolic: api/math/symbolic.md
      - Probability: api/math/probability.md
      - Geometry: api/math/geometry.md
      - Optimization: api/math/optimization.md
      - Differential Equations: api/math/differential_eq.md
      - Graph Theory: api/math/graph.md
      - Game Theory: api/math/game_theory.md
      - Cryptographic: api/math/cryptographic.md
      - Coding Theory: api/math/coding_theory.md
      - Topology: api/math/topology.md
      - Tropical & Lattice: api/math/tropical.md
      - Control Theory: api/math/control.md
      - Wavelets: api/math/wavelets.md
      - Chaos: api/math/chaos.md
      - Transcendental: api/math/transcendental.md
    - Signal Processing:
      - Convolution: api/signal/convolution.md
      - DFT: api/signal/dft.md
      - Filters: api/signal/filters.md
      - Schedule: api/signal/schedule.md
    - Physics:
      - QED: api/physics/qed.md
      - Quantum: api/physics/quantum.md
      - Orbital: api/physics/orbital.md
      - Optics: api/physics/optics.md
      - Structural: api/physics/structural.md
      - Thermodynamics: api/physics/thermo.md
      - Crystallography: api/physics/crystallography.md
      - Geodesy: api/physics/geodesy.md
    - Machine Learning:
      - Softmax: api/ml/softmax.md
      - Exp: api/ml/exp.md
      - Logarithm: api/ml/logarithm.md
      - Neural Networks: api/ml/nn.md
      - Autodiff: api/ml/autodiff.md
      - Optimizers: api/ml/optim.md
      - Attention: api/ml/attention.md
      - Transformer: api/ml/transformer.md
      - Sampling: api/ml/sampling.md
      - Trainer: api/ml/trainer.md
      - Losses: api/ml/losses.md
      - Datasets: api/ml/datasets.md
      - Checkpoint: api/ml/checkpoint.md
      - Metrics: api/ml/metrics.md
      - RNG: api/ml/rng.md
      - Init: api/ml/init.md
      - Tensor: api/ml/tensor.md
    - Diffusion:
      - Schedule: api/diffusion/schedule.md
      - Forward: api/diffusion/forward.md
      - Reverse: api/diffusion/reverse.md
      - Sampling: api/diffusion/sampling.md

markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences
  - pymdownx.arithmatex:
      generic: true
  - admonition
  - toc:
      permalink: true
```

### 4.2 Create docs directory structure and API reference stubs

```bash
#!/bin/bash
# scripts/docs-init.sh — Create docs directory structure
set -e

mkdir -p docs/api/core
mkdir -p docs/api/math
mkdir -p docs/api/signal
mkdir -p docs/api/physics
mkdir -p docs/api/ml
mkdir -p docs/api/diffusion

# Home page (copy README)
cp README.md docs/index.md

# Prose docs (copy from your documentation files)
# These should be the files we wrote: understanding doc, cookbook, migration+extension guide
touch docs/understanding.md
touch docs/cookbook.md
touch docs/migration.md
touch docs/extension.md

# Core API stubs — each file just has the mkdocstrings directive
for mod in core active fn linalg export basis; do
cat > "docs/api/${mod}.md" << EOF
# vdr.${mod}

::: vdr.${mod}
EOF
done

# Math domain stubs
for mod in number_theory continued_fractions combinatorics sequences polynomial symbolic probability geometry optimization differential_eq graph game_theory cryptographic coding_theory topology tropical control wavelets chaos transcendental; do
cat > "docs/api/math/${mod}.md" << EOF
# vdr.math.${mod}

::: vdr.math.${mod}
EOF
done

# Signal stubs
for mod in convolution dft filters schedule; do
cat > "docs/api/signal/${mod}.md" << EOF
# vdr.signal.${mod}

::: vdr.signal.${mod}
EOF
done

# Physics stubs
for mod in qed quantum orbital optics structural thermo crystallography geodesy; do
cat > "docs/api/physics/${mod}.md" << EOF
# vdr.physics.${mod}

::: vdr.physics.${mod}
EOF
done

# ML stubs
for mod in softmax exp logarithm nn autodiff optim attention transformer sampling trainer losses datasets checkpoint metrics rng init tensor; do
cat > "docs/api/ml/${mod}.md" << EOF
# vdr.ml.${mod}

::: vdr.ml.${mod}
EOF
done

# Diffusion stubs
for mod in schedule forward reverse sampling; do
cat > "docs/api/diffusion/${mod}.md" << EOF
# vdr.diffusion.${mod}

::: vdr.diffusion.${mod}
EOF
done

echo "Docs structure created. $(find docs -type f | wc -l) files."
```

Make executable and run:

```bash
chmod +x scripts/docs-init.sh
./scripts/docs-init.sh
```

---

## 5. CI with GitHub Actions

### 5.1 `.github/workflows/test.yml`

```yaml
name: Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.8", "3.9", "3.10", "3.11", "3.12", "3.13"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements-dev.txt
          pip install -e .

      - name: Run tests
        run: python -m pytest tests/ -v --tb=short

      - name: Run tests with coverage
        if: matrix.python-version == '3.12'
        run: |
          python -m pytest tests/ --cov=vdr --cov-report=xml
          
      - name: Upload coverage
        if: matrix.python-version == '3.12'
        uses: codecov/codecov-action@v4
        with:
          file: coverage.xml
```

### 5.2 `.github/workflows/publish.yml`

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install build tools
        run: |
          python -m pip install --upgrade pip
          pip install build twine

      - name: Build
        run: python -m build

      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: python -m twine upload dist/*
```

Create the directories:

```bash
mkdir -p .github/workflows
```

---

## 6. Ruff Configuration

Add to `pyproject.toml`:

```toml
[tool.ruff]
target-version = "py38"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "W", "I"]
ignore = ["E501"]  # line length handled by line-length setting
```

---

## 7. Step-by-Step Launch Procedure

### Phase 1: Set up dev environment

```bash
# 1. Create virtual environment
python -m venv .venv
source .venv/bin/activate

# 2. Install dev dependencies and package in editable mode
./scripts/install-dev.sh

# 3. Verify tests pass
./scripts/test.sh
```

### Phase 2: Fix any test failures

Tests may fail on first run due to import path issues or minor bugs. Fix iteratively:

```bash
# Run core tests first
./scripts/test-fast.sh

# Then gym tests
./scripts/test-gym.sh

# With verbose output for debugging
python -m pytest tests/test_core.py -v -s
```

### Phase 3: Generate docs

```bash
# Initialize docs structure
./scripts/docs-init.sh

# Copy prose documentation into docs/
# (understanding.md, cookbook.md, migration.md, extension.md)
# These are the documents we wrote in this session.

# Build and preview
./scripts/docs-serve.sh
# Open http://127.0.0.1:8000 in browser
```

### Phase 4: Test the build

```bash
# Build sdist and wheel
./scripts/build.sh

# Test install in a fresh venv
python -m venv /tmp/test-vdr
source /tmp/test-vdr/bin/activate
pip install dist/vdr_math-0.1.0-py3-none-any.whl
python -c "from vdr import VDR; print(VDR(1, 3) + VDR(1, 7))"
deactivate
rm -rf /tmp/test-vdr
```

### Phase 5: PyPI accounts

```bash
# 1. Create account at https://pypi.org/account/register/
# 2. Create account at https://test.pypi.org/account/register/
# 3. Generate API tokens:
#    PyPI: https://pypi.org/manage/account/token/
#    Test PyPI: https://test.pypi.org/manage/account/token/

# 4. Configure ~/.pypirc
cat > ~/.pypirc << 'EOF'
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR-TOKEN-HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR-TEST-TOKEN-HERE
EOF

chmod 600 ~/.pypirc
```

### Phase 6: Test PyPI publish

```bash
# Publish to Test PyPI first
./scripts/publish-test.sh

# Verify install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ vdr-math
python -c "from vdr import VDR; print(VDR(1, 3) + VDR(1, 7))"
```

### Phase 7: Real PyPI publish

```bash
# Publish for real
./scripts/publish.sh

# Verify
pip install vdr-math
python -c "from vdr import VDR; print(VDR(1, 3) + VDR(1, 7))"
```

### Phase 8: GitHub setup

```bash
# Push to GitHub
git remote add origin https://github.com/YOUR-USER/vdr-math.git
git push -u origin main

# Add PyPI token as GitHub secret:
# Repository -> Settings -> Secrets -> Actions -> New repository secret
# Name: PYPI_API_TOKEN
# Value: pypi-YOUR-TOKEN-HERE

# Create first release:
# GitHub -> Releases -> Create new release
# Tag: v0.1.0
# Title: vdr-math 0.1.0
# Description: Initial release
# This triggers the publish workflow automatically.
```

---

## 8. Final Checklist

```
Repository structure:
  [ ] .gitignore
  [ ] LICENSE (MIT)
  [ ] README.md (the full documentation)
  [ ] pyproject.toml
  [ ] requirements.txt
  [ ] requirements-dev.txt
  [ ] requirements-docs.txt

Source:
  [ ] src/vdr/__init__.py
  [ ] src/vdr/core.py
  [ ] src/vdr/active.py
  [ ] src/vdr/fn.py
  [ ] src/vdr/linalg.py
  [ ] src/vdr/export.py
  [ ] src/vdr/basis.py
  [ ] src/vdr/_compat.py
  [ ] src/vdr/math/ (20 modules)
  [ ] src/vdr/signal/ (4 modules)
  [ ] src/vdr/physics/ (8 modules)
  [ ] src/vdr/ml/ (17 modules)
  [ ] src/vdr/diffusion/ (4 modules)

Tests:
  [ ] tests/test_core.py
  [ ] tests/test_active.py
  [ ] tests/test_normalize.py
  [ ] tests/test_fn.py
  [ ] tests/test_linalg.py
  [ ] tests/test_export.py
  [ ] tests/test_basis.py
  [ ] tests/gym/test_gym_01.py through test_gym_23.py

Docs:
  [ ] mkdocs.yml
  [ ] docs/index.md (README)
  [ ] docs/understanding.md
  [ ] docs/cookbook.md
  [ ] docs/migration.md
  [ ] docs/extension.md
  [ ] docs/api/ (auto-generated stubs)

Scripts:
  [ ] scripts/test.sh
  [ ] scripts/test-fast.sh
  [ ] scripts/test-gym.sh
  [ ] scripts/test-cov.sh
  [ ] scripts/build.sh
  [ ] scripts/publish-test.sh
  [ ] scripts/publish.sh
  [ ] scripts/lint.sh
  [ ] scripts/docs-build.sh
  [ ] scripts/docs-serve.sh
  [ ] scripts/docs-init.sh
  [ ] scripts/clean.sh
  [ ] scripts/install-dev.sh

CI:
  [ ] .github/workflows/test.yml
  [ ] .github/workflows/publish.yml

Accounts:
  [ ] PyPI account + API token
  [ ] Test PyPI account + API token
  [ ] GitHub repo created
  [ ] PYPI_API_TOKEN secret added to GitHub

Verification:
  [ ] ./scripts/test.sh passes
  [ ] ./scripts/build.sh produces wheel
  [ ] pip install from wheel works
  [ ] from vdr import VDR works
  [ ] Test PyPI publish works
  [ ] Real PyPI publish works
  [ ] GitHub Actions test workflow passes
```

---

## 9. Version Bumping for Future Releases

Edit version in `pyproject.toml`:

```toml
version = "0.2.0"
```

Then:

```bash
git add pyproject.toml
git commit -m "Bump version to 0.2.0"
git tag v0.2.0
git push origin main --tags
```

Create GitHub release from the tag — CI publishes automatically.

---

## 10. Quick Reference Card

```bash
./scripts/install-dev.sh    # set up dev environment
./scripts/test.sh            # run all tests
./scripts/test-fast.sh       # core tests only
./scripts/test-cov.sh        # tests with coverage
./scripts/lint.sh             # ruff + mypy
./scripts/docs-serve.sh      # preview docs at localhost:8000
./scripts/build.sh            # build wheel
./scripts/publish-test.sh    # upload to Test PyPI
./scripts/publish.sh          # upload to real PyPI
./scripts/clean.sh            # remove build artifacts
```
