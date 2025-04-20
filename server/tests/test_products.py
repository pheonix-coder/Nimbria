from fastapi import status
from fastapi.testclient import TestClient
from app import schemas

def test_create_product(test_db, client: TestClient):
    product = schemas.ProductCreate(name="Test Product", description="A test product", price=99.99)
    response = client.post("/products/", json=product.dict())
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == product.name
    assert response.json()["description"] == product.description
    assert response.json()["price"] == product.price

def test_read_product(test_db, client: TestClient):
    product = schemas.ProductCreate(name="Test Product", description="A test product", price=99.99)
    response = client.post("/products/", json=product.dict())
    product_id = response.json()["id"]
    response = client.get(f"/products/{product_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == product.name
    assert response.json()["description"] == product.description
    assert response.json()["price"] == product.price

def test_read_products(test_db, client: TestClient):
    product1 = schemas.ProductCreate(name="Test Product 1", description="A test product", price=99.99)
    product2 = schemas.ProductCreate(name="Test Product 2", description="A test product", price=199.99)
    client.post("/products/", json=product1.dict())
    client.post("/products/", json=product2.dict())
    response = client.get("/products/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2
