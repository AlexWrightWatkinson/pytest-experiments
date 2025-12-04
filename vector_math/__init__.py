"""
vector_math package

Small, clear vector math utilities intended for demonstration
and testing with pytest.
"""

from .math import add, dot, scalar_multiply, normalize, batch_normalize  # re-export

__all__ = ["add", "dot", "scalar_multiply", "normalize", "batch_normalize"]

