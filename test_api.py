import unittest
from mod_service import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login(self):
        response = self.app.post('/login', json={"username": "admin", "password": "password"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.get_json())

    def test_create_user(self):
        token = self.app.post('/login', json={"username": "admin", "password": "password"}).get_json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        response = self.app.post('/users', json={"name": "Test", "email": "test@example.com"}, headers=headers)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
