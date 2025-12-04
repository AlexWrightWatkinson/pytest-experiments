"""
Exception testing, tmp_path usage, monkeypatching, and mocking examples.

Demonstrates:
- pytest.raises for exception testing
- tmp_path to create temporary files/directories
- monkeypatch to temporarily change behavior/environment
- unittest.mock for mocking objects

Note: fixed mocking test so that patch targets module attribute and the
call goes through the patched name (previously it called an already-imported
symbol and the mock saw zero calls).
"""

import json
import os
from unittest import mock

import pytest
from vector_math.math import normalize, batch_normalize, add as add_func


def test_normalize_zero_raises():
    with pytest.raises(ValueError) as exc:
        normalize([0.0, 0.0, 0.0])
    assert "cannot normalize" in str(exc.value)


def test_tmp_path_file(tmp_path):
    # tmp_path: function-scoped temporary directory (pathlib.Path)
    p = tmp_path / "data.json"
    data = {"vectors": [[3.0, 4.0]]}
    p.write_text(json.dumps(data))
    # Read and normalize stored vector
    loaded = json.loads(p.read_text())
    v = loaded["vectors"][0]
    assert pytest.approx(1.0) == (sum(x * x for x in normalize(v)) ** 0.5)


def test_batch_normalize_monkeypatch(monkeypatch):
    # Demonstrate monkeypatching: temporarily replace numpy to force fallback.
    import sys
    monkeypatch.setitem(sys.modules, "numpy", None)
    # Import function again to use current numpy resolution
    from importlib import reload
    import vector_math.math as vmath_module
    reload(vmath_module)
    # Should use fallback path (no exception for normal vectors)
    assert vmath_module.batch_normalize([[3.0, 4.0], [6.0, 8.0]])[0][0] == pytest.approx(0.6)


def test_mocking_add():
    """
    Patch the add function on the module and call the attribute from the module
    so the patched function is invoked. Previous version patched but called the
    already-imported symbol 'add', so the mock recorded 0 calls.
    """
    import vector_math.math as vmath  # import module, so we can patch module attribute
    with mock.patch("vector_math.math.add", wraps=vmath.add) as mocked:
        # call via module attribute so mock intercepts the call
        res = vmath.add([1, 2], [3, 4])
        mocked.assert_called_once()
        assert res == [4, 6]

