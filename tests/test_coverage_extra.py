"""
Extra tests to exercise code paths in vector_math.math that weren't covered.

These exercises:
- private helper _to_list
- length-mismatch errors for add() and dot()
- batch_normalize: numpy path, mismatched lengths, and zero-vector error
"""

import pytest
from vector_math import math as vmath

def test__to_list_helper():
    # internal helper — small smoke test
    assert vmath._to_list((1, 2, 3)) == [1, 2, 3]
    assert vmath._to_list([4.0, 5.0]) == [4.0, 5.0]


def test_add_length_mismatch():
    with pytest.raises(ValueError):
        vmath.add([1, 2], [1])  # differing lengths should raise


def test_dot_length_mismatch():
    with pytest.raises(ValueError):
        vmath.dot([1, 2, 3], [1, 2])


def test_batch_normalize_mismatched_lengths():
    # mismatched inner lengths should raise
    with pytest.raises(ValueError):
        vmath.batch_normalize([[1.0, 2.0], [1.0]])


def test_batch_normalize_zero_vector_error():
    # if any vector is zero-length, batch_normalize must raise
    try:
        import numpy  # type: ignore
        has_numpy = True
    except Exception:
        has_numpy = False

    if has_numpy:
        with pytest.raises(ValueError):
            vmath.batch_normalize([[0.0, 0.0], [1.0, 0.0]])
    else:
        # If numpy is not present, we still get a single-vector zero-length error via normalize()
        with pytest.raises(ValueError):
            vmath.batch_normalize([[0.0, 0.0]])


def test_batch_normalize_numpy_path():
    # only meaningful when numpy is present; ensures the numpy-optimized branch runs
    try:
        import numpy  # type: ignore
    except Exception:
        pytest.skip("numpy not available; skipping numpy-path test")
    data = [[3.0, 4.0], [6.0, 8.0]]
    res = vmath.batch_normalize(data)
    # result should be unit vectors
    for vec in res:
        # length approx 1.0
        assert pytest.approx(1.0, rel=1e-9) == (sum(x * x for x in vec) ** 0.5)

