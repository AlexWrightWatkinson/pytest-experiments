"""
Simple vector math implementation.

- add: vector addition
- dot: dot product
- scalar_multiply: multiply vector by scalar
- normalize: return unit vector (raises ValueError on zero vector)
- batch_normalize: optional SIMD-style batch normalize using NumPy if available

This implementation uses plain Python lists/tuples for simple ops and NumPy
for the batch operation. The code is intentionally small and well-typed.
"""

from typing import Iterable, List, Sequence
import math

try:
    import numpy as _np  # optional dependency used in batch_normalize
except Exception:  # pragma: no cover - environment may or may not have numpy in tests
    _np = None  # type: ignore

Vector = Sequence[float]


def _to_list(v: Iterable[float]) -> List[float]:
    return list(v)


def add(a: Vector, b: Vector) -> List[float]:
    """Return element-wise sum of two vectors of same length."""
    if len(a) != len(b):
        raise ValueError("vectors must be the same length")
    return [x + y for x, y in zip(a, b)]


def dot(a: Vector, b: Vector) -> float:
    """Return dot product of two vectors of same length."""
    if len(a) != len(b):
        raise ValueError("vectors must be the same length")
    return sum(x * y for x, y in zip(a, b))


def scalar_multiply(scalar: float, v: Vector) -> List[float]:
    """Return vector multiplied by scalar."""
    return [scalar * x for x in v]


def normalize(v: Vector) -> List[float]:
    """Return unit vector for v. Raise ValueError for zero vector."""
    l2 = math.sqrt(sum(x * x for x in v))
    if l2 == 0:
        raise ValueError("cannot normalize zero-length vector")
    return [x / l2 for x in v]


def batch_normalize(vs: Iterable[Vector]) -> List[List[float]]:
    """
    SIMD-style batch normalization using NumPy if available.
    Accepts an iterable of vectors (same length). Falls back to Python loop if
    NumPy is not present.
    """
    vs_list = [list(v) for v in vs]
    if not vs_list:
        return []
    n_cols = len(vs_list[0])
    if any(len(row) != n_cols for row in vs_list):
        raise ValueError("all vectors must have the same length")
    if _np is None:
        # Fallback: sequential normalization
        return [normalize(row) for row in vs_list]
    arr = _np.array(vs_list, dtype=float)
    norms = _np.linalg.norm(arr, axis=1)
    if _np.any(norms == 0):
        raise ValueError("cannot normalize zero-length vector in batch")
    return (arr / norms[:, None]).tolist()

