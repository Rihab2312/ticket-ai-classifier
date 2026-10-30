import pytest

from ticket_ai.api import create_app


@pytest.fixture(scope="module")
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_predict_ok(client):
    response = client.post("/predict", json={"text": "La facture contient une erreur de TVA"})
    assert response.status_code == 200
    assert response.get_json()["category"] == "facturation"


def test_predict_missing_text(client):
    response = client.post("/predict", json={})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_predict_invalid_json(client):
    response = client.post("/predict", data="pas du json", content_type="text/plain")
    assert response.status_code == 400
