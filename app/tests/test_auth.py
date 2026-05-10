from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login():
    response = client.post(
        "/api/v1/auth/telegram",
        json={
            "telegram_id": 123456,
            "username": "test_user"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data