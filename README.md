# vector-math-pytest

[![CI](https://github.com/AlexWrightWatkinson/pytest-experiments/actions/workflows/ci.yml/badge.svg)](https://github.com/AlexWrightWatkinson/pytest-experiments/actions/workflows/ci.yml)
[![Coverage Status](https://img.shields.io/badge/coverage-90%25%2B-brightgreen)](#coverage)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vector-math-pytest)](#)

Small, well-structured Python project designed to teach **pytest** thoroughly through an actionable codebase.

---

## Overview

This project implements a tiny `vector_math` module (vector addition, dot product, scalar multiply, normalization, batch normalization) and a **rich pytest suite** demonstrating essentials through advanced testing techniques: parametrization, fixtures, mocking, monkeypatching, property-based testing (Hypothesis), benchmarking (pytest-benchmark), custom markers, coverage enforcement, and CI integration.

---

## Why pytest?

- Clear, expressive syntax (`assert`, parametrization).
- Fixtures for clean test setup and composability.
- Powerful plugin ecosystem (coverage, benchmark, hypothesis).
- Easy to scale from unit tests to integration tests and CI.

---

## Test-suite features demonstrated

| Test file | Feature(s) demonstrated |
|---|---|
| `tests/test_basic.py` | Simple assertions, parametrized tests, basic math correctness |
| `tests/test_param.py` | Module/function fixtures, factory fixtures, grouping tests |
| `tests/test_errors.py` | Exception testing (`pytest.raises`), `tmp_path`, `monkeypatch`, `unittest.mock` |
| `tests/test_property.py` | Property-based testing with Hypothesis (invariants) |
| `tests/test_benchmark.py` | pytest-benchmark usage; how to mark and run benchmarks |
| `conftest.py` | Shared fixtures, custom marker registration, session-scoped reproducible seed |
| `diagrams/architecture.mmd` | Mermaid diagram of test <-> library relationships |

---

## Installation (recommended virtualenv workflow)

```bash
# create virtualenv and activate
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Install project (you can use pip or poetry)
pip install -r requirements.txt

