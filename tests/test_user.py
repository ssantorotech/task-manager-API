import itertools
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import database

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset():
    database.USERS_DB.clear()
    database.USERS_ID = itertools.count(1)
    yield
    app.dependency_overrides.clear()


# USER TEST
def test_add_user():
    response = client.post(
        "/users",
        json={'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
    )
    assert response.status_code == 201

    data = response.json()

    assert data['username'] == 'testuser'
    assert data['email'] == 'testuser@example.com'
    assert data['id'] is not None

    print(data)


def test_get_user():
    client.post(
        "/users",
        json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
    )

    response = client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data['username'] == 'testuser'
    assert data['email'] == 'testuser@example.com'
    assert data['id'] == 1

    print(data)


def test_user_inesistente():
    response = client.get("/users/9999")
    assert response.status_code == 404
    assert response.json()['detail'] == 'Not Found'



@pytest.mark.parametrize("payload", [
    {'username': '', 'email': 'testuser@example.com', 'password': 'testpassword'},
    {'username': 'testuser', 'email': '', 'password': 'testpassword'},
    {'username': 'testuser', 'email': 'testuser@example.com', 'password': ''}
])

def test_user_non_valido(payload):
    response = client.post("/users", json=payload)
    assert response.status_code == 422