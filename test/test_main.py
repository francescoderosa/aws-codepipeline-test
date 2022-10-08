import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.mark.parametrize("name", [None,"Francesco", "Lorenzo"])
def test_hello(name):
    response = client.get(f"/{name}")
    assert response.status_code == 200