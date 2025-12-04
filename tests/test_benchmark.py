"""
Benchmarking with pytest-benchmark.

Demonstrates:
- using benchmark fixture to time functions
- marking benchmark tests so they can be selected/deselected
"""

import pytest
from vector_math.math import normalize, batch_normalize

@pytest.mark.benchmark
def test_normalize_benchmark(benchmark):
    v = [i + 1.0 for i in range(100)]
    # benchmark will execute normalize several times and produce stats
    result = benchmark(normalize, v)
    assert round(sum(x * x for x in result), 10) == pytest.approx(1.0, rel=1e-9)


@pytest.mark.benchmark
def test_batch_normalize_benchmark(benchmark):
    # Create many 100-length vectors for batch normalization
    data = [[i + 1.0 for i in range(100)] for _ in range(100)]
    # benchmark may require numpy; skip if numpy not present to keep CI deterministic
    try:
        import numpy  # type: ignore
    except Exception:
        pytest.skip("numpy not available; skipping SIMD benchmark")
    result = benchmark(batch_normalize, data)
    assert isinstance(result, list)

