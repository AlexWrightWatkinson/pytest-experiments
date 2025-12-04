"""
Intermediate: fixtures (module & function), factory-based test parameter generation.

Demonstrates:
- using fixtures with different scopes
- a simple "factory" fixture that creates random vectors
- grouping related tests
"""

import random
import math
import pytest
from vector_math import math as vmath


@pytest.fixture(scope="module")
def module_vectors():
    # module-scoped fixture: constructed once per module
    return [[1.0, 0.0], [0.0, 1.0], [3.0, 4.0]]


@pytest.fixture
def rnd_vector_factory():
    """A small factory fixture returning callables to produce random vectors.

    Factories are a flexible way to provide parameter generation for tests.
    """
    def factory(length=3, scale=10.0):
        return [random.random() * scale for _ in range(length)]
    return factory


def test_module_vectors_normalize(module_vectors):
    for v in module_vectors:
        u = vmath.normalize(v)
        assert pytest.approx(1.0, rel=1e-9) == math.sqrt(sum(x * x for x in u))


def test_random_vectors_with_factory(rnd_vector_factory):
    v = rnd_vector_factory(length=4, scale=1.0)
    # ensure factory returns correct length and that normalize works
    assert len(v) == 4
    u = vmath.normalize(v)
    assert pytest.approx(1.0, rel=1e-9) == math.sqrt(sum(x * x for x in u))

