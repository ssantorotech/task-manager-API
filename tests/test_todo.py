import itertools
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import database


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset():
    database.TODOS_DB.clear()
    database.ID = itertools.count(1)
    yield
    app.dependency_overrides.clear()



# TODO Test


def test_add_todo():
    response = client.post(
        "/todos", 
        json = {'title': 'Test Todo', 'description': 'This is a test todo', 'priorita': 'media'}
    )
    assert response.status_code == 201

    data = response.json()

    assert data['title'] == 'Test Todo'
    assert data['description'] == 'This is a test todo'
    assert data['priorita'] == 'media'
    assert data['completed'] is False
    assert data['id'] is not None

    print(data)



def test_todo_inesistente():
    response = client.get("/todos/9999")
    assert response.status_code == 404
    assert response.json()['detail'] == 'Todo not found'


@pytest.mark.parametrize("payload", [
    {},
    {'title': '', 'description': 'This is a test todo'},
    {'title': 'Test Todo', 'description': ''},
])

def test_payload_non_valido(payload):
    assert client.post("/todos", json=payload).status_code == 422

