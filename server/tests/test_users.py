from fastapi import status
from fastapi.testclient import TestClient
from app import schemas

def test_register_user(test_db, client):
    user = schemas.UserCreate(username="testuser", email="test@example.com", password="password")
    response = client.post("/users/register", json=user.model_dump())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == user.username
    assert response.json()["email"] == user.email

def test_login_user(test_db, client):
    user = schemas.UserCreate(username="testuser", email="test@example.com", password="password")
    client.post("/users/register", json=user.model_dump())
    form_data = {"username": "testuser", "password": "password"}
    response = client.post("/users/login", data=form_data)
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
