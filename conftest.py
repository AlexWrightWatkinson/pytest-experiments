"""
Project-level test configuration and shared fixtures.

Demonstrates:
- custom fixtures at session scope
- registering custom markers dynamically (helpful for CI/test selection)
- example of a fixture that can be used by many tests
"""

import pytest
import random

def pytest_configure(config):
    # Registering markers so pytest --strict-markers doesn't complain
    config.addinivalue_line("markers", "slow: marks tests as slow")
    config.addinivalue_line("markers", "integration: marks integration tests")


@pytest.fixture(scope="session")
def seed_random():
    """Session-scoped fixture to fix randomness for reproducibility (if needed)."""
    seed = 42
    random.seed(seed)
    return seed


@pytest.fixture(scope="function")
def small_vector():
    """Function-scoped fixture returning a small, known test vector."""
    return [3.0, 4.0]


@pytest.fixture
def tmp_config(tmp_path):
    """Example fixture that creates a temporary config file for tests."""
    p = tmp_path / "config.json"
    p.write_text('{"mode": "test"}')
    return p

