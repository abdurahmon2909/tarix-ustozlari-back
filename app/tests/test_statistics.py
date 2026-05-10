from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_statistics():
    response = client.get(
        "/api/v1/statistics/1"
    )

    assert response.status_code == 200