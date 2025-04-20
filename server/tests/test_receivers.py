from fastapi import status
from fastapi.testclient import TestClient
from app import schemas
import pytest

@pytest.fixture
def create_user(client: TestClient):
    user = schemas.UserCreate(username="testuser", email="test@example.com", password="password")
    response = client.post("/users/register", json=user.dict())
    assert response.status_code == status.HTTP_200_OK
    return response.json()

@pytest.fixture
def get_access_token(client: TestClient, create_user):
    form_data = {"username": "testuser", "password": "password"}
    response = client.post("/users/login", data=form_data)
    assert response.status_code == status.HTTP_200_OK
    return response.json()["access_token"]

def test_create_receiver(test_db, client: TestClient, get_access_token):
    receiver = schemas.ReceiverCreate(name="Test Receiver", mobile="123-456-7890", address="123 Test St")
    headers = {"Authorization": f"Bearer {get_access_token}"}
    response = client.post("/receivers/", json=receiver.dict(), headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == receiver.name
    assert response.json()["mobile"] == receiver.mobile
    assert response.json()["address"] == receiver.address

def test_read_receivers(test_db, client: TestClient, get_access_token):
    receiver1 = schemas.ReceiverCreate(name="Test Receiver 1", mobile="123-456-7890", address="123 Test St")
    receiver2 = schemas.ReceiverCreate(name="Test Receiver 2", mobile="098-765-4321", address="456 Test Ave")
    headers = {"Authorization": f"Bearer {get_access_token}"}
    client.post("/receivers/", json=receiver1.dict(), headers=headers)
    client.post("/receivers/", json=receiver2.dict(), headers=headers)
    response = client.get("/receivers/", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2
