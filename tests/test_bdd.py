import pytest
from app import create_app, db
from app.models import Furniture

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        db.create_all()
    yield client
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_add_furniture(client):
    response = client.post('/furniture', json={
        'name': 'Chair',
        'description': 'A comfortable chair',
        'quantity': 5,
        'location': 'Aisle 3'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Chair'

def test_get_furniture(client):
    response = client.get('/furniture')
    assert response.status_code == 200

def test_update_furniture(client):
    response = client.post('/furniture', json={
        'name': 'Chair',
        'description': 'A comfortable chair',
        'quantity': 5,
        'location': 'Aisle 3'
    })
    furniture_id = response.get_json()['id']
    response = client.put(f'/furniture/{furniture_id}', json={
        'name': 'Updated Chair',
        'description': 'A very comfortable chair'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Updated Chair'

def test_delete_furniture(client):
    response = client.post('/furniture', json={
        'name': 'Chair',
        'description': 'A comfortable chair',
        'quantity': 5,
        'location': 'Aisle 3'
    })
    furniture_id = response.get_json()['id']
    response = client.delete(f'/furniture/{furniture_id}')
    assert response.status_code == 204