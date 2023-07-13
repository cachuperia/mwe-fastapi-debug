"""Package-wide test fixtures and hooks."""

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(name="client")
def fixture_client() -> TestClient:
    """FastAPI test client."""
    from mwe_fastapi_debug.main import app

    return TestClient(app)
