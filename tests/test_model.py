from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Diabetes Prediction API"}

def test_predict_endpoint():
    sample_input = {
        "age": 0.038,
        "sex": 0.05,
        "bmi": 0.06,
        "bp": 0.03,
        "s1": 0.02,
        "s2": -0.02,
        "s3": -0.002,
        "s4": 0.003,
        "s5": 0.02,
        "s6": 0.004
    }
    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    json_data = response.json()
    assert "prediction" in json_data
    assert isinstance(json_data["prediction"], float)

