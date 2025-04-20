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

@pytest.fixture
def create_product(client: TestClient, get_access_token):
    product = schemas.ProductCreate(name="Test Product", description="A test product", price=99.99)
    headers = {"Authorization": f"Bearer {get_access_token}"}
    response = client.post("/products/", json=product.dict(), headers=headers)
    assert response.status_code == status.HTTP_200_OK
    return response.json()

def test_create_order(test_db, client: TestClient, get_access_token, create_product):
    order = schemas.OrderCreate(product_id=create_product["id"], quantity=1)
    headers = {"Authorization": f"Bearer {get_access_token}"}
    response = client.post("/orders/", json=order.dict(), headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["product_id"] == order.product_id
    assert response.json()["quantity"] == order.quantity

def test_read_orders(test_db, client: TestClient, get_access_token, create_product):
    order1 = schemas.OrderCreate(product_id=create_product["id"], quantity=1)
    order2 = schemas.OrderCreate(product_id=create_product["id"], quantity=2)
    headers = {"Authorization": f"Bearer {get_access_token}"}
    client.post("/orders/", json=order1.dict(), headers=headers)
    client.post("/orders/", json=order2.dict(), headers=headers)
    response = client.get("/orders/", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2
