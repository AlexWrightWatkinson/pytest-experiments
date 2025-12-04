"""
Essentials: simple assertion tests, parametrized examples.

Notes:
- Use immutable tuples for parametrized inputs to avoid accidental mutation
  across parameter cases (pytest constructs those parameter values once at import time).
- Convert to lists when calling functions that expect mutable sequences if needed.
"""

import math
import pytest
from vector_math.math import add, dot, scalar_multiply, normalize


def test_add_simple():
    assert add([1, 2], [3, 4]) == [4, 6]


@pytest.mark.parametrize(
    "a,b,expected",
    [
        # use tuples here to avoid accidental in-place mutation by other tests
        ((0, 0), (0, 0), [0, 0]),
        ((1, -1), (-1, 1), [0, 0]),
        ((2.5, 0), (0.5, 1), [3.0, 1.0]),
    ],
)
def test_add_parametrized(a, b, expected):
    """Parametrized test—avoid duplication and exercise multiple cases.
    Convert tuple inputs to lists before passing to functions that may expect list.
    """
    # Defensive copy: convert to list so the implementation can work with sequences.
    assert add(list(a), list(b)) == expected


def test_dot_and_scalar():
    a = [1, 2, 3]
    b = [4, 0, -1]
    assert dot(a, b) == 1 * 4 + 2 * 0 + 3 * -1
    assert scalar_multiply(2, a) == [2, 4, 6]


def test_normalize_unit_vector():
    v = [3.0, 4.0]
    u = normalize(v)
    # length should be 1 (allow small floating error)
    assert pytest.approx(1.0, rel=1e-9) == math.sqrt(sum(x * x for x in u))

