import unittest
from app import app

class TestRoutes(unittest.TestCase):
    """Tests for Flask application routes"""

    def setUp(self):
        # Create a test client for the Flask app
        self.client = app.test_client()

    def test_home_invalid_method(self):
        """Test that the home route returns a 405 for invalid methods"""
        response = self.client.post('/')  # Invalid method (POST)
        self.assertEqual(response.status_code, 405)  # Expecting Method Not Allowed (405)


if __name__ == '__main__':
    unittest.main()
