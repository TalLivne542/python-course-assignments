import pytest
from fastapi.testclient import TestClient
from core.polymer_logic import calculate_crystallinity
from app import app

# Create FastAPI TestClient for integration tests
client = TestClient(app)

# ----------------- 1. Business Logic Tests (Day 04 Core) -----------------

def test_polymer_logic_success():
    # Verify correct calculation for PLA (93.0 J/g) with 0% moisture
    result = calculate_crystallinity("PLA", 46.5, 0.0)
    assert result == 50.0  # 46.5 / 93.0 * 100 = 50%

def test_polymer_logic_invalid_name_raises_error():
    # Verify that an unregistered polymer name triggers a ValueError
    with pytest.raises(ValueError):
        calculate_crystallinity("UnknownPolymer", 50.0)

# ----------------- 2. Web Application Tests (Day 08 API) -----------------

def test_web_home_route():
    # Test GET request to root endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_web_calculate_success():
    # Test valid POST request to /calculate endpoint
    payload = {
        "polymer_name": "PLA",
        "delta_hm_measured": 46.5,
        "moisture_content": 0.0
    }
    response = client.post("/calculate", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["crystallinity_percentage"] == 50.0

def test_web_calculate_invalid_polymer_returns_400():
    # Test that invalid input via web API returns a 400 Bad Request status code
    payload = {
        "polymer_name": "InvalidPolymer",
        "delta_hm_measured": 50.0
    }
    response = client.post("/calculate", json=payload)
    assert response.status_code == 400
    assert "not found" in response.json()["detail"]
