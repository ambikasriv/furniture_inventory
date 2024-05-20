import unittest
from app import create_app, db
from app.models import Furniture

class CRUDTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_furniture(self):
        response = self.client.post('/furniture', json={
            'name': 'Chair',
            'description': 'A comfortable chair',
            'quantity': 5,
            'location': 'Aisle 3'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'Chair')

    def test_get_furniture(self):
        response = self.client.get('/furniture')
        self.assertEqual(response.status_code, 200)

    def test_update_furniture(self):
        response = self.client.post('/furniture', json={
            'name': 'Chair',
            'description': 'A comfortable chair',
            'quantity': 5,
            'location': 'Aisle 3'
        })
        furniture_id = response.get_json()['id']
        response = self.client.put(f'/furniture/{furniture_id}', json={
            'name': 'Updated Chair',
            'description': 'A very comfortable chair'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Updated Chair')

    def test_delete_furniture(self):
        response = self.client.post('/furniture', json={
            'name': 'Chair',
            'description': 'A comfortable chair',
            'quantity': 5,
            'location': 'Aisle 3'
        })
        furniture_id = response.get_json()['id']
        response = self.client.delete(f'/furniture/{furniture_id}')
        self.assertEqual(response.status_code, 204)

if _name_ == '_main_':
    unittest.main()