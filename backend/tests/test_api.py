from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_execute() -> None:
    response = client.post(
        "/api/execute",
        json={"goal": "Research top AI startups in healthcare and create a report"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["goal"].startswith("Research top AI startups")
    assert "final_report" in payload
