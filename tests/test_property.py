"""
Property-based testing using Hypothesis.

Demonstrates:
- writing property tests that assert invariants hold over wide input space
- integration of hypothesis with pytest
"""

from hypothesis import given, strategies as st
import math
import pytest
from vector_math.math import dot, scalar_multiply

# Strategy for non-empty lists of floats (avoids zero-length vector pitfalls)
vectors = st.lists(st.floats(min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False),
                   min_size=1, max_size=10)


@given(v=vectors, w=vectors)
def test_dot_commutative(v, w):
    # Only test when lengths match
    if len(v) != len(w):
        pytest.skip("Hypothesis generated differing lengths; skipping")
    assert dot(v, w) == dot(w, v)


@given(v=vectors, scalar=st.floats(min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False))
def test_scalar_distributive_over_add(v, scalar):
    # property: scalar*(v+w) == scalar*v + scalar*w
    w = [x + 1.0 for x in v]  # produce same-length w
    left = scalar_multiply(scalar, [a + b for a, b in zip(v, w)])
    right = [a + b for a, b in zip(scalar_multiply(scalar, v), scalar_multiply(scalar, w))]
    assert left == pytest.approx(right)

