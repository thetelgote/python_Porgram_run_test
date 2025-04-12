# tests/test_app.py

import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
