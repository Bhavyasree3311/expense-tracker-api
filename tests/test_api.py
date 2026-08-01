from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Smart Expense Tracker API"
    }

def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "id": 100,
            "title": "Book",
            "amount": 500,
            "category": "Education",
            "date": "2026-08-01"
        }
    )

    assert response.status_code == 200

def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200

def test_delete_expense():
    response = client.delete("/expenses/100")
    assert response.status_code == 200